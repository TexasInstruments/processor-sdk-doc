.. _crypto-accelerator:

######
Crypto
######

************
Introduction
************

The Crypto API Driver is a set of Linux drivers that provide access to the
hardware cryptographic accelerators. These drivers are available built-in
in the kernel in the current SDK release.

The following is a list of supported hardware accelerated algorithms:

.. ifconfig:: CONFIG_crypto in ('DTHEv2')

   .. list-table:: DTHEv2 Hardware Cryptography Support
      :header-rows: 1

      * - Device Family
        - Encryption
        - Encryption with Authentication
        - Hash Algorithms
        - MAC Algorithms

      * - AM62LX
        - AES (ECB, CBC, XTS, CTR)
        - AES-GCM, AES-CCM
        - MD5, SHA224, SHA256, SHA384, SHA512
        - HMAC(MD5), HMAC(SHA224), HMAC(SHA256), HMAC(SHA384), HMAC(SHA512)

.. ifconfig:: CONFIG_crypto in ('omap')

   .. list-table:: OMAP Hardware Cryptography Support
      :header-rows: 1

      * - Device Family
        - Encryption
        - Encryption with Authentication
        - Hash Algorithms
        - MAC Algorithms

      * - AM335X
        - AES, DES
        -
        - MD5, SHA1, SHA224, SHA256
        -

      * - AM437X
        - AES, DES, 3DES
        -
        - MD5, SHA1, SHA224, SHA256, SHA384, SHA512
        -

      * - AM57x / DRA7
        - AES, DES, 3DES
        -
        -
        -

.. ifconfig:: CONFIG_crypto in ('sa2ul')

   .. list-table:: SA2UL/SA3UL Hardware Cryptography Support
      :header-rows: 1

      * - Device Family
        - Encryption
        - Encryption with Authentication
        - Hash Algorithms
        - MAC Algorithms

      * - AM65x / J721e / J7200
        - AES (CBC, ECB), 3DES (CBC, ECB)
        - AES-GCM, AUTHENC(HMAC-SHA1, CBC-AES), AUTHENC(HMAC-SHA256, CBC-AES)
        - SHA1, SHA256, SHA512
        - HMAC(SHA1, SHA256, SHA512), CMAC(AES)

      * - J721S2 / J784S4 / J742S2
        - AES (CBC, ECB), 3DES (CBC, ECB)
        - AES-GCM, AUTHENC(HMAC-SHA1, CBC-AES), AUTHENC(HMAC-SHA256, CBC-AES)
        - SHA1, SHA256, SHA512
        - HMAC(SHA1, SHA256, SHA512), CMAC(AES)

      * - AM68 / AM69
        - AES (CBC, ECB), 3DES (CBC, ECB)
        - AES-GCM, AUTHENC(HMAC-SHA1, CBC-AES), AUTHENC(HMAC-SHA256, CBC-AES)
        - SHA1, SHA256, SHA512
        - HMAC(SHA1, SHA256, SHA512), CMAC(AES)

      * - AM64X / J722S
        - AES (CBC, ECB)
        - AES-GCM, AUTHENC(HMAC-SHA256, CBC-AES)
        - SHA256, SHA512
        - CMAC(AES)

      * - AM62X / AM62A / AM62D / AM62P
        - AES (CBC, ECB)
        - AES-GCM, AUTHENC(HMAC-SHA256, CBC-AES)
        - SHA256, SHA512
        - CMAC(AES)

*****************************
Crypto Implementation Options
*****************************

Users can implement cryptographic operations by using one of the following approaches:

1. **Hardware Accelerator**

   - Offloads crypto operations to dedicated hardware engine
   - Frees up CPU cycles for other tasks
   - In general lower throughput but optimized for multi-tasking systems

2. **ARM CPU with Cryptographic Extension (ARM CE)**

   - Uses ARM core's built-in cryptographic hardware level instruction extensions
   - Delivers higher throughput (faster than hardware accelerator)
   - Might require high CPU usage

Choosing the Right Implementation
=================================

**Use Hardware Accelerator when:**

- **Multi-tasking systems** - system runs computation heavy services that need CPU resources alongside crypto operations
- **Functional safety/security requirements** - ASIL or safety-critical applications require offloading crypto operations away from Linux kernel to reduce attack surface and ensure isolation
- **Compliance/regulatory requirements** - FIPS certification, Common Criteria, or TEE integration mandates hardware acceleration

