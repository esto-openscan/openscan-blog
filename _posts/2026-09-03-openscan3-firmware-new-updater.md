---
title: "OpenScan3 Firmware: The New Updater"
date: "2026-09-03T00:00:00+02:00"
author: "Elias Stognienko"
description: "A new apt-based updater makes OpenScan3 easier to update, recover and maintain, while providing a much better foundation for custom setups and future development."
categories:
  - "Firmware"
tags:
  - "openscan3"
  - "firmware"
  - "updater"
image:
  path: "/assets/img/posts/2026-09-03-openscan3-firmware-new-updater/os3-new-updater.png"
  alt: "OpenScan3 firmware updater"
---


With release v0.12.0, we introduced a new update system. I want to briefly explain how it works.


## Why OpenScan3 needed a better update mechanism
In the past, the update procedure was baked into the image and could not be changed easily. This resulted in the need for occasional reflashes. In addition, the operating system would not receive updates at all, which is unacceptable from a security perspective.

## How it works now
The new update mechanism is based on apt. Essentially, we're building `.deb` packages from the OpenScan3 source code and distribute via our own apt repository.

Updating your scanner now means a complete Raspberry Pi OS update including the OpenScan3 packages[^apt]. We made sure to pin (and even mirror) essential dependencies for the camera stack to ensure the functionality between updates. The camera stack dependencies will be gradually updated after thoroughly testing compatibility.

The updater is now cleanly integrated into the frontend and the firmware API. Right now, you can see the installed and available version of OpenScan packages and if system package updates are available. 
The frontend page will be improved in the future with changelogs of the new releases, so you can decide whether you want to update or keep your current version. Updates won't happen automatically; it is always up to you to decide if and when you want to update.

## Update Channels
We now have two OpenScan update channels: **stable** and **nightly**. The standard image (without develop in its name) follows the stable channel. The stable releases are created manually after a testing period. The stable channel is recommended for productive use.

In contrast, the nightly channel is built automatically directly from the develop branch, thus encompassing the latest changes. The downside is that features can still be experimental or even broken until a fix is pushed to the develop branch. Usually, this tradeoff is not acceptable for most users and you should only switch to nightly if you accept the risks of breaking the system. However, if you want to use the latest features as soon as possible or want to help testing, the nightly channel is a great way to contribute! Develop images are set to the nightly channel by default.

## Security
The new update system improved security significantly. We cryptographically sign our apt repository metadata using a hardware key. Your scanner only accepts packages whose integrity can be verified through the trusted Debian, Raspberry Pi or OpenScan repositories.

The nightly repository uses a software-managed signing key and is therefore less well-protected than the stable repository. Though we thoroughly read every PR before we merge, we can't rule out that the automatic build process will never be compromised, and because we build automatically, the nightly signing key is at greater risk than our stable keys. Therefore, we strongly recommend you to stick to the stable channel.

## Recovery
Things can go wrong and your scanner is now better prepared for this.
If an update is interrupted or the normal firmware interface becomes unavailable, the recovery page at `$hostname/recovery/` remains available through a minimal local webservice. Here you can repair OpenScan3, which basically reinstalls the latest packages including the camera stack.

## Advanced usage
The new OpenScan3-as-Debian-package architecture allows you to install OpenScan3 on your own images or make deeper modifications to suit your needs.
 Essentially, you could use a standard Raspberry Pi OS image, add our apt repository, install the OpenScan packages and should have a working scanner!

This provides much more flexibility and enables you to use only specific parts of OpenScan3. For example, you could build your own scanner without the frontend and use only the API for your own scripts or dashboard.


<!-- markdownlint-capture -->
<!-- markdownlint-disable -->
> **Support Note.** If you value an internet-connected scanner that has the latest security patches and is still easily customizable, you can support OpenScan by [sponsoring us on Patreon](https://www.patreon.com/OpenScan). It helps us maintain the less glamorous parts of the project so, ideally, nothing exciting happens besides you having an up-to-date device.
{: .prompt-tip }
<!-- markdownlint-restore -->

## Footnotes

[^apt]: Technically, it's running `apt full-upgrade`, which may update kernel, bootloader and can replace packages. If you build something custom on top of OpenScan3 images, consider pinning your dependencies.
