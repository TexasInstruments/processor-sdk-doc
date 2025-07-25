.. _u-boot-build-guide-target-images-k3:

#############
Target Images
#############

******
Images
******

.. ifconfig:: CONFIG_part_variant in ('AM65X', 'J721E', 'J7200', 'AM64X', 'AM62X', 'AM62AX', 'AM62LX', 'AM62PX', 'J721S2', 'J784S4','J742S2', 'J722S')

   Copy the below images to the boot partition of an SD card and boot.
   Instructions to format the SD card can be found :ref:`here <processor-sdk-linux-create-sd-card>`.

.. ifconfig:: CONFIG_part_variant in ('AM65X')

   * GP

      * :file:`tiboot3-am65x_sr2-gp-evm.bin` and :file:`sysfw-am65x_sr2-gp-evm.itb` from :file:`<output directory>/r5`
      * :file:`tispl.bin_unsigned` and :file:`u-boot.img_unsigned` from :file:`<output directory>/a53`

   * HS

      * :file:`tiboot3-am65x_sr2-hs-evm.bin` and :file:`sysfw-am65x_sr2-hs-evm.itb` from :file:`<output directory>/r5`
      * :file:`tispl.bin` and :file:`u-boot.img` from :file:`<output directory>/a53`

.. ifconfig:: CONFIG_part_variant in ('J721E')

   * GP

      * :file:`tiboot3-j721e-gp-evm.bin` and :file:`sysfw-j721e-gp-evm.itb` from :file:`<output directory>/r5`
      * :file:`tispl.bin_unsigned` and :file:`u-boot.img_unsigned` from :file:`<output directory>/a72`

   * HS-FS

      * :file:`tiboot3-j721e_sr2-hs-fs-evm.bin` and :file:`sysfw-j721e_sr2-hs-fs-evm.itb` from :file:`<output directory>/r5`
      * :file:`tispl.bin` and :file:`u-boot.img` from :file:`<output directory>/a72`

   * HS-SE

      * :file:`tiboot3-j721e_sr2-hs-evm.bin` and :file:`sysfw-j721e_sr2-hs-evm.itb` from :file:`<output directory>/r5`
      * :file:`tispl.bin` and :file:`u-boot.img` from :file:`<output directory>/a72`

.. ifconfig:: CONFIG_part_variant in ('J7200')

   * GP

      * :file:`tiboot3-j7200-gp-evm.bin` from :file:`<output directory>/r5`
      * :file:`tispl.bin_unsigned` and :file:`u-boot.img_unsigned` from :file:`<output directory>/a72`

   * HS-FS

      * :file:`tiboot3-j7200_sr2-hs-fs-evm.bin` from :file:`<output directory>/r5`
      * :file:`tispl.bin` and :file:`u-boot.img` from :file:`<output directory>/a72`

   * HS-SE

      * :file:`tiboot3-j7200_sr2-hs-evm.bin` from :file:`<output directory>/r5`
      * :file:`tispl.bin` and :file:`u-boot.img` from :file:`<output directory>/a72`

.. ifconfig:: CONFIG_part_variant in ('J721S2')

   * GP

      * :file:`tiboot3-j721s2-gp-evm.bin` from :file:`<output directory>/r5`
      * :file:`tispl.bin_unsigned` and :file:`u-boot.img_unsigned` from :file:`<output directory>/a72`

   * HS-FS

      * :file:`tiboot3-j721s2-hs-fs-evm.bin` from :file:`<output directory>/r5`
      * :file:`tispl.bin` and :file:`u-boot.img` from :file:`<output directory>/a72`

   * HS-SE

      * :file:`tiboot3-j721s2-hs-evm.bin` from :file:`<output directory>/r5`
      * :file:`tispl.bin` and :file:`u-boot.img` from :file:`<output directory>/a72`

.. ifconfig:: CONFIG_part_variant in ('J784S4')

   * GP

      * :file:`tiboot3-j784s4-gp-evm.bin` from :file:`<output directory>/r5`
      * :file:`tispl.bin_unsigned` and :file:`u-boot.img_unsigned` from :file:`<output directory>/a72`

   * HS-FS

      * :file:`tiboot3-j784s4-hs-fs-evm.bin` from :file:`<output directory>/r5`
      * :file:`tispl.bin` and :file:`u-boot.img` from :file:`<output directory>/a72`

   * HS-SE

      * :file:`tiboot3-j784s4-hs-evm.bin` from :file:`<output directory>/r5`
      * :file:`tispl.bin` and :file:`u-boot.img` from :file:`<output directory>/a72`

