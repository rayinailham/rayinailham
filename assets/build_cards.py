"""Generate the project card SVGs in assets/cards/ (dark + light). Run: python3 assets/build_cards.py"""
import hashlib
import random
from html import escape
from pathlib import Path

OUT = Path(__file__).parent / "cards"

THEMES = {
    "dark": dict(bg0="#0b1226", bg1="#111c3d", border="#24345f", title="#eef3ff", text="#9fb0d6",
                 chip_bg="#18254a", chip_text="#c9d8f7", star="#dbe7ff", flow="#7f9bd6"),
    "light": dict(bg0="#ffffff", bg1="#f3f6fd", border="#d5deef", title="#0f1d40", text="#55678f",
                  chip_bg="#e8eefa", chip_text="#24345f", star="#7d93c4", flow="#55678f"),
}
ACCENT = {
    "flagship": {"dark": "#4f8ef7", "light": "#2563eb"},
    "ai": {"dark": "#a78bfa", "light": "#7c3aed"},
    "creative": {"dark": "#f5c451", "light": "#b7791f"},
}
PILL = {
    "live": ("● LIVE", "#22c55e"),
    "private": ("PRIVATE", "#8b9bbf"),
    "wip": ("WIP", "#f59e0b"),
    "mvp": ("MVP", "#38bdf8"),
    "founder": ("FOUNDER", "#f5c451"),
}

CARDS = [
    # slug, kind, wide, title, tagline, pill, chips, flow
    ("futureguide", "flagship", True, "FutureGuide", "founded it. architected it. ship it. run it.", "founder",
     ["Go", "RAG", "Gemini", "Docker", "QRIS"], "atlas · apollo · argus · athena"),
    ("kairos", "ai", True, "Kairos", "a desktop app that finds the moment in a long VOD", "wip",
     ["Python", "PyQt6", "yt-dlp", "FFmpeg", "LLM"], "VOD → transcript + chat hype → clip package"),
    ("observatory", "creative", False, "Rayin Observatory", "a portfolio you visit at night", "live", ["R3F", "GSAP", "Lenis"], None),
    ("kanon", "ai", False, "Kanon", "an interviewer, not a quiz", "private", ["TypeScript", "RabbitMQ", "Gemini"], None),
    ("monopoli", "creative", False, "Monopoli Nusantara", "board game night, online", "mvp", ["Go", "WebSocket", "React"], None),
    ("clip-autosubs", "ai", False, "Clip-Autosubs", "captions that bounce", None, ["WhisperX", "FFmpeg", "CUDA"], None),
]

# Automation Gallery: numbers come from each project's README demo run (Testing/*).
GALLERY = ("gallery", "Automation Gallery", "five systems. every number proven.", [
    ("50,000", "forms sent, killed twice,", "0 duplicates", "SURGELINE"),
    ("1,080", "QA combos per sweep,", "in 3.8 min", "CROSSCHECK"),
    ("11/11", "planted breakages", "caught, 0 false alarms", "DRIFTWATCH"),
    ("300", "brand screenshots,", "zero clicks", "BRANDWALL"),
])

BEYOND = ("beyond", [
    ("FOUNDER", "FutureGuide", "backend · architecture · devops", "flagship"),
    ("CLIPPER", "Hololive streams", "After Effects · Premiere", "creative"),
    ("SPEAKS", "id · en · ja", "native · business · learning", "ai"),
])

MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
SANS = "-apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"


def constellation(slug, x0, y0, w, h, color):
    rnd = random.Random(hashlib.md5(slug.encode()).hexdigest())
    pts = [(x0 + rnd.random() * w, y0 + rnd.random() * h) for _ in range(5)]
    pts.sort()
    lines = "".join(
        f'<line x1="{a[0]:.0f}" y1="{a[1]:.0f}" x2="{b[0]:.0f}" y2="{b[1]:.0f}"/>' for a, b in zip(pts, pts[1:]))
    dots = "".join(
        f'<circle class="s{i % 3}" cx="{x:.0f}" cy="{y:.0f}" r="{rnd.choice([2, 2.5, 3.2])}"/>' for i, (x, y) in enumerate(pts))
    return (f'<g stroke="{color}" stroke-opacity=".35" stroke-width="1.4">{lines}</g>'
            f'<g fill="{color}">{dots}</g>')


