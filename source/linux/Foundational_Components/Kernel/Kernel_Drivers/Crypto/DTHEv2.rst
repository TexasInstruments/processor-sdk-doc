.. _DTHEv2-Crypto-Accelerator:

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
                  Hashing                         - MD5, SHA224, SHA256, SHA384, SHA512, HMAC(MD5), HMAC(SHA224), HMAC(SHA256), HMAC(SHA384), HMAC(SHA512)

********************
Building the Drivers
********************

For devices with available cryptographic hardware accelerators, a Linux
driver and additionally a Cryptodev kernel module (for OpenSSL) is used
to access them.  Other devices use the pure software implementation of these
cryptographic operations.

|__PART_FAMILY_DEVICE_NAMES__| SoC supports a hardware accelerator called
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
