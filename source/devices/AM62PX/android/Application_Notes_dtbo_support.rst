.. _android-dtbo:

###########################
Device Tree Overlay Support
###########################

This application note contains steps to configure Device Tree Overlays (DTBO).
DTBOs can be enabled from U-Boot when extra peripherals are connected to the board.

.. attention::

   DTBOs are **board specific**.

It's possible to change the ``adtbo_idx`` from the U-Boot shell.
For example:

.. code-block:: console

   => env set adtbo_idx 1
   => saveenv
   => reset

.. warning::

   Multiple DTBOs are **not supported**.

The following Device-Tree Overlays are supported:

.. list-table:: AM62Px-SK EVM
   :header-rows: 1
   :widths: 5 40

   * - Index
     - Description
   * - 0
     - HDMI audio output (bridge by shorting a (J24) header on the board.)
   * - 1
     - Digilent PCam 5C OV5640 Camera
   * - 2
     - TEVI-OV5640C-S84-IR-RPI Camera
   * - 4
     - Enable MAIN and MCU GPIO + CANUART wakeup source
   * - 9
     - 4x MCAN interfaces (requires external CAN transceivers)
   * - 10
     - Microtips Technology USA 10.1” WUXGA (1920x1200) OLDI panel
   * - 12
     - M.2-CC3351 WiFi board on the M.2 connector
   * - 14
     - RPi 7inch touchscreen DSI panel
