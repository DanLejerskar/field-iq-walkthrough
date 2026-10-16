# Handover: EON Reality draft website

Session: bc-9af26ec8-156f-45cc-a72f-3555ea5c589c
Session name: EON Reality Revamp
Date: 16 Oct 2026
Audience: the development and marketing team, and the agent that will finish this site.

Read this file before you edit anything. The cover email is COVER-EMAIL.md in this same folder.

On 16 Oct 2026 Dan asked Raul and Brita to start from this HTML preview, cross-check it with the live WordPress site, and let their agents do the work. That brief is BOT-BRIEF-RAUL-BRITA.md. The note that goes with it is COVER-EMAIL-BOTS.md. Both are drafts. Neither has been sent.

## 1. What this is

This is a draft of the public EON Reality website. It is a reading copy for review. It is not the live site.

- The new pages live in `eon-product-overview/site/`.
- `site/build.py` is the source of truth. It writes the HTML.
- The site is `noindex, nofollow`. Keep that until Dan says it is public.
- https://eonreality.com stays up. Do not replace it from this branch.

These files in `eon-product-overview/` are an older menu experiment. They are not the new website:

- `index.html`
- `phase-one.html`
- `look-refresh.html`

Do not send people to those three files.

## 2. Where the code lives

- Cloud folder: `/agent/repos/field-iq-walkthrough/eon-product-overview/site`
- GitHub: https://github.com/DanLejerskar/field-iq-walkthrough
- Branch: `cursor/eon-product-overview-589c`
- Pull request: https://github.com/DanLejerskar/field-iq-walkthrough/pull/1
- The header wordmark landed in commit `2268659`. Start from the latest commit on this branch. It includes this handover and the Vercel setup.

Clone and use this branch:

```bash
git clone https://github.com/DanLejerskar/field-iq-walkthrough.git
cd field-iq-walkthrough
git checkout cursor/eon-product-overview-589c
```

## 2a. Git is enough. Vercel is not missing.

The pages, the colors, the prices, the films, and the logo are files in this Git branch. Change the file. Push the branch. The HTML preview updates. That is the whole job.

You do not need a Vercel login to see this draft or to change it. Vercel is a second window with a shorter address. It shows the same files. If you cannot open Vercel, you are not blocked.

The repo is public, so you can already read every file:

https://github.com/DanLejerskar/field-iq-walkthrough

To save a change, push branch `cursor/eon-product-overview-589c`, or open a pull request on https://github.com/DanLejerskar/field-iq-walkthrough/pull/1. If GitHub refuses the push, ask Dan to invite your GitHub username. That invite is on GitHub. It is not a Vercel invite.

The logo you could not change before lives on a different website, the long platform at https://eon-education-government-review.vercel.app/. That site is not this folder. This draft's logo is a picture in Git. Replace the picture. You do not open Vercel.

1. Replace this file with the white logo: `eon-product-overview/assets/brand/eon-reality-logo-white.png`
2. The header size is in `eon-product-overview/site/refresh.css`, in the rule `.brand-logo img`. The height is 56px. Change that number if the logo looks too small or too big.
3. From `eon-product-overview/site/`, run `python3 build.py`. It must exit 0.
4. Commit and push this branch.
5. Wait about a minute. Open the HTML preview again. The new logo is there.

Reading link, no Vercel:

https://htmlpreview.github.io/?https://raw.githubusercontent.com/DanLejerskar/field-iq-walkthrough/cursor/eon-product-overview-589c/eon-product-overview/site/index.html

Leave https://field-iq-walkthrough.vercel.app alone. That is the Field IQ walkthrough. This draft does not use that project.

## 3. How to see it, and how to publish a change

Git is how you change the site. The steps in section 2a are enough.

A Vercel project named `eon-reality-website` also exists, separate from Field IQ. Use it only if you want the shorter address https://eon-reality-website.vercel.app. You can skip it.

Open this address:

https://eon-reality-website.vercel.app

`/` redirects to `/site/index.html`. That redirect is `eon-product-overview/vercel.json`. The folder-root `index.html` is the old menu, so the redirect keeps people on the new site.

Vercel project:

- Name: `eon-reality-website`
- Project id: `prj_YJxRhF6AhVaT4VEJUERVuFedw1sb`
- Dashboard: https://vercel.com/dans-projects-3b851cd9/eon-reality-website
- GitHub repo: `DanLejerskar/field-iq-walkthrough`
- Root directory: `eon-product-overview`
- Framework: none. The HTML is already built. There is no install and no build command.
- Deployment protection: off. No password and no Vercel login. The pages stay `noindex`.
- Production deployment is the draft branch `cursor/eon-product-overview-589c`.

Sibling pages are the same host with a different file name:

- https://eon-reality-website.vercel.app/site/videos.html
- https://eon-reality-website.vercel.app/site/pricing.html
- https://eon-reality-website.vercel.app/site/contact.html
- https://eon-reality-website.vercel.app/site/partners.html
- https://eon-reality-website.vercel.app/site/privacy.html
- https://eon-reality-website.vercel.app/site/terms.html

To publish a change:

1. Edit `site/build.py`. Run `python3 build.py` from `eon-product-overview/site/`. It must exit 0.
2. Commit and push branch `cursor/eon-product-overview-589c`.
3. Open the Vercel project above. Wait until the deployment of your commit says Ready.
4. If that deployment is Production, https://eon-reality-website.vercel.app already has it.
5. If it is a Preview, promote that deployment to Production. Promote only inside `eon-reality-website`.

A push of this branch creates a Preview, because the Vercel production branch is still `main`. The public address stays on the last Production deployment until you promote. If Promote is refused, open the project settings for `eon-reality-website` and set the Production Branch to `cursor/eon-product-overview-589c`. Do that only on this project.

The project ignores a build from every other branch. A push to `main` must not replace this URL. `vercel.json` carries the same ignore rule.

Do not create another Vercel project for this draft. Do not attach a custom domain. Do not point eonreality.com here until Dan says so.

Leave the Field IQ walkthrough alone:

- Project name: `field-iq-walkthrough`
- Project id: `prj_qdgjljRTt1Aj40XCr8OoBqF2TMur`
- Production URL: https://field-iq-walkthrough.vercel.app
- That project is connected to the same GitHub repo. A push of this branch can create a preview deployment there. Leave that preview. Do not promote it. Production on that URL is the Field IQ walkthrough, and it must stay that way.

Backup reading link, if Vercel is down:

https://htmlpreview.github.io/?https://raw.githubusercontent.com/DanLejerskar/field-iq-walkthrough/cursor/eon-product-overview-589c/eon-product-overview/site/index.html

htmlpreview rules that already bit us:

- Links between our pages must be relative, such as `learn.html`.
- Do not put `#` in a link to another page. htmlpreview rewrites any link whose address contains `#` back to the current page.
- `href="#main"` on the same page is allowed. The builder checks this.
- Do not pre-wrap links in an htmlpreview address. That double-wraps them.
- After a push, GitHub raw files can take about a minute to refresh.

Local preview, from `eon-product-overview/`:

```bash
python3 -m http.server 8765
```

Then open http://127.0.0.1:8765/site/index.html

What you need installed: Git, Python 3, and a browser. `build.py` uses the Python standard library only. There is no `package.json`, no env file, and no API key.

GitHub:

- The repo is public: https://github.com/DanLejerskar/field-iq-walkthrough
- Default branch `main` is not this website. Do not merge until Dan has walked through the draft.
- Pull request: https://github.com/DanLejerskar/field-iq-walkthrough/pull/1 (draft).
- GitHub Pages is not the reading link. The workflow `.github/workflows/publish-overview.yml` fails because Pages is not enabled. Dan said to pause that. Do not edit that workflow. Do not enable Pages.
- If you cannot see the Vercel project, ask Dan for an invite to that Vercel team. You can still clone the repo and read the site without one.

## 4. How to change the site

1. Edit `eon-product-overview/site/build.py`.
2. If the look changes, edit `eon-product-overview/site/refresh.css`. It loads after `../assets/site.css`, so its rules win. Bump the query on the CSS link in `shell()` when you change CSS. It is currently `refresh.css?v=prices`.
3. From `eon-product-overview/site/`, run:

```bash
python3 build.py
```

4. The script must print a page count and exit 0. It fails if generated HTML contains an em dash, an en dash, or the retired product name Assist IQ. It also checks the footer, `noindex`, the contact mailto, the partner page, the video page, and the price page.

Do not edit the generated HTML by hand and forget `build.py`. The next build will overwrite the HTML.

## 5. Locked story

Three altitudes. One job each. Do not mix them into one menu.

Story. Why, what, and how. Humble. Do not dictate to universities. Listen to employers and communities. The line is: From the jobs of the future to the education of today. Move from explanation to experience. Government uses the same shape. The journey is Understand, Experience, Practise, Demonstrate, Improve. The Global Virtual Campus is a place you enter, not a fifth product family. Campus URL: https://eonglobalcampus.com/

Shelf. The only public product map. Learn, Train, Perform, Achieve. Achieve is the public name for the old Outcomes column. It means get the job and secure it. Do not use both words. Digital Twin and Work Loop must not sit as a rival menu.

Engine. One sentence, on the platform page only: Learn and train in the Digital Twin. Perform in the Work Loop. Achieve is what you take with you.

Competence IQ and EON Control stay in a shared strip under Perform. They are not a fifth column. The left rail stays out.

## 6. Locked product decisions

Keep, as their own products:

- Career Compass. External page: https://eonreality.com/eon-career-compass/
- Venture Builder. External page: https://eonreality.com/eon-venture-builder/
- AI Fluency. External page: https://eonglobalcampus.com/ai-fluency
- Sentient Worlds. External page: https://eonreality.com/eon-sentient-worlds/

Replace:

- EON XR and EON AI fold into EON XR Infinite.
- Genesis Trainer and Genesis Simulator become Genesis 3.
- Assess IQ stays inside Perform. It is not its own shelf.
- Custom Virtual Builder is now also Situation Room. Creator does not get a second price.

Two cards, not one:

- Field IQ and Field IQ Edge.
- EON Tacit and Brainy Soft Skills. Tacit is not a replacement for Brainy.

Retired:

- Assist IQ has no card, no price row, and no mention in generated HTML. The builder fails if that name appears.

Other products link to the long platform at `https://eon-education-government-review.vercel.app/products/{slug}.html`, using the `long` field in `PRODUCTS`. Do not edit that long platform from this repo. Its source is not here.

## 7. Page list

45 pages come out of `build.py`.

Story and shelves:

- index.html, education.html, government.html, story.html, platform.html
- learn.html, train.html, perform.html, achieve.html

Products, in shelf order:

- Learn: universal, components, mirror, studio, model, worlds, xr, live, tacit
- Train: genesis, controlroom, situation, creator, brainy
- Perform: permit, field, edge, assess, compound, distillery, competence, control
- Achieve: career, venture, fluency, sentient

Public doors:

- pricing.html, contact.html, demo.html, videos.html, news.html, partners.html, sign-in.html, about.html, privacy.html, terms.html

## 8. Look

Use the dark cinematic review look. Blue `#51aeff`, with violet and green accents. Page background `#070c19`. Cards `#0e1830`. Borders `#29364e`.

Logo file: `eon-product-overview/assets/brand/eon-reality-logo-white.png`

It is the official white mark: triangle, circle, and the words eon reality. Header height is 56px after commit `2268659`. Do not go back to a typed wordmark. Do not go back to the old navy `#103060` or maroon `#9A1F3D`.

Favicon: `site/favicon.png` and `site/apple-touch-icon.png`. White mark on `#070c19`.

Hero photos:

- The photo sits on the right, about 58% of the hero width.
- The words stay on the left.
- The fade is solid `#070c19` from 0% to 36%, then clear by 50%.
- People and the main action must stay in the clear part of the photo.
- Do not put the headline under the photo.
- Do not put the photo back under a full-width dark panel.
- Under 600px, the photo is full width above the words.
- Cards, doors, and side bands are not under that fade. Do not shift them.

Hero stills are daylight JPGs in `site/images/`, with `?v=daylight` on the URL. There is no video model in this environment. Do not invent an 8-second hero film. The product films are the YouTube links in section 10.

## 9. Prices

Dan said the real prices are the ones already on the website, and they stay the same. They were copied from https://eonreality.com/product-pricing/ on 12 Oct 2026. They are per user per month.

| Product on this draft | Education | Enterprise | How to read it |
| --- | --- | --- | --- |
| EON XR Infinite | $36 | $124 | Same published numbers as EON XR and as EON AI. Both now sit inside XR Infinite at that same subscription. |
| Genesis 3 | $200 | $350 | Same published numbers as Genesis Trainer and as Genesis Simulator. Both are now Genesis 3 at that same subscription. |
| Brainy Soft Skills | $120 | $200 | Published line. |
| Situation Room | $280 | $450 | Published as Custom Virtual Builder, now also called Situation Room. |
| Situation Room Creator | same line | same line | Do not add a second price. |
| Assess IQ | $85 | $150 | Published line. |
| Field IQ | $170 | $300 | Published line. Field IQ Edge has no separate number. |
| Career Compass | $80 | $150 | Published line. |
| Venture Builder | $80 | $150 | Published line. |
| AI Fluency | $80 | $150 | Published line. |
| Sentient Worlds | $200 | $350 | Published line. On the live price page this product is grouped under Learn. On this draft it sits on Achieve. The price follows the product. |

The live homepage starts EON Classic at $36 and EON Spatial at $80 for education. The classic page lists EON XR and EON AI together from $72 for education: https://eonreality.com/eon-classic/

EON AI Ventures, https://eonaiventures.com/product-pricing/, showed the same numbers for EON XR, EON AI, Sentient Worlds, and the creation engine ($280 and $450). It also offers a university 1 percent, 2 percent, or 2.5 percent of educational revenue. This draft keeps the per-user prices from eonreality.com.

Fifteen products have no separate line on the published price page. Their row says "Scoped with the institution." Do not invent a number for them. They are: EON Universal, 3D Components, Mirror Direct, Mirror Studio, Model Inside, Worlds, EON Live, EON Tacit, EON Control Room, Permit IQ, Field IQ Edge, Compound IQ, The Distillery, Competence IQ, and EON Control.

