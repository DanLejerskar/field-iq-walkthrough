#!/usr/bin/env python3
"""Build the EON Reality story site. One shell, four shelves, one page per product."""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LOGO = "../assets/brand/eon-reality-logo-white.png"
LONG = "https://eon-education-government-review.vercel.app"
CAMPUS = "https://eonglobalcampus.com/"

NAV = [
    ("education.html", "Education"),
    ("government.html", "Government"),
    ("learn.html", "Learn"),
    ("train.html", "Train"),
    ("perform.html", "Perform"),
    ("achieve.html", "Achieve"),
]


def e(text):
    return escape(text, quote=True)


def header(active):
    links = []
    for href, label in NAV:
        current = ' aria-current="page"' if href == active else ""
        links.append(f'<a href="{href}"{current}>{label}</a>')
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <a class="wordmark brand-logo" href="index.html" aria-label="EON Reality home"><img src="{LOGO}" alt="EON Reality" /></a>
  <nav aria-label="Primary">{''.join(links)}</nav>
  <a class="header-action" href="platform.html">One platform <span>↗</span></a>
</header>'''


def footer():
    return f'''<footer class="site-footer">
  <a href="index.html"><img src="{LOGO}" alt="EON Reality" /></a>
  <nav aria-label="Footer">
    <a href="story.html">The story in one page</a>
    <a href="pricing.html">Pricing</a>
    <a href="{CAMPUS}">Global Virtual Campus</a>
    <a href="{LONG}/">The long platform</a>
  </nav>
</footer>'''


def shell(filename, title, body):
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<meta name="robots" content="noindex, nofollow" />
<title>{e(title)} · EON Reality</title>
<link rel="stylesheet" href="../assets/site.css" />
<link rel="stylesheet" href="refresh.css" />
</head>
<body class="home customer-ready">
{header(filename)}
<main id="main">
{body}
</main>
{footer()}
</body>
</html>
'''
    (ROOT / filename).write_text(doc)
    return doc


