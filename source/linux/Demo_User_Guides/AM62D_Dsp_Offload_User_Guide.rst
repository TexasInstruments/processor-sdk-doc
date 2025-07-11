.. _AM62D-dsp-offload-from-linux-user-guide:

AM62D DSP offload from Linux - User Guide
=========================================

Overview
--------

This guide describes how to set up, build, and run audio DSP offload example by using the Texas Instruments AM62D audio evaluation module (EVM).
This demo example shows how to offload 8ch audio filtering  to C7x from Linux, input is 8-channel, 256 block size audio data in channel interleaved form.
The output is the processed eight-channel, sample rate 48KHz and 256 block size audio data in channel interleaved form.
Below figure shows how this demo works:

.. figure:: /images/AM62D_DSP_offload_Demo_Setup.png
   :height: 500
   :width: 1000

Below figure shows the C7x signal chain:

.. figure:: /images/AM62D_dsp_signal_chain_11.01.png
   :height: 80
   :width: 1000

- CasadeBiquad Low-Pass Filter:
  
  - This filter is a three-stage, direct form 1 design with a low-pass cut-off frequency of 10KHz.

- CasadeBiquad High-Pass Filter:
  
  - This filter is also a three-stage, direct form 1 design with a high-pass cut-off frequency of 2KHz.

- Finite Impulse Response(FIR) Low-Pass Filter:
  
  - This filter is a 64-tap low-pass filter with a cut-off frequency of 8KHz.

- Real Fast Fourier Transform(FFT) and Inverse Fast Fourier Transform(IFFT) Real:
  
  - Perform FFT and IFFT of a real signal.

- Matrix Transpose:
  
  - Convert the data format between de-interleaved and interleaved formats within the signal chain.

Hardware Prerequisites
----------------------

- `AM62D-EVM <https://www.ti.com/tool/AUDIO-AM62D-EVM>`__

- Any audio device with output speaker and 3.5mm audio jack (Needed for running audio offload examples)

- SD card (minimum 16GB)

- USB Type-C 20W power supply (make sure to use type-C to type-C cable).

- USB-to-UART cable for console access

- PC (Windows or Linux) to flash image onto an SD Card

- Ethernet cable for audio offload examples host utility

- The ethernet expansion board `DP83867-EVM-AM <https://www.ti.com/tool/DP83867-EVM-AM>`__

- Host PC Requirements:

  - OS:

    - Windows: Windows 11 64-bit

    - Linux: Ubuntu 22.04 64-bit or higher
      
  - Memory: Minimum 4GB RAM (8GB or more recommended)
  
  - Storage: At least 10GB of free space

Software and Tools
------------------

- TI Processor SDK Linux RT (AM62Dx)

- MCU+ SDK for AM62Dx

- `C7000-CGT <https://www.ti.com/tool/C7000-CGT#downloads>`__ compiler

- `Code Composer Studio <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62DX/11_00_00_16/exports/docs/api_guide_am62dx/CCS_PROJECTS_PAGE.html>`__

- `TI Clang Compiler Toolchain <https://www.ti.com/tool/download/ARM-CGT-CLANG>`__

- CMake, GCC, make, git, scp, minicom, Python3

- `rpmsg-dma library <https://github.com/TexasInstruments/rpmsg-dma/tree/scarthgap>`__


EVM Setup
---------

#. Cable Connections

   - The figure below shows some important cable connections, ports and switches.

   - Take note of the location of the "BOOTMODE" switch, this is used to switch between different boot modes like SD, MMC SD mode

        .. figure:: /images/AM62D_evm_setup.png
           :height: 600
           :width: 1000

#. Setup UART Terminal

   - First identify the UART port as enumerated on the host machine.

   - Make sure that the EVM and UART cable connected to  UART to USB port as shown in Cable Connections

   - In windows, you can use the "Device Manager" to see the detected UART ports
     - Search "Device Manager" in Windows Search Box in the Windows taskbar.
       
   - If you don't see any USB serial ports listed in "Device Manager" under "Ports (COM & LPT)", then make sure you have installed the UART to USB driver from `FTDI <https://www.ftdichip.com/drivers>`__.

   - For A53 Linux console select UART boot port (ex: COM34 in below screenshot), keep other options to default and set 115200 baud rate.

#. Setup SDCard Boot Mode

   - This mode is used to boot applications via SD card on the EVM.

     - BOOTMODE [ 8 : 15 ] (SW3) = 0100 0000
       
     - BOOTMODE [ 0 : 7 ] (SW2) = 1100 0010

.. figure:: /images/AM62D_evm_sdcard_boot_mode.png
   :height: 300
   :width: 600

Steps to validate Audio DSP offload Demo
----------------------------------------

#. Flash an SD card with the :file:`tisdk-default-image-rt-am62dxx-evm.rootfs.wix.xz` wic image. Please follow the instructions provided at :ref:`Create SD Card <processor-sdk-linux-create-sd-card>` guide.