**Use ARM CPU (CE) when:**

- **Maximum throughput required** - Need high throughput for bulk data encryption, video transcoding, or media processing
- **Dedicated crypto workload** - Crypto is the primary task and high CPU usage is acceptable
- **Small/infrequent operations** - One-time encryption with small data blocks where accelerator overhead is minimal

**Performance Comparison** : For a detailed comparison of hardware accelerator performance against ARM Cryptographic Extension (CE) and baseline ARM CPU, see :ref:`crypto-performance` in the Linux Performance Guide.

********************
Building the Drivers
********************

For devices with available cryptographic hardware accelerators, a Linux
driver and additionally a Cryptodev kernel module (for OpenSSL) is used
to access them.  Other devices use the pure software implementation of these
cryptographic operations.


.. ifconfig:: CONFIG_crypto in ('DTHEv2')

   |__PART_FAMILY_DEVICE_NAMES__| SoC supports a hardware accelerator called
   DATA TRANSFORM AND HASHING ENGINE (DTHE) v2 for crypto operations.

.. ifconfig:: CONFIG_crypto in ('sa2ul')

   |__PART_FAMILY_DEVICE_NAMES__| SoCs support a hardware accelerator called
   Security Accelerator 2/3 Ultra Light (SA2UL/SA3UL) for crypto operations.

The kernel configuration has already been set up in the SDK and no further
configuration is needed for the drivers to be built-in to the kernel.

For reference, the configuration details are shown below. The
configuration of the cryptographic drivers is done under the
Hardware crypto devices sub-menu of the Cryptographic API menu in the
kernel configuration.

.. ifconfig:: CONFIG_crypto in ('DTHEv2')

   .. code-block:: text

      Symbol: CRYPTO_DEV_TI_DTHEV2 [=m]
         | Type  : tristate
         | Prompt: Support for TI security accelerator
         |   Location:
         |     -> Cryptographic API (CRYPTO [=y])
         | (1)   -> Hardware crypto devices (CRYPTO_HW [=y])

   To check if DTHEv2 module is properly installed,
   run the below command from the Linux command prompt:

   .. code-block:: console

      lsmod | grep dthev2

   Output should show something similar to below:

   .. code-block:: text

      dthev2 262144 0

.. ifconfig:: CONFIG_crypto in ('sa2ul')

   .. code-block:: text

      Symbol: CRYPTO_DEV_SA2UL [=m]
         | Type  : tristate
         | Prompt: Support for TI security accelerator
         |   Location:
         |     -> Cryptographic API (CRYPTO [=y])
         | (1)   -> Hardware crypto devices (CRYPTO_HW [=y])

   To check if sa2ul module is properly installed,
   run the below command from the Linux command prompt:

   .. code-block:: console

      lsmod | grep sa2ul

   Output should show something similar to below:

   .. code-block:: text

      sa2ul 262144 0

.. ifconfig:: CONFIG_crypto in ('omap')

   .. code-block:: text

      --- Cryptographic API
         [*] Hardware crypto devices --->
               --- Hardware crypto devices
                  <*> Support for OMAP MD5/SHA1/SHA2 hw accelerator
                  <*> Support for OMAP AES hw engine
                  <*> Support for OMAP DES3DES hw engine

   Messages printed during bootup will indicate that initialization of the
   crypto modules has taken place.

   .. code-block:: console

      [    2.120565] omap-sham 53100000.sham: hw accel on OMAP rev 4.3
      [    2.160584] mmc1: BKOPS_EN bit is not set
      [    2.173466] omap-aes 53500000.aes: OMAP AES hw accel rev: 3.2
      [    2.180241] edma-dma-engine edma-dma-engine.0: allocated channel for 0:5
      [    2.187808] edma-dma-engine edma-dma-engine.0: allocated channel for 0:6

   For reference, the RNG configuration details are shown below.

   In the configuration menu, scroll down to Device Drivers and hit enter.
   Now scroll to Character devices and hit enter.

   .. code-block:: text

      Device Drivers --->
         Character devices --->
            < > Hardware Random Number Generator Core support
               < > OMAP Random Number Generator support

   Messages printed during bootup will indicate that initialization of the
   RNG module has taken place.

   .. code-block:: console

      [    1.660514] omap_rng 48310000.rng: OMAP Random Number Generator ver. 20

