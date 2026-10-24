"""
All editable content for Kabir Bhuchar's portfolio.

This is the ONLY file you should need to touch to change text, links,
stats, or project details. Structure/styling live in templates/ and
assets/. After editing this file, run:

    python build.py

...to regenerate index.html.
"""

from html import escape

import bento

SITE = {
    "title": "Kabir Bhuchar",
    "description": "Kabir Bhuchar's portfolio as a chess player, programmer, basketballer, violinist.",
    "url": "https://aajukubaa.github.io/",
    "og_image": "med-cup-photos/DSC09519.JPG",
    "favicon": "images/Favicon.png",
    # Not wired into any page yet — stored here so it's ready whenever
    # you want it placed (nav bar, footer, etc.).
    "logo": "images/Logo.png",
}

NAV_TABS = [
    {"id": "tab-overview", "label": "Overview",
     "icon": '<svg viewBox="0 0 24 24" width="1em" height="1em" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="m3 10 9-7 9 7"/><path d="M5 9v12h14V9M9 21v-7h6v7"/></svg>'},
    {"id": "tab-domains", "label": "Domains",
     "icon": '<svg viewBox="0 0 24 24" width="1em" height="1em" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg>'},
    {"id": "tab-projects", "label": "Projects",
     "icon": '<svg viewBox="0 0 24 24" width="1em" height="1em" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h5l2 2h7a2 2 0 0 1 2 2v10H3z"/><path d="M3 10h18"/></svg>'},
    {"id": "tab-archive", "label": "Archive",
     "icon": '<svg viewBox="0 0 24 24" width="1em" height="1em" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 4h18v5H3z"/><path d="M5 9v11h14V9M10 13h4"/></svg>'},
]

HERO = {
    "lines": ["Kabir", "Bhuchar"],
    "intro": "Competitive chess strategist, basketball forward, Python architect, "
             "and classical violinist. Welcome to my digital control center.",
}

SPECS = [
    {"value": "1545", "label": "FIDE Rating"},
    {"value": "182 cm", "label": "Basketball Forward"},
    {"value": "Book 3", "label": "Suzuki Violin"},
    {"value": "Python 3.12", "label": "Engine Architecture"},
]

CONNECT_LINKS = [
    # Chess category
    {"icon": "♟️", "name": "FIDE Profile", "desc": "Official 1545 tournament records",
     "url": "http://ratings.fide.com/profile/498777", "category": "chess"},
    {"icon": "♘", "name": "Chess.com", "desc": "Blitz & rapid online matches",
     "url": "https://www.chess.com/member/aajukubaa", "category": "chess"},
    {"icon": "♞", "name": "Lichess", "desc": "Bullet & puzzle training",
     "url": "https://lichess.org/@/onesandzeros", "category": "chess"},
    # Coding/Tech category
    {"icon": "💻", "name": "GitHub", "desc": "Python repositories & micro-apps",
     "url": "https://github.com/aajukubaa", "category": "coding"},
    {"icon": "⚡", "name": "Replit", "desc": "Live Python code execution",
     "url": "https://replit.com/@Aajukubaa", "category": "coding"},
    # Music/Sports category
    {"icon": "▶️", "name": "YouTube", "desc": "Video edits & athletic highlights",
     "url": "https://www.youtube.com/@Aajukubaa", "category": "music-sports"},
    # Socials category
    {"icon": "✍️", "name": "Medium", "desc": "Articles and analytical logs",
     "url": "https://aajukubaa.medium.com/", "category": "socials"},
    {"icon": "🦉", "name": "Duolingo", "desc": "Daily streak & language stats",
     "url": "https://www.duolingo.com/profile/Aajukubaa", "category": "socials"},
    {"icon": "🏷️", "name": "Vinted", "desc": "Curated style storefront",
     "url": "https://www.vinted.co.uk/member/284456392", "category": "socials"},
    {"icon": "🏺", "name": "Pottery by RG", "desc": "Handmade ceramic works",
     "url": "https://www.etsy.com/uk/shop/PotterybyRG", "category": "socials"},
    {"icon": "✉️", "name": "Gmail", "desc": "kabirbhuchar@gmail.com",
     "url": "mailto:kabirbhuchar@gmail.com", "category": "socials"},
]

# Order + display labels for the connect-section category filter tabs.
# "All" shows every link regardless of category.
CONNECT_CATEGORY_ORDER = [
    ("all", "All"),
    ("chess", "Chess"),
    ("coding", "Coding/Tech"),
    ("music-sports", "Music/Sports"),
    ("socials", "Socials"),
]

# "category" ties a card to its full-screen detail view in CATEGORIES below.
DOMAIN_CARDS = [
    {"category": "chess", "pill": "Strategy", "title": "Chess", "image": None,
     "preview": "1545 FIDE tournament rating specializing in sharp tactical combat "
                "and aggressive 1.e4 openings."},
    {"category": "basketball", "pill": "Athletics", "title": "Basketball",
     "image": {"id": "basketball-image", "src": "med-cup-photos/DSC09520.JPG",
               "alt": "Basketball action"},
     "preview": "6'0\" Forward dominating paint defense, rim protection, "
                "and high-intensity rebounding."},
    {"category": "coding", "pill": "Engineering", "title": "Coding", "image": None,
     "preview": "Building automated Python backends, web micro-apps, "
                "and deploying to GitHub Pages."},
    {"category": "music", "pill": "Performance", "title": "Music", "image": None,
     "preview": "Advanced classical violin performance executing rigorous "
                "Suzuki Book 3 repertoire."},
]

