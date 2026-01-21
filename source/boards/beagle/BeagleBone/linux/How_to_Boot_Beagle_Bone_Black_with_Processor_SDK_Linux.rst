.. http://processors.wiki.ti.com/index.php/How_to_Boot_Beagle_Bone_Black_with_Processor_SDK_Linux

How to Boot Beagle Bone Black with Processor SDK Linux
==================================================================

.. rubric:: Introduction
   :name: introduction-boot-bbb-linux

By default, BeagleBone Black EVM boots with the Debian image on eMMC.
This page describes two ways to boot a BeagleBone Black EVM with
Processor SDK Linux. First, create an SD card with processor SDK Linux
(:ref:`Create SD Card <processor-sdk-linux-create-sd-card>`).
Then, choose either of the two procedures below to boot with Processor
SDK Linux.

.. rubric:: Press S2 Button
   :name: press-s2-button

With the SD card plugged in, simply keep button S2 pressed while
powering up the BeagleBone Black EVM. This needs to be executed every
time powering up the EVM to use Processor SDK Linux.

.. rubric:: Erase eMMC
   :name: erase-emmc

With the SD card plugged in, stop at uboot. Then run the following two
commands to erase eMMC.

::

    mmc dev 1
    mmc erase 100 2800

With eMMC erased (one-time change), the booting falls back to use the SD
card. Power cycle the BeagleBone Black EVM to boot with Processor SDK
Linux.

