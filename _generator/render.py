# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,"/sessions/hopeful-ecstatic-brown/mnt/outputs/build")
from content import *

IMG = "../shared/images/"

def links_html(cls="lnk"):
    return "".join('<a class="%s" href="%s"%s>%s</a>' %
        (cls, u, ' target="_blank" rel="noopener"' if u.startswith("http") else "", n)
        for n, u in LINKS)

def nav_html(active, cls="nav"):
    return "".join('<a href="%s"%s>%s</a>' % (u, ' class="on" aria-current="page"' if u==active else "", n)
                   for u, n in NAV)

def portrait(cls="portrait"):
    return '<img class="%s" src="%sheadshot.jpg" alt="Portrait of Aaron Wolfe Scheffler">' % (cls, IMG)

# ---------- shared content blocks ----------
def hero(show_portrait=True):
    p = portrait() if show_portrait else ""
    return f"""<header class="hero">
  {p}
  <div class="hero-txt">
    <h1>{NAME}</h1>
    <p class="role">{ROLE} &middot; {DEPT}<br>{INST}</p>
    <p class="tag">{TAG}</p>
    <nav class="links">{links_html()}</nav>
  </div>
</header>"""

def facts():
    return '<ul class="facts">' + "".join(
        f'<li><b>{a}</b><span>{b}</span></li>' for a, b in FACTS) + '</ul>'

def bio():
    return '<div class="prose">' + "".join(f"<p>{p}</p>" for p in BIO) + '</div>'

def _news_link(html):
    for frag, url in NEWS_LINK.items():
        if frag in html:
            return f' The manuscript can be viewed <a href="{url}" target="_blank" rel="noopener">here</a>.'
    return ""

def news(limit=None):
    items = NEWS[:limit] if limit else NEWS
    o = ['<section class="block" id="news"><h2>News</h2><ol class="news">']
    for d, kind, html, flag in items:
        extra = _news_link(html) if kind == "paper" else ""
        fl = f'<span class="filled">{flag}</span>' if flag else ''
        o.append(f'<li class="n-{kind}"><div class="ntop"><span class="date">{d}</span>'
                 f'<span class="kind k-{kind}">{NEWS_KIND[kind]}</span>{fl}</div>'
                 f'<div class="what">{html}{extra}</div></li>')
    o.append('</ol></section>')
    return "".join(o)

def research_body(figures=True):
    o = [f'<section class="block"><h1 class="ptitle">Research</h1><p class="lede">{RESEARCH_INTRO}</p></section>']
    o.append('<nav class="areanav">' + "".join(
        f'<a href="#{a["id"]}"><b>{a["n"]}</b>{a["t"]}</a>' for a in AREAS) + '</nav>')
    for a in AREAS:
        fig = ""
        if figures:
            fig = (f'<figure><img src="{IMG}{a["img"]}" alt="{a["alt"]}" loading="lazy" '
                   f'style="aspect-ratio:{a["ratio"]}"><figcaption>{a["cap"]}</figcaption></figure>')
        tags = '<ul class="tags">' + "".join(f"<li>{t}</li>" for t in a["tags"]) + "</ul>"
        rel = ""
        if a.get("pubs"):
            rows = []
            for slug in sorted(a["pubs"], key=lambda k: -M[k][0]):
                y, t, au, ven, det, url, role = M[slug]
                wip = ' <span class="wip">Working paper</span>' if ven == "Preprint" else ''
                lab = f'<a href="{url}" target="_blank" rel="noopener">{t}</a>' if url else t
                vtxt = ven if ven != "Preprint" else (det or "Preprint")
                rows.append(f'<li><span class="ry">{y}</span><div class="rt">{lab}{wip}</div>'
                            f'<div class="rv">{vtxt}</div></li>')
            rel = ('<section class="related"><h3>Related publications</h3>'
                   '<ol class="rlist">' + "".join(rows) + '</ol></section>')
        paras = "".join(f"<p>{p}</p>" for p in a["body"])
        o.append(f"""<article class="area" id="{a['id']}">
  <div class="area-head"><span class="areanum">{a['n']}</span><h2>{a['t']}</h2></div>
  {fig}
  <div class="prose">{paras}</div>
  {tags}
  {rel}
</article>""")
    return "".join(o)

