.. _am62dx_edgeai_getting_started:

===============
Getting Started
===============

This section covers the hardware setup, software requirements, and initial boot process
for the AM62DX EVM to prepare it for running audio AI inference applications.

Hardware Prerequisites
======================

The following hardware is required to run AM62DX EdgeAI demos:

**AM62D-EVM Development Board**

- `AM62D-EVM <https://www.ti.com/tool/AUDIO-AM62D-EVM>`__
- Integrated AM62DX processor with C7x DSP
- Audio input and output connectors (J1, J2, J3, J4)
- McASP interface for audio codec communication

**Storage & Media**

- SD card (minimum 16GB capacity)
- SD card reader for flashing on host PC
- Balena Etcher or similar SD card flashing tool

**Power Supply**

- USB Type-C power supply (20W recommended)
- USB Type-C to Type-C cable for power connection to EVM

**Connectivity**

- USB-to-UART cable for serial console access to board
- Ethernet cable and network connectivity (optional but recommended for remote access)
- Ethernet expansion board `DP83867-EVM-AM <https://www.ti.com/tool/DP83867-EVM-AM>`__ (optional)

**Audio I/O**

- Audio input source (e.g., microphone, audio interface) connected to J1/J2
- Audio output device (e.g., speakers, headphones) connected to J3/J4
- 3.5mm audio jacks or TRS connectors compatible with EVM audio connectors

**Host Computer Requirements**

- Operating System: Windows 10/11 or Ubuntu 20.04/22.04 LTS
- Memory: Minimum 4GB RAM (8GB recommended)
- Storage: At least 10GB free space for SDK and build artifacts
- USB ports for SD card reader and UART adapter

Software and Tools
==================

The following software components are required on the host machine:

**SDK Components**

- TI Processor SDK Linux for AM62DX (latest version)
- MCU+ SDK for AM62DX (for firmware compilation)
- Yocto build system (for building custom images)

**Compilers and Tools**

- ARM Clang Toolchain for ARM64 cross-compilation
- C7000 CGT (C7x compiler) for DSP firmware
- CMake 3.16 or higher
- GCC, make, git
- Python 3.7+

**Development Utilities**

- Balena Etcher (for SD card flashing)
- minicom or Tera Term (for UART serial console)
- SSH client (for remote board access)
- scp (for file transfer)

**Libraries**

- libti_rpmsg_dma - RPMsg DMA library for inter-processor communication
- ti-rpmsg-char - Character device driver for RPMsg
- TVM runtime libraries (Neo-TVM)
- ALSA (Advanced Linux Sound Architecture) libraries
- libsndfile - Audio file I/O library
- json-c - JSON parsing library

EVM Setup and Cable Connections
================================

**Step 1: Identify Board Components and Switch Positions**

The AM62D-EVM has several important components and switches:

.. figure:: /images/AM62D_evm_setup.png
   :height: 600
   :width: 1000
   :align: center

   AM62D-EVM layout showing connectors, switches, and boot mode selection

Take note of:

- BOOTMODE switch (SW2 and SW3) for selecting SD card boot mode
- UART connectors (multiple serial ports)
- Audio connectors (J1, J2 for input; J3, J4 for output)
- Power connector (USB Type-C)
- Ethernet port (if available)

Refer to the `AM62D Quick Start Guide <https://dev.ti.com/tirex/explore/node?isTheia=false&node=A__ARZXwcKmAzaWG2hcFPpKRA__PROCESSORS-DEVTOOLS__FUz-xrs__LATEST>`__
for detailed information about EVM layout and component locations.

**Step 2: Configure Boot Mode Switches**

Set the BOOTMODE switches to SD card boot mode before powering on:

- BOOTMODE [8:15] (SW3) = 0100 0000
- BOOTMODE [0:7] (SW2) = 1100 0010

These settings select SD card as the primary boot device.

**Step 3: Connect Power Supply**

- Ensure the power adapter is disconnected
- Connect the USB Type-C cable from the EVM to the power adapter (do not connect to computer)
- The EVM can be powered on once all other connections are complete

**Step 4: Connect UART Cable**

Connect the USB-to-UART cable to the EVM's UART port for console access:

- On Windows: Use Device Manager to identify the COM port
- On Linux: Use ``ls /dev/ttyUSB*`` to identify the serial port device
- Install FTDI drivers if needed: https://ftdichip.com/drivers

**Step 5: Connect Audio Devices**

- Connect audio input source to connectors J1 and J2 (PCM6240 ADC input)
- Connect audio output to speakers/headphones via connectors J3 and J4 (TAD5212 DAC output)

**Step 6: (Optional) Connect Ethernet**

For remote SSH access and higher bandwidth:

- Connect Ethernet cable from EVM to network
- If using the DP83867-EVM-AM expansion board, connect it to the appropriate header first

UART Serial Console Setup
==========================

The EVM provides multiple serial ports via USB. Configure your terminal software
to access the boot logs and Linux console:

**On Linux with minicom:**

.. code-block:: bash

   # Install minicom if not already installed
   sudo apt-get install minicom

   # Connect to the UART port (typically /dev/ttyUSB0 for first serial port)
   sudo minicom -D /dev/ttyUSB0 -c on

   # Configuration: Set baud rate to 115200 bps
   # To change baud rate in minicom: Ctrl+A, then Z, then B

