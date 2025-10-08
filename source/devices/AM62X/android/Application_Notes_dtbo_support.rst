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

.. list-table:: AM62x-SK EVM
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
   * - 3
     - Microtips Technology USA 10.1" WUXGA (1920x1200) OLDI panel
   * - 4
     - Enable MAIN and MCU GPIO + CANUART wakeup source
   * - 11
     - M.2-CC3351 WiFi board on the M.2 connector
   * - 13
     - WL1837 on-board WiFi for AM62X rev 1,2,3

.. warning::
    On AM62x-SK EVM, LVDS Display is supported only on E3 board revision.

.. list-table:: AM62x-LP-SK EVM
   :header-rows: 1
   :widths: 5 40

   * - Index
     - Description
   * - 5
     - Microtips Technology USA 10.1"  WUXGA (1920x1200) OLDI panel


.. list-table:: Beagle Play
   :header-rows: 1
   :widths: 5 40

   * - Index
     - Description
   * - 6
     - Digilent PCam 5C OV5640 Camera
   * - 7
     - TEVI-OV5640C-S84-IR-RPI Camera
   * - 8
     - Lincoln Technology Solutions LCD185-101CT WUXGA(1920x1200) OLDI panel