PRODUCTS = [
    # Learn
    dict(slug="universal", shelf="learn", shelf_name="Learn", name="EON Universal",
         promise="Make real places and objects part of the lesson.",
         body="Bring real places, captured references, internal models, and explorable objects into one starting point. Five modules sit inside Universal: 3D Components, Mirror Direct, Mirror Studio, Model Inside, and Worlds.",
         long="universal"),
    dict(slug="components", shelf="learn", shelf_name="Learn", name="3D Components",
         promise="Start with the object the lesson needs.",
         body="A reviewed component becomes something a learner can turn, name, and return to. It lives inside EON Universal, not as a separate product family.",
         long="components"),
    dict(slug="mirror", shelf="learn", shelf_name="Learn", name="Mirror Direct",
         promise="Bring a real reference into the lesson.",
         body="A captured place or object stays faithful to what was recorded, so the class begins from something real.",
         long="mirror"),
    dict(slug="studio", shelf="learn", shelf_name="Learn", name="Mirror Studio",
         promise="Shape a captured place for teaching.",
         body="Studio is where a reference is prepared for a lesson, with the capture kept intact and the teaching added on purpose.",
         long="studio"),
    dict(slug="model", shelf="learn", shelf_name="Learn", name="Model Inside",
         promise="Open the object. Understand the system.",
         body="A learner moves inside a model, sees how the parts relate, and comes back out with the explanation still attached.",
         long="model"),
    dict(slug="worlds", shelf="learn", shelf_name="Learn", name="Worlds",
         promise="Start with a place. Discover through a mission.",
         body="A place becomes a world a learner can enter, explore, and return to. Worlds sits inside Universal.",
         long="worlds"),
    dict(slug="xr", shelf="learn", shelf_name="Learn", name="EON XR Infinite",
         promise="Name a subject. Make room for discovery.",
         body="A learner meets a subject in space, explores its parts, and returns to an explanation. EON XR and EON AI fold into this product.",
         long="xr"),
    dict(slug="live", shelf="learn", shelf_name="Learn", name="EON Live",
         promise="Make changing conditions visible.",
         body="Show the relationship between an action, the state of the equipment, and the next safe decision. Live sits with Control Room: one for the conditions, one for the team.",
         long="live"),
    dict(slug="tacit", shelf="learn", shelf_name="Learn", name="EON Tacit",
         promise="Keep the experience that never made it into the handbook.",
         body="Interview the people who know, keep their exact words, and ask a second person to verify the claims. Tacit and Brainy Soft Skills are two products.",
         long="tacit"),
    # Train
    dict(slug="genesis", shelf="train", shelf_name="Train", name="Genesis 3",
         promise="Turn knowledge into something you can practise.",
         body="Use reviewed curriculum, source material, or a procedure to give someone a place to practise, then look at the decisions they made. Genesis Trainer and Genesis Simulator become Genesis 3.",
         long="genesis"),
    dict(slug="controlroom", shelf="train", shelf_name="Train", name="EON Control Room",
         promise="Understand the system. Practise as a team.",
         body="Connect operator, field, command, and instructor views in one virtual operation. The team practises the system together.",
         long="controlroom"),
    dict(slug="situation", shelf="train", shelf_name="Train", name="Situation Room",
         promise="Practise judgement before the difficult moment.",
         body="A team examines an incident, weighs the evidence, and talks through the decision before the pressure is real.",
         long="situation"),
    dict(slug="creator", shelf="train", shelf_name="Train", name="Situation Room Creator",
         promise="The institution's place to train and perform.",
         body="Bring reviewed courses, scenarios, and learning experiences into a space shaped around the institution.",
         long="creator"),
    dict(slug="brainy", shelf="train", shelf_name="Train", name="Brainy Soft Skills",
         promise="Practise the conversations that change outcomes.",
         body="Rehearse with people who respond to what is said. Review how the person listened, explained, and handled competing concerns. Brainy is not a replacement for Tacit.",
         long="brainy"),
    # Perform
    dict(slug="permit", shelf="perform", shelf_name="Perform", name="Permit IQ",
         promise="Understand how controlled work is prepared.",
         body="Make the job, its controls, and the supporting evidence easier to understand. Authorised people remain in charge.",
         long="permit"),
    dict(slug="field", shelf="perform", shelf_name="Perform", name="Field IQ",
         promise="Bring guidance into practical work.",
         body="Connect preparation, training, field use, and monitoring so people can see how a guided task is carried out and reviewed.",
         long="field"),
    dict(slug="edge", shelf="perform", shelf_name="Perform", name="Field IQ Edge",
         promise="Guidance when a cloud connection is unavailable.",
         body="A prepared example of step-by-step assistance when the cloud connection is gone. Field IQ and Field IQ Edge are two cards.",
         long="edge"),
    dict(slug="assess", shelf="perform", shelf_name="Perform", name="Assess IQ",
         promise="Make performance visible against a clear standard.",
         body="Bring the task, a recorded run, and its result together so a learner and an assessor can review the evidence. Assess IQ stays inside the work of Perform.",
         long="assess"),
    dict(slug="compound", shelf="perform", shelf_name="Perform", name="Compound IQ",
         promise="Use reviewed lessons to improve the next practice.",
         body="Look at the difference between the plan and what happened. Keep the safe, repeated lessons ready for a governed update.",
         long="compound"),
    dict(slug="distillery", shelf="perform", shelf_name="Perform", name="The Distillery",
         promise="Prepare reviewed knowledge for careful reuse.",
         body="Turn a bounded source into an evidence package that accountable people can review, test, and release on purpose.",
         long="distillery"),
    dict(slug="competence", shelf="perform", shelf_name="Perform", name="Competence IQ",
         promise="See the evidence behind a capability.",
         body="Connect a task, an assessment, and an accountable decision in a record people can inspect. This stays in the shared strip under Perform.",
         long="competence", shared=True),
    dict(slug="control", shelf="perform", shelf_name="Perform", name="EON Control",
         promise="Keep people, learning, and results in view.",
         body="Help a team find the activity, review progress, and open the evidence behind a result. EON Control sits in the same shared strip as Competence IQ.",
         long="control", shared=True),
    # Achieve
    dict(slug="career", shelf="achieve", shelf_name="Achieve", name="Career Compass",
         promise="Skills to jobs to income.",
         body="A person can see a path from what they can do to work and income. The long story still lives on the published page until it is rebuilt here.",
         external="https://eonreality.com/eon-career-compass/"),
    dict(slug="venture", shelf="achieve", shelf_name="Achieve", name="Venture Builder",
         promise="From a local problem to a launched venture.",
         body="A local problem becomes a venture someone can actually start. The published page remains the current home of that story.",
         external="https://eonreality.com/eon-venture-builder/"),
    dict(slug="fluency", shelf="achieve", shelf_name="Achieve", name="AI Fluency",
         promise="The skill under every other skill.",
         body="Working with intelligent tools is practised as a skill of its own, underneath the rest of the curriculum. The campus page remains the current home of that story.",
         external="https://eonglobalcampus.com/ai-fluency"),
    dict(slug="sentient", shelf="achieve", shelf_name="Achieve", name="Sentient Worlds",
         promise="A topic becomes a world you can return to.",
         body="A subject stays available as a world, so learning does not end when the session ends. The published page remains the current home of that story.",
         external="https://eonreality.com/eon-sentient-worlds/"),
]

