RemoteProc
------------

This section documents how to initialize, load, start and stop remote cores from U-Boot prompt.
Following remotecores support is available in U-boot for K3 devices. However the actual remote
cores deployed depends on the specific SoC used:

-  Cortex-R5F in Lockstep more
-  Cortex-R5F in split mode
-  Cortex-M4F
-  C66x DSP
-  C71x DSP

Initialization
^^^^^^^^^^^^^^^

U-Boot supports for initializing all the available remotecores in one go or
initialize individual core based on the DT alias id.

The below command will initialize all the available remote cores:

.. code-block:: console

   => rproc init

The below command will initialize just the given remote core

.. code-block:: console

   => rproc init <id>

The below command lists all the available/initialized remotecores in a system.

.. code-block:: console

   => rproc list
   0 - Name:'r5f@41000000' type:'internal memory mapped' supports: load start stop reset
   1 - Name:'r5f@41400000' type:'internal memory mapped' supports: load start stop reset
   2 - Name:'r5f@5c00000' type:'internal memory mapped' supports: load start stop reset
   3 - Name:'r5f@5d00000' type:'internal memory mapped' supports: load start stop reset
   4 - Name:'r5f@5e00000' type:'internal memory mapped' supports: load start stop reset
   5 - Name:'r5f@5f00000' type:'internal memory mapped' supports: load start stop reset
   6 - Name:'dsp@4d80800000' type:'internal memory mapped' supports: load start stop reset
   7 - Name:'dsp@4d81800000' type:'internal memory mapped' supports: load start stop reset
   8 - Name:'dsp@64800000' type:'internal memory mapped' supports: load start stop reset


Loading
^^^^^^^^

Once Initialized, remotecores can be loaded with a relevant image. Make sure
image is loaded only after initializing the core.

.. code-block:: console

   => load mmc 1:2 0x90000000 /lib/firmware/j7-main-r5f0_0-fw
   2536540 bytes read in 112 ms (21.6 MiB/s)
   => rproc load 2 0x90000000 0x${filesize}
   Load Remote Processor 2 with data@addr=0x90000000 2536540 bytes: Success!


Starting
^^^^^^^^^

Successfully loaded remotecore can be started using the following command.

.. code-block:: console

   => rproc start 2

Stop
^^^^^

A running remotecore can be stopped using the following command.

.. code-block:: console

   => rproc stop 2

Make sure all the commands are run in the above given sequence. Currently IPC
is not supported in U-boot.

Lockstep and Split mode
^^^^^^^^^^^^^^^^^^^^^^^

.. ifconfig:: (CONFIG_sdk in ('SITARA')) or (CONFIG_part_variant in ('J722S'))

   .. note::

      This is not relevant for this platform and is only applicable to R5 clusters with lockstep suport.

Cortex-R5F can be used in both lockstep (both cores run same code) and split
mode (each core runs independently).

To set lockstep/split mode for R5 remote cores, use :code:`ti,cluster-mode`
property in the u-boot SoC device tree source. :code:`ti,cluster-mode` value
should be set to 1 for lockstep and 0 for split mode.

Furthermore, for setting lockstep/split mode for boot cores (which is MCU R5
in Jacinto platforms), an additional property named :code:`core-opts` in binman
dtsi needs to be updated. This is because the lockstep/split mode for boot
MCU R5 on Jacinto platforms is set by the ROM code itself, based on core-opts
value in the x509 certificate. :code:`core-opts` value in binman dtsi should be
set to 2 for split-mode, and 0 for lockstep mode for boot MCU R5 on Jacinto
platforms.

Refer to the below example on K3 J784S4 SoC.

.. rubric:: Lockstep configuration

