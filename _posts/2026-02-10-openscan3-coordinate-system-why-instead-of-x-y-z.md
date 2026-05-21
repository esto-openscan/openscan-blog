---
title: "OpenScan3 Firmware: The Coordinate System"
date: "2026-02-10T18:27:23+01:00"
author: "Elias Stognienko"
description: "This post explains how OpenScan3 represents camera viewpoints using two angles (φ and θ) instead of (x, y, z), and how those angles map directly to the OpenScan Mini and OpenScan Classic."
shopify_summary_html: |-
  <div class="flex flex-col text-sm pb-25">
  <article class="text-token-text-primary w-full focus:outline-none [--shadow-height:45px] has-data-writing-block:pointer-events-none has-data-writing-block:-mt-(--shadow-height) has-data-writing-block:pt-(--shadow-height) [&amp;:has([data-writing-block])&gt;*]:pointer-events-auto scroll-mt-[calc(var(--header-height)+min(200px,max(70px,20svh)))]" dir="auto" data-turn-id="6ea01284-57a7-4030-aff4-a3bc6a939bcf" data-testid="conversation-turn-14" data-scroll-anchor="true" data-turn="assistant" tabindex="-1">
  <div class="text-base my-auto mx-auto pb-10 [--thread-content-margin:--spacing(4)] @w-sm/main:[--thread-content-margin:--spacing(6)] @w-lg/main:[--thread-content-margin:--spacing(16)] px-(--thread-content-margin)">
  <div class="[--thread-content-max-width:40rem] @w-lg/main:[--thread-content-max-width:48rem] mx-auto max-w-(--thread-content-max-width) flex-1 group/turn-messages focus-visible:outline-hidden relative flex w-full min-w-0 flex-col agent-turn" tabindex="-1">
  <div class="flex max-w-full flex-col grow">
  <div data-message-author-role="assistant" data-message-id="eae2faf7-8d20-478b-b417-87846408e71e" dir="auto" class="min-h-8 text-message relative flex w-full flex-col items-end gap-2 text-start break-words whitespace-normal [.text-message+&amp;]:mt-1" data-message-model-slug="gpt-5-2-thinking">
  <div class="flex w-full flex-col gap-1 empty:hidden first:pt-[1px]">
  <div class="markdown prose dark:prose-invert w-full wrap-break-word light markdown-new-styling">
  <p data-start="0" data-end="199" data-is-last-node="" data-is-only-node="">This post explains how OpenScan3 represents camera viewpoints using two angles (φ and θ) instead of (x, y, z), and how those angles map directly to the OpenScan Mini and OpenScan Classic.</p>
  </div>
  </div>
  </div>
  </div>
  <div class="z-0 flex min-h-[46px] justify-start"><br></div>
  <div class="mt-3 w-full empty:hidden">
  <div class="text-center"><br></div>
  </div>
  </div>
  </div>
  </article>
  </div>
categories:
  - "OpenScan Blog"
tags:
  - "Firmware"
image:
  path: "/assets/img/posts/2026-02-10-openscan3-coordinate-system-why-instead-of-x-y-z/os3-coordinate-system-ad175c30-74f9-4c84-b1a1-184b77f69f7a.jpg"
redirect_from:
  - "/blogs/news/openscan3-coordinate-system-why-%CF%86-%CE%B8-instead-of-x-y-z"
  - "https://62f7a3-4.myshopify.com/blogs/news/openscan3-coordinate-system-why-%CF%86-%CE%B8-instead-of-x-y-z"
---

