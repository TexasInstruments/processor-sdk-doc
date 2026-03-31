.. include:: _CSI2RX_common.rst

***********************
Enabling camera sensors
***********************

J784S4/AM69A and J742S2 has three instances of CSI2RX capture subsystem and
can support upto twelve **IMX390** cameras using FPDLink fusion EVM.
J784S4-EVM/AM69A-SK and J742S2-EVM also supports **OV5640** module connected
to MIPI connector. AM69A-SK has two instances of 22-pin FFC camera connector
to which **IMX219** based RPi camera modules can be interfaced.

Applying sensor overlays
========================

To enable FPDLink cameras you will need to apply the device tree overlays
for both the fusion board and the sensor at U-boot prompt:

.. code-block:: text

   # For single RCM IMX390 connected to RX port 0 on Fusion board EVM on J784S4/J742S2 EVM:
   # FPDLink IMX390 camera overlays are named according to the port connected in the following
   # format : ti/k3-fpdlink-imx390-rcm-<csi_port>-<fusion_rx_port>.dtbo
   => setenv name_overlays ti/k3-j721s2-evm-fusion.dtbo ti/k3-fpdlink-imx390-rcm-0-0.dtbo
   => boot

   # For single RCM IMX390 connected to port 0 on FPDLink IV Fusion 2 board on J784S4/J742S2 EVM:
   => setenv name_overlays ti/k3-j784s4-evm-fpdlink-iv-fusion.dtbo ti/k3-fpdlink-imx390-rcm-0-0.dtbo
   => boot

   # For single RCM IMX390 connected to RX port 0 on DS90UB954-Q1 EVM on J784S4 EVM:
   => setenv name_overlays ti/k3-j721s2-evm-ub954.dtbo ti/k3-fpdlink-imx390-rcm-0-0.dtbo
   => boot

   # For single RCM IMX390 connected to RX port 0 on Fusion board EVM on AM69A SK:
   => setenv name_overlays ti/k3-j721e-sk-fpdlink-fusion.dtbo ti/k3-fpdlink-imx390-rcm-0-0.dtbo
   => boot

   # For single IMX219 connected to RX port 0 on V3Link fusion on AM69A SK:
   => setenv name_overlays ti/k3-am68-sk-v3link-fusion.dtbo ti/k3-v3link-imx219-0-0.dtbo
   => boot

   # For using two CSI TX on V3Link fusion to two CSI RX on AM69A SK
   => setenv name_overlays ti/k3-am68-sk-v3link-fusion-dual-csitx.dtbo ti/k3-v3link-imx219-0-2.dtbo ti/k3-v3link-imx219-0-3.dtbo ti/k3-v3link-imx219-1-0.dtbo ti/k3-v3link-imx219-1-1.dtbo
   => boot
   # After booting, configure routing on the V3Link fusion for the above setup using the following commands:
   => media-ctl -R '"ds90ub960 5-0030" [2/0 -> 4/2 [1], 3/0 -> 4/3 [1]]'
   => media-ctl -R '"ds90ub960 6-0030" [0/0 -> 5/0 [1], 1/0 -> 5/1 [1]]'
   => media-ctl --set-v4l2 '"ds90ub960 5-0030" 2/0 [fmt:SRGGB8_1X8/1920x1080 field:none]'
   => media-ctl --set-v4l2 '"ds90ub960 5-0030" 3/0 [fmt:SRGGB8_1X8/1920x1080 field:none]'
   => media-ctl --set-v4l2 '"ds90ub960 6-0030" 0/0 [fmt:SRGGB8_1X8/1920x1080 field:none]'
   => media-ctl --set-v4l2 '"ds90ub960 6-0030" 1/0 [fmt:SRGGB8_1X8/1920x1080 field:none]'
   # The two CSI TX configuration on V3Link fusion described above can be used on relevant platforms using similar commands.

To enable IMX219 camera connected to the 22-pin FFC connector on AM69A SK,
enable the sensor overlay at U-boot prompt:

.. code-block:: text

   # For IMX219 connected to 22-pin FFC connector
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
| J784S4       | LI OV5640 MIPI CSI Camera             | YUYV8_1X16/1280x720 at 30 fps     |
+--------------+---------------------------------------+-----------------------------------+
| J784S4       | FPDLink fusion 1 EVM, IMX390          | SRGGB12_1X12/1936x1100 at 30 fps  |
+--------------+---------------------------------------+-----------------------------------+
| J784S4       | FPDLink fusion 2 EVM, IMX390          | SRGGB12_1X12/1936x1100 at 30 fps  |
+--------------+---------------------------------------+-----------------------------------+
| J784S4       | DS90UB954-Q1 EVM, IMX390              | SRGGB12_1X12/1936x1100 at 30 fps  |
+--------------+---------------------------------------+-----------------------------------+
| AM69A        | IMX219 RPi Camera                     | SRGGB8_1X8/1920x1080 at 30 fps    |
+--------------+---------------------------------------+-----------------------------------+
| AM69A        | LI OV5640 MIPI CSI Camera             | YUYV8_1X16/1280x720 at 30 fps     |
+--------------+---------------------------------------+-----------------------------------+
| AM69A        | FPDLink fusion 1 EVM, IMX390          | SRGGB12_1X12/1936x1100 at 30 fps  |
+--------------+---------------------------------------+-----------------------------------+
| AM69A        | V3Link fusion, IMX219                 | SRGGB8_1X8/1920x1080 at 30 fps    |
+--------------+---------------------------------------+-----------------------------------+
| J742S2       | FPDLink fusion 1 EVM, IMX390          | SRGGB12_1X12/1936x1100 at 30 fps  |
+--------------+---------------------------------------+-----------------------------------+
