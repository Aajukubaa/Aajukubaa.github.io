// Kabir Bhuchar portfolio — all interactivity, plain JS.
// Content for the detail modal is embedded by build.py as JSON
// (see the #categories-data script tag) so nothing here needs a
// Python runtime in the browser.

(function () {
    "use strict";

    const categories = JSON.parse(document.getElementById("categories-data").textContent);
    let lastOpenedCardId = null;

    // ---------- Sound effects (lazy AudioContext, event delegation) ----------
    // The AudioContext is created on first interaction rather than at load,
    // so the browser never has to warn about (or silently ignore) an
    // AudioContext started before any user gesture.
    let audioCtx = null;
    function getAudioCtx() {
        if (!audioCtx) {
            const Ctor = window.AudioContext || window.webkitAudioContext;
            audioCtx = new Ctor();
        }
        if (audioCtx.state === "suspended") audioCtx.resume();
        return audioCtx;
    }

    function playSound(freq = 500, type = "sine", duration = 0.03) {
        try {
            const ctx = getAudioCtx();
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.type = type;
            osc.frequency.setValueAtTime(freq, ctx.currentTime);
            gain.gain.setValueAtTime(0.02, ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + duration);
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start();
            osc.stop(ctx.currentTime + duration);
        } catch (e) { /* audio is a nice-to-have, never block on it */ }
    }

    function playViolinTone() {
        playSound(440, "triangle", 0.4);
    }

    // Delegated listeners: this covers every current element AND anything
    // shown inside the modal later, unlike a one-time querySelectorAll.
    const SOUND_SELECTOR = "a, button, .pro-card, .standard-card, .highlight-card, .connect-card, .nav-tab";
    document.addEventListener("mouseenter", (e) => {
        if (e.target.closest && e.target.closest(SOUND_SELECTOR)) {
            playSound(800, "sine", 0.01);
        }
    }, true);
    document.addEventListener("click", (e) => {
        if (e.target.closest && e.target.closest(SOUND_SELECTOR)) {
            playSound(400, "sine", 0.04);
        }
    });

    // ---------- Custom cursor ----------
    const cursor = document.getElementById("custom-cursor");
    document.addEventListener("mousemove", (e) => {
        if (cursor && !document.body.classList.contains("modal-active")) {
            cursor.style.transform = `translate3d(${e.clientX - 15}px, ${e.clientY - 15}px, 0)`;
        }
    });
    // Only hide the native cursor once we know this script actually ran.
    // If it's ever blocked, body never gets .js-ready and the CSS falls
    // back to a normal, visible cursor instead of vanishing.
    document.body.classList.add("js-ready");

    // ---------- Tabs ----------
    const navTabs = document.querySelectorAll(".nav-tab");
    const tabContents = document.querySelectorAll(".tab-content");

    navTabs.forEach((tab) => {
        tab.addEventListener("click", () => {
            navTabs.forEach((t) => t.classList.remove("active"));
            tabContents.forEach((c) => c.classList.remove("active-view"));

            tab.classList.add("active");
            const targetView = document.getElementById(tab.getAttribute("data-target"));
            if (targetView) {
                targetView.classList.add("active-view");
                window.scrollTo({ top: 0, behavior: "smooth" });
            }
        });
    });

    // ---------- Detail modal ----------
    function openCategory(card) {
        const catId = card.id;
        const item = categories[catId];
        if (!item) return;

        card.classList.add("card-pressed");
        setTimeout(() => card.classList.remove("card-pressed"), 350);

        document.getElementById("detail-title").innerHTML = item.title;
        document.getElementById("detail-badge").innerHTML = item.badge;
        document.getElementById("detail-content").innerHTML = item.content || "";
        document.getElementById("detail-bento-grid").innerHTML = item.bento || "";

        const detail = document.getElementById("detail-view");
        detail.style.display = "block";

        setTimeout(() => {
            detail.classList.remove("modal-closing");
            detail.classList.add("modal-open");
        }, 10);

        document.body.classList.add("modal-active");
        detail.scrollTop = 0;
        lastOpenedCardId = catId;
    }

    function closeCategory() {
        const detail = document.getElementById("detail-view");
        detail.classList.remove("modal-open");
        detail.classList.add("modal-closing");
        document.body.classList.remove("modal-active");

        if (lastOpenedCardId) {
            const cardEl = document.getElementById(lastOpenedCardId);
            if (cardEl) {
                cardEl.classList.add("card-pressed");
                setTimeout(() => cardEl.classList.remove("card-pressed"), 350);
            }
            lastOpenedCardId = null;
        }

        setTimeout(() => {
            detail.style.display = "none";
            detail.classList.remove("modal-closing");
        }, 400);
    }

    document.querySelectorAll("[data-category]").forEach((card) => {
        card.addEventListener("click", () => openCategory(card));
        // These cards already carry role="button" + tabindex="0"; make
        // them keyboard-activatable with Enter/Space to actually honor that.
        card.addEventListener("keydown", (e) => {
            if (e.key === "Enter" || e.key === " ") {
                e.preventDefault();
                openCategory(card);
            }
        });
    });

    document.querySelectorAll('[data-action="close-detail"]').forEach((btn) => {
        btn.addEventListener("click", closeCategory);
    });

    // ---------- Shortcuts modal ----------
    function toggleShortcuts(show) {
        const modal = document.getElementById("shortcuts-modal");
        if (modal) modal.style.display = show ? "flex" : "none";
    }

    document.querySelectorAll('[data-action="close-shortcuts"]').forEach((el) => {
        el.addEventListener("click", (e) => {
            // Don't close when the click originated inside the shortcuts
            // box itself (the box sits inside the same overlay element).
            if (e.target.closest(".shortcuts-box") && e.currentTarget.id === "shortcuts-modal") return;
            toggleShortcuts(false);
        });
    });

    document.addEventListener("keydown", (e) => {
        if (e.key === "Escape") {
            const detail = document.getElementById("detail-view");
            if (detail && detail.classList.contains("modal-open")) {
                closeCategory();
            } else {
                toggleShortcuts(false);
            }
        }
        if (e.key === "?") {
            e.preventDefault();
            const modal = document.getElementById("shortcuts-modal");
            toggleShortcuts(modal.style.display !== "flex");
        }
        if (["1", "2", "3", "4"].includes(e.key) && !document.body.classList.contains("modal-active")) {
            const index = parseInt(e.key, 10) - 1;
            if (navTabs[index]) navTabs[index].click();
        }
    });

    // ---------- Status-check buttons & violin tone ----------
    document.querySelectorAll("[data-alert]").forEach((btn) => {
        btn.addEventListener("click", () => alert(btn.getAttribute("data-alert")));
    });
    document.querySelectorAll('[data-action="play-violin"]').forEach((btn) => {
        btn.addEventListener("click", playViolinTone);
    });
})();
