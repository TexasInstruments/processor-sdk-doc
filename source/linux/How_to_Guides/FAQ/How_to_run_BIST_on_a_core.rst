##############################
How to trigger BIST on a core?
##############################

   Built-in Self-test (BIST) is a feature that allows self testing of the memory
   areas and logic circuitry in an Integrated Circuit (IC) without any external
   test equipment. In an embedded system, these tests are typically used during
   boot time or shutdown of the system to check the health of an SoC.
   PBIST is used to test the memory regions in the SoC and provides detection for
   permanent faults. The primary use case for PBIST is when it is invoked at
   start-up providing valuable information on any stuck-at bits in the memory.
   LBIST is used to test the logic circuitry in an SoC associated with the CPU
   cores. There are multiple LBIST instances in the SoC, and each has a different
   processor core associated with it. There are LBIST tests that can be
   software-initiated.

      - Current implementation triggers the BIST tests on the MAIN_R5_2_x cores.

      - LBIST/PBIST checks of the WKUP_DMSC0 and MCU_R5FSS0 cores and memories are
        run in the WKUP/MCU domain; this check is part of HW POST. HW POST runs in
        hardware, before the ROM code starts and can be selected by MCU_BOOTMODE[09:08]
        pins.

*********************************
Steps to trigger BIST from U-Boot
*********************************

   - Enable the BIST config at A72 SPL stage:

       .. code-block:: diff

          diff --git a/configs/j784s4_evm_a72_defconfig b/configs/j784s4_evm_a72_defconfig
          index 52d12b6206b..1d2b4c3262f 100644
          --- a/configs/j784s4_evm_a72_defconfig
          +++ b/configs/j784s4_evm_a72_defconfig
          @@ -1,3 +1,4 @@
          +CONFIG_K3_BIST=y
          CONFIG_ARM=y
          CONFIG_ARCH_K3=y
          CONFIG_SYS_MALLOC_LEN=0x2000000

   - Debug logs may be enabled if needed:

       .. code-block:: diff

          diff --git a/drivers/misc/k3_bist.c b/drivers/misc/k3_bist.c
          index fd3140add68..6668de93ab2 100644
          --- a/drivers/misc/k3_bist.c
          +++ b/drivers/misc/k3_bist.c
          @@ -6,7 +6,7 @@
          *      Neha Malcom Francis <n-francis@ti.com>
          *
          */
          -
          +#define LOG_DEBUG
          #include <dm.h>
          #include <errno.h>
          #include <clk.h>

   - Rebuild A72 SPL image (tispl.bin) with the above changes to enable BIST tests
     to run on a particular core.

   - While booting to the U-Boot prompt, your prints should be similar to the log
     below:

      .. code-block:: console

         U-Boot SPL 2025.01-00253-g9a3137c5c11a-dirty (Feb 28 2025 - 09:48:36 +0530)
         SYSFW ABI: 4.0 (firmware rev 0x000a '10.1.6--v10.01.06 (Fiery Fox)')
         Initialized 4 DRAM controllers
         SPL initial stack usage: 13440 bytes
         Trying to boot from MMC2
         Skipping authentication on GP device
         Skipping authentication on GP device
         Skipping authentication on GP device
         Skipping authentication on GP device
         Skipping authentication on GP device
         Loading Environment from nowhere... OK
         Starting ATF on ARM64 core...

         NOTICE:  BL31: v2.12.0(release):5227171c0-dirty
         NOTICE:  BL31: Built : 13:45:40, Feb  3 2025
         I/TC:
         I/TC: OP-TEE version: 4.5.0-73-gef1ebdc23-dev (gcc version 13.3.0 (GCC)) #1 Tue Feb  4 11:33:18 UTC 2025 aarch64
         I/TC: WARNING: This OP-TEE configuration might be insecure!
         I/TC: WARNING: Please check https://optee.readthedocs.io/en/latest/architecture/porting_guidelines.html
         I/TC: Primary CPU initializing
         I/TC: GIC redistributor base address not provided
         I/TC: Assuming default GIC group status and modifier
         I/TC: SYSFW ABI: 4.0 (firmware rev 0x000a '10.1.6--v10.01.06 (Fiery Fox)')
         I/TC: Activated SA2UL device
         I/TC: Fixing SA2UL firewall owner for GP device
         I/TC: Enabled firewalls for SA2UL TRNG device
         I/TC: SA2UL TRNG initialized
         I/TC: SA2UL Drivers initialized
         I/TC: HUK Initialized
         I/TC: Primary CPU switching to normal world boot

         U-Boot SPL 2025.01-00253-g9a3137c5c11a-dirty (Feb 28 2025 - 09:48:54 +0530)
         SYSFW ABI: 4.0 (firmware rev 0x000a '10.1.6--v10.01.06 (Fiery Fox)')
         k3_bist_probe(dev=8047a548)
         check_post_pbist_result: HW POST PBIST completed, test passed
         check_post_lbist_result: HW POST LBIST completed, test passed
         lbist_start(dev=8047a548): LBIST is running
         Trying to boot from MMC2
         Skipping authentication on GP device
         Skipping authentication on GP device


         U-Boot 2025.01-00253-g9a3137c5c11a-dirty (Feb 28 2025 - 09:48:54 +0530)

         SoC:   J784S4 SR1.0 GP
         Model: Texas Instruments J784S4 EVM
         DRAM:  2 GiB (effective 32 GiB)
         Core:  143 devices, 35 uclasses, devicetree: separate
         Flash: 0 Bytes
         MMC:   mmc@4f80000: 0, mmc@4fb0000: 1
         Loading Environment from nowhere... OK
         In:    serial@2880000
         Out:   serial@2880000
         Err:   serial@2880000
         am65_cpsw_nuss ethernet@46000000: K3 CPSW: nuss_ver: 0x6BA02102 cpsw_ver: 0x6BA82102 ale_ver: 0x00293904 Ports:1
         Net:   eth0: ethernet@46000000port@1
         Hit any key to stop autoboot:  0
         =>


   - Run and load firmware on the core as usual:

      .. code-block:: console

         => rproc init
         k3_r5f_rproc r5f@41000000: Core 1 is already in use. No rproc commands work
         k3_r5f_rproc r5f@41400000: Core 2 is already in use. No rproc commands work
         => load mmc 1:2 0x90000000 /lib/firmware/j784s4-main-r5f2_0-fw
         80600 bytes read in 37 ms (2.1 MiB/s)
         => rproc load 6 0x90000000 0x${filesize}
         Load Remote Processor 6 with data@addr=0x90000000 80600 bytes: Success!
         => rproc start 6
         =>
