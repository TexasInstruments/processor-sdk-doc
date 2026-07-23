.. _Uboot-splash-label:

====================
U-Boot splash screen
====================
A splash screen is the first screen a user sees when the device boots up.
Splash screens give the user feedback that the board is booting up and showcase the vendor logo for branding purposes. The logo also identifies the boot image the system uses at startup.

.. ifconfig:: CONFIG_part_variant not in ('AM62LX', 'AM62PX', 'J722S')

   The |__PART_FAMILY_DEVICE_NAMES__| offers out-of-box splash screen experience with OLDI display.

The |__PART_FAMILY_DEVICE_NAMES__| supports displaying a splash screen until the kernel boots up, with a flicker-free handoff across different boot stages.

------------------
Features supported
------------------
The following features are supported for splash screen in U-Boot:

#. Supports 32, 24, and 8 bits per pixel Bitmap (BMP) image.
#. Supports frame buffer of size 1920x1200 resolution, images with a resolution lesser than this can
   still be displayed using the same frame buffer.
#. Supports displaying only BMP and compressed BMP images using gzip or 8-bit Run-Length Encoding (RLE).
#. Supports MultiMediaCard (MMC) and Octal Serial Peripheral Interface (OSPI) as BMP image sources.

The |__PART_FAMILY_DEVICE_NAMES__| supports splash screen at both U-Boot proper and A53 Secondary Program Loader (SPL) with A53 SPL displaying
splash screen **~1.4 seconds** earlier than U-Boot proper.

Enable the splash screen on ti-u-boot
---------------------------------------
In this SDK release ti-u-boot supports a splash screen at both A53 SPL stage and U-Boot proper.

A53 SPL
^^^^^^^
By default the splash screen is only enabled at A53 SPL. The default splash source defaults to SD card and
displays a compressed TI logo BMP image. The SPL splash screen features compile into tispl.bin
as part of the U-Boot build. Any change to the SPL splash screen feature requires rebuilding tispl.bin.
Use the new tispl.bin to boot the board to see the splash screen at SPL stage.

At the SPL stage, the splash screen display function runs from :file:`board/ti/<platform>/evm.c` in ``function spl_board_init``

.. code-block:: c

   video_setup();
   enable_caches();
   if (IS_ENABLED(CONFIG_SPL_SPLASH_SCREEN) && IS_ENABLED(CONFIG_SPL_BMP))
       splash_display();

U-Boot proper
^^^^^^^^^^^^^

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62PX', 'AM62LX', 'J722S')

   To enable the splash screen at U-Boot proper enable the following configs in :file:`configs/<platform>_a53_defconfig`.

   .. code-block:: kconfig

      CONFIG_SPLASH_SCREEN=y
      CONFIG_SPLASH_SOURCE=y
      CONFIG_SPLASH_SCREEN_ALIGN=y
      CONFIG_HIDE_LOGO_VERSION=y

   To use the splash screen only at U-Boot proper, disable the splash screen at A53 SPL
   by disabling **CONFIG_SPL_VIDEO**.

   .. code-block:: kconfig

      # CONFIG_SPL_VIDEO=y

   The U-Boot proper splash screen compiles into :file:`u-boot.img`. Any change to this feature requires
   rebuilding :file:`u-boot.img`. Use the new :file:`u-boot.img` to boot the board to see the splash screen.

   .. note::

      If you enable the splash screen at U-Boot proper, it stays active until Linux boot starts.

Display custom logo as splash screen
------------------------------------
#. In U-Boot, U-Boot reads all splash screen image information from environment variables
   defined below. Add these in the .env file used by the board under :file:`board/ti/<platform>.env`.
   For reference, see :file:`board/ti/am62x.env`:

   .. code-block:: text

      #Name of file to be displayed
      splashfile=ti_logo_414x97_32bpp.bmp.gz

      #DDR address to load image from boot media
      splashimage=0x80200000

      #Position of image on display
      splashpos=m,m

      #Source of bmp image
      splashsource=mmc

#. To display a custom logo change the ``splashfile`` variable to logo_file_name.

#. If using an SD card as splash source, place the image in the boot partition of SD card that has
   :file:`tispl.bin` and :file:`u-boot.img`.

