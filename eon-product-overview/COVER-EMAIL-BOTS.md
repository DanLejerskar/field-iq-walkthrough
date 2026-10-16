# Cover email

Session: bc-9af26ec8-156f-45cc-a72f-3555ea5c589c
Date: 16 Oct 2026
Status: draft. Do not treat this file as a sent message.
Dan adds Raul's email before anyone sends this. Brita's address on the 14 Oct and 15 Oct notes is brita@eonreality.com.

To: Raul and Brita
From: Dan Lejerskar
Subject: Start from the HTML preview, then cross-check the live site with your agents

---

Raul and Brita,

I read the clarification. The refreshed pages on eonreality.com are the WordPress pass. The site I want us to develop is the HTML preview. That one already has the story, the four shelves, the colors, and the hero layout. Use it as the base.

Start here:

https://htmlpreview.github.io/?https://raw.githubusercontent.com/DanLejerskar/field-iq-walkthrough/cursor/eon-product-overview-589c/eon-product-overview/site/index.html

Learn, the page I want the agents to open first among the shelves:

https://htmlpreview.github.io/?https://raw.githubusercontent.com/DanLejerskar/field-iq-walkthrough/cursor/eon-product-overview-589c/eon-product-overview/site/learn.html

The same draft is at https://eon-reality-website.vercel.app

The live site to cross-check is https://eonreality.com/

Give this file to your agents and let them do the work. Do not paste the pages in by hand.

eon-product-overview/BOT-BRIEF-RAUL-BRITA.md

The same brief is also BOT-BRIEF-RAUL-BRITA.docx. The locked product rules are still in HANDOVER.md.

What the agents do:

1. Start from the HTML preview on branch cursor/eon-product-overview-589c. The source is site/build.py. They edit that file and run python3 build.py. They do not edit the generated HTML and leave the builder behind.
2. Review https://eonreality.com/ against that preview. The brief already has the first pass from 16 Oct 2026. The agents recheck it and write eon-product-overview/DECISION-LIST.md.
3. Add one 8-second silent film for each hero on education, government, learn, train, perform, and achieve. The film matches the still that is already there. If an agent has no video model, it stops and says so. It does not drop in a stock clip.
4. Cross-check the two sites. What the live site has, the preview does not. What the preview has, the live site does not.
5. Leave the decision list unmarked. We will sit together and mark Keep, Retire, or Ask Dan. The agents do not take a page down, and they do not replace eonreality.com, until we have done that.

What I already found, so you do not have to guess:

- The live home and the live Learn shelf already use the new sentences.
- https://eonreality.com/education/ is still the older education page, with the 4x line, the 76 percent line, the 97 percent line, and a named quote.
- https://eonreality.com/government/ is still the older SkillBuild page.
- The live home still has Scan to Experience, a Proven at Scale row that showed zeros, and a logo row.
- Neither site has the six 8-second hero films yet.
- The price page on the preview stays with the published per-user prices. Do not replace them with the suggested prices in the spreadsheet.

Repository: https://github.com/DanLejerskar/field-iq-walkthrough
Branch: cursor/eon-product-overview-589c
Pull request: https://github.com/DanLejerskar/field-iq-walkthrough/pull/1

Please do not merge that pull request, and do not deploy this draft onto https://field-iq-walkthrough.vercel.app. That address is the Field IQ walkthrough.

Reply with two or three times when we can go through the decision list.

Dan
