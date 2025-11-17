.. _AM62D-2dfft-dsp-offload-from-linux-user-guide:

###################################
AM62D 2D FFT DSP offload from Linux
###################################

********
Overview
********

This guide describes how to set up, build, and run the 2D Fast Fourier Transform (FFT)
Digital Signal Processing (DSP) offload example by using the Texas Instruments
Audio AM62D evaluation module (EVM). This demo example shows how to offload 2D
Fast Fourier Transform (FFT) computation to the C7x DSP from Linux user-space.
The input is a 128x128 complex matrix, and the output is the 2D FFT transformed
data in the same format.

Below figure shows how this demo works:

.. figure:: /images/AM62D_2DFFT_DSP_offload_Demo.png
   :height: 450
   :width: 1000

- Step 1: Read test data
   - The 2D FFT offload example application reads the 128x128 matrix binary
     test data from SD card.

- Step 2: Copy data to shared Direct Memory Access (DMA) Buffer (DDR)
   - Copies input data to a shared DMA buffer located in DDR memory.

- Step 3: Notify DSP using RPMsg (IPC)
   - A53 sends a control message via RPMsg (Remote Processor Messaging) to
     the C7x core. This message informs the C7x that 2D FFT test input data
     is available for processing in the shared DDR buffer.

- Step 4: C7x reads from shared DMA Buffer into L2 Static Random Access Memory (SRAM)
   - The C7x DSP copies the input data from the DMA buffer (DDR) into its local
     L2 SRAM for processing. This operation minimizes access latency compared
     to reading directly from DDR and performs 2D FFT computation on C7x.

- Step 5:2D FFT computation on DSP
   - Below figure shows 2D FFT computation on C7x.

   .. figure:: /images/fft_2d_signal_chain.png
      :height: 140
      :width: 1000

   - 1D Batched FFT: C7x performs the first 1D FFT on the rows.
   - Matrix Transpose: The system transposes the data matrix to convert columns to
     rows and vice versa. Because as per design, FFTLIB libraries to perform FFT
     on 1D data in rows format.
   - 1D Batched FFT: C7x performs the second 1D FFT on the column data.
   - During processing, the C7x moves data between L2SRAM (lower latency, lower
     capacity) and DDR (higher capacity, higher latency) to use memory efficiently.

- Step 6: Processed data copied back to shared DMA Buffer (DDR)
   - Once DSP processing is complete, the C7x copies the output (2D FFT transformed data)
     back into the shared DMA buffer.
   - C7x sends a control message via RPMsg to the A53 core, informing it that
     processed output data is available in the shared DDR buffer.

- Step 7: A53 reads back processed data from DMA buffer
   - A53 copies the processed data from the shared buffer for validation. 

- Step 8: Validation and Performance Reporting
   - The application compares the output data against expected results to verify correctness.
   - The system displays performance metrics:
     - DSP Load (%)
     - Cycle Count
     - DDR Throughput (MB/s)

**********************
Hardware prerequisites
**********************

- `AM62D-EVM <https://www.ti.com/tool/AUDIO-AM62D-EVM>`__
- Secure Digital (SD) card (minimum 16GB)
- Universal Serial Bus (USB) Type-C 20W power supply (make sure to use type-C to type-C cable)
- USB to Universal asynchronous receiver-transmitter (UART) cable for console access
- PC (Windows or Linux) to flash image onto an SD Card
- Host PC Requirements:
  
  - Operating system:
    
    - Windows: |__WINDOWS_SUPPORTED_LONG__|
    - Ubuntu: |__LINUX_UBUNTU_VERSION_LONG__|
  
  - Memory: Minimum 4GB RAM (8GB or more recommended)
  - Storage: At least 10GB of free space

******************
Software and tools
******************

- TI Processor SDK Linux RT (AM62Dx)
- MCU+SDK for AM62Dx
- `C7000-CGT <https://www.ti.com/tool/C7000-CGT#downloads>`__ compiler
- `Code Composer Studio <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62DX/11_00_00_16/exports/docs/api_guide_am62dx/CCS_PROJECTS_PAGE.html>`__
- `TI Clang Compiler Toolchain <https://www.ti.com/tool/download/ARM-CGT-CLANG>`__
- CMake, GCC, make, git, scp, minicom
- `rpmsg-dma library <https://github.com/TexasInstruments/rpmsg-dma/tree/scarthgap>`__

*********
EVM setup
*********

#. Cable Connections
   
   - The figure below shows some important cable connections, ports and switches.
   - Take note of the location of the "BOOTMODE" switch for SD card boot mode.
   
   .. figure:: /images/AM62D_evm_setup.png
      :height: 600
      :width: 1000

#. Setup UART Terminal
   
   - First identify the UART port as enumerated on the host machine.
   - Connect the EVM and UART cable to the UART to USB port as shown in cable
     connections.
   - In Windows, you can use the "Device Manager" to see the detected UART ports:
     
     - Search "Device Manager" in Windows Search Box in the Windows taskbar.
   
   - If you do not see any USB serial ports listed in "Device Manager" under
     "Ports (COM & LPT)", then make sure you have installed the UART to USB
     driver from `FTDI <https://www.ftdichip.com/drivers>`__.
   - For A53 Linux console, select UART boot port (ex: COM34 in below screenshot),
     keep other options to default and set 115200 baud rate.

