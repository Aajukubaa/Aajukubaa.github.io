// Live Chess.com dashboard for the Chess domain card.
// Loaded on every page view, but does nothing (and loads no external
// libraries) until the chess card is actually opened — see the
// window.initChessDashboard hook called from main.js's openCategory().
//
// Data comes from chess-data.json (same origin, refreshed periodically
// by .github/workflows/build.yml running fetch_chess_data.py), NOT
// directly from api.chess.com — Chess.com's public API does not
// reliably support CORS for browser fetch(), which is why the
// dashboard previously always failed to load.

(function () {
    "use strict";

    var CHESS_USERNAME = "Aajukubaa"; // hardcoded per request

    // ---------- Lazy-load jQuery + chess.js + chessboard.js ----------
    var chessLibsPromise = null;

    function loadScript(src) {
        return new Promise(function (resolve, reject) {
            var el = document.createElement("script");
            el.src = src;
            el.onload = resolve;
            el.onerror = function () { reject(new Error("Failed to load " + src)); };
            document.head.appendChild(el);
        });
    }
    function loadStylesheet(href) {
        if (document.querySelector('link[href="' + href + '"]')) return;
        var link = document.createElement("link");
        link.rel = "stylesheet";
        link.href = href;
        document.head.appendChild(link);
    }
    function ensureChessLibs() {
        if (chessLibsPromise) return chessLibsPromise;
        loadStylesheet("https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/chessboard-1.0.0.min.css");
        chessLibsPromise = loadScript("https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js")
            .then(function () {
                return Promise.all([
                    // NOTE: cdnjs's chess.js@0.13.4 build ships an ES module
                    // (uses `export`), which throws "Unexpected token export"
                    // when loaded via a plain <script> tag — that was the
                    // dashboard's actual bug. 0.12.0 is confirmed to be a
                    // plain browser-global script (window.Chess), same API.
                    loadScript("https://unpkg.com/chess.js@0.12.0/chess.js"),
                    loadScript("https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/chessboard-1.0.0.min.js"),
                ]);
            });
        return chessLibsPromise;
    }

    // ---------- Data (same-origin static JSON, not a live API call) ----------
    var dataPromise = null;
    function loadChessData() {
        if (!dataPromise) {
            dataPromise = fetch("chess-data.json?_=" + Date.now())
                .then(function (res) {
                    if (!res.ok) throw new Error("chess-data.json missing");
                    return res.json();
                });
        }
        return dataPromise;
    }

    var RATING_TYPES = [
        { key: "chess_bullet", label: "Bullet", icon: "⚡" },
        { key: "chess_blitz", label: "Blitz", icon: "🔥" },
        { key: "chess_rapid", label: "Rapid", icon: "♟" },
    ];

    function renderStats(container, stats) {
        container.innerHTML = RATING_TYPES.map(function (t) {
            var s = stats ? stats[t.key] : null;
            if (!s || !s.last) {
                return '<div class="chess-stat-card"><span class="chess-stat-icon">' + t.icon + '</span>' +
                    '<h4>' + t.label + '</h4><p class="chess-stat-rating">—</p>' +
                    '<p class="chess-stat-record">No rated games yet</p></div>';
            }
            var rec = s.record || { win: 0, loss: 0, draw: 0 };
            return '<div class="chess-stat-card"><span class="chess-stat-icon">' + t.icon + '</span>' +
                '<h4>' + t.label + '</h4>' +
                '<p class="chess-stat-rating">' + s.last.rating + '</p>' +
                '<p class="chess-stat-record">' + rec.win + 'W · ' + rec.loss + 'L · ' + rec.draw + 'D</p></div>';
        }).join("");
    }

    function errorHTML(what) {
        return '<p class="chess-dashboard-error">Couldn\u2019t load ' + what + ' right now — try refreshing, or see the profile directly on ' +
            '<a href="https://www.chess.com/member/' + CHESS_USERNAME + '" target="_blank">Chess.com</a>.</p>';
    }
    function debugHTML(detail) {
        if (!detail) return "";
        return '<p class="chess-dashboard-debug">(' + String(detail).slice(0, 200) + ')</p>';
    }

    var DRAW_RESULTS = ["agreed", "repetition", "stalemate", "insufficient", "50move", "timevsinsufficient"];
    function outcomeFor(result) {
        if (result === "win") return "win";
        if (DRAW_RESULTS.indexOf(result) !== -1) return "draw";
        return "loss";
    }

    // ---------- Board + move stepping ----------
    var boardInstance = null;
    var currentHistory = [];
    var currentIndex = 0;

    function renderPositionAt(index) {
        var replay = new window.Chess();
        for (var i = 0; i < index; i++) replay.move(currentHistory[i].san);
        if (boardInstance) boardInstance.position(replay.fen());

        var indicator = document.getElementById("chess-move-indicator");
        var prevBtn = document.getElementById("chess-prev-move");
        var nextBtn = document.getElementById("chess-next-move");
        if (indicator) {
            indicator.textContent = currentHistory.length ? "Move " + index + " / " + currentHistory.length : "No moves recorded";
        }
        if (prevBtn) prevBtn.disabled = index <= 0;
        if (nextBtn) nextBtn.disabled = index >= currentHistory.length;
    }

    // Piece images for chessboard.js were never actually published to npm
    // (only bundled in the project's manual ZIP download), so ANY CDN
    // pointing at the npm/unpkg/cdnjs package 404s on piece images —
    // that was the "pieces don't show up" bug. Rendering them as inline
    // SVG data URIs instead removes that external dependency entirely.
    var PIECE_GLYPH = {
        wK: "♔", wQ: "♕", wR: "♖", wB: "♗", wN: "♘", wP: "♙",
        bK: "♚", bQ: "♛", bR: "♜", bB: "♝", bN: "♞", bP: "♟",
    };
    var pieceThemeCache = {};
    function pieceTheme(piece) {
        if (pieceThemeCache[piece]) return pieceThemeCache[piece];
        var isWhite = piece.charAt(0) === "w";
        var glyph = PIECE_GLYPH[piece];
        var svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 45 45">' +
            '<text x="50%" y="54%" dominant-baseline="middle" text-anchor="middle" ' +
            'font-size="38" font-family="Georgia, \'Times New Roman\', serif" ' +
            'fill="' + (isWhite ? "#f5f5f0" : "#1a1a1a") + '" ' +
            'stroke="' + (isWhite ? "#1a1a1a" : "#f5f5f0") + '" stroke-width="1">' +
            glyph + "</text></svg>";
        var dataUri = "data:image/svg+xml;base64," + btoa(svg);
        pieceThemeCache[piece] = dataUri;
        return dataUri;
    }

    function selectGame(game) {
        var chess = new window.Chess();
        var loaded = false;
        try { loaded = chess.load_pgn(game.pgn, { sloppy: true }); } catch (e) { loaded = false; }
        currentHistory = loaded ? chess.history({ verbose: true }) : [];
        currentIndex = currentHistory.length;

        var boardEl = document.getElementById("chesscom-board");
        if (!boardInstance && boardEl && window.Chessboard) {
            boardInstance = window.Chessboard(boardEl.id, {
                position: "start",
                pieceTheme: pieceTheme,
            });
            if (window.jQuery) {
                window.jQuery(window).on("resize", function () { if (boardInstance) boardInstance.resize(); });
            }
        }
        renderPositionAt(currentIndex);
        // Defensive: if the container's layout wasn't fully settled at
        // construction time (mid-modal-transition), this catches it.
        if (boardInstance) {
            setTimeout(function () { boardInstance.resize(); }, 50);
            setTimeout(function () { boardInstance.resize(); }, 300);
        }
    }

    function renderGamesList(listEl, games) {
        listEl.innerHTML = "";
        games.forEach(function (game, i) {
            var isWhite = game.white.username.toLowerCase() === CHESS_USERNAME.toLowerCase();
            var me = isWhite ? game.white : game.black;
            var opponent = isWhite ? game.black : game.white;
            var outcome = outcomeFor(me.result);

            var row = document.createElement("button");
            row.type = "button";
            row.className = "chess-game-row" + (i === 0 ? " active" : "");
            row.innerHTML =
                '<span class="chess-game-outcome outcome-' + outcome + '">' + outcome.charAt(0).toUpperCase() + "</span>" +
                '<span class="chess-game-info">' +
                '<span class="chess-game-opponent">vs ' + opponent.username + '</span>' +
                '<span class="chess-game-meta">' + opponent.rating + ' rated · ' + game.time_class + '</span>' +
                '</span>';
            row.addEventListener("click", function () {
                listEl.querySelectorAll(".chess-game-row").forEach(function (r) { r.classList.remove("active"); });
                row.classList.add("active");
                selectGame(game);
            });
            listEl.appendChild(row);
        });
    }

    document.addEventListener("click", function (e) {
        if (e.target && e.target.id === "chess-prev-move" && currentIndex > 0) {
            currentIndex--; renderPositionAt(currentIndex);
        }
        if (e.target && e.target.id === "chess-next-move" && currentIndex < currentHistory.length) {
            currentIndex++; renderPositionAt(currentIndex);
        }
    });

    // ---------- Fullscreen board ----------
    function hapticTick(duration) {
        if (navigator.vibrate) {
            try { navigator.vibrate(duration || 10); } catch (e) { /* ignore */ }
        }
    }

    function closeChessBoardFullscreen() {
        var panel = document.querySelector(".chess-board-panel.board-fullscreen");
        if (!panel) return false;
        hapticTick();
        panel.classList.remove("board-fullscreen");
        if (boardInstance) setTimeout(function () { boardInstance.resize(); }, 50);
        return true;
    }
    window.closeChessBoardFullscreen = closeChessBoardFullscreen;

    document.addEventListener("click", function (e) {
        var boardEl = e.target.closest && e.target.closest("#chesscom-board");
        if (boardEl) {
            var panel = boardEl.closest(".chess-board-panel");
            if (panel && !panel.classList.contains("board-fullscreen")) {
                hapticTick();
                panel.classList.add("board-fullscreen");
                if (boardInstance) setTimeout(function () { boardInstance.resize(); }, 50);
            }
            return;
        }
        var closeBtn = e.target.closest && e.target.closest(".chess-board-fullscreen-close");
        if (closeBtn) { closeChessBoardFullscreen(); return; }
        // Click on the fullscreen backdrop itself (not the board/controls) closes it.
        if (e.target.classList && e.target.classList.contains("board-fullscreen")) {
            closeChessBoardFullscreen();
        }
    });

    // ---------- Entry point ----------
    function initChessDashboard() {
        var statsEl = document.getElementById("chesscom-stats");
        var gamesListEl = document.getElementById("chesscom-games-list");
        var updatedEl = document.getElementById("chesscom-updated");
        if (!statsEl || !gamesListEl) return; // chess card isn't open

        statsEl.innerHTML = '<p class="chess-dashboard-loading">Loading live ratings…</p>';
        gamesListEl.innerHTML = '<p class="chess-dashboard-loading">Loading recent games…</p>';

        var libsPromise = ensureChessLibs().catch(function (e) {
            throw new Error("chess libraries failed to load (" + (e && e.message ? e.message : e) + ")");
        });
        var dataPromise = loadChessData().catch(function (e) {
            throw new Error("chess-data.json failed to load (" + (e && e.message ? e.message : e) + ")");
        });

        Promise.all([libsPromise, dataPromise])
            .then(function (results) {
                var data = results[1];

                if (data.stats) {
                    renderStats(statsEl, data.stats);
                } else {
                    statsEl.innerHTML = errorHTML("live ratings") + debugHTML(data.error);
                }

                if (updatedEl && data.fetched_at) {
                    var d = new Date(data.fetched_at);
                    updatedEl.textContent = "Updated " + d.toLocaleString(undefined, {
                        month: "short", day: "numeric", hour: "numeric", minute: "2-digit",
                    });
                }

                var games = data.recent_games || [];
                if (!games.length) {
                    gamesListEl.innerHTML = data.stats ? '<p class="chess-dashboard-error">No recent games found.</p>' : errorHTML("recent games") + debugHTML(data.error);
                    return;
                }
                renderGamesList(gamesListEl, games);
                selectGame(games[0]);
            })
            .catch(function (err) {
                var msg = err && err.message ? err.message : String(err);
                console.error("Chess dashboard failed:", err);
                statsEl.innerHTML = errorHTML("live ratings") + debugHTML(msg);
                gamesListEl.innerHTML = errorHTML("recent games");
            });
    }

    window.initChessDashboard = initChessDashboard;
})();