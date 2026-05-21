---
title: "OpenScan3 Beta — What's New"
date: "2026-04-17T11:46:56+02:00"
author: "Thomas Megel"
categories:
  - "OpenScan Blog"
tags: []
image:
  path: "/assets/img/posts/2026-04-17-openscan3-beta-whats-new/openscan3-beta.png"
redirect_from:
  - "/blogs/news/openscan3-beta-whats-new"
  - "https://62f7a3-4.myshopify.com/blogs/news/openscan3-beta-whats-new"
---

We just announced that OpenScan3 is moving into beta. [That post covers what beta means](https://openscan.eu/blogs/news/openscan3-reaches-beta) and where we still need help. This one is about what's actually in it. Elias has been working on the new firmware for over a year, and it's finally ready for broader use. Here's what changed.

## **What does the new firmware mean for you:**

### **2-3 times faster capturing**

It is now significantly faster to capture a dataset thanks to improved handling of the camera and the motion controller. Capture times with the default IMX519 vary between 0.7s for manual focus and 1.2s for autofocus of full-res images (old software: 3-6s). The 64MP Hawkeye camera takes 5 - 12s per full-res image. This means that the new firmware runs at similar speeds to OpenScan2 at four-times higher pixel count!

### **QR Code Wifi Setup**

Setting up WiFi on a Raspberry Pi has always been a pain. We implemented a relatively simple solution for the user, so that you can just share the WiFi credentials directly from your smartphone by showing the scanner the generated QR code (which usually is hidden somewhere in your smartphone settings).

### **Setup wizard & custom presets**

On first boot, you can simply select the type of scanner and electronics.
OpenScan3 now supports the community-built blackshield out of the box, alongside the Mini v2 and Midi.

![](/assets/img/posts/2026-04-17-openscan3-beta-whats-new/openscan3-firmware-setupwizard.jpg)

### **Polished UI & Extensive tooltips**

The much more modern and responsive interface now includes tooltips throughout, explaining the many options available.

### **Photogrammetry Feature preview**

You can now get live feedback on the surface quality of your scan object. Toggle the overlay and "good" areas appear red while featureless areas appear blue (see below). This is especially useful for beginners getting a feel for which surfaces are easy to scan and which ones will need matting spray or a different approach.

![](/assets/img/posts/2026-04-17-openscan3-beta-whats-new/openscan3-firmware-histo.jpg)

### **Histogram**

A standard photography tool is now built into the firmware. The histogram gives you quick, intuitive feedback for setting shutter speed and avoiding over- or underexposed images.

### [**Arducam Hawkeye (64MP)**](https://openscan.eu/_t/c/v3/AACZWspVW1O3M8AoLInWE3nR-X23UpMzT3tnFLAsdqmTO4wgMgrCZxjiRpcqGmswcCZHQ-sz5Gh5eFByrCqv6UpwHDxZmfvVazwe_8C92c0BTNv_Mt1EKIeQoEoHIE2Xg_0mU4F-7EkCp0JVMMGnEy2O_axsgc59Vr6-MEinML_zZF-8hyruvmMyD41NPBpEUdhqsmYhZN9m2bWBFc6a_sivjvM0JkypO-j8pMNifkbNIv7aLey6DO5tG7eINUBo_gSx_rLfqIySPiMCDfq198DNfE6uwdq2TVZoj8B0Hy8vPpdyj-bjGW11jRrsJuljqzumbxdJTFHNch5b_HxI-UVZtCpU4BigR_Hi6QrmU-sfmQX6MKWO6jHeD28484esMWezWCe-qJ8wE7lazQCRlB_eGS16GrkptFejjFkgcWark1VUEOcYUvzHOHHBy0htQu1V8MLFtXz8wfESIVGfdcz-)**camera**

It is finally possible to use the 64MP Arducam Hawkeye. The new firmware fully supports this higher-resolution camera, which notably improves the scan quality ([see OpenScan Benchy](https://openscan.eu/_t/c/v3/AABynB9pep5MHehphAHTdWuCSoCUcYCnedOBwOG-e6Wt4UFbixpQRi2OXxF2jTWEcR4MA-4A6tdxjCxYMhOLAnoIrX4gLwg57do9BuKcaASnZkyVTaYuIVOwNUjfdBIrbiuP8ohCtYUr86aWxNVCnMk1UFCIKMSoG4Il492dmBvDP5KnwKqlEbljGrpx1ci6baG5K3VkvGDVfPA1y8ei8vXp5sCXMn9ZNQReb2dTzEM4Z7Obo09naIkcxIDNcG5Vslt-XpaoEG-67kNduLm_YcmVN1EG-N4VYNiJ-738bYR0uW4enIo71RkXxWBqffKjU1KERvmIjAmNkNbCWZQXoX0vBZNgt7sSGvecFOzz_bPHtJs3ArvqaNo_rOjPrj6zZwU3NrXAv6ebfGBMP8g=)).

The camera is [available in our shop](https://openscan.eu/_t/c/v3/AADmQzkf69c1u5mPYJoUJODXfbOupJf5Syn72uMReeoL6V29y4lSsps8C30Xbzm9fSmmyiH9oUgl7hf0YVRVh9Z2hXXMXufxdFS0Z7KGtuXktcVB06Cbcl4qvr4zS4HE45uEZxs0firZ2UE5H3OYmKoKbmgnGgcDlaVfgDsuEfuO5T1ihRGLAPsYPi_meGIumWG3XZJXGgnBKFvgvdyvTiV2wPi9FeXNf_VzdTYOX3sRi6qz8FZj1eRKPfY491uH_NUNgGAuh6BwBbFNGIRz-3UOcgsEj_ope1w37KLYWIinis6KhkZQuB1_O01onwGwYd38SAkB0Ob7Vzonf-WKjHEBWRQ909v6MojFSpVLC7_Sze-YoI2ZLt-6T13c2mlXazNTQxKYUI9N6TS--QRdC7Chx8RxA5cxAdVYodjZzo5oprDgg19Hs6ENm7RDWrkO6YPbFXUTP-TIiesoP4VwaR49). Note, that you'll need to select the right Raspbian Image for your SD card. Currently we need a separate image for the Hawkeye camera.

### **Endstops & Angle Clamping**

Motors can now be constrained to defined bounds, either via physical endstops or software clamping. Endstop support is currently implemented for the blackshield; we plan to wire up the endstop connectors on the default pre-soldered Pi shield soon.

### **Seamless OpenScan Cloud integration**

First, the important part: OpenScan Cloud is and will always be optional. The firmware is open source and it will always be an open and hackable system.

That said, we've made the cloud pipeline much easier to use. Activate the Cloud, enter your token in the settings and you can upload scans and download the finished model directly on the device, which could all be automated..

![](/assets/img/posts/2026-04-17-openscan3-beta-whats-new/openscan3-firmware-cloud.jpg)

### **On-device focus stacking**

Close-up shots often suffer from a very narrow depth of field. Only a narrow slice of the object is sharp, and everything in front of or behind it blurs out. Photogrammetry struggles with those blurry areas and 3D scans might fail or contain a lot of artifacts. Taking images at varying lens positions and combining these photos with focus-stacking can solve this issue.
OpenScan3 now does this focus stacking directly on the Raspberry Pi, which is a significant boost to scan quality.

![](/assets/img/posts/2026-04-17-openscan3-beta-whats-new/openscan3-firmware-stacking.gif)

## **What's next**

### **Software Development Kit (SDK)**

At this point, the new API already offers granular control over the device and exposes most of its functionality to the tech-savvy user. We're wrapping those functions into an SDK so you can build end-to-end workflows: control the scanner, capture images, post-process, run photogrammetry.

### **External camera trigger & DSLR support**

A wider range of cameras opens up real quality gains for 3D scans and other applications. nThe new modular structure makes adding new cameras much more straightforward.

### **3D Viewer and simple mesh tool**

We're building a simple in-browser tool for mesh simplification and color correction, so you can turn raw scans into game-ready assets without leaving the browser.

![](/assets/img/posts/2026-04-17-openscan3-beta-whats-new/openscan3-firmware-3dviewer.jpg)

**For developers, companies and researchers**

OpenScan3 is a solid foundation for any project that needs precise motion control, one or more cameras, and configurable I/O. That includes motorized camera sliders, microscopy stages, product photography rigs, stop-motion setups, and plenty more we haven't thought of yet.

Both software and hardware are easily customizable. If you are interested in the technical details of the software, check out the [OpenScan3 code on Github](https://openscan.eu/_t/c/v3/AACoAXronE5rxq149vHSrhX1Sm9bQTGJPD1gVQiFeGsZLk6kaK1XOtW30oVWyL4mHKp_x_fGg0BkfzwrfacOtMwlOJKead6swmp9UhshyviNWvXxK25ycxiPUW4BXTAonkFwrDxi6v0_Jxq-UEYuyUhmThrJWo2wiaJ6HVuHoWBPEYt1f8ej5QgT-8bQJS_vdEna-nE2kWrXp81FBlW8R2vrhh7y5SOFNfsixBlaXge2aXCRBpELEwqlZDS4eEZfuV4JxcFV1twpgQpfJ_c_dsLXkB7AshfgqEqSrzbwBw==) and [our recent blog posts](https://openscan.eu/_t/c/v3/AACoLizs32ziJs-GxkqCg4T3nD1ETziBV-mk-CiE5CNs78f41Tu1xYSjSdZM4z4IaD52e4SPgfeTkcYk2hiZxo8n02IVC8eZJ7rqpHwfzBNnOvUOZck-Q5LLHvDWIrFnEXIWL9NCT_mov6ec_RukeDqqfT-bcDFl4GNTi_aogo4g9bcuAftJ1perFLpy8lc23PNaHk8VtnG1g_68Xd6NNE9tM1y_wzYDRM5x6SFJ3hVY25TmwtzvyMjLEy1i8_DWJCAboOXfWUtu7YqwuNqEo2NurnmE6fS0tZ-lxHyPBKurMVLY4048GZXJODfRR_PEDomfZRPFE45jVvismjNZWcjVJqNyIWCBueVQXmJx38u1kYIZaolyRpC6qni9wrRiDrQb6wm2thj-zr6YguUXrnzOZKEKLEW9loqSG4bIjSxh4lgWYVhEaca_F2YYWEY6P5Nr-FnF87pMHg==).

And if you need a custom solution, feel free to reach out at any time!

**Getting started:**

Grab a new microSD card and follow [the setup guide in this blog article](https://openscan.eu/_t/c/v3/AAB9WAJbhMtX_v1hHjHEm9xTJlXZQwlCdV0Si1zaoE-1jZZo3homCWg3JUZQfRQpD2yUQ-kicQRW7G8M6dZeBsobEFwC7zauolBkf8zwzN6HkkcYduWlclqo_7Fajr-RJQ8I9Bh1FxDEJhXyLsO7L76aY2KRMxcZWnN_UH-gGsol5nRAWPDhRlHQX4TtTXd6msHmFb2e7RPraNF_5h7lPc0Ohao6EkbpC8D7U9CVQkOetAY-6pNNfM1NMJxOxXQazQ06KJyIDpcBCL4KG2zhyOBmMbSxVPaZfP4Yu_D-FBthmvD_nXdU_bvv92qcrO6A0Pizd-8KySNVp18n5ywMROVXvMDZQGE0onSyoxQas-Ka--9jz_D6Xoh8bl82jg-2AQXioYgkBFtGQLtH5VLyHvo5OufYrIqBg39qjwDKzHWgwvYXqzZKtGkRXiFoTBtv41i11Cil615eGGmwjiRMQYNz-3XFkGcNmgSrKhjgdA-ubTAh0PJHYh4=).
The firmware is in beta, so expect some minor changes. You may need to reflash at some point. That said, the current state is already a significant upgrade for almost all users. If you're not sure, if the update is right for you, check out this [blog article about the meaning of the beta state](https://openscan.eu/_t/c/v3/AADQ3zV8LQwJO-1Hmr0Ol_vZBWNIcvQ_sUcd8a1PmDxyz4_WgvHGGbjv0yaOyVMEkHkPIixpjkf0TxzJF2fjrUrYHyu8ZuptRUfqbpwJnJmRco-AfJ4rJ6eeTYe-uzy9NI19vQm1aQcq2LiHsx93lVproL3i97ZDzWhcM7r7OBwAhlua9-TyxDaI0TdrvPVufrxpYzHXtf4A7Y3k2o7_PmnCNidv3z2ANbXtoTpTA5DIggYso3xKDr-B58z8i3nNOwu3wUdZT_oFg9n-ZtmMqfvM2BXMUW3mOjytIWNwe5E5R95Xpprg4RIPh1p7z27UQCI8bhoQK3fAjN6ZEz_x_pWsxh5G8cGOlxbP0J__e2UsW75BEQon5YzAx3ty7nQKi7C8FbQiSNNa2eRlzKNNySHMk2Gr4SUCm9g3vKpTLbe0a5ZOdHVCckgiilocygx4edcv8uczDGhK6irG1lSZHPQvQKNidWbZYVLfmHQ-F7Do)and feel free to join the [discussion on Discord](https://discord.com/invite/gpaKWPpWtG).
