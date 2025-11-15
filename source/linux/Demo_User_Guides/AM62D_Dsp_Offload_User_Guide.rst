.. _AM62D-dsp-offload-from-linux-user-guide:

#########################################
AM62D DSP offload from Linux - User Guide
#########################################

********
Overview
********

This guide describes how to set up, build, and run audio DSP offload example by using the Texas Instruments AM62D audio evaluation module (EVM).
This demo example shows how to offload 8ch audio filtering  to C7x from Linux, input is 8-channel, 256 block size audio data in channel interleaved form.
The output is the processed eight-channel, sample rate 48KHz and 256 block size audio data in channel interleaved form.
Below figure shows how this demo works:

.. figure:: /images/AM62D_DSP_offload_Demo.svg
   :height: 500
   :width: 1000

- Step 1: Read sample audio
   - DSP offload example application read the 8-channel raw audio data from the SD card.

- Step 2: Copy data to shared DMA Buffer (DDR)
   - Copy audio data to a shared DMA buffer located in DDR memory.

- Step 3: Notify DSP using RPMSG (IPC)
   - A53 sends a control message via RPMsg (Remote Processor Messaging) to the C7x core. This message informs the C7x that new input audio data is available for processing in the shared DDR buffer.

- Step 4: C7x reads from shared DMA Buffer into L2 SRAM
   - The C7x DSP copies the audio data from the DMA buffer (DDR) into its local L2 SRAM for processing. This operation minimizes access latency compared to reading directly from DDR.

- Step 5: Signal chain execution on DSP
   - Below figure shows the C7x signal chain executed on C7x:

   .. figure:: /images/AM62D_dsp_signal_chain_audio_offload.png
      :height: 80
      :width: 1000
      
   - CasadeBiquad Low-Pass Filter: This filter is a three-stage, direct form 1 design with a low-pass cut-off frequency of 10KHz.
       
   - CasadeBiquad High-Pass Filter: This filter is also a three-stage, direct form 1 design with a high-pass cut-off frequency of 2KHz.

   - Finite Impulse Response(FIR) Low-Pass Filter: This filter is a 64-tap low-pass filter with a cut-off frequency of 8KHz.
       
   - Real Fast Fourier Transform(FFT) and Inverse Fast Fourier Transform(IFFT) Real: Perform FFT and IFFT of a real signal.
       
   - Matrix Transpose: Convert the data format between de-interleaved and interleaved formats within the signal chain.

- Step 6: Processed data copied back to shared DMA Buffer (DDR)
   - Once DSP processing is complete, the output (filtered/processed audio) copied back into the same section of the shared DMA buffer.
   - C7x sends a control message via RPMsg (Remote Processor Messaging) to the A53 core. This message informs the A53 that processed output audio data available in the shared DDR buffer.

- Step 7: A53 reads back processed data from DMA buffer
   - A53 copies the processed audio data from the shared buffer, send this to audio output and forward to a host for visualization.

- Step 8: Audio output (Playback)
   - The processed 8-channel audio play to speakers (Ch 1–8).

- Step 9: Host GUI utility (Over RJ45 or Serial)
   - A53 communicates with a Host PC GUI utility over Ethernet (RJ45) or Serial.
   - Live display of input/output spectrum (if using IP mode).
   - Latency graphing (measuring round-trip delay).
   - ON/OFF control for filters.
   - DSP/CPU load monitoring.

**********************
Hardware Prerequisites
**********************

- `AM62D-EVM <https://www.ti.com/tool/AUDIO-AM62D-EVM>`__

- Any audio device with output speaker and 3.5mm audio jack (Needed for running audio offload examples)

- SD card (minimum 16GB)

- USB Type-C 20W power supply (make sure to use type-C to type-C cable).

- USB-to-UART cable for console access

- PC (Windows or Linux) to flash image onto an SD Card

- Ethernet cable for audio offload examples host utility

- The ethernet expansion board `DP83867-EVM-AM <https://www.ti.com/tool/DP83867-EVM-AM>`__

- Host PC Requirements:

  - operating system:

    - Windows: |__WINDOWS_SUPPORTED_LONG__|

    - Ubuntu: |__LINUX_UBUNTU_VERSION_LONG__|
      
  - Memory: Minimum 4GB RAM (8GB or more recommended)
  
  - Storage: At least 10GB of free space

******************
Software and Tools
******************

- TI Processor SDK Linux RT (AM62Dx)

- MCU+ SDK for AM62Dx

- `C7000-CGT <https://www.ti.com/tool/C7000-CGT#downloads>`__ compiler

- `Code Composer Studio <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62DX/11_00_00_16/exports/docs/api_guide_am62dx/CCS_PROJECTS_PAGE.html>`__

- `TI Clang Compiler Toolchain <https://www.ti.com/tool/download/ARM-CGT-CLANG>`__

- CMake, GCC, make, git, scp, minicom, Python3

- `rpmsg-dma library <https://github.com/TexasInstruments/rpmsg-dma/tree/scarthgap>`__

*********
EVM Setup
*********

#. Cable Connections

   - The figure below shows some important cable connections, ports and switches.

   - Take note of the location of the "BOOTMODE" switch for SD card boot mode.

        .. figure:: /images/AM62D_evm_setup.png
           :height: 600
           :width: 1000