.. rubric:: Build the Cryptodev kernel module using SDK
   :name: build-the-cryptodev-kernel-module-using-sdk

For using OpenSSL to access the Crypto Hardware Accelerator Drivers
above, the Cryptodev is required (can be built as module). The framework
is not officially in the kernel and was ported to Linux under the name
"cryptodev". It is built as part of the SDK and no further configuration is needed.

******************************************************
Using Cryptographic Hardware Accelerators from OpenSSL
******************************************************

In order to use these drivers from OpenSSL, a
special driver is available which abstracts the access to these
accelerators through Cryprodev module.

Cryptodev is itself a special device driver which provides a general
interface for higher level applications such as OpenSSL to access
hardware accelerators.

The filesystem which comes with the SDK comes built with the Cryptodev
kernel modules and the TI driver which directly accesses the hardware
accelerators is built into the kernel.

The following shows the command used to query the system for the state of
the cryptodev module.

.. code-block:: console

   root@evm:~# lsmod | grep cryptodev
   cryptodev              11962  0

The following example demonstrates the OpenSSL built-in speed
test to demonstrate performance. The addition of the parameter **-engine
devcrypto** tells OpenSSL to use the Cryptodev driver if it exists.

.. code-block:: console

   root@evm:~# openssl speed -evp aes-128-cbc -engine devcrypto
   engine "devcrypto" set.
   Doing AES-128-CBC ops for 3s on 16 size blocks: 108107 AES-128-CBC ops in 0.16s
   Doing AES-128-CBC ops for 3s on 64 size blocks: 103730 AES-128-CBC ops in 0.20s
   Doing AES-128-CBC ops for 3s on 256 size blocks: 15181 AES-128-CBC ops in 0.03s
   Doing AES-128-CBC ops for 3s on 1024 size blocks: 15879 AES-128-CBC ops in 0.03s
   Doing AES-128-CBC ops for 3s on 8192 size blocks: 4879 AES-128-CBC ops in 0.02s
   version: 3.2.3
   built on: Tue Sep  3 12:52:35 2024 UTC
   options: bn(64,64)
   compiler: aarch64-oe-linux-gcc  -mbranch-protection=standard --sysroot=recipe-sysroot -O2 -pipe -g -feliminate-unused-debug-types -fcanon-prefix-map  -fmacro-prefix-map=  -fdebug-prefix-map=  -fmacro-prefix-mapG
   CPUINFO: OPENSSL_armcap=0xbd
   The 'numbers' are in 1000s of bytes per second processed.
   type             16 bytes     64 bytes     256 bytes     1024 bytes     8192 bytes
   AES-128-CBC      10810.70k    33193.60k    129544.53k     542003.20k    1998438.40k

Using the Linux time -v function gives more information about CPU usage
during the test.

.. code-block:: console

   root@evm:~# time -v openssl speed -evp aes-128-cbc -engine devcrypto
   Engine "devcrypto" set.
   Doing AES-128-CBC ops for 3s on 16 size blocks: 108799 AES-128-CBC ops in 0.17s
   Doing AES-128-CBC ops for 3s on 64 size blocks: 102699 AES-128-CBC ops in 0.18s
   Doing AES-128-CBC ops for 3s on 256 size blocks: 16166 AES-128-CBC ops in 0.03s
   Doing AES-128-CBC ops for 3s on 1024 size blocks: 15080 AES-128-CBC ops in 0.03s
   Doing AES-128-CBC ops for 3s on 8192 size blocks: 4838 AES-128-CBC ops in 0.03s
   version: 3.2.3
   built on: Tue Sep  3 12:52:35 2024 UTC
   options: bn(64,64)
   compiler: aarch64-oe-linux-gcc  -mbranch-protection=standard --sysroot=recipe-sysroot -O2 -pipe -g -feliminate-unused-debug-types -fcanon-prefix-map  -fmacro-prefix-map=  -fdebug-prefix-map=  -fmacro-prefix-mapG
   CPUINFO: OPENSSL_armcap=0xbd
   The 'numbers' are in 1000s of bytes per second processed.
   type             16 bytes     64 bytes     256 bytes     1024 bytes     8192 bytes
   AES-128-CBC      10239.91k    36515.20k    137949.87k     514730.67k    1321096.53k
            Command being timed: "openssl speed -evp aes-128-cbc -engine devcrypto"
            User time (seconds): 0.46
            System time (seconds): 5.89
            Percent of CPU this job got: 42%
            Elapsed (wall clock) time (h:mm:ss or m:ss): 0m 15.06s
            Average shared text size (kbytes): 0
            Average unshared data size (kbytes): 0
            Average stack size (kbytes): 0
            Average total size (kbytes): 0
            Maximum resident set size (kbytes): 7104
            Average resident set size (kbytes): 0
            Major (requiring I/O) page faults: 0
            Minor (reclaiming a frame) page faults: 479
            Voluntary context switches: 36143
            Involuntary context switches: 211570
            Swaps: 0
            File system inputs: 0
            File system outputs: 0
            Socket messages sent: 0
            Socket messages received: 0
            Signals delivered: 0
            Page size (bytes): 4096
            Exit status: 0

