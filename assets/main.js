// Kabir Bhuchar portfolio — all interactivity, plain JS.
// Content for the detail modal is embedded by build.py as JSON
// (see the #categories-data script tag) so nothing here needs a
// Python runtime in the browser.

(function () {
    "use strict";

    const categories = JSON.parse(document.getElementById("categories-data").textContent);
    let lastOpenedCardId = null;

    const isEditableTarget = (target) =>
        target instanceof Element && target.closest("input, textarea, [contenteditable]");
    ["contextmenu", "selectstart", "copy", "cut", "dragstart"].forEach((eventName) => {
        document.addEventListener(eventName, (event) => {
            if (!isEditableTarget(event.target)) event.preventDefault();
        });
    });

    // ---------- Sound effects (lazy AudioContext) ----------
    // The AudioContext is created on first interaction rather than at load,
    // so the browser never has to warn about (or silently ignore) an
    // AudioContext started before any user gesture. No in-page mute toggle
    // here — every browser already has a native per-tab mute for this.
    let audioCtx = null;
    function getAudioCtx() {
        if (!audioCtx) {
            const Ctor = window.AudioContext || window.webkitAudioContext;
            audioCtx = new Ctor();
        }
        if (audioCtx.state === "suspended") audioCtx.resume();
        return audioCtx;
    }

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
        try {
            playTone(freq, type, duration, getAudioCtx().currentTime, gainPeak);
        } catch (e) { /* audio is a nice-to-have, never block on it */ }
    }

    function playChime(freqs, type = "sine", noteDuration = 0.16, gainPeak = 0.03) {
        try {
            const ctx = getAudioCtx();
            freqs.forEach((freq, i) => {
                playTone(freq, type, noteDuration, ctx.currentTime + i * (noteDuration * 0.6), gainPeak);
            });
        } catch (e) { /* ditto */ }
    }

    function playModalOpenSound() { playChime([440, 660], "sine", 0.09, 0.02); }
    function playModalCloseSound() { playChime([660, 440], "sine", 0.09, 0.02); }

    // Hover sound: only on the "big" clickable surfaces (cards/nav), not
    // every tiny link or button — constant beeping on every element was
    // the main complaint. Uses mouseover/mouseout (which bubble) with a
    // relatedTarget check so moving between nested children of the same
    // card doesn't retrigger the sound.
    const HOVER_SOUND_SELECTOR = ".pro-card, .standard-card, .highlight-card, .connect-card, .nav-tab, .reveal-tile, .bento-tile-link";
    const CLICK_SOUND_SELECTOR = HOVER_SOUND_SELECTOR + ", .interactive-btn, .card-action-btn, .filter-tab";

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
    // Shared with search.js, which is a separate script and needs the
    // same reference-counted lock rather than its own independent one.
    window.lockBodyScroll = lockBodyScroll;
    window.unlockBodyScroll = unlockBodyScroll;

    // ---------- Haptics ----------
    // Very short, subtle pulses on a handful of meaningful interactions
    // (opening/closing a card, an image, or switching tabs) — not on
    // every hover or small tap. Vibration API support varies (notably
    // absent on iOS Safari), so this silently does nothing where it's
    // unsupported rather than trying to work around that.
    function hapticTick(duration = 10) {
        if (navigator.vibrate) {
            try { navigator.vibrate(duration); } catch (e) { /* ignore */ }
        }
    }

    // ---------- Tabs ----------
    // Scoped to [data-target] specifically, since not every element
    // sharing the .nav-tab look is a page-switching tab.
    const navTabs = document.querySelectorAll(".nav-tab[data-target]");
    const tabContents = document.querySelectorAll(".tab-content");

    function showTab(id, { scrollTop = true } = {}) {
        const targetView = document.getElementById(id);
        const targetTab = Array.from(navTabs).find((tab) => tab.getAttribute("data-target") === id);
        if (!targetView || !targetTab) return false;

        navTabs.forEach((tab) => tab.classList.remove("active"));
        tabContents.forEach((tab) => tab.classList.remove("active-view"));
        targetTab.classList.add("active");
        targetView.classList.add("active-view");
        if (scrollTop) window.scrollTo({ top: 0, behavior: "smooth" });
        return true;
    }
    window.showTab = showTab;

    navTabs.forEach((tab) => {
        tab.addEventListener("click", () => {
            hapticTick();
            showTab(tab.getAttribute("data-target"));
        });
    });

    // ---------- Connect section: filterable infinite carousel ----------
    const connectTrack = document.querySelector(".connect-track");
    const connectSection = document.querySelector(".connect-section");
    const connectCards = Array.from(document.querySelectorAll(".connect-card"));
    const filterTabs = Array.from(document.querySelectorAll(".filter-tab"));
    const CAROUSEL_DELAY = 4000;
    let carouselInterval = null;
    let matchingCards = connectCards;
    let trackCards = [];
    let currentIndex = 0;
    let resizeTimer = null;
    let dragStart = null;
    let dragged = false;

    function isAnyModalOpen() {
        return Boolean(
            document.getElementById("detail-view")?.classList.contains("modal-open") ||
            document.getElementById("lightbox")?.classList.contains("lightbox-open") ||
            document.getElementById("assistant-panel")?.classList.contains("assistant-open") ||
            document.getElementById("shortcuts-modal")?.style.display === "flex"
        );
    }

    function centerCard(index, withoutTransition = false) {
        if (!connectTrack || !trackCards[index]) return;
        const card = trackCards[index];
        currentIndex = index;
        trackCards.forEach((item, i) => item.classList.toggle("active", i === index));
        if (withoutTransition) connectTrack.style.transition = "none";
        const x = window.innerWidth / 2 - (card.offsetLeft + card.offsetWidth / 2);
        connectTrack.style.transform = `translateX(${x}px)`;
        if (withoutTransition) {
            void connectTrack.offsetHeight;
            connectTrack.style.transition = "";
        }
    }

    function cloneCard(card) {
        const clone = card.cloneNode(true);
        clone.classList.remove("active");
        clone.setAttribute("aria-hidden", "true");
        clone.tabIndex = -1;
        clone.querySelectorAll("a, button, input, select, textarea, [tabindex]").forEach((item) => {
            item.tabIndex = -1;
        });
        return clone;
    }

    function rebuildCarousel(category) {
        if (!connectTrack) return;
        matchingCards = connectCards.filter((card) =>
            category === "all" || card.getAttribute("data-category") === category
        );
        const fragment = document.createDocumentFragment();
        if (matchingCards.length > 1) {
            matchingCards.forEach((card) => fragment.appendChild(cloneCard(card)));
            matchingCards.forEach((card) => fragment.appendChild(card));
            matchingCards.forEach((card) => fragment.appendChild(cloneCard(card)));
            currentIndex = matchingCards.length;
        } else {
            matchingCards.forEach((card) => fragment.appendChild(card));
            currentIndex = 0;
        }
        connectTrack.replaceChildren(fragment);
        trackCards = Array.from(connectTrack.querySelectorAll(".connect-card"));
        centerCard(currentIndex, true);
    }

    function normalizeLoopIndex() {
        if (matchingCards.length < 2) return;
        const middleStart = matchingCards.length;
        const middleEnd = middleStart * 2 - 1;
        if (currentIndex < middleStart) {
            centerCard(currentIndex + matchingCards.length, true);
        } else if (currentIndex > middleEnd) {
            centerCard(currentIndex - matchingCards.length, true);
        }
    }

    function stepCarousel(delta, manual = true) {
        if (!connectTrack || matchingCards.length < 2) return;
        if (manual) hapticTick();
        centerCard(currentIndex + delta);
        if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) normalizeLoopIndex();
        if (manual) resetCarouselTimer();
    }

    function startCarousel() {
        if (carouselInterval) clearInterval(carouselInterval);
        carouselInterval = setInterval(() => {
            if (
                document.hidden ||
                isAnyModalOpen() ||
                window.matchMedia("(prefers-reduced-motion: reduce)").matches ||
                connectTrack?.matches(":hover")
            ) return;
            stepCarousel(1, false);
        }, CAROUSEL_DELAY);
    }

    function resetCarouselTimer() {
        startCarousel();
    }

    if (connectTrack) {
        connectTrack.addEventListener("transitionend", (event) => {
            if (event.target === connectTrack && event.propertyName === "transform") normalizeLoopIndex();
        });
        connectTrack.addEventListener("pointerdown", (event) => {
            dragStart = { x: event.clientX, y: event.clientY };
            dragged = false;
        });
        connectTrack.addEventListener("pointerup", (event) => {
            if (!dragStart) return;
            const deltaX = event.clientX - dragStart.x;
            const deltaY = event.clientY - dragStart.y;
            if (Math.abs(deltaX) > 40 && Math.abs(deltaX) > Math.abs(deltaY)) {
                dragged = true;
                stepCarousel(deltaX < 0 ? 1 : -1);
                setTimeout(() => { dragged = false; }, 0);
            }
            dragStart = null;
        });
        connectTrack.addEventListener("pointercancel", () => { dragStart = null; });
        connectTrack.addEventListener("click", (event) => {
            if (!dragged) return;
            event.preventDefault();
            event.stopPropagation();
            dragged = false;
        });
    }

    filterTabs.forEach((tab) => {
        tab.addEventListener("click", () => {
            hapticTick();
            const category = tab.getAttribute("data-category");
            filterTabs.forEach((item) => {
                item.classList.remove("active");
                item.setAttribute("aria-pressed", "false");
            });
            tab.classList.add("active");
            tab.setAttribute("aria-pressed", "true");
            rebuildCarousel(category);
            resetCarouselTimer();
        });
        tab.addEventListener("keydown", (event) => {
            if (event.key !== "ArrowLeft" && event.key !== "ArrowRight") return;
            event.preventDefault();
            const index = filterTabs.indexOf(tab);
            const next = event.key === "ArrowRight"
                ? (index + 1) % filterTabs.length
                : (index - 1 + filterTabs.length) % filterTabs.length;
            filterTabs[next].focus();
            filterTabs[next].click();
        });
    });

    document.addEventListener("keydown", (event) => {
        if (event.key !== "ArrowLeft" && event.key !== "ArrowRight") return;
        if (event.defaultPrevented || event.target.closest?.(".filter-tab")) return;
        if (!document.querySelector('.nav-tab.active[data-target="tab-overview"]')) return;
        if (isAnyModalOpen() || /^(INPUT|TEXTAREA)$/.test(document.activeElement?.tagName || "")) return;
        const bounds = connectSection?.getBoundingClientRect();
        if (!bounds || bounds.bottom <= 0 || bounds.top >= window.innerHeight) return;
        event.preventDefault();
        stepCarousel(event.key === "ArrowRight" ? 1 : -1);
    });

    window.addEventListener("resize", () => {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(() => centerCard(currentIndex, true), 120);
    });

    if (connectTrack) {
        rebuildCarousel("all");
        startCarousel();
    }

    // ---------- Detail modal ----------
    function openCategory(card) {
        const catId = card.id;
        const item = categories[catId];
        if (!item) return;

        hapticTick();
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
    window.openCategoryById = (catId) => {
        const card = document.getElementById(catId);
        if (!card || !categories[catId]) return false;
        openCategory(card);
        return true;
    };

    function closeCategory() {
        const detail = document.getElementById("detail-view");
        hapticTick();
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
            const lightboxOpen = lightbox && lightbox.classList.contains("lightbox-open");
            const detail = document.getElementById("detail-view");
            if (window.closeAssistant && window.closeAssistant()) {
                // handled
            } else if (lightboxOpen) {
                closeLightbox();
            } else if (window.closeChessBoardFullscreen && window.closeChessBoardFullscreen()) {
                // handled
            } else if (detail && detail.classList.contains("modal-open")) {
                closeCategory();
            } else {
                toggleShortcuts(false);
            }
        }
        if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
            e.preventDefault();
            showTab("tab-search");
            const searchInput = document.getElementById("search-input");
            if (searchInput) {
                searchInput.focus();
                searchInput.select();
            }
        }
        if (lightbox && lightbox.classList.contains("lightbox-open")) {
            if (e.key === "ArrowLeft") stepLightbox(-1);
            if (e.key === "ArrowRight") stepLightbox(1);
        }
        if (e.key === "?") {
            e.preventDefault();
            const modal = document.getElementById("shortcuts-modal");
            toggleShortcuts(modal.style.display !== "flex");
        }
        const activeElement = document.activeElement;
        const editingText = activeElement?.matches?.("input, textarea, [contenteditable='true']");
        if (["1", "2", "3", "4", "5"].includes(e.key) &&
            !document.body.classList.contains("modal-active") && !editingText) {
            const index = parseInt(e.key, 10) - 1;
            if (navTabs[index]) navTabs[index].click();
        }
    });

    // ---------- Image/video lightbox ----------
    // Scoped to .media-placeholder img/video specifically — that's every
    // real content photo or clip on the site (thumbnails, galleries, the
    // chess portraits, the basketball clips), and nothing else
    // (chessboard pieces, icons, etc. live outside that wrapper).
    const lightbox = document.getElementById("lightbox");
    const lightboxImg = document.getElementById("lightbox-img");
    const lightboxVideo = document.getElementById("lightbox-video");
    const lightboxPrevBtn = document.querySelector(".lightbox-prev");
    const lightboxNextBtn = document.querySelector(".lightbox-next");

    let lightboxGallery = [];
    let lightboxIndex = 0;

    function showLightboxMedia(mediaEl) {
        if (mediaEl.tagName === "VIDEO") {
            lightboxVideo.src = mediaEl.currentSrc || mediaEl.querySelector("source")?.src || mediaEl.src;
            lightboxVideo.classList.add("lightbox-active");
            lightboxImg.classList.remove("lightbox-active");
            lightboxVideo.currentTime = 0;
            lightboxVideo.play().catch(() => { /* autoplay-with-sound can be blocked; controls still work */ });
        } else {
            lightboxVideo.pause();
            lightboxVideo.removeAttribute("src");
            lightboxImg.src = mediaEl.currentSrc || mediaEl.src;
            lightboxImg.alt = mediaEl.alt || "";
            lightboxImg.classList.add("lightbox-active");
            lightboxVideo.classList.remove("lightbox-active");
        }
    }

    function openLightbox(mediaEl) {
        if (!lightbox) return;
        hapticTick();

        // The gallery is every photo/video inside the same card's detail
        // content (so arrows step through, say, the Mediterranean Cup
        // gallery) — or just this one item if it's not inside a card
        // (e.g. a domain-card thumbnail on the Domains tab).
        const scope = mediaEl.closest("#detail-content") || mediaEl.closest(".media-placeholder");
        lightboxGallery = scope
            ? Array.from(scope.querySelectorAll(".media-placeholder img, .media-placeholder video"))
            : [mediaEl];
        lightboxIndex = Math.max(0, lightboxGallery.indexOf(mediaEl));

        const showArrows = lightboxGallery.length > 1;
        if (lightboxPrevBtn) lightboxPrevBtn.hidden = !showArrows;
        if (lightboxNextBtn) lightboxNextBtn.hidden = !showArrows;

        showLightboxMedia(mediaEl);
        lightbox.classList.add("lightbox-open");
        lockBodyScroll();
    }

    function stepLightbox(delta) {
        if (lightboxGallery.length < 2) return;
        hapticTick();
        lightboxIndex = (lightboxIndex + delta + lightboxGallery.length) % lightboxGallery.length;
        showLightboxMedia(lightboxGallery[lightboxIndex]);
    }

    function closeLightbox() {
        if (!lightbox) return;
        hapticTick();
        lightbox.classList.remove("lightbox-open");
        lightboxVideo.pause();
        lightboxVideo.removeAttribute("src");
        lightboxVideo.load();
        unlockBodyScroll();
    }

    document.addEventListener("click", (e) => {
        const media = e.target.closest(".media-placeholder img, .media-placeholder video");
        if (media) {
            // Stop the click from also bubbling up to a card's own
            // click-to-open-detail handler — clicking the photo/video
            // itself should open it, not the card behind it.
            e.stopPropagation();
            openLightbox(media);
        }
    }, true);

    document.querySelectorAll('[data-action="close-lightbox"]').forEach((el) => {
        el.addEventListener("click", (e) => {
            if (e.target === el) closeLightbox();
        });
    });
    document.querySelectorAll('[data-action="lightbox-prev"]').forEach((el) => {
        el.addEventListener("click", () => stepLightbox(-1));
    });
    document.querySelectorAll('[data-action="lightbox-next"]').forEach((el) => {
        el.addEventListener("click", () => stepLightbox(1));
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
})();