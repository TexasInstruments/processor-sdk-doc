.. include:: _CSI2RX_common.rst

***********************
Enabling camera sensors
***********************

J721E has two instances of CSI2RX capture subsystem and can support upto
eight **IMX390** cameras using FPDLink fusion EVM. J721E EVM and SK also
supports **OV5640** module connected to MIPI connector. J721E SK has two
instances of 15-pin FFC camera connector to which **IMX219** based RPi camera
modules can be interfaced.

Applying sensor overlays
========================

To enable FPDLink cameras you will need to apply the device tree overlays
for both the fusion board and the sensor at U-boot prompt:

.. code-block:: text

   # For single RCM IMX390 connected to RX port 0 on Fusion board EVM on J721E CPB:
   # FPDLink IMX390 camera overlays are named according to the port connected in the following
   # format : ti/k3-fpdlink-imx390-rcm-<csi_port>-<fusion_rx_port>.dtbo
   => setenv name_overlays ti/k3-j721e-evm-fusion.dtbo ti/k3-fpdlink-imx390-rcm-0-0.dtbo
   => boot

   # For single RCM IMX390 connected to RX port 0 on DS90UB954-Q1 EVM on J721E EVM:
   => setenv name_overlays ti/k3-j721e-evm-ub954.dtbo ti/k3-fpdlink-imx390-rcm-0-0.dtbo
   => boot

   # For single RCM IMX390 connected to RX port 0 on Fusion board EVM on J721E SK:222
   => setenv name_overlays ti/k3-j721e-sk-fpdlink-fusion.dtbo  ti/k3-fpdlink-imx390-rcm-0-0.dtbo
   => boot

To enable IMX219 camera connected to the 22-pin FFC connectoron J721E SK,
enable the sensor overlay at U-boot prompt:

.. code-block:: text

   # For IMX219 connected to 15-pin FFC connector
   => setenv name_overlays ti/k3-j721e-sk-csi2-dual-imx219.dtbo
   => boot

For more details on building or applying overlays permanently, refer to the
:ref:`How to enable DT overlays in linux <howto_dt_overlays>` guide.


CSI2RX testing details
======================

The following combinations of sensors are tested in the SDK 11.02.00

+--------------+---------------------------------------+-----------------------------------+
| Hardware     | Sensor                                | Default format and resolution     |
+==============+=======================================+===================================+
| J721E EVM    | LI OV5640 MIPI CSI Camera             | YUYV8_1X16/1280x720 at 30 fps     |
+--------------+---------------------------------------+-----------------------------------+
| J721E EVM    | FPDLink fusion 1 EVM, IMX390          | SRGGB12_1X12/1936x1100 at 30 fps  |
+--------------+---------------------------------------+-----------------------------------+
| J721E EVM    | DS90UB954-Q1 EVM, IMX390              | SRGGB12_1X12/1936x1100 at 30 fps  |
+--------------+---------------------------------------+-----------------------------------+
| J721E SK     | IMX219 RPi Camera                     | SRGGB8_1X8/1920x1080 at 30 fps    |
+--------------+---------------------------------------+-----------------------------------+
| J721E SK     | LI OV5640 MIPI CSI Camera             | YUYV8_1X16/1280x720 at 30 fps     |
+--------------+---------------------------------------+-----------------------------------+
| J721E SK     | FPDLink fusion 1 EVM, IMX390          | SRGGB12_1X12/1936x1100 at 30 fps  |
+--------------+---------------------------------------+-----------------------------------+
