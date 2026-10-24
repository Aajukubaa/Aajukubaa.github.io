(function () {
    "use strict";

    const BLOCK_SELECTOR = "h1, h2, h3, h4, h5, p, li, figcaption, blockquote";
    const SEARCH_EXCLUSIONS = ".connect-carousel, #tab-search, [aria-hidden='true'], .chess-dashboard-loading, script, style";
    const searchInput = document.getElementById("search-input");
    const searchView = document.querySelector("#tab-search .search-page");
    const searchStatus = document.getElementById("search-status");
    const suggestions = document.getElementById("search-suggestions");
    const resultsContainer = document.getElementById("search-results");
    let searchIndex = null;
    let currentResults = [];
    let activeResultIndex = -1;
    let lastRenderedQuery = null;
    let debounceTimer = null;

    function normalizedText(value) {
        return String(value || "").replace(/\s+/g, " ").trim();
    }

    function blocksIn(root) {
        if (!root || !root.querySelectorAll) return [];
        return Array.from(root.querySelectorAll(BLOCK_SELECTOR)).filter((element) => {
            if (!normalizedText(element.textContent)) return false;
            if (element.querySelector(BLOCK_SELECTOR)) return false;
            return !element.closest(SEARCH_EXCLUSIONS);
        });
    }

    function nearestHeading(root, element, selector) {
        let nearest = "";
        root.querySelectorAll(selector).forEach((heading) => {
            if (
                heading === element ||
                (heading.compareDocumentPosition(element) & Node.DOCUMENT_POSITION_FOLLOWING)
            ) {
                nearest = normalizedText(heading.textContent);
            }
        });
        return nearest;
    }

    function titleCase(value) {
        return String(value || "")
            .replace(/[-_]+/g, " ")
            .replace(/\b\w/g, (character) => character.toUpperCase());
    }

    function categorySectionTitle(catId) {
        const card = document.getElementById(catId);
        const cardTitle = card?.querySelector("h3")?.textContent;
        if (cardTitle) return normalizedText(cardTitle);
        return titleCase(catId);
    }

    function parseHtml(html) {
        const template = document.createElement("template");
        template.innerHTML = html || "";
        return template.content;
    }

    function buildSearchIndex() {
        const entries = [];
        document.querySelectorAll(".tab-content").forEach((tab) => {
            if (tab.id === "tab-search") return;
            const navTab = Array.from(document.querySelectorAll(".nav-tab[data-target]"))
                .find((button) => button.getAttribute("data-target") === tab.id);
            const section = normalizedText(navTab?.querySelector(".nav-label")?.textContent || navTab?.textContent);
            blocksIn(tab).forEach((element) => {
                entries.push({
                    kind: "page",
                    tabId: tab.id,
                    el: element,
                    text: normalizedText(element.textContent),
                    section: section || titleCase(tab.id.replace(/^tab-/, "")),
                    heading: nearestHeading(tab, element, "h1, h2, h3, h4, h5"),
                    index: entries.length,
                });
            });
        });

        const dataElement = document.getElementById("categories-data");
        if (!dataElement) return entries;
        const categories = JSON.parse(dataElement.textContent);
        Object.keys(categories).forEach((catId) => {
            const category = categories[catId];
            const section = categorySectionTitle(catId);
            ["bento", "content"].forEach((part) => {
                const root = parseHtml(category[part]);
                blocksIn(root).forEach((element, ordinal) => {
                    entries.push({
                        kind: "detail",
                        catId,
                        part,
                        ordinal,
                        text: normalizedText(element.textContent),
                        section,
                        heading: nearestHeading(root, element, "h2, h4"),
                        index: entries.length,
                    });
                });
            });
        });
        return entries;
    }

    function getSearchIndex() {
        if (!searchIndex) searchIndex = buildSearchIndex();
        return searchIndex;
    }

    function queryTerms(query) {
        const seen = new Set();
        return String(query || "").trim().split(/\s+/)
            .filter((term) => {
                const key = term.toLowerCase();
                if (term.length < 2 || seen.has(key)) return false;
                seen.add(key);
                return true;
            })
            .sort((left, right) => right.length - left.length);
    }

    function escapeHtml(value) {
        return String(value ?? "").replace(/[&<>"']/g, (character) => ({
            "&": "&amp;",
            "<": "&lt;",
            ">": "&gt;",
            '"': "&quot;",
            "'": "&#39;",
        })[character]);
    }

    function escapeRegex(value) {
        return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    }

    function highlightMatches(value, terms) {
        if (!terms.length) return escapeHtml(value);
        const matcher = new RegExp(terms.map(escapeRegex).join("|"), "gi");
        let output = "";
        let lastIndex = 0;
        let match;
        while ((match = matcher.exec(value)) !== null) {
            output += escapeHtml(value.slice(lastIndex, match.index));
            output += '<mark class="search-hit">' + escapeHtml(match[0]) + "</mark>";
            lastIndex = match.index + match[0].length;
        }
        return output + escapeHtml(value.slice(lastIndex));
    }

    function occurrenceCount(text, term) {
        return (text.match(new RegExp(escapeRegex(term), "gi")) || []).length;
    }

    function makeSnippet(text, terms) {
        const lower = text.toLowerCase();
        const firstIndex = Math.min(...terms.map((term) => lower.indexOf(term.toLowerCase())));
        const start = Math.max(0, firstIndex - 65);
        const end = Math.min(text.length, start + 160);
        const adjustedStart = Math.max(0, end - 160);
        return (adjustedStart > 0 ? "…" : "") +
            text.slice(adjustedStart, end).trim() +
            (end < text.length ? "…" : "");
    }

    function runSearch(query) {
        const terms = queryTerms(query);
        if (!terms.length) return { terms, groups: [], count: 0 };

        const grouped = new Map();
        getSearchIndex().forEach((entry) => {
            const lower = entry.text.toLowerCase();
            const matchedTerms = terms.filter((term) => lower.includes(term.toLowerCase()));
            if (!matchedTerms.length) return;

            const totalOccurrences = Math.min(
                5,
                matchedTerms.reduce((total, term) => total + occurrenceCount(entry.text, term), 0)
            );
            const headingMatch = matchedTerms.some((term) =>
                entry.heading.toLowerCase().includes(term.toLowerCase())
            );
            const score = matchedTerms.length * 10 + totalOccurrences + (headingMatch ? 3 : 0);
            const breadcrumb = entry.heading && entry.heading.toLowerCase() !== entry.text.toLowerCase()
                ? entry.section + " › " + entry.heading
                : entry.section;
            const result = {
                ...entry,
                matchedTerms,
                score,
                breadcrumb,
                snippet: makeSnippet(entry.text, matchedTerms),
            };
            if (!grouped.has(entry.section)) grouped.set(entry.section, []);
            grouped.get(entry.section).push(result);
        });

        const orderedGroups = Array.from(grouped.entries())
            .map(([section, results]) => ({
                section,
                firstIndex: Math.min(...results.map((result) => result.index)),
                results: results.sort((left, right) => right.score - left.score || left.index - right.index),
            }))
            .sort((left, right) =>
                right.results[0].score - left.results[0].score ||
                left.firstIndex - right.firstIndex
            );

        const groups = [];
        let count = 0;
        orderedGroups.forEach((group) => {
            if (count >= 50) return;
            const remaining = 50 - count;
            const results = group.results.slice(0, Math.min(8, remaining));
            if (!results.length) return;
            groups.push({ section: group.section, results });
            count += results.length;
        });
        return { terms, groups, count };
    }

    function statusMessage(template, values) {
        return template.replace(/\{(\w+)\}/g, (match, key) =>
            Object.prototype.hasOwnProperty.call(values, key) ? values[key] : match
        );
    }

    function updateSearchHash(query) {
        if (!document.querySelector('.nav-tab.active[data-target="tab-search"]')) return;
        history.replaceState(null, "", "#search?q=" + encodeURIComponent(query));
    }

    function renderSearch(query, { updateHash = true } = {}) {
        if (!searchInput || !searchStatus || !suggestions || !resultsContainer || !searchView) return;
        const value = String(query || "").trim();
        const data = runSearch(value);
        const previousActiveIndex = activeResultIndex;
        const preserveActiveIndex = value === lastRenderedQuery;
        currentResults = data.groups.flatMap((group) => group.results);
        activeResultIndex = currentResults.length
            ? (preserveActiveIndex ? Math.min(previousActiveIndex, currentResults.length - 1) : 0)
            : -1;
        lastRenderedQuery = value;

        if (!value) {
            searchStatus.textContent = searchView.dataset.statusEmpty;
            suggestions.hidden = false;
            resultsContainer.innerHTML = "";
        } else if (!data.terms.length) {
            searchStatus.textContent = searchView.dataset.statusMinimum;
            suggestions.hidden = false;
            resultsContainer.innerHTML = "";
        } else if (!currentResults.length) {
            searchStatus.textContent = statusMessage(searchView.dataset.statusNoResults, { query: value });
            suggestions.hidden = false;
            resultsContainer.innerHTML = '<p class="search-empty-message">' +
                escapeHtml(searchStatus.textContent) + "</p>";
        } else {
            const statusTemplate = currentResults.length === 1
                ? searchView.dataset.statusResultsOne
                : searchView.dataset.statusResultsMany;
            searchStatus.textContent = statusMessage(statusTemplate, {
                count: currentResults.length,
                query: value,
            });
            suggestions.hidden = true;
            let resultIndex = 0;
            resultsContainer.innerHTML = data.groups.map((group) => {
                const rows = group.results.map((result) => {
                    const index = resultIndex++;
                    return '<button type="button" class="search-result-row' +
                        (index === 0 ? " active" : "") +
                        '" data-result-index="' + index + '">' +
                        '<span class="search-result-breadcrumb">' +
                        highlightMatches(result.breadcrumb, result.matchedTerms) +
                        "</span>" +
                        '<span class="search-result-snippet">' +
                        highlightMatches(result.snippet, result.matchedTerms) +
                        "</span></button>";
                }).join("");
                return '<section class="search-result-group"><h2 class="search-result-group-title">' +
                    highlightMatches(group.section, data.terms) + "</h2>" + rows + "</section>";
            }).join("");
        }
        if (updateHash) updateSearchHash(value);
    }

    function updateActiveRow() {
        const rows = Array.from(resultsContainer.querySelectorAll(".search-result-row"));
        rows.forEach((row, index) => {
            row.classList.toggle("active", index === activeResultIndex);
            if (index === activeResultIndex) row.scrollIntoView({ block: "nearest" });
        });
    }

    function clearJumpHighlights() {
        document.querySelectorAll("mark.search-jump-hit").forEach((mark) => {
            const parent = mark.parentNode;
            mark.replaceWith(document.createTextNode(mark.textContent || ""));
            parent?.normalize();
        });
        document.querySelectorAll(".search-jump-target").forEach((element) => {
            element.classList.remove("search-jump-target");
        });
    }

    function markTarget(target, terms) {
        if (!target || !terms.length) return;
        const matcher = new RegExp(terms.map(escapeRegex).join("|"), "gi");
        const walker = document.createTreeWalker(target, NodeFilter.SHOW_TEXT, {
            acceptNode(node) {
                return node.parentElement?.closest("script, style")
                    ? NodeFilter.FILTER_REJECT
                    : NodeFilter.FILTER_ACCEPT;
            },
        });
        const nodes = [];
        while (walker.nextNode()) nodes.push(walker.currentNode);
        nodes.forEach((node) => {
            const matches = Array.from(node.nodeValue.matchAll(matcher));
            for (let index = matches.length - 1; index >= 0; index -= 1) {
                const match = matches[index];
                const selected = node.splitText(match.index);
                selected.splitText(match[0].length);
                const mark = document.createElement("mark");
                mark.className = "search-jump-hit";
                selected.parentNode.replaceChild(mark, selected);
                mark.appendChild(selected);
            }
        });
    }

    function jumpToTarget(target, terms) {
        if (!target) return;
        const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
        target.scrollIntoView({
            behavior: reducedMotion ? "auto" : "smooth",
            block: "center",
        });
        markTarget(target, terms);
        target.classList.add("search-jump-target");
    }

    function firstBlockContainingTerm(blocks, terms) {
        return blocks.find((block) => {
            const text = normalizedText(block.textContent).toLowerCase();
            return terms.some((term) => text.includes(term.toLowerCase()));
        });
    }

    function openResult(result) {
        if (!result) return;
        clearJumpHighlights();
        if (result.kind === "page") {
            if (!window.showTab?.(result.tabId, { scrollTop: false })) return;
            requestAnimationFrame(() => {
                let target = result.el;
                if (!target?.isConnected) {
                    const root = document.getElementById(result.tabId);
                    const blocks = blocksIn(root);
                    target = blocks.find((block) => normalizedText(block.textContent) === result.text) ||
                        firstBlockContainingTerm(blocks, result.matchedTerms);
                }
                jumpToTarget(target, result.matchedTerms);
            });
            return;
        }

        if (!window.openCategoryById?.(result.catId)) return;
        window.setTimeout(() => {
            const rootId = result.part === "bento" ? "detail-bento-grid" : "detail-content";
            const blocks = blocksIn(document.getElementById(rootId));
            let target = blocks[result.ordinal];
            if (!target || normalizedText(target.textContent) !== result.text) {
                target = blocks.find((block) => normalizedText(block.textContent) === result.text) ||
                    firstBlockContainingTerm(blocks, result.matchedTerms);
            }
            jumpToTarget(target, result.matchedTerms);
        }, 350);
    }

    if (searchInput) {
        searchInput.addEventListener("input", () => {
            window.clearTimeout(debounceTimer);
            debounceTimer = window.setTimeout(() => renderSearch(searchInput.value), 120);
        });
        searchInput.addEventListener("keydown", (event) => {
            if (event.key === "ArrowDown" || event.key === "ArrowUp" || event.key === "Enter") {
                window.clearTimeout(debounceTimer);
                renderSearch(searchInput.value);
            }
            if (event.key === "ArrowDown" && currentResults.length) {
                event.preventDefault();
                activeResultIndex = (activeResultIndex + 1) % currentResults.length;
                updateActiveRow();
            } else if (event.key === "ArrowUp" && currentResults.length) {
                event.preventDefault();
                activeResultIndex = (activeResultIndex - 1 + currentResults.length) % currentResults.length;
                updateActiveRow();
            } else if (event.key === "Enter" && activeResultIndex >= 0) {
                event.preventDefault();
                openResult(currentResults[activeResultIndex]);
            }
        });
    }

    if (suggestions) {
        suggestions.addEventListener("click", (event) => {
            const button = event.target.closest("[data-search-suggestion]");
            if (!button || !searchInput) return;
            searchInput.value = button.dataset.searchSuggestion || "";
            renderSearch(searchInput.value);
            searchInput.focus();
        });
    }

    if (resultsContainer) {
        resultsContainer.addEventListener("click", (event) => {
            const row = event.target.closest(".search-result-row");
            if (!row) return;
            const index = Number(row.dataset.resultIndex);
            openResult(currentResults[index]);
        });
    }

    document.querySelector('.nav-tab[data-target="tab-search"]')?.addEventListener("click", () => {
        updateSearchHash(searchInput?.value || "");
    });

    const deepLink = window.location.hash.match(/^#search(?:\?(.*))?$/i);
    if (deepLink) {
        const query = new URLSearchParams(deepLink[1] || "").get("q") || "";
        window.showTab?.("tab-search");
        if (searchInput) searchInput.value = query;
        renderSearch(query, { updateHash: false });
    } else {
        renderSearch("");
    }
})();