.. ifconfig:: CONFIG_part_variant in ('J742S2')

   * GP

      * :file:`tiboot3-j742s2-gp-evm.bin` from :file:`<output directory>/r5`
      * :file:`tispl.bin_unsigned` and :file:`u-boot.img_unsigned` from :file:`<output directory>/a72`

   * HS-FS

      * :file:`tiboot3-j742s2-hs-fs-evm.bin` from :file:`<output directory>/r5`
      * :file:`tispl.bin` and :file:`u-boot.img` from :file:`<output directory>/a72`

   * HS-SE

      * :file:`tiboot3-j742s2-hs-evm.bin` from :file:`<output directory>/r5`
      * :file:`tispl.bin` and :file:`u-boot.img` from :file:`<output directory>/a72`

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   * GP

      * :file:`tiboot3-am64x-gp-evm.bin` from :file:`<output directory>/r5`
      * :file:`tispl.bin_unsigned` and :file:`u-boot.img_unsigned` from :file:`<output directory>/a53`

   * HS-FS

      * :file:`tiboot3-am64x_sr2-hs-fs-evm.bin` from :file:`<output directory>/r5`
      * :file:`tispl.bin` and :file:`u-boot.img` from :file:`<output directory>/a53`

   * HS-SE

      * :file:`tiboot3-am64x_sr2-hs-evm.bin` from :file:`<output directory>/r5`
      * :file:`tispl.bin` and :file:`u-boot.img` from :file:`<output directory>/a53`

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   * GP

      * :file:`tiboot3-am62x-gp-evm.bin` from :file:`<output directory>/r5`
      * :file:`tispl.bin_unsigned` and :file:`u-boot.img_unsigned` from :file:`<output directory>/a53`

   * HS-FS

      * :file:`tiboot3-am62x-hs-fs-evm.bin` from :file:`<output directory>/r5`
      * :file:`tispl.bin` and :file:`u-boot.img` from :file:`<output directory>/a53`

   * HS-SE

      * :file:`tiboot3-am62x-hs-evm.bin` from :file:`<output directory>/r5`
      * :file:`tispl.bin` and :file:`u-boot.img` from :file:`<output directory>/a53`

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

   * GP

      * :file:`tiboot3-am62ax-gp-evm.bin` from :file:`<output directory>/r5`
      * :file:`tispl.bin_unsigned` and :file:`u-boot.img_unsigned` from :file:`<output directory>/a53`

   * HS-FS

      * :file:`tiboot3-am62ax-hs-fs-evm.bin` from :file:`<output directory>/r5`
      * :file:`tispl.bin` and :file:`u-boot.img` from :file:`<output directory>/a53`

   * HS-SE

      * :file:`tiboot3-am62ax-hs-evm.bin` from :file:`<output directory>/r5`
      * :file:`tispl.bin` and :file:`u-boot.img` from :file:`<output directory>/a53`

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   * HS-FS

      * :file:`tiboot3-am62px-hs-fs-evm.bin` from :file:`<output directory>/r5`
      * :file:`tispl.bin` and :file:`u-boot.img` from :file:`<output directory>/a53`

   * HS-SE

      * :file:`tiboot3-am62px-hs-evm.bin` from :file:`<output directory>/r5`
      * :file:`tispl.bin` and :file:`u-boot.img` from :file:`<output directory>/a53`

.. ifconfig:: CONFIG_part_variant in ('J722S')

   * HS-FS

      * :file:`tiboot3-j722s-hs-fs-evm.bin` from :file:`<output directory>/r5`
      * :file:`tispl.bin` and :file:`u-boot.img` from :file:`<output directory>/a53`

   * HS-SE

      * :file:`tiboot3-j722s-hs-evm.bin` from :file:`<output directory>/r5`
      * :file:`tispl.bin` and :file:`u-boot.img` from :file:`<output directory>/a53`

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   * **HS-FS**

      * :file:`tiboot3-am62lx-hs-fs-evm.bin`
      * :file:`tispl.bin`
      * :file:`u-boot.img`

.. ifconfig:: CONFIG_part_variant in ('AM65X', 'J721E', 'J7200', 'AM64X', 'AM62X', 'AM62AX', 'AM62PX', 'J721S2', 'J784S4','J742S2', 'J722S', 'AM62LX')

   .. warning::

      Rename :file:`tiboot3-<board>-evm.bin` to :file:`tiboot3.bin` in order for the device to load this binary from the SD card boot partition.
      Also, (For GP devices only) rename :file:`tispl.bin_unsigned` to :file:`tispl.bin` and :file:`u-boot.img_unsigned` to :file:`u-boot.img` as well.

