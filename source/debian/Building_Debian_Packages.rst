========================
Building Debian Packages
========================

`debian-repos <https://github.com/TexasInstruments/debian-repos>`__ is a set of scripts to build TI's Debian packages with a single command.

The generation of a Debian package from a binary or source involves many steps such as, obtaining the source code in tar (compressed) format, generating template files, modifying template file. The host build system and host build environment variables should also be configured.

The :file:`run.sh` script handles these steps. Therefore, the building of a deb package for TI's packages is as simple as running :file:`run.sh` with the package's name as a command line argument.

This repository is useful to the following audience:

-  Potential package contributors who want to fix bugs or add enhancements to TI packages.
-  Users who want to create a new package with the latest changes or customizations.
-  Anyone who wants to study Debian packaging.

Structure
=========

The :file:`run.sh` file is the "main" script. It takes as argument the name of the package to build.

Each TI package has a corresponding directory, named after its source package. Within this directory exists the :file:`suite/<distro-variant>/debian/` path. All Debian related files (:file:`control`, :file:`rules`, man pages etc) for the package are located here.

There also exists a :file:`<package-name>/version.sh` file. This file is sourced by :file:`run.sh`.

Setting Up Host for the build
=============================

`debian-repos <https://github.com/TexasInstruments/debian-repos>`__ only supports native compilation of packages. Therefore, the build has to be done either on the ARM64 target or an ARM64 Docker Container.

When running on native ARM64 target, no additional setup is required. Proceed with Building the Package.

To setup and run an ARM64 Docker Container, run the following commands:

.. code-block::

   # Setup Qemu multiarch support
   sudo apt install qemu binfmt-support qemu-user-static
   docker run --rm --privileged multiarch/qemu-user-static --reset -p yes

   # Run ARM64 Container
   docker pull ghcr.io/texasinstruments/debian-arm64:latest
   docker run --rm -it ghcr.io/texasinstruments/debian-arm64:latest bash

Building the Package
====================

#. Clone `debian-repos <https://github.com/TexasInstruments/debian-repos>`__:

   .. code-block::

      git clone https://github.com/TexasInstruments/debian-repos.git
      cd debian-repos

#. Build package:

   .. code-block::

      ./run.sh <package-name>

   .. note::

      This command carries out all the necessary steps to build the package including installation of package-specific dependencies.
      The package and all related files are then stored in :file:`build/<package-name>`.

   For example: to build :file:`ti-linux-kernel`, the command is:

   .. code-block::

      ./run.sh ti-linux-kernel

   The output is then found in :file:`build/ti-linux-kernel/`.

Adding Packages
===============

To add a package, follow the following steps:

#. Create directory structure:

   .. code-block::

      mkdir -p <proj-name>/suite/<distro-variant>/debian/

#. Copy all :file:`debian/` specific files that are relevant to building the package:

   .. code-block::

      cp /path/to/debian/* -r  <proj-name>/suite/<distro-variant>/debian/

#. In :file:`<proj-name>/`, create the :file:`version.sh` file. The file must export the following variables:

   .. code-block::

      git_repo # link from which to clone
