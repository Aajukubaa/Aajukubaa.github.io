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
                """,
        "content": """
                    <div class="content-block">
                        <h4>1. Opening Repertoire: Aggressive and Direct</h4>
                        <p><strong>With the White Pieces:</strong> I almost exclusively kick off games with 1. e4, signaling an immediate intent to open up lines, challenge the center, and steer the game into tactical territory. Whether meeting the Sicilian Defense (1...c5) or open responses (1...e5), I look for active piece development and quick initiative.</p>
                        <p><strong>With the Black Pieces:</strong> I am versatile but favor fighting counter-attacking systems. You will frequently see me deploy the Sicilian Defense (1. e4 c5) or the Scandinavian Defense (1. e4 d5) to put immediate pressure on White's center. Against Queen's Pawn openings, I lean toward flexible Indian game setups and fianchetto structures (1. d4 Nf6).</p>
                    </div>

                    """ + _PHOTO_COMING_SOON + """

                    <div class="content-block">
                        <h4>2. Tactical & Dynamic Temperament</h4>
                        <p>My games rarely end in quiet, symmetrical draws. I thrive in complications, often entering sharp middle-game battles involving early piece exchanges, tactical combinations, and exposed king positions. I am not afraid to launch aggressive pawn storms or jump into tactical lines where one precise move decides the game.</p>
                    </div>

                    <div class="content-block">
                        <h4>3. Fast-Paced & Time-Pressure Resilience</h4>
                        <p>A huge part of my playstyle is shaped by fast time controls—predominantly 60+1 bullet/hyper-bullet and 3-minute blitz matches. Because of this, my chess is built for speed and survival under pressure. Many of my games feature intense time scrambles where keeping cool, maintaining clock pressure, and capitalizing on opponent mistakes in the endgame make all the difference.</p>
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

                    """ + _PHOTO_COMING_SOON + """
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

                    """ + _PHOTO_COMING_SOON + """
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

# The two "run a script" buttons. They were hardcoded JS alerts before too —
# that part isn't new — but the copy no longer pretends PyScript is executing
# them live, since there's no Python runtime in the browser anymore.
STATUS_WIDGETS = [
    {
        "pill": "Domain Status Check",
        "heading": "Run Domain Status Script",
        "desc": "Quick status check across all four domains.",
        "button_label": "Run Check",
        "alert": "Status: All 4 domains operating at peak performance. "
                 "FIDE 1545, Center 6'0\\\", Python 3.12, Violin Book 3.",
    },
    {
        "pill": "Quick Stats",
        "heading": "Run Stats Script",
        "desc": "Output a snapshot of current stats.",
        "button_label": "Run Check",
        "alert": "Status: Rating=1545, Status=Active, Domain=Optimal.",
    },
]
