---
title: "OpenScan3 Firmware: An Architectural Overview"
date: "2026-01-23T13:45:49+01:00"
author: "Elias Stognienko"
description: "An overview of the architecture behind the OpenScan3 firmware, explaining core design decisions, abstractions and how different parts of the system fit together."
shopify_summary_html: |-
  <blockquote data-start="229" data-end="393">
  <p data-start="231" data-end="393">An overview of the architecture behind the OpenScan3 firmware, explaining core design decisions, abstractions and how different parts of the system fit together.</p>
  </blockquote>
categories:
  - "OpenScan Blog"
tags:
  - "Firmware"
image:
  path: "/assets/img/posts/2026-01-23-preview-of-the-openscan3-firmware-a-fresh-start-with-modern-architecture/os3-dev-quadrat-20c2d0f9-615c-4808-b209-089bb8cdbb82.jpg"
redirect_from:
  - "/blogs/news/preview-of-the-openscan3-firmware-a-fresh-start-with-modern-architecture"
  - "https://62f7a3-4.myshopify.com/blogs/news/preview-of-the-openscan3-firmware-a-fresh-start-with-modern-architecture"
---

<h5><em>About this post</em></h5>
<p><em><br/></em><em>This is the first post in a small series about the architecture of OpenScan3. The idea is to explain some core design decisions and concepts.<br/></em><em>This post is written by me, Elias (esto), not by Thomas. I work on the OpenScan3 firmware and spend a lot of time developing and maintaining the code.<br/></em><em>If you have thoughts, questions, or suggestions, feel free to send me an <a href="mailto:esto@openscan.eu" rel="noopener noreferrer nofollow">email</a>. These conversations help shape future work on the firmware.<br/></em></p>
<p>&nbsp;</p>
<h2>Introduction</h2>
<p>For nearly a year now, we've been working on OpenScan3, a completely rewritten firmware for OpenScan devices. This post provides an overview of why a rewrite was necessary and how the new firmware is designed from the ground up.</p>
<p>The firmware will be compatible with all existing OpenScan hardware. An early alpha version is available on <a href="https://github.com/OpenScan-org/OpenScan3/releases" rel="noopener noreferrer nofollow">GitHub</a>. At this stage, OpenScan3 is mainly aimed at developers and advanced users who want to explore, test and help shape the firmware.</p>
<p>Some parts of this article are technical. If you are more interested in practical implications, you can safely skip the deeper sections.</p>
<h2>Why a new Firmware?</h2>
<p>The previous OpenScan2 firmware was built on <a href="https://nodered.org" rel="noopener noreferrer nofollow">Node-RED</a> and was essentially frontend-driven. Logic for individual components was spread across UI elements, which made the system harder to extend and maintain. It was also tightly coupled to Node-RED as the frontend and over time it became less reasonable to add new features.</p>
<p>As OpenScan grew beyond a single device and use case, the existing architecture became a limiting factor rather than an enabler.</p>
<h2>What Makes the new Firmware Different?</h2>
<p>OpenScan3 takes a fundamentally different approach:</p>
<ul>
<li>
<strong>Pure Python backend</strong> based on <a href="https://fastapi.tiangolo.com" rel="noopener noreferrer nofollow">FastAPI</a>
</li>
<li>
<strong>Type-safety</strong> using <a href="https://docs.pydantic.dev/latest/concepts/models/" rel="noopener noreferrer nofollow">Pydantic models</a> for data validation</li>
<li>
<strong>Versioned REST API</strong> for stable client integration</li>
<li>
<strong>Model-View-Controller inspired design</strong> for clean separation of concerns</li>
<li>
<strong>Decoupled controller components</strong> with defined interfaces, enabling easy replacement and improvement</li>
<li>
<strong>API documentation</strong> with automatic OpenAPI/Swagger generation and versioning</li>
</ul>
<h2>The Big Picture: How Everything Fits Together</h2>
<p>At its core, OpenScan3 follows a simple but powerful architecture: a small set of clearly separated layers working together:</p>
<p><img alt="Diagram of the OpenScan3 firmware architecture, showing clients at the top, the API layer, the business logic layer, and the physical hardware at the bottom." src="/assets/img/posts/2026-01-23-preview-of-the-openscan3-firmware-a-fresh-start-with-modern-architecture/openscan3-01-architecture-overview.jpg"/></p>
<h2>The API Layer: The Gateway to the Scanner</h2>
<p>The API layer is the main entry point for interacting with an OpenScan device. External applications do not talk to the hardware or internal services directly. Instead, all communication goes through a standardized REST API, whether you use a web browser, a mobile app, or a custom script.</p>
<p>The API is designed to remain stable over time. Endpoints are versioned (for example <code>/v0.5/</code>, <code>/v0.6/</code>, or <code>/latest/</code>), so existing integrations continue to work even as new features are added. The API also provides automatic documentation at <code>/latest/docs</code>, showing available endpoints and data structures. Consistent patterns and data types across endpoints make the API easier to learn and use.</p>
<h2>The Controller Layer: Where the Actual Work Is Done</h2>
<p>This is the &ldquo;brain&rdquo; of the scanner. It is split into hardware controllers and service controllers.</p>
<!-- TODO: insert diagram/image here -->
<h3>Hardware Controllers</h3>
<p>OpenScan3 treats hardware through small, well-defined interfaces. From the outside, cameras, motors and lights are controlled in a consistent way, even though their internal behavior can differ significantly.</p>
<p>Some components, such as motors or cameras, can be busy while performing an action. Others, like lights, simply switch on or off. These differences are handled inside the hardware controllers and are not exposed to the rest of the system.</p>
<p>Each controller is encapsulated behind a common interface. This makes it possible to replace concrete implementations without changing higher-level logic. For example, an Arducam IMX519 can be replaced with a DSLR camera, or one motor driver can be swapped for another, while the rest of the application remains unchanged because the interface stays the same.</p>
<p>If you are curious about how this is implemented, the code is a good starting point and future posts in this series will go into more detail.</p>
<h3>Service Controllers</h3>
<p>Service controllers orchestrate higher-level operations:</p>
<ul>
<li>
<strong>Project management</strong> handles creating, storing and organizing scan projects</li>
<li>
<strong>Task management</strong> ensures long-running operations don&rsquo;t block the system and can be paused, resumed, or cancelled</li>
<li>The <strong>scan task</strong> coordinates the scan routine: moving motors, triggering the camera with specific settings and saving images</li>
</ul>
<h3>The Task System: Flexible and Extensible</h3>
<p>One of the most important additions in OpenScan3 is the centralized task system. You can think of it as a job scheduler that helps the scanner run operations safely in a defined order and, where possible, even concurrently.</p>
<p>This is also where custom tasks can live, such as scan routines, image analysis, or post-processing steps. Thanks to the interfaces described above, tasks can focus on the &ldquo;what&rdquo; without needing to care about hardware details.</p>
<p>Tasks are automatically discovered at startup, which makes it easier for the community to add new functionality without changing core code. A follow-up post will explain this in more detail with examples.</p>
<h2>Models &amp; Configuration</h2>
<p>Throughout the system, Pydantic models define what data looks like. You can think of them as contracts that allow controllers and tasks to speak the same language.</p>
<p>Because controllers depend on these model contracts rather than concrete implementations, they remain interchangeable and easy to test. The same models are used across tasks and controllers keeping the system consistent and predictable. The API layer stays intentionally thin.</p>
<p>Configuration complements this by describing the system declaratively: which hardware exists, how components behave and how controllers are connected. By moving these decisions into structured configuration files, OpenScan3 avoids hardcoded setups and remains adaptable to different scanner models and future extensions.</p>
<h2>Summary</h2>
<p>In short, models define what exists, configuration defines how it is wired and controllers define what happens. Together, they keep OpenScan3 flexible, extensible and maintainable as new hardware, tasks and workflows are added.</p>
<h2>Contribution to the OpenScan Ecosystem</h2>
<p>With OpenScan3, we aim to provide a flexible, modular foundation that complements the broader OpenScan ecosystem. Many excellent firmwares, tools and workflows already exist and our goal is not to replace them, but to make it easier to experiment, share and build on each other&rsquo;s work.</p>
<p>By separating models, controllers, tasks and interfaces, the firmware allows different parts of the system to evolve independently while still fitting together. Contributors can focus on the areas they care about (hardware support, scan routines, automation, or user interfaces) without needing to master the entire codebase. Improvements in one area tend to benefit other parts of the system as well.</p>
<p>In that sense, OpenScan3 is a contribution rather than a replacement: a shared starting point designed to make collaboration smoother, encourage experimentation and make it easier to integrate new hardware, workflows and ideas.</p>
<hr/>
<p><em>Do you have questions or suggestions? Join the discussion on <a href="https://discord.gg/eBdqtdkXyF" rel="noopener noreferrer nofollow">Discord</a> or on <a href="https://github.com/OpenScan-org/OpenScan3" rel="noopener noreferrer nofollow">GitHub</a>.</em></p>