#. To display image from a different source, add the source information in struct
   default_splash_locations, defined in :file:`board/ti/<platform>/evm.c`.
   For example in :file:`board/ti/am62x/evm.c`, by default the code adds OSPI and SD card as sources as shown below :

   .. code-block:: c

      static struct splash_location default_splash_locations[] = {
           {
                   .name = "sf",
                   .storage = SPLASH_STORAGE_SF,
                   .flags = SPLASH_STORAGE_RAW,
                   .offset = 0x700000,
           },
           {
                   .name		= "mmc",
                   .storage	= SPLASH_STORAGE_MMC,
                   .flags		= SPLASH_STORAGE_FS,
                   .devpart	= "1:1",
           },
      };

#. Change the ``splashsource`` variable to the name of the source defined in the struct shown earlier.

.. important::

   :file:`<platform>.env` file gets compiled into :file:`u-boot.img` for U-Boot proper and into :file:`tispl.bin` for A53 SPL.
   Any changes made in .env will require the recompilation of :file:`u-boot.img`, :file:`tispl.bin`, or both, depending on the stage at which you enable the splash screen.

Enable splash screen on upstream U-Boot
-----------------------------------------

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   In upstream, the splash screen is supported at the driver level for both A53 SPL and U-Boot proper.

   However, user needs to enable the required kconfigs and device-tree nodes manually, The below commit can be used as
   a reference for making such changes.

   * `arm: dts: k3-am625-sk-u-boot: Add panel device-tree node  <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/commit/?h=ti-u-boot-2025.01&id=073bea998eb95d26c01e336a7b533c9e9fdbe767>`_

A53 SPL config options
^^^^^^^^^^^^^^^^^^^^^^

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62PX', 'J722S')

   To enable the splash screen at A53 SPL enable the following configs in :file:`configs/am62x_evm_a53_defconfig`:

   .. code-block:: kconfig

      CONFIG_CMD_BMP=y
      CONFIG_VIDEO=y
      CONFIG_SYS_WHITE_ON_BLACK=y
      CONFIG_VIDEO_TIDSS=y
      CONFIG_SPLASH_SCREEN=y
      CONFIG_SPLASH_SCREEN_ALIGN=y
      CONFIG_HIDE_LOGO_VERSION=y
      CONFIG_SPLASH_SOURCE=y
      CONFIG_VIDEO_BMP_GZIP=y
      CONFIG_BMP_24BPP=y
      CONFIG_BMP_32BPP=y
      CONFIG_SPL_GZIP=y
      CONFIG_SPL_VIDEO=y
      CONFIG_SPL_SPLASH_SCREEN=y
      CONFIG_SPL_SPLASH_SOURCE=y
      CONFIG_SPL_VIDEO_TIDSS=y
      CONFIG_SPL_BMP=y
      CONFIG_SPL_BOARD_INIT=y
      CONFIG_FS_LOADER=y
      CONFIG_SPL_SYS_WHITE_ON_BLACK=y
      CONFIG_SYS_SPL_MALLOC=y
      CONFIG_SPL_BMP_24BPP=y
      CONFIG_SPL_BMP_32BPP=y
      CONFIG_SPL_SPLASH_SCREEN_ALIGN=y
      CONFIG_SPL_DM_DEVICE_REMOVE=y
      CONFIG_SPL_VIDEO_BMP_GZIP=y
      CONFIG_SPL_HIDE_LOGO_VERSION=y
      CONFIG_BLOBLIST=y
      CONFIG_BLOBLIST_ADDR=0x80D00000

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   To enable the splash screen at A53 SPL enable the following configs in :file:`configs/am62x_evm_a53_defconfig`:

   .. code-block:: kconfig

      CONFIG_CMD_BMP=y
      CONFIG_VIDEO=y
      CONFIG_SYS_WHITE_ON_BLACK=y
      CONFIG_VIDEO_TIDSS=y
      CONFIG_SPLASH_SCREEN=y
      CONFIG_SPLASH_SCREEN_ALIGN=y
      CONFIG_HIDE_LOGO_VERSION=y
      CONFIG_SPLASH_SOURCE=y
      CONFIG_VIDEO_BMP_GZIP=y
      CONFIG_BMP_24BPP=y
      CONFIG_BMP_32BPP=y
      CONFIG_SPL_GZIP=y
      CONFIG_SPL_VIDEO=y
      CONFIG_SPL_SPLASH_SCREEN=y
      CONFIG_SPL_SPLASH_SOURCE=y
      CONFIG_SPL_VIDEO_TIDSS=y
      CONFIG_SPL_BMP=y
      CONFIG_SPL_BOARD_INIT=y
      CONFIG_FS_LOADER=y
      CONFIG_SPL_SYS_WHITE_ON_BLACK=y
      CONFIG_SYS_SPL_MALLOC=y
      CONFIG_SPL_BMP_24BPP=y
      CONFIG_SPL_BMP_32BPP=y
      CONFIG_SPL_SPLASH_SCREEN_ALIGN=y
      CONFIG_SPL_DM_DEVICE_REMOVE=y
      CONFIG_SPL_VIDEO_BMP_GZIP=y
      CONFIG_SPL_HIDE_LOGO_VERSION=y
      CONFIG_BLOBLIST=y

