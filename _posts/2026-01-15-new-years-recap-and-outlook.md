---
title: "New Year's recap and outlook"
date: "2026-01-15T13:49:29+01:00"
author: "Thomas Megel"
categories:
  - "OpenScan Blog"
tags: []
image:
  path: "/assets/img/posts/2026-01-15-new-years-recap-and-outlook/recap2025-openscan-5f074abd-0f32-4462-bf5a-6b6e9f50a2ba.jpg"
redirect_from:
  - "/blogs/news/new-years-recap-and-outlook"
  - "https://62f7a3-4.myshopify.com/blogs/news/new-years-recap-and-outlook"
---

<h1 data-pm-slice="0 0 []" dir="ltr"><strong>Recap of 2025</strong></h1>
<h2 dir="ltr"><strong>Intro</strong></h2>
<p dir="ltr">2025 has been quite a ride.</p>
<p dir="ltr">It has been almost eight years since I started tinkering with 3D scanning, initially just trying to understand how photogrammetry works and how far you can push it with simple hardware. What began as a personal experiment slowly turned into OpenScan: a community-driven, open-source project with users all over the world.</p>
<p dir="ltr">This post is a short recap of what happened in 2025, what we actually worked on, what changed behind the scenes, and where OpenScan currently stands.</p>
<h2 dir="ltr"><strong>A short look back: how we got here</strong></h2>
<p dir="ltr">For a long time, OpenScan was developed and maintained almost entirely by myself, with help from the community. Like many maker projects, it grew organically and sometimes faster than expected and sometimes in directions I did not fully anticipate.</p>
<p dir="ltr">As OpenScan gained traction, parts of the project became more formalized: hardware production, shipping, customer support, documentation, and all the administrative overhead that comes with running an open-source hardware project internationally. That shift brought new challenges and changed how much time could realistically be spent on development and community interaction.</p>
<h2 dir="ltr"><strong>What we worked on in 2025</strong></h2>
<p dir="ltr">Although progress was not always visible, 2025 focused mainly on foundational work that will influence the future of OpenScan.</p>
<h3 dir="ltr"><strong>A new firmware foundation</strong></h3>
<p dir="ltr">One of the most important steps in 2025 was starting work on a completely new firmware framework for OpenScan devices.</p>
<p dir="ltr">Elias (known online as <em>esto</em>) picked up an earlier firmware prototype originally created by community members Polectron and jorgerobles and began turning it into something more robust and future-proof than my previous firmware. The goal is not just better usability for end users, but also a cleaner, more modular architecture that makes it easier for developers to extend, customize, and maintain.</p>
<p dir="ltr">An alpha version is already <a data-md-href="https://github.com/OpenScan-org/OpenScan3" data-text-el="text-only-link" href="https://github.com/OpenScan-org/OpenScan3" rel="noopener noreferrer nofollow"><u>available on GitHub</u></a>, and while there is still work ahead, this new firmware lays the groundwork for a much more flexible OpenScan ecosystem.</p>
<h2 dir="ltr"><strong>Research</strong></h2>
<p dir="ltr">A major focus in 2025 was validating long-standing assumptions about photogrammetry with reproducible experiments.</p>
<p dir="ltr">We tackled questions that come up again and again in the photogrammetry community:</p>
<ul>
<li dir="ltr">
<p dir="ltr"><a data-md-href="https://openscan.eu/blogs/news/optimizing-3d-scans-how-many-photos-do-you-really-need" data-text-el="text-only-link" href="https://openscan.eu/blogs/news/optimizing-3d-scans-how-many-photos-do-you-really-need" rel="noopener noreferrer nofollow"><u>How many photos do you really need for a good scan?</u></a></p>
</li>
<li dir="ltr">
<p dir="ltr"><a data-md-href="https://openscan.eu/blogs/news/optimizing-3d-scans-what-is-the-right-shutter-speed" data-text-el="text-only-link" href="https://openscan.eu/blogs/news/optimizing-3d-scans-what-is-the-right-shutter-speed" rel="noopener noreferrer nofollow"><u>What is the right shutter speed?</u></a></p>
</li>
<li dir="ltr">
<p dir="ltr"><a data-md-href="https://openscan.eu/blogs/news/testing-the-influence-of-jpeg-quality-on-the-3d-scan-results" data-text-el="text-only-link" href="https://openscan.eu/blogs/news/testing-the-influence-of-jpeg-quality-on-the-3d-scan-results" rel="noopener noreferrer nofollow"><u>How much does JPEG quality affect reconstruction results?</u></a></p>
</li>
</ul>
<p dir="ltr">The results largely confirmed practical experience. In the process, we also discovered a fast method to estimate feature density that is significantly quicker than running full SIFT analysis on an image. The image analyzer is easily available <a data-md-href="https://openscan.eu/pages/openscancloud" data-text-el="text-only-link" href="https://openscan.eu/pages/openscancloud" rel="noopener noreferrer nofollow"><u>here</u></a> for you to test!</p>
<p dir="ltr">These findings are not just theoretical. They already influence how presets and workflows are designed and will be reflected in upcoming firmware revisions. All results and tools are publicly available, including the image analyzer and the growing <a data-md-href="https://github.com/OpenScanEu/OpenScanBenchy/blob/main/README.md" data-text-el="text-only-link" href="https://github.com/OpenScanEu/OpenScanBenchy/blob/main/README.md" rel="noopener noreferrer nofollow"><u>OpenScan Benchy dataset</u></a>, which was expanded in collaboration with users around the world.</p>
<p dir="ltr">To better understand how OpenScan devices are actually used, we ran a community survey and used the findings as guidelines for the new firmware.</p>
<h2 dir="ltr"><strong>Visibility and communication</strong></h2>
<p dir="ltr">If there is one thing we could have done better in 2025, it is communication.</p>
<p dir="ltr">There were periods where progress was real, but not very visible from the outside. That is something we are aware of and actively working to improve. Open-source projects thrive on transparency, and showing work is part of the work.</p>
<p dir="ltr">Building and maintaining an open-source hardware project is rewarding, but also resource-intensive. Development, research, support, and the free-to-use OpenScanCloud all take time and money. At the same time, the external environment changed significantly in 2025: The US tariffs made international trade more complex, costs increased, and margins tightened. Despite this, our kit prices have remained stable since early 2022!</p>
<p dir="ltr">OpenScan thrives because of its community. One of the most valuable ways to support the project is by participating, sharing your experiences, and helping others discover OpenScan. If you find the project useful, you can also support it financially through <a data-md-href="https://www.patreon.com/OpenScan" data-text-el="text-only-link" href="https://www.patreon.com/OpenScan" rel="noopener noreferrer nofollow"><u>Patreon</u></a>, <a data-md-href="https://buymeacoffee.com/openscan" data-text-el="text-only-link" href="https://buymeacoffee.com/openscan" rel="noopener noreferrer nofollow"><u>BuyMeACoffee</u></a>, or by <a data-md-href="https://openscan.eu/collections/all" data-text-el="text-only-link" href="https://openscan.eu/collections/all" rel="noopener noreferrer nofollow"><u>purchasing a kit</u></a>.</p>
<p dir="ltr">For me personally, seeing people use OpenScan, experiment with it, and share their results is what makes it all worthwhile. Every bit of support, whether through feedback, contributions, or simply spreading the word, helps to create the stability needed to focus on what matters most: building reliable, open tools that you truly own.</p>
<h2 dir="ltr"><strong>What OpenScan stands for in 2026 and beyond</strong></h2>
<p dir="ltr">OpenScan has always been rooted in a simple belief: that 3D scanning should be accessible, affordable, and open.</p>
<p dir="ltr">We still strongly believe in open-source software and open hardware. High-quality 3D scanning does not have to live inside closed ecosystems or walled gardens where you do not fully own your device, your data, or your workflow.</p>
<p dir="ltr">Our mission remains unchanged: <em>Affordable 3D Scanning for the Masses.</em></p>
<p dir="ltr">That is why we invest so much effort into building a solid, long-term firmware foundation under an AGPL license and why we publish our research results openly. Understanding how and why things work is just as important as making them work.</p>
<p dir="ltr">OpenScan is not about locking users into platforms, it is about giving them tools they can trust, adapt, and truly own.</p>
<p dir="ltr">Thank you to everyone who scanned, tested, reported bugs, shared results, or supported the project in any way.</p>
<p dir="ltr">Happy New Year 2026! And Happy Scanning!</p>
<p dir="ltr">Thomas</p>
<p>PS: sorry for the AI-generated title image, it is impossible to put 2025 into one image... Besides the image, everything is human-made :)</p>
