.. _Uboot-splash-label:

====================
U-Boot Splash Screen
====================
A splash screen is an introductory screen the user sees over the display when the device boots up.
Splash screens are typically used to provide feedback to the user that the board is booting up and
to showcase the vendor logo which helps with branding and identification of which boot
image is being used for the bootup.

The |__PART_FAMILY_DEVICE_NAMES__| offers out-of-box splash screen experience with OLDI display.
It also supports displaying a splash screen until kernel is booted up with flicker-free transition across different boot stages.

------------------
Features supported
------------------
The following features are supported for splash screen in U-Boot:

#. Supports 32, 24, and 8 bits per pixel BMP image.
#. Supports frame buffer of size 1920x1200 resolution, images with a resolution lesser than this can
   still be displayed using the same frame buffer.
#. Supports displaying only BMP and compressed BMP images(gzip and 8bit RLE).
#. Supports MMC and OSPI as bmp image sources.
#. Supports splash screen only on OLDI panel.

The |__PART_FAMILY_DEVICE_NAMES__| supports splash screen at both U-Boot proper and A53 SPL with A53 SPL displaying
splash screen **~1.4 seconds** earlier than U-Boot proper.

Enabling the splash screen on ti-u-boot
---------------------------------------
In this SDK release ti-u-boot supports a splash screen at both A53 SPL stage and U-Boot proper.

A53 SPL
^^^^^^^
By default the splash screen is only enabled at A53 SPL. The default splash source is set to SD card and
displays a gzip TI logo BMP Image. The SPL splash screen features are compiled in the tispl.bin
which is built during u-boot compilation. Any changes made to SPL splash screen feature will require
recompiling tispl.bin. Use the new tispl.bin to boot the board to see splash screen at SPL stage.

At the SPL stage, the splash screen display function is called from :file:`board/ti/<platform>/evm.c` in ``function spl_board_init``

.. code-block:: c

   video_setup();
   enable_caches();
   if (IS_ENABLED(CONFIG_SPL_SPLASH_SCREEN) && IS_ENABLED(CONFIG_SPL_BMP))
       splash_display();

U-Boot proper
^^^^^^^^^^^^^

To enable the splash screen at U-Boot proper enable the following configs in :file:`configs/<platform>_a53_defconfig`.

.. code-block:: kconfig

   CONFIG_SPLASH_SCREEN=y
   CONFIG_SPLASH_SOURCE=y
   CONFIG_SPLASH_SCREEN_ALIGN=y
   CONFIG_HIDE_LOGO_VERSION=y

If the user only wants the splash screen feature at U-Boot proper, the user can disable the splash screen at A53 SPL
by disabling the kconfig **CONFIG_SPL_VIDEO**.

.. code-block:: kconfig

   # CONFIG_SPL_VIDEO=y

The splash screen feature at U-Boot proper gets compiled in :file:`u-boot.img`, which is built during U-Boot
compilation. Any changes made to U-Boot splash screen feature will require the recompilation of :file:`u-boot.img`.
User should use the recompiled u-boot.img to boot the board, to see splash screen at U-Boot proper.

.. note::
   * If splash screen is enabled at U-Boot proper it will stay persistent until linux boot starts.

.. _Display custom logo as splash screen:

Display custom logo as splash screen
------------------------------------
#. In U-Boot all information for the image to be displayed as splash screen is passed through environment variables,
   defined below. These should be added in the .env file used by the board under :file:`board/ti/<platform>.env`.
   For reference, :file:`board/ti/am62x.env` is shown below :

   .. code-block:: bash

      #Name of file to be displayed
      splashfile=ti_logo_414x97_32bpp.bmp.gz

      #DDR address to load image from boot media
      splashimage=0x80200000

      #Position of image on display
      splashpos=m,m

      #Source of bmp image
      splashsource=mmc

#. To display a custom logo change the **splashfile** variable to logo_file_name.

#. If using an SD card as splash source, place the image in the boot partition of SD card which contains
   :file:`tispl.bin` and :file:`u-boot.img`.

