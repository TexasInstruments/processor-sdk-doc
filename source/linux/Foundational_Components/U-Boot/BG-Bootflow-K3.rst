.. _u-boot-build-guide-bootflow-k3:

########
Bootflow
########

.. _Boot-Flow-label:

*********
Boot Flow
*********

.. ifconfig:: CONFIG_part_family in ('General_family', 'AM335X_family', 'AM437X_family')

   Booting the Linux kernel on an embedded platform is not as simple as simply
   pointing a program counter to the kernel location and letting the processor
   run. This section will review the four bootloader software stages that must
   be run before the kernel can be booted and run on the device.

   Application processors such as the the AM335x are complex pieces of hardware,
   but have limited internal RAM (e.g., 128KB). Because of this limited amount
   of RAM, multiple bootloader stages are needed. These bootloader stages
   systematically unlock the full functionality of the device so that all
   complexities of the device are available to the kernel.

   There are four distinct bootloader stages:

   .. Image:: /images/U-Boot_Boot_Order_32bit.png

   1. ROM Code

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

   2. SPL or MLO

   The second stage bootloader is known as the SPL (Secondary Program Loader),
   but is sometimes referred to as the MLO (MMC Card Loader). The SPL is the
   first stage of U-Boot, and must be loaded from one of the boot sources into
   internal RAM. The SPL has very limited configuration or user interaction,
   and mainly serves to initialize the external DDR memory and set-up the boot
   process for the next bootloader stage: U-Boot.

   3. U-Boot

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

   4. Linux Kernel

   **zImage** is the compressed kernel image wrapped with header info that
   describes the kernel. This header includes the target architecture, the
   operating system, kernel size, entry points, etc. The loading of the kernel
   image is typically performed through the use of scripts stored in the U-Boot
   environment (all starting with the **bootcmd** ENV variable that gets
   executed after the autoboot countdown expires or manually by entering the
   **boot** command at the U-Boot prompt). This also involves passing a board-
   specific device tree blob (DTB) as an argument to U-Boot's **bootz**
   command that will extract and start the actual kernel.

