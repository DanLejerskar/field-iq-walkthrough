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
    contact_current = ' aria-current="page"' if active == "contact.html" else ""
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <a class="wordmark brand-logo" href="index.html" aria-label="EON Reality home"><img src="{LOGO}" alt="EON Reality" /></a>
  <nav aria-label="Primary">{''.join(links)}</nav>
  <div class="header-actions">
    <a class="header-contact" href="contact.html"{contact_current}>Contact</a>
    <a class="header-action" href="platform.html">One platform <span>↗</span></a>
  </div>
</header>'''


def footer():
    return f'''<footer class="site-footer">
  <a href="index.html"><img src="{LOGO}" alt="EON Reality" /></a>
  <nav aria-label="Footer">
    <a href="story.html">The story in one page</a>
    <a href="platform.html">One platform</a>
    <a href="pricing.html">Pricing</a>
    <a href="{CAMPUS}">Global Virtual Campus</a>
    <a href="{LONG}/">The long platform</a>
    <a href="contact.html">Contact</a>
    <a href="demo.html">Demo</a>
    <a href="news.html">News</a>
    <a href="partners.html">Partners</a>
    <a href="sign-in.html">Sign in</a>
    <a href="about.html">About</a>
    <a href="privacy.html">Privacy</a>
    <a href="terms.html">Terms</a>
    <a href="https://eonreality.com/?lang=fr">French</a>
    <a href="https://eonreality.com/?lang=zh-hans">Chinese</a>
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
<link rel="icon" href="favicon.png" type="image/png" />
<link rel="apple-touch-icon" href="apple-touch-icon.png" />
<link rel="stylesheet" href="../assets/site.css" />
<link rel="stylesheet" href="refresh.css?v=finish" />
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

# Second paragraph on each product page. Only actions already implied by the promise and body.
DOING = {
    "universal": "Choose the place, the captured reference, the model, or the world the lesson needs. The five modules stay inside Universal.",
    "components": "Turn one reviewed object, name it, and come back to the same component when the lesson continues.",
    "mirror": "Start the class from a captured place or object, and keep that reference faithful to what was recorded.",
    "studio": "Prepare a captured reference for a lesson. The capture stays intact. The teaching is added on purpose.",
    "model": "Move inside a model, see how the parts relate, and leave with the explanation still attached.",
    "worlds": "Enter a place, discover it through a mission, and return to the same world later.",
    "xr": "Name a subject, explore its parts in space, and return to an explanation.",
    "live": "Show how an action, the state of the equipment, and the next safe decision relate.",
    "tacit": "Keep the exact words of someone who knows, and ask a second person to verify the claim before it is reused.",
    "genesis": "Give someone a place to practise from reviewed curriculum, source material, or a procedure, then look at the decisions they made.",
    "controlroom": "Connect operator, field, command, and instructor views in one virtual operation, and practise the system as a team.",
    "situation": "Examine an incident, weigh the evidence, and talk through the decision before the pressure is real.",
    "creator": "Bring reviewed courses, scenarios, and learning experiences into a space shaped around the institution.",
    "brainy": "Rehearse a conversation with people who respond, then review how the person listened, explained, and handled competing concerns.",
    "permit": "Look at the job, its controls, and the supporting evidence together. Authorised people remain in charge.",
    "field": "Follow a guided task from preparation and training into field use, and see how that task is monitored and reviewed.",
    "edge": "Open a prepared example of step-by-step assistance when the cloud connection is gone.",
    "assess": "Bring the task, a recorded run, and its result together so a learner and an assessor can review the evidence.",
    "compound": "Look at the difference between the plan and what happened, and keep the safe, repeated lessons ready for a governed update.",
    "distillery": "Turn a bounded source into an evidence package that accountable people can review, test, and release on purpose.",
    "competence": "Open a record that connects a task, an assessment, and an accountable decision, and inspect the evidence.",
    "control": "Find the activity, review progress, and open the evidence behind a result.",
    "career": "See a path from what a person can do to work and income.",
    "venture": "Take a local problem and shape it into a venture someone can start.",
    "fluency": "Practise working with intelligent tools as a skill of its own, underneath the rest of the curriculum.",
    "sentient": "Return to a subject as a world after the session ends, so the learning stays available.",
}

