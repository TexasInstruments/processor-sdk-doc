UART
------------------------------------


This section documents how to use the UART to load files to boot the
board into U-Boot. After that the user is expected to know how they want
to continue loading files.

Booting U-Boot from the console UART
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In some cases we support loading SPL and U-Boot over the console UART.
You will need to use the :file:`tiboot3.bin`, :file:`tispl.bin` and :file:`u-boot.img`
files to boot. As per the TRM, the file is to be loaded via the X-MODEM
protocol at 115200 baud 8 stop bits no parity (same as using it for
console). SPL in turn expects to be sent :file:`u-boot.img` at the same rate
but via Y-MODEM. An example session from the host PC, assuming console
is on ttyUSB0 and already configured would be and the **lrzsz** package
is installed

.. ifconfig:: CONFIG_part_variant in ('AM65X', 'J721E', 'J7200')

   In K3 based platforms, ROM supports booting from MCU_UART0 via X-Modem protocol.
   The entire UART-based boot process up to U-Boot (proper) prompt goes through
   different stages and uses different UART peripherals as follows:

.. ifconfig:: CONFIG_part_variant in ('AM65X', 'J721E')

   +---------------+---------------+-------------+------------+
   |   WHO         | Loading WHAT  |  HW Module  |  Protocol  |
   +===============+===============+=============+============+
   | Boot ROM      |  tiboot3.bin  |  MCU_UART0  |  X-Modem   |
   +---------------+---------------+-------------+------------+
   | R5 SPL        |  sysfw.itb    |  MCU_UART0  |  Y-Modem   |
   +---------------+---------------+-------------+------------+
   | R5 SPL        |  tispl.bin    |  MAIN_UART0 |  Y-Modem   |
   +---------------+---------------+-------------+------------+
   | A53/A72 SPL   |  u-boot.img   |  MAIN_UART0 |  Y-Modem   |
   +---------------+---------------+-------------+------------+

   UART_BOOT_MAIN_UART and UART_BOOT_MCU_UART should be set to serial ports such as /dev/ttyUSBx.

   .. code-block:: console

      $ sb --xmodem $OUT_R5/tiboot3.bin > $UART_BOOT_MCU_UART < $UART_BOOT_MCU_UART
      $ sb --ymodem $SYSFW_ITB > $UART_BOOT_MCU_UART < $UART_BOOT_MCU_UART
      $ sb --ymodem $OUT_AXX/tispl.bin > $UART_BOOT_MAIN_UART < $UART_BOOT_MAIN_UART
      $ sb --ymodem $OUT_AXX/u-boot.img > $UART_BOOT_MAIN_UART < $UART_BOOT_MAIN_UART

.. ifconfig:: CONFIG_part_variant in ('J7200', 'J721S2', 'J784S4','J742S2')

   +---------------+---------------+-------------+------------+
   |   WHO         | Loading WHAT  |  HW Module  |  Protocol  |
   +===============+===============+=============+============+
   | Boot ROM      |  tiboot3.bin  |  MCU_UART0  |  X-Modem   |
   +---------------+---------------+-------------+------------+
   | R5 SPL        |  tispl.bin    |  MAIN_UART0 |  Y-Modem   |
   +---------------+---------------+-------------+------------+
   | A53/A72 SPL   |  u-boot.img   |  MAIN_UART0 |  Y-Modem   |
   +---------------+---------------+-------------+------------+

   UART_BOOT_MAIN_UART and UART_BOOT_MCU_UART should be set to serial ports such as /dev/ttyUSBx.

   .. code-block:: console

      $ sb --xmodem $OUT_R5/tiboot3.bin > $UART_BOOT_MCU_UART < $UART_BOOT_MCU_UART
      $ sb --ymodem $OUT_AXX/tispl.bin > $UART_BOOT_MAIN_UART < $UART_BOOT_MAIN_UART
      $ sb --ymodem $OUT_AXX/u-boot.img > $UART_BOOT_MAIN_UART < $UART_BOOT_MAIN_UART

.. ifconfig:: CONFIG_part_variant in ('AM64X', 'AM62X', 'J722S', 'AM62PX', 'AM62DX')

   ROM supports booting from MAIN_UART0 via X-Modem protocol. R5 SPL, A53
   SPL and U-Boot use Y-MODEM Protocol for downloading next stages over
   MAIN_UART0

   +---------------+---------------+-------------+------------+
   |   WHO         | Loading WHAT  |  HW Module  |  Protocol  |
   +===============+===============+=============+============+
   | Boot ROM      |  tiboot3.bin  |  MAIN_UART0 |  X-Modem   |
   +---------------+---------------+-------------+------------+
   | R5 SPL        |  tispl.bin    |  MAIN_UART0 |  Y-Modem   |
   +---------------+---------------+-------------+------------+
   | A53 SPL       |  u-boot.img   |  MAIN_UART0 |  Y-Modem   |
   +---------------+---------------+-------------+------------+

   UART_BOOT_MAIN_UART should be set to serial ports such as /dev/ttyUSBx.

   .. code-block:: console

      $ sb --xmodem $OUT_R5/tiboot3.bin > $UART_BOOT_MAIN_UART < $UART_BOOT_MAIN_UART
      $ sb --ymodem $OUT_AXX/tispl.bin > $UART_BOOT_MAIN_UART < $UART_BOOT_MAIN_UART
      $ sb --ymodem $OUT_AXX/u-boot.img > $UART_BOOT_MAIN_UART < $UART_BOOT_MAIN_UART