<p><em>This is the third blog post of a series on the OpenScan3 firmware. Read the <a href="https://openscan.eu/blogs/news/openscan3-firmware-projects-scans">previous post here</a>. Comments, questions, or suggestions are always very welcome and a great help for future work on the firmware!</em></p>
<p>tl;dr: OpenScan3 uses a spherical coordinate system and expresses positions using two angles. <strong>&phi;</strong> (phi) is the azimuth (="the turntable") and <strong>&theta;</strong> (theta) is like the vertical height angle (="the rotor" of an OpenScan Mini.)</p>
<h2>The Theory: Why (&phi;, &theta;) instead of (x,y,z)?</h2>
<p>Instead of describing camera positions using Cartesian coordinates (x, y, z), OpenScan3 represents viewpoints using two angles: <strong>&phi; (phi)</strong> and <strong>&theta; (theta)</strong>. The reason is simple: most scanners don&rsquo;t &ldquo;fly freely&rdquo; in 3D space. They rotate their view around an object and tilt it up and down.</p>
<p>You can think of these viewpoints as lying on a sphere. Figure 1 shows the idea:</p>
<p><img alt="" src="/assets/img/posts/2026-02-10-openscan3-coordinate-system-why-instead-of-x-y-z/os3-03-coordinates-1.jpg"/><em>Source: <a href="https://de.wikipedia.org/wiki/Datei:Kugelkoord-def.svg" rel="noopener" target="_blank">&ldquo;Kugelkoord-def.svg&rdquo;</a> by Ag2gaeh (Wikimedia Commons), <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>.<br/>Image version includes edits by Geek3.</em></p>
<p>Figure 1 shows the standard spherical coordinate system. The object sits at the center of a sphere <strong>O</strong>, and each camera position corresponds to a viewing <strong>direction</strong> from a point <strong>P</strong> on that sphere. This direction can be sufficiently described by two angles: the azimuth <strong>&phi;</strong> and the polar angle <strong>&theta;</strong>. The radius <em>r</em> describes the distance from the center, but in OpenScan setups this distance is usually fixed by the hardware.</p>
<p>Note: Different fields swap &phi;/&theta; or choose different zero directions. In OpenScan3, we define &theta; = 0&deg; as top-down (camera pointing straight down to the object) and increase &theta; towards a horizontal side view.</p>
<p>As you can see in Figure 1, the sphere we described with <strong>&phi;</strong>, <strong>&theta;</strong> and <em>r</em> sits in a Cartesian coordinate system and it is trivial to transform the (<strong>&phi;</strong>, <strong>&theta;</strong>, <em>r</em>) coordinates to (x, y, z). This transformation is built in OpenScan3 and used for example for the photo metadata, because photogrammetry reconstruction tools like Colmap use this format.</p>
<p>So why use spherical coordinates at all? The answer is less technical and more human: it is much easier to reason about &ldquo;a turntable angle&rdquo; and &ldquo;a height angle&rdquo; than juggling three variables with possibly different signs.</p>
<p>Here is a small concrete example of what I mean. Assume the camera moves on a sphere with a fixed distance r = 100 mm. We keep the azimuth constant at <strong>&phi; = 30&deg;</strong> and only &ldquo;move down&rdquo; by increasing <strong>&theta;</strong>:</p>
<ul>
<li>
<strong>Point A</strong> (spherical)<strong>:</strong> (&phi; = 30&deg;, &theta; = 30&deg;, r = 100)</li>
<li>
<strong>Point B</strong> (spherical)<strong>:</strong> (&phi; = 30&deg;, &theta; = 60&deg;, r = 100)</li>
</ul>
<p>In spherical coordinates this motion is obvious: <strong>only &theta; changes</strong>.</p>
<p>If we convert both points to Cartesian coordinates (x, y, z), we get:</p>
<ul>
<li>
<strong>Point A</strong> (Cartesian)<strong>:</strong> (x, y, z) &asymp; (43.3, 25.0, 86.6)<br/>
</li>
<li>
<strong>Point B</strong> (Cartesian)<strong>:</strong> (x, y, z) &asymp; (75.0, 43.3, 50.0)</li>
</ul>
<p>Here, all three values change at the same time: <strong>x and y increase, z decreases</strong>. That is correct, but it does not directly communicate the simple idea of &ldquo;same turntable angle, just move down&rdquo;.</p>
<h3>OpenScan Mini</h3>
<p>For OpenScan Mini devices, this spherical interpretation is particularly intuitive. The camera is mounted on a curved rotor arm that allows it to tilt up and down, directly sweeping through different values of &theta;. At the same time, the object itself is rotated on a turntable, which corresponds to changing &phi;. Together, these two motions allow the system to sample viewpoints distributed over a spherical surface around the object.</p>
<p>To make this more tangible, <strong>Figure 2</strong> breaks the spherical model down into the two views. The left diagram shows the turntable view (top-down), which defines the azimuth angle &phi;. The right diagram shows the rotor view (side), which defines the polar angle &theta;.</p>
<p><img alt="" src="/assets/img/posts/2026-02-10-openscan3-coordinate-system-why-instead-of-x-y-z/os3-03-coordinates-2.jpg"/></p>
<p>In the turntable view (Figure 2, left), &phi; is the rotation around the object in the horizontal plane: it runs from <strong>0&deg; to 360&deg;</strong>, measured <strong>counterclockwise </strong>when viewed from above.</p>
<p>In the<strong> rotor view </strong>(Figure 2, right), &theta; is the vertical tilt away from the top-down direction: <strong>&theta; = 0&deg;</strong> is straight down, <strong>&theta; = 90&deg;</strong> is a horizontal side view, and <strong>&theta; = 180&deg;</strong> would be bottom-up. The shaded region indicates the mechanically reachable window on a typical OpenScan Mini. In OpenScan3, these limits are configurable in the settings.</p>
<p>A simple way to remember it:</p>
<ul>
<li>
<strong>&theta;</strong> moves your view <strong>up and down</strong>
</li>
<li>
<strong>&phi;</strong> moves your view <strong>around the object</strong>
</li>
</ul>
<p>While &phi; can rotate freely without a fixed reference,<strong> </strong>&theta; depends on a known physical starting position, especially on OpenScan Mini devices. (More on this in a follow up blog post)</p>
<h3>OpenScan Classic</h3>
<p>The situation for OpenScan Classic is conceptually the same, even though the camera is fixed in space. Instead of moving the camera, OpenScan Classic achieves equivalent viewpoints by rotating and tilting the object. From the perspective of the coordinate system, the relative viewing direction between camera and object still traces points on a sphere. Those directions are again described by <strong>&phi;</strong> and <strong>&theta;</strong>.</p>
<p><strong><img alt="" src="/assets/img/posts/2026-02-10-openscan3-coordinate-system-why-instead-of-x-y-z/os3-03-coordinates-3.jpg"/><br/></strong><strong>Figure 3</strong> shows how <strong>&theta;</strong> maps to the Classic rotor angle: <strong>&theta; = 0&deg;</strong> is a top-down view, <strong>&theta; = 45&deg;</strong> is slightly from above, and <strong>&theta; = 90&deg;</strong> is a horizontal view.</p>
<p>One big difference to the Mini: the Classic is not limited to a small &ldquo;reachable window&rdquo; of &theta; by the rotor geometry. In theory, you can drive almost any angle.</p>
<p>In practice though, not every angle is useful.<br/><img alt="" src="/assets/img/posts/2026-02-10-openscan3-coordinate-system-why-instead-of-x-y-z/os3-03-coordinates-4.jpg"/><br/><strong>Figure 4: </strong><em>&ldquo;Just because you can, doesn&rsquo;t mean you should.&rdquo;</em><br/>Left: at extreme angles you mostly capture the stepper motor.<br/>Right: at <em>very</em> extreme angles you might experience catastrophic failure (also known as gravity).</p>
<h2>The Reality</h2>
<p>In our theoretical model shown in Figure 1, we described the view from&nbsp;<em>P</em> as pointing straight to the center of the sphere where the object sits. This is an ideal case. In reality, there are small deviations.</p>
<p>Take the OpenScan Mini: due to material tolerances, the camera is not always perfectly centered to the turntable. For the OpenScan Classic, it&rsquo;s also obvious: rotating the object around two axes with a fixed camera means the object &ldquo;jitters&rdquo; a bit around the theoretical center of the sphere.</p>
<p>These deviations are negligible in practice. But if you made it this far in the blog post, you are most likely interested in these details.</p>