HIGHLIGHT_PROJECTS = [
    {"category": "proj_basketball", "pill": "Leadership & Athletics",
     "title": "The Mediterranean Cup",
     "desc": "Captaining the team through a high-stakes basketball tournament. "
             "Required on-court leadership and paint dominance.",
     "cta": "View Tournament Details",
     "image": {"id": "mediterranean-image", "src": "med-cup-photos/DSC09521.JPG",
               "alt": "Mediterranean Cup Action"}},
    {"category": "proj_website", "pill": "Full-Stack Development",
     "title": "Engineering This Showcase",
     "desc": "The technical breakdown of building this portfolio with a Python "
             "static-site generator, compiled into fast, dependency-free HTML/CSS/JS.",
     "cta": "View Architecture",
     "image": None},
    {"category": "proj_chess", "pill": "Competitive Strategy",
     "title": "Chess: School & Circuit",
     "desc": "Representing the school team with top-board performance, securing "
             "the Best Player award, and competing in external circuits.",
     "cta": "View Match Analysis",
     "image": None},
]

CREATIVE_ARCHIVE = [
    {"category": "presentations", "pill": "Keynote Decks", "title": "PowerPoint Presentations",
     "image": None,
     "desc": "Dynamic visual slide decks engineered with minimalist layouts.",
     "cta": "View Presentations"},
    {"category": "portfolios", "pill": "Creative Showcase", "title": "Design Portfolios",
     "image": None,
     "desc": "Curated archive of 9+ comprehensive design project portfolios.",
     "cta": "View Design Work"},
]

# All 29 Mediterranean Cup photos (the original, uncompressed replacement
# set — authoritative list as of the images/ folder reorg). Most of the
# site's photo content lives on the Mediterranean Cup project's own detail
# page (see CATEGORIES["proj_basketball"] below) — a handful are reused on
# the Basketball domain card/category too, since that's the same
# tournament. Everything else (chess, coding, music, presentations,
# portfolios, projects, proj_website, proj_chess) doesn't have matching
# photos, so those show an honest "Photo coming soon" box instead of a
# mismatched basketball shot.
MEDITERRANEAN_CUP_PHOTOS = [
    "DSC09519.JPG", "DSC09520.JPG", "DSC09521.JPG", "DSC09540.JPG", "DSC09542.JPG",
    "DSC09543.JPG", "DSC09545.JPG", "DSC09547.JPG", "DSC09561.JPG", "DSC09585.JPG",
    "DSC09586.JPG", "DSC09587.JPG", "DSC09588.JPG", "DSC09589.JPG", "DSC09590.JPG",
    "DSC09597.JPG", "DSC09603.JPG", "DSC09615.JPG", "DSC09714.JPG", "DSC09715.JPG",
    "DSC09716.JPG", "DSC09717.JPG", "DSC09729.JPG", "DSC09732.JPG", "DSC09736.JPG",
    "DSC09737.JPG", "DSC09741.JPG", "DSC09743.JPG", "DSC09744.JPG",
]

# A handful of these are woven directly into the Mediterranean Cup
# narrative below (see CATEGORIES["proj_basketball"]); everything else
# stays in the tournament gallery grid at the end of that page.
_MED_CUP_INLINE_PHOTOS = [
    "DSC09519.JPG", "DSC09540.JPG", "DSC09543.JPG", "DSC09585.JPG",
    "DSC09603.JPG", "DSC09714.JPG", "DSC09732.JPG", "DSC09744.JPG",
]
_MED_CUP_GRID_PHOTOS = [p for p in MEDITERRANEAN_CUP_PHOTOS if p not in _MED_CUP_INLINE_PHOTOS]


def _med_cup_photo_html(name, i):
    return (f'<div class="media-placeholder"><img src="med-cup-photos/{name}" '
            f'alt="Mediterranean Cup — photo {i}" loading="lazy"></div>')


_MED_CUP_GALLERY_HTML = "\n".join(
    "                    " + _med_cup_photo_html(name, i)
    for i, name in enumerate(_MED_CUP_GRID_PHOTOS, start=1)
)

_PHOTO_COMING_SOON = '<div class="media-placeholder">Photo coming soon</div>'


def _account_tile(link_name, size="sm"):
    """Create one clickable bento tile for a CONNECT_LINKS entry."""
    link = next(l for l in CONNECT_LINKS if l["name"] == link_name)
    return bento.tile(
        size,
        f'<h4>{link["icon"]} {link["name"]}</h4><p>{link["desc"]}</p>'
        '<span class="bento-link-arrow">↗</span>',
        href=link["url"],
    )


# Add a Chess.com game ID from Share → Embed → the number in
# https://www.chess.com/emboard?id=XXXX.
CHESS_EMBED_GAMES = [
    {"title": "Game 1", "embed_id": None},
    {"title": "Game 2", "embed_id": None},
    {"title": "Game 3", "embed_id": None},
    {"title": "Game 4", "embed_id": None},
    {"title": "Game 5", "embed_id": None},
]


def _chess_featured_games_html():
    games = []
    for game in CHESS_EMBED_GAMES:
        title = escape(str(game["title"]), quote=True)
        embed_id = game["embed_id"]
        if embed_id is not None and str(embed_id).isdigit():
            games.append(
                f'<iframe src="https://www.chess.com/emboard?id={escape(str(embed_id), quote=True)}" '
                f'loading="lazy" allowtransparency="true" frameborder="0" '
                f'style="width:100%;border:none;" title="{title}"></iframe>'
            )
        else:
            games.append(
                f'<div class="chess-game-placeholder">♟ {title} — Chess.com embed coming soon</div>'
            )
    return (
        '<section class="chess-featured-games"><h4>Featured Games</h4>'
        '<div class="chess-game-grid">' + "".join(games) + "</div></section>"
    )