#. To display image from a different source, add the source information in struct
   default_splash_locations, which is defined in :file:`board/ti/<platform>/evm.c`.
   For example in :file:`board/ti/am62x/evm.c`, by default OSPI and SD card are added as sources as shown below :

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

#. Change **splashsource** variable to the name of the source defined in above struct.

.. important::
   :file:`<platform>.env` file gets compiled into :file:`u-boot.img` and :file:`tispl.bin` for U-Boot proper and A53 SPL respectively,
   any changes made in .env will require the recompilation of :file:`u-boot.img` and :file:`tispl.bin` depending on the stage splash screen is enabled.

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   Enabling splash screen on upstream U-Boot
   -----------------------------------------
   In upstream, the splash screen is supported at the driver level for both A53 SPL and U-Boot proper.

   However, user needs to enable the required kconfigs and device-tree nodes manually, The below commit can be used as
   a reference for making such changes.

   * `arm: dts: k3-am625-sk-u-boot: Add panel device-tree node  <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/commit/?h=ti-u-boot-2025.01&id=073bea998eb95d26c01e336a7b533c9e9fdbe767>`_

   A53 SPL
   ^^^^^^^
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

   U-Boot proper
   ^^^^^^^^^^^^^
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

Enabling splash screen on custom board based on |__PART_FAMILY_DEVICE_NAMES__| SoC
-----------------------------------------------------------------------------------
To enable splash screen on custom board based on |__PART_FAMILY_DEVICE_NAMES__| SoC, follow the below steps:

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

 1. Add video driver and panel node in the dts file by referring following patches:

  * `arm: dts: k3-am62p5-sk-u-boot: Add panel device-tree node <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/commit/?h=ti-u-boot-2026.01&id=1cdea8def9297ae52c6434146d4909c330a212f2>`_

.. ifconfig:: CONFIG_part_variant in ('AM62X')

 1. Add video driver and panel node in the dts file by referring following patches:

  * `arm: dts: k3-am625-sk-u-boot: Add panel device-tree node  <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/commit/?h=ti-u-boot-2025.01&id=073bea998eb95d26c01e336a7b533c9e9fdbe767>`_

.. ifconfig:: CONFIG_part_variant in ('J722S')

 1. Add video driver and panel node in the dts file. Panel-specific device-tree overlays are
    selected via config fragments — see `Panel-specific config fragments`_ for details.

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

 1. Add video driver and panel node in the dts file. The DSI panel overlay is selected via the
    :file:`configs/am62lx_evm_dsi_rpi_panel.config` fragment — see `Panel-specific config fragments`_ for details.

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

 2. Enable the A53 SPL splash screen related configurations in the |__PART_FAMILY_DEVICE_NAMES__| defconfig by referring to below patches and files:

  * `configs: am62px: Enable A53 splashscreen <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/commit/?h=ti-u-boot-2026.01&id=4dacc20b3fd78ac5f61de8096a376afb2fcfd089>`_
  * `Splash screen config fragment for AM62x and AM62P  <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tree/configs/am62x_a53_splashscreen.config?h=ti-u-boot-2026.01>`_

.. ifconfig:: CONFIG_part_variant in ('AM62X')

 2. Enable the A53 SPL splash screen related configurations in the |__PART_FAMILY_DEVICE_NAMES__| defconfig by referring to below patches and files:

  * `configs: am62x_evm_a53_defconfig: Enable A53 splashscreen at U-Boot SPL <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/commit/?h=ti-u-boot-2025.01&id=a53de9902936442fa17b26cb17e639ecafccaa4d>`_
  * `Splash screen config fragment for AM62x and AM62P  <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tree/configs/am62x_a53_splashscreen.config?h=ti-u-boot-2025.01>`_

