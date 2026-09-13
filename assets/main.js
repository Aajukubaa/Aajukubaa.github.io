// Kabir Bhuchar portfolio — all interactivity, plain JS.
// Content for the detail modal is embedded by build.py as JSON
// (see the #categories-data script tag) so nothing here needs a
// Python runtime in the browser.

(function () {
    "use strict";

    const categories = JSON.parse(document.getElementById("categories-data").textContent);
    let lastOpenedCardId = null;

    // ---------- Sound effects (lazy AudioContext, mute toggle) ----------
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

    let soundEnabled = true;
    try {
        soundEnabled = localStorage.getItem("soundEnabled") !== "off";
    } catch (e) { /* localStorage can be unavailable (private mode etc.) — default on */ }

    function playTone(freq, type, duration, startTime, gainPeak) {
        const ctx = getAudioCtx();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = type;
        osc.frequency.setValueAtTime(freq, startTime);
        // Small linear ramp up before the exponential decay avoids the
        // audible "click" a hard instant-on can cause on short tones.
        gain.gain.setValueAtTime(0.0001, startTime);
        gain.gain.linearRampToValueAtTime(gainPeak, startTime + Math.min(0.008, duration / 4));
        gain.gain.exponentialRampToValueAtTime(0.0001, startTime + duration);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(startTime);
        osc.stop(startTime + duration);
    }

    function playSound(freq = 500, type = "sine", duration = 0.03, gainPeak = 0.02) {
        if (!soundEnabled) return;
        try {
            playTone(freq, type, duration, getAudioCtx().currentTime, gainPeak);
        } catch (e) { /* audio is a nice-to-have, never block on it */ }
    }

    function playChime(freqs, type = "sine", noteDuration = 0.16, gainPeak = 0.03) {
        if (!soundEnabled) return;
        try {
            const ctx = getAudioCtx();
            freqs.forEach((freq, i) => {
                playTone(freq, type, noteDuration, ctx.currentTime + i * (noteDuration * 0.6), gainPeak);
            });
        } catch (e) { /* ditto */ }
    }

    function playViolinTone() {
        // A short pleasant arpeggio rather than one flat tone.
        playChime([392.0, 493.88, 587.33], "triangle", 0.35, 0.025); // G4, B4, D5
    }

    function playModalOpenSound() { playChime([440, 660], "sine", 0.09, 0.02); }
    function playModalCloseSound() { playChime([660, 440], "sine", 0.09, 0.02); }

    // Sound mute toggle, in the nav bar.
    const soundToggle = document.getElementById("sound-toggle");
    function updateSoundToggleUI() {
        if (!soundToggle) return;
        soundToggle.textContent = soundEnabled ? "🔊" : "🔇";
        soundToggle.classList.toggle("is-muted", !soundEnabled);
        soundToggle.setAttribute("aria-pressed", String(!soundEnabled));
    }
    if (soundToggle) {
        updateSoundToggleUI();
        soundToggle.addEventListener("click", () => {
            soundEnabled = !soundEnabled;
            try { localStorage.setItem("soundEnabled", soundEnabled ? "on" : "off"); } catch (e) { /* ignore */ }
            updateSoundToggleUI();
            if (soundEnabled) playSound(600, "sine", 0.05, 0.03);
        });
    }

    // Hover sound: only on the "big" clickable surfaces (cards/nav), not
    // every tiny link or button — constant beeping on every element was
    // the main complaint. Uses mouseover/mouseout (which bubble) with a
    // relatedTarget check so moving between nested children of the same
    // card doesn't retrigger the sound.
    const HOVER_SOUND_SELECTOR = ".pro-card, .standard-card, .highlight-card, .connect-card, .nav-tab, .reveal-tile, .bento-tile-link";
    const CLICK_SOUND_SELECTOR = HOVER_SOUND_SELECTOR + ", .interactive-btn, .card-action-btn";

    document.addEventListener("mouseover", (e) => {
        const el = e.target.closest(HOVER_SOUND_SELECTOR);
        if (!el) return;
        if (e.relatedTarget && el.contains(e.relatedTarget)) return;
        playSound(800, "sine", 0.045, 0.012);
    });
    document.addEventListener("click", (e) => {
        if (e.target.closest && e.target.closest(CLICK_SOUND_SELECTOR)) {
            playSound(400, "sine", 0.05, 0.018);
        }
    });

    // ---------- Custom cursor ----------
    const cursor = document.getElementById("custom-cursor");
    document.addEventListener("mousemove", (e) => {
        if (cursor) {
            cursor.style.transform = `translate3d(${e.clientX - 15}px, ${e.clientY - 15}px, 0)`;
        }
    });
    // Fade out (not just leave in place) once the pointer actually leaves
    // the browser window — checking relatedTarget is null is the standard
    // cross-browser way to distinguish "left the window" from "moved to
    // a child element".
    document.addEventListener("mouseout", (e) => {
        if (cursor && !e.relatedTarget) cursor.classList.add("cursor-hidden");
    });
    document.addEventListener("mouseover", () => {
        if (cursor) cursor.classList.remove("cursor-hidden");
    });
    // Only hide the native cursor once we know this script actually ran.
    // If it's ever blocked, body never gets .js-ready and the CSS falls
    // back to a normal, visible cursor instead of vanishing.
    document.body.classList.add("js-ready");

    // ---------- Body scroll lock (used by both modals) ----------
    // overflow:hidden alone doesn't reliably stop background touch-scroll
    // on iOS Safari. Pinning the body at its current scroll position and
    // restoring it on close is the standard cross-device-reliable fix.
    let lockedScrollY = 0;
    let scrollLockCount = 0;
    function lockBodyScroll() {
        if (scrollLockCount === 0) {
            lockedScrollY = window.scrollY;
            document.body.style.position = "fixed";
            document.body.style.top = `-${lockedScrollY}px`;
            document.body.style.width = "100%";
            document.body.classList.add("modal-active");
        }
        scrollLockCount++;
    }
    function unlockBodyScroll() {
        scrollLockCount = Math.max(0, scrollLockCount - 1);
        if (scrollLockCount === 0) {
            document.body.classList.remove("modal-active");
            document.body.style.position = "";
            document.body.style.top = "";
            document.body.style.width = "";
            window.scrollTo(0, lockedScrollY);
        }
    }

    // ---------- Tabs ----------
    // Scoped to [data-target] specifically so the sound-mute button
    // (also styled .nav-tab) never gets treated as a page tab.
    const navTabs = document.querySelectorAll(".nav-tab[data-target]");
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

        lockBodyScroll();
        detail.scrollTop = 0;
        lastOpenedCardId = catId;
        playModalOpenSound();

        // The dashboard's containers only exist in the DOM once this
        // category's HTML has just been injected above, so it can only
        // be initialized from here — not on page load.
        if (catId === "chess" && window.initChessDashboard) {
            window.initChessDashboard();
        }
    }

    function closeCategory() {
        const detail = document.getElementById("detail-view");
        detail.classList.remove("modal-open");
        detail.classList.add("modal-closing");
        unlockBodyScroll();

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
        playModalCloseSound();
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

    // ---------- Shortcuts modal ----------
    function toggleShortcuts(show) {
        const modal = document.getElementById("shortcuts-modal");
        if (!modal) return;
        modal.style.display = show ? "flex" : "none";
        if (show) lockBodyScroll();
        else unlockBodyScroll();
    }

    document.querySelectorAll('[data-action="close-shortcuts"]').forEach((el) => {
        el.addEventListener("click", (e) => {
            // Don't close when the click originated inside the shortcuts
            // box itself (the box sits inside the same overlay element).
            if (e.target.closest(".shortcuts-box") && e.currentTarget.id === "shortcuts-modal") return;
            toggleShortcuts(false);
        });
    });

    // The one persistent close button (lives at body level, see index.html.j2)
    // closes whichever overlay is currently open.
    const globalCloseBtn = document.getElementById("global-close-btn");
    if (globalCloseBtn) {
        globalCloseBtn.addEventListener("click", () => {
            const detail = document.getElementById("detail-view");
            if (detail && detail.classList.contains("modal-open")) {
                closeCategory();
            } else {
                toggleShortcuts(false);
            }
        });
    }

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

    // ---------- Image lightbox ----------
    // Scoped to .media-placeholder img specifically — that's every real
    // content photo on the site (domain/highlight/archive thumbnails,
    // the Mediterranean Cup gallery, the chess portraits), and nothing
    // else (chessboard pieces, icons, etc. live outside that wrapper).
    const lightbox = document.getElementById("lightbox");
    const lightboxImg = document.getElementById("lightbox-img");

    function openLightbox(imgEl) {
        if (!lightbox || !lightboxImg) return;
        lightboxImg.src = imgEl.currentSrc || imgEl.src;
        lightboxImg.alt = imgEl.alt || "";
        lightbox.classList.add("lightbox-open");
        lockBodyScroll();
    }
    function closeLightbox() {
        if (!lightbox) return;
        lightbox.classList.remove("lightbox-open");
        unlockBodyScroll();
    }

    document.addEventListener("click", (e) => {
        const img = e.target.closest(".media-placeholder img");
        if (img) {
            // Stop the click from also bubbling up to a card's own
            // click-to-open-detail handler — clicking the photo itself
            // should open the photo, not the card behind it.
            e.stopPropagation();
            openLightbox(img);
        }
    }, true);

    document.querySelectorAll('[data-action="close-lightbox"]').forEach((el) => {
        el.addEventListener("click", (e) => {
            if (e.target === el) closeLightbox();
        });
    });

    // ---------- Reveal tiles (placeholder galleries + puzzle widget) ----------
    function toggleReveal(tile) {
        const expanded = tile.classList.toggle("expanded");
        tile.setAttribute("aria-expanded", String(expanded));
    }
    document.addEventListener("click", (e) => {
        const tile = e.target.closest(".reveal-tile");
        if (tile) toggleReveal(tile);
    });
    document.addEventListener("keydown", (e) => {
        if ((e.key === "Enter" || e.key === " ") && e.target.classList && e.target.classList.contains("reveal-tile")) {
            e.preventDefault();
            toggleReveal(e.target);
        }
    });

    // ---------- Violin tone ----------
    document.querySelectorAll('[data-action="play-violin"]').forEach((btn) => {
        btn.addEventListener("click", () => {
            playViolinTone();
            btn.classList.add("pulse");
            setTimeout(() => btn.classList.remove("pulse"), 400);
        });
    });
})();
