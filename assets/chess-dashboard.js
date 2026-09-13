// Live Chess.com dashboard for the Chess domain card.
// Loaded on every page view, but does nothing (and loads no external
// libraries) until the chess card is actually opened — see the
// window.initChessDashboard hook called from main.js's openCategory().

(function () {
    "use strict";

    // Hardcoded per request — this is the one place to change it.
    var CHESS_USERNAME = "Aajukubaa";

    // ---------- Lazy-load jQuery + chess.js + chessboard.js ----------
    // Nothing here costs the page anything until someone actually opens
    // the chess card — these are real (small) library downloads, so they
    // stay off the critical path for every other visit.
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
        // chessboard.js requires jQuery to already be present when it
        // loads, so that has to finish first; chess.js is independent
        // and can load in parallel with it.
        chessLibsPromise = loadScript("https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js")
            .then(function () {
                return Promise.all([
                    loadScript("https://cdnjs.cloudflare.com/ajax/libs/chess.js/0.13.4/chess.min.js"),
                    loadScript("https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/chessboard-1.0.0.min.js"),
                ]);
            });
        return chessLibsPromise;
    }

    // ---------- Chess.com API ----------
    var API_BASE = "https://api.chess.com/pub/player/" + CHESS_USERNAME.toLowerCase();
    var CACHE_MS = 5 * 60 * 1000; // avoid re-hitting the API every time the card is reopened
    var cache = { stats: null, games: null, fetchedAt: 0 };

    function fetchJSON(url) {
        return fetch(url).then(function (res) {
            if (!res.ok) throw new Error("Request failed: " + url);
            return res.json();
        });
    }

    var RATING_TYPES = [
        { key: "chess_bullet", label: "Bullet" },
        { key: "chess_blitz", label: "Blitz" },
        { key: "chess_rapid", label: "Rapid" },
    ];

    function renderStats(container, stats) {
        container.innerHTML = RATING_TYPES.map(function (t) {
            var s = stats[t.key];
            if (!s || !s.last) {
                return '<div class="chess-stat-card"><h4>' + t.label + '</h4>' +
                    '<p class="chess-stat-rating">—</p>' +
                    '<p class="chess-stat-record">No rated games yet</p></div>';
            }
            var rec = s.record || { win: 0, loss: 0, draw: 0 };
            return '<div class="chess-stat-card"><h4>' + t.label + '</h4>' +
                '<p class="chess-stat-rating">' + s.last.rating + '</p>' +
                '<p class="chess-stat-record">' + rec.win + 'W – ' + rec.loss + 'L – ' + rec.draw + 'D</p></div>';
        }).join("");
    }

    function statsErrorHTML() {
        return '<p class="chess-dashboard-error">Couldn\u2019t load live ratings right now — try refreshing, or see the profile directly on ' +
            '<a href="https://www.chess.com/member/' + CHESS_USERNAME + '" target="_blank">Chess.com</a>.</p>';
    }
    function gamesErrorHTML() {
        return '<p class="chess-dashboard-error">Couldn\u2019t load recent games right now — try refreshing, or see the profile directly on ' +
            '<a href="https://www.chess.com/member/' + CHESS_USERNAME + '" target="_blank">Chess.com</a>.</p>';
    }

    // Chess.com's per-side "result" field, mapped to an outcome from
    // that side's point of view. Anything not listed here (checkmated,
    // resigned, timeout, abandoned, lose, kingofthehill, threecheck,
    // bughousepartnerlose) counts as a loss for that side.
    var DRAW_RESULTS = ["agreed", "repetition", "stalemate", "insufficient", "50move", "timevsinsufficient"];
    function outcomeFor(result) {
        if (result === "win") return "win";
        if (DRAW_RESULTS.indexOf(result) !== -1) return "draw";
        return "loss";
    }

    function fetchStatsAndGames() {
        var now = Date.now();
        if (cache.stats && cache.games && now - cache.fetchedAt < CACHE_MS) {
            return Promise.resolve(cache);
        }
        var statsPromise = fetchJSON(API_BASE + "/stats").catch(function () { return null; });
        var gamesPromise = fetchJSON(API_BASE + "/games/archives")
            .then(function (data) {
                var archives = data.archives || [];
                if (!archives.length) return { games: [] };
                return fetchJSON(archives[archives.length - 1]);
            })
            .catch(function () { return null; });

        return Promise.all([statsPromise, gamesPromise]).then(function (results) {
            cache.stats = results[0];
            cache.games = results[1];
            cache.fetchedAt = now;
            return cache;
        });
    }

    // ---------- Board + move stepping ----------
    var boardInstance = null;
    var currentHistory = [];
    var currentIndex = 0;

    function renderPositionAt(index) {
        var replay = new window.Chess();
        for (var i = 0; i < index; i++) {
            replay.move(currentHistory[i].san);
        }
        if (boardInstance) boardInstance.position(replay.fen());

        var indicator = document.getElementById("chess-move-indicator");
        var prevBtn = document.getElementById("chess-prev-move");
        var nextBtn = document.getElementById("chess-next-move");
        if (indicator) {
            indicator.textContent = currentHistory.length
                ? "Move " + index + " / " + currentHistory.length
                : "No moves recorded";
        }
        if (prevBtn) prevBtn.disabled = index <= 0;
        if (nextBtn) nextBtn.disabled = index >= currentHistory.length;
    }

    function selectGame(game, listEl) {
        var chess = new window.Chess();
        var loaded = false;
        try { loaded = chess.load_pgn(game.pgn, { sloppy: true }); } catch (e) { loaded = false; }
        currentHistory = loaded ? chess.history({ verbose: true }) : [];
        currentIndex = currentHistory.length; // land on the final position

        var boardEl = document.getElementById("chesscom-board");
        if (!boardInstance && boardEl && window.Chessboard) {
            boardInstance = window.Chessboard(boardEl.id, {
                position: "start",
                pieceTheme: "https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/img/chesspieces/wikipedia/{piece}.png",
            });
            if (window.jQuery) {
                window.jQuery(window).on("resize", function () {
                    if (boardInstance) boardInstance.resize();
                });
            }
        }
        renderPositionAt(currentIndex);
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
                '<span class="chess-game-opponent">vs ' + opponent.username + " (" + opponent.rating + ")</span>" +
                '<span class="chess-game-class">' + game.time_class + "</span>";
            row.addEventListener("click", function () {
                listEl.querySelectorAll(".chess-game-row").forEach(function (r) { r.classList.remove("active"); });
                row.classList.add("active");
                selectGame(game, listEl);
            });
            listEl.appendChild(row);
        });
    }

    document.addEventListener("click", function (e) {
        if (e.target && e.target.id === "chess-prev-move" && currentIndex > 0) {
            currentIndex--;
            renderPositionAt(currentIndex);
        }
        if (e.target && e.target.id === "chess-next-move" && currentIndex < currentHistory.length) {
            currentIndex++;
            renderPositionAt(currentIndex);
        }
    });

    // ---------- Entry point ----------
    function initChessDashboard() {
        var statsEl = document.getElementById("chesscom-stats");
        var gamesListEl = document.getElementById("chesscom-games-list");
        if (!statsEl || !gamesListEl) return; // chess card isn't open

        statsEl.innerHTML = '<p class="chess-dashboard-loading">Loading live ratings…</p>';
        gamesListEl.innerHTML = '<p class="chess-dashboard-loading">Loading recent games…</p>';

        ensureChessLibs()
            .then(fetchStatsAndGames)
            .then(function (data) {
                if (data.stats) {
                    renderStats(statsEl, data.stats);
                } else {
                    statsEl.innerHTML = statsErrorHTML();
                }

                var games = (data.games && data.games.games) ? data.games.games.filter(function (g) { return g.pgn; }) : [];
                if (!games.length) {
                    gamesListEl.innerHTML = data.games ? '<p class="chess-dashboard-error">No games found this month yet.</p>' : gamesErrorHTML();
                    return;
                }
                games.sort(function (a, b) { return b.end_time - a.end_time; });
                var recent = games.slice(0, 10);
                renderGamesList(gamesListEl, recent);
                selectGame(recent[0], gamesListEl);
            })
            .catch(function () {
                statsEl.innerHTML = statsErrorHTML();
                gamesListEl.innerHTML = gamesErrorHTML();
            });
    }

    window.initChessDashboard = initChessDashboard;
})();