def _reveal_grid(items):
    """Render a grid of click-to-expand tiles (used for the temporary
    presentation/portfolio placeholders below). Each item needs a
    "title" and "description"."""
    tiles = "\n".join(
        f'''                    <div class="reveal-tile" tabindex="0" role="button" aria-expanded="false">
                        <div class="reveal-tile-header">
                            <span class="reveal-tile-title">{item["title"]}</span>
                            <span class="reveal-tile-icon">+</span>
                        </div>
                        <div class="reveal-tile-body">
                            <p>{item["description"]}</p>
                        </div>
                    </div>'''
        for item in items
    )
    return f'<div class="reveal-grid">\n{tiles}\n                    </div>'


# Temporary placeholders — titles/descriptions are generic until you send
# the real ones. Easy to replace: just edit the "title"/"description"
# text below (and add a "url" key + link once each one is uploaded
# somewhere, which the reveal tile isn't wired to yet).
PRESENTATIONS_LIST = [
    {"title": "Presentation 1", "description": "Title and summary coming soon."},
    {"title": "Presentation 2", "description": "Title and summary coming soon."},
]

PORTFOLIOS_LIST = [
    {"title": "Grade 6 Portfolio 1", "description": "Title and summary coming soon."},
    {"title": "Grade 6 Portfolio 2", "description": "Title and summary coming soon."},
    {"title": "Grade 6 Portfolio 3", "description": "Title and summary coming soon."},
    {"title": "Grade 7 Portfolio 1", "description": "Title and summary coming soon."},
    {"title": "Grade 7 Portfolio 2", "description": "Title and summary coming soon."},
    {"title": "Grade 7 Portfolio 3", "description": "Title and summary coming soon."},
    {"title": "Grade 8 Portfolio 1", "description": "Title and summary coming soon."},
    {"title": "Grade 8 Portfolio 2", "description": "Title and summary coming soon."},
    {"title": "Grade 8 Portfolio 3", "description": "Title and summary coming soon."},
]

_PRESENTATIONS_GALLERY_HTML = _reveal_grid(PRESENTATIONS_LIST)
_PORTFOLIOS_GALLERY_HTML = _reveal_grid(PORTFOLIOS_LIST)

# Codingal certificates — PDFs are rendered to JPGs at build time by
# render_certificates.py (browsers can't display a raw PDF as an <img>),
# using a slugified version of each PDF's filename.
CERTIFICATES = [
    {"file": "python-programmer-certificate.jpg", "name": "Python Programmer"},
    {"file": "advance-python-developer-certificate.jpg", "name": "Advance Python Developer"},
    {"file": "python-game-developer-certificate.jpg", "name": "Python Game Developer"},
    {"file": "sql-developer-certificate.jpg", "name": "SQL Developer"},
]
_CERTIFICATES_HTML = "\n".join(
    f'''                    <figure class="certificate-item">
                        <div class="media-placeholder certificate-frame"><img src="certificates/{c["file"]}" alt="{c["name"]} certificate" loading="lazy"></div>
                        <figcaption>{c["name"]}</figcaption>
                    </figure>'''
    for c in CERTIFICATES
)
_CERTIFICATES_GRID_HTML = f'<div class="certificate-grid">\n{_CERTIFICATES_HTML}\n                    </div>'

# Codingal progress reports, in the given order.
PROGRESS_REPORT_URLS = [
    "https://www.codingal.com/progress-reports/BF1vi6eL/",
    "https://www.codingal.com/progress-reports/7spnyHqv/",
    "https://www.codingal.com/progress-reports/ZJ9DEg33/",
    "https://www.codingal.com/progress-reports/hYlhSUfp/",
    "https://www.codingal.com/progress-reports/X8CeIftK/",
    "https://www.codingal.com/progress-reports/LHAmYr9y/",
    "https://www.codingal.com/progress-reports/jzQQUOGS/",
    "https://www.codingal.com/progress-reports/p3mclR2g/",
    "https://www.codingal.com/progress-reports/hTEKhhR0/",
    "https://www.codingal.com/progress-reports/7hj2i3NV/",
]
PROGRESS_REPORT_NAMES = [
    "Python Basics",
    "Let's Begin with Loops",
    "Python Functions and Modules",
    "Data Structures in Python",
    "Object Oriented Programming",
    "Game Building with Pygame",
    "GUI using Python Tkinter",
    "Welcome to Data Science",
    "SQL",
    "SQL using Python II",
]
_PROGRESS_REPORTS_HTML = "\n".join(
    f'''                    <a href="{url}" target="_blank" class="progress-report-row">
                        <span class="progress-report-number">{i}</span>
                        <span class="progress-report-label">{name}</span>
                        <span class="progress-report-arrow">↗</span>
                    </a>'''
    for i, (url, name) in enumerate(zip(PROGRESS_REPORT_URLS, PROGRESS_REPORT_NAMES), start=1)
)
_PROGRESS_REPORTS_LIST_HTML = f'<div class="progress-reports-list">\n{_PROGRESS_REPORTS_HTML}\n                    </div>'

GOALS = [
    {"emoji": "♟️", "title": "FIDE Rating Target: 1800", "current": "1545",
     "target": "1800", "percent": 85},
    {"emoji": "🎻", "title": "Suzuki Violin Goal: Reach Book 5", "current": "Book 3",
     "target": "Book 5", "percent": 60},
    {"emoji": "🎻", "title": "Trinity Grade 3 Exam", "current": "In progress",
     "target": "Pass Grade 3", "percent": 15},
]