SHELF_IMAGE = {
    "learn": "images/learn-shelf.jpg",
    "train": "images/train-shelf.jpg",
    "perform": "images/perform-shelf.jpg",
    "achieve": "images/achieve-shelf.jpg",
}

SHELVES = {
    "learn": ("Learn", "See the subject, the place, and the knowledge.", "Learn is where a person meets a subject in a place they can examine. The Digital Twin is the engine under this shelf and under Train."),
    "train": ("Train", "Practise the task, the decision, and the conversation.", "Train is where knowledge becomes something a person can rehearse. It uses the same Digital Twin as Learn."),
    "perform": ("Perform", "Do the work, then show the evidence.", "Perform is the Work Loop: prepare the job, carry it out, and keep the evidence. Achieve is not part of this shelf."),
    "achieve": ("Achieve", "Get the job, and secure it.", "Achieve is what a person takes with them. It is not a third engine. Learn and train feed it. Perform makes it visible."),
}


def product_href(product):
    return f'{product["slug"]}.html'


def image_for(product):
    specific = ROOT / "images" / f"{product['slug']}.jpg"
    if specific.exists():
        return f"images/{product['slug']}.jpg"
    return SHELF_IMAGE[product["shelf"]]


def cards_for(shelf):
    bits = []
    shared_started = False
    for product in PRODUCTS:
        if product["shelf"] != shelf:
            continue
        if product.get("shared") and not shared_started:
            bits.append('<p class="group-label">Shared intelligence</p>')
            shared_started = True
        image = image_for(product)
        bits.append(
            f'<a class="card" href="{product_href(product)}"><img src="{image}" alt="" />'
            f'<div><strong>{e(product["name"])}</strong><em>{e(product["promise"])}</em></div></a>'
        )
    return '<div class="cards">' + "".join(bits) + "</div>"