# One more paragraph, taken from a page that is already public. No new claims.
MORE = {
    "universal": "The public customer page says five connected modules turn equipment, references, and places into one starting point a learner can explore.",
    "components": "The public customer page calls this a library of objects that explain themselves.",
    "mirror": "The public customer page starts from reference images and keeps a model that can still be edited.",
    "studio": "The public customer page says every part is reviewed before learners rely on it.",
    "model": "The public customer page keeps the same promise: open the object, and understand the system.",
    "worlds": "The public customer page keeps the same promise: start with a place, and discover it through a mission.",
    "xr": "The public customer page says a learner meets a subject in space, explores its parts, and can return to the explanation.",
    "live": "The public customer page says Live makes the link between an action, the state of the equipment, and the next safe decision visible.",
    "tacit": "The public customer page says the exact words stay, and a second person checks the claim before it is reused.",
    "genesis": "The public customer page says a learner practises from reviewed curriculum, source material, or a procedure, and then the decisions are reviewed.",
    "controlroom": "The public customer page connects operator, field, command, and instructor views in one virtual operation.",
    "situation": "The public customer page says a team examines an incident, weighs the evidence, and discusses the decision before the pressure is real.",
    "creator": "The public customer page says reviewed courses, scenarios, and learning experiences sit in a space shaped around the institution.",
    "brainy": "The public customer page says the rehearsal is with people who respond, and then you review how the person listened, explained, and handled competing concerns.",
    "permit": "The public customer page connects the job, its controls, and the supporting evidence. Authorised people remain in charge.",
    "field": "The public customer page follows a guided task from preparation and training into field use, and into how that task is reviewed.",
    "edge": "The public customer page shows a prepared example of step-by-step assistance when the cloud connection is gone.",
    "assess": "The public customer page puts the briefing, the recorded task, and the result together so an assessor can review the evidence.",
    "compound": "The public customer page looks at the difference between the intended task and what happened before the guidance is changed.",
    "distillery": "The public customer page turns a reviewed lesson into a package only after accountable people review it, test it, and release it.",
    "competence": "The public customer page connects a task, an assessment, and an accountable decision in a record people can inspect.",
    "control": "The public customer page says a team finds the activity, reviews progress, and opens the evidence behind a result.",
    "career": "The published Career Compass page describes a path in this order: look at current skills, name a direction, see the gap, gather the learning, practise, keep a record of that learning, and match the skills to work. That page remains the full story.",
    "venture": "The published Venture Builder page describes five steps: find a local problem worth solving, start from a prepared pattern for that kind of problem, check that the idea can work, repeat what works in a similar place, and offer it where people can use it. A person does not need to be a programmer to start. That page remains the full story.",
    "fluency": "The published campus page describes 100 courses in five groups, from someone who is just starting to someone who can lead and build with these tools. Each group has something to learn, something to practise, and a result the person can show. That page remains the full story.",
    "sentient": "The published Sentient Worlds page describes four steps: a short film of the topic, a conversation that stays with the topic, a place you can walk through in a browser, and the same place on a phone. That page remains the full story.",
}

