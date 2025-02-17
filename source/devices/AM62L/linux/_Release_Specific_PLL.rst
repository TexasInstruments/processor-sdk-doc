
PLL Programing Sequence Update To Avoid PLL Instability
=======================================================

In 10.00 SDK release, PLL programing sequence has been updated to follow the
correct programing sequence to avoid PLL instability. The PLL programing
sequence has been updated in following components of the SDK.

   #. TIFS firmware (ti-linux firmware repo)
   #. DM R5 firmware (ti-linux-firmware repo)
   #. R5 SPL (u-boot repo)

SDK 10.0 has all the updated components by default.

Below section provides information on how to pick up these updates for last
major SDK releases - SDK 09.02.

SDK 09.02.01.10
---------------

Linux SDK 09.02 was the last SDK release with LTS Kernel version 6.1 and
u-boot version 2024.x. To pick up the PLL updates on top of this SDK, pick the
components listed below when building the u-boot binaries.


   #. TIFS and DM Firmware

      - Pick up the SDK 10.0 TIFS and DM firmware from tag `10.00.07` of ti-linux-firmware repo

         - https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/tag/?h=10.00.07

   #. U-boot patches for SPL

      - Apply the below patches to u-boot project for getting the PLL driver updates in R5 SPL

         - https://git.ti.com/cgit/ti-u-boot/ti-u-boot/commit/?h=ti-u-boot-2024.04&id=a99fde602fae9efafeaafd57a7f684557f9cd666
         - https://git.ti.com/cgit/ti-u-boot/ti-u-boot/commit/?h=ti-u-boot-2024.04&id=fda88f8bcea30590528930ff9441c6e958da86f5

Refer to `SDK 09.02 u-boot build instructions <https://software-dl.ti.com/processor-sdk-linux/esd/AM62PX/09_02_01_10/exports/docs/linux/Foundational_Components/U-Boot/UG-General-Info.html#build-u-boot>`__
for more information on building u-boot binaries.
