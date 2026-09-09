---
title: "OpenScan3 Firmware: How to run it from your fork"
date: "2026-09-09T00:00:00+02:00"
author: "Elias Stognienko"
description: "OpenScan3 development images make it straightforward to replace the bundled runtime with your own fork or branch and switch back whenever you want."
categories:
  - "Firmware"
tags:
  - "openscan3"
  - "firmware"
  - "developing"
image:
  path: "/assets/img/posts/2026-09-09-openscan3-firmware-new-dev-tool/os3-git_fork.png"
---


If you ask us, hardware should invite you to experiment with it. You shouldn't have to fight the device before you can even get started modifying it.[^except]
If you want to change how your scanner works, test an idea or build something we never anticipated, running your own version of the firmware should be a normal thing to do. Here, I want to explain what we did to make it as frictionless as possible.

The OpenScan3 development images offer a new way to conveniently use your own fork as scanner firmware replacement. You can now seamlessly switch between the included nightly build runtime and your own git repositories without worrying about systemd units and other pitfalls, which may get in the way when testing and deploying on an OpenScan device.

The so-called *dev helper* is only available to development images and is not included in standard stable images!

## Why use your own repository
### Developing
Having a reliable and reproducible dev environment is key on embedded devices. If you want to contribute, it is a hassle-free way to get to the code immediately without losing an evening to install the toolchain.

Just fork [OpenScan3 on Github](https://github.com/OpenScan-org/OpenScan3) or on your forge of choice, and point your scanner to your repo, and that's it, you can start working on the code.

### Customization
Not all changes make it upstream for many reasons, and this is totally fine. You can keep your OpenScan3 modification in your fork and still get upstream changes when you sync your fork. Beware of occasional merge conflicts, though.

### Experiments
Any kind of tinkering, hacking and experimenting is strongly encouraged. No matter if you want to test new hardware, a new workflow or an idea, just try it and switch back to the included runtime at any time seamlessly. Just one thing to keep in mind: both the included runtime and your fork use the same device config file.

### Privacy
You can even create a private fork of OpenScan3 to use, e.g. if nothing of your workflow customization should be known publicly.

## How to use the `openscan-dev` tool
Note: The latest [valid documentation](https://github.com/esto-openscan/OpenScan3-pi-gen/blob/main/DOCUMENTATION.md#develop-image-git-workflow) is in the OpenScan3-pi-gen repository on Github.

SSH login to a scanner running the development image of OpenScan3 using the default user `openscan:openscan` (consider changing the password) or the user you created while using, e.g. the Raspberry Pi imager.

First, let's check the status of the dev tool:
```bash
$ openscan-dev status
```

results in:
```bash
repo=https://github.com/OpenScan-org/OpenScan3.git
branch=develop
root=/opt/openscan3-dev
override=disabled
checkout=missing
```

As you can see, the dev helper is currently targeted at the develop branch of the official OpenScan3 repository, but it is not active because the standard runtime shipped with the image is still used.

Now I will point the dev helper tool to my GitHub fork and specifically to the feature branch I want to test on a real device:
```bash
$ sudo openscan-dev deploy \
  --repo https://github.com/esto-openscan/OpenScan3.git \
  --branch feature/auto-stack
```

The dev helper now clones this into `/opt/openscan3-dev/src`, checks out the latest commit of the branch and creates a Python virtual venv with the dependencies listed in `pyproject.toml`. This can take a little while.

The dev helper overrides the system services with the ones provided in the repository and restarts the service.

Running the status command again confirms this:
```bash
$ openscan-dev status

repo=https://github.com/esto-openscan/OpenScan3.git
branch=feature/auto-stack
root=/opt/openscan3-dev
override=enabled
checkout=b624475
checkout_branch=feature/auto-stack
```

And indeed: When inspecting the automatically generated Openapi Specs, I can see the new fields I introduced for the new feature I'm building.

For going back to the bundled standard runtime, you can use:
```bash
$ sudo openscan-dev disable
```
This will deactivate the override, but the local git checkout remains in place on the device.

And if you want to use it again, you can enable it anytime:
```bash
$ sudo openscan-dev enable
```

Now, considering that you may not develop on the scanner itself but use another machine, we need a way to get the newest commits to your scanner. There are two options available. The first one will **override local changes on the Pi**, because
```bash
$ sudo openscan-dev deploy
```
will:
1. `git fetch origin <your-branch>`
2. Set the local branch to `FETCH_HEAD`
3. Reset the checkout to the remote state using `reset --hard`
4. Rebuild the virtual environment
5. Restart the `openscan3` service

Alternatively, you can manage the checkout with Git directly. This gives you full control over local changes but also means dealing with conflicts yourself:
```bash
$ sudo -u openscan git -C /opt/openscan3-dev/src pull --ff-only origin develop

# and restart service afterwards:
$ sudo systemctl restart openscan3
```


## Where to go from here
Here is an overview of the [firmware architecture](https://github.com/OpenScan-org/OpenScan3/blob/develop/docs/ARCHITECTURE.md).

The "OpenScan3 Firmware" [blog post series](https://blog.openscan.eu/categories/firmware/) is a good place to learn more on the rationale behind some firmware decisions and is intended as a higher-up overview.

I'm also happy to answer any question, you can reach me at [esto@openscan.eu](mailto:esto@openscan.eu) or on Discord/Reddit/GitHub.

Don't hesitate to share what you build. We'd love to hear anything: great successes or things that didn't work out as expected.


## Footnotes

[^except]: Except, of course, if you like the art of hacking. In this case, we then recommend skipping this blog post entirely so you don't ruin the joy of figuring it out with the dullness of knowing ;) 
