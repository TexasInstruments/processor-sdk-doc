
.. _fitImage-for-HS:

Creating the kernel fitImage for high security device / GP devices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SDKs have pre-built FIT images that contain the default Kernel and DTB files.
But developers may want to deploy and test new Kernel and DTB without going
through the standard build system. For the specific purpose, board specific
fitImage.its will be present in the prebuilt-images directory.

.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family', 'AM57X_family')

   Pre-requisites ( Already part of SDK installations ):

   - Uboot build directory for ARMV7
   - Linux Image and DTB

.. ifconfig:: CONFIG_part_family not in ('AM335X_family', 'AM437X_family', 'AM57X_family')

   Pre-requisites ( Already part of SDK installations ):

   - Uboot build directory for ARMV8
   - Linux Image and DTB

.. note::

   GP/HS-FS devices will also enforce authentication if booting fitImage. To
   disable authentication enforcement, FIT_SIGNATURE_ENFORCE needs to be
   disabled in defconfig for the specific board during uboot build.

Describing FIT source
"""""""""""""""""""""

FIT Image is a packed structure containing binary blobs and configurations.
The Kernel FIT image that we have has Kernel Image, DTB and the DTBOs.

.. ifconfig:: CONFIG_part_family not in ('AM335X_family', 'AM437X_family', 'AM57X_family')

   .. code-block:: dts

      kernel-1 {
         description = "Linux kernel";
         data = /incbin/("linux.bin");
         type = "kernel";
         arch = "arm64";
         os = "linux";
         compression = "gzip";
         load = <0x81000000>;
         entry = <0x81000000>;
         hash-1 {
            algo = "sha512";
         };
      };

      fdt-ti_k3-j721e-common-proc-board.dtb {
         description = "Flattened Device Tree blob";
         data = /incbin/("arch/arm64/boot/dts/ti/k3-j721e-common-proc-board.dtb");
         type = "flat_dt";
         arch = "arm64";
         compression = "none";
         load = <0x83000000>;
         hash-1 {
            algo = "sha512";
         };
      };

      fdt-ti_k3-j721e-evm-virt-mac-client.dtbo {
         description = "Flattened Device Tree blob";
         data = /incbin/("arch/arm64/boot/dts/ti/k3-j721e-evm-virt-mac-client.dtbo");
         type = "flat_dt";
         arch = "arm64";
         compression = "none";
         load = <0x83080000>;
         hash-1 {
            algo = "sha512";
         };
      };

.. ifconfig:: CONFIG_part_family in ('AM57X_family')

   .. code-block:: dts

      kernel-1 {
         description = "Linux kernel";
         data = /incbin/("linux.bin.sec");
         type = "kernel";
         arch = "arm";
         os = "linux";
         compression = "none";
         load = <0x82000000>;
         entry = <0x82000000>;
      };

      am5729-beagleboneai.dtb {
         description = "Flattened Device Tree blob";
         data = /incbin/("arch/arm/boot/dts/am5729-beagleboneai.dtb.sec");
         type = "flat_dt";
         arch = "arm";
         compression = "none";
      };

      am57xx-beagle-x15.dtb {
         description = "Flattened Device Tree blob";
         data = /incbin/("arch/arm/boot/dts/am57xx-beagle-x15.dtb.sec");
         type = "flat_dt";
         arch = "arm";
         compression = "none";
      };

Change the path in data variables to point to the respective files in your
local machine.

For e.g change "linux.bin" to
:file:`<path-to-tisdk>/board-support/prebuilt-images/Image`.

.. ifconfig:: CONFIG_part_family not in ('AM335X_family', 'AM437X_family', 'AM57X_family')

   The new addition to the FIT from 8.6 to 9.0 is the FIT Signature.

   .. code-block:: dts

      conf-ti_k3-j721e-common-proc-board.dtb {
         description = "Linux kernel, FDT blob";
         fdt = "fdt-ti_k3-j721e-common-proc-board.dtb";
         kernel = "kernel-1";
         signature-1 {
            algo = "sha512,rsa4096";
            key-name-hint = "custMpk";
            sign-images = "kernel", "fdt";
         };
      };


   Specify all images you need the signature to authenticate as a part of
   sign-images. The key-name-hint needs to be changed if you are using some
   other key other than the TI dummy key that we are using for this example.
   It should be the name of the file containing the keys.

   .. note::

      Generating new set of keys:

      .. code-block:: console

         $ mkdir keys
         $ openssl genpkey -algorithm RSA -out keys/dev.key \
          -pkeyopt rsa_keygen_bits:4096 -pkeyopt rsa_keygen_pubexp:65537
         $ openssl req -batch -new -x509 -key keys/dev.key -out keys/dev.crt

Generating the fitImage
^^^^^^^^^^^^^^^^^^^^^^^

.. ifconfig:: CONFIG_part_family not in ('AM335X_family', 'AM437X_family', 'AM57X_family')

   .. note::

      For signing a secondary platform like SK boards, you'll require
      additional steps

   Change the CONFIG_DEFAULT_DEVICE_TREE and binman nodes to package :file:`u-boot.dtb`.

   For e.g

   .. code-block:: diff

      diff --git a/configs/j721e_evm_a72_defconfig b/configs/j721e_evm_a72_defconfig
      index a5c1df7e0054..6d0126d955ef 100644
      --- a/configs/j721e_evm_a72_defconfig
      +++ b/configs/j721e_evm_a72_defconfig
      @@ -13,7 +13,7 @@ CONFIG_CUSTOM_SYS_INIT_SP_ADDR=0x80480000
      CONFIG_ENV_SIZE=0x20000
      CONFIG_DM_GPIO=y
      CONFIG_SPL_DM_SPI=y
      -CONFIG_DEFAULT_DEVICE_TREE="k3-j721e-common-proc-board"
      +CONFIG_DEFAULT_DEVICE_TREE="k3-j721e-sk"
      CONFIG_SPL_TEXT_BASE=0x80080000
      CONFIG_DM_RESET=y
      CONFIG_SPL_MMC=y

      diff --git a/arch/arm/dts/k3-j721e-binman.dtsi b/arch/arm/dts/k3-j721e-binman.dtsi
      index 673be646b1e3..752fa805fe8d 100644
      --- a/arch/arm/dts/k3-j721e-binman.dtsi
      +++ b/arch/arm/dts/k3-j721e-binman.dtsi
      @@ -299,8 +299,8 @@
      #define SPL_J721E_SK_DTB "spl/dts/k3-j721e-sk.dtb"

      #define UBOOT_NODTB "u-boot-nodtb.bin"
      -#define J721E_EVM_DTB "u-boot.dtb"
      -#define J721E_SK_DTB "arch/arm/dts/k3-j721e-sk.dtb"
      +#define J721E_EVM_DTB "arch/arm/dts/k3-j721e-common-proc-board.dtb"
      +#define J721E_SK_DTB "u-boot.dtb"

This step will embed the public key in the u-boot.dtb file that was already
built during the initial u-boot build.

.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family', 'AM57X_family')

   .. code-block:: console

      mkimage -r -f fitImage.its -k $UBOOT_PATH/board/ti/keys -K $UBOOT_PATH/build/$ARMV7/dts/dt.dtb fitImage

.. ifconfig:: CONFIG_part_family not in ('AM335X_family', 'AM437X_family', 'AM57X_family')

   .. code-block:: console

      mkimage -r -f fitImage.its -k $UBOOT_PATH/arch/arm/mach-k3/keys -K $UBOOT_PATH/build/$ARMV8/dts/dt.dtb fitImage

.. note::

   If you have another set of keys then change the -k argument to point to
   the folder where your keys are present, the build requires the presence
   of both .key and .crt file.

Build uboot again
^^^^^^^^^^^^^^^^^

.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family', 'AM57X_family')

   The updated u-boot.dtb needs to be packed in u-boot.img for authentication
   so rebuild uboot ARMV7 without changing any parameters.

.. ifconfig:: CONFIG_part_family not in ('AM335X_family', 'AM437X_family', 'AM57X_family')

   The updated u-boot.dtb needs to be packed in u-boot.img for authentication
   so rebuild uboot ARMV8 without changing any parameters.

Refer to :ref:`top-level-makefile`
