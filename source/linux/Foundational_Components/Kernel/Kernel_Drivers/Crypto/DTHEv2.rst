.. _DTHEv2-Crypto-Accelerator:
.. _crypto-accelerator:

######
Crypto
######

************
Introduction
************

The Crypto API Driver is a set of Linux drivers that provide access to
the hardware cryptographic accelerators available on AM62L devices.
These drivers are available built-in in the kernel in the current SDK release.

Following are the Hardware accelerators supported on the following
devices:

.. code-block:: text

   * AM62LX    :  Encryption                      - AES-ECB, AES-CBC, AES-XTS, AES-CTR
                  Encryption with Authentication  - AES-GCM, AES-CCM
                  Hashing                         - MD5, SHA224, SHA256, SHA384, SHA512
                  Message Authentication          - HMAC(MD5), HMAC(SHA224), HMAC(SHA256), HMAC(SHA384), HMAC(SHA512)

********************
Building the Drivers
********************

For devices with available cryptographic hardware accelerators, a Linux
driver and additionally a Cryptodev kernel module (for OpenSSL) is used
to access them.  Other devices use the pure software implementation of these
cryptographic operations.

|__PART_FAMILY_NAME__| SoC supports a hardware accelerator called
DATA TRANSFORM AND HASHING ENGINE (DTHE) v2 for crypto operations.

The kernel configuration has already been set up in the SDK and no further
configuration is needed for the drivers to be built-in to the kernel.

For reference, the configuration details are shown below. The
configuration of the cryptographic drivers is done under the
Hardware crypto devices sub-menu of the Cryptographic API menu in the
kernel configuration.

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
   Engine "devcrypto" set.
   Doing AES-128-CBC ops for 3s on 16 size blocks: 37316 AES-128-CBC ops in 0.00s
   Doing AES-128-CBC ops for 3s on 64 size blocks: 37305 AES-128-CBC ops in 0.00s
   Doing AES-128-CBC ops for 3s on 256 size blocks: 37503 AES-128-CBC ops in 0.00s
   Doing AES-128-CBC ops for 3s on 1024 size blocks: 37504 AES-128-CBC ops in 0.00s
   Doing AES-128-CBC ops for 3s on 8192 size blocks: 18784 AES-128-CBC ops in 0.00s
   Doing AES-128-CBC ops for 3s on 16384 size blocks: 18701 AES-128-CBC ops in 0.00s
   version: 3.2.3
   built on: Tue Sep  3 12:52:35 2024 UTC
   options: bn(64,64)
   compiler: aarch64-oe-linux-gcc  -mbranch-protection=standard --sysroot=recipe-sysroot -O2 -pipe -g -feliminate-unused-debug-types -fcanon-prefix-map  -fmacro-prefix-map=  -fdebug-prefix-map=  -fmacro-prefix-mapG
   CPUINFO: OPENSSL_armcap=0xbd
   The 'numbers' are in 1000s of bytes per second processed.
   type             16 bytes     64 bytes    256 bytes   1024 bytes   8192 bytes  16384 bytes
   AES-128-CBC           infk         infk         infk         infk         infk         infk

Using the Linux time -v function gives more information about CPU usage
during the test.

