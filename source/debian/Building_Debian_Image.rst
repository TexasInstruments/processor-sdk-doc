====================================
Building Debian Images Using Armbian
====================================

Introduction
============

Texas Instruments uses the **Armbian** build framework to generate Debian images for its platforms.
*Armbian* describes itself to be a "base operating system"; that is, a build framework used to build
Linux images optimized for Single-Board Computers.

|__SDK_DOWNLOAD_URL__| provides Debian images, but users can also build these, especially if users
require something custom (such as different kernel configurations or default desktop environments).

Armbian Usage
=============

This document provides high-level information about how to build Debian images for TI platforms,
using Armbian. For a full list of options available for users to configure these images at build
time, see `Armbian Documentation <https://docs.armbian.com/>`__.

Get Armbian
-----------

For the time being, TI's fork of Armbian maintains support for TI platforms. Therefore, the first
step is to fetch TI's fork:

.. code-block:: console

   git clone https://github.com/TexasInstruments/armbian-build.git

Repository Structure
--------------------

There are 4 files and directories of relevance to this high-level overview:

- :file:`configs/`: This directory has configurations for boards, families, kernel configurations,
  desktop or CLI environments and so on. To find configuration files relevant to TI, see:

   - :file:`configs/sources/families/k3.conf`
   - :file:`configs/kernel/linux-k3-current.conf`
   - :file:`configs/kernel/linux-k3-rt-current.conf`

- :file:`compile.sh`: This is the script that the user should run for building Armbian images.

- :file:`lib/`: This directory stores the scripts that do most of the work in building Armbian images.

- :file:`extensions/`: This directory has files that define **extension hooks**. In Armbian, *extension
  hooks* are function signatures, which the build framework calls in the process of building an
  image. However, the build framework does not define these in ``lib/``. Users can define these
  functions and integrate custom steps in the build process. TI has ``extensions/ti-debpkgs.sh``
  extension file. To customize the build process, create a new file in this directory, and define
  your extension hooks there. Once the file is created, be sure to add the following line to
  board/family config file:

   .. code-block:: console

      enable_extension <extension_name>

- :file:`userpatches/`: This directory stores files that define build parameters, user patches and so on.

Building Images
---------------

Armbian supports an interactive build process. To build interactively, go to TI's Armbian fork you
cloned, and use the following command:

.. code-block:: console

   ./compile.sh

The build framework will then display dialog boxes. The user can use this to select the board, CLI
or desktop environment, kernel configurations and so on.

To build the image non-interactively, specify all required **Build Switches** in the command:

.. code-block:: console

   ./compile.sh [command] [switch...] [command...]

A full list of build switches is available at `Build Switches <https://docs.armbian.com/Developer-Guide_Build-Switches/>`__.

For example, the following command builds the minimal non-RT Trixie image:

.. code-block:: console

   ./compile.sh build BOARD=<target> BRANCH=current BUILD_MINIMAL=yes KERNEL_CONFIGURE=no RELEASE=trixie SKIP_ARMBIAN_REPO=yes

For a list of targets corresponding to each board, refer:

      +------------------------------+--------------+
      | Board                        | Target       |
      +==============================+==============+
      | AM62P                        | sk-am62p     |
      +------------------------------+--------------+
      | AM62x                        | sk-am62b     |
      +------------------------------+--------------+
      | AM62-LP                      | sk-am62-lp   |
      +------------------------------+--------------+
      | AM62SIP                      | sk-am62-sip  |
      +------------------------------+--------------+
      | AM64x                        | sk-am64b     |
      +------------------------------+--------------+


``output/images/`` stores the built images. These images have a ``.img`` extension.