.. ifconfig:: CONFIG_part_family not in ('General_family', 'AM335X_family', 'AM437X_family', 'AM62LX_family')

   On K3 architecture based devices, ROM supports boot only via MCU(R5). This means that
   bootloader has to run on R5 core. In order to meet this constraint, keeping
   safety in picture and to have faster boot time, the software boot architecture
   is designed as below:

   .. ifconfig:: CONFIG_part_family not in ('J7_family', 'AM64X_family', 'AM62X_family', 'AM62AX_family')

      .. code-block:: text

            +------------------------------------------------------------------------+
            |        DMSC            |         R5            |        ARM64          |
            +------------------------------------------------------------------------+
            |    +--------+          |                       |                       |
            |    |  Reset |          |                       |                       |
            |    +--------+          |                       |                       |
            |         :              |                       |                       |
            |    +--------+          |   +-----------+       |                       |
            |    | *ROM*  |----------|-->| Reset rls |       |                       |
            |    +--------+          |   +-----------+       |                       |
            |    |        |          |         :             |                       |
            |    |  ROM   |          |         :             |                       |
            |    |services|          |         :             |                       |
            |    |        |          |   +-------------+     |                       |
            |    |        |          |   |  *R5 ROM*   |     |                       |
            |    |        |          |   +-------------+     |                       |
            |    |        |<---------|---|Load and auth|     |                       |
            |    |        |          |   | tiboot3.bin |     |                       |
            |    |        |          |   +-------------+     |                       |
            |    |        |          |         :             |                       |
            |    |        |          |         :             |                       |
            |    |        |          |         :             |                       |
            |    |        |          |   +-------------+     |                       |
            |    |        |          |   |  *R5 SPL*   |     |                       |
            |    |        |          |   +-------------+     |                       |
            |    |        |          |   |    Load     |     |                       |
            |    |        |          |   |  sysfw.itb  |     |                       |
            |    | Start  |          |   +-------------+     |                       |
            |    | System |<---------|---|    Start    |     |                       |
            |    |Firmware|          |   |    SYSFW    |     |                       |
            |    +--------+          |   +-------------+     |                       |
            |        :               |   |             |     |                       |
            |    +---------+         |   |   Load      |     |                       |
            |    | *SYSFW* |         |   |   system    |     |                       |
            |    +---------+         |   | Config data |     |                       |
            |    |         |<--------|---|             |     |                       |
            |    |         |         |   +-------------+     |                       |
            |    |         |         |   |             |     |                       |
            |    |         |         |   |    DDR      |     |                       |
            |    |         |         |   |   config    |     |                       |
            |    |         |         |   +-------------+     |                       |
            |    |         |         |   |             |     |                       |
            |    |         |<--------|---| Start A53   |     |                       |
            |    |         |         |   |  and Reset  |     |                       |
            |    |         |         |   +-------------+     |                       |
            |    |         |         |                       |     +-----------+     |
            |    |         |---------|-----------------------|---->| Reset rls |     |
            |    |         |         |                       |     +-----------+     |
            |    |  DMSC   |         |                       |          :            |
            |    |Services |         |                       |     +-----------+     |
            |    |         |<--------|-----------------------|---->|*ATF/OPTEE*|     |
            |    |         |         |                       |     +-----------+     |
            |    |         |         |                       |          :            |
            |    |         |         |                       |     +-----------+     |
            |    |         |<--------|-----------------------|---->| *A53 SPL* |     |
            |    |         |         |                       |     +-----------+     |
            |    |         |         |                       |     |   Load    |     |
            |    |         |         |                       |     | u-boot.img|     |
            |    |         |         |                       |     +-----------+     |
            |    |         |         |                       |          :            |
            |    |         |         |                       |     +-----------+     |
            |    |         |<--------|-----------------------|---->| *U-Boot*  |     |
            |    |         |         |                       |     +-----------+     |
            |    |         |         |                       |     |  prompt   |     |
            |    |         |         |                       |     +-----------+     |
            |    +---------+         |                       |                       |
            |                        |                       |                       |
            +------------------------------------------------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('J721E')

      .. code-block:: text

         +------------------------------------------------------------------------+-----------------------+
         |        DMSC            |      MCU R5           |        A72            |  MAIN R5/C66x/C7x     |
         +------------------------------------------------------------------------+-----------------------+
         |    +--------+          |                       |                       |                       |
         |    |  Reset |          |                       |                       |                       |
         |    +--------+          |                       |                       |                       |
         |         :              |                       |                       |                       |
         |    +--------+          |   +-----------+       |                       |                       |
         |    | *ROM*  |----------|-->| Reset rls |       |                       |                       |
         |    +--------+          |   +-----------+       |                       |                       |
         |    |        |          |         :             |                       |                       |
         |    |  ROM   |          |         :             |                       |                       |
         |    |services|          |         :             |                       |                       |
         |    |        |          |   +-------------+     |                       |                       |
         |    |        |          |   |  *R5 ROM*   |     |                       |                       |
         |    |        |          |   +-------------+     |                       |                       |
         |    |        |<---------|---|Load and auth|     |                       |                       |
         |    |        |          |   | tiboot3.bin |     |                       |                       |
         |    |        |          |   +-------------+     |                       |                       |
         |    |        |          |         :             |                       |                       |
         |    |        |          |         :             |                       |                       |
         |    |        |          |         :             |                       |                       |
         |    |        |          |   +-------------+     |                       |                       |
         |    |        |          |   |  *R5 SPL*   |     |                       |                       |
         |    |        |          |   +-------------+     |                       |                       |
         |    |        |          |   |    Load     |     |                       |                       |
         |    |        |          |   |  sysfw.itb  |     |                       |                       |
         |    | Start  |          |   +-------------+     |                       |                       |
         |    | System |<---------|---|    Start    |     |                       |                       |
         |    |Firmware|          |   |    SYSFW    |     |                       |                       |
         |    +--------+          |   +-------------+     |                       |                       |
         |        :               |   |             |     |                       |                       |
         |    +---------+         |   |   Load      |     |                       |                       |
         |    | *SYSFW* |         |   |   system    |     |                       |                       |
         |    +---------+         |   | Config data |     |                       |                       |
         |    |         |<--------|---|             |     |                       |                       |
         |    |         |         |   +-------------+     |                       |                       |
         |    |         |         |   |    DDR      |     |                       |                       |
         |    |         |         |   |   config    |     |                       |                       |
         |    |         |         |   +-------------+     |                       |                       |
         |    |         |         |   |    Load     |     |                       |                       |
         |    |         |         |   |  tispl.bin  |     |                       |                       |
         |    |         |         |   +-------------+     |                       |                       |
         |    |         |         |   |   Load R5   |     |                       |                       |
         |    |         |         |   |   firmware  |     |                       |                       |
         |    |         |         |   +-------------+     |                       |                       |
         |    |         |<--------|---| Start A72   |     |                       |                       |
         |    |         |         |   | and jump to |     |                       |                       |
         |    |         |         |   | DM fw image |     |                       |                       |
         |    |         |         |   +-------------+     |                       |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |---------|-----------------------|---->| Reset rls |     |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |  TIFS   |         |                       |          :            |                       |
         |    |Services |         |                       |     +-----------+     |                       |
         |    |         |<--------|-----------------------|---->|*ATF/OPTEE*|     |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |         |                       |          :            |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |<--------|-----------------------|---->| *A72 SPL* |     |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |         |                       |     |   Load    |     |                       |
         |    |         |         |                       |     | u-boot.img|     |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |         |                       |          :            |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |<--------|-----------------------|---->| *U-Boot*  |     |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |         |                       |     |  prompt   |     |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |         |                       |     |  Load R5  |     |                       |
         |    |         |         |                       |     |  Firmware |     |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |<--------|-----------------------|-----|  Start R5 |     |      +-----------+    |
         |    |         |---------|-----------------------|-----+-----------+-----|----->| R5 starts |    |
         |    |         |         |                       |     |  Load C6  |     |      +-----------+    |
         |    |         |         |                       |     |  Firmware |     |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |<--------|-----------------------|-----|  Start C6 |     |      +-----------+    |
         |    |         |---------|-----------------------|-----+-----------+-----|----->| C6 starts |    |
         |    |         |         |                       |     |  Load C7  |     |      +-----------+    |
         |    |         |         |                       |     |  Firmware |     |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |<--------|-----------------------|-----|  Start C7 |     |      +-----------+    |
         |    |         |---------|-----------------------|-----+-----------+-----|----->| C7 starts |    |
         |    +---------+         |                       |                       |      +-----------+    |
         |                        |                       |                       |                       |
         +------------------------------------------------------------------------+-----------------------+

   .. ifconfig:: CONFIG_part_variant in ('J7200', 'J721S2', 'J784S4','J742S2')

      .. code-block:: text

         +------------------------------------------------------------------------+-----------------------+
         |        SMS             |      MCU R5           |        A72            |  MAIN R5/C7x          |
         +------------------------------------------------------------------------+-----------------------+
         |    +--------+          |                       |                       |                       |
         |    |  Reset |          |                       |                       |                       |
         |    +--------+          |                       |                       |                       |
         |         :              |                       |                       |                       |
         |    +--------+          |   +-----------+       |                       |                       |
         |    | *ROM*  |----------|-->| Reset rls |       |                       |                       |
         |    +--------+          |   +-----------+       |                       |                       |
         |    |        |          |         :             |                       |                       |
         |    |  ROM   |          |         :             |                       |                       |
         |    |services|          |         :             |                       |                       |
         |    |        |          |   +-------------+     |                       |                       |
         |    |        |          |   |  *R5 ROM*   |     |                       |                       |
         |    |        |          |   +-------------+     |                       |                       |
         |    |        |<---------|---|Load and auth|     |                       |                       |
         |    |        |          |   | tiboot3.bin |     |                       |                       |
         |    | Start  |          |   +-------------+     |                       |                       |
         |    |  TIFS  |<---------|---|    Start    |     |                       |                       |
         |    |        |          |   |    TIFS     |     |                       |                       |
         |    +--------+          |   +-------------+     |                       |                       |
         |        :               |   |             |     |                       |                       |
         |    +---------+         |   |   Load      |     |                       |                       |
         |    | *TIFS*  |         |   |   system    |     |                       |                       |
         |    +---------+         |   | Config data |     |                       |                       |
         |    |         |<--------|---|             |     |                       |                       |
         |    |         |         |   +-------------+     |                       |                       |
         |    |         |         |         :             |                       |                       |
         |    |         |         |         :             |                       |                       |
         |    |         |         |         :             |                       |                       |
         |    |         |         |   +-------------+     |                       |                       |
         |    |         |         |   |  *R5 SPL*   |     |                       |                       |
         |    |         |         |   +-------------+     |                       |                       |
         |    |         |         |   |    DDR      |     |                       |                       |
         |    |         |         |   |   config    |     |                       |                       |
         |    |         |         |   +-------------+     |                       |                       |
         |    |         |         |   |    Load     |     |                       |                       |
         |    |         |         |   |  tispl.bin  |     |                       |                       |
         |    |         |         |   +-------------+     |                       |                       |
         |    |         |         |   |   Load R5   |     |                       |                       |
         |    |         |         |   |   firmware  |     |                       |                       |
         |    |         |         |   +-------------+     |                       |                       |
         |    |         |<--------|---| Start A72   |     |                       |                       |
         |    |         |         |   | and jump to |     |                       |                       |
         |    |         |         |   | DM fw image |     |                       |                       |
         |    |         |         |   +-------------+     |                       |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |---------|-----------------------|---->| Reset rls |     |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |  TIFS   |         |                       |          :            |                       |
         |    |Services |         |                       |     +-----------+     |                       |
         |    |         |<--------|-----------------------|---->|*ATF/OPTEE*|     |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |         |                       |          :            |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |<--------|-----------------------|---->| *A72 SPL* |     |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |         |                       |     |   Load    |     |                       |
         |    |         |         |                       |     | u-boot.img|     |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |         |                       |          :            |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |<--------|-----------------------|---->| *U-Boot*  |     |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |         |                       |     |  prompt   |     |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |         |                       |     |  Load R5  |     |                       |
         |    |         |         |                       |     |  Firmware |     |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |<--------|-----------------------|-----|  Start R5 |     |      +-----------+    |
         |    |         |---------|-----------------------|-----+-----------+-----|----->| R5 starts |    |
         |    |         |         |                       |     |  Load C7  |     |      +-----------+    |
         |    |         |         |                       |     |  Firmware |     |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |<--------|-----------------------|-----|  Start C7 |     |      +-----------+    |
         |    |         |---------|-----------------------|-----+-----------+-----|----->| C7 starts |    |
         |    |         |         |                       |                       |      +-----------+    |
         |    |         |         |                       |                       |                       |
         |    +---------+         |                       |                       |                       |
         |                        |                       |                       |                       |
         +------------------------------------------------------------------------+-----------------------+

   .. ifconfig:: CONFIG_part_variant in ('AM64X')

      .. code-block:: text

         +------------------------------------------------------------------------+-----------------------+
         |        DMSC            |      MAIN R50         |         A53           |   MAIN R51            |
         +------------------------------------------------------------------------+-----------------------+
         |    +--------+          |                       |                       |                       |
         |    |  Reset |          |                       |                       |                       |
         |    +--------+          |                       |                       |                       |
         |         :              |                       |                       |                       |
         |    +--------+          |   +-----------+       |                       |                       |
         |    | *ROM*  |----------|-->| Reset rls |       |                       |                       |
         |    +--------+          |   +-----------+       |                       |                       |
         |    |        |          |         :             |                       |                       |
         |    |  ROM   |          |         :             |                       |                       |
         |    |services|          |         :             |                       |                       |
         |    |        |          |   +-------------+     |                       |                       |
         |    |        |          |   |  *R5 ROM*   |     |                       |                       |
         |    |        |          |   +-------------+     |                       |                       |
         |    |        |<---------|---|Load and auth|     |                       |                       |
         |    |        |          |   | tiboot3.bin |     |                       |                       |
         |    | Start  |          |   +-------------+     |                       |                       |
         |    | SYSFW  |<---------|---|    Start    |     |                       |                       |
         |    |        |          |   |    SYSFW    |     |                       |                       |
         |    +--------+          |   +-------------+     |                       |                       |
         |        :               |   |             |     |                       |                       |
         |    +---------+         |   |   Load      |     |                       |                       |
         |    | *SYSFW* |         |   |   system    |     |                       |                       |
         |    +---------+         |   | Config data |     |                       |                       |
         |    |         |<--------|---|             |     |                       |                       |
         |    |         |         |   +-------------+     |                       |                       |
         |    |         |         |         :             |                       |                       |
         |    |         |         |         :             |                       |                       |
         |    |         |         |         :             |                       |                       |
         |    |         |         |   +-------------+     |                       |                       |
         |    |         |         |   |  *R5 SPL*   |     |                       |                       |
         |    |         |         |   +-------------+     |                       |                       |
         |    |         |         |   |    DDR      |     |                       |                       |
         |    |         |         |   |   config    |     |                       |                       |
         |    |         |         |   +-------------+     |                       |                       |
         |    |         |         |   |    Load     |     |                       |                       |
         |    |         |         |   |  tispl.bin  |     |                       |                       |
         |    |         |         |   +-------------+     |                       |                       |
         |    |         |<--------|---| Start A53   |     |                       |                       |
         |    |         |         |   +-------------+     |                       |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |---------|-----------------------|---->| Reset rls |     |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |  SYSFW  |         |                       |          :            |                       |
         |    |Services |         |                       |     +-----------+     |                       |
         |    |         |<--------|-----------------------|---->|*ATF/OPTEE*|     |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |         |                       |          :            |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |<--------|-----------------------|---->| *A53 SPL* |     |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |         |                       |     |   Load    |     |                       |
         |    |         |         |                       |     | u-boot.img|     |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |         |                       |          :            |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |<--------|-----------------------|---->| *U-Boot*  |     |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |         |                       |     |  prompt   |     |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |         |                       |     |  Load R5  |     |                       |
         |    |         |         |                       |     |  Firmware |     |                       |
         |    |         |         |                       |     +-----------+     |                       |
         |    |         |<--------|-----------------------|-----|  Start R5 |     |      +-----------+    |
         |    |         |---------|-----------------------|-----+-----------+-----|----->| R5 starts |    |
         |    |         |         |                       |                       |      +-----------+    |
         |    |         |         |                       |                       |                       |
         |    +---------+         |                       |                       |                       |
         |                        |                       |                       |                       |
         +------------------------------------------------------------------------+-----------------------+

   .. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX', 'AM62PX', 'J722S')

      .. code-block:: text

         +------------------------------------------------------------------------+
         |        TIFS            |      Main R5          |        A53            |
         +------------------------------------------------------------------------+
         |    +--------+          |                       |                       |
         |    |  Reset |          |                       |                       |
         |    +--------+          |                       |                       |
         |         :              |                       |                       |
         |    +--------+          |   +-----------+       |                       |
         |    | *ROM*  |----------|-->| Reset rls |       |                       |
         |    +--------+          |   +-----------+       |                       |
         |    |        |          |         :             |                       |
         |    |  ROM   |          |         :             |                       |
         |    |services|          |         :             |                       |
         |    |        |          |   +-------------+     |                       |
         |    |        |          |   |  *R5 ROM*   |     |                       |
         |    |        |          |   +-------------+     |                       |
         |    |        |<---------|---|Load and auth|     |                       |
         |    |        |          |   | tiboot3.bin |     |                       |
         |    +--------+          |   +-------------+     |                       |
         |    |        |<---------|---| Load sysfw  |     |                       |
         |    |        |          |   | part to TIFS|     |                       |
         |    |        |          |   | core        |     |                       |
         |    |        |          |   +-------------+     |                       |
         |    |        |          |         :             |                       |
         |    |        |          |         :             |                       |
         |    |        |          |         :             |                       |
         |    |        |          |   +-------------+     |                       |
         |    |        |          |   |  *R5 SPL*   |     |                       |
         |    |        |          |   +-------------+     |                       |
         |    |        |          |   |    DDR      |     |                       |
         |    |        |          |   |   config    |     |                       |
         |    |        |          |   +-------------+     |                       |
         |    |        |          |   |    Load     |     |                       |
         |    |        |          |   |  tispl.bin  |     |                       |
         |    |        |          |   +-------------+     |                       |
         |    |        |          |   |   Load R5   |     |                       |
         |    |        |          |   |   firmware  |     |                       |
         |    |        |          |   +-------------+     |                       |
         |    |        |<---------|---| Start A53   |     |                       |
         |    |        |          |   | and jump to |     |                       |
         |    |        |          |   | DM fw image |     |                       |
         |    |        |          |   +-------------+     |                       |
         |    |        |          |                       |     +-----------+     |
         |    |        |----------|-----------------------|---->| Reset rls |     |
         |    |        |          |                       |     +-----------+     |
         |    |  TIFS  |          |                       |          :            |
         |    |Services|          |                       |     +-----------+     |
         |    |        |<---------|-----------------------|---->|*ATF/OPTEE*|     |
         |    |        |          |                       |     +-----------+     |
         |    |        |          |                       |          :            |
         |    |        |          |                       |     +-----------+     |
         |    |        |<---------|-----------------------|---->| *A53 SPL* |     |
         |    |        |          |                       |     +-----------+     |
         |    |        |          |                       |     |   Load    |     |
         |    |        |          |                       |     | u-boot.img|     |
         |    |        |          |                       |     +-----------+     |
         |    |        |          |                       |          :            |
         |    |        |          |                       |     +-----------+     |
         |    |        |<---------|-----------------------|---->| *U-Boot*  |     |
         |    |        |          |                       |     +-----------+     |
         |    |        |          |                       |     |  prompt   |     |
         |    |        |----------|-----------------------|-----+-----------+-----|
         |    +--------+          |                       |                       |
         |                        |                       |                       |
         +------------------------------------------------------------------------+

   Here |__SYSFW_CORE_NAME__| acts as master and provides all the critical services. R5/ARM64
   requests |__SYSFW_CORE_NAME__| to get these services done as shown in the above diagram.

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   Unlike with most other K3 SoCs the AM62LX does not have an Cortext-R5
   MCU core which ROM uses to initialize the SoC therefore uses a 2
   phase ROM boot. The first phase will load the tiboot3.bin image which
   contains Trusted-Firmware-A's BL-1 loader along with the typical X.509
   certificate to authenticate and validate the image which is used to
   intialize the console and DDR for the next phase.

   .. code-block:: text

      ┌───────────────────┐┌───────────────────┐
      │    Secure ROM     ││    Public ROM     │
      │     SMS (M4)      ││   (Cortex-A53)    │
      │                   ││                   │
      │┌─────────────────┐││                   │
      ││  Reset Release  │││                   │
      │└────────┬────────┘││                   │
      │         │         ││                   │
      │┌────────▼────────┐││                   │
      ││    ROM Init     │││                   │
      │└────────┬────────┘││                   │
      │         │         ││                   │
      │┌────────▼────────┐││┌─────────────────┐│
      ││   Release A53   ┼┼┼►   Release A53   ││
      │└─────────────────┘││└────────┬────────┘│
      │                   ││         │         │
      │  Validate Image   ││┌────────▼────────┐│
      │┌─────────────────┐│││    ROM Init     ││
      ││ Integrity Check ◄┼┼┼   (1st Phase)   ││
      │├─────────────────│││└────────┬────────┘│
      ││ Authentication  │││         │         │
      │├─────────────────┤││┌────────▼────────┐│
      ││    Decryption   ││││       WFI       ││
      │└────────┬────────┘││└─────────────────┘│
      │         │         ││                   │
      │┌────────▼────────┐││    End of ROM     │
      ││  Wait for WFI   │││~~~~~~~~~~~~~~~~~~~│
      ││  on Cortex-A53  │││     Start of      │
      │└────────┬────────┘││       BL-1        │
      │         │         ││                   │
      │┌────────▼────────┐││┌─────────────────┐│
      ││    Start BL-1   ┼┼┼►    DDR Init     ││
      │└────────┬────────┘││└────────┬────────┘│
      │         │         ││         │         │
      │┌────────▼────────┐││┌────────▼────────┐│
      ││  Wait for BL-1  ◄┼┼┼  Send BL-1 Done ││
      ││     Done Msg    │││└────────┬────────┘│
      │└─────────────────┘││         │         │
      │                   ││┌────────▼────────┐│
      │                   │││       WFI       ││
      │                   ││└─────────────────┘│
      └───────────────────┘└───────────────────┘

   After the BL-1 sends a message back to the Secure ROM to indicate it
   has completed, the Secure ROM will reset the A53 back into Public ROM
   to begin the 2nd ROM boot phase to load the tispl.bin into the SoC.

   .. code-block:: text

      ┌───────────────────┐┌───────────────────┐
      │    Secure ROM     ││    Public ROM     │
      │     SMS (M4)      ││   (Cortex-A53)    │
      │                   ││                   │
      │┌─────────────────┐││                   │
      ││  Program Reset  │││┌─────────────────┐│
      ││   Vector And    ┼┼┼►   Release A53   ││
      ││    Reset A53    │││└────────┬────────┘│
      │└─────────────────┘││         │         │
      │                   ││         │         │
      │   Validate Image  ││┌────────▼────────┐│
      │┌─────────────────┐│││    ROM Init     ││
      ││ Integrity Check ◄┼┼┼   (2nd Phase)   ││
      │├─────────────────┤││└────────┬────────┘│
      ││ Authentication  │││         │         │
      │├─────────────────┤││┌────────▼────────┐│
      ││   Decryption    ││││       WFI       ││
      │└────────┬────────┘││└─────────────────┘│
      │         │         ││                   │
      │┌────────▼────────┐││     End of ROM    │
      ││  Wait for WFI   │││~~~~~~~~~~~~~~~~~~~│
      ││  on Cortex-A53  │││                   │
      │└────────┬────────┘││                   │
      │         │         ││                   │
      │┌────────▼────────┐││                   │
      ││  Program Reset  │││┌─────────────────┐│
      ││   Vector And    ┼┼┼►   TF-A (BL-31)  ││
      ││    Reset A53    │││└────────┬────────┘│
      │└────────┬────────┘││         │         │
      │         │         ││┌────────▼────────┐│
      │┌────────▼────────┐│││    U-Boot SPL   ││
      ││  Prep M4 Reset  │││└────────┬────────┘│
      │└────────┬────────┘││         │         │
      │         │         ││┌────────▼────────┐│
      │┌────────▼────────┐│││     U-Boot      ││
      ││    Boot TI-FS   │││└────────┬────────┘│
      │└────────┬────────┘││         │         │
      │         │         ││         │         │
      │     End of ROM    ││         │         │
      │~~~~~~~~~~~~~~~~~~~││         │         │
      │         │         ││┌────────▼────────┐│
      │┌────────▼────────┐│││                 ││
      ││                 ││││                 ││
      ││      TI-FS      ││││      Linux      ││
      └┴─────────────────┴┘└┴─────────────────┴┘

   From there TIFS, TF-A and U-Boot will has completed their
   initialization routines which can begin loading the operating system
   and complete the boot process.
