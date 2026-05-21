---
title: "OpenScan3 Firmware: Smooth Moves"
date: "2026-03-06T10:46:47+01:00"
author: "Elias Stognienko"
description: "OpenScan3 replaces OpenScan2’s “delay tuning” with a simple motion model: max_speed and acceleration . This post explains the new mental model (trapezoid vs triangle profiles) and gives a practical tuning guide to get smooth, reliable motor movement across devices."
shopify_summary_html: |-
  <div class="flex flex-col text-sm pb-25">
  <article class="text-token-text-primary w-full focus:outline-none [--shadow-height:45px] has-data-writing-block:pointer-events-none has-data-writing-block:-mt-(--shadow-height) has-data-writing-block:pt-(--shadow-height) [&amp;:has([data-writing-block])&gt;*]:pointer-events-auto scroll-mt-[calc(var(--header-height)+min(200px,max(70px,20svh)))]" dir="auto" data-turn-id="request-69a9c03d-6ef4-838c-b120-d6eb9cdd2ffd-0" data-testid="conversation-turn-40" data-scroll-anchor="true" data-turn="assistant" tabindex="-1">
  <div class="text-base my-auto mx-auto pb-10 [--thread-content-margin:var(--thread-content-margin-xs,calc(var(--spacing)*4))] @w-sm/main:[--thread-content-margin:var(--thread-content-margin-sm,calc(var(--spacing)*6))] @w-lg/main:[--thread-content-margin:var(--thread-content-margin-lg,calc(var(--spacing)*16))] px-(--thread-content-margin)">
  <div class="[--thread-content-max-width:40rem] @w-lg/main:[--thread-content-max-width:48rem] mx-auto max-w-(--thread-content-max-width) flex-1 group/turn-messages focus-visible:outline-hidden relative flex w-full min-w-0 flex-col agent-turn" tabindex="-1">
  <div class="flex max-w-full flex-col gap-4 grow">
  <div data-message-author-role="assistant" data-message-id="b6def9bf-7036-4a9b-b660-757c88ad0939" dir="auto" data-message-model-slug="gpt-5-2-thinking" class="min-h-8 text-message relative flex w-full flex-col items-end gap-2 text-start break-words whitespace-normal [.text-message+&amp;]:mt-1">
  <div class="flex w-full flex-col gap-1 empty:hidden">
  <div class="markdown prose dark:prose-invert w-full wrap-break-word light markdown-new-styling">
  <p data-start="0" data-end="272" data-is-last-node="" data-is-only-node="">OpenScan3 replaces OpenScan2’s “delay tuning” with a simple motion model: <strong data-start="74" data-end="87">max_speed</strong> and <strong data-start="92" data-end="108">acceleration</strong>. This post explains the new mental model (trapezoid vs triangle profiles) and gives a practical tuning guide to get smooth, reliable motor movement across devices.</p>
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
  path: "/assets/img/posts/2026-03-06-openscan3-firmware-smooth-moves/os3-motion-tuning-ba0710ed-016e-48e4-a8a5-8c0cbe45d79e.jpg"
redirect_from:
  - "/blogs/news/openscan3-firmware-smooth-moves"
  - "https://62f7a3-4.myshopify.com/blogs/news/openscan3-firmware-smooth-moves"
---

