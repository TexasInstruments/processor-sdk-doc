.. _foundational-secure-boot:

**********************************
Secure Boot
**********************************

Introduction
------------

Each device contains customer programmable keys used to authenticate, and optionally decrypt, code/data to be used on the device. A job for
the Public Boot ROM of both General Purpose (GP) and High Security (HS) devices is to load the next stage of the boot process into memory. On
High Security devices, Public ROM also checks the initial boot image for an attached header containing details about the image, including
a signature used to verify the authorship of the image, and optionally encryption information. This header must be attached and the image must
pass authentication for Public Boot ROM to continue boot. It is then the responsibility of the authors to maintain a Chain-of-Trust by ensuring
each next stage is itself authenticated. One weak link and all lower trust levels could be compromised.

.. Note::
    Example: Forgetting to disable u-boot console or environment loading means a non-secured linux can be loaded. The U-Boot console (or command
    line interface (CLI)) and environment are powerful features that make it great for creating a customized boot process. However,
    leaving either or them enabled in a production system allows non-secured software to be loaded and the Chain-of-Trust to be broken.

The following is an example list where Chain-of-Trust should be maintained.

- Remove U-Boot uEnv.txt loading support.
- Disable environment loading (the default built-in environment must be compiled to be the one you want).
- Environment must not fallback to other boot modes.
- Place firewalls in board-config to match the location of loaded artifacts (ATF/OP-TEE).
- Update debug sections of initial image cert.
- Enable DM-verity/DM-crypt.
- Set root password or disable root account.
- Read the OP-TEE porting guide and turn off developer options
- Disable kernel debug options
- Disable/remove userspace debug tools, devmem disable, etc..

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   The U-Boot's Secondary Program Loader (SPL) securely verifies the U-Boot
   proper. U-Boot uses its verified boot framework to do this. U-Boot proper
   then securely verifies and decrypts the kernel, Device Tree Blobs (DTB),
   and initramfs.

   .. Image:: /images/AM62L_KF.png
      :scale: 70%

.. ifconfig:: CONFIG_part_variant not in ('AM62LX')

   We offer methods for U-Boot's Secondary Program Loader (SPL) to securely
   verify the U-Boot proper. U-Boot calls Texas Instrument Foundational
   Security (TIFS) through Texas Instruments System Controller Interface
   (TISCI) to do this. For more information about using TISCI methods see the
   `TISCI User Guide <https://software-dl.ti.com/tisci/esd/latest/index.html>`__.
   U-Boot proper then securely verifies and decrypts the kernel, Device Tree
   Blobs (DTB), and initramfs.

   .. Image:: /images/K3_KF.png
      :scale: 70%

Secure boot has layers. Some layers are trusted more than others. Secure ROM has the highest trust and Runtime Execution
Environment (REE) non-trustzone user-space applications have the least. If a
lower trust entity must load a higher trust code, an even higher trust entity
must verify it and not allow access by the lower trust entity after that
point. Some such trust inversions are as follows:

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   - A53 Public Boot ROM loading TF-A/OP-TEE
   - A53 Public Boot ROM loading TIFS
   - Linux loading Trusted applications (TA)

.. ifconfig:: CONFIG_part_variant not in ('AM62LX')

   - R5 U-Boot loading TF-A/OP-TEE
   - R5 Public Boot ROM loading TIFS
   - Linux loading Trusted applications (TA)

These are called out in the sequence as shown in the following image and their method of ensuring trust is explained.

Secure Boot Flow
--------------------

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   .. Image:: /images/AM62L_BF.png
      :scale: 70%

.. ifconfig:: CONFIG_part_variant not in ('AM62LX')

   .. Image:: /images/K3_BF.jpg
      :scale: 70%

.. rubric:: ROM

