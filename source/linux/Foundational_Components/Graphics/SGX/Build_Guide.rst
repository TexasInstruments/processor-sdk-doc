###############
SGX build guide
###############

The graphics stack on SGX will not receive any major feature updates. The last
major change occurred in release 12.02.

As part of the kernel 6.1 support effort, this driver now mimics the build and
structure of rogue. The stack consists of 3 main components with varying
classifications:

   - The kernel module (KM) (Open Source, but out-of-tree)
   - The GLES 2.0 user mode (UM) libraries (Closed Source, binary release)
   - The mesa shim (Open Source, but out-of-tree)

All 3 of these components are mandatory for GLES support.

*****************
SGX kernel module
*****************

The kernel module is responsible for:

   - Memory and power management
   - Monitoring device state
   - Orchestrating hardware recoveries
   - Creating an interface for the user space server

The source for this is available at:

   https://git.ti.com/cgit/graphics/omap5-sgx-ddk-linux

Building the SGX kernel module
==============================

The latest branch has the most bug-fixes and has the widest general
compatibility in modern applications. This is ``1.17.4948957/mesa/k6.1``, and
despite the mention of kernel 6.1 it is also interoperable with kernel 6.6,
6.12, and 6.18.

The :file:`INSTALL` file gives a brief overview of how to build and install the
module. This gives you the common variables, but it does omit some of the more
important ones for the build. The following variables are key and *must* match
with the values used in the UM release:

   - ``BUILD`` -- Options: ``release`` or ``debug``
   - ``PVR_BUILD_DIR`` -- Options: ``<platform>_linux``, for example ``ti572x_linux``
   - ``WINDOW_SYSTEM`` -- Options: ``lws-generic``, ``xorg``, ``wayland``, among
     others

These variables are mandatory. To check for updated build variables see the
``EXTRA_OEMAKE`` variable in the `ti-sgx-ddk-km recipe in meta-ti`_. This will
always contain the latest required variables to compile the driver.

.. _ti-sgx-ddk-km recipe in meta-ti: https://git.ti.com/cgit/arago-project/meta-ti/tree/meta-ti-bsp/recipes-bsp/powervr-drivers/ti-sgx-ddk-km_1.17.4948957.bb

As before mentioned these build options must match with the corresponding UM
build options. Currently we only release binaries with ``BUILD=release`` and
``WINDOW_SYSTEM=lws-generic``. The UM section will go over earlier exceptions
to this.

*************************
SGX user space components
*************************

The proprietary user space components are necessary for all interactions with
the GPU. It has the firmware, GLES implementation, and the primary control
server. Unlike rogue, the firmware is part of the control sever library.

The binary release is available at:

   https://git.ti.com/cgit/graphics/omap5-sgx-ddk-um-linux

Installing the SGX user space components
========================================

The repository has binaries for each platform in release specific branches. The
newest release, which matches with the earlier mentioned kernel module branch is
``1.17.4948957/mesa/glibc-2.35``. This branch deviates from the existing naming
pattern to indicate that, unlike other releases, it requires a new version of
mesa and at least glibc-2.35.

The repository has the following structure:

.. code-block:: text

   .
   ├── LICENSE
   ├── Makefile
   ├── README.md
   └── targetfs
       ├── common
       │   ├── 50-pvrsrvctl.rules.template
       │   ├── etc
       │   └── pvrsrvctl.service.template
       ├── ti335x_linux
       │   └── lws-generic
       ├── ti343x_linux
       │   └── lws-generic
       ├── ti437x_linux
       │   └── lws-generic
       ├── ti443x_linux
       │   └── lws-generic
       ├── ti572x_linux
       │   └── lws-generic
       └── ti654x_linux
           └── lws-generic

Under the :file:`targetfs` directory there is a subdirectory for each
``PVR_BUILD_DIR`` build variable. Under that directory is a subdirectory
corresponding to the ``WINDOW_SYSTEM`` build variable. Finally, under that
directory is a subdirectory corresponding to the ``BUILD`` build variable.

