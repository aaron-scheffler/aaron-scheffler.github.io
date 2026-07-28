# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,"/sessions/hopeful-ecstatic-brown/mnt/outputs/build")
from content import *
from render import nav_html, links_html, portrait, body_for, title_for, IMG

def head(t, fonts):
    return f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><meta name="description" content="{SHORT}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{fonts}" rel="stylesheet"><link rel="stylesheet" href="style.css">
</head><body>"""

SW = '<a class="tswitch" href="../index.html">&#8592; All templates</a>'
FOOT = f'<footer class="foot"><p>{NAME} &middot; {DEPT}, {INST} &middot; <a href="mailto:{EMAIL}">{EMAIL}</a></p></footer>'

def side(p):
    return (f'<aside class="side"><div class="sidein">'
            f'<a class="swm" href="index.html">{NAME}</a>'
            f'<div class="slab">Sections</div><nav class="nav">{nav_html(p)}</nav></div></aside>')

def page(p, body, fonts):
    return head(title_for(p), fonts) + '<div class="shell">' + side(p) + \
           '<main class="main">' + body + FOOT + '</main></div>' + SW + '</body></html>'

F_MIX = ("https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700"
         "&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap")
F_LIB = "https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Inter:wght@400;500;600&display=swap"
F_SANS= "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap"
F_FR  = "https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Inter:wght@400;500;600&display=swap"

# ---- shared Academic structure: layout + typography, no colour decisions ----
ACADEMIC = r"""
.shell{display:grid;grid-template-columns:224px minmax(0,1fr);gap:64px;
  max-width:1180px;margin:0 auto;padding:54px 34px 90px}
.side{position:sticky;top:54px;align-self:start;height:max-content}
.swm{display:block;font:600 15px/1.3 var(--display);color:var(--fg-str);letter-spacing:-.01em;margin-bottom:26px}
.slab{font:600 10px/1 var(--ui);letter-spacing:.14em;text-transform:uppercase;color:var(--fg-dim);margin:0 0 11px}
.nav{display:flex;flex-direction:column}
.nav a{font:500 14.5px/1 var(--ui);color:var(--fg-dim);padding:10px 0 10px 14px;
  border-left:2px solid var(--line);transition:.15s}
