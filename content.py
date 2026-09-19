"""
All editable content for Kabir Bhuchar's portfolio.

This is the ONLY file you should need to touch to change text, links,
stats, or project details. Structure/styling live in templates/ and
assets/. After editing this file, run:

    python build.py

...to regenerate index.html.
"""

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
    {"id": "tab-overview", "label": "Overview"},
    {"id": "tab-domains", "label": "Domains"},
    {"id": "tab-projects", "label": "Projects"},
    {"id": "tab-archive", "label": "Archive"},
]

HERO = {
    "lines": ["Kabir", "Bhuchar"],
    "intro": "Competitive chess strategist, basketball center, Python architect, "
             "and classical violinist. Welcome to my digital control center.",
}

SPECS = [
    {"value": "1545", "label": "FIDE Rating"},
    {"value": "182 cm", "label": "Basketball Center"},
    {"value": "Book 3", "label": "Suzuki Violin"},
    {"value": "Python 3.12", "label": "Engine Architecture"},
]

CONNECT_LINKS = [
    {"icon": "♟️", "name": "FIDE Profile", "desc": "Official 1545 tournament records",
     "url": "http://ratings.fide.com/profile/498777"},
    {"icon": "♘", "name": "Chess.com", "desc": "Blitz & rapid online matches",
     "url": "https://www.chess.com/member/aajukubaa"},
    {"icon": "♞", "name": "Lichess", "desc": "Bullet & puzzle training",
     "url": "https://lichess.org/@/onesandzeros"},
    {"icon": "💻", "name": "GitHub", "desc": "Python repositories & micro-apps",
     "url": "https://github.com/aajukubaa"},
    {"icon": "⚡", "name": "Replit", "desc": "Live Python code execution",
     "url": "https://replit.com/@Aajukubaa"},
    {"icon": "▶️", "name": "YouTube", "desc": "Video edits & athletic highlights",
     "url": "https://www.youtube.com/@Aajukubaa"},
    {"icon": "✍️", "name": "Medium", "desc": "Articles and analytical logs",
     "url": "https://aajukubaa.medium.com/"},
    {"icon": "🦉", "name": "Duolingo", "desc": "Daily streak & language stats",
     "url": "https://www.duolingo.com/profile/Aajukubaa"},
    {"icon": "🏷️", "name": "Vinted", "desc": "Curated style storefront",
     "url": "https://www.vinted.co.uk/member/284456392"},
    {"icon": "🏺", "name": "Pottery by RG", "desc": "Handmade ceramic works",
     "url": "https://www.etsy.com/uk/shop/PotterybyRG"},
    {"icon": "✉️", "name": "Gmail", "desc": "kabirbhuchar@gmail.com",
     "url": "mailto:kabirbhuchar@gmail.com"},
]