SHELF_IMAGE = {
    "learn": "images/learn-shelf.jpg?v=daylight",
    "train": "images/train-shelf.jpg?v=daylight",
    "perform": "images/perform-shelf.jpg?v=daylight",
    "achieve": "images/achieve-shelf.jpg?v=daylight",
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
        return f"images/{product['slug']}.jpg?v=daylight"
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
  <div class="hero-art"><img alt="Three people around a luminous campus model in daylight." src="images/home-hero.jpg?v=daylight" width="1536" height="864" /></div>
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
  <img src="images/education-experience.jpg?v=daylight" alt="A learner and an educator study a luminous heart." />
  <div class="copy"><p class="eyebrow">FOR EDUCATION</p><h2>Help people learn by experiencing.</h2><p>A heart becomes a spatial lesson. A historical place becomes an investigation. A practical procedure becomes something a learner can rehearse. The Global Virtual Campus is the place they enter.</p><p class="actions"><a class="button primary" href="education.html">The education story</a></p></div>
</section>
<section class="band reverse">
  <div class="copy"><p class="eyebrow">FOR GOVERNMENT</p><h2>Build public-service capability that lasts.</h2><p>The same story, told for institutions. Preserve experience, rehearse the difficult conversation, and help people prepare for a responsibility that has a name.</p><p class="actions"><a class="button primary" href="government.html">The government story</a></p></div>
  <img src="images/government-story.jpg?v=daylight" alt="Three public servants around a city model in daylight." />
</section>
<section class="plain"><p class="eyebrow">THE SHELVES</p><h2>Learn. Train. Perform. Achieve.</h2><p>This is the only product map. The path above is the story. These four words are how you choose. Learn and train use the Digital Twin. Perform uses the Work Loop. Achieve is what a person takes with them.</p></section>
<div class="doors">
  <a class="door" href="learn.html"><img src="images/learn-shelf.jpg?v=daylight" alt="" /><span><strong>Learn</strong><em>See the subject, the place, and the knowledge.</em></span></a>
  <a class="door" href="train.html"><img src="images/train-shelf.jpg?v=daylight" alt="" /><span><strong>Train</strong><em>Practise the task, the decision, and the conversation.</em></span></a>
  <a class="door" href="perform.html"><img src="images/perform-shelf.jpg?v=daylight" alt="" /><span><strong>Perform</strong><em>Do the work, then show the evidence.</em></span></a>
  <a class="door" href="achieve.html"><img src="images/achieve-shelf.jpg?v=daylight" alt="" /><span><strong>Achieve</strong><em>Get the job, and secure it.</em></span></a>
</div>
<section class="plain">
  <p class="eyebrow">FROM THE CURRENT SITE</p>
  <h2>News that is already public.</h2>
  <p>This draft links to posts that are already on eonreality.com. It does not replace that site.</p>
  <p class="actions"><a class="button secondary" href="news.html">See the news</a></p>
</section>
<div class="news-list">
  <a class="news-row" href="https://eonreality.com/eon-launches-demo-clinics-to-showcase-the-full-one-platform-portfolio/"><strong>8 Oct 2026. Demo Clinics for the whole platform.</strong><em>The opening session was led on 9 Oct 2026. Weekly clinics follow.</em></a>
</div>
<section class="plain">
  <p class="eyebrow">STILL ON THE CURRENT SITE</p>
  <h2>Partners, French, and Chinese.</h2>
  <p>The partner list stays on eonreality.com. This draft does not copy the names or the contact details. The current website is also published in French and in Simplified Chinese. This draft is English only. Those buttons open the current site. They are not a translation of these pages.</p>
  <p class="actions"><a class="button secondary" href="partners.html">Partners</a><a class="button secondary" href="https://eonreality.com/?lang=fr">French on the current site</a><a class="button secondary" href="https://eonreality.com/?lang=zh-hans">Chinese on the current site</a></p>
</section>
<section class="plain start-here">
  <p class="eyebrow">START HERE</p>
  <h2>The next step is a conversation.</h2>
  <p>The four shelves are the product map. If you are an institution, tell us the need first. Include the institution, the need, and whether this is education or government.</p>
  <p class="actions"><a class="button primary" href="contact.html">Request a conversation</a><a class="button secondary" href="story.html">The story in one page</a></p>
</section>
'''
    shell("index.html", "From the jobs of the future", body)


def build_story_pages():
    shell("education.html", "Education", f'''
<section class="product-hero"><img src="images/education-experience.jpg?v=daylight" alt="" /><div class="veil"></div>
  <div class="copy"><p class="eyebrow">FOR EDUCATION</p><h1>Help people learn by experiencing.</h1>
  <p class="hero-description">Connect abstract ideas with memorable experiences. Give learners a place to practise and a way to discuss how they performed.</p></div>
</section>
<section class="plain"><p>See the subject. A heart becomes a spatial lesson. A historical place becomes an investigation. A practical procedure becomes something a learner can rehearse.</p>
<p>The Global Virtual Campus is where that learning is entered. It is a place, not a fifth product shelf.</p>
<p>When you want to talk, say that the conversation is for education. Include the institution and the need.</p>
<p class="actions"><a class="button primary" href="{CAMPUS}">Open the Global Virtual Campus</a><a class="button secondary" href="learn.html">Go to Learn</a><a class="button secondary" href="contact.html">Request a conversation</a></p></section>
''')
    shell("government.html", "Government", '''
<section class="product-hero"><img src="images/government-story.jpg?v=daylight" alt="" /><div class="veil"></div>
  <div class="copy"><p class="eyebrow">FOR GOVERNMENT</p><h1>Build public-service capability that lasts.</h1>
  <p class="hero-description">Preserve institutional experience, rehearse decisions, and help people prepare for clearly defined responsibilities.</p></div>
</section>
<section class="plain"><p>Imagine a public-service academy where people learn from experienced colleagues, practise difficult conversations, and discuss evidence before a high-pressure decision.</p>
<p>The shape is the same as education. Listen first. Move from explanation to experience. Make progress visible.</p>
<p>When you want to talk, say that the conversation is for government. Include the institution and the need.</p>
<p class="actions"><a class="button primary" href="train.html">Situation Room and practice</a><a class="button secondary" href="learn.html">Tacit and the lessons</a><a class="button secondary" href="contact.html">Request a conversation</a></p></section>
''')
    shell("story.html", "The story in one page", '''
<section class="plain"><p class="eyebrow">THE STORY IN ONE PAGE</p><h1>From the jobs of the future to the education of today.</h1>
<p>We start with employers and communities, not with a prescription for the institution. Knowledge still matters. So does the ability to use it.</p>
<p>The journey is understand, experience, practise, demonstrate, improve. People examine an object, enter a setting, rehearse a conversation, and practise a decision. Educators stay in charge of the learning.</p>
<p>Education and government share that story. The campus is the place a learner enters. The products are chosen on four shelves only: Learn, Train, Perform, Achieve.</p>
<p>Learn and train happen in the Digital Twin. Perform happens in the Work Loop. Achieve is what a person takes with them: the job, and the security of being able to show the evidence.</p>
<p class="actions"><a class="button primary" href="contact.html">Request a conversation</a><a class="button secondary" href="platform.html">One platform</a><a class="button secondary" href="index.html">Back to the opening</a></p></section>
''')
    shell("platform.html", "One platform", '''
<section class="product-hero"><img src="images/platform.jpg?v=daylight" alt="A campus model and a work folder on one table." /><div class="veil"></div>
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
        doing = DOING[product["slug"]]
        more = MORE[product["slug"]]
        body = f'''
<section class="product-hero"><img src="{image}" alt="" /><div class="veil"></div>
  <div class="copy"><p class="eyebrow">{e(product["shelf_name"].upper())}</p><h1>{e(product["name"])}</h1>
  <p class="hero-description">{e(product["promise"])}</p></div>
</section>
<section class="product-body"><p>{e(product["body"])}</p>
<p>{e(more)}</p>
<p>What you can do here. {e(doing)}</p>
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
<p>Learn, Train, Perform, and Achieve are the only groups. A single public price list is not invented here. Each engagement is scoped with the institution after the need is clear. The descriptions on these pages are the ones the price must match.</p>
<p>To ask for that conversation, include the institution, the need, and whether it is education or government.</p>
<p class="actions"><a class="button primary" href="contact.html">Request a conversation</a></p></section>
''' + "".join(groups)
    shell("pricing.html", "Pricing", body)


def build_public_pages():
    shell("contact.html", "Contact", '''
<section class="plain">
  <p class="eyebrow">CONTACT</p>
  <h1>Request a conversation.</h1>
  <p>We listen first. If you are with a university, a school, or a public institution, ask for a conversation about education or about government. We start from the need.</p>
  <p>For this draft, email <a href="mailto:dan@eonreality.com">dan@eonreality.com</a>. Include the institution, the need, and whether the conversation is for education or for government.</p>
  <p>The office details below are copied from the current public website. The contact page lists Suite 173. The privacy policy lists Suite 110 at the same street. Both are shown until the suite is confirmed.</p>
</section>
<div class="fact-grid">
  <article class="fact"><strong>Email</strong><p>General: <a href="mailto:info@eonreality.com">info@eonreality.com</a><br/>Sales: <a href="mailto:sales@eonreality.com">sales@eonreality.com</a><br/>This draft: <a href="mailto:dan@eonreality.com">dan@eonreality.com</a></p></article>
  <article class="fact"><strong>Phone and hours</strong><p><a href="tel:+19494602000">+1 (949) 460-2000</a><br/>Monday to Friday, 9am to 5pm PT</p></article>
  <article class="fact"><strong>Address on the contact page</strong><p>18 Technology Drive, Suite 173<br/>Irvine, CA 92618</p></article>
  <article class="fact"><strong>Address on the privacy policy</strong><p>18 Technology Drive, Suite 110<br/>Irvine, CA 92618<br/>Also listed there: <a href="mailto:contact@eonreality.com">contact@eonreality.com</a> and <a href="mailto:privacy@eonreality.com">privacy@eonreality.com</a></p></article>
</div>
<section class="plain">
  <p class="actions"><a class="button primary" href="mailto:dan@eonreality.com">Email dan@eonreality.com</a><a class="button secondary" href="https://eonreality.com/connect-with-us/">Open the current contact page</a><a class="button secondary" href="demo.html">Request a demo</a></p>
</section>
''')
    shell("demo.html", "Demo", '''
<section class="plain">
  <p class="eyebrow">DEMO</p>
  <h1>See it on the current website.</h1>
  <p>This draft does not host the demo form. The button below opens the published demo page on eonreality.com.</p>
  <p>That page offers two paths. A shorter discovery conversation. A longer hands-on session that uses material from the institution.</p>
  <p>There is also a Demo Clinic series. The opening session was Friday 9 Oct 2026 at 11:30 CEST. Weekly clinics were planned from 15 Oct 2026. The clinic page is where the time and the registration live.</p>
  <p class="actions"><a class="button primary" href="https://eonreality.com/schedule-a-free-demo/">Open the published demo page</a><a class="button secondary" href="https://eonreality.com/eon-demo-clinic/">Open the Demo Clinic</a><a class="button secondary" href="news.html">Read the 8 Oct announcement</a></p>
</section>
''')
    shell("news.html", "News", '''
<section class="plain">
  <p class="eyebrow">NEWS</p>
  <h1>Posts that are already public.</h1>
  <p>These links go to eonreality.com. This draft does not add new posts, and it does not replace the current site.</p>
</section>
<div class="news-list">
  <a class="news-row" href="https://eonreality.com/eon-launches-demo-clinics-to-showcase-the-full-one-platform-portfolio/"><strong>8 Oct 2026. EON launches Demo Clinics.</strong><em>A series to show the whole platform. Dan Lejerskar led the opening session on 9 Oct 2026. Weekly product clinics were planned after that.</em></a>
  <a class="news-row" href="https://eonreality.com/eon-demo-clinic/"><strong>Demo Clinic page.</strong><em>The place to see the series and the registration. Opening time listed there: Friday 9 Oct 2026, 11:30 CEST.</em></a>
</div>
<section class="plain">
  <p>More news stays on the current website.</p>
  <p class="actions"><a class="button primary" href="https://eonreality.com/">Open eonreality.com</a><a class="button secondary" href="demo.html">Request a demo</a></p>
</section>
''')
    shell("sign-in.html", "Sign in", '''
<section class="plain">
  <p class="eyebrow">SIGN IN</p>
  <h1>Use the published sign-in pages.</h1>
  <p>This draft does not ask for a password. The current website points people to these two places.</p>
  <p class="actions"><a class="button primary" href="https://eon-xr.com/">Open eon-xr.com</a><a class="button secondary" href="https://core.eon-xr.com/">Open core.eon-xr.com</a></p>
  <p>If you are not sure which one you need, start with a conversation instead of guessing.</p>
  <p class="actions"><a class="button secondary" href="contact.html">Request a conversation</a></p>
</section>
''')
    shell("about.html", "About", '''
<section class="plain">
  <p class="eyebrow">ABOUT</p>
  <h1>Who EON Reality is.</h1>
  <p>EON Reality works with education and with government. The work is to connect what employers and communities need with learning people can see, explore, practise, and demonstrate.</p>
  <p>We listen first. We do not arrive with a finished prescription for a university or a public institution. Educators and institutions stay in charge of the learning.</p>
  <p>The journey is understand, experience, practise, demonstrate, improve. The Global Virtual Campus is the place a learner enters. Learn, Train, Perform, and Achieve are the shelves.</p>
  <p class="actions"><a class="button primary" href="story.html">The story in one page</a><a class="button secondary" href="contact.html">Request a conversation</a></p>
</section>
''')
    shell("privacy.html", "Privacy", '''
<section class="plain">
  <p class="eyebrow">DRAFT FOR COUNSEL</p>
  <h1>Privacy</h1>
  <p>This is a short plain-language draft for counsel. It is not a finished privacy notice.</p>
  <p>These pages are a draft reading copy. They do not ask you to create an account, and they do not include a form or a tracker. If you email dan@eonreality.com, that message is ordinary email. It leaves this site.</p>
  <p>The pages ask search engines not to index this draft. Wait to send confidential material until the institution has agreed what may be shared.</p>
  <p>Counsel needs to review this draft before anyone treats it as policy. It cites no statute.</p>
  <p>The privacy policy that is already public stays on the current website. This draft does not replace it, and it does not copy that policy onto this page.</p>
  <p class="actions"><a class="button primary" href="https://eonreality.com/privacy-policy/">Open the published privacy policy</a></p>
</section>
''')
    shell("terms.html", "Terms", '''
<section class="plain">
  <p class="eyebrow">DRAFT FOR COUNSEL</p>
  <h1>Terms</h1>
  <p>This is a short plain-language draft for counsel. It is not a finished set of terms.</p>
  <p>The pages explain how EON Reality describes education and government. They are a draft for review. They are not an offer, and they are not a promise that a product will be delivered in a particular form.</p>
  <p>Pricing on this site says each engagement is scoped with the institution. No public price is set here. Product names and short descriptions are for orientation. The longer review of the platform lives on its own site.</p>
  <p>Counsel needs to replace this draft before anyone relies on it. It cites no statute.</p>
  <p>The terms of use that are already public stay on the current website. This draft does not replace them, and it does not copy those terms onto this page.</p>
  <p class="actions"><a class="button primary" href="https://eonreality.com/terms-of-use/">Open the published terms</a></p>
</section>
''')
    shell("partners.html", "Partners", '''
<section class="plain">
  <p class="eyebrow">PARTNERS</p>
  <h1>The partner list stays on the current website.</h1>
  <p>EON Reality works with partners in many countries. The published list, including how to reach each partner, stays on eonreality.com.</p>
  <p>This draft does not copy partner names, phone numbers, or email addresses. Open the current page to see them.</p>
  <p class="actions"><a class="button primary" href="https://eonreality.com/value-added-resellers/">Open the partner list</a><a class="button secondary" href="contact.html">Request a conversation</a></p>
</section>
''')


def main():
    missing = [slug for slug in (p["slug"] for p in PRODUCTS) if slug not in DOING or slug not in MORE]
    if missing:
        raise SystemExit(f"missing doing text: {missing}")
    build_home()
    build_story_pages()
    build_shelves()
    build_products()
    build_pricing()
    build_public_pages()
    pages = list(ROOT.glob("*.html"))
    text = "\n".join(p.read_text() for p in pages)
    if "—" in text or "–" in text or "Assist IQ" in text:
        raise SystemExit("copy check failed")
    footer_html = (ROOT / "index.html").read_text().split("<footer", 1)[1]
    for href in (
        "story.html",
        "platform.html",
        "pricing.html",
        "contact.html",
        "demo.html",
        "news.html",
        "partners.html",
        "sign-in.html",
        "about.html",
        "privacy.html",
        "terms.html",
        "https://eonreality.com/?lang=fr",
        "https://eonreality.com/?lang=zh-hans",
        CAMPUS,
        f"{LONG}/",
    ):
        if href not in footer_html:
            raise SystemExit(f"footer missing {href}")
    if 'content="noindex, nofollow"' not in text:
        raise SystemExit("noindex missing")
    for name in ("contact.html", "about.html", "privacy.html", "terms.html"):
        if "DRAFT FOR COUNSEL" not in (ROOT / name).read_text() and name in ("privacy.html", "terms.html"):
            raise SystemExit(f"draft marking missing {name}")
    if "mailto:dan@eonreality.com" not in (ROOT / "contact.html").read_text():
        raise SystemExit("contact mailto missing")
    privacy = (ROOT / "privacy.html").read_text()
    terms = (ROOT / "terms.html").read_text()
    partners = (ROOT / "partners.html").read_text()
    if "https://eonreality.com/privacy-policy/" not in privacy:
        raise SystemExit("privacy link missing")
    if "https://eonreality.com/terms-of-use/" not in terms:
        raise SystemExit("terms link missing")
    if "https://eonreality.com/value-added-resellers/" not in partners or "@" in partners:
        raise SystemExit("partners page check failed")
    allowed_hash = 'href="#main"'
    if text.replace(allowed_hash, "").find('href="#') != -1:
        raise SystemExit("hash fragment")
    print(f"{len(pages)} pages")


if __name__ == "__main__":
    main()