When the cryptodev driver is removed, OpenSSL reverts to the software
implementation of the crypto algorithm. The performance using the
software only implementation can be compared to the previous test.

.. code-block:: console

   root@evm:~# modprobe -r cryptodev
   root@evm:~# time -v openssl speed -evp aes-128-cbc
   Doing AES-128-CBC ops for 3s on 16 size blocks: 697674 AES-128-CBC ops in 2.99s
   Doing AES-128-CBC ops for 3s on 64 size blocks: 187556 AES-128-CBC ops in 3.00s
   Doing AES-128-CBC ops for 3s on 256 size blocks: 47922 AES-128-CBC ops in 3.00s
   Doing AES-128-CBC ops for 3s on 1024 size blocks: 12049 AES-128-CBC ops in 3.00s
   Doing AES-128-CBC ops for 3s on 8192 size blocks: 1509 AES-128-CBC ops in 3.00s
   version: 3.2.3
   built on: Tue Sep  3 12:52:35 2024 UTC
   options: bn(64,64)
   compiler: aarch64-oe-linux-gcc  -mbranch-protection=standard --sysroot=recipe-sysroot -O2 -pipe -g -feliminate-unused-debug-types -fcanon-prefix-map  -fmacro-prefix-map=  -fdebug-prefix-map=  -fmacro-prefix-mapG
   CPUINFO: OPENSSL_armcap=0xbd
   The 'numbers' are in 1000s of bytes per second processed.
   type             16 bytes     64 bytes     256 bytes     1024 bytes     8192 bytes
   AES-128-CBC       3733.37k     4001.19k      4089.34k       4112.73k       4120.58k
         Command being timed: "openssl speed -evp aes-128-cbc"
         User time (seconds): 15.03
         System time (seconds): 0.00
         Percent of CPU this job got: 99%
         Elapsed (wall clock) time (h:mm:ss or m:ss): 0m 15.07s
         Average shared text size (kbytes): 0
         Average unshared data size (kbytes): 0
         Average stack size (kbytes): 0
         Average total size (kbytes): 0
         Maximum resident set size (kbytes): 7216
         Average resident set size (kbytes): 0
         Major (requiring I/O) page faults: 1
         Minor (reclaiming a frame) page faults: 484
         Voluntary context switches: 13
         Involuntary context switches: 35
         Swaps: 0
         File system inputs: 0
         File system outputs: 0
         Socket messages sent: 0
         Socket messages received: 0
         Signals delivered: 0
         Page size (bytes): 4096
         Exit status: 0

******************************************************************
Using the True Random Number Generator (TRNG) Hardware Accelerator
******************************************************************

In the default SDK, OP-TEE controls the TRNG engine and firewalls its
hardware registers, blocking outside access. To use TRNG from Linux instead,
disable the OP-TEE driver and enable the RNG node in the Linux device tree.

Using TRNG from OP-TEE requires no further configuration. Verify the optee-rng
driver loads:

.. ifconfig:: CONFIG_crypto in ('sa2ul', 'DTHEv2')

   Check that the optee-rng driver is loaded:

   .. code-block:: console

      root@evm:~# cat /sys/class/misc/hw_random/rng_current
      optee-rng

The hwrng device should now show up in the filesystem.

.. code-block:: console

   root@evm:~# ls -l /dev/hwrng
   crw------- 1 root root 10, 183 Jan 1 2000 /dev/hwrng