def build_home():
    body = '''
<section class="cinematic-hero platform root-hero">
  <div class="hero-art"><img alt="Three people around a luminous campus model at dusk." src="images/home-hero.jpg" width="1536" height="864" /></div>
  <div class="hero-shade"></div>
  <div class="hero-copy">
    <p class="eyebrow">EON REALITY · EDUCATION FOR THE AI ERA</p>
    <h1>From the jobs of the <em>future.</em><br/>To the education of <em>today.</em></h1>
    <h2>Knowledge. Experience. Practice. Capability.</h2>
    <p class="hero-description">Connect the needs of employers and communities with learning people can see, explore, practise and demonstrate.</p>
    <div class="actions"><a class="button primary" href="education.html">Explore education <span>↓</span></a><a class="button secondary" href="learn.html">Discover the products <span>↗</span></a></div>
  </div>
  <div class="hero-caption"><span>IMAGINE THE EXPERIENCE</span><p>A campus where knowledge becomes capability.</p></div>
</section>
<div class="journey-ribbon"><span>THE CONNECTED JOURNEY</span><strong>Understand</strong><i>→</i><strong>Experience</strong><i>→</i><strong>Practise</strong><i>→</i><strong>Demonstrate</strong><i>→</i><strong>Improve</strong></div>
<section class="section story-section">
  <div class="section-heading"><div><p class="eyebrow">THE PURPOSE</p><h2>Knowledge matters.<br/>So does the ability to use it.</h2></div>
  <p>Education builds understanding, curiosity and citizenship. EON connects those foundations with the skills, judgement and practical experience people need for a changing world. We listen first. We do not arrive with a finished prescription.</p></div>
  <div class="story-grid">
    <article><span>01 / START WITH A NEED</span><h3>Listen to employers<br/>and communities.</h3><p>Identify meaningful tasks, emerging responsibilities and public needs. Use those insights to shape the capabilities learners develop.</p></article>
    <article><span>02 / MAKE LEARNING ACTIVE</span><h3>Move from explanation<br/>to experience.</h3><p>Let people examine an object, enter a setting, rehearse a conversation and practise a decision, with educators guiding the learning.</p></article>
    <article><span>03 / MAKE PROGRESS VISIBLE</span><h3>Look at what people<br/>can demonstrate.</h3><p>Review performance against a defined standard, inspect the evidence and use approved lessons to improve the next experience.</p></article>
  </div>
</section>
<section class="band">
  <img src="images/education-experience.jpg" alt="A learner and an educator study a luminous heart." />
  <div class="copy"><p class="eyebrow">FOR EDUCATION</p><h2>Help people learn by experiencing.</h2><p>A heart becomes a spatial lesson. A historical place becomes an investigation. A practical procedure becomes something a learner can rehearse. The Global Virtual Campus is the place they enter.</p><p class="actions"><a class="button primary" href="education.html">The education story</a></p></div>
</section>
<section class="band reverse">
  <div class="copy"><p class="eyebrow">FOR GOVERNMENT</p><h2>Build public-service capability that lasts.</h2><p>The same story, told for institutions. Preserve experience, rehearse the difficult conversation, and help people prepare for a responsibility that has a name.</p><p class="actions"><a class="button primary" href="government.html">The government story</a></p></div>
  <img src="images/government-story.jpg" alt="Three public servants around a city model at dusk." />
</section>
<section class="plain"><p class="eyebrow">THE SHELVES</p><h2>Learn. Train. Perform. Achieve.</h2><p>This is the only product map. The path above is the story. These four words are how you choose. Learn and train use the Digital Twin. Perform uses the Work Loop. Achieve is what a person takes with them.</p></section>
<div class="doors">
  <a class="door" href="learn.html"><img src="images/learn-shelf.jpg" alt="" /><span><strong>Learn</strong><em>See the subject, the place, and the knowledge.</em></span></a>
  <a class="door" href="train.html"><img src="images/train-shelf.jpg" alt="" /><span><strong>Train</strong><em>Practise the task, the decision, and the conversation.</em></span></a>
  <a class="door" href="perform.html"><img src="images/perform-shelf.jpg" alt="" /><span><strong>Perform</strong><em>Do the work, then show the evidence.</em></span></a>
  <a class="door" href="achieve.html"><img src="images/achieve-shelf.jpg" alt="" /><span><strong>Achieve</strong><em>Get the job, and secure it.</em></span></a>
</div>
'''
    shell("index.html", "From the jobs of the future", body)


def build_story_pages():
    shell("education.html", "Education", f'''
<section class="product-hero"><img src="images/education-experience.jpg" alt="" /><div class="veil"></div>
  <div class="copy"><p class="eyebrow">FOR EDUCATION</p><h1>Help people learn by experiencing.</h1>
  <p class="hero-description">Connect abstract ideas with memorable experiences. Give learners a place to practise and a way to discuss how they performed.</p></div>
</section>
<section class="plain"><p>See the subject. A heart becomes a spatial lesson. A historical place becomes an investigation. A practical procedure becomes something a learner can rehearse.</p>
<p>The Global Virtual Campus is where that learning is entered. It is a place, not a fifth product shelf.</p>
<p class="actions"><a class="button primary" href="{CAMPUS}">Open the Global Virtual Campus</a><a class="button secondary" href="learn.html">Go to Learn</a></p></section>
''')
    shell("government.html", "Government", '''
<section class="product-hero"><img src="images/government-story.jpg" alt="" /><div class="veil"></div>
  <div class="copy"><p class="eyebrow">FOR GOVERNMENT</p><h1>Build public-service capability that lasts.</h1>
  <p class="hero-description">Preserve institutional experience, rehearse decisions, and help people prepare for clearly defined responsibilities.</p></div>
</section>
<section class="plain"><p>Imagine a public-service academy where people learn from experienced colleagues, practise difficult conversations, and discuss evidence before a high-pressure decision.</p>
<p>The shape is the same as education. Listen first. Move from explanation to experience. Make progress visible.</p>
<p class="actions"><a class="button primary" href="train.html">Situation Room and practice</a><a class="button secondary" href="learn.html">Tacit and the lessons</a></p></section>
''')
    shell("story.html", "The story in one page", '''
<section class="plain"><p class="eyebrow">THE STORY IN ONE PAGE</p><h1>From the jobs of the future to the education of today.</h1>
<p>We start with employers and communities, not with a prescription for the institution. Knowledge still matters. So does the ability to use it.</p>
<p>The journey is understand, experience, practise, demonstrate, improve. People examine an object, enter a setting, rehearse a conversation, and practise a decision. Educators stay in charge of the learning.</p>
<p>Education and government share that story. The campus is the place a learner enters. The products are chosen on four shelves only: Learn, Train, Perform, Achieve.</p>
<p>Learn and train happen in the Digital Twin. Perform happens in the Work Loop. Achieve is what a person takes with them: the job, and the security of being able to show the evidence.</p>
<p class="actions"><a class="button primary" href="platform.html">One platform</a><a class="button secondary" href="index.html">Back to the opening</a></p></section>
''')
    shell("platform.html", "One platform", '''
<section class="product-hero"><img src="images/platform.jpg" alt="A campus model and a work folder on one table." /><div class="veil"></div>
  <div class="copy"><p class="eyebrow">ONE PLATFORM</p><h1>Four shelves. Two engines.</h1>
  <p class="hero-description">Learn and train in the Digital Twin. Perform in the Work Loop. Achieve is what you take with you.</p></div>
</section>
<section class="plain"><p>There is one platform. The public map is Learn, Train, Perform, Achieve. Those four words are the shelves.</p>
<p>Under Learn and Train, the engine is the Digital Twin: the place, the object, the practice, the conversation. Under Perform, the engine is the Work Loop: prepare the work, do it, and keep the evidence. Competence IQ and EON Control sit in a shared strip under Perform. They are not a fifth shelf.</p>
<p>Achieve is not an engine. It is the outcome the other three make visible: skills to work, a venture, fluency, a world you can return to.</p>
<p class="actions"><a class="button primary" href="learn.html">Start with Learn</a><a class="button secondary" href="pricing.html">See how pricing is grouped</a></p></section>
''')


