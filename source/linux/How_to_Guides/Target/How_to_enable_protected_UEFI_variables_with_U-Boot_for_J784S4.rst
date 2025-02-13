How to enable Protected UEFI Variables in U-Boot for the J784S4 and AM69 platforms
==================================================================================

This article details the process of enabling protected UEFI variables in U-Boot specifically for
the J784S4 platforms. Protected UEFI variables offer a secure storage mechanism within the board's
eMMC flash, accessible only by authorized software. This is crucial for safeguarding sensitive data
like cryptographic keys and passwords.

While the eMMC device is typically managed by the non-secure world (e.g., Linux), EFI variables can
be securely stored in the eMMC's RPMB partition. This implementation leverages OP-TEE, a StandaloneMM
pseudo TA for EFI variable services, the eMMC driver, tee-supplicant, and a dedicated tee-based
variable access driver.


Prerequisites
-------------

Before starting, ensure you have the following:

* A J784S4 board (for the purpose of this article we're going to use the AM69-SK Starter Kit)
* A U-Boot source tree configured for the AM69-SK.
* A Linux host machine for building U-Boot.
* Familiarity with building U-Boot.


Build StandaloneMM as EFI Variable Service Pseudo TA
----------------------------------------------------

As described in the `U-Boot documentation <https://docs.u-boot.org/en/latest/develop/uefi/uefi.html#using-op-tee-for-efi-variables>`_,
UEFI variable services can be implemented in the secure world using an OP-TEE module, rather than within U-Boot itself.  This approach
leverages Tianocore EDK II's standalone management mode driver, linked to OP-TEE, and uses the
eMMC's RPMB for persistent storage of non-volatile variables.

These are the steps to build StandaloneMM.

1. **Clone the EDK2 Repositories:**

   ```bash
   git clone https://github.com/tianocore/edk2.git
   git clone https://github.com/tianocore/edk2-platforms.git
   cd edk2
   git submodule init && git submodule update --init --recursive
   ```

2. **Build the StandaloneMM application:**

   ```bash
   cd ..
   export WORKSPACE=$(pwd)
   export PACKAGES_PATH=$WORKSPACE/edk2:$WORKSPACE/edk2-platforms
   export ACTIVE_PLATFORM="Platform/StandaloneMm/PlatformStandaloneMmPkg/PlatformStandaloneMmRpmb.dsc"
   export GCC5_AARCH64_PREFIX=aarch64-linux-gnu-
   source edk2/edksetup.sh
   make -C edk2/BaseTools
   build -p $ACTIVE_PLATFORM -b RELEASE -a AARCH64 -t GCC5 -n `nproc`
   ```

   This will generate the StandaloneMM image (e.g., `BL32_AP_MM.fd`) in the `Build/MmStandaloneRpmb/RELEASE_GCC5/FV/` directory.


Build OP-TEE including StandaloneMM application
-----------------------------------------------

As the Open Portable Trusted Execution Environment (OP-TEE) needs to include the StandaloneMM
application we need to rebuild OP-TEE, some extra parameters needs to be passed as described below.

1. **Setup the build environment variables:**

   ```bash
   export CC32=arm-linux-gnu-
   export CC64=aarch64-linux-gnu-
   export OPTEE_PLATFORM=k3-j784s4
   export OPTEE_EXTRA_ARGS="CFG_CONSOLE_UART=0x8"
   ```

2. **Clone and configure OP-TEE to include StandaloneMM**

   ```bash
   git clone https://github.com/OP-TEE/optee_os.git
   cd optee_os
   ln -s ../Build/MmStandaloneRpmb/RELEASE_GCC5/FV/BL32_AP_MM.fd
   ```

3. **Build OP-TEE using the RPMB and STMM configs**

   ```
   make CROSS_COMPILE="$CC32" CROSS_COMPILE64="$CC64" \
	   PLATFORM="$OPTEE_PLATFORM" CFG_ARM64_core=y $OPTEE_EXTRA_ARGS \
	   CFG_RPMB_FS_DEV_ID=0 CFG_REE_FS=n CFG_RPMB_FS=y \
	   CFG_RPMB_WRITE_KEY=y CFG_RPMB_TESTKEY=y \
	   CFG_STMM_PATH=BL32_AP_MM.fd \
	   CFG_CORE_HEAP_SIZE=524288 CFG_CORE_DYN_SHM=y CFG_SCTLR_ALIGNMENT_CHECK=n \
	   CFG_TEE_CORE_LOG_LEVEL=1 CFG_TEE_CORE_DEBUG=y CFG_TEE_TA_LOG_LEVEL=1
   ```

..warning::
   OP-TEE will program the RPMB key (which is one time programmable). On your first boot, if the
   RPMB key is not programmed, OP-TEE will do that for you. If your platform port of OP-TEE doesn't
   have a way of retrieving a secure key from the hardware you might end up with the default
   CFG_RPMB_TESTKEY (which makes your system unsecure)


Assembling the final image
--------------------------

The build steps for U-Boot should be standard. For assembling the final image you must take in consideration
the following steps:

1. **Enable OP-TEE and RPMB support**

   This can be activated specifying:

   ```bash
   CONFIG_TEE=y
   CONFIG_OPTEE=y
   CONFIG_CMD_OPTEE_RPMB=y
   CONFIG_EFI_MM_COMM_TEE=y
   CONFIG_SUPPORT_EMMC_RPMB=y
   ```

2. **Build U-boot using the OP-TEE binary**

   Building u-boot is pretty standard, you can follow the `U-Boot documentation <https://docs.u-boot.org/en/latest/board/ti/j784s4_evm.html>`_,
   just remember to link against the OP-TEE binary previously built.


Testing protected EFI runtime variables service from U-Boot
------------------------------------------------------------

Notice OP-TEE probing before accessing the variables (E.g. OP-TEE: revision 4.4 (dd7b51e590c4ddae))

The `printenv -e` command is used to print environment for UEFI variables.

   ```
   => printenv -e
   SetupMode:
      8be4df61-93ca-11d2-aa0d-00e098032b8c (EFI_GLOBAL_VARIABLE_GUID)
      BS|RT|RO, DataSize = 0x1
      00000000: 01                                               .
   SecureBoot:
      8be4df61-93ca-11d2-aa0d-00e098032b8c (EFI_GLOBAL_VARIABLE_GUID)
      BS|RT|RO, DataSize = 0x1
      00000000: 00                                               .
   certdbv:
      d9bee56e-75dc-49d9-b4d7-b534210f637a (d9bee56e-75dc-49d9-b4d7-b534210f637a)
      2106-01-25 07:33:52
      BS|RT|AT|RO, DataSize = 0x4
      00000000: 04 00 00 00                                      ....
   AuditMode:
      8be4df61-93ca-11d2-aa0d-00e098032b8c (EFI_GLOBAL_VARIABLE_GUID)
      BS|RT|RO, DataSize = 0x1
      00000000: 00                                               .
   DeployedMode:
      8be4df61-93ca-11d2-aa0d-00e098032b8c (EFI_GLOBAL_VARIABLE_GUID)
      BS|RT|RO, DataSize = 0x1
      00000000: 00                                               .
   VendorKeys:
      8be4df61-93ca-11d2-aa0d-00e098032b8c (EFI_GLOBAL_VARIABLE_GUID)
      BS|RT|RO, DataSize = 0x1
      00000000: 00                                               .
   PlatformLangCodes:
      8be4df61-93ca-11d2-aa0d-00e098032b8c (EFI_GLOBAL_VARIABLE_GUID)
      BS|RT|RO, DataSize = 0x6
      00000000: 65 6e 2d 55 53 00                                en-US.
   OsIndicationsSupported:
      8be4df61-93ca-11d2-aa0d-00e098032b8c (EFI_GLOBAL_VARIABLE_GUID)
      BS|RT|RO, DataSize = 0x8
      00000000: 00 00 00 00 00 00 00 00                          ........
   SignatureSupport:
      8be4df61-93ca-11d2-aa0d-00e098032b8c (EFI_GLOBAL_VARIABLE_GUID)
      BS|RT|RO, DataSize = 0x20
      00000000: 26 16 c4 c1 4c 50 92 40 ac a9 41 f9 36 93 43 28  &...LP.@..A.6.C(
      00000010: a1 59 c0 a5 e4 94 a7 4a 87 b5 ab 15 5c 2b f0 72  .Y.....J....\+.r
   CustomMode:
      c076ec0c-7028-4399-a072-71ee5c448b9f (c076ec0c-7028-4399-a072-71ee5c448b9f)
      NV|BS, DataSize = 0x1
      00000000: 00                                               .
   certdb:
      d9bee56e-75dc-49d9-b4d7-b534210f637a (d9bee56e-75dc-49d9-b4d7-b534210f637a)
      2106-01-25 07:33:52
      NV|BS|RT|AT|RO, DataSize = 0x4
      00000000: 04 00 00 00                                      ....
   VendorKeysNv:
      9073e4e0-60ec-4b6e-9903-4c223c260f3c (9073e4e0-60ec-4b6e-9903-4c223c260f3c)
      2106-01-25 07:33:52
      NV|BS|AT|RO, DataSize = 0x1
      00000000: 01                                               .
   Boot0000:
      8be4df61-93ca-11d2-aa0d-00e098032b8c (EFI_GLOBAL_VARIABLE_GUID)
      NV|BS|RT, DataSize = 0x68
      00000000: 01 00 00 00 46 00 6d 00 6d 00 63 00 20 00 30 00  ....F.m.m.c. .0.
      00000010: 00 00 01 04 1c 00 b9 73 1d e6 84 a3 cc 4a ae ab  .......s.....J..
      00000020: 82 e8 28 f3 62 8b 00 00 00 00 00 00 00 00 01 04  ..(.b...........
      00000030: 1c 00 b9 73 1d e6 84 a3 cc 4a ae ab 82 e8 28 f3  ...s.....J....(.
      00000040: 62 8b 6d 00 00 00 00 00 00 00 03 1d 05 00 00 03  b.m.............
      00000050: 1d 05 00 00 7f ff 04 00 4e ac 08 81 11 9f 59 4d  ........N.....YM
      00000060: 85 0e e2 1a 52 2c 59 b2                          ....R,Y.
   PlatformLang:
      8be4df61-93ca-11d2-aa0d-00e098032b8c (EFI_GLOBAL_VARIABLE_GUID)
      NV|BS|RT, DataSize = 0x6
      00000000: 65 6e 2d 55 53 00                                en-US.
   Boot0002:
      8be4df61-93ca-11d2-aa0d-00e098032b8c (EFI_GLOBAL_VARIABLE_GUID)
      NV|BS|RT, DataSize = 0x78
      00000000: 01 00 00 00 64 00 46 00 65 00 64 00 6f 00 72 00  ....d.F.e.d.o.r.
      00000010: 61 00 00 00 04 01 2a 00 01 00 00 00 00 48 00 00  a.....*......H..
      00000020: 00 00 00 00 00 40 06 00 00 00 00 00 67 80 74 c1  .....@......g.t.
      00000030: 00 00 00 00 00 00 00 00 00 00 00 00 01 01 04 04  ................
      00000040: 36 00 5c 00 45 00 46 00 49 00 5c 00 66 00 65 00  6.\.E.F.I.\.f.e.
      00000050: 64 00 6f 00 72 00 61 00 5c 00 73 00 68 00 69 00  d.o.r.a.\.s.h.i.
      00000060: 6d 00 61 00 61 00 36 00 34 00 2e 00 65 00 66 00  m.a.a.6.4...e.f.
      00000070: 69 00 00 00 7f ff 04 00                          i.......
   Boot0001:
      8be4df61-93ca-11d2-aa0d-00e098032b8c (EFI_GLOBAL_VARIABLE_GUID)
      NV|BS|RT, DataSize = 0x78
      00000000: 01 00 00 00 64 00 46 00 65 00 64 00 6f 00 72 00  ....d.F.e.d.o.r.
      00000010: 61 00 00 00 04 01 2a 00 01 00 00 00 00 08 00 00  a.....*.........
      00000020: 00 00 00 00 00 60 09 00 00 00 00 00 5b 90 b2 68  .....`......[..h
      00000030: 3e df b3 4f 80 fa 49 d1 e7 73 aa 33 02 02 04 04  >..O..I..s.3....
      00000040: 36 00 5c 00 45 00 46 00 49 00 5c 00 66 00 65 00  6.\.E.F.I.\.f.e.
      00000050: 64 00 6f 00 72 00 61 00 5c 00 73 00 68 00 69 00  d.o.r.a.\.s.h.i.
      00000060: 6d 00 61 00 61 00 36 00 34 00 2e 00 65 00 66 00  m.a.a.6.4...e.f.
      00000070: 69 00 00 00 7f ff 04 00                          i.......
   LoaderSystemToken:
      4a67b082-0a4c-41cf-b6c7-440b29bb8c4f (4a67b082-0a4c-41cf-b6c7-440b29bb8c4f)
      NV|BS|RT, DataSize = 0x20
      00000000: 74 6e c8 c6 37 86 90 55 d6 f0 43 95 ad ab 83 5a  tn..7..U..C....Z
      00000010: 36 b4 94 88 5d e7 c1 06 62 88 62 1a 98 10 23 44  6...]...b.b...#D
   Boot0003:
      8be4df61-93ca-11d2-aa0d-00e098032b8c (EFI_GLOBAL_VARIABLE_GUID)
      NV|BS|RT, DataSize = 0xa2
      00000000: 01 00 00 00 76 00 4c 00 69 00 6e 00 75 00 78 00  ....v.L.i.n.u.x.
      00000010: 20 00 42 00 6f 00 6f 00 74 00 20 00 4d 00 61 00   .B.o.o.t. .M.a.
      00000020: 6e 00 61 00 67 00 65 00 72 00 00 00 04 01 2a 00  n.a.g.e.r.....*.
      00000030: 01 00 00 00 00 08 00 00 00 00 00 00 00 60 09 00  .............`..
      00000040: 00 00 00 00 5b 90 b2 68 3e df b3 4f 80 fa 49 d1  ....[..h>..O..I.
      00000050: e7 73 aa 33 02 02 04 04 48 00 5c 00 45 00 46 00  .s.3....H.\.E.F.
      00000060: 49 00 5c 00 73 00 79 00 73 00 74 00 65 00 6d 00  I.\.s.y.s.t.e.m.
      00000070: 64 00 5c 00 73 00 79 00 73 00 74 00 65 00 6d 00  d.\.s.y.s.t.e.m.
      00000080: 64 00 2d 00 62 00 6f 00 6f 00 74 00 61 00 61 00  d.-.b.o.o.t.a.a.
      00000090: 36 00 34 00 2e 00 65 00 66 00 69 00 00 00 7f ff  6.4...e.f.i.....
      000000a0: 04 00                                            ..
   SbatLevel:
      605dab50-e046-4300-abb6-3dd810dd8b23 (605dab50-e046-4300-abb6-3dd810dd8b23)
      NV|BS, DataSize = 0x12
      00000000: 73 62 61 74 2c 31 2c 32 30 32 31 30 33 30 32 31  sbat,1,202103021
      00000010: 38 0a                                            8.
   BootOrder:
      8be4df61-93ca-11d2-aa0d-00e098032b8c (EFI_GLOBAL_VARIABLE_GUID)
      NV|BS|RT, DataSize = 0x8
      00000000: 02 00 03 00 01 00 00 00                          ........
   ```

To check the available storage, use the `efidebug` command:

   ```bash
   => efidebug query -bs -rt -nv
   Max storage size 16284
   Remaining storage size 14724
   Max variable size 8132
   ```
You can set (`setenv -e`) and get (`printenv -e`) UEFI variables:

   ```bash
   => setenv -e -nv -bs -rt test 1234
   => printenv -e test
   test:
    8be4df61-93ca-11d2-aa0d-00e098032b8c (EFI_GLOBAL_VARIABLE_GUID)
    NV|BS|RT, DataSize = 0x4
    00000000: 31 32 33 34                                      1234
   ```


Testing protected EFI runtime variables service from Linux
-----------------------------------------------------------

When OP-TEE is compiled to include StandAloneMM. the `tee_stmm_efi` (`CONFIG_TEE_STMM_EFI`) driver
has the ability to check and store EFI variables on an RPMB or any other non-volatile medium used
by StandAloneMM.

First check that OP-TEE is up and running. E.e:

   ```bash
   # dmesg | grep tee
   [    0.000000] OF: reserved mem: 0x000000009e800000..0x000000009fffffff (24576 KiB) nomap non-reusable optee@9e800000
   [    6.599969] optee: probing for conduit method.
   [    6.600010] optee: revision 4.4 (dd7b51e590c4ddae)
   [    6.600714] optee: dynamic shared memory is enabled
   [    6.601188] optee: initialized driver
   ```

Linux needs a user space supplicant daemon (`tee-supplicant``) which is responsible for remote
services expected by the TEE OS. Running the daemon can be done with:

   ```bash
   # tee-suplicant
   ```

This should load the `tee_stmm_efi` driver module and register the efivars operations:

   ```bash
   [    7.392466] efivars: Unregistered efivars operations
   [    7.392483] Using TEE-based EFI runtime variable services
   [    7.392488] efivars: Registered efivars operations
   ```

The `efivar` command is used to print environment for UEFI variables.


   ```bash
   # efivar --list
   8be4df61-93ca-11d2-aa0d-00e098032b8c-BootOrder
   8be4df61-93ca-11d2-aa0d-00e098032b8c-test
   8be4df61-93ca-11d2-aa0d-00e098032b8c-Boot0003
   4a67b082-0a4c-41cf-b6c7-440b29bb8c4f-LoaderSystemToken
   8be4df61-93ca-11d2-aa0d-00e098032b8c-Boot0001
   8be4df61-93ca-11d2-aa0d-00e098032b8c-Boot0002
   8be4df61-93ca-11d2-aa0d-00e098032b8c-PlatformLang
   8be4df61-93ca-11d2-aa0d-00e098032b8c-Boot0000
   d9bee56e-75dc-49d9-b4d7-b534210f637a-certdb
   4a67b082-0a4c-41cf-b6c7-440b29bb8c4f-LoaderTimeExecUSec
   4a67b082-0a4c-41cf-b6c7-440b29bb8c4f-LoaderEntrySelected
   4a67b082-0a4c-41cf-b6c7-440b29bb8c4f-LoaderTimeMenuUSec
   4a67b082-0a4c-41cf-b6c7-440b29bb8c4f-LoaderEntries
   4a67b082-0a4c-41cf-b6c7-440b29bb8c4f-LoaderDevicePartUUID
   4a67b082-0a4c-41cf-b6c7-440b29bb8c4f-LoaderImageIdentifier
   4a67b082-0a4c-41cf-b6c7-440b29bb8c4f-LoaderFeatures
   4a67b082-0a4c-41cf-b6c7-440b29bb8c4f-LoaderFirmwareType
   4a67b082-0a4c-41cf-b6c7-440b29bb8c4f-LoaderFirmwareInfo
   4a67b082-0a4c-41cf-b6c7-440b29bb8c4f-LoaderInfo
   4a67b082-0a4c-41cf-b6c7-440b29bb8c4f-LoaderTimeInitUSec
   605dab50-e046-4300-abb6-3dd810dd8b23-ShimRetainProtocol
   8be4df61-93ca-11d2-aa0d-00e098032b8c-BootCurrent
   8be4df61-93ca-11d2-aa0d-00e098032b8c-SignatureSupport
   8be4df61-93ca-11d2-aa0d-00e098032b8c-OsIndicationsSupported
   8be4df61-93ca-11d2-aa0d-00e098032b8c-PlatformLangCodes
   8be4df61-93ca-11d2-aa0d-00e098032b8c-VendorKeys
   8be4df61-93ca-11d2-aa0d-00e098032b8c-DeployedMode
   8be4df61-93ca-11d2-aa0d-00e098032b8c-AuditMode
   d9bee56e-75dc-49d9-b4d7-b534210f637a-certdbv
   8be4df61-93ca-11d2-aa0d-00e098032b8c-SecureBoot
   8be4df61-93ca-11d2-aa0d-00e098032b8c-SetupMode
   ```


Using the same program, you can set (`efivar -p`) and get (`efivar -w`) UEFI variables:

   ```bash
   # efivar -p -n 8be4df61-93ca-11d2-aa0d-00e098032b8c-test
   GUID: 8be4df61-93ca-11d2-aa0d-00e098032b8c
   Name: "test"
   Attributes:
      Non-Volatile
      Boot Service Access
      Runtime Service Access
   Value:
   00000000  31 32 33 34                                       |1234            |
   ```

Finally, to not start the the daemon manually, you can easily integrate as a systemd service (E.g. `tee-supplicant.service`)

   ```bash
   [Unit]
   Description=TEE-Supplicant
   After=systemd-sysctl.service local-fs.target
   Before=systemd-networkd.service

   [Service]
   Type=forking
   PermissionsStartOnly=true
   ExecStart=/usr/sbin/tee-supplicant -d /dev/teepriv0

   [Install]
   WantedBy=multi-user.target
   ```

Conclusion
----------

By following these steps, you can successfully enable and utilize protected UEFI variables on your J784S4 or AM69 board,
enhancing the security of your embedded system. Remember to consult the U-Boot documentation for the most up-to-date
information and advanced options.
s