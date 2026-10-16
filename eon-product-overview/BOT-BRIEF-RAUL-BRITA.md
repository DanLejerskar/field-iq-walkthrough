# Bot brief for Raul and Brita

Session: bc-9af26ec8-156f-45cc-a72f-3555ea5c589c
Session name: EON Reality Revamp
Date: 16 Oct 2026
Audience: Raul, Brita, and the agents they run.

This file is the job. A person does not paste paragraphs into WordPress. An agent reads this file, works in Git, and stops where this file says to stop.

The cover note is COVER-EMAIL-BOTS.md in this same folder. It has not been sent.

## 1. What Dan wants

The website to develop is the HTML preview already built on this branch. The colors, the type, the hero layout, and the four shelves are part of that website. They are not a suggestion beside another design.

Open the base here:

https://htmlpreview.github.io/?https://raw.githubusercontent.com/DanLejerskar/field-iq-walkthrough/cursor/eon-product-overview-589c/eon-product-overview/site/index.html

The Learn shelf Dan named:

https://htmlpreview.github.io/?https://raw.githubusercontent.com/DanLejerskar/field-iq-walkthrough/cursor/eon-product-overview-589c/eon-product-overview/site/learn.html

The same pages are also at https://eon-reality-website.vercel.app

The live site to cross-check is https://eonreality.com/

Brita's notes of 14 Oct 2026 and 15 Oct 2026 say Phase 1 of a WordPress refresh is live: a new homepage, short product pages, See in Action, and Education and Government. Those notes are the clarification the team wrote. Dan's instruction on 16 Oct 2026 is to start from the HTML preview, then review that live site and list what is missing. He and the team will decide together what to keep and what to retire. The agent does not retire a page on its own.

## 2. How the agent works

1. Clone the repo and check out this branch.

```bash
git clone https://github.com/DanLejerskar/field-iq-walkthrough.git
cd field-iq-walkthrough
git checkout cursor/eon-product-overview-589c
```

2. Read, in this order: this file, HANDOVER.md, eon-product-overview/site/build.py.
3. Change pages by editing build.py. If the look changes, edit site/refresh.css. From eon-product-overview/site/, run `python3 build.py`. It must exit 0.
4. Commit on this branch and push. Open the Vercel project eon-reality-website and promote the Preview to Production, or set that project's Production Branch to `cursor/eon-product-overview-589c`.
5. Fetch https://eonreality.com/ and the HTML preview with the agent. Write the difference into a file in this folder. Do not decide the difference by memory.
6. Stop before deleting a live page, changing a price, or replacing eonreality.com. Put the choice in the decision list and wait for Dan.

Rules the builder already enforces:

- No em dash and no en dash in generated HTML.
- Do not write the retired product name Assist IQ into generated HTML.
- Links between our pages stay relative. Do not put # in a link to another page.
- Keep noindex until Dan says the draft is public.

Leave these alone:

- https://field-iq-walkthrough.vercel.app and the Vercel project field-iq-walkthrough.
- .github/workflows/publish-overview.yml. Do not enable GitHub Pages.
- Do not merge this branch to main until Dan has walked through the draft.

Installed tools: Git, Python 3, and a browser. build.py uses the Python standard library only.

## 3. The look that stays

These values are in eon-product-overview/assets/site.css and site/refresh.css. Keep them.

- Page background #070c19
- Panels #0e1830
- Lines #29364e
- Text #f4f6ff
- Secondary text #aebbd2
- Blue #51aeff
- Green #a5e461
- Violet #a688ff
- Focus outline #ffc975
- Typeface: Titillium Web, stored as the family name EON

The logo is the official white wordmark at eon-product-overview/assets/brand/eon-reality-logo-white.png. Header height is 56px. Do not put back a typed wordmark. Do not put back the old navy and maroon.

Heroes: daylight stills. Words on the left. The photo sits on the right, about 58 percent of the hero, so the people and the action stay visible. A solid #070c19 panel covers the words and fades out by the middle. Under 600px the photo is full width above the words. Do not move the headline under the photo. Do not put the photo back under a full-width dark panel.

## 4. Eight-second hero films

Add one 8-second film for each of these heroes. The still stays as the poster. The film does not replace the YouTube product films on videos.html.