.. ifconfig:: CONFIG_part_variant not in ('AM62LX')

   On device startup, execution begins with the ROM bootloader (Secure ROM)
   running on the DSMC/TIFS core. After initial device security setup the
   Secure ROM starts the Public ROM running on the R5 core. The Public Boot ROM
   handles loading the first stage image :file:`tiboot3.bin` from a peripheral
   as selected by the BOOTMODE pins. This image is placed into on chip SRAM as
   external memory interfaces such as DDR are not yet enabled. The exact
   location is device dependent. More details can be found in the device
   "Technical Reference Manual".

   .. ifconfig:: CONFIG_part_variant in ('AM64X')

      The contents of this first stage image are authenticated and decrypted by
      the Secure ROM. Contents include:

      * DMSC firmware: `Texas Instruments Foundational Security (TIFS)` + Device/Power Manager: After authentication/decryption, DMSC firmware replaces the Secure ROM as the authenticator entity executing on the DMSC core.
      * R5 SPL: The R5 SPL bootloader is executed on the R5 core.

   .. ifconfig:: CONFIG_part_variant not in ('AM64X')

      The contents of this first stage image are authenticated and decrypted by
      the Secure ROM. Contents include:

      * `Texas Instruments Foundational Security (TIFS)` firmware: After authentication/decryption, TIFS firmware replaces the Secure ROM as the authenticator entity executing on the TIFS core.
      * R5 SPL: The R5 SPL bootloader is executed on the R5 core.

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   On device startup, execution begins with the ROM bootloader (Secure ROM)
   running on SMS M4 core. After initial device security setup, the Secure ROM
   starts the Public ROM running on the A53 core. The Public ROM handles
   loading the first stage image :file:`tiboot3.bin` from a peripheral as
   selected by the BOOTMODE pins. This image is placed into on-chip SRAM as
   external memory interfaces such as DDR are not yet enabled. The exact
   location is device dependent. More details can be found in the device
   "Technical Reference Manual".

   The contents of this first stage image are authenticated and decrypted by the Secure ROM. Contents include:

   * `Texas Instruments Foundational Security (TIFS)` firmware: After authentication/decryption, TIFS firmware replaces the Secure ROM as the authenticator entity executing on the M4 core in the 2nd phase of the boot.
   * BL-1: The pre-bootloader executed on the A53 core, initializes the console and DDR for the 2nd phase of the boot.

.. ifconfig:: CONFIG_part_variant not in ('AM62LX')

   .. rubric:: R5 SPL

   R5 SPL loads the second boot stage FIT image `tispl.bin` from the
   peripheral as selected by the BOOTMODE pins. From this FIT image, TF-A,
   OPTEE, A53 SPL, and SPL DTB are extracted and authenticated and/or decrypted
   by TIFS. If authentication passed, the R5 SPL starts the ARM64 core. TF-A,
   OPTEE, and A53 SPL will begin execution on the ARM64 core. R5 SPL also
   configures DDR and the console so the user can see the first prints as seen
   below:

   R5 SPL's output will be similar to this:
   Notice the "Authentication passed" lines as TF-A, OPTEE, A53 SPL, and SPL DTB are authenticated.

   .. code-block:: console

      U-Boot SPL 2021.01-dirty (May 13 2022 - 15:05:11 -0500)
      SYSFW ABI: 3.1 (firmware rev 0x0008 '8.4.0-3-gd5cb1+ (Jolly Jellyfis')
      SPL initial stack usage: 13392 bytes
      Trying to boot from MMC2
      Authentication passed
      Authentication passed
      Authentication passed
      Authentication passed
      Starting ATF on ARM64 core...

   .. ifconfig:: CONFIG_part_variant in ('AM62x')

      After R5 SPL, the device/power manager firmware continues running on the R5 core.

.. rubric:: A53 SPL

.. ifconfig:: CONFIG_part_variant not in ('AM62LX')

   A53 SPL then loads the U-Boot proper FIT image :file:`u-boot.img` from the
   peripheral as selected by the BOOTMODE pins. From this FIT image, the U-Boot
   bootloader and DTB are extracted before passing execution to U-Boot proper.

   A53 SPL's output will be similar to this: (notice the "Authentication passed" lines as U-Boot and the DTB are authenticated).

   .. code-block:: console

      U-Boot SPL 2021.01-g2de57d278b (May 16 2022 - 14:28:40 +0000)
      SYSFW ABI: 3.1 (firmware rev 0x0008 '8.4.0-3-gd5cb1+ (Jolly Jellyfis')
      Trying to boot from MMC2
      Authentication passed
      Authentication passed

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   Public ROM loads the second boot stage image :file:`tispl.bin` from the
   peripheral as selected by the BOOTMODE pins. From this image, TF-A, OP-TEE,
   A53 SPL (U-Boot SPL) and SPL DTB are extracted and authenticated and/or
   decrypted by the Secure ROM. If authenticated, the Secure ROM resets the A53
   core. TF-A, OP-TEE and U-Boot SPL begin execution on the A53 core.

   U-Boot SPL then loads the U-Boot proper FIT image :file:`u-boot.img` from
   the peripheral as selected by the BOOTMODE pins. The U-Boot SPL verifies the
   signed FIT image independently, without using TIFS. From this FIT image, the
   U-Boot bootloader and DTB are extracted before passing execution to U-Boot
   proper.

   U-Boot SPL's output will be similar to this: (notice the "Checking hash(es)"
   lines as U-Boot and DTB are authenticated).

   .. code-block:: console

      U-Boot SPL 2026.01-ti-gee3048ee0822 (Apr 09 2026 - 00:09:07 +0000)
      SPL initial stack usage: 1936 bytes
      Trying to boot from DFU
      ######DOWNLOAD ... OK
      Ctrl+C to exit ...
      ## Checking hash(es) for config conf-0 ... sha512,rsa4096:custMpk+ OK
      ## Checking hash(es) for Image uboot ... sha512+ OK
      ## Checking hash(es) for Image fdt-0 ... sha512+ OK