This is in the :file:`Makefile` as:

.. code-block:: Makefile

   PRODUCTDIR := ./targetfs/${TARGET_PRODUCT}/${WINDOW_SYSTEM}/${BUILD}

The :file:`Makefile` simply unpacks this directory structure and installs the
corresponding files into ``DESTDIR`` in the install step. Do not worry about the
clean step, as this is for development.

Unlike rogue, there is an additional :file:`common` directory that has
startup script templates. These templates are automatically modified by the
:file:`Makefile` as part of the install step.

These are not strictly required, but you will need to manually start the device
with :command:`pvrsrvctl` if you decide not to use these templates. Please note
that this binary is, and always has been brittle. It likely will not realize
what kernel you are running so you should specify ``--no-module`` when
interacting with it.

*******************
SGX mesa components
*******************

Mesa, at this point in time, is a collection of Graphics (GFX) tools and
utilities for setting up and interacting with rendering contexts. It has
everything from a driver selection system to full GLES/GL implementations. If
you're interested in learning GFX under Linux it is worth familiarizing yourself
with everything else it provides.

With mesa 25.X the legacy DRI interface is no longer present. With this update
``kmsro`` binds displays to their associated drivers. We still need a small shim
to load our GLES implementation and configure the mesa dispatch table.

This shim, currently, is in the form of a gallium driver. This is the main
reason for the fork and the 60 odd patches we carry at the following repository:

   https://github.com/texasInstruments/mesa

There are also other nice-to-have features there such as additional pixel
formats, minor fix-ups, and a few performance tweaks Imagination has picked up
over the years. The main reason we need it is for that shim.

Building the SGX mesa components
================================

In earlier releases the SGX shim was a separate gallium frontend. Starting with
``f52f27edce0e (all: unify sgx and rogue dri layers, 2026-11-12)`` a unified PVR
driver replaces this. This means any older PVR specific mesa branches should
also work, though support is not guaranteed.

We recommend following the `Mesa build guide`_ for general options. Currently
the mesa components use a standard interface that allows the use of any
``powervr/*`` branch. This guide expects a version equal to or greater than
``25.2.8``.

.. note::

   Releases before 1.18 did not use this standard interface. Instead the UM
   binaries include all relevant mesa components for those releases.

The only necessary build options are:

   - ``-Dgallium-drivers=pvr`` -- This is a comma separated list, just make sure
     pvr is present in it.

*******************
Using the SGX stack
*******************

Assuming you're using the SDK or you've built and installed the earlier parts
correctly, you should see a message similar to the following in :command:`dmesg`
after the kernel module loads:

.. code-block:: dmesg

   [   17.344567] [drm] Initialized pvr 1.17.4948957 20110701 for 56000000.gpu on minor 1

If the module loads but does not detect the device, make sure your device tree
has defined the node properly. This corresponds to one of the values of
``powervr_id_table`` in the :file:`services4/srvkm/env/linux/module.c`.

Upon starting the user space daemon you should see the following message:

.. code-block:: dmesg

   [   29.277564] PVR_K: UM DDK-(4948957) and KM DDK-(4948957) match. [ OK ]

You should now be able to issue a simple test. We recommend
:command:`kmscube`. You should see the following indicating you are
using the correct driver:

.. code-block:: console

   root@am335x-evm:~# kmscube
   Using display 0x6564b0 with EGL version 1.4
   ===================================
   EGL information:
     version: "1.4"
     vendor: "Mesa Project"
   [snip]
   ===================================
   OpenGL ES 2.x information:
     version: "OpenGL ES 2.0 build 1.17@4948957"
     shading language version: "OpenGL ES GLSL ES 1.00 build 1.17@4948957"
     vendor: "Imagination Technologies"
     renderer: "PowerVR SGX 530"
   [snip]
   ===================================
   Rendered 120 frames in 2.002120 sec (59.936461 fps)

The vendor should report ``Imagination Technologies`` with the renderer
corresponding to the graphics processor in that device.

.. _Mesa build guide: https://docs.mesa3d.org/install.html

