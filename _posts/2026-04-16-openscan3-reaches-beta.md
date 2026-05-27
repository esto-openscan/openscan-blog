---
title: "OpenScan3 Beta"
date: "2026-04-16T13:31:25+02:00"
author: "Elias Stognienko"
description: "OpenScan3 is moving from alpha to beta. The core architecture is now solid enough for broader real-world testing, while development continues to focus on refinement, stability, and closing the remaining feature gaps."
categories:
  - "News"
tags:
  - "firmware"
  - "openscan3"
image:
  path: "/assets/img/posts/2026-04-16-openscan3-reaches-beta/openscan3-beta-2d3e53ec-5997-4802-a69f-09bacfbc0146.png"
redirect_from:
  - "/blogs/news/openscan3-reaches-beta"
  - "https://openscan.eu/blogs/news/openscan3-reaches-beta"
---

We are happy to announce that OpenScan3 is moving from alpha to beta.

This means the core architecture and main workflows are now solid enough for broader real-world testing, and that development can focus more on refinement, stability, and closing the remaining feature gaps.

### What beta means for OpenScan3

OpenScan3 has matured to the point where it is no longer just an early experiment. The backend and firmware foundation are in place, the web frontend has become much more usable, and the overall system is now coherent enough that broader testing makes sense.

OpenScan3 now has a modular backend and firmware architecture, a modern SPA frontend, and a more reliable image and update pipeline. Together, these pieces make the project significantly easier to use, maintain, and improve than in its earlier stages.

### What is still missing / still rough

There are still known rough edges and missing pieces. For example, support for the Arducam Hawkeye is greatly improved but still has minor issues, including mismatches between preview crop and captured image in the frontend. The frontend still needs further UI and UX refinement, and some API endpoints may still change as the project continues to stabilize.

This is exactly why we consider this a beta phase: the foundation is there, but broader testing and feedback are still needed to make the system more reliable and polished.

### Who should try it now

OpenScan3 beta is a good fit for makers, contributors, and technically comfortable users who want to work with the new platform already and can tolerate occasional changes or rough edges.

If you enjoy testing evolving software, reporting issues, or helping shape workflows and features, this is a good time to get involved.

If you need a fully polished, frictionless, production-ready experience, it is still better to treat OpenScan3 as work in progress.

### What feedback we need

At this stage, real-world feedback is especially valuable.

We want to know where actual scan workflows still break down, which rough edges are more confusing than expected, what hardware-specific problems still exist, and which missing features still prevent regular use.

Bug reports, workflow feedback, and reports about unclear or non-obvious behavior are all highly appreciated.

### What comes next

The next steps toward a stable release include continued work on frontend polish and usability, improved hardware support, and improving the update routine to include system packages.

Some of the larger items on the roadmap include UART motor control, and a CLI client plus Python SDK for smoother workflow integration.

### Thanks

A big thank you to everyone contributing to OpenScan and everyone using it in practice.

Using OpenScan, sharing results, building scanners, wiring PCBs, testing unfinished features, and reporting problems is what turns this into a real open-source and open-hardware project.

It is a privilege to work in open source and open hardware, and none of this would be possible without the people around the project.

Thank you.