Use :command:`cat` on this device to generate random numbers.

.. code-block:: console

   root@evm:~# cat /dev/hwrng | od -x
   0000000 b2bd ae08 4477 be48 4836 bf64 5d92 01c9
   0000020 0cb6 7ac5 16f9 8616 a483 7dfd 6bf4 3aa5
   0000040 d693 db24 d917 5ee7 feb7 34c3 34e9 e7a5
   0000060 36b7 ea85 fc17 0e66 555c 0934 7a0c 4c69
   0000100 523b 9f21 1546 fddb d58b e5ed 142a 6712
   0000120 8d76 8f80 a6d2 30d8 d107 32bc 7f45 f997
   0000140 9d5d 0d0c f1f0 64f9 a77f 408f b0c1 f5a0
   0000160 39c6 f0ae 4b59 1a76 84a7 a364 8964 f557
   root@evm:~#

Test the random number generator on the target.

.. code-block:: console

   root@evm:~# cat /dev/hwrng | rngtest -c 1000
   rngtest 6.16
   Copyright (c) 2004 by Henrique de Moraes Holschuh
   This is free software; see the source for copying conditions.  There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

   rngtest: starting FIPS tests...
   rngtest: bits received from input: 20000032
   rngtest: FIPS 140-2 successes: 999
   rngtest: FIPS 140-2 failures: 1
   rngtest: FIPS 140-2(2001-10-10) Monobit: 0
   rngtest: FIPS 140-2(2001-10-10) Poker: 0
   rngtest: FIPS 140-2(2001-10-10) Runs: 1
   rngtest: FIPS 140-2(2001-10-10) Long run: 0
   rngtest: FIPS 140-2(2001-10-10) Continuous run: 0
   rngtest: input channel speed: (min=788.218; avg=4070.983; max=2790178.571)Kibits/s
   rngtest: FIPS tests speed: (min=846.755; avg=15388.376; max=21920.595)Kibits/s
   rngtest: Program run time: 6072670 microseconds

Note that the results may be slightly different on your system, since,
after all, we're dealing with a random number generator. Any appreciable
number of errors typically indicates a bad random number generator.

If you're satisfied the random number generator is working correctly,
you can use :program:`rngd` (the random number generator daemon) to feed the
:file:`/dev/random` entropy pool.

****************************
Hardware Accelerator testing
****************************

Testing using the :program:`tcrypt` module
==========================================

