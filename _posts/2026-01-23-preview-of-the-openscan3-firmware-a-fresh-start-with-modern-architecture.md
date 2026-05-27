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
  - "Firmware"
tags:
  - "openscan3"
  - "firmware"
  - "architecture"
image:
  path: "/assets/img/posts/2026-01-23-preview-of-the-openscan3-firmware-a-fresh-start-with-modern-architecture/os3-dev-quadrat-20c2d0f9-615c-4808-b209-089bb8cdbb82.jpg"
redirect_from:
  - "/blogs/news/preview-of-the-openscan3-firmware-a-fresh-start-with-modern-architecture"
  - "https://openscan.eu/blogs/news/preview-of-the-openscan3-firmware-a-fresh-start-with-modern-architecture"
---

##### *About this post*

*This is the first post in a small series about the architecture of OpenScan3. The idea is to explain some core design decisions and concepts.**This post is written by me, Elias (esto), not by Thomas. I work on the OpenScan3 firmware and spend a lot of time developing and maintaining the code.**If you have thoughts, questions, or suggestions, feel free to send me an [email](mailto:esto@openscan.eu). These conversations help shape future work on the firmware.*

## Introduction

For nearly a year now, we've been working on OpenScan3, a completely rewritten firmware for OpenScan devices. This post provides an overview of why a rewrite was necessary and how the new firmware is designed from the ground up.

The firmware will be compatible with all existing OpenScan hardware. An early alpha version is available on [GitHub](https://github.com/OpenScan-org/OpenScan3/releases). At this stage, OpenScan3 is mainly aimed at developers and advanced users who want to explore, test and help shape the firmware.

Some parts of this article are technical. If you are more interested in practical implications, you can safely skip the deeper sections.

## Why a new Firmware?

The previous OpenScan2 firmware was built on [Node-RED](https://nodered.org) and was essentially frontend-driven. Logic for individual components was spread across UI elements, which made the system harder to extend and maintain. It was also tightly coupled to Node-RED as the frontend and over time it became less reasonable to add new features.

As OpenScan grew beyond a single device and use case, the existing architecture became a limiting factor rather than an enabler.

## What Makes the new Firmware Different?

OpenScan3 takes a fundamentally different approach:

- **Pure Python backend** based on [FastAPI](https://fastapi.tiangolo.com)
- **Type-safety** using [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/) for data validation
- **Versioned REST API** for stable client integration
- **Model-View-Controller inspired design** for clean separation of concerns
- **Decoupled controller components** with defined interfaces, enabling easy replacement and improvement
- **API documentation** with automatic OpenAPI/Swagger generation and versioning

## The Big Picture: How Everything Fits Together

At its core, OpenScan3 follows a simple but powerful architecture: a small set of clearly separated layers working together:

![Diagram of the OpenScan3 firmware architecture, showing clients at the top, the API layer, the business logic layer, and the physical hardware at the bottom.](/assets/img/posts/2026-01-23-preview-of-the-openscan3-firmware-a-fresh-start-with-modern-architecture/openscan3-01-architecture-overview.jpg)

## The API Layer: The Gateway to the Scanner

The API layer is the main entry point for interacting with an OpenScan device. External applications do not talk to the hardware or internal services directly. Instead, all communication goes through a standardized REST API, whether you use a web browser, a mobile app, or a custom script.

The API is designed to remain stable over time. Endpoints are versioned (for example <code>/v0.5/</code>, <code>/v0.6/</code>, or <code>/latest/</code>), so existing integrations continue to work even as new features are added. The API also provides automatic documentation at <code>/latest/docs</code>, showing available endpoints and data structures. Consistent patterns and data types across endpoints make the API easier to learn and use.

## The Controller Layer: Where the Actual Work Is Done

This is the “brain” of the scanner. It is split into hardware controllers and service controllers.

TODO: insert diagram/image here

### Hardware Controllers

OpenScan3 treats hardware through small, well-defined interfaces. From the outside, cameras, motors and lights are controlled in a consistent way, even though their internal behavior can differ significantly.

Some components, such as motors or cameras, can be busy while performing an action. Others, like lights, simply switch on or off. These differences are handled inside the hardware controllers and are not exposed to the rest of the system.

Each controller is encapsulated behind a common interface. This makes it possible to replace concrete implementations without changing higher-level logic. For example, an Arducam IMX519 can be replaced with a DSLR camera, or one motor driver can be swapped for another, while the rest of the application remains unchanged because the interface stays the same.

If you are curious about how this is implemented, the code is a good starting point and future posts in this series will go into more detail.

### Service Controllers

Service controllers orchestrate higher-level operations:

- **Project management** handles creating, storing and organizing scan projects
- **Task management** ensures long-running operations don’t block the system and can be paused, resumed, or cancelled
- The **scan task** coordinates the scan routine: moving motors, triggering the camera with specific settings and saving images

### The Task System: Flexible and Extensible

One of the most important additions in OpenScan3 is the centralized task system. You can think of it as a job scheduler that helps the scanner run operations safely in a defined order and, where possible, even concurrently.

This is also where custom tasks can live, such as scan routines, image analysis, or post-processing steps. Thanks to the interfaces described above, tasks can focus on the “what” without needing to care about hardware details.

Tasks are automatically discovered at startup, which makes it easier for the community to add new functionality without changing core code. A follow-up post will explain this in more detail with examples.

## Models & Configuration

Throughout the system, Pydantic models define what data looks like. You can think of them as contracts that allow controllers and tasks to speak the same language.

Because controllers depend on these model contracts rather than concrete implementations, they remain interchangeable and easy to test. The same models are used across tasks and controllers keeping the system consistent and predictable. The API layer stays intentionally thin.

Configuration complements this by describing the system declaratively: which hardware exists, how components behave and how controllers are connected. By moving these decisions into structured configuration files, OpenScan3 avoids hardcoded setups and remains adaptable to different scanner models and future extensions.

## Summary

In short, models define what exists, configuration defines how it is wired and controllers define what happens. Together, they keep OpenScan3 flexible, extensible and maintainable as new hardware, tasks and workflows are added.

## Contribution to the OpenScan Ecosystem

With OpenScan3, we aim to provide a flexible, modular foundation that complements the broader OpenScan ecosystem. Many excellent firmwares, tools and workflows already exist and our goal is not to replace them, but to make it easier to experiment, share and build on each other’s work.

By separating models, controllers, tasks and interfaces, the firmware allows different parts of the system to evolve independently while still fitting together. Contributors can focus on the areas they care about (hardware support, scan routines, automation, or user interfaces) without needing to master the entire codebase. Improvements in one area tend to benefit other parts of the system as well.

In that sense, OpenScan3 is a contribution rather than a replacement: a shared starting point designed to make collaboration smoother, encourage experimentation and make it easier to integrate new hardware, workflows and ideas.

---

*Do you have questions or suggestions? Join the discussion on [Discord](https://discord.gg/eBdqtdkXyF) or on [GitHub](https://github.com/OpenScan-org/OpenScan3).*