U-Boot proper config options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62PX', 'AM62LX', 'J722S')

   To enable splash screen at U-Boot proper enable following configs in :file:`configs/am62x_evm_a53_defconfig`:

   .. code-block:: kconfig

      CONFIG_DM_GPIO=y
      CONFIG_CMD_BMP=y
      CONFIG_SYSCON=y
      CONFIG_VIDEO=y
      CONFIG_SYS_WHITE_ON_BLACK=y
      CONFIG_VIDEO_TIDSS=y
      CONFIG_SPLASH_SCREEN=y
      CONFIG_SPLASH_SCREEN_ALIGN=y
      CONFIG_HIDE_LOGO_VERSION=y
      CONFIG_SPLASH_SOURCE=y
      CONFIG_VIDEO_BMP_GZIP=y
      CONFIG_BMP_24BPP=y
      CONFIG_BMP_32BPP=y
      CONFIG_BMP=y
      CONFIG_VIDEO_BMP_GZIP=y
      CONFIG_VIDEO_LOGO=y

Enable splash screen on a custom board based on |__PART_FAMILY_DEVICE_NAMES__| SoC
-----------------------------------------------------------------------------------
To enable splash screen on custom board based on |__PART_FAMILY_DEVICE_NAMES__| SoC, follow these steps:

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   1. Config fragments select the panel-specific device-tree overlays; see
      `Panel-specific config fragments`_ for details.

   2. Enable the A53 SPL splash screen related configurations. The :file:`configs/am62px_evm_a53_defconfig`
      already includes the splash screen config fragment, which enables splash screen by default.
      For custom boards, refer to the following file:

      * `Splash screen config fragment <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tree/configs/am62x_a53_splashscreen.config?h=ti-u-boot-2026.01>`_

   3. To enable different boot media for splash, define splash file locations struct in the board file
      present at :file:`board/ti/<platform>/evm.c`

      AM62PX supports two splash storage locations: SPI-NOR flash (raw at offset ``0x700000``) and
      MMC FAT filesystem, defined in :file:`board/ti/am62px/evm.c`:

      .. code-block:: c

         static struct splash_location default_splash_locations[] = {
              {
                      .name = "sf",
                      .storage = SPLASH_STORAGE_SF,
                      .flags = SPLASH_STORAGE_RAW,
                      .offset = 0x700000,
              },
              {
                      .name    = "mmc",
                      .storage = SPLASH_STORAGE_MMC,
                      .flags   = SPLASH_STORAGE_FS,
                      .devpart = "1:1",
              },
         };

   4. If a different boot media other than mmc is used for storing splash, then update the
      splash-related env variables in board.env file present at :file:`board/ti/<platform>/<platform>.env`

      The default splash environment variables for AM62PX are set in :file:`board/ti/am62px/am62px.env`:

      .. code-block:: text

         splashfile=ti_logo_414x97_32bpp.bmp.gz
         splashimage=0x80200000
         splashpos=m,m

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   1. Add video driver and panel node in the dts file by referring following patches:

      * `arm: dts: k3-am625-sk-u-boot: Add panel device-tree node  <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/commit/?h=ti-u-boot-2025.01&id=073bea998eb95d26c01e336a7b533c9e9fdbe767>`_

   2. Enable the A53 SPL splash screen related configurations in the |__PART_FAMILY_DEVICE_NAMES__| defconfig by referring to the following patches and files:

      * `configs: am62x_evm_a53_defconfig: Enable A53 splashscreen at U-Boot SPL <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/commit/?h=ti-u-boot-2025.01&id=a53de9902936442fa17b26cb17e639ecafccaa4d>`_
      * `Splash screen config fragment for AM62x and AM62P  <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tree/configs/am62x_a53_splashscreen.config?h=ti-u-boot-2025.01>`_

   3. To enable different boot media for splash, define splash file locations struct in the board file present at :file:`board/ti/<platform>/evm.c`

   4. If a different boot media other than mmc is used for storing splash, then update the splash-related env variables in board.env file present at :file:`board/ti/<platform>/<platform>.env`