.. rubric:: U-Boot

The boot flow continues as it does on a non-secure device, until loading the next FIT image named `fitImage`. This FIT image includes the Linux kernel, DTB, and
other required boot artifacts. U-boot verifies the signed images on boot independently, without using TIFS. U-boot extracts each component from the FIT image and verifies its signature. Once u-boot verifies all components, it starts Linux. For more information, see: `U-Boot FIT Signature Documentation <https://docs.u-boot.org/en/latest/usage/fit/signature.html>`__

U-boot's output will be similar to this:

.. code-block:: console

    U-Boot 2021.01-g2de57d278b (May 16 2022 - 14:28:40 +0000)

    SoC:   AM64X SR1.0
    Model: Texas Instruments AM642 EVM
    Board: AM64-GPEVM rev A
    DRAM:  2 GiB
    NAND:  0 MiB
    MMC:   mmc@fa10000: 0, mmc@fa00000: 1
    Loading Environment from FAT... *** Warning - bad CRC, using default environment

    In:    serial@2800000
    Out:   serial@2800000
    Err:   serial@2800000
    Net:   eth0: ethernet@8000000port@1
    Hit any key to stop autoboot:  0
    switch to partitions #0, OK
    mmc1 is current device
    SD/MMC found on device 1
    Failed to load 'boot.scr'
    1011 bytes read in 2 ms (493.2 KiB/s)
    Loaded env from uEnv.txt
    Importing environment from mmc1 ...
    Running uenvcmd ...
    7862647 bytes read in 328 ms (22.9 MiB/s)
    ## Loading kernel from FIT Image at 90000000 ...
    Using 'k3-am642-evm.dtb' configuration
    Trying 'kernel@1' kernel subimage
        Description:  Linux kernel
        Type:         Kernel Image
        Compression:  gzip compressed
        Data Start:   0x900000f8
        Data Size:    7743643 Bytes = 7.4 MiB
        Architecture: AArch64
        OS:           Linux
        Load Address: 0x80080000
        Entry Point:  0x80080000
    Verifying Hash Integrity ... OK
    ## Loading fdt from FIT Image at 90000000 ...
    Using 'k3-am642-evm.dtb' configuration
    Trying 'k3-am642-evm.dtb' fdt subimage
        Description:  Flattened Device Tree blob
        Type:         Flat Device Tree
        Compression:  uncompressed
        Data Start:   0x90762a54
        Data Size:    56436 Bytes = 55.1 KiB
        Architecture: AArch64
        Load Address: 0x83000000
    Verifying Hash Integrity ... OK
    Loading fdt from 0x90762a54 to 0x83000000
    Booting using the fdt blob at 0x83000000
    Uncompressing Kernel Image
    Loading Device Tree to 000000008ffef000, end 000000008ffff602 ... OK

.. rubric:: Linux

If initramfs is included, we can trust our initial modules and tasks, but we cannot trust anything beyond this as the root file-system may have been
modified. To allow trusted use of files outside of our initramfs we use dm-verity. With this we can authenticate a block device as we read from it. As
any changes to this block-device will cause the authentication to fail, we cannot put any user-modifiable configurations or user installed programs
here. Only important, read-only, files should be placed on this partition, such as static kernel and operating system files and configurations. All
other files must be placed in a non-verifiable read-write user partition.

HS Boot Flow Tools
-------------------

