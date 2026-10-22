.. _am62dx_edgeai_getting_started_platform:

======================================
Hardware Setup and Configuration
======================================

This section covers the hardware setup and software configuration required to prepare
the AM62D EVM for running EdgeAI inference applications.

Hardware setup
==============

.. _pub_edgeai_am62dx_evm_setup:

AM62D EVM
---------

The AM62D EVM is a development board for audio AI applications built around the AM62DX
processor with a dedicated C7x DSP for neural network inference and digital signal
processing.

To run the demos on the AM62D EVM you will require:

- `AM62D EVM <https://www.ti.com/tool/AUDIO-AM62D-EVM>`__
- Minimum 16GB SD card
- USB Type-C power supply (20W recommended)
- USB-to-UART cable for serial console access
- Audio input source (e.g., microphone) connected to J1/J2
- Audio output device (e.g., headphones) connected to J3/J4
- Optional: Ethernet cable for remote access via `DP83867-EVM-AM <https://www.ti.com/tool/DP83867-EVM-AM>`__

Connect the components to the AM62D EVM as shown below:

.. figure:: /images/AM62D_evm_setup.png
   :height: 600
   :width: 1000
   :align: center

   AM62D EVM layout showing connectors, switches, and boot mode selection

Refer to the `AM62D Quick Start Guide <https://dev.ti.com/tirex/explore/node?isTheia=false&node=A__ARZXwcKmAzaWG2hcFPpKRA__PROCESSORS-DEVTOOLS__FUz-xrs__LATEST>`__
for detailed information about AM62D EVM layout and component locations.

Boot Mode Configuration
-----------------------

Set the BOOTMODE switches to SD card boot mode before powering on:

- BOOTMODE [8:15] (SW3) = 0100 0000
- BOOTMODE [0:7] (SW2) = 1100 0010

Audio Connectors
----------------

- Connect audio input source to J1 and J2 (PCM6240 ADC input)
- Connect audio output to speakers/headphones via J3 and J4 (TAD5212 DAC output)

Software setup
==============

Preparing SD Card Image
-----------------------

Download the latest Processor SDK Linux AM62DX image from:

|__SDK_DOWNLOAD_URL__|

Look for the file: ``tisdk-edgeai-image-am62dxx-evm.rootfs.wic.xz``

Download Balena Etcher from https://www.balena.io/etcher/ and flash the image:

.. figure:: /images/edgeai/balena_etcher.png
   :scale: 100
   :align: center

   Balena Etcher SD card flashing tool

1. Insert SD card into card reader connected to host PC
2. Launch Balena Etcher
3. Click "Select image" and choose the downloaded ``.wic.xz`` file
4. Click "Select target" and choose the SD card device
5. Click "Flash" to start flashing (this may take 10-15 minutes)
6. Wait for completion confirmation
7. Safely eject the SD card

.. note::

   Tested with Balena Etcher version 1.7.0. Some issues reported with version 1.7.2.
   If flashing fails, try a different version or use ``dd`` command on Linux.

If using a larger than 16GB SD card, expand the root filesystem to use the full capacity:

.. code-block:: bash

   #find the SD card device entry using lsblk (Eg: /dev/sdc)
   #Unmount the BOOT and rootfs partition before using parted tool
   umount /dev/sdX1
   umount /dev/sdX2

   #Use parted tool to resize the rootfs partition
   parted -s /dev/sdX resizepart 2 '100%'
   e2fsck -f /dev/sdX2
   resize2fs /dev/sdX2

   #replace /dev/sdX in above commands with SD card device entry

.. _pub_edgeai_am62dxx_flashing:

Power ON and Boot
-----------------

Ensure that the power supply is disconnected before inserting the SD card.
Once the SD card is firmly inserted and the AM62D EVM is powered ON, the board will
boot in 15-30 seconds.

Monitor the UART console for boot messages:

.. code-block:: console

   U-Boot 2023.01 (Oct  5 2024 - 12:34:56 +0000)

   SoC   : AM62Dx
   Model: TI AM62Dx EVM
   Board: AM62Dx EVM
   DRAM:  2 GiB
   ...
   Booting from MMC...
   ...
   Arago login:

At the login prompt, log in as the root user with no password:

.. code-block:: console

   Arago login: root
   root@am62dxx-evm:~#

UART Serial Console
-------------------

The AM62D EVM provides multiple serial ports via USB. 4 serial ports will come up on
your PC — connect to port 0 to get the boot logs.

For **Linux** use minicom:

.. code-block:: bash

   sudo minicom -D /dev/ttyUSB0 -c on

.. note::

   If you are unable to input from keyboard, disable Hardware Flow Control in minicom:
   Press Ctrl+A, then O (Setup), then S (Serial port), and verify Flow Control is off.

For **Windows** use Tera Term:

https://learn.sparkfun.com/tutorials/terminal-basics/tera-term-windows

.. note::

   Baud rate should be configured to 115200 bps.

Connect Remotely
----------------

You can also access the AM62D EVM via SSH using the IP address shown on the console:

.. code-block:: bash

   root@am62dxx-evm:~# ifconfig

From your host PC:

.. code-block:: bash

   ssh root@<EVM_IP_ADDRESS>

If using Ubuntu 22.04, add the following to ``~/.ssh/config``:

.. code-block:: bash

   Host 192.168.*
      HostKeyAlgorithms=+ssh-rsa

For a full IDE experience, install Visual Studio Code with the "Remote Development"
extension pack from https://code.visualstudio.com/download and connect via Remote-SSH.

Verifying the System
--------------------

After logging in, verify the system is properly booted:

.. code-block:: bash

   # Check DSP state (should report 'running')
   cat /sys/class/remoteproc/remoteproc*/state

   # List RPMsg devices
   ls -l /dev/rpmsg*

   # List DMA heap devices
   ls -l /dev/dma_heap/

   # List ALSA audio devices
   arecord -l    # Input devices
   aplay -l      # Output devices
