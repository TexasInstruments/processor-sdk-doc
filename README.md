# Processor SDK documentation

This is the documentation for the Texas Instruments Processor Software
Development Kit (PSDK). It uses Sphinx and reStructuredText. There are some
light plugins and a custom configuration tool to handle device specific values.

## Build guide

Continue reading if you have any questions about the following command.

```
docker run -it --rm -v "$PWD":/build ghcr.io/texasinstruments/processor-sdk-doc:latest make DEVFAMILY=AM62X OS=linux
```

### Clone the repository

```
git clone https://github.com/TexasInstruments/processor-sdk-doc.git
```

### Start the container

A small container with all required tools is available on the GitHub. The source
is in the [`docker/`](docker/) subdirectory.

To start the container, issue the following at the root of the project.

```
docker run -it --rm -v "$PWD":/build ghcr.io/texasinstruments/processor-sdk-doc:latest
```

### Issue make

GNU Make handles some initial setup. Specify the `DEVFAMILY` and `OS` values as
either arguments to `make` or as environment variables.

`DEVFAMILY` stands for the Device Family. Possible values correspond to the
names of directories listed under [`configs/`](configs/).

`OS` stands for the operating system. Possible values correspond to the second
part of files listed under the `configs/<DEVFAMILY>/` directory. For example
`AM57X_linux_toc.txt` means that `linux` is a valid `OS` value.

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

Currently only HTML output is supported. The output is available in directories
matching the following template on a successful build:

```
./build/processor-sdk-<OS>-<DEVFAMILY>/esd/docs/<VERSION>/index.html
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for information about formatting,
workflows, and common issues.

## Development previews through GitHub Pages

GitHub Pages are now live for all `DEVFAMILY` and `OS` supported by this
project. This means that the current `master` build is on GitHub
Pages at the following link.

https://texasinstruments.github.io/processor-sdk-doc/
