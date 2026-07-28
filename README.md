# aaron-scheffler.github.io

Personal academic site for Aaron Wolfe Scheffler, Associate Professor in
Residence, Department of Epidemiology & Biostatistics, UCSF.

Plain static HTML served by GitHub Pages. No Ruby, no Jekyll, no build step
needed to view it.

## Updating the site

All content lives in one file: **`_generator/content.py`**. Edit it on
github.com, commit, and a GitHub Action regenerates the pages and commits the
HTML back within about a minute. No terminal required.

| To change | Edit in `_generator/content.py` |
|---|---|
| A news item | `NEWS` |
| A publication | `METHODS` (and `SLUGS` just below it) |
| Which papers show under a research area | `pubs=[...]` inside `AREAS` |
| Group members | `PEOPLE` |
| Courses | `COURSES` |
| Title, tagline, contact, links | the constants at the top |
| Colourway | `VARIANT` in `_generator/build_site.py` |

To preview locally instead (optional, needs Python):

```bash
python3 _generator/build_site.py
python3 -m http.server 4000     # then open http://localhost:4000
```

## Layout

```
index.html  research.html  publications.html  people.html  teaching.html
style.css              generated - do not edit by hand
images/                headshot and research figures
aaron_cv_2026.pdf      stable filename; replace in place when the CV updates
_generator/            content and build scripts
.github/workflows/     Action that rebuilds on any change to _generator/
.nojekyll              tells GitHub Pages to serve files as-is
```

Colours are from the [UCSF brand palette](https://identity.ucsf.edu/brand-guide/color)
(A1 Navy, A2, J5). Body text runs at 13:1 contrast, secondary text at 8:1 —
comfortably clear of WCAG AA.
