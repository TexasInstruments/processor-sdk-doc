###############
SGX build guide
###############

The graphics stack on SGX will not receive any new major updates. The last major
change occurred in release 09.01. This will capture the build process and some
of the caveats of this legacy driver.

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
despite the mention of kernel 6.1 it is also interoperable with kernel 6.6 and
6.12.

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
``WINDOW_SYSTEM=lws-generic``. The UM section will go previous exceptions
to this.

*************************
SGX user space components
*************************

The proprietary user space components are necessary for all interactions with
the GPU. It has the firmware, GLES implementation, and the primary control
server. Unlike rogue, the firmware part of the control sever library.

The binary release is available at:

   https://git.ti.com/cgit/graphics/omap5-sgx-ddk-um-linux

Installing the SGX user space components
========================================

The repository has binaries for each platform in release specific branches. The
newest release, which matches with the earlier mentioned kernel module branch is
``1.17.4948957/mesa/glibc-2.35``. This branch deviates from the existing naming
pattern to indicate that unlike previous releases it required a new version of
mesa and was linked against glibc-2.35.

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
everything from a DRI "megadriver" to full GLES/GL implementations. If you're
interested in learning GFX under Linux it is worth familiarizing yourself with
everything else it provides.

For us, the important part is that DRI "megadriver." This is the mechanism used
to decide what GLES / GL implementation gets selected when you bind one of the
before mentioned API to a context. This is also where things get tricky.

Historically there has been some issues with embedded GFX because, unlike your
standard PC GPU, we tend to mix and match actual Graphics Processing Units and
Display Controllers. The megadriver uses the display device name to coordinate
between API implementations. As such, we need a shim to act as a DRI driver and
coordinate the link with the SGX GLES implementation.

This shim, currently, is in the form of a Gallium Frontend. This is the main
reason for the fork and the 60 odd patches we carry at the following repository:

   https://gitlab.freedesktop.org/StaticRocket/mesa

There are also other nice-to-have features there such as additional pixel
formats, minor fix-ups, and a few performance tweaks IMG have picked up over the
years. The main reason we need it is for that shim.

Building the SGX mesa components
================================

We recommend following the `Mesa build guide`_ for general options. Currently
the mesa components use a standard interface that allows use of any
``powervr/*`` branch equal to or greater than ``22.3.5``.

The only necessary build options are:

   - ``-Dgallium-drivers=sgx`` -- This is a comma separated list, just make sure
     sgx is present in it.

   - ``-Dgallium-sgx-alias=`` -- This should match the display controller you
     want to bind to. This can either be ``tilcdc``, ``tidss``, or ``omapdrm``
     depending on the device.

This will produce 3 important files relevant to the shim mechanism we discussed
earlier:

   - :file:`sgx_dri.so` -- Main DRI interface

   - :file:`pvr_dri.so` -- GPU interface that points back to :file:`sgx_dri.so`.
     This is for an application that attempts to interact with the GPU directly
     because the DRI device is still registered with the name ``pvr``.

   - :file:`<display>_dri.so` -- Display controller interface that points back
     at :file:`sgx_dri.so`. This is from the value specified with
     ``-Dgallium-sgx-alias``.

*******************
Using the SGX stack
*******************

Assuming you're using the SDK or you've built and installed the preceding
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
:command:`glmark2-es2-drm`. You should see the following indicating you are
using the correct driver:

.. code-block:: console

   root@am335x-evm:~# glmark2-es2-drm
   MESA: info: Loaded libpvr_dri_support.so
   =======================================================
       glmark2 2021.12
   =======================================================
       OpenGL Information
       GL_VENDOR:     Imagination Technologies
       GL_RENDERER:   PowerVR SGX 530
       GL_VERSION:    OpenGL ES 2.0 build 1.17@4948957
   =======================================================

The ``GL_VENDOR`` should report ``Imagination Technologies`` with the renderer
corresponding to the graphics processor in that device.

.. _Mesa build guide: https://docs.mesa3d.org/install.html

