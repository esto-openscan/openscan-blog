---
title: "Is OpenScan an Open Source project?"
date: "2024-02-04T13:30:00+01:00"
author: "Thomas Megel"
categories:
  - "Projects"
tags:
  - "open-source"
  - "openscancloud"
  - "community"
image:
  path: "/assets/img/posts/2024-02-04-is-openscan-an-open-source-project/2024-02-04-teachingtech.png"
redirect_from:
  - "/blogs/news/is-openscan-an-open-source-project"
  - "https://openscan.eu/blogs/news/is-openscan-an-open-source-project"
---

The short answer is absolutely yes, the longer answer gets a bit more nuanced and we will have to dig into some details. So if you are concerned or just interested, stick around and feel free to share your thoughts.

<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/dwRMK9LzBBc?si=myztSq5xz06ZMunV" title="YouTube video player" width="560"></iframe>

Michael aka TeachingTech's video sparked quite some discussion about the Open Source nature of the OpenScan project. In my humble opinion, the video is very well-balanced and gives a great overview of the OpenScan Mini. But there seem to be quite a few misconceptions and open questions raised in the comments, which I will try to answer in this post. **Please join in and add your concerns and thoughts, so that I can update the post accordingly!**

## Why Open Source matters?

Making something open is a contribution and a commitment to a larger goal. When I started my journey into the wonderful world of 3d scanning in 2017, there has been very little information on this (besides in academic papers). But the maker movement already amassed a ton of information about 3d printing, soldering, programming publicly... Since so many parts of the project would not be possible without people that shared their bits of knowledge, we feel absolutely obliged to give back our part to this great cycle!

## But isn't OpenScanCloud (OSC) a closed source solution?

Short answer, yes! OpenScanCloud (OSC) is and will stay closed source, but we will keep up the open access! We process hundreds of thousands of images every month on machines that not everyone wants or could afford. The OSC was built for internal use, but we quickly realized that we did not use anything close to its capacity. So in the sense of sharing, we opened up the access to this processing engine. At the beginning we used the data internally to improve the pipeline and add some nice features (in consent with the users).

## So OpenScan isn't so open after all?

There is a ton of documentation and options for photogrammetry available. Before building the OSC solution, we tested almost all available software options. People seem to overlook, that great photogrammetry software has been out there for many years. But with all tools, especially complex ones, these come with a learning curve. Especially the FOSS Meshroom is a widely underrated project - it comes with a ton of parameters, that have to be adjusted to the individual use-case. Unfortunately the default settings are somewhat suboptimal for the use with a turntable setup like the OpenScan devices.

**BUT, using the available options and documentation, you can easily run a fully open source pipeline locally without ever connecting to the internet.**

**We tried to do our fair share of contributing knowledge to those willing to learn a new technique. We provide intense documentation on the process and open sourced all our hardware. We provide free datasets. We even opened up our internal processing ressources for free external use.**

**See this section of our documentation of the photogrammetry process:**[**https://openscan-org.github.io/OpenScan-Doc/photogrammetry/basics/**](https://openscan-org.github.io/OpenScan-Doc/photogrammetry/basics/)

## But OSC seems superior, so the users are basically dependent on this solution?

This is a charming claim about the quality of the OSC, but it is definitely not the best option out there. With a little bit of tweaking, you can get similar results out of FOSS like Meshroom or VisualSFM. With paid software like Agisoft Metashape (or similar) you can definitely exceed those results from the OSC.

## But what about the data?

The OpenScan devices are built in a very modular way, so you can access your data at any point for local processing. Nothing is transmitted to our server without your explicit consent. The data on our servers is stored for 14days and deleted after that period without any backup.

## But what if OpenScan decides to charge monthly or sell out the service?

I bet, this happened to most of us, you like a service and build a workflow and after a while you find yourself forced into one of those many monthly subscriptions. We strongly oppose that trend, which we see as a perverted effect of late capitalism.

**Unfortunately, there is nothing but my word that I can give! OpenScanCloud is and will be open and free/donation-based as long as the OpenScan project lives. No external investment or interest will change that fact! We already turned down several, financially very tempting, offers, which have not been in line with our core values!**

OSC has been in operation since 2021 and the generous support of our Patreons ([https://www.patreon.com/OpenScan](https://www.patreon.com/OpenScan)) definitely helped a lot along the way.

## But what about the production files of the PCBs?

We published the wiring diagrams of our hardware, so that you can easily build your own version. The board is simple enough, that people have done it on breadboards..

Providing the production-ready files will not happen, in line with many other and larger open source conpanies like PRUSA or the Raspberry Pi foundation!

**Please let's try to have a constructive discussion. I will try to answer all questions as best as I can and I will update this blog post accordingly.**

**Happy scanning,**

**Thomas**
