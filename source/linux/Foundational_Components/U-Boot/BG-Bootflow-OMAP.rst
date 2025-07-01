.. _u-boot-build-guide-bootflow-omap:

########
Bootflow
########

.. _Boot-Flow-label:

*********
Boot Flow
*********

Booting the Linux kernel on an embedded platform is not as simple as simply
pointing a program counter to the kernel location and letting the processor
run. This section will review the four bootloader software stages that must
be run before the kernel can be booted and run on the device.

Application processors such as these are complex pieces of hardware,
but have limited internal RAM (e.g., 128KB). Because of this limited amount
of RAM, multiple bootloader stages are needed. These bootloader stages
systematically unlock the full functionality of the device so that all
complexities of the device are available to the kernel.

There are four distinct bootloader stages:

.. Image:: /images/U-Boot_Boot_Order_32bit.png

#. ROM Code

   The first stage bootloader is housed in ROM on the device. The ROM code is
   the first block of code that is automatically run on device start-up or
   after power-on reset (POR). The ROM bootloader code is hardcoded into the
   device and cannot be changed by the user. Because of this, it is important
   to get an understanding of what exactly the ROM code is doing.

   The ROM code has two main functions:

   * Configuration of the device and initialization of primary peripherals
     such as stack setup, configuring the Watchdog Timer (see TRM for details)
     as well as the PLL and system clocks configuration

   * Readies the device for next bootloader by checking boot sources for next
     stage of bootloader (SPL) as well as loading the actual next stage
     bootloader code into memory and starting it

   The list of booting devices that the ROM code will search through for the
   second stage bootloader is configured by the voltage levels set on the
   devices SYSBOOT pins on startup. These pins also set other boot parameters
   (i.e. expected crystal frequency, bus width of external memory). For more
   information on the SYSBOOT pins and associated boot parameters see the
   device TRM.

#. SPL or MLO

   The second stage bootloader is known as the SPL (Secondary Program Loader),
   but is sometimes referred to as the MLO (MMC Card Loader). The SPL is the
   first stage of U-Boot, and must be loaded from one of the boot sources into
   internal RAM. The SPL has very limited configuration or user interaction,
   and mainly serves to initialize the external DDR memory and set-up the boot
   process for the next bootloader stage: U-Boot.

#. U-Boot

   U-Boot allows for powerful command-based control over the kernel boot
   environment via a serial terminal. The user has control over a number of
   parameters such as boot arguments and the kernel boot command. In addition,
   U-Boot environment variables can be configured. These environment variables
   are stored in the **uEnv.txt** file on your storage medium or directly in
   a Flash-based memory if configured such. These environment variables can be
   viewed, modified, and saved using the **env print**, **env set**, and
   **env save** commands, respectively. U-Boot is also a very useful tool to
   program and manipulate a wide range of external memory devices as well as
   a helpful aid during custom board bringup.

#. Linux Kernel

   **zImage** is the compressed kernel image wrapped with header info that
   describes the kernel. This header includes the target architecture, the
   operating system, kernel size, entry points, etc. The loading of the kernel
   image is typically performed through the use of scripts stored in the U-Boot
   environment (all starting with the **bootcmd** ENV variable that gets
   executed after the autoboot countdown expires or manually by entering the
   **boot** command at the U-Boot prompt). This also involves passing a board-
   specific device tree blob (DTB) as an argument to U-Boot's **bootz**
   command that will extract and start the actual kernel.
