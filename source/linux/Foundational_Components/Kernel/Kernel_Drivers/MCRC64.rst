MCRC64
------

.. rubric:: Introduction
   :name: introduction-linux-mcrc64

The MCRC64 driver provides access to the hardware MCRC64 engine
available on |__PART_FAMILY_NAME__| devices. This driver is
available as kernel module in the current SDK release.

It supports crc64 hardware acceleration.

.. rubric:: Building MCRC64 driver
   :name: building-mcrc64-driver

For devices with available MCRC64 engine, a Linux driver and additionally a
kernel module, user-space interface for hash algorithms is used to access them.
Other devices use the pure software implementation of these crc64 calculations.

.. ifconfig:: CONFIG_mcrc64 in ('mcrc64')

    |__PART_FAMILY_NAME__| SoCs support a hardware accelerator called
    MCRC64 engine for crc64 calculations.

The kernel configuration has already been set up in the SDK and no further
configuration is needed for the driver to be built as kernel module.

For reference, the configuration details are shown below. The
configuration of the MCRC64 driver is done under the
Hardware crypto devices sub-menu of the Cryptographic API menu in the
kernel configuration.

.. ifconfig:: CONFIG_mcrc64 in ('mcrc64')

   .. code-block:: kconfig

      Symbol: CRYPTO_DEV_TI_MCRC64 [=m]
      Type  : tristate
      Defined at drivers/crypto/ti/Kconfig:2
        Prompt: Texas Instruments MCRC64 engine support
        Depends on: CRYPTO [=y] && CRYPTO_HW [=y] && (ARCH_K3 [=y] || COMPILE_TEST [=n])
        Location:
          -> Cryptographic API (CRYPTO [=y])
            -> Hardware crypto devices (CRYPTO_HW [=y])
      (1)     -> Texas Instruments MCRC64 engine support (CRYPTO_DEV_TI_MCRC64 [=m])
      Selects: CRYPTO_HASH [=y] && CRYPTO_CRC64_ISO3309 [=m]

   To check if mcrc64 module is properly installed,
   run the below command from the Linux command prompt:

   .. code-block:: console

      root@<machine># lsmod | grep mcrc64
      mcrc64  20480  0

.. rubric:: Build the algif_hash kernel module using SDK
   :name: build-the-algif_hash-kernel-module-using-sdk

For using user application to access the MCRC64 Drivers above, the algif_hash
kernel module is required (can be built as module). It is built as part of the
SDK and no further configuration is needed.

algif_hash: User-space interface for hash algorithms

For reference, the configuration details are shown below.

.. code-block:: kconfig

   Symbol: CRYPTO_USER_API_HASH [=m]
    Type  : tristate
    Defined at crypto/Kconfig:1869
      Prompt: User-space interface for hash algorithms
      Depends on: CRYPTO [=y] && NET [=y]
      Location:
        -> Cryptographic API (CRYPTO [=y])
    Selects: CRYPTO_HASH [=y] && CRYPTO_USER_API [=m]

The following shows the command used to query the system for the state of
the algif_hash module.

.. note::
   If not already loaded, these modules will get loaded
   automatically while running user space application.

.. code-block:: console

   root@<machine># lsmod | grep alg
   algif_hash             20480  0
   af_alg                 32768  1 algif_hash

.. rubric:: Working of MCRC64 controller
   :name: working-of-mcrc64-controller

MCRC64 Controller is a module which is used to perform CRC (Cyclic
Redundancy Check) to verify the integrity of memory system. A signature (CRC)
representing the contents of the memory is obtained when the contents of the
memory are read into MCRC64 Controller.

Writing the data into 64-bit Signature Register calculates the Signature (CRC).
The 64-bit Signature Register is based on the primitive polynomial to produce
the maximum length LFSR (Linear Feedback Shift Register).

The polynomial used was published in ISO-3309:1991.

Below is the mathematical representation of used primitive polynomial.

.. code-block:: mathematica

   f[x] = x^(64) + x^(4) + x^(3) + x + 1