def _goal_bar_html(goal):
    """Render one GOALS entry as the same progress-bar card that used to
    live in the (now-removed) Now & Goals tab — now embedded directly in
    the relevant domain card's detail content instead."""
    return f'''<div class="goal-bar-card">
                        <div class="goal-bar-header">
                            <span class="goal-title">{goal["emoji"]} {goal["title"]}</span>
                            <span class="goal-metric">Current: {goal["current"]} / Target: {goal["target"]}</span>
                        </div>
                        <div class="progress-track">
                            <div class="progress-fill" style="width: {goal["percent"]}%;"></div>
                        </div>
                    </div>'''


NOW = "Making this website..."

# Full detail-view content for every clickable card. Keys match the
# "category" fields above. Bento tiles use the validated helpers in
# bento.py; longer-form content remains HTML for the detail modal.
CATEGORIES = {
    "chess": {
        "title": "CHESS",
        "badge": "STRATEGY",
        "bento": [
        bento.tile('wide', '\n                        <h4>Current Rating</h4>\n                        <h2>1545 FIDE</h2>\n                        <p style="margin-top:auto;">Official competitive tournament bracket rating.</p>\n                    '),
        bento.tile('wide', '\n                        <h4 style="color: #ffffff;">Opening Base</h4>\n                        <h2 style="font-size: 5rem; margin-top:20px;">1.e4</h2>\n                    ', style='background: #1c1c22; border-color: #44444d;'),
        bento.tile('wide', '\n                        <h4>Playstyle</h4>\n                        <p style="color:#fff; font-size:1.1rem; font-weight:600; margin-top:10px;">Aggressive & Direct</p>\n                    '),
        bento.tile('wide', '\n                        <h4>Time Controls</h4>\n                        <p style="color:#fff; font-size:1.1rem; font-weight:600; margin-top:10px;">60+1 Hyper-Bullet & 3-Min Blitz</p>\n                    '),
        bento.tile('wide', '\n                        <h4>Black Defenses</h4>\n                        <p>Sicilian (1...c5)<br>Scandinavian (1...d5)</p>\n                    '),
        bento.tile('wide', '\n                        <h4>Tactical Streak</h4>\n                        <p style="color:#fff; font-weight:600;">2800+ Puzzle Peak</p>\n                    '),
        bento.tile('wide', '\n                        <h4>Club Standing</h4>\n                        <p style="color:#fff; font-weight:600;">Top Board Representative & School Team MVP</p>\n                    '),
        _account_tile('FIDE Profile', size='wide'),
        _account_tile('Chess.com', size='wide'),
        _account_tile('Lichess', size='wide'),
    ],
        "content": """
                    <div class="content-block">
                        <p class="lead-paragraph">My game is defined by high-octane, uncompromising, and direct aggression. Whenever I sit down with the White pieces, I strictly initiate the batt[...]
                    </div>

                    <div class="content-block">
                        <h4>My Opening Repertoire & Philosophical Foundations</h4>
                        <p>My goal in the opening is rapid piece activation, immediate central dominance, and forcing my opponents out of their comfort zones right from move one:</p>
                        <ul>
                            <li><strong>Against 1...e5 (Italian Game):</strong> I steer directly into the sharp, classic lines of the Italian Game with 3. Bc4. From there, I love launching the It[...]
                            <li><strong>Against the French Defense (1...e6):</strong> I claim full central control using 2. d4 d5 3. Nc3 to set up active piece play, or I pivot into a King's Indi[...]
                            <li><strong>Against the Scandinavian Defense (1...d5):</strong> I accept the challenge immediately with 2. exd5 Qxd5, followed by 3. Nc3 to kick their queen with tempo[...]
                            <li><strong>Against the Caro-Kann Defense (1...c6):</strong> I refuse to let Black settle behind a quiet pawn wall, pushing 2. d4 d5 3. Nc3 to assert early space and m[...]
                        </ul>
                    </div>

                    <div class="media-placeholder chess-portrait"><img src="chess-photos/20250614_110030.jpg" alt="Kabir playing chess 1" loading="lazy"></div>

                    <div class="content-block">
                        <h4>Midgame Execution & Tactical DNA</h4>
                        <p>Once the opening transitions into the middlegame, my primary focus turns toward heavy pawn storms and direct, decisive assaults on the enemy king. When I secure a spati[...]
                    </div>

                    <div class="media-placeholder chess-portrait"><img src="chess-photos/20250614_111530.jpg" alt="Kabir playing chess 2" loading="lazy"></div>

                    <div class="content-block">
                        <h4>Endgame Strategy & Rating Progression</h4>
                        <p>If a match reaches the endgame, my approach shifts toward relentless pawn promotion and active king participation. I push passed pawns with urgency while marching my ki[...]
                        </div>

                    <div class="media-placeholder chess-portrait"><img src="chess-photos/20250614_120820.jpg" alt="Kabir playing chess 3" loading="lazy"></div>

                    <div class="content-block">
                        <p>This high-pressure playing identity has fueled my steady climb from sub-1000 levels up to a peak rating above 1451 Elo in longer rapid time controls. Along the way, I h[...]
                    </div>

                    <div class="media-placeholder chess-portrait"><img src="chess-photos/20250614_140223.jpg" alt="Kabir playing chess 4" loading="lazy"></div>

                    <div class="content-block">
                        <h4>Goal</h4>
                        """ + _goal_bar_html(GOALS[0]) + """
                    </div>

                    <div class="content-block">
                        <h4>Live Chess.com Dashboard</h4>
                        <div class="chess-widget">
                            <div class="chess-widget-header">
                                <span class="card-pill">Live from Chess.com</span>
                                <span id="chesscom-updated" class="chess-updated"></span>
                            </div>
                            <div id="chesscom-stats" class="chess-stats-grid">
                                <p class="chess-dashboard-loading">Loading live ratings…</p>
                            </div>
                            """ + _chess_featured_games_html() + """
                        </div>
                    </div>
                """,
    },
    "basketball": {
        "title": "BASKETBALL",
        "badge": "ATHLETICS",
        "bento": [
        bento.tile('wide', '\n                        <h4>Position</h4>\n                        <h2>6\'0" Forward</h2>\n                        <p style="margin-top:auto;">182 cm interior anchor.</p>\n                    '),
        bento.tile('wide', '\n                        <h4>Focus Areas</h4>\n                        <p style="color:#fff; font-size:1.1rem; font-weight:600; margin-top:10px;">Rim Protection & Box-outs</p>\n                    '),
        bento.tile('sm', '\n                        <h4>Rebounding</h4>\n                        <p style="color:#fff; font-weight:600;">High-Intensity Glass Control</p>\n                    '),
        bento.tile('sm', '\n                        <h4>Tournament</h4>\n                        <p style="color:#fff; font-weight:600;">Mediterranean Cup Captain</p>\n                    '),
        bento.tile('wide', '\n                        <h4>Court Vision</h4>\n                        <p style="color:#fff; font-weight:600;">High Post Passing & Screen Setting</p>\n                    '),
    ],
        "content": """
                    <div class="content-block">
                        <p class="lead-paragraph">At 6'0" playing forward, my game is built around mobile physical dominance, blending traditional low-post grit with face-up perimeter versatility.[...]
                    </div>

                    <div class="media-placeholder basketball-media"><img src="basketball-media/20260201_115535.jpg" alt="Basketball action" loading="lazy"></div>

                    <div class="content-block">
                        <h4>Offensive Arsenal: Post Touch & Face-Up Drives</h4>
                        <p>My scoring identity revolves around high-efficiency interior moves and capitalizing on mismatches when slower defenders guard me:</p>
                        <ul>
                            <li><strong>Low-Post Scoring & Soft Touch:</strong> I establish firm deep post position, using patient pump fakes, drop steps, and a soft turnaround hook shot over con[...]
                            <li><strong>Face-Up Dribble Attacks:</strong> I don't just stay stuck in the paint; I readily receive the ball at the top of the key or wing, put the ball on the deck,[...]
                            <li><strong>Glass Cleaning & Putbacks:</strong> On the offensive boards, I track flight paths relentlessly, carving out space to grab missed shots and cash in on immed[...]
                        </ul>
                    </div>

                    <div class="media-placeholder has-video basketball-media"><video src="basketball-media/20260201_115601.mp4" muted loop autoplay playsinline preload="metadata"></video></div>

                    <div class="content-block">
                        <h4>Defensive Anchor & Rim Protection</h4>
                        <p>On the defensive end, I set the physical tone by locking down the key and controlling the defensive glass:</p>
                        <ul>
                            <li><strong>Verticality & Shot Contests:</strong> I use proper timing and vertical extension to disrupt interior drives at the rim, altering shots without getting baited into cheap foul trouble.</li>
                            <li><strong>Physical Box-Outs:</strong> I use my lower center of gravity and core strength to body up opposing centers early, sealing them off to secure defensive rebounds cleanly.</li>
                            <li><strong>High Motor & Recovery:</strong> My mobility allows me to hedge on perimeter screens and recover quickly back into the paint to safeguard the basket.</li>
                        </ul>
                    </div>

                    <div class="media-placeholder has-video basketball-media"><video src="basketball-media/20260201_120317.mp4" muted loop autoplay playsinline preload="metadata"></video></div>

                    <div class="media-placeholder basketball-media"><img src="med-cup-photos/DSC09543.JPG" alt="Basketball action" loading="lazy"></div>

                    <div class="content-block">
                        <h4>Player Profile & On-Court Metrics</h4>
                        <table class="content-table">
                            <thead>
                                <tr><th>Metric / Dimension</th><th>On-Court Execution</th></tr>
                            </thead>
                            <tbody>
                                <tr><td>Position / Archetype</td><td>Mobile Forward / Modern Point-Forward</td></tr>
                                <tr><td>Offensive Strengths</td><td>Face-up dribble drives, soft turnaround hooks, offensive putbacks</td></tr>
                                <tr><td>Defensive Role</td><td>Paint anchor, shot alteration, defensive glass control</td></tr>
                                <tr><td>Tactical Advantage</td><td>Out-pacing traditional static big men with quickness and floor spacing</td></tr>
                            </tbody>
                        </table>
                    </div>

                    <div class="media-placeholder basketball-media"><img src="basketball-media/20260201_120254.jpg" alt="Kabir playing basketball" loading="lazy"></div>

                    <div class="content-block">
                        <p>I play with an energetic, unrelenting interior presence, wearing down my matchup by forcing them to defend both in the paint and out on the perimeter.</p>
                    </div>

                    <div class="media-placeholder has-video basketball-media"><video src="basketball-media/20260317_163100.mp4" muted loop autoplay playsinline preload="metadata"></video></div>

                    <!-- NEW: three additional basketball action clips (added 2026-10-17) -->
                    <div class="media-placeholder has-video basketball-media"><video src="basketball-media/20260920_125226.mp4" muted loop autoplay playsinline preload="metadata"></video></div>
                    <div class="media-placeholder has-video basketball-media"><video src="basketball-media/20260920_125247.mp4" muted loop autoplay playsinline preload="metadata"></video></div>
                    <div class="media-placeholder has-video basketball-media"><video src="basketball-media/20260920_125503.mp4" muted loop autoplay playsinline preload="metadata"></video></div>
                """,
    },
    "coding": {
        "title": "CODING",
        "badge": "ENGINEERING",
        "bento": [
        bento.tile('big', '\n                        <h4>Architecture</h4>\n                        <h2>Python 3.12</h2>\n                        <p style="margin-top:auto;">Building automated backend scripts, data pipelines, and this very site\'s Python build system.</p>\n                    '),
        bento.tile('sm', '\n                        <h4>Frontend</h4>\n                        <p style="color:#fff; font-weight:600;">HTML5, CSS3, DOM</p>\n                    '),
        bento.tile('sm', '\n                        <h4>Deployment</h4>\n                        <p style="color:#fff; font-weight:600;">GitHub Pages</p>\n                    '),
        bento.tile('wide', '\n                        <h4>Design Focus</h4>\n                        <p style="color:#fff; font-weight:600;">Minimalist Solid Matte Interface</p>\n                    '),
        bento.tile('wide', '\n                        <h4>Automation</h4>\n                        <p style="color:#fff; font-weight:600;">Scripting & Data Pipelines</p>\n                    '),
        _account_tile('GitHub', size='sm'),
        _account_tile('Replit', size='sm'),
    ],
        "content": """
                    <div class="content-block">
                        <p class="lead-paragraph">I learn to code through Codingal, a live, one-on-one online coding platform. Each session builds on the last through structured modules that comb[...]
                    </div>

                    <div class="content-block">
                        <p>� My journey began when I earned my first certificate as a Python Programmer! 🐍 This shows I've mastered the fundamental building blocks of programming. I learned[...]
                        <p>💪 I then leveled up my skills tremendously to become an Advance Python Developer! 🚀 This achievement means I've dived much deeper into the world of programming. I[...]
                        <p>🎮 And the adventure continued as I became a Python Game Developer! ✨ This is super exciting because it means I can now create my very own interactive games and app[...]
                        <p>My certificates clearly show an impressive progression in my coding abilities! 🌟 From understanding the core principles of Python programming to building advanced st[...]
                        <p class="text-caption">Generated on June 30, 2026</p>
                    </div>

                    <div class="content-block">
                        <h4>Certificates Earned</h4>
                        """ + _CERTIFICATES_GRID_HTML + """
                    </div>

                    <div class="content-block">
                        <h4>Progress Reports</h4>
                        """ + _PROGRESS_REPORTS_LIST_HTML + """
                    </div>

                    <div class="content-block">
                        <p>All of this Codingal work is also on my <a href="https://github.com/aajukubaa" target="_blank">GitHub</a> — each completed module is its own repository, and inside ea[...]
                    </div>
                """,
    },
    "music": {
        "title": "VIOLIN",
        "badge": "PERFORMANCE",
        "bento": [
        bento.tile('wide', '\n                        <h4>Repertoire Level</h4>\n                        <h2>Suzuki Book 3</h2>\n                    '),
        bento.tile('wide', '\n                        <h4>Focus</h4>\n                        <p style="color:#fff; font-weight:600;">Clean intonation & controlled bowing articulation</p>\n                    '),
        bento.tile('full', '\n                        <h4>Artistic Discipline</h4>\n                        <p style="color:#fff; font-weight:600;">Classical piece interpretation, vibrato control, and tone purity.</p>\n                    '),
    ],
        "content": """
                    <div class="content-block">
                        <h4>Progressing Through Suzuki Book 3</h4>
                        <p>My violin studies follow the Suzuki Method, a repertoire-based approach that builds technique piece by piece rather than through dry drills alone. Each book raises the [...]
                    </div>

                    <div class="media-placeholder chess-portrait"><img src="violin-photos/IMG_20250403_181316.jpg" alt="Kabir playing violin 1" loading="lazy"></div>
                    <div class="media-placeholder chess-portrait"><img src="violin-photos/PXL_20260310_180215963.jpg" alt="Kabir playing violin 2" loading="lazy"></div>

                    <div class="content-block">
                        <h4>School Strings Ensemble</h4>
                        <p>Alongside my individual Suzuki repertoire, I've been a member of my school's Strings Ensemble Group since Grade 6. The ensemble performs a broader, non-Suzuki repertoir[...]
                    </div>

                    <div class="media-placeholder chess-portrait"><img src="violin-photos/PXL_20260310_192822793.jpg" alt="Kabir playing violin 3" loading="lazy"></div>
                    <div class="media-placeholder chess-portrait"><img src="violin-photos/PXL_20260310_192858519.jpg" alt="Kabir playing violin 4" loading="lazy"></div>

                    <!-- NEW: Inline violin audio snippet (added 2026-10-17) -->
                    <div class="content-block">
                        <h4>Audio Snippet — Suzuki Practice</h4>
                        <p>Short excerpt from a practice session.</p>
                        <div class="media-placeholder violin-audio">
                            <audio controls preload="metadata" src="violin-media/20260310_192805.mp3" aria-label="Violin practice audio"></audio>
                        </div>
                    </div>

                    <div class="content-block">
                        <h4>Goals</h4>
                        """ + _goal_bar_html(GOALS[1]) + _goal_bar_html(GOALS[2]) + """
                    </div>

                    <div class="content-block">
                        <h4>Videos</h4>
                        <p>More to come in a future update.</p>
                        <div class="photo-grid">
                            <div class="media-placeholder">Video coming soon</div>
                            <div class="media-placeholder">Video coming soon</div>
                        </div>
                    </div>
                """,
    },
    "presentations": {
        "title": "POWERPOINT",
        "badge": "ACADEMIC DECK ARCHITECTURE",
        "bento": [
        bento.tile('full', '\n                        <h4>Design Standard</h4>\n                        <p style="color:#fff; font-weight:600; font-size:1.2rem;">Minimalist typography & synchronized visual storytelling</p>\n                    '),
        bento.tile('wide', '\n                        <h4>Layouts</h4>\n                        <p style="color:#fff; font-weight:600;">Grid-aligned structure</p>\n                    '),
        bento.tile('wide', '\n                        <h4>Visuals</h4>\n                        <p style="color:#fff; font-weight:600;">High-impact contrast</p>\n                    '),
    ],
        "content": """
                    <div class="content-block">
                        <h4>Slide Deck Design</h4>
                        <p>Engineered dynamic visual presentations featuring clean hierarchical typography and synchronized animations.</p>
                    </div>

                    <div class="content-block">
                        <h4>Presentations</h4>
                        <p>Tap any presentation for a quick summary.</p>
                    </div>
                    """ + _PRESENTATIONS_GALLERY_HTML + """
                """,
    },
    "portfolios": {
        "title": "PORTFOLIOS",
        "badge": "CREATIVE SHOWCASE",
        "bento": [
        bento.tile('full', '\n                        <h4>Archive Volume</h4>\n                        <h2>9+ Portfolios</h2>\n                    '),
        bento.tile('full', '\n                        <h4>Aesthetic</h4>\n                        <p style="color:#fff; font-weight:600;">Monochromatic dark palettes & precision card architectures</p>\n                    '),
    ],
        "content": """
                    <div class="content-block">
                        <h4>Visual Identity</h4>
                        <p>A curated compilation of 9+ comprehensive design project portfolios highlighting minimalist layout grids.</p>
                    </div>

                    <div class="content-block">
                        <h4>Portfolios (Grades 6–8)</h4>
                        <p>Tap any portfolio for a quick summary.</p>
                    </div>
                    """ + _PORTFOLIOS_GALLERY_HTML + """
                """,
    },
    "proj_basketball": {
        "title": "MEDITERRANEAN CUP",
        "badge": "TOURNAMENT CAPTAIN",
        "bento": [
        bento.tile('full', '\n                        <h4>Role</h4>\n                        <h2>Team Captain</h2>\n                        <p style="margin-top:auto;">Lead team strategy and on-court execution.</p>\n                    '),
        bento.tile('wide', '\n                        <h4>Venue</h4>\n                        <p style="color:#fff; font-weight:600;">International Circuit</p>\n                    '),
        bento.tile('wide', '\n                        <h4>Impact</h4>\n                        <p style="color:#fff; font-weight:600;">Paint Defense & Leadership</p>\n                    '),
    ],
        "content": """
                    <div class="content-block">
                        <h4>Flying Out Alone</h4>
                        <p>The Mediterranean Cup was the first time I ever traveled abroad completely by myself. Not with my family, not as part of a big group being walked through the airport by[...]
                        <p>By the time I landed and made my way to the team hotel, that nervous energy had mostly turned into excitement. This was a real international tournament, with teams from[...]
                    </div>

                    """ + _med_cup_photo_html("DSC09519.JPG", 1) + """

                    <div class="content-block">
                        <h4>Rained Out</h4>
                        <p>The tournament was supposed to open with a full day of games, but it rained hard enough on day one that the entire schedule was cancelled. No games, no warm-ups on the [...]
                        <p>What none of us realized yet was how much that single cancelled day was going to change everything that followed. The tournament still had eight games scheduled for our[...]
                    </div>

                    """ + _med_cup_photo_html("DSC09540.JPG", 2) + """

                    <div class="content-block">
                        <h4>The Fall</h4>
                        <p>Games finally got underway the next day, and it didn't take long for things to get complicated. Early in our very first game, I went down hard going for a loose ball ��[...]
                        <p>That wasn't really an option. It was game one of what was about to become a very long day, and there was no version of the schedule where I could afford to sit out and [...]
                    </div>

                    """ + _med_cup_photo_html("DSC09543.JPG", 3) + """

                    <div class="content-block">
                        <h4>Eight Games, One Day</h4>
                        <p>Because the first day had been completely rained out, the tournament organizers compressed the entire remaining schedule to make sure every team still played its full s[...]
                        <p>And I played every single minute of every single one of those eight games. Not most of the minutes, not in and out for rest — every minute, injuries included. By the [...]
                    </div>

                    """ + _med_cup_photo_html("DSC09585.JPG", 4) + """

                    <div class="content-block">
                        <h4>Double-Teamed</h4>
                        <p>By the time we reached the second-to-last game of that marathon day, fatigue had well and truly set in for everyone on the court, not just me. That game was against the[...]
                        <p>I remember the specific feeling of it — catching the ball and suddenly having two defenders collapse on me at once, cutting off every angle I was used to having. It h[...]
                    </div>

                    """ + _med_cup_photo_html("DSC09603.JPG", 5) + """

                    <div class="content-block">
                        <h4>Sixth Place</h4>
                        <p>When the final standings came out, we'd finished sixth out of the eight teams in the tournament. Not the podium finish anyone dreams about walking in, but nowhere near [...]
                        <p>Thinking back on the whole week — flying out on my own for the first time, losing an entire day to rain, falling and playing through real injuries for the rest of the[...]
                    </div>

                    """ + _med_cup_photo_html("DSC09714.JPG", 6) + _med_cup_photo_html("DSC09732.JPG", 7) + _med_cup_photo_html("DSC09744.JPG", 8) + """

                    <div class="content-block">
                        <h4>Tournament Gallery</h4>
                        <p>The rest of the photo set from the tournament.</p>
                    </div>
                    <div class="photo-grid">
""" + _MED_CUP_GALLERY_HTML + """
                    </div>
                """,
    },
    "proj_website": {
        "title": "THIS SHOWCASE",
        "badge": "ARCHITECTURE",
        "bento": [
        bento.tile('wide', '\n                        <h4>Engine</h4>\n                        <h2>Python</h2>\n                    '),
        bento.tile('wide', '\n                        <h4>Style</h4>\n                        <p style="color:#fff; font-weight:600; font-size:1.1rem; margin-top:10px;">Solid Matte & Bento Grids</p>\n                    '),
        bento.tile('full', '\n                        <h4>Philosophy</h4>\n                        <p style="color:#fff; font-weight:600;">Zero-bloat performance: Python builds it, plain JS/CSS run it.</p>\n                    '),
        _account_tile('GitHub', size='full'),
    ],
        "content": """
                    <div class="content-block">
                        <h4>Where This Started</h4>
                        <p>This site didn't start out anything like it looks now. The very first version was a single enormous HTML file with everything crammed into it — the markup, close to a[...]
                        <p>In practice, it was a performance disaster. Loading a complete Python runtime just to swap an image's source attribute and populate a details panel meant every single v[...]
                    </div>

                    <div class="content-block">
                        <h4>Deciding What "Python-Centric" Actually Meant</h4>
                        <p>The first real turning point was realizing that "Python-centric" could mean two very different things: Python running live in the browser, which is what PyScript does, [...]
                        <p>I went with build-time Python. It meant giving up the literal "there's Python executing in your browser right now" novelty, but it meant the site could genuinely be fas[...]
                    </div>

                    <div class="content-block">
                        <h4>Rebuilding It as a Real Static Site Generator</h4>
                        <p>That decision meant rebuilding the entire site from the ground up. All of the PyScript was stripped out completely. In its place, the site became a small Python-based s[...]
                        <p>This meant that changing a piece of text, a stat, or a project description became a matter of editing one clearly organized Python file, instead of hunting through near[...]
                    </div>

                    <div class="content-block">
                        <h4>Learning GitHub's Web Upload the Hard Way</h4>
                        <p>Since I manage this repository entirely through GitHub's website rather than the command line, getting the new file structure live came with its own lessons. The first [...]
                        <p>That turned into a real lesson about how to structure a project for someone uploading through a browser instead of git: keep folders one level deep wherever possible, a[...]
                    </div>

                    <div class="content-block">
                        <h4>Automating the Build Itself</h4>
                        <p>Both of those upload mistakes were symptoms of the same underlying problem: rebuilding the site was a manual step I had to remember to do every single time. So a GitHub[...]
                    </div>

                    <div class="content-block">
                        <h4>Rebuilding the Photo Library</h4>
                        <p>The images went through several full rounds of reorganization. The originals were low-quality, inconsistently named, and some of them referenced files that had never ac[...]
                    </div>

                    <div class="content-block">
                        <h4>A Full Design and Interaction Pass</h4>
                        <p>Once the architecture and content pipeline were solid, the focus shifted to actually refining how the site felt to use. That meant fixing a custom cursor that would get[...]
                    </div>

                    <div class="content-block">
                        <h4>Adding Things That Actually Do Something</h4>
                        <p>Beyond fixing what was already there, a few genuinely new pieces got built in. My Chess.com ratings, records, and recent games now load from a small Python script that[...]
                    </div>

                    <div class="content-block">
                        <h4>Where It Stands Now</h4>
                        <p>The site keeps changing in fairly large jumps — entire sections have been deleted, moved, and reshuffled more than once as the actual content and priorities became cl[...]
                    </div>
                """,
    },
    "proj_chess": {
        "title": "CHESS CIRCUIT",
        "badge": "SCHOOL REPRESENTATIVE",
        "bento": [
        bento.tile('wide', '\n                        <h4>Accolade</h4>\n                        <h2>Best Player</h2>\n                        <p style="margin-top:auto;">Top board performance.</p>\n                    '),
        bento.tile('wide', '\n                        <h4>Format</h4>\n                        <p style="color:#fff; font-weight:600; font-size:1.1rem; margin-top:10px;">In-School & External Circuits</p>\n                    '),
        bento.tile('full', '\n                        <h4>Record</h4>\n                        <p style="color:#fff; font-weight:600;">Undefeated streak on Board 1 during regional school matches.</p>\n                    '),
        _account_tile('FIDE Profile', size='full'),
        _account_tile('Chess.com', size='wide'),
        _account_tile('Lichess', size='wide'),
    ],
        "content": """
                    <div class="content-block">
                        <h4>Competitive Milestones</h4>
                        <p>Representing the school team on top boards, securing the Best Player award for highest win rate.</p>
                    </div>

                    <div class="content-block">
                        <h4>Representing My School</h4>
                        <p>This tournament was my first time playing competitive chess as part of a school team rather than as an individual. That changed the whole feel of the event — every re[...]
                        <p>Out of everyone on my team, I finished with the most individual wins. It was a genuinely tight event — we didn't come away with first place, but we also didn't finish[...]
                    </div>
                """,
    },
}