.nav a:hover{color:var(--fg-str);border-left-color:var(--fg-dim)}
.nav a.on{color:var(--accent);border-left-color:var(--accent);font-weight:600}
.main{min-width:0}
.hero{align-items:flex-start;gap:38px}
.hero h1{letter-spacing:-.02em}
.portrait{box-shadow:0 2px 16px rgba(5,32,73,.10)}
.foot{border-top:1px solid var(--line);margin-top:56px;padding-top:20px;font:.76em/1.65 var(--ui);color:var(--fg-dim)}
@media(max-width:1080px){.hero{flex-direction:column;gap:24px}}
@media(max-width:880px){
  .shell{grid-template-columns:1fr;gap:26px;padding:26px 22px 70px}
  .side{position:static}.nav{flex-direction:row;flex-wrap:wrap;gap:6px}.swm{margin-bottom:14px}
  .hero{gap:20px}
}
"""

def academic_vars(bg, fg, fg_str, fg_dim, line, soft, accent, accent2, link, link_h,
                  r1, r2, r3, r4, chip="transparent"):
    """r* are (bg, fg) pairs for the four author-role badges."""
    return f""":root{{
--bg:{bg};--fg:{fg};--fg-str:{fg_str};--fg-dim:{fg_dim};--line:{line};--soft:{soft};
--accent:{accent};--accent2:{accent2};--link:{link};--link-h:{link_h};--chip-bg:{chip};
--display:'Source Serif 4',Georgia,serif;--ui:'Inter',sans-serif;--mono:'JetBrains Mono',monospace;
--body:400 17px/1.68 'Inter',sans-serif;--h1:38px;--h2:27px;--h3:20px;
--gap-l:46px;--gap-s:20px;--br:8px;--pw:clamp(200px,24vw,270px);--sticky:78px;
--r1-bg:{r1[0]};--r1-fg:{r1[1]};--r2-bg:{r2[0]};--r2-fg:{r2[1]};
--r3-bg:{r3[0]};--r3-fg:{r3[1]};--r4-bg:{r4[0]};--r4-fg:{r4[1]};
--linkline:{line};--onaccent:{bg}}}
""" + ACADEMIC

THEMES = []
def T(**kw): THEMES.append(kw)

NAVY="#052049"; INK="#0a2c5c"; BODY="#3c4859"; DIM="#6a7686"
GRAYLINE="#E1E3E5"; GRAYSOFT="#F2F3F4"; COOL="#506380"

# ---------- the ten UCSF variants ----------
UCSF = [
 dict(key="u01-navy", name="Navy", codes="A1 Navy · A3 CTA Blue · J5",
   blurb="Navy with the CTA blue reserved for links. The most literal reading of the brand guide.",
   swatch=["#052049","#006BE9","#E1E3E5"],
   v=dict(bg="#fff",fg=BODY,fg_str=NAVY,fg_dim=DIM,line=GRAYLINE,soft=GRAYSOFT,
     accent="#052049",accent2="#006BE9",link="#0F388A",link_h="#052049",
     r1=("#e6ecf5","#052049"),r2=("#e2eeff","#0b53b8"),r3=("#eef0f2","#5c6773"),r4=("#e9e8f4","#2E2872"))),

 dict(key="u02-teal", name="Deep Teal", codes="A1 Navy · C1 · C3 Teal",
   blurb="Navy structure, C1 deep teal accents. Cool and clinical without going cold.",
   swatch=["#052049","#0E5258","#16A0AC"],
   v=dict(bg="#fff",fg=BODY,fg_str=NAVY,fg_dim=DIM,line="#dfe5e6",soft="#f2f7f7",
     accent="#0E5258",accent2="#FA6E1E",link="#0E5258",link_h="#052049",
     r1=("#e0eeef","#0E5258"),r2=("#fdece0","#b34e10"),r3=("#eef0f2","#5c6773"),r4=("#e6ecf5","#052049"))),

 dict(key="u03-green", name="Forest", codes="A1 Navy · D1 · D2",
   blurb="D1 deep green against navy. Closest to the palette you had before, now on-brand.",
   swatch=["#052049","#00483A","#007242"],
   v=dict(bg="#fff",fg=BODY,fg_str=NAVY,fg_dim=DIM,line="#dee5e2",soft="#f1f6f4",
     accent="#00483A",accent2="#FA6E1E",link="#00483A",link_h="#052049",
     r1=("#e0ede8","#00483A"),r2=("#fdece0","#b34e10"),r3=("#eef0f2","#5c6773"),r4=("#e6ecf5","#052049"))),

 dict(key="u04-indigo", name="Indigo", codes="A1 Navy · F1 · F2",
   blurb="F1 deep indigo. Reads scholarly and slightly formal; strong on a white page.",
   swatch=["#052049","#2E2872","#443E8C"],
   v=dict(bg="#fff",fg=BODY,fg_str="#1c1b3a",fg_dim=DIM,line="#e2e1ea",soft="#f4f3f9",
     accent="#2E2872",accent2="#FEB80A",link="#2E2872",link_h="#1a1547",
     r1=("#e7e6f2","#2E2872"),r2=("#fdf2d5","#8a6200"),r3=("#eef0f2","#5c6773"),r4=("#e0eeef","#0E5258"))),

 dict(key="u05-violet", name="Violet", codes="A1 Navy · G1 · G2",
   blurb="G1 deep violet. Unusual for an academic site, and memorable because of it.",
   swatch=["#052049","#461850","#6C247C"],
   v=dict(bg="#fff",fg=BODY,fg_str="#2a1230",fg_dim=DIM,line="#e7e0e9",soft="#f8f3f9",
     accent="#461850",accent2="#14828C",link="#6C247C",link_h="#461850",
     r1=("#f0e5f3","#461850"),r2=("#dff0f1","#0d6d76"),r3=("#eef0f2","#5c6773"),r4=("#e6ecf5","#052049"))),

 dict(key="u06-wine", name="Wine", codes="A1 Navy · H1 · H2",
   blurb="H1 deep wine with navy. Warm, editorial, and the most distinctive of the ten.",
   swatch=["#052049","#561038","#821A56"],
   v=dict(bg="#fffdfd",fg=BODY,fg_str="#2e0d20",fg_dim=DIM,line="#ebe0e5",soft="#faf3f6",
     accent="#561038",accent2="#0E5258",link="#821A56",link_h="#561038",
     r1=("#f5e4ec","#561038"),r2=("#e0eeef","#0E5258"),r3=("#eef0f2","#5c6773"),r4=("#e6ecf5","#052049"))),

 dict(key="u07-bluegray", name="Blue Gray", codes="I3 Blue Gray · A1 Navy · J5",
   blurb="I3 blue-gray doing most of the work. The quietest option — nearly monochrome.",
   swatch=["#052049","#506380","#B4B9BF"],
   v=dict(bg="#fcfcfd",fg="#454f5c",fg_str=NAVY,fg_dim="#78828f",line="#e3e5e9",soft="#f4f6f8",
     accent="#506380",accent2="#052049",link="#506380",link_h="#052049",
     r1=("#e6eaf1","#3d5070"),r2=("#e6ecf5","#052049"),r3=("#eff1f3","#697380"),r4=("#e9edf0","#4a5866"))),

 dict(key="u08-chartreuse", name="Chartreuse", codes="A1 Navy · E3 Chartreuse · E4 Point Reyes",
   blurb="Navy body with E3 chartreuse as a single bright accent. Energetic; use sparingly.",
   swatch=["#052049","#84C234","#B4DC55"],
   v=dict(bg="#fff",fg=BODY,fg_str=NAVY,fg_dim=DIM,line="#e3e6e0",soft="#f6f8f0",
     accent="#4d7016",accent2="#052049",link="#3f5f10",link_h="#2b4208",
     r1=("#eaf3d8","#3f5f10"),r2=("#e6ecf5","#052049"),r3=("#eef0f2","#5c6773"),r4=("#e0eeef","#0E5258"))),

 dict(key="u09-gold", name="Ink & Gold", codes="A1 Navy · L3 Yellow · M3 Orange",
   blurb="Navy with the secondary warm pair. Gold marks news and awards; orange marks links.",
   swatch=["#052049","#FEB80A","#FA6E1E"],
   v=dict(bg="#fffdf9",fg=BODY,fg_str=NAVY,fg_dim=DIM,line="#e8e4da",soft="#faf6ed",
     accent="#052049",accent2="#b34e10",link="#a35a06",link_h="#7a4204",
     r1=("#e6ecf5","#052049"),r2=("#fdf1d3","#8a6200"),r3=("#f0eee8","#6b6558"),r4=("#fdece0","#b34e10"))),

 dict(key="u10-navydark", name="Navy Reversed", codes="A1 Navy ground · C4 · B5",
   blurb="The palette inverted: navy ground, pale blue type. Figures sit on white cards.",
   swatch=["#052049","#60D0DA","#B8E6FA"],
   v=dict(bg="#052049",fg="#c3d2e4",fg_str="#f4f8fc",fg_dim="#8ba2bf",line="#153károly",soft="#0a2c5c",
     accent="#60D0DA",accent2="#FEB80A",link="#60D0DA",link_h="#B8E6FA",chip="#0a2c5c",
     r1=("#0d3f4a","#60D0DA"),r2=("#3d3212","#FEB80A"),r3=("#12325e","#9fb4cc"),r4=("#1b2f5e","#B8E6FA"))),
]
UCSF[-1]["v"]["line"] = "#15355f"

for u in UCSF:
    T(key=u["key"], name=u["name"], blurb=u["blurb"], codes=u["codes"], swatch=u["swatch"],
      group="UCSF palette", fonts=F_MIX, css=academic_vars(**u["v"]))


# ---------- high-contrast ink variants ----------
def ink_vars(**kw):
    """academic_vars plus rules that push the accent and the ink much harder."""
    extra = r"""
