
U-Boot Splash Screen
==========================

.. rubric:: Adding a splash screen
   :name: adding-a-splash-screen

.. rubric:: AM335x
   :name: am335x

A splash screen is an introductory screen the user sees over the display when the device boots up. Splash screens are typically used to provide feedback to the user that the board is booting up and to showcase
the vendor logo, which helps with branding and identification of which boot image is used for the bootup.
All the code related to u-boot splash screen support is based on Processor Linux SDK 09.03.05.02.

For AM335x, the splash screen is enabled in u-boot which uses the LCDC driver.
On AM335x EVM, the LCD backlight is controlled using enhanced Auxiliary(eCAP0) PWM.
Enable the following configurations in :file:`configs/am335x_evm_defconfig` to use this.

.. code-block:: kconfig

   CONFIG_SPLASH_SCREEN=y
   CONFIG_SPLASH_SOURCE=y
   CONFIG_SPLASH_SCREEN_ALIGN=y
   CONFIG_HIDE_LOGO_VERSION=y
   CONFIG_AM335X_LCD=y
   CONFIG_VIDEO_BMP_GZIP=y
   CONFIG_BMP_24BPP=y
   CONFIG_BMP_32BPP=y
   CONFIG_BMP=y
   CONFIG_VIDEO=y
   CONFIG_CMD_BMP=y
   CONFIG_SYSCON=y
   CONFIG_REGMAP=y
   CONFIG_CLK_CCF=y
   CONFIG_CLK_TI_AM3_DPLL=y
   CONFIG_CLK_TI_DIVIDER=y
   CONFIG_CLK_TI_MUX=y
   CONFIG_DM_PWM=y
   CONFIG_BACKLIGHT_PWM=y
   CONFIG_PWM_TI_ECAP=y

If the user is using enhanced High Resolution PWM(eHRPWM) to control the display backlight,
enable the following config.


.. code-block:: kconfig

   CONFIG_CLK_TI_GATE=y

.. rubric:: Features supported

The following features are supported and validated on am335x EVM:

#. Supports 32, 24, and 8 bits per pixel BMP image.
#. Supports displaying only BMP and compressed BMP images(gzip).
#. Supports MMC as bmp image sources.

.. rubric:: Display Image using U-Boot command line
   :name: Display Image

To test the display and video driver in U-Boot, run the following commands at the U-Boot console:

.. code-block:: console

   #To see all the files in your boot partition, run
   => ls mmc 0

   #To load the image
   => fatload mmc 0 $loadaddr ti_logo_414x97_32bpp.bmp.gz

   #To display the image
   =>  bmp display $loadaddr m m

The above command will display an image at the center of the screen as shown below.

.. Image:: /images/AM335x_evm_uboot_splash_screen.jpg
   :width: 600

User can use the custom image to display the splash screen.

.. code-block:: console

   #To get the BMP image info
   => bmp info