<p><em>This is the a blog post in a series on the OpenScan3 firmware. Read the <a href="https://openscan.eu/blogs/news/openscan3-coordinate-system-why-%CF%86-%CE%B8-instead-of-x-y-z">previous post here</a>. Comments, questions, or suggestions are always very welcome and a great help for future work on the firmware!</em></p>
<p><strong>tl;dr:</strong> OpenScan3&rsquo;s motor controller uses a simple motion model (max speed + acceleration) instead of &ldquo;delay tuning&rdquo;.<br/>The result is smoother motion, more predictable behavior, and easier configuration across devices.</p>
<p>The first part of the post is about the rationale of the new motor contoller. If you just want to know how to tune the settings, <a href="#tuning-guide">skip right ahead to the practical guide</a>.</p>
<h2>Why we entirely replaced the old motor control logic</h2>
<p>OpenScan2 motion tuning mostly boiled down to step delays and a few ramp parameters. It worked, but it was hard to reason about:</p>
<ul>
<li>settings didn&rsquo;t map cleanly to real-world motion,</li>
<li>tuning wasn&rsquo;t very transferable between devices,</li>
<li>small changes could have big (and sometimes surprising) effects.</li>
</ul>
<p>If you&rsquo;re coming from OpenScan2, you might be looking for the old "delay" values.<br/>In OpenScan3, you typically don&rsquo;t need them anymore:<br/><code>max_speed</code> and <code>acceleration</code> give you a much more direct handle on how the device will move.</p>
<p>With OpenScan3 we rebuilt the motor controller around a simple motion model:<br/><strong>accelerate &rarr; cruise &rarr; decelerate</strong>.</p>
<p>Instead of tuning a <em>timer</em>, you tune <em>motion</em>.</p>
<h2>The mental model</h2>
<p>OpenScan3 uses a simple motion profile that should feel familiar from school physics:<br/><strong>uniform acceleration</strong> for start/stop, and (optionally) <strong>constant velocity</strong> in between.</p>
<p>If we plot <strong>velocity over time</strong>, the shape is almost always one of these:</p>
<ul>
<li>
<strong>Trapezoid:</strong> accelerate &rarr; cruise at <code>max_speed</code> &rarr; decelerate</li>
<li>
<strong>Triangle:</strong> accelerate &rarr; immediately decelerate (short move, never reaches <code>max_speed</code>)</li>
</ul>
<p><img alt="&ldquo;Schematic position-versus-time plot (degrees vs seconds) with two S-curves. The curves start flat, become steeper mid-move, and flatten again, illustrating smooth acceleration and deceleration and how different motion profiles change the timing and steepness of the movement.&rdquo;" src="/assets/img/posts/2026-03-06-openscan3-firmware-smooth-moves/os3-04-motion-1.jpg"/></p>
<p><strong>Figure 1: Velocity over time (schematic)</strong><br/><br/></p>
<p>If we plot spatial position against time, the smoothness of the motion is obvious:</p>
<p><em><br/><img alt="Schematic plot of motor position (degrees) over time showing two S-shaped curves with the same final position: higher acceleration reaches the target sooner with a snappier start/stop, while lower acceleration ramps more gently and takes longer; note that slope approximately corresponds to velocity." src="/assets/img/posts/2026-03-06-openscan3-firmware-smooth-moves/os3-04-motion-2.jpg"/></em><em><br/></em><strong style="font-size: 0.875rem;">Figure 2: Position over time (schematic)<br/></strong><em style="font-size: 0.875rem;">The &ldquo;felt&rdquo; result: a smooth start/stop becomes a gentle S-curve rather than abrupt changes.</em></p>
<p>Still not convinced? See here:<br/></p>
<div style="max-width: 900px; margin: 1.2rem auto;">
<div style="position: relative; width: 100%; aspect-ratio: 16 / 9;"><iframe src="https://www.youtube.com/embed/UDOgNwDDQuM?rel=0" style="position: absolute; inset: 0; width: 100%; height: 100%; border: 0;" title="OpenScan3 motor controller demo">
</iframe></div>
</div>
<h2>The two settings that matter</h2>
<p>There are many configuration fields in OpenScan3, but for motion quality there are basically two responsible:</p>
<h3>1. <code>max_speed</code>
</h3>
<p>The maximum speed the motor is allowed to reach, measured in steps per second.<br/>Higher <code>max_speed</code> can reduce scan time, but it can also increase noise and vibration and the risk of skipped steps especially on high loads.</p>
<h3>2. <code>acceleration</code>
</h3>
<p>How quickly the motor ramps up (and ramps down) its speed, measured in steps per second&sup2;.</p>
<p>Acceleration is what makes motion feel &ldquo;snappy&rdquo; vs &ldquo;smooth&rdquo;:</p>
<ul>
<li>too high &rarr; jerky, harsh sound, higher chance of skipped steps</li>
<li>lower &rarr; softer starts/stops, more forgiving</li>
</ul>
<h2 id="tuning-guide">Tuning guide</h2>
<div style="display: grid; gap: 14px; margin: 18px 0;">
<div style="border: 1px solid rgba(0,0,0,0.12); border-radius: 14px; padding: 14px 16px;">
<p style="margin: 0 0 8px 0;"><strong>If motion feels too aggressive / jerky:</strong></p>
<ul style="margin: 0; padding-left: 1.2em;">
<li style="margin: 0;">reduce <code>acceleration</code>
</li>
</ul>
</div>
<div style="border: 1px solid rgba(0,0,0,0.12); border-radius: 14px; padding: 14px 16px;">
<p style="margin: 0 0 8px 0;"><strong>If everything feels smooth but too slow overall:</strong></p>
<ul style="margin: 0; padding-left: 1.2em;">
<li style="margin: 0;">increase <code>max_speed</code>
</li>
</ul>
</div>
<div style="border: 1px solid rgba(0,0,0,0.12); border-radius: 14px; padding: 14px 16px;">
<p style="margin: 0 0 8px 0;"><strong>If you hear rattling / the motor stalls / steps are skipped:</strong></p>
<ul style="margin: 0; padding-left: 1.2em;">
<li style="margin: 0;">reduce <code>max_speed</code>
</li>
<li style="margin: 0;">and/or reduce <code>acceleration</code>
</li>
<li style="margin: 0;">also check mechanical friction</li>
</ul>
</div>
</div>
<div style="border: 1px solid rgba(0,0,0,0.12); border-radius: 14px; padding: 14px 16px; margin: 18px 0;">
<p style="margin: 0 0 10px 0;"><strong>A good workflow is:</strong></p>
<ol style="margin: 0; padding-left: 1.2em;">
<li style="margin: 0 0 6px 0;">Start with conservative <code>max_speed</code>
</li>
<li style="margin: 0 0 6px 0;">Increase <code>acceleration</code> until it starts feeling harsh</li>
<li style="margin: 0 0 6px 0;">Back off a bit</li>
<li style="margin: 0;">Increase <code>max_speed</code> until you hit the next limiting factor (noise, vibration, skipping), then back off</li>
</ol>
</div>