#. Insert the flashed SD card to `AUDIO-AM62D-EVM <https://www.ti.com/tool/AUDIO-AM62D-EVM>`__, connect the 3.5mm jack headset/Speaker, Ethernet Cable and power on TI AUDIO-AM62D-EVM.

#. Make sure the EVM boot mode switches are set properly for SD card boot as described earlier

#. Connect the USB-C cable from the power adapter to one of the two USB-C ports on the EVM.

#. Download Host Utility `audmon.py <https://github.com/TexasInstruments/rpmsg-dma/blob/scarthgap/example/audio_offload/host%20utility/audmon.py>`__.

#. The EVM should boot and the booting progress should display in the serial port console. At the end of booting, the Arago login prompt will appear. Just enter "root" to log in.

#. Get the EVM ip address

   .. code-block:: console

      root@am62dxx-evm:~# ifconfig

.. Note:: EVM ip address is required for host utility to connect to demo application

#. Run audio-dsp offload demo application from console

   .. code-block:: console

      root@am62dxx-evm:~# rpmsg_audio_offload_example

#. On host machine launch the :file:`audiomon.py` utility either in IP mode or UART mode
   
   - IP Mode
     
   .. code-block:: console

      # python audmon.py ip <EVM IP address>
      Ex: # python audmon.py ip 192.168.0.101
   
   - UART mode

   .. code-block:: console

      # python audmon.py uart <device serial port>
      Ex: # python audmon.py uart /dev/ttyUSB1

#. :file:`audiomon.py` utility GUI will be launched and it will automatically connect to demo application which supports below features:

   - Real-time visualization of:

     - Frame-level average amplitude (dBFS)
     
     - latency tracking
     
     - Avg load
     
     - Input/output FFT spectrum (only in IP mode)

   - Command interface to toggle features (e.g., enabling/disabling FFT filter)

   - Ctrl+S based save for graphs and log summaries

   - Summary labels for min/max/avg stats per run

   - For more information refer: `README <https://github.com/TexasInstruments/rpmsg-dma/blob/scarthgap/example/audio_offload/host%20utility/README.md>`_.

.. note:: Note: Input/output audio spectrum plotting is only supported in ip mode. UART mode supports only metrics and command interface, not audio data streams.
   Below is sample snapshot:

.. figure:: /images/AM62D_host_utility_snapshot.png
   :height: 600
   :width: 1200

- For more information on demo application & it's configuration, refer:  `DSP Offload Example <https://github.com/TexasInstruments/rpmsg-dma/blob/scarthgap/example/audio_offload/host%20utility/README.md>`__.


How to build Audio DSP offload Demo
====================================

Building Audio DSP offload wic image from Yocto
-----------------------------------------------

- To build the Audio DSP offload wic image, please refer :ref:`Processor SDK - Building the SDK with Yocto <building-the-sdk-with-yocto>`

Building the Linux Demo binary from sources
-------------------------------------------

#. The source code for Audio DSP offload  demo is available as part of the `rpmsg-dma <https://github.com/TexasInstruments/rpmsg-dma/tree/scarthgap>`__.

   .. code-block:: console

      host# git clone https://github.com/TexasInstruments/rpmsg-dma.git -b scarthgap

#. Download and Install the AM62D Linux SDK from |__SDK_DOWNLOAD_URL__| following the steps mentioned at :ref:`Download and Install the SDK <download-and-install-sdk>`.

#. Prepare the environment for cross compilation.

   .. code-block:: console

      host# source <path-to-linux-installer>/linux-devkit/environment-setup

#. Compile the sources

    .. code-block:: console

       [linux-devkit]:> cd <path-to-rpmsg-dma-sources>
       [linux-devkit]:> cmake -S . -B build; cmake --build build

  - This will build:

    - The example application :file:`rpmsg_audio_offload_example`

  - Transfer the generated files to evm sdcard:

    - The example binary :file:`rpmsg_audio_offload_example`  to :file:`/usr/bin`

    - The configuration file :file:`dsp_offload.cfg` to :file:`/etc`

    - The sample audio file :file:`sample_audio.wav` to :file:`/usr/share/`

    - The C7 DSP firmware file :file:`dsp_audio_filter_offload.c75ss0-0.release.strip.out` to :file:`/usr/lib/`

  - Optional:

    - To build only the library or only the example, use:

        .. code-block:: console

           cmake -S . -B build -DBUILD_LIB=OFF    # disables library build
           cmake -S . -B build -DBUILD_EXAMPLE=OFF # disables example build


Building the C7 Firmware from sources
--------------------------------------

- Please refer to the `MCU+ SDK Documentation  <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62DX/11_00_00_16/exports/docs/api_guide_am62dx/GETTING_STARTED_BUILD.html>`__
