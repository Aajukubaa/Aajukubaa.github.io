(function () {
    "use strict";

    const ratingTypes = [
        ["chess_rapid", "Rapid", "♟"],
        ["chess_blitz", "Blitz", "🔥"],
        ["chess_bullet", "Bullet", "⚡"],
        ["chess_daily", "Daily", "📅"],
        ["chess960_daily", "Daily 960", "♜"],
    ];

    function escapeHtml(value) {
        return String(value ?? "").replace(/[&<>"']/g, (character) => ({
            "&": "&amp;",
            "<": "&lt;",
            ">": "&gt;",
            '"': "&quot;",
            "'": "&#39;",
        })[character]);
    }

    function safeGameUrl(value) {
        return typeof value === "string" && /^https:\/\/www\.chess\.com\//i.test(value)
            ? value
            : null;
    }

    function ratingCard(title, icon, rating) {
        const last = rating.last || {};
        const best = rating.best || {};
        const record = rating.record || {};
        const wins = Number(record.win) || 0;
        const losses = Number(record.loss) || 0;
        const draws = Number(record.draw) || 0;
        const total = wins + losses + draws;
        const bestValue = best.rating == null ? "—" : escapeHtml(best.rating);
        const bestUrl = safeGameUrl(best.game);
        const bestMarkup = bestUrl
            ? `<a class="chess-stat-best" href="${escapeHtml(bestUrl)}" target="_blank" rel="noopener">Best ${bestValue} ↗</a>`
            : `<p class="chess-stat-best">Best ${bestValue}</p>`;

        return `<article class="chess-stat-card">
            <div class="chess-stat-header">
                <span class="chess-stat-icon">${escapeHtml(icon)}</span>
                <h4>${escapeHtml(title)}</h4>
            </div>
            <p class="chess-stat-rating">${last.rating == null ? "—" : escapeHtml(last.rating)}</p>
            ${bestMarkup}
            <p class="chess-stat-record">${escapeHtml(wins)}W · ${escapeHtml(losses)}L · ${escapeHtml(draws)}D</p>
            <p class="chess-stat-winrate">${total ? `${Math.round((wins / total) * 100)}% wins` : "Win rate —"}</p>
        </article>`;
    }

    function renderStats(container, stats) {
        const cards = [];
        ratingTypes.forEach(([key, label, icon]) => {
            if (stats && stats[key] && typeof stats[key] === "object") {
                cards.push(ratingCard(label, icon, stats[key]));
            }
        });
        if (stats && stats.tactics && typeof stats.tactics === "object") {
            const highest = stats.tactics.highest && stats.tactics.highest.rating;
            const lowest = stats.tactics.lowest && stats.tactics.lowest.rating;
            cards.push(`<article class="chess-stat-card">
                <div class="chess-stat-header">
                    <span class="chess-stat-icon">🧩</span>
                    <h4>Tactics</h4>
                </div>
                <p class="chess-stat-rating">${highest == null ? "—" : escapeHtml(highest)}</p>
                <p class="chess-stat-record">Highest rating</p>
                <p class="chess-stat-winrate">Lowest ${lowest == null ? "—" : escapeHtml(lowest)}</p>
            </article>`);
        }
        if (stats && stats.puzzle_rush && typeof stats.puzzle_rush === "object") {
            const score = stats.puzzle_rush.best && stats.puzzle_rush.best.score;
            cards.push(`<article class="chess-stat-card">
                <div class="chess-stat-header">
                    <span class="chess-stat-icon">⏱️</span>
                    <h4>Puzzle Rush</h4>
                </div>
                <p class="chess-stat-rating">${score == null ? "—" : escapeHtml(score)}</p>
                <p class="chess-stat-record">Best score</p>
            </article>`);
        }
        if (stats && stats.fide != null) {
            cards.push(`<article class="chess-stat-card">
                <div class="chess-stat-header">
                    <span class="chess-stat-icon">♟</span>
                    <h4>FIDE</h4>
                </div>
                <p class="chess-stat-rating">${escapeHtml(stats.fide)}</p>
                <p class="chess-stat-record">Official rating</p>
            </article>`);
        }
        container.innerHTML = cards.length
            ? cards.join("")
            : '<p class="chess-dashboard-error">No chess rating data is available.</p>';
    }

    let dataPromise;

    function loadChessData() {
        if (!dataPromise) {
            dataPromise = fetch("chess-data.json")
                .then((response) => {
                    if (!response.ok) throw new Error("Could not load chess-data.json");
                    return response.json();
                });
        }
        return dataPromise;
    }

    function initChessDashboard() {
        const statsEl = document.getElementById("chesscom-stats");
        const updatedEl = document.getElementById("chesscom-updated");
        if (!statsEl) return;
        statsEl.innerHTML = '<p class="chess-dashboard-loading">Loading live ratings…</p>';

        loadChessData()
            .then((data) => {
                renderStats(statsEl, data && data.stats ? data.stats : {});
                if (updatedEl && data && data.fetched_at) {
                    const date = new Date(data.fetched_at);
                    updatedEl.textContent = Number.isNaN(date.getTime())
                        ? ""
                        : `Updated ${date.toLocaleString(undefined, {
                            month: "short",
                            day: "numeric",
                            hour: "numeric",
                            minute: "2-digit",
                        })}`;
                }
            })
            .catch(() => {
                statsEl.innerHTML = '<p class="chess-dashboard-error">Couldn’t load chess ratings right now. Try refreshing later.</p>';
            });
    }

    window.addEventListener("message", (event) => {
        if (!/^https:\/\/([a-z0-9-]+\.)*chess\.com$/.test(event.origin)) return;
        const data = event.data;
        if (!data || data.id == null || data.frameHeight == null) return;
        const frame = document.getElementById(String(data.id));
        if (frame && frame.tagName === "IFRAME") {
            frame.style.height = (Number(data.frameHeight) + 37) + "px";
        }
    });

    window.initChessDashboard = initChessDashboard;
})();
