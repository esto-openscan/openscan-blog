---
title: "OpenScan3 Firmware: Projects & Scans"
date: "2026-02-02T12:11:18+01:00"
author: "Elias Stognienko"
description: "This post explains how OpenScan3 separates Projects and Scans to support multi-pass scanning, flexible capture strategies, and automation-friendly workflows."
shopify_summary_html: |-
  <p data-end="584" data-start="427">This post explains how OpenScan3 separates Projects and Scans to support multi-pass scanning, flexible capture strategies, and automation-friendly workflows.</p>
categories:
  - "OpenScan Blog"
tags:
  - "Firmware"
image:
  path: "/assets/img/posts/2026-02-02-openscan3-firmware-projects-scans/os3-projects-and-scans-title-6a2efd02-ab87-4003-9c27-fb19f96c09db.jpg"
redirect_from:
  - "/blogs/news/openscan3-firmware-projects-scans"
  - "https://62f7a3-4.myshopify.com/blogs/news/openscan3-firmware-projects-scans"
---

<p><em>This is the second blogpost of a series on the OpenScan3 firmware. Read the </em><a href="https://openscan.eu/blogs/news/preview-of-the-openscan3-firmware-a-fresh-start-with-modern-architecture"><em>previous post here</em></a><em>. Comments, questions, or suggestions are always welcome and a great help for future work on the firmware!</em></p>
<h1>OpenScan3: Projects and Scans</h1>
<p><em>tl;dr:</em> In OpenScan3, we distinguish between <em>Projects</em> and <em>Scans</em>. A <em>Project</em> represents the object you want to digitize.<br/>A <em>Scan</em> represents one concrete scanning strategy applied to that object, including its own settings and camera calibration.</p>
<h2>The Problem</h2>
<p>3D scanning never works with a single pass if you want to reconstruct an entire object.</p>
<p>Even with turntables, multi-axis rigs, or rotating camera arms, parts of an object inevitably remain occluded. A classic example is the underside of an object resting on the turntable. To capture it properly, you have to flip the object and scan it again.</p>
<p>But occlusion is not the only reason for multiple scans. Different areas of an object often benefit from different scanning strategies. Some regions have many fine details or holes and require many images from slightly varied angles. Other parts are comparatively simple and can be captured with fewer images.</p>
<p><strong><img alt="Front and back views of a small 3D-printed figurine used as an OpenScan benchmark, showing fine surface details and geometry." src="/assets/img/posts/2026-02-02-openscan3-firmware-projects-scans/os3-projects-and-scans-benchy.png"/></strong></p>
<p>Take the OpenScan Benchy[1] as an example: From the front, the miniature contains a lot of fine details: facial features, a sharp sword, and a pointy helmet. Capturing these areas benefits from many images taken at small angular steps. The back is rather simple in comparison. Fewer images are usually sufficient here, without negatively affecting reconstruction quality.</p>
<p>If you were capturing images manually, you would naturally adapt your approach to be as effective as possible. You would spend more time and take more photos where it matters, and less where it does not. Not only would the picture-taking be much faster, also the reconstruction time will decrease significantly.</p>
<p>The same idea applies to semi-automated systems like OpenScan. When you then want to use advanced techniques like focus or exposure stacking (or bracketing) it becomes clear that in practice, scanning a single object usually means:</p>
<ul>
<li>different camera settings or calibration</li>
<li>adapted photo density</li>
<li>multiple capture passes with the flipped object</li>
</ul>
<p>So, scanning an object usually means having more than one scan routine ideally using different scan settings and camera calibrations.</p>
<h2>The Solution: Projects and Scans</h2>
<p>OpenScan3 embraces this reality by introducing a simple but flexible concept.</p>
<p>Think of a <strong>Project</strong> as everything related to one physical object.</p>
<p>Within that <em>Project</em>, you create one or more <strong>Scans</strong>. Each <em>Scan</em> represents a specific strategy for capturing part of that object. A <em>Scan</em> can e.g. differ in:</p>
<ul>
<li>number of images</li>
<li>angles or movement patterns</li>
<li>focus, exposure and/or other camera calibration</li>
</ul>
<h3>A Concrete Example: The OpenScan Benchy</h3>
<p>Here you can see how I scanned the OpenScan Benchy miniature on an OpenScan Mini using the alpha firmware of OpenScan3:</p>
<p><img alt="OpenScan3 web interface showing a project with multiple completed scans, including scan settings, image counts, and download options." src="/assets/img/posts/2026-02-02-openscan3-firmware-projects-scans/os3-projects-and-scans-screenshot.jpg"/></p>
<p>In <em>Scan</em> #1, I did a &ldquo;general&rdquo; pass and captured the Benchy from all possible angles using the auto focus mode to ensure sharpness across the pictures.</p>
<p>To catch the finer details, I made a second pass, where I used focus stacking. The scanner took 3 photos with different focus settings from 30 positions totaling in 90 pictures for <em>Scan</em> #2. But focus stacking wasn't the only thing I did differently from the first <em>Scan</em>: I also restricted the angles of the scanning path and thus ensured, that most of the photos were in the areas with fine details and not e.g. from very high or low angles.</p>
<p>For the final <em>Scan</em> #3, I flipped the figurine on the turntable to get some pictures of the underside using only 20 pictures.</p>
<h2>A Short Technical Detour</h2>
<p>This section deep dives in the current implementation and is suited for those interested, what's happening behind the curtains and can be safely skipped ;)</p>
<p><em>Projects</em> in OpenScan3 are meant to be portable and user-owned: a <em>Project</em> is a self-contained bundle you can download, backup, share or feed into your own tooling. We decided to stick to plain files and small JSON manifests so projects remain inspectable without special software: a file browser and a text editor are enough.</p>
<p>A <em>Scan</em> is simply one capture run inside a <em>Project</em> living in its own folder. That&rsquo;s helpful when you run multi-pass workflows (general pass, detail pass, flipped pass) or when you want to trigger different downstream steps depending on the type of <em>Scan</em>. In practice, this means you don&rsquo;t just get &ldquo;a pile of images&rdquo;, you get images that are explicitly grouped and described in a way that other tools can act on.</p>
<p>Each photo within a <em>Scan</em> folder is stored as a normal image file and comes with a small &ldquo;sidecar&rdquo; metadata JSON next to it. That metadata is meant to be useful outside of OpenScan as well: you can filter or sort pictures, debug lighting or focus issues, map images back to capture positions, or generate your own reports without having to reverse-engineer anything. The goal of this structure isn&rsquo;t to be fancy, it&rsquo;s to stay approachable and scriptable, so you can use OpenScan projects as building blocks in your own workflow!</p>
<h3>What's happening inside the firmware?</h3>
<p>Inside the firmware, <em>Projects</em> are handled by a dedicated project service controller that acts as the single interface for loading, updating, and persisting <em>Project</em> data.</p>
<p>Other parts of the system interact with projects only through this interface. A scanning routine, for example, doesn&rsquo;t need to know how files are laid out on disk or how metadata is stored. It simply reports captures (images plus metadata) to the project service.</p>
<p>Both <em>Projects</em> and <em>Scans</em> have their own data model and in case of <em>Scans</em> an additional settings model. These models closely mirror what you see when you download a <em>Project</em>, which keeps the system consistent and makes the on-disk format easy to understand.</p>
<p>Overall, this keeps responsibilities clearly separated and reduces coupling between subsystems, which is important OpenScan3 continues to grow with new features.</p>
<h2>What this structure makes possible</h2>
<p>This structure enables a number of useful extensions:</p>
<ul>
<li>scan-specific pre- and post-processing</li>
<li>reusable <em>Scan</em> templates for recurring workflows</li>
<li>cleaner automation and scripting</li>
<li>easier experimentation with new hardware or capture strategies</li>
</ul>
<p>While this seems a bit complex right now, we work hard on automate the settings so that especially new users are not overwhelmed and get good results.</p>
<h2>Summary</h2>
<p>In OpenScan3, <em>Projects</em> are object-centric and approachable.<br/><em>Scans</em> encapsulate strategies, settings and technical details.</p>
<p>This gives newcomers a clear mental model and a straightforward workflow, while offering experienced users and developers well-defined extension points for automation, customization and future features.</p>
<p>&nbsp;</p>
<p><em>If you have thoughts, questions, suggestions, or want to contribute we would love hearing from you. You can reach out via&nbsp;</em><a href="mailto:esto@openscan.eu"><em>e-mail</em></a><em>, join the </em><a href="https://discord.gg/eBdqtdkXyF"><em>Discord</em></a><em> or create issues on </em><a href="[https://github.com/OpenScan-org/OpenScan3](https://github.com/OpenScan-org/OpenScan3)"><em>GitHub/OpenScan3</em></a><em>.</em></p>
<p>&nbsp;</p>
<hr/>
<p>[1] OpenScan Benchy is a creation by <a href="https://cults3d.com/en/users/Valandar/3d-models">Valander</a> and used as a 3d scanner benchmark on <a href="https://github.com/OpenScanEu/OpenScanBenchy">GitHub</a></p>
