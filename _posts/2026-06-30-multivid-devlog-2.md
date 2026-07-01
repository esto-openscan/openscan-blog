---
title: "Multivid Devlog 2: Three Camera Nodes and a first Video"
date: "2026-07-2T12:00:00+02:00"
author: "Elias Stognienko"
description: "Turning three Raspberry Pi Zero camera nodes into a small recording workflow: positioning, harvesting, stringouts, and a first scanning video."
categories:
- "Projects"
tags:
- "openscan"
- "multivid"
- "prototype"
- "multicamera"
- "automation"
- "raspberry pi"
- "ansible"
- "video"
image:
   path: "/assets/img/posts/2026-06-30-multivid-devlog-2/cover-500x500.webp"
---



This is the second part of a series of posts about the development of a multicamera recording setup with low-cost hardware components based on Raspberry Pi Zero boards.

In the [first post](https://blog.openscan.eu/posts/multivid-devlog-1/), I described how we set up the camera nodes and showed the first results.


For this next milestone, I set out to solve some very practical problems: positioning the camera nodes, starting and stopping recordings without juggling terminal commands, and getting the recorded files from the distributed nodes back onto my editing PC.

At first, this sounded like a fairly technical milestone, but while working on this, something way more interesting and enjoyable happened: while adding the features, I started to discover a workflow.  This post is about the small tools that made cutting the first video possible.


## The Setup

I chose to use our photo booth because it not only offers a frame to attach the camera nodes to, it also has controlled lighting, which is important to get a consistent and calm-looking video. Because this is a prototype, I used the obvious professional-grade mounting solution: zip ties and cardboard.

<div class="row g-3 my-3">
  <div class="col-12 col-md-6">
    <img src="/assets/img/posts/2026-06-30-multivid-devlog-2/panorama-view-1000x1000.webp" alt="Photo booth setup" class="img-fluid w-100">
  </div>
  <div class="col-12 col-md-6">
    <img src="/assets/img/posts/2026-06-30-multivid-devlog-2/prototype-cardboard-1000x750.webp" alt="Prototype cardboard" class="img-fluid w-100">
  </div>
</div>


The nodes could record, but operating a headless multicam setup from separate URLs and CLI commands was still clumsy. So it was time to let AI do what it is currently good at: quickly sketching a slightly weird but useful internal dashboard that I probably would not have taken the time to build by hand at this stage.

As you can see in the screenshot below, we have the "Operator Dashboard," which offers a quick overview of our three camera nodes and exposes the controls we need.

![inital Multivid dashboard](/assets/img/posts/2026-06-30-multivid-devlog-2/dashboard-first-glance-1000x414.webp)

Our low-res preview reveals that the initial positioning needs some rework and more importantly, that we need a setting to flip the front and top camera node picture before proceeding.

After applying the necessary patches and repositioning, we can see that the angles look good now and that we are roughly within the center of the images. The upright frame within the picture shows the area we could use if we want to create vertical videos, which is handy if we later decide we want to create a smartphone-targeted video out of the recording.

![Multivid Dashboard](/assets/img/posts/2026-06-30-multivid-devlog-2/dashboard-positioned2-1000x518.webp)

But we also see in the pictures that the scanner almost fills up the whole field of view of our cameras.

![Reference Still](/assets/img/posts/2026-06-30-multivid-devlog-2/reference-still-1000x751.webp){: width="972" height="589" .w-50 .right}

This is a huge problem because you wouldn't see, for example, any manipulation by hand which is problematic if we want to create assembly tutorials and the like! But then I realized this was most likely not a small FOV of the camera but rather the smaller sensor area of the camera preview mode. The still image (that's how high-res photos are called) confirms this.

Good thing we can pull these reference stills from the Dashboard too!

After positioning I did a calibration to lock the camera controls in place which ensures that different takes won't look different. After this I was ready to record our very first session "hello_world_01" using `Multivid`. Spoiler: It went so well I didn't need to create a "_02" version ;)


## Taking the actual footage

Because we want to show how OpenScan devices work, I wanted to scan the OpenScan Benchy[^benchy].

I recorded a few takes, including a staged placing of the Benchy, the scan and a few experimental shots, which I will show you later. Here I want to reflect on the workflow:


I really like it! With the Multivid setup I can feel how my creativity is stimulated. I immediately want to try new scenes or lighting setups, like in Take 05. When it comes to visual work (video, image, posters), I usually do not plan every visual detail upfront.[^perspective] I try something, look at it, adjust it and try again until something starts to feel right.

Photography, and especially recording video, has long felt too cumbersome for me. Positioning cameras, collecting files, sorting takes, getting an overview of the footage... All of that created enough friction that I often gave up before it really started. I need the fast iteration loop I get when editing on a PC. If getting footage from a smartphone, camera or SD card already feels like work, I often abort the process or grudgingly accept the footage I already have.



## Harvesting from the video nodes

Distributed recordings are useful, but editing starts once everything is in one place. We need to get the footage from the camera nodes and put them on the host PC conveniently. Therefore, we use the `harvest` command which will fetch the recorded videos from the camera nodes and gather them on our host PC.

```bash
$ multicam --nodes examples/nodes.yml harvest \
    --session hello_world_01 \
    --output ./harvested_sessions

harvest session=hello_world_01 status=complete output=harvested_sessions/hello_world_01

NODE       CAMERA  STATUS    COPIED  UNCHANGED  CONFLICTS  MISSING  ERRORS
---------  ------  --------  ------  ---------  ---------  -------  ------
cam-front  front   complete      18          0          0        0       0
cam-side   side    complete      18          0          0        0       0
cam-top    top     complete      18          0          0        0       0

Index:  harvested_sessions/hello_world_01/session_index.json
Report: harvested_sessions/hello_world_01/harvest_report.json
```