.. ifconfig:: CONFIG_part_variant in ('J722S')

   1. Config fragments select the panel-specific device-tree overlays; see
      `Panel-specific config fragments`_ for details.

   2. Enable the A53 SPL splash screen related configurations. The :file:`configs/j722s_evm_a53_defconfig`
      already includes the splash screen config fragment, which enables splash screen by default.
      For custom boards, refer to the following file:

      * `Splash screen config fragment <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tree/configs/am62x_a53_splashscreen.config?h=ti-u-boot-2026.01>`_

   3. To enable different boot media for splash, define splash file locations struct in the board file
      present at :file:`board/ti/<platform>/evm.c`

      J722S supports two splash storage locations: SPI-NOR flash (raw at offset ``0x700000``) and
      MMC FAT filesystem, defined in :file:`board/ti/j722s/evm.c`:

      .. code-block:: c

         static struct splash_location default_splash_locations[] = {
              {
                      .name = "sf",
                      .storage = SPLASH_STORAGE_SF,
                      .flags = SPLASH_STORAGE_RAW,
                      .offset = 0x700000,
              },
              {
                      .name    = "mmc",
                      .storage = SPLASH_STORAGE_MMC,
                      .flags   = SPLASH_STORAGE_FS,
                      .devpart = "1:1",
              },
         };

   4. If a different boot media other than mmc is used for storing splash, then update the
      splash-related env variables in board.env file present at :file:`board/ti/<platform>/<platform>.env`

      The default splash environment variables for J722S are set in :file:`board/ti/j722s/j722s.env`:

      .. code-block:: text

         splashfile=ti_logo_414x97_32bpp.bmp.gz
         splashimage=0x80200000
         splashpos=m,m

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   1. The :file:`configs/am62lx_evm_dsi_rpi_panel.config` fragment selects the DSI panel overlay;
      see `Panel-specific config fragments`_ for details.

   2. Enable the A53 SPL splash screen related configurations. The :file:`configs/am62lx_evm_defconfig`
      does not include the splash screen config fragment by default; pass the required fragments at
      build time. For custom boards, refer to the following files:

      * `Splash screen config fragment <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tree/configs/am62x_a53_splashscreen.config?h=ti-u-boot-2026.01>`_
      * `AM62LX DSI panel config fragment <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tree/configs/am62lx_evm_dsi_rpi_panel.config?h=ti-u-boot-2026.01>`_

   3. To enable different boot media for splash, define splash file locations struct in the board file
      present at :file:`board/ti/<platform>/evm.c`

      AM62LX supports only MMC FAT filesystem as the splash storage location, defined in
      :file:`board/ti/am62lx/evm.c`:

      .. code-block:: c

         static struct splash_location default_splash_locations[] = {
              {
                      .name    = "mmc",
                      .storage = SPLASH_STORAGE_MMC,
                      .flags   = SPLASH_STORAGE_FS,
                      .devpart = "1:1",
              },
         };

   4. If a different boot media other than mmc is used for storing splash, then update the
      splash-related env variables in board.env file present at :file:`board/ti/<platform>/<platform>.env`

      The default splash environment variables for AM62LX are set in :file:`board/ti/am62lx/am62lx.env`.
      Note that AM62LX uses a different DDR load address for the splash image:

      .. code-block:: text

         splashfile=ti_logo_414x97_32bpp.bmp.gz
         splashimage=0x82200000
         splashpos=m,m