def _year_blocks(rows):
    o = []
    for y in sorted({r[0] for r in rows}, reverse=True):
        rs = [r for r in rows if r[0] == y]
        o.append(f'<section class="yr"><div class="yrlab"><span>{y}</span>'
                 f'<em>{len(rs)} paper{"s" if len(rs)>1 else ""}</em></div><ol class="ylist">')
        for _, t, au, ven, det, url, role in rs:
            head = f'<a href="{url}" target="_blank" rel="noopener">{t}</a>' if url else t
            meta = f'<em>{ven}</em>' + (f' &middot; {det}' if det else '')
            o.append(f'<li class="pub">'
                     f'<div class="pt">{head}</div><div class="pa">{au}</div>'
                     f'<div class="pj">{meta}</div></li>')
        o.append('</ol></section>')
    return "".join(o)

def pubs_body():
    published = [m for m in METHODS if m[3] != "Preprint"]
    working   = [m for m in METHODS if m[3] == "Preprint"]
    o = [f'<section class="block"><h1 class="ptitle">Publications</h1><p class="lede">{PUB_INTRO}</p>']
    o.append('</section>')
    o.append(f'<section class="pubsec"><div class="sechead"><h2>Published</h2>'
             f'<span class="seccount">{len(published)} papers</span></div>'
             f'<div class="pubs">{_year_blocks(published)}</div></section>')
    o.append(f'<section class="pubsec"><div class="sechead"><h2>Working papers</h2>'
             f'<span class="seccount">{len(working)} in review or preparation</span></div>'
             f'<p class="sublede">Preprints and manuscripts under review.</p>'
             f'<div class="pubs">{_year_blocks(working)}</div></section>')

    o.append(f'<p class="note">{PUB_NOTE}</p>')
    return "".join(o)

def people_body():
    o = [f'<section class="block"><h1 class="ptitle">People</h1><p class="lede">{PEOPLE_INTRO}</p></section>']
    for grp in PEOPLE:
        o.append(f'<section class="pgroup"><h2 class="glab">{grp["group"]}</h2><div class="plist">')
        for m in grp["members"]:
            links = "".join(
                f'<a class="lnk" href="{u}"{" target=_blank rel=noopener" if u.startswith("http") else ""}>{n}</a>'
                for n, u in m["links"])
            o.append(f"""<article class="person">
  <img class="pphoto" src="{IMG}{m['img']}" alt="Portrait of {m['name']}" loading="lazy">
  <div class="pbody"><h3>{m['name']}</h3><div class="prole">{m['role']}</div>
  <p>{m['bio']}</p><nav class="links">{links}</nav></div>
</article>""")
        o.append('</div></section>')
    o.append(f'<section class="block join"><p>{PEOPLE_JOIN}</p></section>')
    return "".join(o)

def teach_body():
    o = [f'<section class="block"><h1 class="ptitle">Teaching</h1><p class="lede">{TEACH_INTRO}</p></section>',
         '<div class="courses">']
    for code, t, when, role, d, ev, u in COURSES:
        evh = f'<div class="evals">{ev}</div>' if ev else ''
        o.append(f"""<article class="course">
  <div class="chead"><code class="ccode">{code}</code><span class="cwhen">{when}</span></div>
  <h2>{t}</h2><div class="crole">{role}</div><p>{d}</p>{evh}
  <a href="{u}" target="_blank" rel="noopener">Course description &rarr;</a>
</article>""")
    o.append('</div>')
    o.append(f'<section class="block"><p class="outro">{TEACH_OUTRO}</p></section>')
    return "".join(o)

def home_body(**kw):
    return hero(True) + '<section class="block">' + bio() + '</section>' + news()

PAGES = ["index.html", "research.html", "publications.html", "people.html", "teaching.html"]

def body_for(page, **kw):
    return {"index.html": home_body, "research.html": research_body,
            "publications.html": pubs_body, "people.html": people_body,
            "teaching.html": teach_body}[page]()

def title_for(page):
    n = {"index.html": None, "research.html": "Research", "publications.html": "Publications",
         "people.html": "People", "teaching.html": "Teaching"}[page]
    return NAME if n is None else f"{n} &middot; {NAME}"
