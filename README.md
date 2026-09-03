# aajukubaa.github.io — Python-built static site

## What changed

This portfolio used to run PyScript (a full Python interpreter compiled to
WebAssembly) live in every visitor's browser, just to swap one image `src`
and fill in a details panel. That's gone. Python now only runs **on your
machine** (or in CI) to *generate* the site; visitors get plain, fast
HTML/CSS/JS with no runtime to download.

- `content.py` — every piece of text, link, stat, and project detail on
  the site. **This is the file to edit for day-to-day changes.**
- `templates/index.html.j2` — the page structure (Jinja2 template).
- `build.py` — reads `content.py` + the template, writes `index.html`.
- `assets/style.css` — all styling (previously inline in the page).
- `assets/main.js` — all interactivity: tabs, the detail modal, the
  custom cursor, sound effects, keyboard shortcuts, etc.
- `index.html` — the generated output. **This is what GitHub Pages serves.**
  Don't hand-edit it — your edits will be overwritten next build.

## Making a change (automatic — via GitHub Action)

As of `.github/workflows/build.yml`, you no longer need to manually run
`build.py` or upload `index.html` yourself. Just edit `content.py` (or
`templates/index.html.j2`, `assets/style.css`, `assets/main.js`) directly
on GitHub (pencil ✏️ icon → edit → commit), and a GitHub Action
automatically rebuilds `index.html` and commits it back for you within
a minute or two. Refresh the live site after that to see your change.

**One-time setup required** for the auto-commit step to be allowed to
push: go to your repo's **Settings → Actions → General → Workflow
permissions**, and select **"Read and write permissions"**, then Save.
Without this, the build will run but fail at the final "commit" step.

You can watch it run under the **Actions** tab of your repo.

## Making a change (manual — if you ever need to build locally)

1. Edit `content.py` (text/links/stats) and/or `templates/index.html.j2`
   (layout) and/or `assets/`.
2. Rebuild:
   ```bash
   pip install -r requirements.txt   # first time only
   python build.py
   ```
3. Commit and push `index.html` along with your source changes. GitHub
   Pages serves whatever `index.html` is committed — there's no build
   step on their end unless the Action above is set up, so without it
   you do need to run `build.py` and commit the result yourself.

## Uploading this via GitHub's web interface (no git required)

If you're using "Add file → Upload files" in the browser rather than git,
folders can be unreliable — GitHub's upload **button** opens a file picker
that generally can't select folders at all, and drag-and-drop of folders
depends on your browser. The most foolproof way to get a nested file like
`assets/style.css` into the repo through the web UI:

1. Go to **Add file → Create new file** (not "Upload files").
2. In the filename box, type the full path: `assets/style.css` — GitHub
   will automatically create the `assets` folder for you as you type the `/`.
3. Paste the file's contents in and commit.
4. Repeat for `assets/main.js`.

For everything else here (`index.html`, `content.py`, `build.py`,
`templates/index.html.j2`, `requirements.txt`, `README.md`), plain
"Upload files" works fine since none of them need more than one folder
level deep, which is what caused the last break — `assets/css/style.css`
and `assets/js/main.js` were two folders deep and silently never uploaded,
which is why the site lost all its styling. If you'd rather avoid this
entire class of problem going forward, consider GitHub Desktop or the
`git` command line — both handle nested folders without any of this.

## What's *not* included here

Your `compressedImages/`, `images/`, and `K.png` folders/files are
untouched — keep them exactly where they are in the repo. This bundle
only replaces `index.html` and adds the `content.py` / `build.py` /
`templates/` / `assets/` files alongside them.

## Notable fixes made along the way

- Removed PyScript/Pyodide entirely (was several MB downloaded on every
  visit for trivial DOM work) — this was the single biggest speed cost
  on the old site.
- The two "Run script.py" buttons were always hardcoded JS alerts, never
  real Python — the copy around them no longer claims otherwise.
- Copy that referenced "PyScript" / "native Python execution" as the
  site's live engine has been reworded to describe the actual new
  architecture (Python at build time).
- The custom cursor now only hides the native one once `main.js`
  confirms it's actually running, so a blocked/failed script can't leave
  visitors with no cursor at all.
- Hover/click sound effects use event delegation instead of a one-time
  `querySelectorAll`, so they consistently cover every interactive
  element instead of only the ones present at page load.
- The `AudioContext` for sound effects is now created lazily on first
  interaction instead of at page load.
- Domain/project/archive cards (`role="button" tabindex="0"`) are now
  actually keyboard-activatable with Enter/Space, matching what that
  markup already implied.

Nothing about the visual design was changed in this pass — same layout,
same colors, same content, same images.
