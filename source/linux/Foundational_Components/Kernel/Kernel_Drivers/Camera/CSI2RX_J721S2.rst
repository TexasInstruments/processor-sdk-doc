.. include:: _CSI2RX_common.rst

***********************
Enabling camera sensors
***********************

J721S2 has two instances of CSI2RX capture subsystem and can support upto
eight **IMX390** cameras using FPDLink fusion EVM, J721S2 EVM and AM68A SK also
supports **OV5640** module connected to MIPI connector. AM68A SK has two
instances of 22-pin FFC camera connector to which **IMX219** based RPi camera
modules can be interfaced.

Applying sensor overlays
========================

To enable FPDLink cameras you will need to apply the device tree overlays
for both the fusion board and the sensor at U-boot prompt:

.. code-block:: text

   # For single RCM IMX390 connected to RX port 0 on Fusion board EVM on J721S2 CPB:
   # FPDLink IMX390 camera overlays are named according to the port connected in the following
   # format : ti/k3-fpdlink-imx390-rcm-<csi_port>-<fusion_rx_port>.dtbo
   => setenv name_overlays ti/k3-j721s2-evm-fusion.dtbo ti/k3-fpdlink-imx390-rcm-0-0.dtbo
   => boot

   # For single RCM IMX390 connected to RX port 0 on DS90UB954-Q1 EVM on J721S2 EVM:
   => setenv name_overlays ti/k3-j721s2-evm-ub954.dtbo ti/k3-fpdlink-imx390-rcm-0-0.dtbo
   => boot

   # For single RCM IMX390 connected to RX port 0 on Fusion board EVM on AM68A SK:
   => setenv name_overlays ti/k3-j721e-sk-fpdlink-fusion.dtbo ti/k3-fpdlink-imx390-rcm-0-0.dtbo
   => boot

   # For single IMX219 connected to RX port 0 on V3Link fusion on AM68A SK:
   => setenv name_overlays ti/k3-am68-sk-v3link-fusion.dtbo ti/k3-v3link-imx219-0-0.dtbo
   => boot

To enable IMX219 camera connected to the 22-pin FFC connectoron AM68A SK,
enable the sensor overlay at U-boot prompt:

.. code-block:: text

   # For IMX219 connected to 22-pin FFC connector
   => setenv name_overlays ti/k3-j721e-sk-csi2-dual-imx219.dtbo
   => boot

For more details on building or applying overlays permanently, refer to the
:ref:`How to enable DT overlays in linux <howto_dt_overlays>` guide.


CSI2RX testing details
======================

The following combinations of sensors are tested on J721S2 in the SDK 11.02.00

+--------------+---------------------------------------+-----------------------------------+
| Hardware     | Sensor                                | Default format and resolution     |
+==============+=======================================+===================================+
| J721S2       | LI OV5640 MIPI CSI Camera             | YUYV8_1X16/1280x720 at 30 fps     |
+--------------+---------------------------------------+-----------------------------------+
| J721S2       | FPDLink fusion 1 EVM, IMX390          | SRGGB12_1X12/1936x1100 at 30 fps  |
+--------------+---------------------------------------+-----------------------------------+
| J721S2       | DS90UB954-Q1 EVM, IMX390              | SRGGB12_1X12/1936x1100 at 30 fps  |
+--------------+---------------------------------------+-----------------------------------+
| AM68A        | IMX219 RPi Camera                     | SRGGB8_1X8/1920x1080 at 30 fps    |
+--------------+---------------------------------------+-----------------------------------+
| AM68A        | LI OV5640 MIPI CSI Camera             | YUYV8_1X16/1280x720 at 30 fps     |
+--------------+---------------------------------------+-----------------------------------+
| AM68A        | FPDLink fusion 1 EVM, IMX390          | SRGGB12_1X12/1936x1100 at 30 fps  |
+--------------+---------------------------------------+-----------------------------------+
| AM68A        | V3Link fusion, IMX219                 | SRGGB8_1X8/1920x1080 at 30 fps    |
+--------------+---------------------------------------+-----------------------------------+
