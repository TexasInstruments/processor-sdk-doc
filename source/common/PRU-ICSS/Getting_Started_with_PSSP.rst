.. _getting_started_with_pssp:

Getting Started with PRU Software Support Package
=================================================

.. rubric:: Overview
   :name: overview-pruss-getting-started

.. note::

 This section covers the software aspects of getting started with a PRU
 Subsystem (PRU-ICSS, PRU_ICSSG, PRU-SS).
 Hardware information, training material, software development
 resources, and more are in the :ref:`pru_subsystem_overview`


The PRU Software Support Package (PSSP) provides support for the PRU
Subsystem in AM335x, AM437x, AM57xx, AM62x, AM64x, and AM65x devices. This package
contains:

-  Support for ARM loading and initializing PRU via Remoteproc Linux driver

   -  Remoteproc supports basic control functions such as firmware load,
      start/halt, simple debug, and interrupt managing

-  Support for communication between ARM and PRU via RPMsg Linux driver
   -  RPMsg supports message passing

-  Basic firmware examples showing simple functionality
-  Register header files for easy register programming
-  Library/API for controlling vrings (used for RPMsg)

.. rubric:: Things to Obtain
   :name: things-to-obtain

-  `Code Composer Studio <https://www.ti.com/tool/CCSTUDIO>`__
-  `PRU Code Generation
   Tools <https://www.ti.com/tool/PRU-CGT>`__
   (you can also get these tools through the CCS App Center)
-  For an ARM running Linux:

   -  Install the Linux Processor SDK for the device.
   -  The PSSP is built into the Linux Processor
      SDK in the '<%SDK_INSTALL_DIR%>/example-applications/pru-icss-x.y.z' folder

-  For an ARM running RTOS:

   -  Install the MCU+ SDK or RTOS SDK for the device.
   -  The `PRU Software Support
      Package <https://git.ti.com/pru-software-support-package/pru-software-support-package/trees/master>`__
      contains header files and register mappings

|

.. rubric:: Installation of Tools
   :name: installation-of-tools

Tools installation paths are generally fairly arbitrary, but we do have
a few requirements once you have installed to your preferred directory.

.. rubric:: Linux

#. Install Processor SDK to the directory of your choosing.
   Follow the installation instructions found at
   :ref:`overview-getting-started`.

#. If your Processor SDK Linux has a top-level example-applications folder, the PRU
   Software Support Package is built into the SDK at
   'example-applications/pru-icss-x.y.z/'. Otherwise you can download the files
   from the public Git repository
   `here <https://git.ti.com/pru-software-support-package/pru-software-support-package/trees/master>`__.

#. (**Optional**) Install CCS to the directory of your choosing
   CCS installation instruction for Linux can be found
   `here <https://software-dl.ti.com/ccs/esd/documents/ccs_linux_host_support.html>`__.
   Makefiles are provided in order to build all examples in the PRU Software Support
   Package. The ability to build the PRU projects using the Makefiles
   makes CCS optional in a Linux environment.

|

.. rubric:: Windows
   :name: windows

#. Download the PRU files from the public Git repository
   `here <https://git.ti.com/pru-software-support-package/pru-software-support-package/trees/master>`__.
#. Install CCS to the directory of your choosing
   Installers can be found
   `here <https://www.ti.com/tool/download/CCSTUDIO>`__.

|

.. rubric:: How to Enable PRU Support in Kernel
   :name: how-to-enable-pru-support-in-kernel

This step is used to enable the remoteproc driver in the Linux kernel.
Windows users that are loading the PRU through CCS can safely skip
this step during the development phase.

Beginning with Linux Processor SDK v2.0.2.11 the remoteproc and rpmsg
modules are enabled by default and included out of the box in the
Linux Processor SDK. Therefore, you do not need to make any menuconfig
changes in order to load firmwares in the PRU cores.

.. rubric:: How to Begin Programming
   :name: how-to-begin-programming

Programming the PRU core is not terribly different from programming any
other core. Because we now have a C compiler we are able to write
regular C code and have it perform tasks on the PRU cores. A great place
to start development is to take a look at the :ref:`pru_getting_started_labs`
and :ref:`pru_hands_on_labs`
that are provided in the PSSP.

.. rubric:: Register Header Files
   :name: register-header-files

Several register header files were created to help facilitate quick and
easy configuration. In Linux, these are located in the
<SDK_install_dir>/example-applications/pru-icss-x.y.z/include
directory by default. In the Git repository these are located in the
include folder. See the :ref:`pru_header_files` page for more information.

|

.. rubric:: Special Considerations
   :name: special-considerations

There are a couple of special CPU registers available with different
functionality.

-  Writes to R30 control the General Purpose Output pins, and reads
   allow the user to determine the current state of those pins
-  R31 is used to read General Purpose Input pins as well as the status
   of the two PRU host interrupts (bits 30 and 31)

   -  Writes to R31 are used to generate interrupts - see the
      device-specific TRM for more information on how these work.

.. rubric:: What Next?
   :name: what-next

For support please post questions on `E2E Processor Support
<https://e2e.ti.com/support/processors/>`__.