.. ifconfig:: CONFIG_crypto not in ('DTHEv2')

   .. code-block:: console

      root@evm:~# modprobe tcrypt mode=500 sec=1
      [ 3006.234145] testing speed of async ecb(aes) (ecb-aes-sa2ul) encryption
      [ 3006.242891] tcrypt: test 0 (128 bit key, 16 byte blocks): 87335 operations in 1 seconds (1397360 bytes)
      [ 3007.251651] tcrypt: test 1 (128 bit key, 64 byte blocks): 87669 operations in 1 seconds (5610816 bytes)
      [ 3008.259651] tcrypt: test 2 (128 bit key, 256 byte blocks): 87481 operations in 1 seconds (22395136 bytes)
      [ 3009.267828] tcrypt: test 3 (128 bit key, 1024 byte blocks): 58076 operations in 1 seconds (59469824 bytes)
      [ 3010.275914] tcrypt: test 4 (128 bit key, 8192 byte blocks): 22556 operations in 1 seconds (184778752 bytes)
      [ 3011.284006] tcrypt: test 5 (192 bit key, 16 byte blocks): 80305 operations in 1 seconds (1284880 bytes)
      [ 3012.291648] tcrypt: test 6 (192 bit key, 64 byte blocks): 84537 operations in 1 seconds (5410368 bytes)
      [ 3013.299648] tcrypt: test 7 (192 bit key, 256 byte blocks): 90540 operations in 1 seconds (23178240 bytes)
      [ 3014.307834] tcrypt: test 8 (192 bit key, 1024 byte blocks): 56054 operations in 1 seconds (57399296 bytes)
      [ 3015.315915] tcrypt: test 9 (192 bit key, 8192 byte blocks): 20701 operations in 1 seconds (169582592 bytes)
      [ 3016.324006] tcrypt: test 10 (256 bit key, 16 byte blocks): 81816 operations in 1 seconds (1309056 bytes)
      [ 3017.331736] tcrypt: test 11 (256 bit key, 64 byte blocks): 82418 operations in 1 seconds (5274752 bytes)
      [ 3018.339739] tcrypt: test 12 (256 bit key, 256 byte blocks): 87217 operations in 1 seconds (22327552 bytes)
      [ 3019.347917] tcrypt: test 13 (256 bit key, 1024 byte blocks): 56534 operations in 1 seconds (57890816 bytes)
      [ 3020.356012] tcrypt: test 14 (256 bit key, 8192 byte blocks): 20428 operations in 1 seconds (167346176 bytes)
      [ 3021.364131] tcrypt:
      [ 3021.364131] testing speed of async ecb(aes) (ecb-aes-sa2ul) decryption
      [ 3021.373505] tcrypt: test 0 (128 bit key, 16 byte blocks): 81655 operations in 1 seconds (1306480 bytes)
      [ 3022.379660] tcrypt: test 1 (128 bit key, 64 byte blocks): 87373 operations in 1 seconds (5591872 bytes)
      [ 3023.387659] tcrypt: test 2 (128 bit key, 256 byte blocks): 81323 operations in 1 seconds (20818688 bytes)
      [ 3024.395825] tcrypt: test 3 (128 bit key, 1024 byte blocks): 58990 operations in 1 seconds (60405760 bytes)
      [ 3025.403928] tcrypt: test 4 (128 bit key, 8192 byte blocks): 22613 operations in 1 seconds (185245696 bytes)
      [ 3026.411996] tcrypt: test 5 (192 bit key, 16 byte blocks): 79558 operations in 1 seconds (1272928 bytes)
      [ 3027.419648] tcrypt: test 6 (192 bit key, 64 byte blocks): 86877 operations in 1 seconds (5560128 bytes)
      [ 3028.427648] tcrypt: test 7 (192 bit key, 256 byte blocks): 80615 operations in 1 seconds (20637440 bytes)
      [ 3029.435831] tcrypt: test 8 (192 bit key, 1024 byte blocks): 62007 operations in 1 seconds (63495168 bytes)
      [ 3030.443907] tcrypt: test 9 (192 bit key, 8192 byte blocks): 21569 operations in 1 seconds (176693248 bytes)
      [ 3031.452015] tcrypt: test 10 (256 bit key, 16 byte blocks): 86171 operations in 1 seconds (1378736 bytes)
      [ 3032.459743] tcrypt: test 11 (256 bit key, 64 byte blocks): 79752 operations in 1 seconds (5104128 bytes)
      [ 3033.467770] tcrypt: test 12 (256 bit key, 256 byte blocks): 84351 operations in 1 seconds (21593856 bytes)
      [ 3034.475919] tcrypt: test 13 (256 bit key, 1024 byte blocks): 57082 operations in 1 seconds (58451968 bytes)
      [ 3035.483995] tcrypt: test 14 (256 bit key, 8192 byte blocks): 20489 operations in 1 seconds (167845888 bytes)
      [ 3036.492101] tcrypt:
      ...