#. Setup SD card Boot Mode
   
   - EVM SD card boot mode setting:
     
     - BOOTMODE [ 8 : 15 ] (SW3) = 0100 0000
     - BOOTMODE [ 0 : 7 ] (SW2) = 1100 0010

*****************************************
Steps to validate 2D FFT DSP offload demo
*****************************************

#. Flash an SD card with the :file:`tisdk-default-image-rt-am62dxx-evm.rootfs.wic.xz`
   image and follow the instructions provided at :ref:`Create SD Card <processor-sdk-linux-create-sd-card>` guide.

#. Insert the flashed SD card into the `AUDIO-AM62D-EVM <https://www.ti.com/tool/AUDIO-AM62D-EVM>`__
   and power on the TI AUDIO-AM62D-EVM.

#. Make sure the EVM boot mode switches are positioned for SD card boot as
   described earlier.

#. Connect the USB-C cable from the power adapter to one of the two USB-C
   ports on the EVM.

#. The EVM should boot and the booting progress should display in the serial
   port console. At the end of booting, the Arago login prompt will appear.
   Just enter "root" to log in.

#. Run the 2D FFT DSP offload demo application from the console:
   
   .. code-block:: console
      
      root@am62dxx-evm:~# rpmsg_2dfft_example

#. The application will execute and display the results:
   
   .. code-block:: console
      
      RPMsg based 2D FFT Offload Example
      
      *****************************************
      *****************************************
      
      C7x 2DFFT Test PASSED
      C7x Load: 1%
      C7x Cycle Count: 327000
      C7x DDR Throughput: 0.801656 MB/s
      
      *****************************************
      *****************************************

.. note::
   
   The test reports "PASSED" if the computed 2D FFT output matches the
   expected results within tolerance (0.01), otherwise it reports "FAILED".

Demo output interpretation
==========================

The demo provides the following performance metrics:

- **Test Result**: PASSED or FAILED based on output validation
- **C7x Load**: DSP utilization percentage during FFT computation
- **C7x Cycle Count**: Number of DSP cycles consumed for the operation
- **C7x DDR Throughput**: Data transfer rate to/from DDR memory in MB/s

************************************
How to build 2D FFT DSP offload demo
************************************

Building 2D FFT DSP offload image from yocto
============================================

- To build the 2D FFT DSP offload image, refer :ref:`Processor SDK - Building the SDK with Yocto <building-the-sdk-with-yocto>`

Building the linux demo binary from sources
===========================================

#. The source code for the 2D FFT DSP offload demo is available as part of
   the `rpmsg-dma <https://github.com/TexasInstruments/rpmsg-dma/tree/scarthgap>`__.
   
   .. code-block:: console
      
      host# git clone https://github.com/TexasInstruments/rpmsg-dma.git -b scarthgap

#. Download and Install the AM62D Linux SDK from |__SDK_DOWNLOAD_URL__| following
   the steps mentioned at :ref:`Download and Install the SDK <download-and-install-sdk>`.

#. Prepare the environment for cross compilation.
   
   .. code-block:: console
      
      host# source <path to linux installer>/linux-devkit/environment-setup

#. Compile the source:
   
   .. code-block:: console
      
      [linux-devkit]:> cd <path to rpmsg-dma source>
      [linux-devkit]:> cmake -S . -B build; cmake --build build
   
   - This command builds:
     
     - The example application :file:`rpmsg_2dfft_example`
   
   - Transfer the generated files to SD card:
     
     - The example binary :file:`rpmsg_2dfft_example` to :file:`/usr/bin`
     - The test input data file :file:`2dfft_input_data.bin` to :file:`/usr/share/2dfft_test_data/`
     - The expected output data file :file:`2dfft_expected_output_data.bin` to :file:`/usr/share/2dfft_test_data/`
     - The C7 DSP firmware file :file:`fft2d_linux_dsp_offload_example.c75ss0-0.release.strip.out` to :file:`/lib/firmware/`
   
   - Optional:
     
     - To build only the library or only the example, use:
       
       .. code-block:: console
          
          cmake -S . -B build -DBUILD_LIB=OFF    # disables library build
          cmake -S . -B build -DBUILD_AUDIO_OFFLOAD_EXAMPLE=OFF # disables audio_offload example build
          cmake -S . -B build -DBUILD_2DFFT_OFFLOAD_EXAMPLE=OFF # disables 2dfft_offload example build

Building the C7 firmware from sources
=====================================

- Refer to the `MCU+ SDK Documentation  <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62DX/11_02_00_20/exports/docs/api_guide_am62dx/GETTING_STARTED_BUILD.html>`__
- Refer to the `C7x TISP Linux 2D FFT Offload Example <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62DX/11_02_00_20/exports/docs/api_guide_am62dx/EXAMPLES_TISP_FFT2D_LINUX_DSP_OFFLOAD.html>`__