Do not copy marketing claims from the old homepage onto this draft. That includes download counts, country counts, job counts, and multiples such as "4x". Prices above are allowed because Dan confirmed them. New prices are not.

## 10. Videos

The button "See the platform in action" goes to `videos.html`. The films are the YouTube links in the `VIDEOS` dict in `build.py`. They were taken from the EON One Platform video pages in Dan's Drive, file "EON_One_Platform_Videos_2026-10-09.pptx", checked against the shorter videos-only deck from the same day.

41 links. 22 products have at least one film. Each button opens YouTube. This draft does not host the video file and does not embed a player, so the page does not add a tracker.

No film in that set yet:

- Career Compass
- Venture Builder
- AI Fluency
- Sentient Worlds

If Dan sends those YouTube addresses, add them to `VIDEOS` and rebuild. Do not use a different film and call it one of these.

A separate public HTML address for "See the platform in action" was not found. `videos.html` is that page. If Dan later sends a different address, link it. Do not replace these YouTube ids on a guess.

## 11. Public facts already copied

Contact, from https://eonreality.com/connect-with-us/ :

- info@eonreality.com
- sales@eonreality.com
- +1 (949) 460-2000
- Monday to Friday, 9am to 5pm PT
- 18 Technology Drive, Suite 173, Irvine, CA 92618

The privacy policy at https://eonreality.com/privacy-policy/ lists Suite 110 at the same street, plus contact@eonreality.com and privacy@eonreality.com. Both suites are shown until Dan confirms one.

Draft conversation address: dan@eonreality.com. Keep that mailto on the contact page.

Demo does not host a form. It links to https://eonreality.com/schedule-a-free-demo/ and https://eonreality.com/eon-demo-clinic/. Do not copy the named testimonials from the demo page.

News is the 8 Oct 2026 Demo Clinics post and the clinic page. Do not invent headlines.

Partners only link to https://eonreality.com/value-added-resellers/. Do not copy partner names, phone numbers, or email addresses. The builder fails if `@` appears on partners.html.

Sign-in does not ask for a password. It links to https://eon-xr.com/ and https://core.eon-xr.com/.

Privacy and terms stay marked DRAFT FOR COUNSEL. They link to https://eonreality.com/privacy-policy/ and https://eonreality.com/terms-of-use/. Do not paste the live legal text onto the draft. Do not cite a statute.

French: https://eonreality.com/?lang=fr
Simplified Chinese: https://eonreality.com/?lang=zh-hans

Those buttons open the current site. They are not a translation of this draft. Do not machine-translate the 45 pages.

## 12. Copy rules

- No em dash. No en dash. The builder checks generated HTML for both.
- Straight apostrophes.
- Do not invent customer names, quotes, or prices.
- Do not add Assist IQ.
- Voice: listen first. Educators and institutions stay in charge. Do not prescribe a finished program to a university.

## 13. What is already done

- Story, four shelves, 26 products, and the public doors listed above.
- Official white logo, favicon, daylight heroes, photo on the right.
- Header wordmark size updated in commit `2268659`. Do not revert that logo.
- Published prices and the ventures comparison.
- Video page and per-product YouTube buttons.
- Contact facts, with both suites still visible.
- Partners, privacy, and terms point at the live pages.

## 14. What you still need from Dan

Do not guess these.

- Suite 173 or Suite 110.
- YouTube links for the four Achieve products that have no film.
- A translator for French and Simplified Chinese of this draft.
- A lawyer before privacy or terms are treated as policy.
- Permission to replace eonreality.com. Until then, this stays a draft.
- Raul's email, if someone is sending the cover note. Do not invent an address. Do not send mail from this repo.

## 15. What you can do without a new decision

- Fix a broken relative link, a wrong label, or a build failure.
- Add a film only when Dan gives the URL.
- Rebuild with `python3 build.py` after a change to `build.py`.
- Push this branch, then confirm the deployment on project `eon-reality-website`. The public address is https://eon-reality-website.vercel.app

## 16. Files the agent should open first

| File | Why |
| --- | --- |
| eon-product-overview/HANDOVER.md | This briefing. |
| eon-product-overview/COVER-EMAIL.md | The note for the team. |
| eon-product-overview/site/build.py | Pages, products, prices, videos, checks. |
| eon-product-overview/site/refresh.css | Look that overrides site.css. |
| eon-product-overview/assets/brand/eon-reality-logo-white.png | Official logo. |
| eon-product-overview/site/images/ | Hero and card stills. |
| eon-product-overview/vercel.json | Sends `/` to the new site, and ignores builds from other branches. |

Leave `.github/workflows/publish-overview.yml` unchanged. Leave the Vercel project `field-iq-walkthrough` unchanged.