def card(slug, kind, wide, title, tagline, pill, chips, flow, theme):
    t, accent = THEMES[theme], ACCENT[kind][theme]
    W, H = (1200, 230) if wide else (600, 270)
    title_size, tag_size, chip_size = (50, 26, 20) if wide else (44, 25, 20)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{escape(title)}: {escape(tagline)}">',
        f"<title>{escape(title)}: {escape(tagline)}</title>",
        f'<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{t["bg0"]}"/><stop offset="1" stop-color="{t["bg1"]}"/></linearGradient></defs>',
        "<style>.s0,.s1,.s2{animation:tw 4s ease-in-out infinite}.s1{animation-duration:5.5s;animation-delay:-2s}"
        ".s2{animation-duration:3.2s;animation-delay:-1s}@keyframes tw{0%,100%{opacity:.9}50%{opacity:.3}}"
        "@media (prefers-reduced-motion: reduce){.s0,.s1,.s2{animation:none}}</style>",
        f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="18" fill="url(#g)" stroke="{t["border"]}" stroke-width="2"/>',
        f'<rect x="1" y="30" width="6" height="{H - 60}" rx="3" fill="{accent}"/>',
    ]
    if wide:
        parts.append(constellation(slug, W - 330, 40, 280, 90, accent))
    else:
        parts.append(constellation(slug, W - 210, 150, 170, 55, accent))
    parts.append(f'<text x="44" y="{80 if wide else 84}" font-family="{SANS}" font-size="{title_size}" font-weight="800" fill="{t["title"]}">{escape(title)}</text>')
    parts.append(f'<text x="46" y="{124 if wide else 128}" font-family="{SANS}" font-size="{tag_size}" fill="{t["text"]}">{escape(tagline)}</text>')
    if pill:
        label, color = PILL[pill]
        pw = len(label) * 10 + 26
        parts.append(f'<rect x="{W - pw - 28}" y="26" width="{pw}" height="30" rx="15" fill="{color}" fill-opacity=".15" stroke="{color}" stroke-opacity=".6"/>')
        parts.append(f'<text x="{W - 28 - pw / 2}" y="46" font-family="{MONO}" font-size="15" font-weight="700" fill="{color}" text-anchor="middle" letter-spacing="1">{label}</text>')
    x, y = 44, H - 52
    cw = chip_size * 0.6
    for c in chips:
        w = len(c) * cw + 28
        parts.append(f'<rect x="{x}" y="{y}" width="{w:.0f}" height="34" rx="8" fill="{t["chip_bg"]}"/>')
        parts.append(f'<text x="{x + w / 2:.0f}" y="{y + 23}" font-family="{MONO}" font-size="{chip_size}" fill="{t["chip_text"]}" text-anchor="middle">{escape(c)}</text>')
        x += w + 10
    if flow:
        parts.append(f'<text x="{W - 44}" y="{H - 30}" font-family="{MONO}" font-size="19" fill="{t["flow"]}" text-anchor="end">{escape(flow)}</text>')
    parts.append("</svg>\n")
    return "\n".join(parts)


def frame(W, H, label, t, accent):
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{escape(label)}">',
        f"<title>{escape(label)}</title>",
        f'<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{t["bg0"]}"/><stop offset="1" stop-color="{t["bg1"]}"/></linearGradient></defs>',
        f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="18" fill="url(#g)" stroke="{t["border"]}" stroke-width="2"/>',
        f'<rect x="1" y="30" width="6" height="{H - 60}" rx="3" fill="{accent}"/>',
    ]


def gallery(slug, title, tagline, stats, theme):
    t, accent = THEMES[theme], ACCENT["creative"][theme]
    W, H = 1200, 330
    label = f"{title}: {tagline} " + "; ".join(f"{s[3].title()}: {s[0]} {s[1]} {s[2]}" for s in stats)
    parts = frame(W, H, label, t, accent)
    parts.append(f'<text x="44" y="80" font-family="{SANS}" font-size="50" font-weight="800" fill="{t["title"]}">{escape(title)}</text>')
    parts.append(f'<text x="46" y="122" font-family="{SANS}" font-size="26" fill="{t["text"]}">{escape(tagline)}</text>')
    tw, gap, x = 262, 18, 44
    for big, l1, l2, name in stats:
        parts.append(f'<rect x="{x}" y="152" width="{tw}" height="146" rx="12" fill="{t["chip_bg"]}"/>')
        parts.append(f'<text x="{x + 20}" y="178" font-family="{MONO}" font-size="14" letter-spacing="2" fill="{accent}">{name}</text>')
        parts.append(f'<text x="{x + 18}" y="230" font-family="{SANS}" font-size="46" font-weight="800" fill="{t["title"]}">{escape(big)}</text>')
        parts.append(f'<text x="{x + 20}" y="258" font-family="{SANS}" font-size="18" fill="{t["text"]}">{escape(l1)}</text>')
        parts.append(f'<text x="{x + 20}" y="282" font-family="{SANS}" font-size="18" fill="{t["text"]}">{escape(l2)}</text>')
        x += tw + gap
    parts.append("</svg>\n")
    return "\n".join(parts)


def beyond(slug, tiles, theme):
    t = THEMES[theme]
    W, H = 1200, 190
    label = "Beyond code: " + "; ".join(f"{a.title()}: {b}, {c}" for a, b, c, _ in tiles)
    parts = frame(W, H, label, t, ACCENT["flagship"][theme])
    tw, gap, x = 360, 18, 44
    for role, what, how, kind in tiles:
        accent = ACCENT[kind][theme]
        parts.append(f'<rect x="{x}" y="28" width="{tw}" height="134" rx="12" fill="{t["chip_bg"]}"/>')
        parts.append(f'<text x="{x + 22}" y="62" font-family="{MONO}" font-size="16" letter-spacing="3" fill="{accent}">{role}</text>')
        parts.append(f'<text x="{x + 22}" y="106" font-family="{SANS}" font-size="32" font-weight="800" fill="{t["title"]}">{escape(what)}</text>')
        parts.append(f'<text x="{x + 22}" y="140" font-family="{SANS}" font-size="19" fill="{t["text"]}">{escape(how)}</text>')
        x += tw + gap
    parts.append("</svg>\n")
    return "\n".join(parts)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for old in OUT.glob("*.svg"):
        old.unlink()
    for theme in THEMES:
        for spec in CARDS:
            (OUT / f"{spec[0]}-{theme}.svg").write_text(card(*spec, theme))
        (OUT / f"{GALLERY[0]}-{theme}.svg").write_text(gallery(*GALLERY, theme))
        (OUT / f"{BEYOND[0]}-{theme}.svg").write_text(beyond(*BEYOND, theme))
    print(f"wrote {len(list(OUT.glob('*.svg')))} cards to {OUT}")
