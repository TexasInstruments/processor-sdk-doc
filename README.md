# Processor software development kit documentation

This repository holds the documentation for the Texas Instruments Processor
Software Development Kit (PSDK). It currently uses Sphinx and reStructuredText.
There are some light plugins and a custom configuration tool to handle platform
specific values.

## Build guide

If you know what you are doing and just need a command:

```
docker run -it --rm -v "$PWD":/build ghcr.io/texasinstruments/processor-sdk-doc:latest make DEVFAMILY=AM62X OS=linux
```

If you have any questions about the preceding command, see the following
sections.

### Clone the repository

```
git clone https://github.com/TexasInstruments/processor-sdk-doc.git
```

### Start the container

A lightweight container with all required dependencies is available on the
GitHub container registry. The source code to build this container is available
under the [`docker/`](docker/) subdirectory.

To start the container, issue the following at the root of the project.

```
docker run -it --rm -v "$PWD":/build ghcr.io/texasinstruments/processor-sdk-doc:latest
```

### Issue make

GNU Make handles some initial configuration. Specify the `DEVFAMILY` and `OS`
values as either arguments to `make` or as environment variables before
execution of `make`.

`DEVFAMILY` represents the Device Family. Possible values correspond to the
names of directories listed under [`configs/`](configs/). For example:

   - "AM335X" (representing AM335X family)
   - "AM437X" (representing AM437X family)
   - "AM57X" (representing AM57X family)
   - "AM64X" (representing AM64X family)
   - "AM62X" (representing AM62X family)
   - "AM62AX" (representing AM62AX family)
   - "AM62PX" (representing AM62PX family)
   - "AM62LX" (representing AM62L family)
   - "AM62DX" (representing AM62D family)
   - "AM65X" (representing AM65X family)
   - "DRA821A" (representing DRA821A)
   - "J721E" (representing Jacinto 7 ES)
   - "J7200" (representing Jacinto 7 VCL)
   - "J721S2" (representing Jacinto 7 AEP)
   - "J784S4" (representing Jacinto 7 AHP)
   - "J722S" (representing Jacinto 7 AEN)

`OS` represents the operating system. Possible values correspond to the second
parameter of files listed under the `configs/<DEVFAMILY>/` directory. For
example `AM57X_linux_toc.txt` means that `linux` is a valid `OS` value.

Example build commands:

   - Build Linux documentation for AM335X
     ```
     make DEVFAMILY=AM335X OS=linux
     ```
   - Build Android documentation for AM62X
     ```
     make DEVFAMILY=AM62X OS=android
     ```
   - Build Debian documentation for AM62PX
     ```
     make DEVFAMILY=AM62PX OS=debian
     ```
   - Build EdgeAI documentation for AM62AX
     ```
     make DEVFAMILY=AM62AX OS=edgeai
     ```

### Document output

Currently only HTML output is possible. The output is available in directories
matching the following structure on a successful build:

```
./build/processor-sdk-<OS>-<DEVFAMILY>/esd/docs/<VERSION>/index.html
```

## Contributing

See the [contribution guidelines](CONTRIBUTING.md) for information about
formatting guidelines, workflows, and common issues.

## Development previews through GitHub Pages

GitHub Pages are now live for all `DEVFAMILY` and `OS` supported by this
repository. This means that the current `master` branch build is available on
GitHub Pages.

You can access the latest bleeding-edge documentation at the following link:

https://texasinstruments.github.io/processor-sdk-doc/

Please treat the GitHub Pages deployment as the most up-to-date source of
documentation.