**On Windows with Tera Term:**

1. Download Tera Term from https://learn.sparkfun.com/tutorials/terminal-basics/tera-term-windows
2. Launch Tera Term and select the COM port shown in Device Manager
3. Go to Setup → Serial port and set baud rate to 115200 bps
4. Click OK to establish the connection

**Configuration Settings:**

- Baud Rate: 115200 bps
- Data Bits: 8
- Stop Bits: 1
- Parity: None
- Flow Control: None (disable hardware flow control if enabled)

.. note::

   If you cannot input text in minicom, disable Hardware Flow Control:
   Press Ctrl+A, then O (Setup), then S (Serial port), and verify Flow Control is off.

Preparing and Flashing SD Card
================================

**Step 1: Download the SD Card Image**

Download the latest Processor SDK Linux AM62DX image from:

|__SDK_DOWNLOAD_URL__|

Look for the file: ``tisdk-edgeai-image-am62dxx-evm.rootfs.wic.xz``

**Step 2: Flash the Image Using Balena Etcher**

Download Balena Etcher from https://www.balena.io/etcher/

.. figure:: /images/edgeai/balena_etcher.png
   :scale: 100
   :align: center

   Balena Etcher SD card flashing tool

Steps to flash:

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

**Step 3: Expand Filesystem (if needed)**

The default image is configured for 16GB SD cards. If using a larger card,
expand the root filesystem to use the full capacity:

.. code-block:: bash

   # On Linux host machine:
   # 1. Find the SD card device (e.g., /dev/sdc)
   lsblk

   # 2. Unmount partitions
   umount /dev/sdX1
   umount /dev/sdX2

   # 3. Resize rootfs partition to use full card
   sudo parted -s /dev/sdX resizepart 2 '100%'
   sudo e2fsck -f /dev/sdX2
   sudo resize2fs /dev/sdX2

   # Replace /dev/sdX with your SD card device identifier

Power On and Initial Boot
==========================

**Step 1: Insert SD Card**

- Ensure power adapter is disconnected
- Firmly insert the flashed SD card into the SD card slot on the EVM
- The card should be fully seated with a click

**Step 2: Connect Power**

- Connect the USB Type-C power adapter to the EVM
- The EVM will automatically power on and begin booting
- Boot process typically takes 15-30 seconds

**Step 3: Verify Boot on UART Console**

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

**Step 4: Login to Linux**

At the login prompt, log in as the root user with no password:

.. code-block:: console

   Arago login: root
   root@am62dxx-evm:~#

You now have shell access to the AM62DX EVM!

Verifying System and Initialization
====================================

**Check System Information**

After logging in, verify the system is properly booted:

.. code-block:: bash

   # Check processor information
   cat /proc/cpuinfo

   # Check memory
   free -h

   # Check Linux version
   uname -a

**Check DSP Remoteproc**

Verify the C7x DSP is available for communication:

.. code-block:: bash

   # List available remote processors
   grep . /sys/class/remoteproc/remoteproc*/name

   # Check DSP state (should report 'running')
   cat /sys/class/remoteproc/remoteproc*/state

**Check RPMsg and DMA Heap**

Verify RPMsg-char and DMA heap devices are available:

.. code-block:: bash

   # List RPMsg devices
   ls -l /dev/rpmsg*

   # List DMA heap devices
   ls -l /dev/dma_heap/

**Audio Device Setup**

Check connected audio devices:

.. code-block:: bash

   # List ALSA audio devices
   arecord -l    # Input devices
   aplay -l      # Output devices

Remote SSH Connection
====================

For more convenient access and file transfer, you can connect to the EVM via SSH:

**Step 1: Get EVM IP Address**

On the EVM console, get the IP address:

.. code-block:: bash

   root@am62dxx-evm:~# ifconfig
   eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>
       inet 192.168.1.100  netmask 255.255.255.0  broadcast 192.168.1.255
       ...

Note the IP address assigned to eth0 (in this example: 192.168.1.100)

**Step 2: SSH from Host Machine**

From your host PC, connect via SSH:

.. code-block:: bash

   # Connect to EVM
   ssh root@192.168.1.100

   # You should be prompted for a password (default: none for root)
   # If needed, use SSH config to avoid key issues (Ubuntu 22.04):
   # Add to ~/.ssh/config:
   # Host 192.168.*
   #    HostKeyAlgorithms=+ssh-rsa

**Step 3: Visual Studio Code Remote Development (Optional)**

For a full IDE experience with remote development:

1. Install Visual Studio Code from https://code.visualstudio.com/download
2. Install the "Remote Development" extension pack
3. In VSCode, press Ctrl+Shift+P and select "Remote-SSH: Connect to Host"
4. Enter ``root@<EVM_IP_ADDRESS>`` and connect
5. You can now browse files and edit directly on the EVM

Next Steps
==========

With the EVM now running and accessible, you're ready to proceed with building and running
the AM62DX audio inference application. Proceed to the Linux Audio Inference Application
section for detailed build and usage instructions.