U-boot:

   .. ifconfig:: CONFIG_part_variant not in ('AM62LX')

      The ti-u-boot source is a project used to create tiboot3.bin, tispl.bin, and u-boot.img. To create  tiboot3.bin for K3 family devices, u-boot builds R5 SPL and
      binman packages it in a `tiboot3.bin` image. To build A53 SPL, binman takes TF-A (bl31.bin), OPTEE (bl32.bin), A53 SPL, and A53 DTBs and packages
      them in a `tispl.bin` image. U-Boot can then use the openssl library to sign each component as specified in k3-<soc>-binman.dtsi.

      .. code-block:: console

         $ git clone https://git.ti.com/git/ti-u-boot/ti-u-boot.git

         $ # Example use:
         $ make ARCH=arm CROSS_COMPILE=aarch64-none-linux-gnu- am64x_evm_a53_defconfig
         $ make CROSS_COMPILE=aarch64-none-linux-gnu- BL31=bl31.bin TEE=tee-pager_v2.bin BINMAN_INDIRS=<path-to-tisdk>/board-support/prebuilt-images

   .. ifconfig:: CONFIG_part_variant in ('AM62LX')

      The ti-u-boot source is a project used to create :file:`tiboot3.bin`,
      :file:`tispl.bin`, and :file:`u-boot.img`. To create :file:`tiboot3.bin`
      for K3 family devices, U-Boot builds BL-1 and binman packages it in a
      :file:`tiboot3.bin` image. To build A53 SPL, binman takes TF-A
      (:file:`bl31.bin`), OPTEE (:file:`bl32.bin`), A53 SPL, and A53 DTBs and
      packages them in a :file:`tispl.bin` image. U-Boot can then use the
      openssl library to sign each component as specified in
      :file:`k3-am62l3-evm-binman.dtsi`.

      .. code-block:: console

         $ git clone https://git.ti.com/git/ti-u-boot/ti-u-boot.git

         $ # Example use:
         $ make ARCH=arm CROSS_COMPILE=aarch64-none-linux-gnu- am62lx_evm_defconfig
         $ make CROSS_COMPILE=aarch64-none-linux-gnu- BL1=bl1.bin BL31=bl31.bin TEE=tee-pager_v2.bin BINMAN_INDIRS=<path-to-tisdk>/board-support/prebuilt-images

Linux:

    The ti-linux source is a TI project used to build Linux kernel, DTB, and other boot artifacts. Some of these components could be included in a verifiable image
    `fitImage`. For HS devices, only the fitImage will be allowed to boot once `fitImage` has been authenticated.

    .. code-block:: console

        $ git clone https://git.ti.com/git/ti-linux-kernel/ti-linux-kernel.git

        Example use:
        $ make ARCH=arm64 CROSS_COMPILE=aarch64-none-linux-gnu- defconfig ti_arm64_prune.config
        $ make ARCH=arm64 CROSS_COMPILE=aarch64-none-linux-gnu- menuconfig
        $ make ARCH=arm64 CROSS_COMPILE=aarch64-none-linux-gnu-

ATF:

    The ATF source (now called TF-A) is used to build `bl31.bin` that gets packaged into `tispl.bin`. For HS devices, this binary needs to be signed.

    .. code-block:: console

        $ git clone https://git.trustedfirmware.org/TF-A/trusted-firmware-a.git

        Example use:
        $ make ARCH=aarch64 CROSS_COMPILE=aarch64-none-linux-gnu- PLAT=k3 TARGET_BOARD=lite SPD=opteed

OPTEE:

   The OPTEE source is used to build `bl32.bin/tee-pager_v2.bin` that gets packaged into `tispl.bin`. For HS devices, this binary needs to be signed.

    .. code-block:: console

        $ git clone https://github.com/OP-TEE/optee_os.git

        Example use:
        $ make CROSS_COMPILE64=aarch64-linux-gnu- PLATFORM=k3-<soc> CFG_ARM64_core=y

Ti-linux-firmware:

    The ti-linux-firmware is a TI repository where all firmware releases are stored. Firmwares for a device family can also be found in the pre-built SDK
    under :file:`<path-to-tisdk>/board-support/prebuilt-images/<evm>`. Binman expects to find the device firmware with the following appended to u-boot build command:
    BINMAN_INDIRS=<path-to-tisdk>/board-support/prebuilt-images, and expects to find a ti-sysfw directory in this path.

    .. code-block:: console

        $ <https://git.ti.com/git/processor-firmware/ti-linux-firmware.git
        Branch: ti-linux-firmware.