*************
Image Formats
*************

   .. ifconfig:: CONFIG_part_variant not in ('J7200', 'AM64X', 'J721S2', 'J721E', 'AM62X', 'AM62AX', 'AM62LX', 'J784S4','J742S2', 'J722S')

      - tiboot3.bin

      .. code-block:: text

         +-----------------------+
         |        X.509          |
         |      Certificate      |
         | +-------------------+ |
         | |                   | |
         | |        R5         | |
         | |   u-boot-spl.bin  | |
         | |                   | |
         | +-------------------+ |
         | |                   | |
         | |     FIT header    | |
         | | +---------------+ | |
         | | |               | | |
         | | |   DTB 1...N   | | |
         | | +---------------+ | |
         | +-------------------+ |
         +-----------------------+

      - tispl.bin

      .. code-block:: text

         +-----------------------+
         |                       |
         |       FIT HEADER      |
         | +-------------------+ |
         | |                   | |
         | |      ARM64 ATF    | |
         | +-------------------+ |
         | |                   | |
         | |     ARM64 OPTEE   | |
         | +-------------------+ |
         | |                   | |
         | |      ARM64 SPL    | |
         | +-------------------+ |
         | |                   | |
         | |   SPL DTB 1...N   | |
         | +-------------------+ |
         +-----------------------+

      - sysfw.itb

      .. code-block:: text

         +-----------------------+
         |                       |
         |       FIT HEADER      |
         | +-------------------+ |
         | |                   | |
         | |     sysfw.bin     | |
         | +-------------------+ |
         | |                   | |
         | |    board config   | |
         | +-------------------+ |
         | |                   | |
         | |     PM config     | |
         | +-------------------+ |
         | |                   | |
         | |     RM config     | |
         | +-------------------+ |
         | |                   | |
         | |    Secure config  | |
         | +-------------------+ |
         +-----------------------+

   .. ifconfig:: CONFIG_part_variant in ('J721E')

      - tiboot3.bin

      .. code-block:: text

         +-----------------------+
         |        X.509          |
         |      Certificate      |
         | +-------------------+ |
         | |                   | |
         | |        R5         | |
         | |   u-boot-spl.bin  | |
         | |                   | |
         | +-------------------+ |
         | |                   | |
         | |     FIT header    | |
         | | +---------------+ | |
         | | |               | | |
         | | |   DTB 1...N   | | |
         | | +---------------+ | |
         | +-------------------+ |
         +-----------------------+

      - tispl.bin

      .. code-block:: text

         +-----------------------+
         |                       |
         |       FIT HEADER      |
         | +-------------------+ |
         | |                   | |
         | |      A72 ATF      | |
         | +-------------------+ |
         | |                   | |
         | |     A72 OPTEE     | |
         | +-------------------+ |
         | |                   | |
         | |      R5 DM FW     | |
         | +-------------------+ |
         | |                   | |
         | |      A72 SPL      | |
         | +-------------------+ |
         | |                   | |
         | |   SPL DTB 1...N   | |
         | +-------------------+ |
         +-----------------------+

      - sysfw.itb

      .. code-block:: text

         +-----------------------+
         |                       |
         |       FIT HEADER      |
         | +-------------------+ |
         | |                   | |
         | |     sysfw.bin     | |
         | +-------------------+ |
         | |                   | |
         | |    board config   | |
         | +-------------------+ |
         | |                   | |
         | |     PM config     | |
         | +-------------------+ |
         | |                   | |
         | |     RM config     | |
         | +-------------------+ |
         | |                   | |
         | |    Secure config  | |
         | +-------------------+ |
         +-----------------------+

   .. ifconfig:: CONFIG_part_variant in ('J7200', 'J721S2', 'J784S4','J742S2')

      - tiboot3.bin:

         .. code-block:: text

                  +-----------------------+
                  |        X.509          |
                  |      Certificate      |
                  | +-------------------+ |
                  | |                   | |
                  | |        R5         | |
                  | |   u-boot-spl.bin  | |
                  | |                   | |
                  | +-------------------+ |
                  | |                   | |
                  | |     FIT header    | |
                  | | +---------------+ | |
                  | | |               | | |
                  | | |   DTB 1...N   | | |
                  | | +---------------+ | |
                  | +-------------------+ |
                  | |                   | |
                  | |      FIT HEADER   | |
                  | | +---------------+ | |
                  | | |               | | |
                  | | |   sysfw.bin   | | |
                  | | +---------------+ | |
                  | | |               | | |
                  | | |  board config | | |
                  | | +---------------+ | |
                  | | |               | | |
                  | | |   PM config   | | |
                  | | +---------------+ | |
                  | | |               | | |
                  | | |   RM config   | | |
                  | | +---------------+ | |
                  | | |               | | |
                  | | | Secure config | | |
                  | | +---------------+ | |
                  | +-------------------+ |
                  +-----------------------+

      - tispl.bin

         .. code-block:: text

                  +-----------------------+
                  |                       |
                  |       FIT HEADER      |
                  | +-------------------+ |
                  | |                   | |
                  | |      A72 ATF      | |
                  | +-------------------+ |
                  | |                   | |
                  | |     A72 OPTEE     | |
                  | +-------------------+ |
                  | |                   | |
                  | |      R5 DM FW     | |
                  | +-------------------+ |
                  | |                   | |
                  | |      A72 SPL      | |
                  | +-------------------+ |
                  | |                   | |
                  | |   SPL DTB 1...N   | |
                  | +-------------------+ |
                  +-----------------------+

   .. ifconfig:: CONFIG_part_variant in ('AM64X')

      - tiboot3.bin:

         .. code-block:: text

                  +-----------------------+
                  |        X.509          |
                  |      Certificate      |
                  | +-------------------+ |
                  | |                   | |
                  | |        R5         | |
                  | |   u-boot-spl.bin  | |
                  | |                   | |
                  | +-------------------+ |
                  | |                   | |
                  | |     FIT header    | |
                  | | +---------------+ | |
                  | | |               | | |
                  | | |   DTB 1...N   | | |
                  | | +---------------+ | |
                  | +-------------------+ |
                  | |                   | |
                  | |      FIT HEADER   | |
                  | | +---------------+ | |
                  | | |               | | |
                  | | |   sysfw.bin   | | |
                  | | +---------------+ | |
                  | | |               | | |
                  | | |  board config | | |
                  | | +---------------+ | |
                  | | |               | | |
                  | | |   PM config   | | |
                  | | +---------------+ | |
                  | | |               | | |
                  | | |   RM config   | | |
                  | | +---------------+ | |
                  | | |               | | |
                  | | | Secure config | | |
                  | | +---------------+ | |
                  | +-------------------+ |
                  +-----------------------+

      - tispl.bin

         .. code-block:: text

                  +-----------------------+
                  |                       |
                  |       FIT HEADER      |
                  | +-------------------+ |
                  | |                   | |
                  | |      A53 ATF      | |
                  | +-------------------+ |
                  | |                   | |
                  | |     A53 OPTEE     | |
                  | +-------------------+ |
                  | |                   | |
                  | |      A53 SPL      | |
                  | +-------------------+ |
                  | |                   | |
                  | |   SPL DTB 1...N   | |
                  | +-------------------+ |
                  +-----------------------+

   .. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX', 'AM62PX', 'J722S')

      - tiboot3.bin:

      .. code-block:: text

         +-----------------------+
         |        X.509          |
         |      Certificate      |
         | +-------------------+ |
         | |                   | |
         | |        R5         | |
         | |   u-boot-spl.bin  | |
         | |                   | |
         | +-------------------+ |
         | |                   | |
         | |TIFS with board cfg| |
         | |                   | |
         | +-------------------+ |
         | |                   | |
         | |                   | |
         | |     FIT header    | |
         | | +---------------+ | |
         | | |               | | |
         | | |   DTB 1...N   | | |
         | | +---------------+ | |
         | +-------------------+ |
         +-----------------------+

      - tispl.bin

      .. code-block:: text

         +-----------------------+
         |                       |
         |       FIT HEADER      |
         | +-------------------+ |
         | |                   | |
         | |      A53 ATF      | |
         | +-------------------+ |
         | |                   | |
         | |     A53 OPTEE     | |
         | +-------------------+ |
         | |                   | |
         | |      R5 DM FW     | |
         | +-------------------+ |
         | |                   | |
         | |      A53 SPL      | |
         | +-------------------+ |
         | |                   | |
         | |   SPL DTB 1...N   | |
         | +-------------------+ |
         +-----------------------+

   .. ifconfig:: CONFIG_part_variant in ('AM62LX')

      - tiboot3.bin

      .. code-block:: text

            TIBOOT3
         ┌─────────────┐
         │    X.509    │
         │ Certificate │
         │┌───────────┐│
         ││   BL-1    ││
         │├───────────┤│
         ││   TIFS    ││
         │├───────────┤│
         ││ TIFS CERT ││
         │└───────────┘│
         └─────────────┘

      - tispl.bin

      .. code-block:: text

            TISPL
         ┌─────────────┐
         │    X.509    │
         │ Certificate │
         │┌───────────┐│
         ││   BL-31   ││
         │├───────────┤│
         ││   TIFS    ││
         │├───────────┤│
         ││ TIFS CERT ││
         │├───────────┤│
         ││ BRD + SEC ││
         ││  CONFIGS  ││
         │├───────────┤│
         ││  U-BOOT   ││
         ││    SPL    ││
         │└───────────┘│
         └─────────────┘
