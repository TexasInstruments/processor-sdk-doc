########
Overview
########

Debian, also known as Debian GNU/Linux, is a Linux distribution composed of free and open source
software. Community-supported Debian Project develops and maintains it. It offers a vast repository
of software packages, which the ``apt`` package manager can install.

TI creates Debian images by using the popular project called **Armbian**. Armbian is a highly-optimized
**base operating system** (i.e. an extensive build framework) for building Debian-based images for
Single-Board Computers. Unlike other tools, such as mmdebstrap and bdebstrap, which are often
used for creating Debian images, Armbian focuses on creating images for Single-Board Computers.

A few key highlights of this project are:

-  The Debian filesystem image requires standard packages from debian.org and TI's additional packages as
   ``.deb`` packages. TI's package build infrastructure uses public sources of git repositories to build
   deb packages. TI's official repository maintained on `Github/TexasInstruments/ti-debpkgs
   <https://github.com/TexasInstruments/ti-debpkgs>`__ hosts these packages.

-  This document also provides the required steps and instructions to customize the TI's components
   for |__PART_FAMILY_DEVICE_NAMES__| System-on-a-Chip (SoC) and create the corresponding deb packages.

-  The entire project is public and we accept community contributions as pull requests to GitHub
   repositories.

Debian vs Yocto
===============

TI provides both Debian and OpenEmbedded/Yocto based images as their Linux offering. Here's a quick
comparison between both to decide the one to start with:

Comparison
----------

+-------------------+--------------------------------------+---------------------------------------+
|  **File System**  |              **Debian**              |    **OpenEmbedded/Yocto (Arago)**     |
+-------------------+--------------------------------------+---------------------------------------+
| Build Time        | Fast since all the packages are      | All the packages are built from       |
|                   | downloaded as deb packages and       | source. so build time is high.        |
|                   | installed.                           |                                       |
+-------------------+--------------------------------------+---------------------------------------+
| Patching SW Stack | Difficult because all components are | Since all the components are built    |
|                   | installed as deb packages.           | from sources, patches can be applied  |
|                   |                                      | using yocto recipes.                  |
+-------------------+--------------------------------------+---------------------------------------+
| Host Hardware     | Less because every component is      | High because building all the         |
| Requirements      | downloaded except for bootloader.    | software stack takes so much storage  |
|                   |                                      | space and computing power.            |
+-------------------+--------------------------------------+---------------------------------------+
| Installing new    | Since there is a package manager,    | Since there is no package manager,    |
| packages on the   | installing packages is as simple as  | packages has to be built using yocto  |
| target            | running ``apt install <package>``.   | or cross-compiled, and then copied to |
|                   |                                      | the RootFS.                           |
+-------------------+--------------------------------------+---------------------------------------+


Acknowledgements
================

-  `armbian/build <https://github.com/armbian/build/>`__
-  `TI/armbian-build <https://github.com/TexasInstruments/armbian-build>`__
-  `beagleboard/repos-arm64 <https://git.beagleboard.org/beagleboard/repos-arm64>`__


.. _technical-support:

Technical Support
=================

Technical support is a broad term. Our desire is to provide a solid
product, good documentation, and useful training that defines a clear
path for developing a product based on the Linux/Debian/RTOS/Android SDKs.
However, we know we'll never cover everything that can be done, and
occasionally we even make mistakes <gasp>. So, when you can't seem to
find what you need, there's a good place to search through previously
answered questions or ask a new one:
the `E2E Support Forums <https://e2e.ti.com/support/processors/>`__.

The E2E Support Forums is an active community of TIers and other customers
like you already using a TI Processor. You may find your question has already
been answered with a quick Search of the Forums. If not, a quick post will
likely provide you the answers you need.