/* --- ink emphasis --- */
.ptitle,.hero h1{color:var(--accent)}
.slab,.glab{color:var(--accent)}
.sechead{border-bottom-color:var(--accent)}
.areanum,.yrlab span,.ry,.ccode{color:var(--accent)}
.area h2,.person h3,.course h2,.pubsec h2{color:var(--fg-str)}
.lead{border-left-width:4px;color:var(--fg-str)}
a{color:var(--link);border-bottom:1px solid var(--linkline)}
a:hover{border-bottom-color:var(--link)}
.lnk,.nav a,.tags li,.rt a,.pt a,.swm,.tswitch,.softtop code,.key li a{border-bottom:0}
.rt a,.pt a{border-bottom:1px solid var(--linkline)}
.nav a{font-weight:600}
.nav a.on{border-left-width:3px}
.hero .lnk{border:1px solid var(--accent);color:var(--accent)}
.hero .lnk:hover{background:var(--accent);color:var(--onaccent)}
.news .date{color:var(--fg-str);font-weight:600}
figure img{border-color:var(--line)}
"""
    return academic_vars(**kw) + extra

INKS = [
 dict(key="i01-inknavy", name="Ink · Navy", codes="A1 Navy ink · A3 CTA Blue", group="High-contrast ink",
   blurb="Full-strength navy for body text instead of a softened gray, with CTA blue links. Maximum legibility on white.",
   swatch=["#052049","#006BE9","#ffffff"],
   v=dict(bg="#fff",fg="#0d2a52",fg_str="#03142f",fg_dim="#4a5a74",line="#c8d2e0",soft="#eef2f8",
     accent="#052049",accent2="#006BE9",link="#0a49c4",link_h="#052049",
     r1=("#dde6f4","#052049"),r2=("#dbe9ff","#0a49c4"),r3=("#e8ecf2","#3f4d63"),r4=("#e2e0f4","#2E2872"))),

 dict(key="i02-inkteal", name="Ink · Teal", codes="C1 · C3 Teal · A1", group="High-contrast ink",
   blurb="C1 deep teal carried into headings and rules, not just links. Ink pushed to near-black.",
   swatch=["#0E5258","#16A0AC","#ffffff"],
   v=dict(bg="#fff",fg="#12262a",fg_str="#04181c",fg_dim="#4a6065",line="#c6d6d8",soft="#eef6f7",
     accent="#0E5258",accent2="#C42882",link="#0b5a62",link_h="#04181c",
     r1=("#daecee","#0E5258"),r2=("#fbe0ee","#a01f69"),r3=("#e9eded","#465356"),r4=("#dde6f4","#052049"))),

 dict(key="i03-inkmagenta", name="Ink · Magenta", codes="H1 · H3 Magenta · A1", group="High-contrast ink",
   blurb="Near-black ink with H3 magenta doing the accent work. The boldest of the light variants.",
   swatch=["#561038","#C42882","#ffffff"],
   v=dict(bg="#fff",fg="#231018",fg_str="#12060a",fg_dim="#5d4650",line="#dcccd3",soft="#faf1f5",
     accent="#a01f69",accent2="#0E5258",link="#a01f69",link_h="#561038",
     r1=("#fbe2ef","#8e1a5d"),r2=("#daecee","#0E5258"),r3=("#eeeaec","#54474d"),r4=("#dde6f4","#052049"))),

 dict(key="i04-groundnavy", name="Ground · Navy", codes="A1 Navy ground · C4 · B5", group="High-contrast ink",
   blurb="Navy ground with near-white ink and a bright C4 accent. Figures sit on white cards.",
   swatch=["#052049","#60D0DA","#B8E6FA"],
   v=dict(bg="#052049",fg="#dbe6f3",fg_str="#ffffff",fg_dim="#93aac6",line="#1c3f6e",soft="#0a2c5c",
     accent="#60D0DA",accent2="#FEB80A",link="#8fe0e8",link_h="#B8E6FA",chip="#0a2c5c",
     r1=("#0d3f4a","#8fe0e8"),r2=("#3d3212","#FEB80A"),r3=("#12325e","#a9bdd4"),r4=("#1b2f5e","#B8E6FA"))),

 dict(key="i05-groundink", name="Ground · Ink", codes="Black ground · E3 Chartreuse", group="High-contrast ink",
   blurb="Near-black ground with E3 chartreuse. The highest accent contrast on this list.",
   swatch=["#0b0d10","#84C234","#B4DC55"],
   v=dict(bg="#0b0d10",fg="#d2d7dc",fg_str="#ffffff",fg_dim="#8d959d",line="#242a31",soft="#12161a",
     accent="#9ada45",accent2="#60D0DA",link="#9ada45",link_h="#B4DC55",chip="#12161a",
     r1=("#22300f","#9ada45"),r2=("#0d3239","#60D0DA"),r3=("#1b2026","#9aa3ac"),r4=("#221a38","#b9a6ff"))),

 dict(key="i06-groundviolet", name="Ground · Violet", codes="G1 ground · G4 · H4", group="High-contrast ink",
   blurb="G1 deep violet ground with pale ink and a G4 accent. Warm and unusual for a dark theme.",
   swatch=["#461850","#C45ED8","#E266AE"],
   v=dict(bg="#2b0f31",fg="#e2d3e6",fg_str="#ffffff",fg_dim="#ac8fb4",line="#4a2352",soft="#37143f",
     accent="#e08cf2",accent2="#F2C2DE",link="#e08cf2",link_h="#EACCF0",chip="#37143f",
     r1=("#4a2352","#e08cf2"),r2=("#4a2340","#F2C2DE"),r3=("#3a1c41","#c4a9cb"),r4=("#23304a","#B8E6FA"))),
]

for u in INKS:
    T(key=u["key"], name=u["name"], blurb=u["blurb"], codes=u["codes"], swatch=u["swatch"],
      group=u["group"], fonts=F_MIX, css=ink_vars(**u["v"]))

# keep the three non-academic directions available
OTHER = [
 ("b-letterpress","Letterpress","Cream stock and Baskerville. Bookish and warm.",["#221d18","#7a1f1f","#f4efe6"],F_LIB),
 ("c-darklab","Dark Lab","Dark surface, mint accent, mono labels.",["#0b0f10","#4ade80","#161b1d"],F_SANS),
 ("d-soft","Soft Modern","Fraunces headings, indigo accent, rounded surfaces.",["#1e1b34","#5b46c9","#faf9fc"],F_FR),
]

for th in THEMES:
    th["shell"] = (lambda f: (lambda p, b: page(p, b, f)))(th["fonts"])
