# -*- coding: utf-8 -*-
"""Regenerate the site from content.py. Writes HTML + style.css to the repo root.

Locally:  python3 _generator/build_site.py
Or just edit _generator/content.py on github.com — the Action runs this for you.
"""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from base_css import BASE
from contrast import boost
from render import body_for, PAGES
from themes import THEMES

VARIANT = "u01-navy"          # change to switch colourway
SITE = "https://aaron-scheffler.github.io/"

th = next(t for t in THEMES if t["key"] == VARIANT)
css, _ = boost(BASE + th["css"])
open(os.path.join(ROOT, "style.css"), "w", encoding="utf-8").write(css)
for pg in PAGES:
    html = th["shell"](pg, body_for(pg))
    html = html.replace("../shared/images/", "images/")
    html = html.replace("../shared/aaron_cv_2026.pdf", "aaron_cv_2026.pdf")
    html = re.sub(r'<a class="tswitch".*?</a>', "", html)
    html = html.replace('<link rel="stylesheet" href="style.css">',
        '<link rel="stylesheet" href="style.css">\n<link rel="canonical" href="%s%s">'
        % (SITE, "" if pg == "index.html" else pg))
    open(os.path.join(ROOT, pg), "w", encoding="utf-8").write(html)
    print("wrote", pg)
print("wrote style.css")