* MAIN R5F:

   arch/arm/dts/k3-j784s4-main.dtsi

   .. code-block:: dts

      main_r5fss0: r5fss@5c00000 {
         compatible = "ti,j721s2-r5fss";
         ti,cluster-mode = <1>; # set to lockstep-mode
         #address-cells = <1>;
         #size-cells = <1>;
         ranges = <0x5c00000 0x00 0x5c00000 0x20000>,
         <0x5d00000 0x00 0x5d00000 0x20000>;
         power-domains = <&k3_pds 336 TI_SCI_PD_EXCLUSIVE>;
         ...

* Boot MCU R5F:

   arch/arm/dts/k3-j784s4-mcu-wakeup.dtsi

   .. code-block:: dts

      mcu_r5fss0: r5fss@41000000 {
         compatible = "ti,j721s2-r5fss";
         ti,cluster-mode = <1>; # set to lockstep-mode
         #address-cells = <1>;
         #size-cells = <1>;
         ranges = <0x41000000 0x00 0x41000000 0x20000>,
         ...

   arch/arm/dts/k3-j784s4-binman.dtsi

   .. code-block:: dts

      &binman {
         tiboot3-j784s4-gp-evm.bin { # In the case of GP boards
         filename = "tiboot3-j784s4-gp-evm.bin";
         symlink = "tiboot3.bin";
            ti-secure-rom {
               content = <&u_boot_spl_unsigned>, <&ti_fs_gp>,
               <&combined_tifs_cfg_gp>, <&combined_dm_cfg_gp>;
               combined;
               dm-data;
               core-opts = <0>; # core-opts value should be set to 0 for lockstep-mode on boot core
               content-sbl = <&u_boot_spl_unsigned>;
               load = <0x41c00000>;
               ...

.. rubric:: Split-mode configuration

* MAIN R5F:

   arch/arm/dts/k3-j784s4-main.dtsi

   .. code-block:: dts

      main_r5fss0: r5fss@5c00000 {
         compatible = "ti,j721s2-r5fss";
         ti,cluster-mode = <0>; # set to split-mode
         #address-cells = <1>;
         #size-cells = <1>;
         ranges = <0x5c00000 0x00 0x5c00000 0x20000>,
         <0x5d00000 0x00 0x5d00000 0x20000>;
         power-domains = <&k3_pds 336 TI_SCI_PD_EXCLUSIVE>;
         ...

* Boot MCU R5:

   arch/arm/dts/k3-j784s4-mcu-wakeup.dtsi

   .. code-block:: dts

      mcu_r5fss0: r5fss@41000000 {
         compatible = "ti,j721s2-r5fss";
         ti,cluster-mode = <0>; # set to split-mode
         #address-cells = <1>;
         #size-cells = <1>;
         ranges = <0x41000000 0x00 0x41000000 0x20000>,
         ...

   arch/arm/dts/k3-j784s4-binman.dtsi

   .. code-block:: dts

      &binman {
         tiboot3-j784s4-gp-evm.bin { # In the case of GP boards
         filename = "tiboot3-j784s4-gp-evm.bin";
         symlink = "tiboot3.bin";
         ti-secure-rom {
            content = <&u_boot_spl_unsigned>, <&ti_fs_gp>,
            <&combined_tifs_cfg_gp>, <&combined_dm_cfg_gp>;
            combined;
            dm-data;
            core-opts = <2>; # core-opts value should be set to 2 for split-mode on boot core
            content-sbl = <&u_boot_spl_unsigned>;
            load = <0x41c00000>;
            ...

.. note::

   From SDK 9.1 onward, default mode is split mode for boot cores.

HS Devices
^^^^^^^^^^

HS Devices by default use the secure firmware images present in the filesystem
for booting the remoteproc cores. Symlinks to these secure firmware images have
a suffix of `-sec` on them.

All the firmware images are authenticated while loading from U-boot.

Steps for signing and updating firmware images in filesystem.

* Getting Security Dev Tool

   .. code-block:: console

      $ git clone https://git.ti.com/git/security-development-tools/core-secdev-k3.git -b master
      $ export TI_SECURE_DEV_PKG=`pwd`/core-secdev-k3

* Export the path for secdev

   .. code-block:: console

      $ ${TI_SECURE_DEV_PKG}/scripts/secure-binary-image.sh $FIRMWARE $FIRMWARE.signed

* Updating firmware image

   .. code-block:: console

      $ ln -vfs $FIRMWARE.signed /lib/firmware/j7-main-r5f0_0-fw-sec