| Page | Still the film must match |
| --- | --- |
| education.html | site/images/education-experience.jpg |
| government.html | site/images/government-story.jpg |
| learn.html | site/images/learn-shelf.jpg |
| train.html | site/images/train-shelf.jpg |
| perform.html | site/images/perform-shelf.jpg |
| achieve.html | site/images/achieve-shelf.jpg |

The agent generates each film with a video model. Spec:

- Length: 8 seconds.
- Silent. Loop. Muted. No burned-in words, captions, or logo.
- Daylight. Same people, place, and action as the still.
- The important action stays on the right side of the frame, because the left side is covered by the text panel.
- MP4, H.264. Save under eon-product-overview/site/videos/ with a clear file name, for example learn-hero.mp4.
- In build.py, the hero uses a video element with the existing still as the poster, autoplay, muted, loop, playsinline.
- Rebuild with python3 build.py.

If the agent has no video model, it stops and says so in the commit message and in the decision file. It does not download a stock clip. It does not rename a still and call it a film. It does not swap in a YouTube id and call that the hero.

The product films already on videos.html stay YouTube links. Four products still have no film in that set: Career Compass, Venture Builder, AI Fluency, Sentient Worlds. Do not invent those links.

## 5. What I checked on 16 Oct 2026

I opened the HTML preview and the live site on the same day as this brief.

The HTML preview home and the live home now share the same story sentences: "From the jobs of the future. To the education of today.", the connected journey, Learn, Train, Perform, Achieve, and the 8 Oct 2026 Demo Clinic line. https://eonreality.com/home-latest/ carries that same story. The live home also still shows blocks that are not in the HTML preview: Scan to Experience, a Proven at Scale row that rendered as zeros, and a logo row titled Trusted by 1000s of Organisations in the World.

https://eonreality.com/learn/ matches the HTML preview Learn shelf: the same headline and the same nine product lines, from EON Universal through EON Tacit.

https://eonreality.com/eon-xr-infinite/ uses the short draft line "Name a subject. Make room for discovery." and points at YouTube for soft skills, hard skills, and the next generation of EON-XR.

https://eonreality.com/platform-in-action/ says there is a short video for each product and names the four Achieve products that have no film yet.

https://eonreality.com/education/ is still the older education page. It still says students learn 4x faster, learning effectiveness increases by 76 percent, students are more keen by 97 percent, and it quotes David Hornsby of Carleton University. It still splits University, TVET / CTE, Community Colleges, K-12, and Custom Academic Courses.

https://eonreality.com/government/ is still the older government page. It is about SkillBuild SPV, lenders, WIOA, IRA, and CHIPS. It is not the humble government story in government.html.

I did not receive a separate attachment beyond the two addresses Dan sent and the team notes already in Drive. The team notes I used are:

- EON Reality Website Response, 14 Oct 2026, owned by brita@eonreality.com
- EON Reality Website Response, 15 Oct 2026, owned by brita@eonreality.com
- hub_missing_products_pricing.xlsx, owned by brita@eonreality.com

## 6. On the live site, missing from the HTML preview

The agent lists these. Dan decides. The agent does not copy them in until he says yes.

Working systems Brita said are already live:

- Forms connected to Radar, tested.
- Email notice to marketing, Brita, and Dan when a form is submitted.
- The news archive, including the press releases already on the site.
- Events pages.
- Demo Clinic registration. The 9 Oct and 15 Oct registrations were removed.
- SEO on the WordPress site.
- Automatic translation.

Older blocks still on the public URLs I opened:

- Scan to Experience and the QR flow.
- Proven at Scale counters. On 16 Oct 2026 they rendered as zero.
- The organisation logo row.
- The older /education/ page, including the 4x, 76 percent, and 97 percent lines and the named quote.
- The older /government/ page about SkillBuild SPV.
- Solutions pages for academia, enterprise, government, and B2C.
- EON Classic and EON Spatial pages.
- The pricing calculator.
- A second price system in hub_missing_products_pricing.xlsx: site fees and seat fees from eonenterprisehub.com, plus rows marked as suggested. The HTML preview keeps the published per-user prices from https://eonreality.com/product-pricing/. Do not replace those with the spreadsheet. Do not publish a suggested price.
- Pages that still use retired or folded names: Assist IQ, Genesis Trainer 2.0, Genesis Simulator 3.0, Custom Virtual Builder, EON Spark, Brainy Mentor PRO, and other old product URLs still in WordPress.

## 7. In the HTML preview, missing on the live site

