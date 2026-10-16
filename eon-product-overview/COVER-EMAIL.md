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

Practice site, for reading in a browser:

https://htmlpreview.github.io/?https://raw.githubusercontent.com/DanLejerskar/field-iq-walkthrough/cursor/eon-product-overview-589c/eon-product-overview/site/index.html

Videos: change index.html to videos.html in that link.
Prices: change index.html to pricing.html.

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