.. rubric:: Using MCRC64 engine from user space application
   :name: using-mcrc64-engine-from-user-space-application

In order to use MCRC64 driver from user space, AF_ALG is used.
AF_ALG is User-space interface for Crypto API. Each algorithm type will provide its
own implementation that plugs into af_alg. They're keyed using a string such as
"skcipher" or "hash". The filesystem which comes with the SDK comes built with the
af_alg, algif_hash kernel modules and the TI driver which directly accesses the MCRC64
engine is built as kernel module.

The following code is for user-space application to access mcrc64 engine

.. code-block:: c

    #include <unistd.h>
    #include <stdio.h>
    #include <stdlib.h>
    #include <sys/socket.h>
    #include <linux/if_alg.h>
    #include <string.h>

    #define BUFFER_SIZE 4096
    #define SECTOR 4096

    int main (int argc, char **argv) {

        int desc[2] = { -1, -1 };

        struct sockaddr_alg sock = {
            .salg_family = AF_ALG,
            .salg_type   = "hash",
            .salg_name   = "crc64-iso3309"
        };

        if ((desc[0] = socket(AF_ALG, SOCK_SEQPACKET, 0)) == -1 ) {
            perror("socket");
            return -1;
        }

        if( bind(desc[0], (struct sockaddr *) &sock, sizeof(sock)) != 0 ) {
            perror("bind");
            return -1;
        }

        if( (desc[1] = accept(desc[0], NULL, 0)) == -1 )
            return -1;

        if (argc != 2 || strlen(argv[1]) == 0) {
            printf("Please specify filename\n");
            return -1; // empty string
        }

        FILE* file;
        unsigned char *buffer;
        if(posix_memalign((void *)&buffer, SECTOR, BUFFER_SIZE)) {
            perror("posix_memalign failed");
            return -1;
        }

        file = fopen(argv[1], "rb");
        if(file == NULL)
        {
            printf("An error occured while opening file: %s\n", argv[1]);
            free(buffer);
            return -1;
        }

        while(!feof(file))
        {
            unsigned int count = fread(buffer, sizeof(char), BUFFER_SIZE, file);
            if(ferror(file))
            {
                printf("An error occurred while accessing the file: %s\n", argv[1]);
                fclose(file);
                free(buffer);
                return -1;
            }

            if (send(desc[1], buffer, count, MSG_MORE) != count) {
                free(buffer);
                return -1;
            }
        }

        long int crc64 = 0x0000000000000000;
        if(read(desc[1], &crc64, 8) != 8) {
            free(buffer);
            return -1;
        }

        printf("0x%llx\n", crc64);
        free(buffer);
        return 0;
    }

Compile the code on target using below command

.. code-block:: console

   root@<machine># cc <filename> -o calculate_crc

.. rubric:: Run the executable

.. code-block:: console

   root@<machine># ./calculate_crc <path-to-file-for-crc-calculation>

   #Example
   root@<machine># ./calculate_crc cscope.files
   0xfa68a95edc9f3b45

Using the Linux time function gives more information about CPU usage
during the test.

.. code-block:: console

   root@<machine># time ./calculate_crc cscope.files
   0xfa68a95edc9f3b45

   real    0m0.213s
   user    0m0.000s
   sys     0m0.213s

To verify the result against pycrc module available `here <https://github.com/tpircher/pycrc.git>`_ on host PC.

.. code-block:: console

   host# time python3 ~/pycrc/src/pycrc.py --width 64 --poly 0x000000000000001b --reflect-in False --xor-in 0x0000000000000000 --reflect-out False --xor-out 0x0000000000000000 --check-file cscope.files
   0xfa68a95edc9f3b45

   real    1m36.405s
   user    1m36.216s
   sys     0m0.052s



.. rubric:: MCRC64 engine speed testing

Testing using the tcrypt module on target:

.. code-block:: console

   root@<machine># sudo modprobe tcrypt mode=329 sec=1
   sudo modprobe tcrypt mode=329 sec=1
   [  420.706237] tcrypt: testing speed of async crc64-iso3309 (mcrc64)
   [  420.712461] tcrypt: test  0 (   16 byte blocks,   16 bytes per update,   1 updates): 789148 opers/sec,  12626368 bytes/sec
   [  421.719575] tcrypt: test  1 (   64 byte blocks,   16 bytes per update,   4 updates): 363004 opers/sec,  23232256 bytes/sec
   [  422.727566] tcrypt: test  2 (   64 byte blocks,   64 bytes per update,   1 updates): 771433 opers/sec,  49371712 bytes/sec
   [  423.735553] tcrypt: test  3 (  256 byte blocks,   16 bytes per update,  16 updates): 119069 opers/sec,  30481664 bytes/sec
   [  424.743550] tcrypt: test  4 (  256 byte blocks,   64 bytes per update,   4 updates): 346712 opers/sec,  88758272 bytes/sec
   [  425.751540] tcrypt: test  5 (  256 byte blocks,  256 bytes per update,   1 updates): 672290 opers/sec, 172106240 bytes/sec
   [  426.759536] tcrypt: test  6 ( 1024 byte blocks,   16 bytes per update,  64 updates):  32296 opers/sec,  33071104 bytes/sec
   [  427.767535] tcrypt: test  7 ( 1024 byte blocks,  256 bytes per update,   4 updates): 273303 opers/sec, 279862272 bytes/sec
   [  428.775529] tcrypt: test  8 ( 1024 byte blocks, 1024 bytes per update,   1 updates): 442304 opers/sec, 452919296 bytes/sec
   [  429.783523] tcrypt: test  9 ( 2048 byte blocks,   16 bytes per update, 128 updates):  16378 opers/sec,  33542144 bytes/sec
   [  430.791574] tcrypt: test 10 ( 2048 byte blocks,  256 bytes per update,   8 updates): 155153 opers/sec, 317753344 bytes/sec
   [  431.788486] tcrypt: test 11 ( 2048 byte blocks, 1024 bytes per update,   2 updates): 263325 opers/sec, 539289600 bytes/sec
   [  432.799504] tcrypt: test 12 ( 2048 byte blocks, 2048 bytes per update,   1 updates): 303687 opers/sec, 621950976 bytes/sec
   [  433.807495] tcrypt: test 13 ( 4096 byte blocks,   16 bytes per update, 256 updates):   8249 opers/sec,  33787904 bytes/sec
   [  434.815592] tcrypt: test 14 ( 4096 byte blocks,  256 bytes per update,  16 updates):  83206 opers/sec, 340811776 bytes/sec
   [  435.823491] tcrypt: test 15 ( 4096 byte blocks, 1024 bytes per update,   4 updates): 148290 opers/sec, 607395840 bytes/sec
   [  436.831482] tcrypt: test 16 ( 4096 byte blocks, 4096 bytes per update,   1 updates): 187059 opers/sec, 766193664 bytes/sec
   [  437.839475] tcrypt: test 17 ( 8192 byte blocks,   16 bytes per update, 512 updates):   4139 opers/sec,  33906688 bytes/sec
   [  438.847507] tcrypt: test 18 ( 8192 byte blocks,  256 bytes per update,  32 updates):  43169 opers/sec, 353640448 bytes/sec
   [  439.855468] tcrypt: test 19 ( 8192 byte blocks, 1024 bytes per update,   8 updates):  79294 opers/sec, 649576448 bytes/sec
   [  440.863457] tcrypt: test 20 ( 8192 byte blocks, 4096 bytes per update,   2 updates): 100024 opers/sec, 819396608 bytes/sec
   [  441.871452] tcrypt: test 21 ( 8192 byte blocks, 8192 bytes per update,   1 updates): 100349 opers/sec, 822059008 bytes/sec
   modprobe: ERROR: could not insert 'tcrypt': Resource temporarily unavailable
   ...
