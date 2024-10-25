# psdk-doc-docker

A simple docker container to build
[processor-sdk-doc](https://github.com/TexasInstruments/processor-sdk-doc).


## Why

Preempting incompatibility as that repos is still using some deprecated sphinx
calls. Sphinx has some dependency resolution issues when mixing system and local
python library installations that causes unusual artifacts. This guarantees a
reproducible build output.


## Building

You need podman or docker for building. If either one of those is already
installed then just run `make`.


## Usage

New tooling has unified the invocation of Podman and Docker by fetching the
owner of the build directory and remapping an internal user to satisfy build
requirements. It will fail if the directory owner is in a reserved uid/gid
region.

After starting the container with your preferred container tool, follow the
instructions for building the documentation as usual.

```bash
docker run -it --rm -v "$PWD":/build ghcr.io/texasinstruments/processor-sdk-doc
```