Refer section `Display custom logo as splash screen`_
to know more about splash file location struct and env variables.

Display image using U-Boot command line
---------------------------------------
To test the display and video driver in U-Boot, Run the following commands at U-Boot console:

.. code-block:: console

   #To see all the files in your boot partition run
   => ls mmc 1

   #To load image
   => fatload mmc 1 $loadaddr ti_logo_414x97_32bpp.bmp.gz

   #To display image
   =>  bmp display $loadaddr m m

This command will display an image at center of the screen.

.. code-block:: console

   #To get the BMP image info
   => bmp info

Run splash screen using OSPI NOR
--------------------------------
#. To load a BMP image on OSPI Not-OR (NOR) flash, run the following commands

   .. code-block:: console

    => sf probe
    => fatload mmc 1 $loadaddr file_name.bmp
    => sf update $loadaddr 0x700000 $filesize

#. Change ``splashsource`` to ``sf`` in board.env, recompile :file:`tispl.bin` for SPL stage and :file:`u-boot.img` for U-Boot
   proper.

.. important::

   OSPI NOR does not support displaying compressed BMP images.

Display RLE compressed image
-----------------------------
Enable the following ``Kconfig`` options to support **8-bit** RLE compressed image.

.. code-block:: kconfig

   CONFIG_SPL_VIDEO_BMP_RLE8  #for SPL splash screen
   CONFIG_VIDEO_BMP_RLE8      #for U-Boot splash screen

Flicker free display across boot stages and Linux kernel
--------------------------------------------------------

1. This SDK release supports flicker-free display across all boot stages from A53 SPL to U-Boot proper. It uses a ``bloblist`` scheme in which the Video ``Bloblist`` passes the framebuffer size and address from A53 SPL to U-Boot proper.

2. It also keeps the splash screen active while the operating system boots, with a smooth move to the Linux boot logo and then to PSplash boot animation. This uses framebuffer reservation and a simple-framebuffer approach described in the following points.

3. To keep the splash screen active while the Linux kernel boots, ti-u-boot updates the Linux device-tree with framebuffer region data and marks it as reserved. If a custom boot loader or board does not support this update, reserve the framebuffer address and size manually in the board device-tree file as shown below:

   .. code-block:: dts

        framebuffer: framebuffer@ff700000 {
             reg = <0x00 0xff700000 0x00 0x008ca000>;
             no-map;
        };

4. To move smoothly from the boot loader splash screen to the Linux boot logo and then to PSplash, enable the simple-framebuffer driver in :file:`arch/arm64/configs/defconfig`. Add a simple-framebuffer device-tree node with status disabled in the board device-tree file. ti-u-boot updates this node with framebuffer data before enabling it:

   .. code-block:: kconfig

        CONFIG_FB_SIMPLE=y

   .. ifconfig:: CONFIG_part_variant in ('AM62X')

        .. code-block:: dts

           framebuffer0: framebuffer@0 {
                compatible = "simple-framebuffer";
                power-domains = <&k3_pds 186 TI_SCI_PD_EXCLUSIVE>;
                clocks = <&k3_clks 186 6>,
                         <&dss0_vp1_clk>,
                         <&k3_clks 186 2>;
                display = <&dss>;
                status = "disabled";
           };

   .. ifconfig:: CONFIG_part_variant in ('AM62PX')

        .. code-block:: dts

           framebuffer0: framebuffer@0 {
                compatible = "simple-framebuffer";
                power-domains = <&k3_pds 186 TI_SCI_PD_EXCLUSIVE>,
                                <&k3_pds 243 TI_SCI_PD_EXCLUSIVE>,
                                <&k3_pds 244 TI_SCI_PD_EXCLUSIVE>;
                clocks = <&k3_clks 186 6>,
                         <&dss0_vp1_clk>,
                         <&k3_clks 186 2>;
                display = <&dss0>;
                status = "disabled";
           };