Now we have all the videos in one place and can start editing them. The last time I did video editing was in school using Windows Movie Maker. Because I'm a Linux user now and have learned to look for advice on the internet, I decided it would be a good idea to learn how professionals approach editing today. Turns out they start with getting an overview of the recorded footage first.

## Getting an Overview with the multicam stringout

While building `Multivid`, I learned a lot of new terms like "stringout". If you have a lot of takes and recordings and especially if you multiply all of this by using different camera angles, you need an efficient way of screening the vast amount of material. To no surprise, there are practices and techniques used in professional video editing. We adapt one of them and derive a so-called stringout video from all the individual videos. We just take the different angles, arrange them side by side like on a surveillance camera stream and speed things up a bit because we don't need details at the moment but a quick overview. For convenience, we add some labels to know which camera node is where, what take is currently shown and the original time (before the speed-up) so we can easily note interesting situations and find them in the original footage.

Now we can easily digest the data and get a feeling which camera angles work, if some parts look particularly good from a specific angle or if something is boring (even when sped up).

If we experiment and e.g. took multiple takes, we can use the stringout to quickly decide which of them to mark for later use and which to discard.

Were all cameras running? Was framing okay? Was focus okay? Which angle is useful? Is the take worth editing?

So let's create a sped-up stringout video from our harvested videos:

```bash
$ multicam derive-stringout \
    --session-path ./harvested_sessions/hello_world_01 \
    --speed 5 \
    --overwrite

stringout session=hello_world_01 status=complete \
output=./harvested_sessions/hello_world_01/derivatives/review/multicam_stringout.mp4

TAKE      STATUS    CAMERAS         MISSING  DURATION  WARNINGS
--------  --------  --------------  -------  --------  --------
take_001  included  front,side,top           26.90s    0
take_002  included  front,side,top           29.63s    0
take_003  included  front,side,top           640.68s   0
take_004  included  front,side,top           28.59s    0
take_005  included  front,side,top           26.48s    0

Report:           ./derivatives/review/multicam_stringout_report.json
FFmpeg commands:  ./derivatives/review/ffmpeg_commands.txt
Per-take outputs: 5
```

Here is the result: all takes, all camera angles, sped up and labeled with the original time so I can quickly decide and note what is usable.

<div class="ratio ratio-16x9">
  <iframe
    src="https://www.youtube-nocookie.com/embed/npR1wyZ3KEA"
    title="Multivid stringout demo"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
</div>

**Take01**: (staged) positioning of the Benchy

**Take02**: ~~record scan session~~ add LAN cable

**Take03**: actual scanning the Benchy

**Take04**: done, lights out!

**Take05**: wait... let's try how it looks with only the scanner light on?

What we can see immediately: Take 1 needs a tighter cut, so it looks like I am placing the Benchy rather than removing and placing it again.

We can also see that not every angle is equally useful. The side perspective is mostly self-occluding and therefore not very interesting for this setup. But it revealed another issue: the 3D-printed backplate is important for structural integrity. This scanner did not have it installed, and the resulting skew is visible in the footage.

## Editing and final video

Now let's actually create a useful video out of our footage! I used Kdenlive for this and chose to keep it simple and use just simple effects like Picture in Picture views and sped up the middle scanning routine part which would otherwise be about ten minutes long.

You can watch the video here. It is not perfect, but that was not the goal of this devlog anyway:
<div class="ratio ratio-16x9">
  <iframe
    src="https://www.youtube-nocookie.com/embed/aFC8JsfM1XI"
    title="Multivid Devlog 2 demo cut"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
</div>

Editing was a bit of a hassle because I didn't know Kdenlive before, but because I already had a vague idea and notes from the stringout and enough material, I could focus on learning the basics of Kdenlive. This was actually fun because I didn't need to figure out a new user interface and reason about which parts to show when at the same time. Learning things is fun if you have the material and tools at hand, and the workflow felt exactly like this and was quite enjoyable.

## And now?

Things I want to add next:

- a hardware interface with buttons for starting/stopping recordings.[^clap]
- OpenScan3 integration so we can compare scanning metadata and timelines with our recordings, start the recording once we start a scan and maybe create video renderings of the reconstructed 3d models
- a generic clip factory that produces: timelapses, vertical candidates, cutaways, thumbnails.

I believe that it will be very helpful to use the Multivid prototype as a kind of workflow documentation. When we include surface preparation, scan settings and the final results, we create a very useful resource for anyone who wants to get into scanning.

<!-- markdownlint-capture -->
<!-- markdownlint-disable -->
> **Support Note.** If you also think that documenting and openly sharing scanning workflows under Creative Commons licenses is valuable, you can support OpenScan by [sponsoring us on Patreon](https://www.patreon.com/OpenScan) or by sharing this post. It helps us maintain and document the OpenScan project and open-source tools like [`Multivid` on GitHub](https://github.com/esto-openscan/multivid).
{: .prompt-tip }
<!-- markdownlint-restore -->

## Footnotes

[^perspective]: I have a decent theoretical 3D intuition, but I struggle with colorful or picturesque mental images. I usually think in abstract concepts rather than finished pictures.

[^benchy]: The OpenScan Benchy is used in a public scanner workflow benchmark and comparison. You can learn more about this in the [GitHub repository](https://github.com/OpenScanEu/OpenScanBenchy) or on our blog [here](https://blog.openscan.eu/posts/openscan-benchy-3d-scanning-benchmark/).

[^clap]: Or maybe control it with a clap? Would be way cooler, but I'm not sure if it works in our workshop because of the noise and ambient sounds.
