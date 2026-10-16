#!/usr/bin/env python3
"""Content-only pages for the existing EON Reality WordPress site.

Each file is the hero through the last content section. No header, no menu,
no logo bar, and no footer. Elementor Pro already supplies those.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OVERVIEW = ROOT.parent
OUT = OVERVIEW / "wordpress"
SITE = "https://eon-reality-website.vercel.app"
ASSETS = f"{SITE}/assets"
IMAGES = f"{SITE}/site"
WP = "https://eonreality.com"

# Draft file -> page on the current EON Reality site.
# Slugs checked against the live WordPress page list on 16 Oct 2026
# are marked live. The others are the address to use when the page is added.
PAGES = {
    "index.html": f"{WP}/",
    "education.html": f"{WP}/education/",
    "government.html": f"{WP}/government/",
    "story.html": f"{WP}/story/",
    "platform.html": f"{WP}/one-platform/",
    "learn.html": f"{WP}/learn/",
    "train.html": f"{WP}/train/",
    "perform.html": f"{WP}/perform/",
    "achieve.html": f"{WP}/achieve/",
    "pricing.html": f"{WP}/product-pricing/",
    "contact.html": f"{WP}/connect-with-us/",
    "demo.html": f"{WP}/eon-demo-clinic/",
    "videos.html": f"{WP}/platform-in-action/",
    "news.html": f"{WP}/news/",
    "partners.html": f"{WP}/value-added-resellers/",
    "sign-in.html": f"{WP}/sign-in/",
    "about.html": f"{WP}/about/",
    "privacy.html": f"{WP}/privacy-policy/",
    "terms.html": f"{WP}/terms-of-use/",
    "universal.html": f"{WP}/eon-universal/",
    "components.html": f"{WP}/3d-components/",
    "mirror.html": f"{WP}/mirror-direct/",
    "studio.html": f"{WP}/mirror-studio/",
    "model.html": f"{WP}/model-inside/",
    "worlds.html": f"{WP}/worlds/",
    "xr.html": f"{WP}/eon-xr-infinite/",
    "live.html": f"{WP}/eon-live/",
    "tacit.html": f"{WP}/eon-tacit/",
    "genesis.html": f"{WP}/genesis-3/",
    "controlroom.html": f"{WP}/eon-control-room/",
    "situation.html": f"{WP}/situation-room/",
    "creator.html": f"{WP}/situation-room-creator/",
    "brainy.html": f"{WP}/brainy-soft-skills/",
    "permit.html": f"{WP}/permit-iq/",
    "field.html": f"{WP}/field-iq/",
    "edge.html": f"{WP}/field-iq-edge/",
    "assess.html": f"{WP}/assess-iq-2/",
    "compound.html": f"{WP}/compound-iq/",
    "distillery.html": f"{WP}/the-distillery/",
    "competence.html": f"{WP}/competence-iq/",
    "control.html": f"{WP}/eon-control/",
    "career.html": f"{WP}/eon-career-compass/",
    "venture.html": f"{WP}/eon-venture-builder/",
    "fluency.html": "https://eonglobalcampus.com/ai-fluency",
    "sentient.html": f"{WP}/eon-sentient-worlds/",
}


def split_blocks(css):
    blocks = []
    buf = []
    depth = 0
    for char in css:
        buf.append(char)
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                blocks.append("".join(buf).strip())
                buf = []
    tail = "".join(buf).strip()
    if tail:
        blocks.append(tail)
    return blocks


def prefix_selector(selector, scope):
    selector = selector.strip()
    if selector in ("html", "body", ":root"):
        return scope
    for token in ("html", "body", ":root"):
        if selector.startswith(token):
            rest = selector[len(token):]
            if rest.startswith((".", "#", "[", ":")):
                return scope + rest
            rest = rest.strip()
            return scope if not rest else f"{scope} {rest}"
    if selector == "*":
        return f"{scope}, {scope} *"
    return f"{scope} {selector}"


def split_selectors(selectors):
    parts = []
    buf = []
    depth = 0
    for char in selectors:
        if char == "(":
            depth += 1
        elif char == ")":
            depth = max(0, depth - 1)
        if char == "," and depth == 0:
            parts.append("".join(buf))
            buf = []
            continue
        buf.append(char)
    if buf:
        parts.append("".join(buf))
    return parts


def prefix_list(selectors, scope):
    return ", ".join(prefix_selector(part, scope) for part in split_selectors(selectors) if part.strip())


def prefix_block(block, scope):
    if block.startswith("@font-face"):
        block = block.replace("font-family:EON", 'font-family:"EON Reality Content"')
        block = block.replace("url(fonts/", f"url({ASSETS}/fonts/")
        return block
    if block.startswith("@media"):
        head, _, rest = block.partition("{")
        inner = rest[:-1] if rest.endswith("}") else rest
        inner_blocks = split_blocks(inner)
        scoped = "".join(prefix_block(part, scope) for part in inner_blocks)
        return head + "{" + scoped + "}"
    if block.startswith("@") or "{" not in block:
        return block
    head, _, body = block.partition("{")
    return prefix_list(head, scope) + " {" + body


def scope_css(css, scope):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = css.replace("EON,Arial,sans-serif", '"EON Reality Content",Arial,sans-serif')
    css = css.replace("font-family:EON", 'font-family:"EON Reality Content"')
    return "".join(prefix_block(block, scope) for block in split_blocks(css) if block.strip())


def rewrite_html(main, filename):
    def href(match):
        value = match.group(1)
        if value in PAGES:
            return f'href="{PAGES[value]}"'
        return match.group(0)

    def src(match):
        value = match.group(1)
        if value.startswith("images/"):
            return f'src="{IMAGES}/{value}"'
        if value.startswith("../assets/"):
            return f'src="{ASSETS}/{value[len("../assets/"):]}"'
        return match.group(0)

    main = re.sub(r'href="([^"]+)"', href, main)
    main = re.sub(r'src="([^"]+)"', src, main)
    slug = filename[:-5]
    scope = f"eon-reality-page eon-reality-page--{slug} home customer-ready"
    note = (
        "<!-- EON Reality content only. Paste this into the Elementor HTML widget. "
        "Do not add a header, menu, logo bar, or footer. "
        f"Load {slug}.css on this page only. -->\n"
    )
    return (
        note
        + f'<link rel="stylesheet" href="{slug}.css" />\n'
        + f'<div class="{scope}" id="eon-reality-{slug}">\n'
        + main.strip()
        + "\n</div>\n"
    )


def main():
    OUT.mkdir(exist_ok=True)
    site_css = (OVERVIEW / "assets" / "site.css").read_text()
    refresh_css = (ROOT / "refresh.css").read_text()
    pages = sorted(ROOT.glob("*.html"))
    count = 0
    for path in pages:
        html = path.read_text()
        found = re.search(r"<main id=\"main\">(.*)</main>", html, re.S)
        if not found:
            raise SystemExit(f"No main content in {path.name}")
        slug = path.stem
        scope = f".eon-reality-page--{slug}"
        css = scope_css(site_css + "\n" + refresh_css, scope)
        (OUT / f"{slug}.css").write_text(css)
        (OUT / f"{slug}.html").write_text(rewrite_html(found.group(1), path.name))
        count += 1
    sample = (OUT / "learn.html").read_text()
    checks = [
        "<header" not in sample,
        "<footer" not in sample,
        "brand-logo" not in sample,
        'class="eon-reality-page eon-reality-page--learn' in sample,
        "https://eonreality.com/eon-universal/" in sample,
        f"{IMAGES}/images/learn-shelf.jpg" in sample,
    ]
    css_sample = (OUT / "learn.css").read_text()
    checks.append(".eon-reality-page--learn .shelf-hero" in css_sample)
    checks.append("body{" not in css_sample)
    if not all(checks):
        raise SystemExit(f"Export checks failed: {checks}")
    print(f"{count} WordPress content pages")


if __name__ == "__main__":
    main()
