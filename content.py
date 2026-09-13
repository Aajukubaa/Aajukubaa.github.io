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
    {"id": "tab-archive", "label": "Projects & Archive"},
    {"id": "tab-now-goals", "label": "Now & Goals"},
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
    {"category": "projects", "pill": "Python Workflows", "title": "Custom Code Repos",
     "image": None,
     "desc": "Automated scripts, data pipelines, and browser app micro-services.",
     "cta": "View Code Repos"},
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

GOALS = [
    {"emoji": "♟️", "title": "FIDE Rating Target: 1800", "current": "1545",
     "target": "1800", "percent": 85},
    {"emoji": "🎻", "title": "Suzuki Violin Goal: Reach Book 5", "current": "Book 3",
     "target": "Book 5", "percent": 60},
]

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
                        <h4>Live Chess.com Dashboard</h4>
                        <p>Live ratings, records, and recent games — pulled directly from Chess.com.</p>
                        <div id="chesscom-stats" class="chess-stats-grid">
                            <p class="chess-dashboard-loading">Loading live ratings…</p>
                        </div>
                        <div class="chess-dashboard">
                            <div id="chesscom-games-list" class="chess-games-list">
                                <p class="chess-dashboard-loading">Loading recent games…</p>
                            </div>
                            <div class="chess-board-panel">
                                <div id="chesscom-board"></div>
                                <div class="chess-board-controls">
                                    <button id="chess-prev-move" class="interactive-btn" disabled>← Prev</button>
                                    <span id="chess-move-indicator">Select a game</span>
                                    <button id="chess-next-move" class="interactive-btn" disabled>Next →</button>
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
                        <h4>Paint Dominance & Defensive Anchoring</h4>
                        <p>Operating as a 6'0" (182 cm) Center. Combines vertical leap, aggressive rim protection, strong defensive box-outs, and vocal floor communication to shut down opposing drives.</p>
                    </div>

                    <div class="media-placeholder"><img src="med-cup-photos/DSC09640.JPG" alt="Basketball Post Play" loading="lazy"></div>

                    <div class="content-block">
                        <h4>Rebounding & High Post Distribution</h4>
                        <p>Securing defensive and offensive boards in traffic, initiating fast breaks with accurate outlet passes, and setting solid screens in the half-court set.</p>
                    </div>

                    <div class="media-placeholder"><img src="med-cup-photos/DSC09642.JPG" alt="Basketball Contest" loading="lazy"></div>
                    <div class="media-placeholder"><img src="med-cup-photos/DSC09543.JPG" alt="Basketball Huddle" loading="lazy"></div>
                    <div class="media-placeholder"><img src="med-cup-photos/DSC09561.JPG" alt="Mediterranean Cup Action" loading="lazy"></div>
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
                        <h4>Stack & Workflow</h4>
                        <p>Specializes in Python 3.12 backend scripting, data workflows, DOM event handling, and deploying responsive micro-apps directly to GitHub Pages.</p>
                    </div>

                    """ + _PHOTO_COMING_SOON + """
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
                        <h4>Musical Discipline</h4>
                        <p>Advanced classical repertoire execution currently advancing through Suzuki Book 3. Emphasizes clean intonation, dynamic phrasing, and pure tone production.</p>
                    </div>

                    """ + _PHOTO_COMING_SOON + """
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
    "projects": {
        "title": "REPOSITORIES",
        "badge": "AUTOMATION & MICRO-APPS",
        "bento": """
                    <div class="bento-tile span-4">
                        <h4>Repositories</h4>
                        <p style="color:#fff; font-weight:600;">Automated scripts & dynamic browser utilities</p>
                    </div>
                    <div class="bento-tile span-2">
                        <h4>Hosting</h4>
                        <p style="color:#fff; font-weight:600;">GitHub Pages</p>
                    </div>
                    <div class="bento-tile span-2">
                        <h4>Runtime</h4>
                        <p style="color:#fff; font-weight:600;">Static Site (Python-built)</p>
                    </div>
                    """ + _account_tile("GitHub") + _account_tile("Replit") + """
                """,
        "content": """
                    <div class="content-block">
                        <h4>Open Source</h4>
                        <p>Showcases custom Python scripts and interactive browser apps built for maximum performance.</p>
                    </div>

                    """ + _PHOTO_COMING_SOON + """
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