# "category" ties a card to its full-screen detail view in CATEGORIES below.
DOMAIN_CARDS = [
    {"category": "chess", "pill": "Strategy", "title": "Chess", "image": None,
     "preview": "1545 FIDE tournament rating specializing in sharp tactical combat "
                "and aggressive 1.e4 openings."},
    {"category": "basketball", "pill": "Athletics", "title": "Basketball",
     "image": {"id": "basketball-image", "src": "med-cup-photos/DSC09520.JPG",
               "alt": "Basketball action"},
     "preview": "6'0\" Center dominating paint defense, rim protection, "
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
    "DSC09519.JPG", "DSC09520.JPG", "DSC09521.JPG", "DSC09640.JPG", "DSC09642.JPG",
    "DSC09543.JPG", "DSC09545.JPG", "DSC09547.JPG", "DSC09561.JPG", "DSC09585.JPG",
    "DSC09586.JPG", "DSC09587.JPG", "DSC09588.JPG", "DSC09589.JPG", "DSC09590.JPG",
    "DSC09597.JPG", "DSC09603.JPG", "DSC09615.JPG", "DSC09714.JPG", "DSC09715.JPG",
    "DSC09716.JPG", "DSC09717.JPG", "DSC09729.JPG", "DSC09732.JPG", "DSC09736.JPG",
    "DSC09737.JPG", "DSC09741.JPG", "DSC09743.JPG", "DSC09744.JPG",
]

_MED_CUP_GALLERY_HTML = "\n".join(
    f'                    <div class="media-placeholder"><img src="med-cup-photos/{name}" '
    f'alt="Mediterranean Cup — photo {i}" loading="lazy"></div>'
    for i, name in enumerate(MEDITERRANEAN_CUP_PHOTOS, start=1)
)

_PHOTO_COMING_SOON = '<div class="media-placeholder">Photo coming soon</div>'


def _account_tile(link_name):
    """Render one CONNECT_LINKS entry as a clickable bento tile."""
    link = next(l for l in CONNECT_LINKS if l["name"] == link_name)
    return (
        f'<a href="{link["url"]}" target="_blank" class="bento-tile bento-tile-link">'
        f'<h4>{link["icon"]} {link["name"]}</h4>'
        f'<p>{link["desc"]}</p>'
        f'<span class="bento-link-arrow">↗</span></a>'
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
# "category" fields above. "bento" and "content" are hand-authored HTML
# fragments (kept as HTML, same as the original design) — main.js drops
# them straight into the detail modal when a card is clicked.
CATEGORIES = {
    "chess": {
        "title": "CHESS",
        "badge": "STRATEGY",
        "bento": """
                    <div class="bento-tile span-2">
                        <h4>Current Rating</h4>
                        <h2>1545 FIDE</h2>
                        <p style="margin-top:auto;">Official competitive tournament bracket rating.</p>
                    </div>
                    <div class="bento-tile row-2" style="background: #1c1c22; border-color: #44444d;">
                        <h4 style="color: #ffffff;">Opening Base</h4>
                        <h2 style="font-size: 5rem; margin-top:20px;">1.e4</h2>
                    </div>
                    <div class="bento-tile">
                        <h4>Playstyle</h4>
                        <p style="color:#fff; font-size:1.1rem; font-weight:600; margin-top:10px;">Aggressive & Direct</p>
                    </div>
                    <div class="bento-tile span-2">
                        <h4>Time Controls</h4>
                        <p style="color:#fff; font-size:1.1rem; font-weight:600; margin-top:10px;">60+1 Hyper-Bullet & 3-Min Blitz</p>
                    </div>
                    <div class="bento-tile">
                        <h4>Black Defenses</h4>
                        <p>Sicilian (1...c5)<br>Scandinavian (1...d5)</p>
                    </div>
                    <div class="bento-tile">
                        <h4>Tactical Streak</h4>
                        <p style="color:#fff; font-weight:600;">2800+ Puzzle Peak</p>
                    </div>
                    <div class="bento-tile span-2">
                        <h4>Club Standing</h4>
                        <p style="color:#fff; font-weight:600;">Top Board Representative & School Team MVP</p>
                    </div>
                    """ + _account_tile("FIDE Profile") + _account_tile("Chess.com") + _account_tile("Lichess") + """
                """,
        "content": """
                    <div class="content-block">
                        <p class="lead-paragraph">My game is defined by high-octane, uncompromising, and direct aggression. Whenever I sit down with the White pieces, I strictly initiate the battle with 1. e4, grabbing immediate central territory and laying the groundwork to drag my opponents into sharp, tactical struggles where they rarely get room to breathe.</p>
                    </div>

                    <div class="content-block">
                        <h4>My Opening Repertoire & Philosophical Foundations</h4>
                        <p>My goal in the opening is rapid piece activation, immediate central dominance, and forcing my opponents out of their comfort zones right from move one:</p>
                        <ul>
                            <li><strong>Against 1...e5 (Italian Game):</strong> I steer directly into the sharp, classic lines of the Italian Game with 3. Bc4. From there, I love launching the Italian Knight Attack with an early 4. Ng5, placing immediate, relentless pressure on the vulnerable f7-square to test whether my opponent knows their theory or buckles under early tension.</li>
                            <li><strong>Against the French Defense (1...e6):</strong> I claim full central control using 2. d4 d5 3. Nc3 to set up active piece play, or I pivot into a King's Indian Attack setup with 2. d3, coiling my pieces for a long-term kingside buildup.</li>
                            <li><strong>Against the Scandinavian Defense (1...d5):</strong> I accept the challenge immediately with 2. exd5 Qxd5, followed by 3. Nc3 to kick their queen with tempo and accelerate my development.</li>
                            <li><strong>Against the Caro-Kann Defense (1...c6):</strong> I refuse to let Black settle behind a quiet pawn wall, pushing 2. d4 d5 3. Nc3 to assert early space and maintain an active, commanding presence.</li>
                        </ul>
                    </div>

                    <div class="media-placeholder chess-portrait"><img src="chess-photos/20250614_110030.jpg" alt="Kabir playing chess 1" loading="lazy"></div>

                    <div class="content-block">
                        <h4>Midgame Execution & Tactical DNA</h4>
                        <p>Once the opening transitions into the middlegame, my primary focus turns toward heavy pawn storms and direct, decisive assaults on the enemy king. When I secure a spatial advantage, I do not hesitate to launch my wing pawns forward—marching g4, h4, and h5 straight down the board, particularly against kingside fianchetto structures. My objective is simple: rip open attacking files, tear down enemy pawn shelters, and unleash dynamic piece activity. I thrive in chaotic, sharp tactical scrambles where forcing checks and unrelenting threats take absolute priority over slow positional maneuvering. I actively trade off key defensive pieces—such as central knights or bishops—if doing so dismantles my opponent's protective cover and exposes key weak squares around their king.</p>
                    </div>

                    <div class="media-placeholder chess-portrait"><img src="chess-photos/20250614_111530.jpg" alt="Kabir playing chess 2" loading="lazy"></div>

                    <div class="content-block">
                        <h4>Endgame Strategy & Rating Progression</h4>
                        <p>If a match reaches the endgame, my approach shifts toward relentless pawn promotion and active king participation. I push passed pawns with urgency while marching my king aggressively into the action to dominate key central squares.</p>
                    </div>

                    <div class="media-placeholder chess-portrait"><img src="chess-photos/20250614_120820.jpg" alt="Kabir playing chess 3" loading="lazy"></div>

                    <div class="content-block">
                        <p>This high-pressure playing identity has fueled my steady climb from sub-1000 levels up to a peak rating above 1451 Elo in longer rapid time controls. Along the way, I have secured memorable victories against strong 1300–1400+ opponents, including key wins over malcgriff (1406 Elo), Italyane (1342 Elo), EliasRO51 (1337 Elo), and Luxa1988 (1302 Elo). Whether I am competing in fast-paced 60-second bullet battles or deeply calculated 10-minute rapid games, my ultimate ambition remains the same: grab the initiative, maintain constant pressure, and force defensive mistakes.</p>
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
                            <div class="chess-dashboard">
                                <div id="chesscom-games-list" class="chess-games-list">
                                    <p class="chess-dashboard-loading">Loading recent games…</p>
                                </div>
                                <div class="chess-board-panel">
                                    <button class="chess-board-fullscreen-close" aria-label="Exit fullscreen board">✕</button>
                                    <div id="chesscom-board"></div>
                                    <div class="chess-board-controls">
                                        <button id="chess-prev-move" class="interactive-btn" disabled>← Prev</button>
                                        <span id="chess-move-indicator">Select a game</span>
                                        <button id="chess-next-move" class="interactive-btn" disabled>Next →</button>
                                    </div>
                                    <p class="chess-board-hint">Tap the board to expand it</p>
                                </div>
                            </div>
                        </div>
                    </div>
                """,
    },
    "basketball": {
        "title": "BASKETBALL",
        "badge": "ATHLETICS",
        "bento": """
                    <div class="bento-tile span-2">
                        <h4>Position</h4>
                        <h2>6'0" Center</h2>
                        <p style="margin-top:auto;">182 cm interior anchor.</p>
                    </div>
                    <div class="bento-tile span-2">
                        <h4>Focus Areas</h4>
                        <p style="color:#fff; font-size:1.1rem; font-weight:600; margin-top:10px;">Rim Protection & Box-outs</p>
                    </div>
                    <div class="bento-tile">
                        <h4>Rebounding</h4>
                        <p style="color:#fff; font-weight:600;">High-Intensity Glass Control</p>
                    </div>
                    <div class="bento-tile">
                        <h4>Tournament</h4>
                        <p style="color:#fff; font-weight:600;">Mediterranean Cup Captain</p>
                    </div>
                    <div class="bento-tile span-2">
                        <h4>Court Vision</h4>
                        <p style="color:#fff; font-weight:600;">High Post Passing & Screen Setting</p>
                    </div>
                """,
        "content": """
                    <div class="content-block">
                        <p class="lead-paragraph">At 6'0" playing center, my game is built around mobile physical dominance, blending traditional low-post grit with face-up perimeter versatility. I leverage my body control, active footwork, and length to anchor the paint while constantly keeping opposing bigs guessing off the bounce.</p>
                    </div>

                    <div class="media-placeholder basketball-media"><img src="med-cup-photos/DSC09640.JPG" alt="Basketball action" loading="lazy"></div>

                    <div class="content-block">
                        <h4>Offensive Arsenal: Post Touch & Face-Up Drives</h4>
                        <p>My scoring identity revolves around high-efficiency interior moves and capitalizing on mismatches when slower defenders guard me:</p>
                        <ul>
                            <li><strong>Low-Post Scoring & Soft Touch:</strong> I establish firm deep post position, using patient pump fakes, drop steps, and a soft turnaround hook shot over contesting arms to finish smoothly around the basket.</li>
                            <li><strong>Face-Up Dribble Attacks:</strong> I don't just stay stuck in the paint; I readily receive the ball at the top of the key or wing, put the ball on the deck, and drive hard through the lane to finish at the rim.</li>
                            <li><strong>Glass Cleaning & Putbacks:</strong> On the offensive boards, I track flight paths relentlessly, carving out space to grab missed shots and cash in on immediate second-chance points.</li>
                        </ul>
                    </div>

                    <div class="media-placeholder has-video basketball-media"><video src="basketball-media/20260201_115601.mp4" muted loop autoplay playsinline></video></div>

                    <div class="content-block">
                        <h4>Defensive Anchor & Rim Protection</h4>
                        <p>On the defensive end, I set the physical tone by locking down the key and controlling the defensive glass:</p>
                        <ul>
                            <li><strong>Verticality & Shot Contests:</strong> I use proper timing and vertical extension to disrupt interior drives at the rim, altering shots without getting baited into cheap foul trouble.</li>
                            <li><strong>Physical Box-Outs:</strong> I use my lower center of gravity and core strength to body up opposing centers early, sealing them off to secure defensive rebounds cleanly.</li>
                            <li><strong>High Motor & Recovery:</strong> My mobility allows me to hedge on perimeter screens and recover quickly back into the paint to safeguard the basket.</li>
                        </ul>
                    </div>

                    <div class="media-placeholder has-video basketball-media"><video src="basketball-media/20260201_120317.mp4" muted loop autoplay playsinline></video></div>

                    <div class="media-placeholder basketball-media"><img src="med-cup-photos/DSC09543.JPG" alt="Basketball action" loading="lazy"></div>

                    <div class="content-block">
                        <h4>Player Profile & On-Court Metrics</h4>
                        <table class="content-table">
                            <thead>
                                <tr><th>Metric / Dimension</th><th>On-Court Execution</th></tr>
                            </thead>
                            <tbody>
                                <tr><td>Position / Archetype</td><td>Mobile Center / Modern Point-Center</td></tr>
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

                    <div class="media-placeholder has-video basketball-media"><video src="basketball-media/20260317_163100.mp4" muted loop autoplay playsinline></video></div>
                """,
    },
    "coding": {
        "title": "CODING",
        "badge": "ENGINEERING",
        "bento": """
                    <div class="bento-tile row-2 span-2">
                        <h4>Architecture</h4>
                        <h2>Python 3.12</h2>
                        <p style="margin-top:auto;">Building automated backend scripts, data pipelines, and this very site's Python build system.</p>
                    </div>
                    <div class="bento-tile">
                        <h4>Frontend</h4>
                        <p style="color:#fff; font-weight:600;">HTML5, CSS3, DOM</p>
                    </div>
                    <div class="bento-tile">
                        <h4>Deployment</h4>
                        <p style="color:#fff; font-weight:600;">GitHub Pages</p>
                    </div>
                    <div class="bento-tile span-2">
                        <h4>Design Focus</h4>
                        <p style="color:#fff; font-weight:600;">Minimalist Solid Matte Interface</p>
                    </div>
                    <div class="bento-tile span-2">
                        <h4>Automation</h4>
                        <p style="color:#fff; font-weight:600;">Scripting & Data Pipelines</p>
                    </div>
                    """ + _account_tile("GitHub") + _account_tile("Replit") + """
                """,
        "content": """
                    <div class="content-block">
                        <p class="lead-paragraph">I learn to code through Codingal, a live, one-on-one online coding platform. Each session builds on the last through structured modules that combine short lessons with hands-on projects — which is where the certificates and progress reports below come from.</p>
                    </div>

                    <div class="content-block">
                        <p>🌟 My journey began when I earned my first certificate as a Python Programmer! 🐍 This shows I've mastered the fundamental building blocks of programming. I learned how to handle different types of data, use operators to make calculations, and create clever loops to repeat actions. 🔄 I even brought my code to life by developing projects using cool turtle graphics! 🐢 This certificate proves I have a strong foundation in putting code together.</p>
                        <p>💪 I then leveled up my skills tremendously to become an Advance Python Developer! 🚀 This achievement means I've dived much deeper into the world of programming. I learned how to organize complex information using data structures 📚 and how to build powerful, reusable code with object-oriented programming concepts like inheritance. 🧠 This certificate highlights my ability to tackle more sophisticated coding challenges and design efficient programs.</p>
                        <p>🎮 And the adventure continued as I became a Python Game Developer! ✨ This is super exciting because it means I can now create my very own interactive games and applications. I mastered the basics of the Pygame library to bring my games to life and learned about GUI development with the Tkinter module to create engaging visual interfaces. 🎨 I even built an amazing game like Space Invaders! 👾 This certificate showcases my creativity and ability to build fun, playable experiences.</p>
                        <p>My certificates clearly show an impressive progression in my coding abilities! 🌟 From understanding the core principles of Python programming to building advanced structures and ultimately creating interactive games, I've demonstrated remarkable problem-solving skills 💡 and a true talent for bringing ideas to life through code. I will keep exploring and building amazing things! 💻</p>
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
                        <p>All of this Codingal work is also on my <a href="https://github.com/aajukubaa" target="_blank">GitHub</a> — each completed module is its own repository, and inside each one you'll find a folder per lesson, named after that lesson. Inside those lesson folders are all the files I wrote to complete it, including every activity and the final project, saved as A1.py, A2.py, A3.py, and so on.</p>
                    </div>
                """,
    },
    "music": {
        "title": "VIOLIN",
        "badge": "PERFORMANCE",
        "bento": """
                    <div class="bento-tile span-2">
                        <h4>Repertoire Level</h4>
                        <h2>Suzuki Book 3</h2>
                    </div>
                    <div class="bento-tile span-2">
                        <h4>Focus</h4>
                        <p style="color:#fff; font-weight:600;">Clean intonation & controlled bowing articulation</p>
                    </div>
                    <div class="bento-tile span-4">
                        <h4>Artistic Discipline</h4>
                        <p style="color:#fff; font-weight:600;">Classical piece interpretation, vibrato control, and tone purity.</p>
                    </div>
                """,
        "content": """
                    <div class="content-block">
                        <h4>Progressing Through Suzuki Book 3</h4>
                        <p>My violin studies follow the Suzuki Method, a repertoire-based approach that builds technique piece by piece rather than through dry drills alone. Each book raises the technical bar — cleaner intonation, more controlled bowing, and more demanding dynamic phrasing — and I'm currently working through Book 3. Reaching this point reflects several years of consistent, steady practice rather than a quick jump.</p>
                    </div>

                    <div class="content-block">
                        <h4>School Strings Ensemble</h4>
                        <p>Alongside my individual Suzuki repertoire, I've been a member of my school's Strings Ensemble Group since Grade 6. The ensemble performs a broader, non-Suzuki repertoire, which has given me consistent experience playing alongside other musicians, following a conductor, and performing live in school concerts — a different skill set from solo practice, and one I've kept building every year since.</p>
                    </div>

                    <div class="content-block">
                        <h4>Goals</h4>
                        """ + _goal_bar_html(GOALS[1]) + _goal_bar_html(GOALS[2]) + """
                    </div>

                    <div class="content-block">
                        <h4>Photos & Videos</h4>
                        <p>More to come in a future update.</p>
                        <div class="photo-grid">
                            <div class="media-placeholder">Photo coming soon</div>
                            <div class="media-placeholder">Photo coming soon</div>
                            <div class="media-placeholder">Video coming soon</div>
                            <div class="media-placeholder">Video coming soon</div>
                            <div class="media-placeholder">Photo coming soon</div>
                            <div class="media-placeholder">Video coming soon</div>
                        </div>
                    </div>
                """,
    },
    "presentations": {
        "title": "POWERPOINT",
        "badge": "ACADEMIC DECK ARCHITECTURE",
        "bento": """
                    <div class="bento-tile span-4">
                        <h4>Design Standard</h4>
                        <p style="color:#fff; font-weight:600; font-size:1.2rem;">Minimalist typography & synchronized visual storytelling</p>
                    </div>
                    <div class="bento-tile span-2">
                        <h4>Layouts</h4>
                        <p style="color:#fff; font-weight:600;">Grid-aligned structure</p>
                    </div>
                    <div class="bento-tile span-2">
                        <h4>Visuals</h4>
                        <p style="color:#fff; font-weight:600;">High-impact contrast</p>
                    </div>
                """,
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
        "bento": """
                    <div class="bento-tile span-4">
                        <h4>Archive Volume</h4>
                        <h2>9+ Portfolios</h2>
                    </div>
                    <div class="bento-tile span-4">
                        <h4>Aesthetic</h4>
                        <p style="color:#fff; font-weight:600;">Monochromatic dark palettes & precision card architectures</p>
                    </div>
                """,
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
        "bento": """
                    <div class="bento-tile span-4">
                        <h4>Role</h4>
                        <h2>Team Captain</h2>
                        <p style="margin-top:auto;">Lead team strategy and on-court execution.</p>
                    </div>
                    <div class="bento-tile span-2">
                        <h4>Venue</h4>
                        <p style="color:#fff; font-weight:600;">International Circuit</p>
                    </div>
                    <div class="bento-tile span-2">
                        <h4>Impact</h4>
                        <p style="color:#fff; font-weight:600;">Paint Defense & Leadership</p>
                    </div>
                """,
        "content": """
                    <div class="content-block">
                        <h4>Leading the Squad</h4>
                        <p>Captained the team through the highly competitive Mediterranean Cup, demanding intense communication and paint leadership.</p>
                    </div>

                    <div class="content-block">
                        <h4>Tournament Gallery</h4>
                        <p>The full photo set from the tournament.</p>
                    </div>
                    <div class="photo-grid">
""" + _MED_CUP_GALLERY_HTML + """
                    </div>
                """,
    },
    "proj_website": {
        "title": "THIS SHOWCASE",
        "badge": "ARCHITECTURE",
        "bento": """
                    <div class="bento-tile span-2">
                        <h4>Engine</h4>
                        <h2>Python</h2>
                    </div>
                    <div class="bento-tile span-2">
                        <h4>Style</h4>
                        <p style="color:#fff; font-weight:600; font-size:1.1rem; margin-top:10px;">Solid Matte & Bento Grids</p>
                    </div>
                    <div class="bento-tile span-4">
                        <h4>Philosophy</h4>
                        <p style="color:#fff; font-weight:600;">Zero-bloat performance: Python builds it, plain JS/CSS run it.</p>
                    </div>
                    """ + _account_tile("GitHub") + """
                """,
        "content": """
                    <div class="content-block">
                        <h4>Building the UI/UX</h4>
                        <p>Built with a Python static-site generator: Jinja2 templates and a small Python content model compile into a single dependency-free HTML page, so visitors never download a runtime just to view it.</p>
                    </div>

                    """ + _PHOTO_COMING_SOON + """
                """,
    },
    "proj_chess": {
        "title": "CHESS CIRCUIT",
        "badge": "SCHOOL REPRESENTATIVE",
        "bento": """
                    <div class="bento-tile span-2">
                        <h4>Accolade</h4>
                        <h2>Best Player</h2>
                        <p style="margin-top:auto;">Top board performance.</p>
                    </div>
                    <div class="bento-tile span-2">
                        <h4>Format</h4>
                        <p style="color:#fff; font-weight:600; font-size:1.1rem; margin-top:10px;">In-School & External Circuits</p>
                    </div>
                    <div class="bento-tile span-4">
                        <h4>Record</h4>
                        <p style="color:#fff; font-weight:600;">Undefeated streak on Board 1 during regional school matches.</p>
                    </div>
                    """ + _account_tile("FIDE Profile") + _account_tile("Chess.com") + _account_tile("Lichess") + """
                """,
        "content": """
                    <div class="content-block">
                        <h4>Competitive Milestones</h4>
                        <p>Representing the school team on top boards, securing the Best Player award for highest win rate.</p>
                    </div>

                    """ + _PHOTO_COMING_SOON + """
                """,
    },
}
