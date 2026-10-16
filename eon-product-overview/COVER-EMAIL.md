# Cover email

Session: bc-9af26ec8-156f-45cc-a72f-3555ea5c589c
Date: 16 Oct 2026
Status: draft. Do not treat this file as a sent message.

To: Raul and the marketing and development team
From: Dan Lejerskar
Subject: Handover for the EON Reality draft website

---

Raul and the team,

The draft of the new EON Reality website is in Git, with the briefing your agent needs to finish it.

Repository: https://github.com/DanLejerskar/field-iq-walkthrough
Branch: cursor/eon-product-overview-589c

Start here, in this order:

1. eon-product-overview/HANDOVER.md
2. eon-product-overview/COVER-EMAIL.md
3. eon-product-overview/site/build.py

The same two notes are also saved as Word files next to them: HANDOVER.docx and COVER-EMAIL.docx.

The site to open:

https://eon-reality-website.vercel.app

Videos: https://eon-reality-website.vercel.app/site/videos.html
Prices: https://eon-reality-website.vercel.app/site/pricing.html

Vercel project: eon-reality-website
Dashboard: https://vercel.com/dans-projects-3b851cd9/eon-reality-website

That project is the only Vercel project for this draft. Do not deploy it onto https://field-iq-walkthrough.vercel.app. That address is the Field IQ walkthrough and it stays as it is.

If Vercel is down, the same pages are also here:

https://htmlpreview.github.io/?https://raw.githubusercontent.com/DanLejerskar/field-iq-walkthrough/cursor/eon-product-overview-589c/eon-product-overview/site/index.html

If a page looks old, wait about a minute and refresh.

What you are taking over:

- 45 pages. The new site is the folder eon-product-overview/site/.
- Four shelves only: Learn, Train, Perform, Achieve.
- 26 product pages. The source of truth is site/build.py. Run python3 build.py from that folder after you edit it. Do not hand-edit the generated HTML and leave build.py behind.
- Published prices from eonreality.com. EON AI Ventures was checked beside them.
- 41 short YouTube films on the page called See the platform in action.

Please do not replace eonreality.com, and do not merge this branch to main, until we have walked through it together.

Still needs a decision from me before you invent an answer:

- Which Irvine suite is right, Suite 173 or Suite 110.
- YouTube links for Career Compass, Venture Builder, AI Fluency, and Sentient Worlds.
- A translator for French and Simplified Chinese of this draft.
- A lawyer for the privacy page and the terms page.

Reply with two or three times when we can meet and go through the draft.

Dan