5. If a custom boot loader or board does not support this dynamic update, define the simple-framebuffer node manually in the board device-tree file under the chosen node.

   .. ifconfig:: CONFIG_part_variant in ('AM62X')

        .. code-block:: dts

           framebuffer0: framebuffer@0 {
                compatible = "simple-framebuffer";
                power-domains = <&k3_pds 186 TI_SCI_PD_EXCLUSIVE>;
                clocks = <&k3_clks 186 6>,
                         <&dss0_vp1_clk>,
                         <&k3_clks 186 2>;
                display = <&dss>;
                reg = <0x00 0xff700000 0x00 0x008ca000>;
                width = <1920>;
                height = <1200>;
                stride = <(1920 * 4)>;
                format = "x8r8g8b8";
           };

   .. ifconfig:: CONFIG_part_variant in ('AM62PX')

       .. code-block:: dts

          framebuffer0: framebuffer@0 {
                compatible = "simple-framebuffer";
                power-domains = <&k3_pds 186 TI_SCI_PD_EXCLUSIVE>,
                                <&k3_pds 243 TI_SCI_PD_EXCLUSIVE>,
                                <&k3_pds 244 TI_SCI_PD_EXCLUSIVE>;
                clocks = <&k3_clks 186 6>,
                         <&dss0_vp1_clk>,
                         <&k3_clks 186 2>;
                display = <&dss0>;
                reg = <0x00 0xff700000 0x00 0x008ca000>;
                width = <1920>;
                height = <1200>;
                stride = <(1920 * 4)>;
                format = "x8r8g8b8";
           };

6. This scheme lets the Linux kernel reuse the boot loader framebuffer for the boot logo and animation before it loads the display driver, giving a smooth handoff.

.. note::

   For more on simple-framebuffer, see the `simple-framebuffer device-tree binding doc <https://github.com/torvalds/linux/blob/master/Documentation/devicetree/bindings/display/simple-framebuffer.yaml>`_.
   Even if a non-Linux boot loader shows the splash screen before moving to Linux, update the framebuffer data in the device-tree nodes listed earlier. This gives a flicker-free display during operating system boot and reduces memory use.


Flicker free and persistent display until display server
--------------------------------------------------------

To keep the boot animation active until the display server starts, disable the Direct Rendering Manager (DRM) "framebuffer device emulation" feature in :file:`arch/arm64/configs/defconfig`. This feature disables the simple-framebuffer region and resets the display hardware before it takes over.

.. code-block:: kconfig

   # CONFIG_DRM_FBDEV_EMULATION is not set

.. note::

   The SDK enables this option by default. Disable it manually if you need an active splash screen and do not use the DRM ``fbdev`` emulation feature.

Panel-specific config fragments
-------------------------------

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   The |__PART_FAMILY_DEVICE_NAMES__| supports only the OLDI Microtips MF101HIE panel. The panel
   configuration is included directly in :file:`arch/arm/dts/k3-am625-sk-u-boot.dtsi` and does not
   require a separate config fragment.

   .. list-table::
      :header-rows: 1
      :widths: 35 65

      * - Panel
        - Config fragments required
      * - OLDI Microtips MF101HIE
        - None (panel included in :file:`arch/arm/dts/k3-am625-sk-u-boot.dtsi`)

.. ifconfig:: CONFIG_part_variant in ('AM62LX', 'AM62PX', 'J722S')

   In addition to the base :file:`configs/am62x_a53_splashscreen.config`, pass panel-specific config
   fragments to select the correct device-tree overlay and display pipeline drivers.

   .. ifconfig:: CONFIG_part_variant in ('AM62PX')

      .. list-table::
         :header-rows: 1
         :widths: 35 65

         * - Panel
           - Config fragments required
         * - OLDI Microtips MF101HIE
           - :file:`configs/am62p5_j722s_evm_oldi-microtips-mf101hie-panel.config`
         * - DSI Raspberry Pi 7-inch
           - :file:`configs/k3_a53_dsi.config` :file:`configs/am62p5_evm_dsi_rpi_panel.config`

   .. ifconfig:: CONFIG_part_variant in ('J722S')

      .. list-table::
         :header-rows: 1
         :widths: 35 65

         * - Panel
           - Config fragments required
         * - OLDI Microtips MF101HIE
           - :file:`configs/am62p5_j722s_evm_oldi-microtips-mf101hie-panel.config`
         * - DSI Raspberry Pi 7-inch
           - :file:`configs/k3_a53_dsi.config` :file:`configs/j722s_evm_dsi_rpi_panel.config`
         * - eDP
           - :file:`configs/k3_a53_dsi.config` :file:`configs/j722s_evm_a53_edp.config`

   .. ifconfig:: CONFIG_part_variant in ('AM62LX')

      .. list-table::
         :header-rows: 1
         :widths: 35 65

         * - Panel
           - Config fragments required
         * - DSI Raspberry Pi 7-inch
           - :file:`configs/am62x_a53_splashscreen.config` :file:`configs/k3_a53_dsi.config` :file:`configs/am62lx_evm_dsi_rpi_panel.config`

