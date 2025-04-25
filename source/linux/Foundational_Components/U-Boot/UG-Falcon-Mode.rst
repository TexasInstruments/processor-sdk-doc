==================
U-Boot Falcon Mode
==================

U-Boot's falcon mode on |__PART_FAMILY_DEVICE_NAMES__| bypasses the A-core SPL
and U-Boot stage, which allows for booting straight to linux kernel after OP-TEE
and ATF.

**Normal boot flow:**

* R5 SPL -> ATF -> OP-TEE -> *Cortex-A SPL* -> *U-Boot* -> Kernel

**With falcon mode:**

* R5 SPL -> ATF -> OP-TEE -> Kernel

Falcon boot support is added by the ``ti-falcon`` yocto override which can be
enabled before :ref:`building the SDK <building-the-sdk-with-yocto>` as follows:

.. code-block:: console

   $ echo 'DISTROOVERRIDES:append = ":ti-falcon"' >> conf/local.conf
   $ # build the SDK
   $ MACHINE=<machine> bitbake -k tisdk-default-image

-------------------------------------
Changes made by *ti-falcon* override:
-------------------------------------

ATF:
----

To meet the 2MiB alignment requirement for the linux kernel's load address,
the ``K3_HW_CONFIG_BASE`` *(kernel address)* and ``PRELOADED_BL33_BASE``
*(DTB address)* for ATF are modified from K3 defaults to ``0x82000000`` and
``0x88000000`` respectively.

TISPL:
------

Falcon mode makes use of a cut down variant of the tispl binary called
``tifalcon.bin`` with the Cortex-A SPL and it’s corresponding DTB removed.
This file is deployed to the boot directory inside rootfs so it can be picked by
the R5 SPL at boot time.

R5 SPL:
-------

The R5 SPL is used for loading the kernel ``fitImage`` as well as the
``tifalcon.bin`` file, though the ``fitImage`` for falcon boot is signed
using an x509 certificate with TIFS keys instead of making use of signature
nodes and keys present in the DT. This allows for faster authentication since
TIFS uses the security accelerator for authentication which is much faster than
doing the same on R5 core.

This support depends on the U-Boot's ``k3_r5_falcon.config`` fragment, which is
built alongside the standard R5 defconfig when ``ti-falcon`` is enabled.

fitImage:
---------

The resulting ``fitImage`` file in the boot directory of rootfs is produced
with the constituent binaries pre-signed with x509 certificates. This file is
authenticated from TIFS at boot time which allows for a lower boot time than
authenticating on the R5 core.

-------------------
Extra Configuration
-------------------

.. ifconfig:: CONFIG_part_variant not in ('AM62AX')

   OSPI boot:
   ----------

   For OSPI boot, the ``tiboot3.bin`` and ``tifalcon.bin`` files should be
   flashed to the same addresses in flash as regular boot flow but the DTB and
   the ``fitImage`` are read from the rootfs's boot directory.

   Below U-Boot commands can be used to download ``tiboot3.bin`` and
   ``tifalcon.bin`` over tftp and then flash those to OSPI at their respective
   addresses.

   .. code-block:: console

      => sf probe
      => tftp ${loadaddr} tiboot3.bin
      => sf update $loadaddr 0x0 $filesize
      => tftp ${loadaddr} tifalcon.bin
      => sf update $loadaddr 0x80000 $filesize

eMMC Boot:
----------

In eMMC boot mode, the ``tiboot3.bin`` file should be flashed to the hardware
boot partition whereas ``tifalcon.bin`` and the ``fitImage`` are read from
the rootfs inside UDA. Use the U-Boot commands below to set the correct boot
partition and write ``tiboot3.bin`` to the correct offset.

.. code-block:: console

   => # Set boot0 as the boot partition
   => mmc partconf 0 1 1 1
   => mmc bootbus 0 2 0 0
   => # Flash tiboot3.bin to boot0
   => mmc dev 0 1
   => fatload mmc 1 ${loadaddr} tiboot3.bin
   => mmc write ${loadaddr} 0x0 0x400

For more information check: :ref:`How to flash eMMC and boot with eMMC Boot
<how-to-emmc-boot>`.

Custom fitImage creation:
-------------------------

Clone the `core-secdev-k3 source <https://git.ti.com/cgit/security-development-tools/core-secdev-k3>`__:

.. code-block:: console

   $ git clone https://git.ti.com/cgit/security-development-tools/core-secdev-k3

Copy the required kernel image renamed to ``Image`` and the DTB renamed to
``falcon.dtb`` inside the core-secdev-k3 source directory.

Copy the following contents to a file named ``fitImage.its`` inside
core-secdev-k3 source:

.. code-block:: dts

   /dts-v1/;

   / {
       description = "Kernel fitImage for falcon mode";
       #address-cells = <1>;

       images {
           kernel-1 {
               description = "Linux kernel";
               data = /incbin/("Image.sec");
               type = "kernel";
               arch = "arm64";
               os = "linux";
               compression = "none";
               load = <0x82000000>;
               entry = <0x82000000>;
           };
           falcon.dtb {
               description = "Flattened Device Tree blob";
               data = /incbin/("falcon.dtb.sec");
               type = "flat_dt";
               arch = "arm64";
               compression = "none";
               load = <0x88000000>;
           };
       };

       configurations {
           default = "conf-falcon";
           conf-falcon {
               description = "Presigned Kernel and DTB";
               kernel = "kernel-1";
               fdt = "falcon.dtb";
           };
       };
   };

Sign the kernel and dtb using ``secure-binary-image.sh`` and create the
``fitImage`` using mkimage:

.. code-block:: console

   $ # inside core-secdev-k3 source
   $ ./scripts/secure-binary-image.sh Image Image.sec
   $ ./scripts/secure-binary-image.sh falcon.dtb falcon.dtb.sec
   $ mkimage -f fitImage.its fitImage

----------------------
Boot time comparisons:
----------------------

Removing A-core SPL and U-Boot from the boot process leads to ~60% reduction in
time to kernel. Saving about 1-2 seconds during boot depending on the platform.

**Falcon Mode (Left) vs Regular Boot (Right):**

  .. Image:: /images/U-Boot_Falcon_Comparison.gif
