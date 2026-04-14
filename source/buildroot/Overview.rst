########
Overview
########

Buildroot is an open-source, simple, and efficient tool for building complete
Linux systems for embedded devices. It automates the process of generating
cross-compiled toolchains, root filesystems, Linux kernels, and bootloaders.
Buildroot is highly customizable, allowing developers to tailor their Linux
environment to meet the specific needs of their embedded projects.


**************************************
Buildroot Architecture for TI Devices
**************************************

The diagram below shows the Buildroot-based Linux embedded software distribution main components for TI devices.

The open-source Linux\ :sup:`®` distribution, based on the Buildroot build system, running on the Arm\ :sup:`®` Cortex\ :sup:`®`\-A processors, includes:

- **TI BSP Components** — the Texas Instruments Board Support Package, comprising:

  - The boot chain based on **TF-A** (Trusted Firmware-A) and **U-Boot**.
  - The secure monitor based on **TF-A** and **OP-TEE**, running on the Arm\ :sup:`®`
    Cortex\ :sup:`®`\-A in secure mode.
  - The **OP-TEE** secure OS running on the Arm\ :sup:`®` Cortex\ :sup:`®`\-A in secure mode,
    providing a Trusted Execution Environment (TEE) for Trusted Applications.
  - The **Linux Kernel** and **TI Kernel Drivers** running on the Arm\ :sup:`®`
    Cortex\ :sup:`®`\-A in non-secure mode, along with board-specific **Device Trees**.
  - The **TI Linux Firmware** providing co-processor firmwares
    (not applicable for AM62Lx-EVM).

- **Buildroot Build System** — consisting of:

  - **Buildroot Core**: the upstream Buildroot framework that drives the entire build.
  - **Buildroot External-TI**: the TI-specific external tree
    (`buildroot-external-TI <https://github.com/TexasInstruments/buildroot-external-TI>`__)
    that adds TI board configurations, packages, and patches without modifying upstream Buildroot.

- **Applications** — the user-space software layer built on top of the BSP, including
  GUI applications, custom applications, Trusted Applications running under OP-TEE,
  and middleware and libraries.

- **Build Artifacts** — the outputs produced by the Buildroot build system: an SD card
  image, individual boot artifacts, and a root filesystem.

.. note::

   Each component in the diagram below is a **clickable hyperlink** that navigates
   directly to the corresponding source repository or documentation.

.. graphviz:: ../graphviz/Buildroot_architecture.gv
   :caption: Buildroot-based Linux Architecture for TI Devices

*************************
Key Features of Buildroot
*************************

#. **Simplicity**:
    Buildroot is designed to be easy to use and understand, making it
    accessible for developers with varying levels of experience in embedded
    systems.
#. **Customization**:
    With a vast library of packages and a flexible configuration system,
    Buildroot allows for extensive customization of the target system.
#. **Efficiency**:
    Buildroot’s minimalistic approach ensures that the generated system is lean
    and efficient, which is critical for resource-constrained embedded
    environments.
#. **Active Community**:
    A vibrant community of developers continually maintains and enhances
    Buildroot, providing regular updates and support.

***********************
Buildroot External Tree
***********************

TI provides a Buildroot external tree `Github/TexasInstruments <https://github.com/TexasInstruments/buildroot-external-TI>`__.
, to incorporate TI specific configurations and packages. This external
tree allows to customize and extend the Buildroot environment without modifying
the original Buildroot source code. It serves as a centralized repository for
custom configurations, ensuring consistency and ease of maintenance. The entire
project is made public and we accept community contributions as pull requests
to github repository.

Repository structure
====================

.. code-block:: text

   buildroot-external-TI
   ├── external.desc
   ├── external.mk
   ├── Config.in
   ├── board
   │   ├── ti
   │   │   ├── am62x-sk
   │   │   ├── am62lx-evm
   │   │   ├── common
   ├── COPYING
   ├── README.md
   ├── configs
   │   ├─ ti_release_am62x_sk_defconfig
   │   ├─ ti_release_am62x_sk_rt_defconfig
   │   ├─ ti_release_am62lx_evm_defconfig
   │   ├─ ti_release_am62lx_evm_rt_defconfig
   ├── package

:file:`external.desc`: contains name and description of br2-external tree.

:file:`configs/`: contains board specific configurtion files.

:file:`board/`: contains board specific files patches, genimage configuraion and hash file.

:file:`external.mk`: used to define package recipes.

:file:`Config.in`: used to define package recipes.

:file:`package`: used to add package.

.. _technical-support:

*****************
Technical Support
*****************

Technical support is a broad term. Our desire is to provide a solid
product, good documentation, and useful training that defines a clear
path for developing a product based on the Linux/Debian/Buildroot/RTOS/Android
SDKs. However, we know we'll never cover everything that can be done, and
occasionally we even make mistakes <gasp>. So, when you can't seem to
find what you need, there's a good place to search through previously
answered questions and ask a new one - The E2E Support Forums.

There is an active community of TIers and other customers like you
already using a TI Processor, on these forums. You may find your
question has already been answered with a quick Search of the Forums. If
not, a quick post will likely provide you the answers you need.

-  `E2E Processor Support
   <https://e2e.ti.com/support/processors/>`__