Build U-Boot with splash screen enabled
---------------------------------------

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   :file:`configs/am62x_evm_a53_defconfig` already includes :file:`configs/am62x_a53_splashscreen.config`,
   so a standard A53 build has splash screen with the OLDI panel enabled:

   .. code-block:: console

      $ export UBOOT_DIR=<path_to_ti_u_boot>
      $ export TI_LINUX_FW_DIR=<path_to_ti_linux_firmware>
      $ export TFA_DIR=<path_to_arm_trusted_firmware>
      $ export OPTEE_DIR=<path_to_ti_optee_os>
      $ cd $UBOOT_DIR

      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" am62x_evm_a53_defconfig O=$UBOOT_DIR/out/a53
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" CC="$CC_64" BL31=$TFA_DIR/build/k3/lite/release/bl31.bin TEE=$OPTEE_DIR/out/arm-plat-k3/core/tee-pager_v2.bin O=$UBOOT_DIR/out/a53 BINMAN_INDIRS=$TI_LINUX_FW_DIR

.. ifconfig:: CONFIG_part_variant in ('AM62LX', 'AM62PX', 'J722S')

   The splash screen is enabled by passing the appropriate config fragment(s) alongside the platform
   defconfig at the ``make`` configuration step. The second ``make`` invocation compiles the binaries.

   .. ifconfig:: CONFIG_part_variant in ('AM62PX')

      :file:`configs/am62px_evm_a53_defconfig` already includes :file:`configs/am62x_a53_splashscreen.config`,
      so a standard A53 build has splash screen enabled. To use a specific panel, apply the corresponding
      config fragment:

      .. code-block:: console

         $ export UBOOT_DIR=<path_to_ti_u_boot>
         $ export TI_LINUX_FW_DIR=<path_to_ti_linux_firmware>
         $ export TFA_DIR=<path_to_arm_trusted_firmware>
         $ export OPTEE_DIR=<path_to_ti_optee_os>
         $ cd $UBOOT_DIR

         # OLDI panel
         $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" am62px_evm_a53_defconfig am62p5_j722s_evm_oldi-microtips-mf101hie-panel.config O=$UBOOT_DIR/out/a53
         $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" CC="$CC_64" BL31=$TFA_DIR/build/k3/lite/release/bl31.bin TEE=$OPTEE_DIR/out/arm-plat-k3/core/tee-pager_v2.bin O=$UBOOT_DIR/out/a53 BINMAN_INDIRS=$TI_LINUX_FW_DIR

         # DSI Raspberry Pi 7-inch panel
         $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" am62px_evm_a53_defconfig k3_a53_dsi.config am62p5_evm_dsi_rpi_panel.config O=$UBOOT_DIR/out/a53
         $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" CC="$CC_64" BL31=$TFA_DIR/build/k3/lite/release/bl31.bin TEE=$OPTEE_DIR/out/arm-plat-k3/core/tee-pager_v2.bin O=$UBOOT_DIR/out/a53 BINMAN_INDIRS=$TI_LINUX_FW_DIR

   .. ifconfig:: CONFIG_part_variant in ('J722S')

      :file:`configs/j722s_evm_a53_defconfig` already includes :file:`configs/am62x_a53_splashscreen.config`,
      so a standard A53 build has splash screen enabled. To use a specific panel, apply the corresponding
      config fragment:

      .. code-block:: console

         $ export UBOOT_DIR=<path_to_ti_u_boot>
         $ export TI_LINUX_FW_DIR=<path_to_ti_linux_firmware>
         $ export TFA_DIR=<path_to_arm_trusted_firmware>
         $ export OPTEE_DIR=<path_to_ti_optee_os>
         $ cd $UBOOT_DIR

         # OLDI panel
         $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" j722s_evm_a53_defconfig am62p5_j722s_evm_oldi-microtips-mf101hie-panel.config O=$UBOOT_DIR/out/a53
         $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" CC="$CC_64" BL31=$TFA_DIR/build/k3/lite/release/bl31.bin TEE=$OPTEE_DIR/out/arm-plat-k3/core/tee-pager_v2.bin O=$UBOOT_DIR/out/a53 BINMAN_INDIRS=$TI_LINUX_FW_DIR

         # DSI Raspberry Pi 7-inch panel
         $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" j722s_evm_a53_defconfig k3_a53_dsi.config j722s_evm_dsi_rpi_panel.config O=$UBOOT_DIR/out/a53
         $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" CC="$CC_64" BL31=$TFA_DIR/build/k3/lite/release/bl31.bin TEE=$OPTEE_DIR/out/arm-plat-k3/core/tee-pager_v2.bin O=$UBOOT_DIR/out/a53 BINMAN_INDIRS=$TI_LINUX_FW_DIR

         # eDP
         $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" j722s_evm_a53_defconfig k3_a53_dsi.config j722s_evm_a53_edp.config O=$UBOOT_DIR/out/a53
         $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" CC="$CC_64" BL31=$TFA_DIR/build/k3/lite/release/bl31.bin TEE=$OPTEE_DIR/out/arm-plat-k3/core/tee-pager_v2.bin O=$UBOOT_DIR/out/a53 BINMAN_INDIRS=$TI_LINUX_FW_DIR

   .. ifconfig:: CONFIG_part_variant in ('AM62LX')

      AM62LX does not include splash screen configs in the base defconfig. All required config
      fragments must be passed explicitly alongside the defconfig:

      .. code-block:: console

         $ export UBOOT_DIR=<path_to_ti_u_boot>
         $ export TI_LINUX_FW_DIR=<path_to_ti_linux_firmware>
         $ export TFA_DIR=<path_to_arm_trusted_firmware>
         $ export OPTEE_DIR=<path_to_ti_optee_os>
         $ cd $UBOOT_DIR

         # DSI Raspberry Pi 7-inch panel
         $ make CROSS_COMPILE="$CROSS_COMPILE_64" am62lx_evm_defconfig am62x_a53_splashscreen.config k3_a53_dsi.config am62lx_evm_dsi_rpi_panel.config O=$UBOOT_DIR/out
         $ make CROSS_COMPILE="$CROSS_COMPILE_64" \
              BL1=$TFA_DIR/build/k3low/am62lx/release/bl1.bin \
              BL31=$TFA_DIR/build/k3low/am62lx/release/bl31.bin \
              BINMAN_INDIRS=$TI_LINUX_FW_DIR \
              TEE=$OPTEE_DIR/out/arm-plat-k3/core/tee-pager_v2.bin \
              O=$UBOOT_DIR/out

      .. warning::

         When U-Boot splash screen is enabled on |__PART_FAMILY_DEVICE_NAMES__|, Linux boot will
         hang unless the display pipeline drivers are built into the kernel (``=y``) rather than
         compiled as modules (``=m``). Modules are loaded too late in the boot sequence to take
         over the display handed off by U-Boot.

         Apply the following changes to :file:`arch/arm64/configs/defconfig` in Linux:

         .. code-block:: kconfig

            CONFIG_REGULATOR_RASPBERRYPI_TOUCHSCREEN_ATTINY=y
            CONFIG_DRM=y
            CONFIG_DRM_PANEL_SIMPLE=y
            CONFIG_DRM_SIMPLE_BRIDGE=y
            CONFIG_DRM_TOSHIBA_TC358762=y
            CONFIG_DRM_CDNS_DSI=y
            CONFIG_DRM_TIDSS=y
            CONFIG_PHY_CADENCE_DPHY=y

Disable splash screen
---------------------

To disable splash screen use `configs/am62x_evm_prune_splashscreen.config <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tree/configs/am62x_evm_prune_splashscreen.config?h=ti-u-boot-2025.01>`__ fragment while building u-boot with the corresponding a53 ``defconfig``.
