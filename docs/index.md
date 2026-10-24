# Introduction

Welcome to the home of the LinuxServer.io documentation! It is our goal to ensure that all of our images are properly documented with all of the relevant information, in order to help our users get started. In addition to individual set up guides for each image, there is also general information, and best practices, pertaining to running Docker containers.

!!! warning "This is the v2 playground"

    Everything under `linuxserver-playground` is a proof of concept of the next LinuxServer.io build system. The images it publishes to `ghcr.io/linuxserver-playground/` are **not for production use**. The production images and documentation remain at [linuxserver](https://github.com/linuxserver) and [docs.linuxserver.io](https://docs.linuxserver.io).

## Where things live

The image pages on this site are not written here. Every image repository carries one manifest, `image.yml`; the [hub](https://linuxserver-playground.github.io/hub/) renders the page from it and this site fetches the result at build time. The same manifest produces the README, the store templates, the SWAG proxy confs and the Kubernetes and Podman documents, so the page you read, the template you import and the container you run always describe the same thing. [How a build happens](general/how-a-build-happens.md) walks through the pipeline; [Contributing an image](general/contributing-an-image.md) explains how to change one.

| What | Where |
| :--- | :--- |
| Image pages, by category | [Images by category](images-by-category.md) |
| Fleet data, generated documents, build reports | [Hub](https://linuxserver-playground.github.io/hub/) ([API](API.md)) |
| Live build status, queue, releases | [Control plane](https://ci.thelamer.duckdns.org:8443/) |
| Source | [github.com/linuxserver-playground](https://github.com/linuxserver-playground) |

## Want to get hold of the team?

The team resides primarily in our Discord server. We also have a forum if chat isn't your thing, and the playground has its own GitHub Discussions.

| Where | Link |
| :--- | :--- |
| Discord | [https://linuxserver.io/discord](https://linuxserver.io/discord) |
| Forum | [https://discourse.linuxserver.io](https://discourse.linuxserver.io) |
| Discussions | [https://github.com/orgs/linuxserver-playground/discussions](https://github.com/orgs/linuxserver-playground/discussions) |

Before asking, please read [How to get support](general/how-to-get-support.md) and the [support policy](misc/support-policy.md).
