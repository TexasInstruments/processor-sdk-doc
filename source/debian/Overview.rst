########
Overview
########

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   Armbian is a highly-optimized **base operating system** (i.e. an extensive build framework) for building Debian-based images for Single-Board Computers (SBCs).


Debian, also known as Debian GNU/Linux, is a Linux distribution composed of free and open-source software, developed by the community-supported Debian Project.

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   The Linux Debian distribution, built using Armbian, is enabled for TI's AM62Lx platform. Few key highlights of this project are:

.. ifconfig:: CONFIG_part_variant not in ('AM62LX')

   The Linux Debian distribution is enabled for TI's AM62Px, AM62x and AM64x platforms. Few key highlights of this project are:

- The Debian filesystem image requires standard packages from debian.org and TI's customizations as .deb packages. The deb packages for the components owned by TI are built using the public sources hosted on respective git repositories and the deb packages are hosted on TI's official PPA repository maintained on `Github/TexasInstruments <https://github.com/TexasInstruments/ti-debpkgs>`__.

.. ifconfig:: CONFIG_part_variant not in ('AM62LX')

   - The entire Debian build process is made easy with a build script, the script "ti-bdebstrap" is hosted on `TI Debian Github <https://github.com/TexasInstruments/ti-bdebstrap>`__.

- This document also provides the required steps and instructions to customize the TI's components for AM62Lx, AM62Px, AM62x and AM64x SOCs and create the corresponding deb packages.

- The entire project is made public and we accept community contributions as pull requests to github repositories.

.. ifconfig:: CONFIG_part_variant not in ('AM62LX')

   - Github actions are enabled for the buildscripts workflow. So, any change in the config files, package additions or modifications in build scripts will result in auto generation of a new debian filesystem that reflects these changes. The new builds will store the filesystem image as an artifact hosted on the same repo, allowing other users to test the change without making a new build. These images are available via github for 90 days after which they may be purged to save disk space.


Debian vs Yocto
===============

TI provides both Debian and OpenEmbedded/Yocto based images as their Linux offering. Here's a quick comparision between both to let you choose which one to get started with.

Comparision
-----------

+-------------------+--------------------------------------+---------------------------------------+
|  **File System**  |              **Debian**              |    **OpenEmbedded/Yocto (Arago)**     |
+-------------------+--------------------------------------+---------------------------------------+
| Build Time        | Faster since all the packages are    | All the packages are built from       |
|                   | downloaded as deb packages and       | source. so build time is too high.    |
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

    - `beagleboard/image-builder <https://github.com/beagleboard/image-builder.git>`__
    - `beagleboard/repos-arm64 <https://git.beagleboard.org/beagleboard/repos-arm64>`__


.. _technical-support:

Technical Support
=================

Technical support is a broad term. Our desire is to provide a solid
product, good documentation, and useful training that defines a clear
path for developing a product based on the Linux/Debian/RTOS/Android SDKs.
However, we know we'll never cover everything that can be done, and
occasionally we even make mistakes <gasp>. So, when you can't seem to
find what you need, there's a good place to search through previously
answered questions and ask a new one - The E2E Support Forums.

There is an active community of TIers and other customers like you
already using a TI Processor, on these forums. You may find your
question has already been answered with a quick Search of the Forums. If
not, a quick post will likely provide you the answers you need.

-  `E2E Processor Support
   <https://e2e.ti.com/support/processors/>`__

