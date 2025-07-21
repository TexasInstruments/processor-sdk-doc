Processor SDK Documentation in Sphinx
=====================================

## Instructions to build the project on Ubuntu

### Clone the Git Repo

    $ git clone https://github.com/TexasInstruments/processor-sdk-doc.git

### Install tools on Ubuntu

Use the following command in a python virtual environment for a known working
config:

    $ cd processor-sdk-doc
    $ python3 -m pip install -r requirements.txt

> [!WARNING]
> This is supported using Python v3.12+. If using an older Python version, some package versions in `requirements.txt` may not be compatible, possibly due to an older
> bundled `pip` version.

OR you can use a docker container like the following:
    - [psdk-doc-docker](https://github.com/TexasInstruments/processor-sdk-doc/pkgs/container/processor-sdk-doc)

### Build on Ubuntu

To build the documentation a DEVFAMILY and OS must be specified as either an
argument to `make` or set as environment variables prior to execution of `make`.

DEVFAMILY represents the Device Family. Possible values correspond to the names
of directories listed under `configs/`. For example:

 * "AM335X" (representing AM335X family)
 * "AM437X" (representing AM437X family)
 * "AM57X" (representing AM57X family)
 * "AM64X" (representing AM64X family)
 * "AM62X" (representing AM62X family)
 * "AM62AX" (representing AM62AX family)
 * "AM62PX" (representing AM62PX family)
 * "AM62LX" (representing AM62L family)
 * "AM62DX" (representing AM62D family)
 * "AM65X" (representing AM65X family)
 * "DRA821A" (representing DRA821A)
 * "J721E" (representing Jacinto 7 ES)
 * "J7200" (representing Jacinto 7 VCL)
 * "J721S2" (representing Jacinto 7 AEP)
 * "J784S4" (representing Jacinto 7 AHP)
 * "J722S" (representing Jacinto 7 AEN)
 * "GEN" (representing General family not listed above)
 * "CORESDK" (representing CORESDK)

OS represents the operating system. Possible values correspond to the second
parameter of files listed under the `configs/<DEVFAMILY>/` directory. For
example `AM57X_linux_toc.txt` means that `linux` is a valid OS value.

Example build commands:

 - Build linux documentation for AM335X

       $ make DEVFAMILY=AM335X OS=linux

 - Build android documentation for AM62X

       $ make DEVFAMILY=AM62X OS=android

 - Build debian documentation for AM62PX

       $ make DEVFAMILY=AM62PX OS=debian

 - Build EdgeAI documentation for AM62AX

       $ make DEVFAMILY=AM62AX OS=edgeai

### HTML Page Output

Open the index page in a web browser

    linux:   ./build/processor-sdk-linux-<FAMILY>/esd/docs/[version]/index.html
    android: ./build/processor-sdk-android-<FAMILY>/esd/docs/[version]/index.html
    debian:  ./build/processor-sdk-debian-<FAMILY>/esd/docs/[version]/index.html
    edgeai:  ./build/processor-sdk-edgeai-<FAMILY>/esd/docs/[version]/index.html

## Contributing

See the [contribution guidelines](CONTRIBUTING.md) for information about
formatting guidelines, workflows, and common issues.

## Live Preview on GitHub Pages

GitHub Pages are now live for all `DEVFAMILY` and `OS` supported by this repository.
This means that for every pull request merged into the master branch, an equivalent
preview will be available on GitHub Pages immediately.

You can access the latest bleeding-edge documentation at the following link:
    - [Processor SDK Documentation](https://texasinstruments.github.io/processor-sdk-doc/)

Please treat GitHub Pages as the most up-to-date source of documentation.
