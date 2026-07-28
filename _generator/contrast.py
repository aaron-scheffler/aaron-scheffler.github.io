# -*- coding: utf-8 -*-
"""Darken --fg / --fg-dim until they clear a contrast target against --bg."""
import re

def _hex(h):
    h = h.strip().lstrip('#')
    if len(h) == 3: h = "".join(c*2 for c in h)
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def _lum(rgb):
    c = [x/255 for x in rgb]
    c = [x/12.92 if x <= .03928 else ((x+.055)/1.055)**2.4 for x in c]
    return .2126*c[0] + .7152*c[1] + .0722*c[2]

def ratio(a, b):
    l1, l2 = sorted([_lum(_hex(a)), _lum(_hex(b))], reverse=True)
    return (l1+.05)/(l2+.05)

def _mix(rgb, t):
    """t=0 -> unchanged, t=1 -> black. Preserves hue by scaling channels."""
    return tuple(max(0, min(255, round(c*(1-t)))) for c in rgb)

def _tint(rgb, t):
    """t=0 -> unchanged, t=1 -> white."""
    return tuple(max(0, min(255, round(c + (255-c)*t))) for c in rgb)

def lighten_to(colour, bg, target):
    if ratio(colour, bg) >= target:
        return colour
    rgb = _hex(colour)
    for i in range(1, 101):
        hx = "#%02x%02x%02x" % _tint(rgb, i/100)
        if ratio(hx, bg) >= target:
            return hx
    return "#ffffff"

def darken_to(colour, bg, target):
    """Return colour darkened just enough to hit `target` contrast on bg."""
    if ratio(colour, bg) >= target:
        return colour
    rgb = _hex(colour)
    for i in range(1, 101):
        cand = _mix(rgb, i/100)
        hx = "#%02x%02x%02x" % cand
        if ratio(hx, bg) >= target:
            return hx
    return "#000000"

VAR = lambda css, n: (re.search(r'--%s:\s*([^;}\n]+)' % n, css) or [None, None])[1]

def boost(css, fg_target=13.0, dim_target=8.0):
    """Rewrite --fg and --fg-dim in a stylesheet if the ground is light."""
    bg, fg, dim = VAR(css, 'bg'), VAR(css, 'fg'), VAR(css, 'fg-dim')
    if not (bg and fg and dim) or not bg.startswith('#'):
        return css, None
    move = lighten_to if _lum(_hex(bg)) < 0.5 else darken_to
    nfg = move(fg.strip(), bg, fg_target)
    ndim = move(dim.strip(), bg, dim_target)
    css = re.sub(r'(--fg:\s*)[^;}\n]+', r'\g<1>' + nfg, css, count=1)
    css = re.sub(r'(--fg-dim:\s*)[^;}\n]+', r'\g<1>' + ndim, css, count=1)
    return css, (bg, fg.strip(), nfg, dim.strip(), ndim)