#. Setup UART Terminal

   - First identify the UART port as enumerated on the host machine.

   - Make sure that the EVM and UART cable connected to  UART to USB port as shown in Cable Connections

   - In windows, you can use the "Device Manager" to see the detected UART ports
     - Search "Device Manager" in Windows Search Box in the Windows taskbar.
       
   - If you do not see any USB serial ports listed in "Device Manager" under "Ports (COM & LPT)", then make sure you have installed the UART to USB driver from `FTDI <https://www.ftdichip.com/drivers>`__.

   - For A53 Linux console select UART boot port (ex: COM34 in below screenshot), keep other options to default and set 115200 baud rate.

#. Setup SD card Boot Mode

   - EVM SD card  boot mode setting:

     - BOOTMODE [ 8 : 15 ] (SW3) = 0100 0000
       
     - BOOTMODE [ 0 : 7 ] (SW2) = 1100 0010

****************************************
Steps to validate audio DSP offload demo
****************************************

#. Flash an SD card with the :file:`tisdk-default-image-rt-am62dxx-evm.rootfs.wic.xz` image and follow the instructions provided at :ref:`Create SD Card <processor-sdk-linux-create-sd-card>` guide.

#. Insert the flashed SD card to `AUDIO-AM62D-EVM <https://www.ti.com/tool/AUDIO-AM62D-EVM>`__, connect the 3.5mm jack headset/Speaker, Ethernet Cable and power on TI AUDIO-AM62D-EVM.

#. Make sure the EVM boot mode switches position set for SD card boot as described earlier

#. Connect the USB-C cable from the power adapter to one of the two USB-C ports on the EVM.

#. Download Host Utility `audmon.py <https://github.com/TexasInstruments/rpmsg-dma/blob/scarthgap/example/audio_offload/host%20utility/audmon.py>`__.

#. The EVM should boot and the booting progress should display in the serial port console. At the end of booting, the Arago login prompt will appear. Just enter "root" to log in.

#. Get the EVM IP address

   .. code-block:: console

      root@am62dxx-evm:~# ifconfig

.. note::

   EVM IP address required for host utility to connect to demo application

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

#. :file:`audiomon.py` utility GUI automatically connect to demo application which supports below features:

   - Real-time visualization of:

     - Frame-level average amplitude (dBFS)
     
     - latency tracking
     
     - Avg load
     
     - Input/output FFT spectrum (only in IP mode)

   - Command interface to toggle features (e.g., enabling/disabling FFT filter)

   - Ctrl+S based save for graphs and log summaries

   - Summary labels for min/max/avg stats per run

   - For more information refer: `README <https://github.com/TexasInstruments/rpmsg-dma/blob/scarthgap/example/audio_offload/host%20utility/README.md>`_.

.. note::
   
   Input/output audio spectrum plotting is only supported in IP mode. UART mode supports only metrics and command interface, not audio data streams.
   
Below is sample snapshot:

.. figure:: /images/AM62D_host_utility_snapshot.png
   :height: 600
   :width: 1200

- For more information on demo application and configuration, refer: `DSP Offload Example <https://github.com/TexasInstruments/rpmsg-dma/blob/scarthgap/example/audio_offload/host%20utility/README.md>`__.

***********************************
How to build audio DSP offload demo
***********************************

Building audio DSP offload image from Yocto
===========================================

- To build the Audio DSP offload image, refer :ref:`Processor SDK - Building the SDK with Yocto <building-the-sdk-with-yocto>`

Building the Linux demo binary from sources
===========================================

#. The source code for Audio DSP offload  demo is available as part of the `rpmsg-dma <https://github.com/TexasInstruments/rpmsg-dma/tree/scarthgap>`__.

   .. code-block:: console

      host# git clone https://github.com/TexasInstruments/rpmsg-dma.git -b scarthgap

#. Download and Install the AM62D Linux SDK from |__SDK_DOWNLOAD_URL__| following the steps mentioned at :ref:`Download and Install the SDK <download-and-install-sdk>`.

#. Prepare the environment for cross compilation.

   .. code-block:: console

      host# source <path to linux installer>/linux-devkit/environment-setup

#. Compile the source

    .. code-block:: console

       [linux-devkit]:> cd <path to rpmsg-dma source>
       [linux-devkit]:> cmake -S . -B build; cmake --build build

  - This will build:

    - The example application :file:`rpmsg_audio_offload_example`

  - Transfer the generated files to SD card:

    - The example binary :file:`rpmsg_audio_offload_example`  to :file:`/usr/bin`

    - The configuration file :file:`dsp_offload.cfg` to :file:`/etc`

    - The sample audio file :file:`sample_audio.wav` to :file:`/usr/share/`

    - The C7 DSP firmware file :file:`dsp_audio_filter_offload.c75ss0-0.release.strip.out` to :file:`/usr/lib/`

  - Optional:

    - To build only the library or only the example, use:

        .. code-block:: console

           cmake -S . -B build -DBUILD_LIB=OFF    # disables library build
           cmake -S . -B build -DBUILD_AUDIO_OFFLOAD_EXAMPLE=OFF # disables audio_offload example build
           cmake -S . -B build -DBUILD_2DFFT_OFFLOAD_EXAMPLE=OFF # disables 2dfft_offload example build


Building the c7 firmware from sources
=====================================

- Refer to the `MCU+ SDK Documentation  <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62DX/11_02_00_20/exports/docs/api_guide_am62dx/GETTING_STARTED_BUILD.html>`__
- Refer to the `C7 Demo Firmware <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62DX/11_02_00_20/exports/docs/api_guide_am62dx/EXAMPLES_DRIVERS_IPC_RPMESSAGE_LINUX_AUDIO_FILTER_OFFLOAD.html>`__
