---
title: "OpenScan3 Firmware: Smooth Moves"
date: "2026-03-06T10:46:47+01:00"
author: "Elias Stognienko"
description: "OpenScan3 replaces OpenScan2’s “delay tuning” with a simple motion model: max_speed and acceleration . This post explains the new mental model (trapezoid vs triangle profiles) and gives a practical tuning guide to get smooth, reliable motor movement across devices."
categories:
  - "Firmware"
tags:
  - "openscan3"
  - "firmware"
  - "architecture"
  - "how-to"
image:
  path: "/assets/img/posts/2026-03-06-openscan3-firmware-smooth-moves/os3-motion-tuning-ba0710ed-016e-48e4-a8a5-8c0cbe45d79e.jpg"
redirect_from:
  - "/blogs/news/openscan3-firmware-smooth-moves"
  - "https://openscan.eu/blogs/news/openscan3-firmware-smooth-moves"
---

*This is the a blog post in a series on the OpenScan3 firmware. Read the [previous post here](https://openscan.eu/blogs/news/openscan3-coordinate-system-why-%CF%86-%CE%B8-instead-of-x-y-z). Comments, questions, or suggestions are always very welcome and a great help for future work on the firmware!*

**tl;dr:** OpenScan3’s motor controller uses a simple motion model (max speed + acceleration) instead of “delay tuning”.
The result is smoother motion, more predictable behavior, and easier configuration across devices.

The first part of the post is about the rationale of the new motor contoller. If you just want to know how to tune the settings, [skip right ahead to the practical guide](#tuning-guide).

## Why we entirely replaced the old motor control logic

OpenScan2 motion tuning mostly boiled down to step delays and a few ramp parameters. It worked, but it was hard to reason about:

- settings didn’t map cleanly to real-world motion,
- tuning wasn’t very transferable between devices,
- small changes could have big (and sometimes surprising) effects.

If you’re coming from OpenScan2, you might be looking for the old "delay" values.
In OpenScan3, you typically don’t need them anymore:
<code>max_speed</code> and <code>acceleration</code> give you a much more direct handle on how the device will move.

With OpenScan3 we rebuilt the motor controller around a simple motion model:
**accelerate → cruise → decelerate**.

Instead of tuning a *timer*, you tune *motion*.

## The mental model

OpenScan3 uses a simple motion profile that should feel familiar from school physics:
**uniform acceleration** for start/stop, and (optionally) **constant velocity** in between.

If we plot **velocity over time**, the shape is almost always one of these:

- **Trapezoid:** accelerate → cruise at <code>max_speed</code> → decelerate
- **Triangle:** accelerate → immediately decelerate (short move, never reaches <code>max_speed</code>)

![“Schematic position-versus-time plot (degrees vs seconds) with two S-curves. The curves start flat, become steeper mid-move, and flatten again, illustrating smooth acceleration and deceleration and how different motion profiles change the timing and steepness of the movement.”](/assets/img/posts/2026-03-06-openscan3-firmware-smooth-moves/os3-04-motion-1.jpg)

**Figure 1: Velocity over time (schematic)**

If we plot spatial position against time, the smoothness of the motion is obvious:

*![Schematic plot of motor position (degrees) over time showing two S-shaped curves with the same final position: higher acceleration reaches the target sooner with a snappier start/stop, while lower acceleration ramps more gently and takes longer; note that slope approximately corresponds to velocity.](/assets/img/posts/2026-03-06-openscan3-firmware-smooth-moves/os3-04-motion-2.jpg)***Figure 2: Position over time (schematic)***The “felt” result: a smooth start/stop becomes a gentle S-curve rather than abrupt changes.*

Still not convinced? See here:

<div>
<div><iframe src="https://www.youtube.com/embed/UDOgNwDDQuM?rel=0" title="OpenScan3 motor controller demo">
</iframe></div>
</div>

## The two settings that matter

There are many configuration fields in OpenScan3, but for motion quality there are basically two responsible:

### 1. <code>max_speed</code>

The maximum speed the motor is allowed to reach, measured in steps per second.
Higher <code>max_speed</code> can reduce scan time, but it can also increase noise and vibration and the risk of skipped steps especially on high loads.

### 2. <code>acceleration</code>

How quickly the motor ramps up (and ramps down) its speed, measured in steps per second².

Acceleration is what makes motion feel “snappy” vs “smooth”:

- too high → jerky, harsh sound, higher chance of skipped steps
- lower → softer starts/stops, more forgiving

## Tuning guide

**If motion feels too aggressive / jerky:**

- reduce <code>acceleration</code>

**If everything feels smooth but too slow overall:**

- increase <code>max_speed</code>

**If you hear rattling / the motor stalls / steps are skipped:**

- reduce <code>max_speed</code>
- and/or reduce <code>acceleration</code>
- also check mechanical friction

**A good workflow is:**

1. Start with conservative <code>max_speed</code>
2. Increase <code>acceleration</code> until it starts feeling harsh
3. Back off a bit
4. Increase <code>max_speed</code> until you hit the next limiting factor (noise, vibration, skipping), then back off
