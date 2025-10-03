################
USB Mass Storage
################

USB Mass Storage (UMS) functionality, allows a connected USB host to
access U-Boot block devices and enable file transfer. This is useful
for accessing storage devices such as SD or MMC from a USB host such
as host PC.

**************************
Configuration requirements
**************************

Set the following configuration in the U-Boot config file to enable UMS
support:

.. code-block:: kconfig

   CONFIG_CMD_USB_MASS_STORAGE=y

*****
Usage
*****

To use the UMS command:

.. code-block:: console

   => ums <dev> [<interface>] <devnum[:partnum]>

.. rubric:: dev

USB gadget device number.

.. rubric:: interface

Interface for accessing block device (MMC, SATA, ....), default is MMC.

.. rubric:: devnum

Device number for selected interface.

.. rubric:: partnum

Partition number for selected device, default is 0. 0 to expose all
partitions.

Example usage:

.. code-block:: console

   => mmc list
   mmc@fa10000: 0 (eMMC)
   mmc@fa00000: 1 (SD)
   => ums 0 mmc 1
   UMS: LUN 0, dev mmc 1, hwpart 0, sector 0x0, count 0x3b72400

This example exposes the SD card (mmc 1) as a USB mass storage device
to the connected host PC. The host PC can then mount and access the
storage device for file transfer. Press Ctrl+C to exit UMS command and
return to the U-boot prompt.

.. note::

   The USB controller must be in peripheral mode for UMS to work. If
   the controller is in host mode, then reconfigure it to
   peripheral mode before using the UMS command. The USB controller can
   be configured to operate in peripheral mode by changing the value of
   ``dr_mode`` property of USB controller node in device tree to ``peripheral``.