def build_shelves():
    for key, (name, line, text) in SHELVES.items():
        body = f'''
<section class="shelf-hero"><img src="{SHELF_IMAGE[key]}" alt="" /><div class="veil"></div>
  <div class="copy"><p class="eyebrow">{e(name.upper())}</p><h1>{e(line)}</h1><p class="hero-description">{e(text)}</p></div>
</section>
{cards_for(key)}
'''
        shell(f"{key}.html", name, body)


def build_products():
    for product in PRODUCTS:
        image = image_for(product)
        if product.get("external"):
            action = f'<a class="button primary" href="{product["external"]}">Open the published page</a>'
        else:
            action = f'<a class="button primary" href="{LONG}/products/{product["long"]}.html">Open the long story</a>'
        body = f'''
<section class="product-hero"><img src="{image}" alt="" /><div class="veil"></div>
  <div class="copy"><p class="eyebrow">{e(product["shelf_name"].upper())}</p><h1>{e(product["name"])}</h1>
  <p class="hero-description">{e(product["promise"])}</p></div>
</section>
<section class="product-body"><p>{e(product["body"])}</p>
<p class="actions">{action}<a class="button secondary" href="{product["shelf"]}.html">Back to {e(product["shelf_name"])}</a></p></section>
'''
        shell(f'{product["slug"]}.html', product["name"], body)


def build_pricing():
    groups = []
    for key in ("learn", "train", "perform", "achieve"):
        name = SHELVES[key][0]
        rows = []
        for product in PRODUCTS:
            if product["shelf"] != key:
                continue
            rows.append(
                f'<a class="price-row" href="{product["slug"]}.html"><strong>{e(product["name"])}</strong><span>Scoped with the institution</span></a>'
            )
        groups.append(f'<section class="plain"><h2>{name}</h2></section><div class="price-list">{"".join(rows)}</div>')
    body = '''
<section class="plain"><p class="eyebrow">PRICING</p><h1>Grouped the same way as the shelves.</h1>
<p>Learn, Train, Perform, and Achieve are the only groups. A single public price list is not invented here. Each engagement is scoped with the institution after the need is clear. The descriptions on these pages are the ones the price must match.</p></section>
''' + "".join(groups)
    shell("pricing.html", "Pricing", body)


def main():
    build_home()
    build_story_pages()
    build_shelves()
    build_products()
    build_pricing()
    pages = list(ROOT.glob("*.html"))
    text = "\n".join(p.read_text() for p in pages)
    if "—" in text or "Assist IQ" in text:
        raise SystemExit("copy check failed")
    print(f"{len(pages)} pages")


if __name__ == "__main__":
    main()