.. code-block:: console

   root@evm:~# time -v openssl speed -evp aes-128-cbc -engine devcrypto
   Engine "devcrypto" set.
   Doing AES-128-CBC ops for 3s on 16 size blocks: 37194 AES-128-CBC ops in 0.00s
   Doing AES-128-CBC ops for 3s on 64 size blocks: 37406 AES-128-CBC ops in 0.00s
   Doing AES-128-CBC ops for 3s on 256 size blocks: 37455 AES-128-CBC ops in 0.00s
   Doing AES-128-CBC ops for 3s on 1024 size blocks: 37503 AES-128-CBC ops in 0.00s
   Doing AES-128-CBC ops for 3s on 8192 size blocks: 18744 AES-128-CBC ops in 0.01s
   Doing AES-128-CBC ops for 3s on 16384 size blocks: 18727 AES-128-CBC ops in 0.01s
   version: 3.2.3
   built on: Tue Sep  3 12:52:35 2024 UTC
   options: bn(64,64)
   compiler: aarch64-oe-linux-gcc  -mbranch-protection=standard --sysroot=recipe-sysroot -O2 -pipe -g -feliminate-unused-debug-types -fcanon-prefix-map  -fmacro-prefix-map=  -fdebug-prefix-map=  -fmacro-prefix-mapG
   CPUINFO: OPENSSL_armcap=0xbd
   The 'numbers' are in 1000s of bytes per second processed.
   type             16 bytes     64 bytes    256 bytes   1024 bytes   8192 bytes  16384 bytes
   AES-128-CBC           infk         infk         infk         infk 15355084.80k 30682316.80k
            Command being timed: "openssl speed -evp aes-128-cbc -engine devcrypto"
            User time (seconds): 0.02
            System time (seconds): 11.40
            Percent of CPU this job got: 62%
            Elapsed (wall clock) time (h:mm:ss or m:ss): 0m 18.42s
            Average shared text size (kbytes): 0
            Average unshared data size (kbytes): 0
            Average stack size (kbytes): 0
            Average total size (kbytes): 0
            Maximum resident set size (kbytes): 23760
            Average resident set size (kbytes): 0
            Major (requiring I/O) page faults: 0
            Minor (reclaiming a frame) page faults: 329
            Voluntary context switches: 187095
            Involuntary context switches: 95
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
   Doing AES-128-CBC ops for 3s on 16 size blocks: 18675602 AES-128-CBC ops in 2.99s
   Doing AES-128-CBC ops for 3s on 64 size blocks: 14189260 AES-128-CBC ops in 2.99s
   Doing AES-128-CBC ops for 3s on 256 size blocks: 7121339 AES-128-CBC ops in 2.98s
   Doing AES-128-CBC ops for 3s on 1024 size blocks: 2437075 AES-128-CBC ops in 2.99s
   Doing AES-128-CBC ops for 3s on 8192 size blocks: 340806 AES-128-CBC ops in 2.98s
   Doing AES-128-CBC ops for 3s on 16384 size blocks: 171986 AES-128-CBC ops in 2.98s
   version: 3.2.3
   built on: Tue Sep  3 12:52:35 2024 UTC
   options: bn(64,64)
   compiler: aarch64-oe-linux-gcc  -mbranch-protection=standard --sysroot=recipe-sysroot -O2 -pipe -g -feliminate-unused-debug-types -fcanon-prefix-map  -fmacro-prefix-map=  -fdebug-prefix-map=  -fmacro-prefix-mapG
   CPUINFO: OPENSSL_armcap=0xbd
   The 'numbers' are in 1000s of bytes per second processed.
   type             16 bytes     64 bytes    256 bytes   1024 bytes   8192 bytes  16384 bytes
   AES-128-CBC      99936.33k   303716.60k   611766.03k   834637.06k   936873.41k   945576.72k
         Command being timed: "openssl speed -evp aes-128-cbc"
         User time (seconds): 17.91
         System time (seconds): 0.04
         Percent of CPU this job got: 99%
         Elapsed (wall clock) time (h:mm:ss or m:ss): 0m 18.02s
         Average shared text size (kbytes): 0
         Average unshared data size (kbytes): 0
         Average stack size (kbytes): 0
         Average total size (kbytes): 0
         Maximum resident set size (kbytes): 24304
         Average resident set size (kbytes): 0
         Major (requiring I/O) page faults: 0
         Minor (reclaiming a frame) page faults: 324
         Voluntary context switches: 1
         Involuntary context switches: 24
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

The pre-built kernel included within the SDK already has the OP-TEE TRNG
driver enabled. You do not need any further configuration.

Verify that the optee-rng driver is loaded:

.. code-block:: console

   root@am62lxx-evm:~# cat /sys/class/misc/hw_random/rng_current
   optee-rng

The hwrng device should now show up in the filesystem.

.. code-block:: console

   root@am62lxx-evm:~# ls -l /dev/hwrng
   crw------- 1 root root 10, 183 Jan 1 2000 /dev/hwrng

Use :command:`cat` on this device to generate random numbers.

.. code-block:: console

   root@am62lxx-evm:~# cat /dev/hwrng | od -x
   0000000 b2bd ae08 4477 be48 4836 bf64 5d92 01c9
   0000020 0cb6 7ac5 16f9 8616 a483 7dfd 6bf4 3aa5
   0000040 d693 db24 d917 5ee7 feb7 34c3 34e9 e7a5
   0000060 36b7 ea85 fc17 0e66 555c 0934 7a0c 4c69
   0000100 523b 9f21 1546 fddb d58b e5ed 142a 6712
   0000120 8d76 8f80 a6d2 30d8 d107 32bc 7f45 f997
   0000140 9d5d 0d0c f1f0 64f9 a77f 408f b0c1 f5a0
   0000160 39c6 f0ae 4b59 1a76 84a7 a364 8964 f557
   root@am62lxx-evm:~#

Test the random number generator on the target.

.. code-block:: console

   root@am62lxx-evm:~# cat /dev/hwrng | rngtest -c 1000
   rngtest 6.16
   Copyright (c) 2004 by Henrique de Moraes Holschuh
   This is free software; see the source for copying conditions.  There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

   rngtest: starting FIPS tests...
   rngtest: bits received from input: 20000032
   rngtest: FIPS 140-2 successes: 999
   rngtest: FIPS 140-2 failures: 1
   rngtest: FIPS 140-2(2001-10-10) Monobit: 0
   rngtest: FIPS 140-2(2001-10-10) Poker: 0
   rngtest: FIPS 140-2(2001-10-10) Runs: 0
   rngtest: FIPS 140-2(2001-10-10) Long run: 1
   rngtest: FIPS 140-2(2001-10-10) Continuous run: 0
   rngtest: input channel speed: (min=72.965; avg=3848.070; max=9765625.000)Kibits/s
   rngtest: FIPS tests speed: (min=10.794; avg=53.373; max=54.967)Mibits/s
   rngtest: Program run time: 5710839 microseconds
   root@am62lxx-evm:~#

Note that the results might be slightly different on your system, since,
after all, we are dealing with a random number generator. Any appreciable
number of errors typically indicates a bad random number generator.

If you're satisfied the random number generator is working correctly,
you can use :program:`rngd` (the random number generator daemon) to feed the
:file:`/dev/random` entropy pool.

****************************
Hardware Accelerator testing
****************************

Testing using the :program:`tcrypt` module
==========================================

.. code-block:: console

   root@am62lxx-evm:~# modprobe tcrypt mode=500 sec=1
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