.. ifconfig:: CONFIG_crypto in ('DTHEv2')

   .. code-block:: console

      root@evm:~# modprobe tcrypt mode=500 sec=1
      [ 1012.121422] tcrypt: testing speed of async ecb(aes) (ecb-aes-dthev2) encryption
      [ 1012.128872] tcrypt: test 0 (128 bit key, 16 byte blocks): 4931 operations in 1 seconds (78896 bytes)
      [ 1013.138110] tcrypt: test 1 (128 bit key, 64 byte blocks): 4940 operations in 1 seconds (316160 bytes)
      [ 1014.146146] tcrypt: test 2 (128 bit key, 128 byte blocks): 4940 operations in 1 seconds (632320 bytes)
      [ 1015.154298] tcrypt: test 3 (128 bit key, 256 byte blocks): 4940 operations in 1 seconds (1264640 bytes)
      [ 1016.162329] tcrypt: test 4 (128 bit key, 1024 byte blocks): 4980 operations in 1 seconds (5099520 bytes)
      [ 1017.170491] tcrypt: test 5 (128 bit key, 1424 byte blocks): 4940 operations in 1 seconds (7034560 bytes)
      [ 1018.178486] tcrypt: test 6 (128 bit key, 4096 byte blocks): 4960 operations in 1 seconds (20316160 bytes)
      [ 1019.186570] tcrypt: test 7 (192 bit key, 16 byte blocks): 4960 operations in 1 seconds (79360 bytes)
      [ 1020.194482] tcrypt: test 8 (192 bit key, 64 byte blocks): 4940 operations in 1 seconds (316160 bytes)
      [ 1021.202151] tcrypt: test 9 (192 bit key, 128 byte blocks): 5000 operations in 1 seconds (640000 bytes)
      [ 1022.210225] tcrypt: test 10 (192 bit key, 256 byte blocks): 4940 operations in 1 seconds (1264640 bytes)
      [ 1023.218410] tcrypt: test 11 (192 bit key, 1024 byte blocks): 5000 operations in 1 seconds (5120000 bytes)
      [ 1024.226494] tcrypt: test 12 (192 bit key, 1424 byte blocks): 5000 operations in 1 seconds (7120000 bytes)
      [ 1025.234490] tcrypt: test 13 (192 bit key, 4096 byte blocks): 4980 operations in 1 seconds (20398080 bytes)
      [ 1026.242625] tcrypt: test 14 (256 bit key, 16 byte blocks): 4940 operations in 1 seconds (79040 bytes)
      [ 1027.250155] tcrypt: test 15 (256 bit key, 64 byte blocks): 4960 operations in 1 seconds (317440 bytes)
      [ 1028.258293] tcrypt: test 16 (256 bit key, 128 byte blocks): 4940 operations in 1 seconds (632320 bytes)
      [ 1029.266342] tcrypt: test 17 (256 bit key, 256 byte blocks): 4940 operations in 1 seconds (1264640 bytes)
      [ 1030.274405] tcrypt: test 18 (256 bit key, 1024 byte blocks): 4960 operations in 1 seconds (5079040 bytes)
      [ 1031.282506] tcrypt: test 19 (256 bit key, 1424 byte blocks): 4980 operations in 1 seconds (7091520 bytes)
      [ 1032.294641] tcrypt: test 20 (256 bit key, 4096 byte blocks): 4980 operations in 1 seconds (20398080 bytes)
      [ 1033.302656] tcrypt: testing speed of async ecb(aes) (ecb-aes-dthev2) decryption
      [ 1033.310809] tcrypt: test 0 (128 bit key, 16 byte blocks): 4940 operations in 1 seconds (79040 bytes)
      [ 1034.318058] tcrypt: test 1 (128 bit key, 64 byte blocks): 4960 operations in 1 seconds (317440 bytes)
      [ 1035.326153] tcrypt: test 2 (128 bit key, 128 byte blocks): 4940 operations in 1 seconds (632320 bytes)
      [ 1036.334354] tcrypt: test 3 (128 bit key, 256 byte blocks): 4940 operations in 1 seconds (1264640 bytes)
      [ 1037.342372] tcrypt: test 4 (128 bit key, 1024 byte blocks): 4920 operations in 1 seconds (5038080 bytes)
      [ 1038.350475] tcrypt: test 5 (128 bit key, 1424 byte blocks): 4940 operations in 1 seconds (7034560 bytes)
      [ 1039.358415] tcrypt: test 6 (128 bit key, 4096 byte blocks): 4940 operations in 1 seconds (20234240 bytes)
      [ 1040.366508] tcrypt: test 7 (192 bit key, 16 byte blocks): 4940 operations in 1 seconds (79040 bytes)
      [ 1041.374071] tcrypt: test 8 (192 bit key, 64 byte blocks): 4960 operations in 1 seconds (317440 bytes)
      [ 1042.382158] tcrypt: test 9 (192 bit key, 128 byte blocks): 4960 operations in 1 seconds (634880 bytes)
      [ 1043.390282] tcrypt: test 10 (192 bit key, 256 byte blocks): 4940 operations in 1 seconds (1264640 bytes)
      [ 1044.398466] tcrypt: test 11 (192 bit key, 1024 byte blocks): 4940 operations in 1 seconds (5058560 bytes)
      [ 1045.406558] tcrypt: test 12 (192 bit key, 1424 byte blocks): 4940 operations in 1 seconds (7034560 bytes)
      [ 1046.414503] tcrypt: test 13 (192 bit key, 4096 byte blocks): 4940 operations in 1 seconds (20234240 bytes)
      [ 1047.422793] tcrypt: test 14 (256 bit key, 16 byte blocks): 4960 operations in 1 seconds (79360 bytes)
      [ 1048.430409] tcrypt: test 15 (256 bit key, 64 byte blocks): 4960 operations in 1 seconds (317440 bytes)
      [ 1049.438295] tcrypt: test 16 (256 bit key, 128 byte blocks): 4940 operations in 1 seconds (632320 bytes)
      [ 1050.446313] tcrypt: test 17 (256 bit key, 256 byte blocks): 4940 operations in 1 seconds (1264640 bytes)
      [ 1051.454411] tcrypt: test 18 (256 bit key, 1024 byte blocks): 4960 operations in 1 seconds (5079040 bytes)
      [ 1052.462508] tcrypt: test 19 (256 bit key, 1424 byte blocks): 4960 operations in 1 seconds (7063040 bytes)
      [ 1053.470497] tcrypt: test 20 (256 bit key, 4096 byte blocks): 4960 operations in 1 seconds (20316160 bytes)
      ...

