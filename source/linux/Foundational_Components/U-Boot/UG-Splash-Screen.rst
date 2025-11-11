.. _Uboot-splash-label:

====================
U-Boot Splash Screen
====================
A splash screen is an introductory screen the user sees over the display when the device boots up.
Splash screens are typically used to provide feedback to the user that the board is booting up and
to showcase the vendor logo which helps with branding and identification of which boot
image is being used for the bootup.

The |__PART_FAMILY_NAME__| offers out-of-box splash screen experience with OLDI display.
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

The |__PART_FAMILY_NAME__| supports splash screen at both U-Boot proper and A53 SPL with A53 SPL displaying
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

Enabling splash screen on custom board based on |__PART_FAMILY_NAME__| SoC
-----------------------------------------------------------------------------------
To enable splash screen on custom board based on |__PART_FAMILY_NAME__| SoC, follow the below steps:

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

 1. Add video driver and panel node in the dts file by referring following patches:

  * `arm: dts: k3-am62p5-sk-u-boot: Add panel device-tree node <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/commit/?h=ti-u-boot-2025.01&id=1cdea8def9297ae52c6434146d4909c330a212f2>`_

.. ifconfig:: CONFIG_part_variant in ('AM62X')

 1. Add video driver and panel node in the dts file by referring following patches:

  * `arm: dts: k3-am625-sk-u-boot: Add panel device-tree node  <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/commit/?h=ti-u-boot-2025.01&id=073bea998eb95d26c01e336a7b533c9e9fdbe767>`_

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

 2. Enable the A53 SPL splash screen related configurations in the |__PART_FAMILY_NAME__| defconfig by referring to below patches and files:

  * `configs: am62px: Enable A53 splashscreen <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/commit/?h=ti-u-boot-2025.01&id=4dacc20b3fd78ac5f61de8096a376afb2fcfd089>`_
  * `Splash screen config fragment for AM62x and AM62P  <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tree/configs/am62x_a53_splashscreen.config?h=11.00.09>`_

.. ifconfig:: CONFIG_part_variant in ('AM62X')

 2. Enable the A53 SPL splash screen related configurations in the |__PART_FAMILY_NAME__| defconfig by referring to below patches and files:

  * `configs: am62x_evm_a53_defconfig: Enable A53 splashscreen at U-Boot SPL <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/commit/?h=ti-u-boot-2025.01&id=a53de9902936442fa17b26cb17e639ecafccaa4d>`_
  * `Splash screen config fragment for AM62x and AM62P  <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tree/configs/am62x_a53_splashscreen.config?h=11.00.09>`_

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
4. If a different boot media other than mmc is used for storing splash, then update the splash-related env variables in board.env file present at :file:`board/ti/<platform>/<platform>.env`

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

Disabling splash screen
-----------------------
To disable splash screen use `configs/am62x_evm_prune_splashscreen.config <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tree/configs/am62x_evm_prune_splashscreen.config?h=ti-u-boot-2025.01>`__ fragment while building u-boot with corresponding a53 defconfig.