These are part of the base. The agent keeps them while the live site catches up.

- The dark cinematic look, the color values in section 3, and the official white wordmark.
- Heroes with the photo on the right and the words on the left.
- Eight-second hero films for education, government, learn, train, perform, and achieve. Neither site has these yet.
- education.html and government.html as the humble stories. The live /education/ and /government/ URLs are different pages.
- One platform page, with one sentence only: Learn and train in the Digital Twin. Perform in the Work Loop. Achieve is what you take with you.
- Competence IQ and EON Control in a shared strip under Perform. They are not a fifth column. The left rail stays out.
- 26 product pages generated from build.py, with the longer description and the YouTube buttons.
- The price page that follows https://eonreality.com/product-pricing/. Fifteen products say "Scoped with the institution" because no separate published line was used.
- Contact facts from the current site, with both Irvine suites still shown: Suite 173 and Suite 110. Dan has not picked one.
- Privacy and terms marked DRAFT FOR COUNSEL, linking to the live policies. Do not paste the legal text.
- Partners as a link to https://eonreality.com/value-added-resellers/ only. Do not copy names, phone numbers, or email addresses.
- French and Simplified Chinese as doors to https://eonreality.com/?lang=fr and https://eonreality.com/?lang=zh-hans. Do not machine-translate the 45 draft pages.
- noindex, nofollow on the draft.

## 8. Decision list

The agent writes this list into eon-product-overview/DECISION-LIST.md after it rechecks both sites. It does not check the boxes. Dan and the team check them together.

For each row, the only allowed marks are: Keep, Retire, or Ask Dan.

| Item | Where it is now | Proposed mark until Dan says otherwise |
| --- | --- | --- |
| HTML preview look, colors, logo, hero layout | Draft | Keep |
| Four shelves: Learn, Train, Perform, Achieve | Draft and parts of the live site | Keep |
| Humble education story | education.html | Keep |
| Humble government story | government.html | Keep |
| Older /education/ claims and quote | eonreality.com/education/ | Ask Dan |
| Older /government/ SkillBuild page | eonreality.com/government/ | Ask Dan |
| Scan to Experience and QR | Live home | Ask Dan |
| Proven at Scale counters | Live home, rendering as zero | Ask Dan |
| Organisation logo row | Live home | Ask Dan |
| Radar forms and mail notices | Live WordPress | Ask Dan |
| News archive and events | Live WordPress | Ask Dan |
| Demo Clinic registration | Live WordPress | Ask Dan |
| Automatic translation | Live WordPress | Ask Dan |
| Per-user prices from product-pricing | Draft pricing page | Keep |
| Enterprise hub site fees and suggested prices | Brita's spreadsheet | Ask Dan |
| Assist IQ pages | Live WordPress | Retire when Dan confirms the pages can come down |
| Folded names: EON XR, EON AI, Genesis Trainer, Genesis Simulator, Custom Virtual Builder | Older live URLs | Ask Dan |
| Eight-second hero films | Missing on both | Keep, and the agent adds them |
| YouTube product films | Draft videos.html and live platform-in-action | Keep |
| Four Achieve films still missing | Both | Ask Dan for the URLs |
| Suite 173 or Suite 110 | Both addresses on the draft | Ask Dan |
| Replace eonreality.com with this draft | Not done | Ask Dan |
| noindex on the draft | Draft | Keep until Dan says it is public |

## 9. What the agent does next, in order

1. Recheck the six hero pages on both sites and confirm section 5 still matches. If a live page has changed, update DECISION-LIST.md and stop for Dan before editing the story.
2. Generate the six 8-second films to the spec in section 4. Wire them in build.py. Run python3 build.py. Commit and push.
3. Do not import the older education page, the older government page, the zero counters, the named quote, or a suggested price.
4. Open a note in the commit that lists any live block the agent could not classify. That note is for the meeting. It is not a license to delete the block.

## 10. Files to open first

| File | Why |
| --- | --- |
| eon-product-overview/BOT-BRIEF-RAUL-BRITA.md | This job. |
| eon-product-overview/COVER-EMAIL-BOTS.md | The note for Raul and Brita. Not sent. |
| eon-product-overview/HANDOVER.md | Locked products, prices, films, and how to publish. |
| eon-product-overview/site/build.py | The pages. |
| eon-product-overview/site/refresh.css | The look that wins over site.css. |