IPSec Testing
=============

.. rubric:: Server side

.. code-block:: console

   # iperf3 --server

   Accepted connection from 192.168.1.1, port 41266
   [  5] local 192.168.1.1 port 5201 connected to 192.168.1.2 port 58177
   [ ID] Interval       Transfer     Bandwidth       Jitter    Lost/Total Datagrams
   [  5]   0.00-1.00   sec  45.6 MBytes   382 Mbits/sec  0.021 ms  0/33017 (0%)
   [  5]   1.00-2.00   sec  47.7 MBytes   400 Mbits/sec  0.014 ms  0/34534 (0%)
   [  5]   2.00-3.00   sec  47.7 MBytes   400 Mbits/sec  0.013 ms  0/34527 (0%)
   [  5]   3.00-4.00   sec  47.7 MBytes   400 Mbits/sec  0.037 ms  0/34507 (0%)
   [  5]   4.00-5.00   sec  47.7 MBytes   400 Mbits/sec  0.021 ms  0/34540 (0%)
   [  5]   5.00-6.00   sec  47.7 MBytes   400 Mbits/sec  0.020 ms  0/34537 (0%)
   [  5]   6.00-7.00   sec  47.7 MBytes   400 Mbits/sec  0.013 ms  0/34511 (0%)
   [  5]   7.00-8.00   sec  47.7 MBytes   400 Mbits/sec  0.017 ms  0/34543 (0%)
   [  5]   8.00-9.00   sec  47.7 MBytes   400 Mbits/sec  0.012 ms  0/34518 (0%)
   [  5]   9.00-10.00  sec  47.7 MBytes   400 Mbits/sec  0.022 ms  0/34532 (0%)
   [  5]  10.00-10.04  sec  2.10 MBytes   403 Mbits/sec  0.014 ms  0/1518 (0%)

.. rubric:: Client side

.. code-block:: console

   # iperf3 -c 192.168.1.1 -u -b 400.0M -t 10
   Connecting to host 192.168.1.1, port 5201
   [  5] local 192.168.1.2 port 58177 connected to 192.168.1.1 port 5201
   [ ID] Interval           Transfer     Bitrate         Total Datagrams
   [  5]   0.00-1.00   sec  47.7 MBytes   400 Mbits/sec  34510
   [  5]   1.00-2.00   sec  47.7 MBytes   400 Mbits/sec  34531
   [  5]   2.00-3.00   sec  47.7 MBytes   400 Mbits/sec  34530
   [  5]   3.00-4.00   sec  47.7 MBytes   400 Mbits/sec  34531
   [  5]   4.00-5.00   sec  47.7 MBytes   400 Mbits/sec  34530
   [  5]   5.00-6.00   sec  47.7 MBytes   400 Mbits/sec  34530
   [  5]   6.00-7.00   sec  47.7 MBytes   400 Mbits/sec  34531
   [  5]   7.00-8.00   sec  47.7 MBytes   400 Mbits/sec  34530
   [  5]   8.00-9.00   sec  47.7 MBytes   400 Mbits/sec  34530
   [  5]   9.00-10.00  sec  47.7 MBytes   400 Mbits/sec  34531