.. ifconfig:: CONFIG_part_variant in ('J722S')

 2. Enable the A53 SPL splash screen related configurations. The :file:`configs/j722s_evm_a53_defconfig`
    already includes :file:`configs/am62x_a53_splashscreen.config` so splash screen is enabled by default.
    For custom boards, refer to the following file:

  * `Splash screen config fragment <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tree/configs/am62x_a53_splashscreen.config?h=ti-u-boot-2026.01>`_

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

 2. Enable the A53 SPL splash screen related configurations by passing all required config fragments
    at build time. For custom boards, refer to the following files:

  * `Splash screen config fragment <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tree/configs/am62x_a53_splashscreen.config?h=ti-u-boot-2026.01>`_
  * `AM62LX DSI panel config fragment <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tree/configs/am62lx_evm_dsi_rpi_panel.config?h=ti-u-boot-2026.01>`_

.. note::

   To enable the splash screen at U-Boot proper instead of A53 SPL, enable the following configs in :file:`configs/am62x_a53_splashscreen.config`

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

3. To enable different boot media for splash, define splash file locations struct in the board file present at :file:`board/ti/<platform>/evm.c`

.. ifconfig:: CONFIG_part_variant in ('J722S')

   J722S supports two splash storage locations: SPI-NOR flash (raw at offset ``0x700000``) and
   MMC FAT filesystem. These are defined in :file:`board/ti/j722s/evm.c`:

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

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   AM62LX supports MMC FAT filesystem as the splash storage location. Only MMC is supported
   as a splash source. This is defined in :file:`board/ti/am62lx/evm.c`:

   .. code-block:: c

      static struct splash_location default_splash_locations[] = {
           {
                   .name    = "mmc",
                   .storage = SPLASH_STORAGE_MMC,
                   .flags   = SPLASH_STORAGE_FS,
                   .devpart = "1:1",
           },
      };

4. If a different boot media other than mmc is used for storing splash, then update the splash-related env variables in board.env file present at :file:`board/ti/<platform>/<platform>.env`

.. ifconfig:: CONFIG_part_variant in ('J722S')

   The default splash environment variables for J722S are set in :file:`board/ti/j722s/j722s.env`:

   .. code-block:: bash

      splashfile=ti_logo_414x97_32bpp.bmp.gz
      splashimage=0x80200000
      splashpos=m,m
      splashsource=mmc

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   The default splash environment variables for AM62LX are set in :file:`board/ti/am62lx/am62lx.env`.
   Note that AM62LX uses a different DDR load address for the splash image:

   .. code-block:: bash

      splashfile=ti_logo_414x97_32bpp.bmp.gz
      splashimage=0x82200000
      splashpos=m,m
      splashsource=mmc

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

The above command will display an image at centre of the screen.

.. code-block:: console

   #To get the BMP image info
   => bmp info

Run splash screen using OSPI NOR
--------------------------------
#. To load bmp image on OSPI NOR run the following commands

   .. code-block:: console

    => sf probe
    => fatload mmc 1 $loadaddr file_name.bmp
    => sf update $loadaddr 0x700000 $filesize

#. Change splashsource to sf in board.env, recompile :file:`tispl.bin` for SPL stage and :file:`u-boot.img` for U-Boot
   proper.

.. important::
   OSPI NOR doesn't support displaying gzip bmp image.

Display RLE compressed image
-----------------------------
Enable the following kconfigs to support **8bit** RLE compressed image.

.. code-block:: kconfig

   CONFIG_SPL_VIDEO_BMP_RLE8  #for SPL splash screen
   CONFIG_VIDEO_BMP_RLE8      #for U-Boot splash screen

Flicker free display across boot stages and Linux Kernel
--------------------------------------------------------

1. This SDK release supports flicker-free display with splash screen displayed persistently across all the bootloader stages starting from A53 SPL to U-Boot proper using a bloblist-based scheme, where framebuffer related information like size of framebuffer, address of framebuffer are passed from A53 SPL to U-Boot proper using Video Bloblist.

2. It also supports persistent splash screen display while the operating system is booting up, along with the seamless transition to Linux Boot logo and thereafter to PSplash boot animation using framebuffer reservation and simple-framebuffer based approach as described in the following points.

3. To make sure that the splash screen remains persistent while Linux Kernel boots up, ti-u-boot dynamically updates the Linux kernel device-tree with framebuffer region meta-data, marking it as reserved in Linux device tree. In case a custom bootloader or a different board is used which doesn't support the aforementioned dynamic node update for reserving framebuffer region, then frame-buffer address and size can be manually reserved in board-specific device-tree file as shown below :

   .. code-block:: dts

        framebuffer: framebuffer@ff700000 {
             reg = <0x00 0xff700000 0x00 0x008ca000>;
             no-map;
        };

