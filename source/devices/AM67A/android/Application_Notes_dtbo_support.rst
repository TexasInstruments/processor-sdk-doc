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

.. list-table:: AM67A-EVM
   :header-rows: 1
   :widths: 5 40

   * - Index
     - Description
   * - 15
     - CSI2 Quad RPi Camera IMX219
   * - 16
     - CSI2 Quad TEVI-OV5640 Camera
   * - 17
     - RPi 7inch touchscreen DSI panel
   * - 18
     - FPDLink Fusion display
