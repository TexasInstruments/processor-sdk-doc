.. include:: _CSI2RX_common.rst

***********************
Enabling camera sensors
***********************

J722S has two instances of CSI2RX capture subsystem and
can support upto eight **IMX390** cameras using FPDLink fusion EVM.
J722S also supports **OV5640** and **IMX219** module connected to MIPI connector.

Applying sensor overlays
========================

To enable FPDLink cameras you will need to apply the device tree overlays
for both the fusion board and the sensor at U-boot prompt:

.. code-block:: text

   # For single RCM IMX390 connected to RX port 0 on Fusion board EVM on J722S EVM:
   # FPDLink IMX390 camera overlays are named according to the port connected in the following
   # format : ti/k3-fpdlink-imx390-rcm-<csi_port>-<fusion_rx_port>.dtbo
   => setenv name_overlays ti/k3-j721s2-evm-fusion.dtbo ti/k3-fpdlink-imx390-rcm-0-0.dtbo
   => boot

   # For single IMX219 connected to RX port 0 on V3Link fusion on J722S EVM:
   => setenv name_overlays ti/k3-j722s-evm-v3link-fusion.dtbo ti/k3-v3link-imx219-0-0.dtbo
   => boot

For more details on building or applying overlays permanently, refer to the
:ref:`How to enable DT overlays in linux <howto_dt_overlays>` guide.


CSI2RX testing details
======================

The following combinations of sensors are tested in the SDK 11.02.00

+--------------+---------------------------------------+-----------------------------------+
| Hardware     | Sensor                                | Default format and resolution     |
+==============+=======================================+===================================+
| J722S        | OV5640 TEVI/PCAM Rpi Module           | YUYV8_1X16/1280x720 at 30 fps     |
+--------------+---------------------------------------+-----------------------------------+
| J722S        | FPDLink fusion 1 EVM, IMX390          | SRGGB12_1X12/1936x1100 at 30 fps  |
+--------------+---------------------------------------+-----------------------------------+
| J722S        | IMX219 RPi Camera                     | SRGGB8_1X8/1920x1080 at 30 fps    |
+--------------+---------------------------------------+-----------------------------------+
| J722S        | V3Link fusion, IMX219                 | SRGGB8_1X8/1920x1080 at 30 fps    |
+--------------+---------------------------------------+-----------------------------------+