4. To enable the seamless transition from bootloader splash screen to Linux boot logo and thereafter to PSplash based boot animation, simple-framebuffer driver was enabled in :file:`arch/arm64/configs/defconfig`. A simple-framebuffer device-tree node with status as disabled was created in board specific device-tree file as shown below and ti-u-boot dynamically updates this node with framebuffer related meta-data before enabling it.  :

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

5. In case a custom bootloader or a different board is used that doesn't support the aforementioned dynamic node update, then the simple-framebuffer node can be defined manually in the board device-tree file under the chosen node as shown below :

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

6. The above scheme also ensures that the bootloader allocated framebuffer region is re-used by Linux kernel for displaying the boot logo and animation even before Linux kernel loads the display driver, thus giving a seamless experience during transition.

.. note::

   More information regarding simple-framebuffer can be found in `the simple-framebuffer device-tree binding doc <https://github.com/torvalds/linux/blob/master/Documentation/devicetree/bindings/display/simple-framebuffer.yaml>`_
   Even if a non-Linux based custom bootloader is used to display the splash screen before transitioning to Linux, the framebuffer-related information can be updated in aforementioned device-tree nodes to enable seamless and flicker-free transition during operating system bootup along with reduced memory footprint.


Flicker free and persistent display until display server
--------------------------------------------------------
If the user wants to keep the boot animation alive until the display server starts up, then they need to manually disable "DRM framebuffer device emulation" feature in :file:`arch/arm64/configs/defconfig`. This is required since the framebuffer emulation feature disables the simple-framebuffer region and resets the display hardware before taking control of the display.

.. code-block:: kconfig

   # CONFIG_DRM_FBDEV_EMULATION is not set

.. note::

   The above option is enabled by default in the SDK, The user will need to disable it manually if they desire a persistent splash screen and they are not using the DRM fbdev emulation feature.

.. _Panel-specific config fragments:

Panel-specific config fragments
--------------------------------
In addition to the base :file:`configs/am62x_a53_splashscreen.config`, panel-specific config
fragments must be applied to select the correct device-tree overlay and display pipeline drivers.

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

.. _Building U-Boot with splash screen enabled:

Building U-Boot with splash screen enabled
------------------------------------------
The splash screen is enabled by passing the appropriate config fragment(s) alongside the platform
defconfig at the ``make`` configuration step. The second ``make`` invocation compiles the binaries.

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   :file:`configs/am62px_evm_a53_defconfig` already includes :file:`configs/am62x_a53_splashscreen.config`,
   so a standard A53 build has splash screen enabled. To use a specific panel, apply the corresponding
   config fragment:

   .. code-block:: console

      $ export UBOOT_DIR=<path-to-ti-u-boot>
      $ export TI_LINUX_FW_DIR=<path-to-ti-linux-firmware>
      $ export TFA_DIR=<path-to-arm-trusted-firmware>
      $ export OPTEE_DIR=<path-to-ti-optee-os>
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

      $ export UBOOT_DIR=<path-to-ti-u-boot>
      $ export TI_LINUX_FW_DIR=<path-to-ti-linux-firmware>
      $ export TFA_DIR=<path-to-arm-trusted-firmware>
      $ export OPTEE_DIR=<path-to-ti-optee-os>
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

      $ export UBOOT_DIR=<path-to-ti-u-boot>
      $ export TI_LINUX_FW_DIR=<path-to-ti-linux-firmware>
      $ export TFA_DIR=<path-to-arm-trusted-firmware>
      $ export OPTEE_DIR=<path-to-ti-optee-os>
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

Disabling splash screen
-----------------------
To disable splash screen use `configs/am62x_evm_prune_splashscreen.config <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tree/configs/am62x_evm_prune_splashscreen.config?h=ti-u-boot-2025.01>`__ fragment while building u-boot with corresponding a53 defconfig.
