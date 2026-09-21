// Site-wide search. Builds its index from data already on the page —
// the visible domain/highlight/archive cards, plus the categories JSON
// that's embedded for the detail modal — so there's no separate search
// data pipeline to keep in sync with content.py.

(function () {
    "use strict";

    let searchIndex = null;
    let activeResultIndex = -1;
    let currentResults = [];

    function stripHtml(html) {
        const div = document.createElement("div");
        div.innerHTML = html || "";
        return (div.textContent || "").replace(/\s+/g, " ").trim();
    }

    function buildSearchIndex() {
        const dataEl = document.getElementById("categories-data");
        if (!dataEl) return [];
        const categories = JSON.parse(dataEl.textContent);

        const entries = Object.keys(categories).map((catId) => {
            const cat = categories[catId];
            const plain = [stripHtml(cat.title), stripHtml(cat.badge), stripHtml(cat.bento), stripHtml(cat.content)]
                .join(" ")
                .replace(/\s+/g, " ")
                .trim();
            return { id: catId, title: stripHtml(cat.title) || catId, cardTitle: null, blurb: "", plain };
        });

        // Pull a nicer display title/blurb from the visible card itself,
        // where one exists (title casing there is friendlier than the
        // all-caps detail-view title).
        document.querySelectorAll("[data-category]").forEach((card) => {
            const catId = card.getAttribute("data-category");
            const entry = entries.find((e) => e.id === catId);
            if (!entry) return;
            const h3 = card.querySelector("h3");
            const p = card.querySelector(".card-preview p, p");
            if (h3) entry.cardTitle = h3.textContent.trim();
            if (p) entry.blurb = p.textContent.trim();
        });

        return entries;
    }

    function runSearch(query) {
        const q = query.trim().toLowerCase();
        if (q.length < 2) return [];
        if (!searchIndex) searchIndex = buildSearchIndex();

        const results = [];
        for (const entry of searchIndex) {
            const lower = entry.plain.toLowerCase();
            const idx = lower.indexOf(q);
            if (idx === -1) continue;

            const start = Math.max(0, idx - 40);
            const end = Math.min(entry.plain.length, idx + q.length + 70);
            let snippet = entry.plain.slice(start, end).trim();
            if (start > 0) snippet = "…" + snippet;
            if (end < entry.plain.length) snippet = snippet + "…";

            results.push({
                id: entry.id,
                title: entry.cardTitle || entry.title,
                snippet: snippet || entry.blurb,
            });
            if (results.length >= 8) break;
        }
        return results;
    }

    function renderResults(results, query) {
        const container = document.getElementById("search-results");
        if (!container) return;
        currentResults = results;
        activeResultIndex = results.length ? 0 : -1;

        if (!query || query.trim().length < 2) {
            container.innerHTML = '<p class="search-empty">Type at least 2 characters…</p>';
            return;
        }
        if (!results.length) {
            container.innerHTML = '<p class="search-empty">No matches for "' + query.replace(/</g, "&lt;") + '".</p>';
            return;
        }

        container.innerHTML = results
            .map(
                (r, i) =>
                    '<button type="button" class="search-result-row' + (i === 0 ? " active" : "") + '" data-result-id="' + r.id + '">' +
                    '<span class="search-result-title">' + r.title + "</span>" +
                    '<span class="search-result-snippet">' + r.snippet + "</span>" +
                    "</button>"
            )
            .join("");

        container.querySelectorAll(".search-result-row").forEach((row, i) => {
            row.addEventListener("click", () => {
                openResult(currentResults[i]);
            });
        });
    }

    function updateActiveRow() {
        const container = document.getElementById("search-results");
        if (!container) return;
        container.querySelectorAll(".search-result-row").forEach((row, i) => {
            row.classList.toggle("active", i === activeResultIndex);
            if (i === activeResultIndex) row.scrollIntoView({ block: "nearest" });
        });
    }

    function openResult(result) {
        if (!result) return;
        closeSearch();
        // Every card-driving element shares its category id as its
        // element id — calling .click() reuses the site's existing
        // open-detail logic instead of duplicating it here. This works
        // even if the card lives in a tab that isn't currently active,
        // since detail-view is a full-screen overlay regardless.
        const card = document.getElementById(result.id);
        if (card) card.click();
    }

    function openSearch() {
        const modal = document.getElementById("search-modal");
        const input = document.getElementById("search-input");
        if (!modal || !input) return;
        if (!searchIndex) searchIndex = buildSearchIndex();
        modal.classList.add("search-open");
        if (window.lockBodyScroll) window.lockBodyScroll();
        input.value = "";
        renderResults([], "");
        setTimeout(() => input.focus(), 30);
    }

    function closeSearch() {
        const modal = document.getElementById("search-modal");
        if (!modal || !modal.classList.contains("search-open")) return false;
        modal.classList.remove("search-open");
        if (window.unlockBodyScroll) window.unlockBodyScroll();
        return true;
    }
    window.closeSearchModal = closeSearch;

    const searchToggle = document.getElementById("search-toggle");
    if (searchToggle) searchToggle.addEventListener("click", openSearch);

    document.querySelectorAll('[data-action="close-search"]').forEach((el) => {
        el.addEventListener("click", (e) => {
            if (e.target === el) closeSearch();
        });
    });

    const searchInput = document.getElementById("search-input");
    if (searchInput) {
        searchInput.addEventListener("input", () => {
            renderResults(runSearch(searchInput.value), searchInput.value);
        });
        searchInput.addEventListener("keydown", (e) => {
            if (e.key === "ArrowDown") {
                e.preventDefault();
                if (currentResults.length) {
                    activeResultIndex = (activeResultIndex + 1) % currentResults.length;
                    updateActiveRow();
                }
            } else if (e.key === "ArrowUp") {
                e.preventDefault();
                if (currentResults.length) {
                    activeResultIndex = (activeResultIndex - 1 + currentResults.length) % currentResults.length;
                    updateActiveRow();
                }
            } else if (e.key === "Enter") {
                e.preventDefault();
                if (activeResultIndex >= 0) openResult(currentResults[activeResultIndex]);
            }
        });
    }

    document.addEventListener("keydown", (e) => {
        const isSearchShortcut = (e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k";
        if (isSearchShortcut) {
            e.preventDefault();
            const modal = document.getElementById("search-modal");
            if (modal && modal.classList.contains("search-open")) {
                closeSearch();
            } else {
                openSearch();
            }
        }
    });
})();