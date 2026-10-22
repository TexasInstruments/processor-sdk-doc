.. _AM62D-edgeai-from-linux-user-guide:

##################
AM62D Edge AI Demo
##################

********
Overview
********

This guide describes how to set up, build, and run the Edge AI inference demo on the
Texas Instruments AM62D audio evaluation module (EVM). This demo showcases real-time
audio deep learning inference on the C7x DSP, including speech enhancement and audio
classification pipelines using TVM-compiled models. The following pre-compiled models
are included out of the box: GCRN (speech enhancement), YAMNet (521-class audio event
classification), and VGGish (10-class audio classification).
Below figure shows how this demo works:

.. figure:: /images/am62dx_edgeai.png
   :height: 400
   :width: 1200

- Step 1: Copy sample audio data to shared DMA Buffer (DDR)
   - The Linux application copies input audio data to a shared DMA buffer located
     in DDR memory for communication with the C7x DSP.

- Step 2: Notify DSP using RPMsg (IPC)
   - A53 sends a control message via RPMsg (Remote Processor Messaging) to the C7x
     core. This message informs the C7x that new input audio data is available for
     processing in the shared DDR buffer.

- Step 3: C7x receives RPMsg and processes the request
   - The C7x DSP receives the RPMsg message, reads the buffer address and parameters,
     and prepares for inference processing.

- Step 4: C7x reads from shared DMA Buffer into L2 SRAM
   - The C7x DSP copies the audio data from the DMA buffer (DDR) into its local L2
     SRAM for processing. This operation minimizes access latency compared to reading
     directly from DDR.

- Step 5: Inference execution on DSP
   - Below figure shows the inference signal chain executed on C7x:

   - STFT: Converts time-domain audio frames to frequency-domain spectral frames.
   - TVM Inference: Runs the selected TVM-compiled model (GCRN, YAMNet, or VGGish)
     on the C7x NPU.
   - ISTFT: For speech enhancement models, converts enhanced spectral output back to
     time-domain audio.

- Step 6: Inference results copied back to shared DMA Buffer (DDR)
   - Once DSP processing is complete, the output (inference results or enhanced audio)
     is copied back into the shared DMA buffer.

- Step 7: C7x notifies A53 using RPMsg
   - C7x sends a control message via RPMsg to the A53 core. This message informs the
     A53 that processed output data is available in the shared DDR buffer.

- Step 8: A53 receives RPMsg
   - The A53 Linux application receives the RPMsg notification from the C7x confirming
     that inference results are ready in the shared DDR buffer.

- Step 9: A53 reads back results from DMA buffer
   - A53 copies the inference results from the shared buffer. Depending on the pipeline:

   - **Speech enhancement**: Enhanced audio is saved to a WAV file or played back
     through the TAD5212 DAC via McASP.
   - **Audio classification**: Top-k class names and confidence scores are printed to
     the console or displayed in the web GUI.

**********************
Hardware Prerequisites
**********************

- `AM62D EVM <https://www.ti.com/tool/AUDIO-AM62D-EVM>`__

- Audio input source (e.g., microphone) connected to J1/J2 (PCM6240 ADC)

- Audio output device (e.g., headphones/speakers) connected to J3/J4 (TAD5212 DAC)

- SD card (minimum 16GB)

- USB Type-C 20W power supply (make sure to use type-C to type-C cable)

- USB-to-UART cable for console access

- PC (Windows or Linux) to flash image onto an SD Card

- Ethernet cable and the expansion board `DP83867-EVM-AM <https://www.ti.com/tool/DP83867-EVM-AM>`__ for network access

- Host PC Requirements:

  - Operating system:

    - Windows: |__WINDOWS_SUPPORTED_LONG__|

    - Ubuntu: |__LINUX_UBUNTU_VERSION_LONG__|

  - Memory: Minimum 4GB RAM (8GB or more recommended)

  - Storage: At least 10GB of free space

******************
Software and Tools
******************

- TI Processor SDK Linux EdgeAI (AM62Dx)

- MCU+ SDK for AM62Dx

- `TI Clang Compiler Toolchain <https://www.ti.com/tool/download/ARM-CGT-CLANG>`__

- CMake, GCC, make, git, scp, minicom

- `rpmsg-dma library <https://github.com/TexasInstruments/rpmsg-dma/tree/main>`__

*********
EVM Setup
*********

#. Cable Connections

   - The figure below shows some important cable connections, ports and switches.

   - Take note of the location of the "BOOTMODE" switch for SD card boot mode.

        .. figure:: /images/AM62D_evm_setup.png
           :height: 600
           :width: 1000

   - Refer `Quick Start Guide for AM62D EVM <https://dev.ti.com/tirex/explore/node?isTheia=false&node=A__ARZXwcKmAzaWG2hcFPpKRA__PROCESSORS-DEVTOOLS__FUz-xrs__LATEST>`__ for more details.

#. Setup UART Terminal

   - First identify the UART port as enumerated on the host machine.

   - Make sure that the EVM and UART cable are connected to the UART to USB port as shown in Cable Connections.

   - In Windows, you can use the "Device Manager" to see the detected UART ports.

   - If you do not see any USB serial ports listed under "Ports (COM & LPT)", install the UART to USB driver from `FTDI <https://www.ftdichip.com/drivers>`__.

   - For A53 Linux console, select UART boot port, keep other options to default and set 115200 baud rate.

#. Setup SD card Boot Mode

   - EVM SD card boot mode setting:

     - BOOTMODE [ 8 : 15 ] (SW3) = 0100 0000

     - BOOTMODE [ 0 : 7 ] (SW2) = 1100 0010

#. Audio Connections

   - Connect audio input source to J1 and J2 (PCM6240 ADC input).

   - Connect audio output to speakers/headphones via J3 and J4 (TAD5212 DAC output).

*************************
Steps to run Edge AI demo
*************************

There are two ways to run and visualize this demo:

Using Web GUI
=============

The AM62D EVM ships with a web-based GUI portal that provides an out-of-box way to
run speech enhancement and audio classification demos from any browser on the same
network — no additional software installation required.

#. Flash an SD card with the :file:`tisdk-edgeai-image-am62dxx-evm.rootfs.wic.xz`
   image and follow the instructions provided at :ref:`Create SD Card <processor-sdk-linux-create-sd-card>` guide.

#. Insert the flashed SD card into the AM62D EVM, connect audio input/output and
   Ethernet cable, then power on the EVM.

#. Make sure the EVM boot mode switches are set for SD card boot as described above.

#. The EVM should boot and display the Arago login prompt. Enter ``root`` to log in.

#. Get the EVM IP address:

   .. code-block:: console

      root@am62dxx-evm:~# ifconfig

#. Open a browser on your host PC and navigate to ``http://<EVM_IP>:3000``

#. On the home screen, click **Audio Intelligence** or select it from the left sidebar
   under **Demos**.

.. figure:: /images/am62dx_web_gui_home.png
   :align: center
   :width: 80%

   AM62D Web GUI — Audio Intelligence home screen

#. Select **Speech Enhancement** (GCRN) and click the run button to start noise
   reduction on the sample audio input.

.. figure:: /images/am62dx_web_gui_speech_enhancement.png
   :align: center
   :width: 80%

   AM62D Web GUI — Speech Enhancement demo

.. figure:: /images/am62dx_web_gui_speech_enhancement_result_1.png
   :align: center
   :width: 80%

   AM62D Web GUI — Speech Enhancement result

#. Select **Audio Classification** (YAMNet or VGGish) and click the run button to
   start audio event classification.

.. figure:: /images/am62dx_web_gui_audio_classification.png
   :align: center
   :width: 80%

   AM62D Web GUI — Audio Classification demo

.. figure:: /images/am62dx_web_gui_audio_classification_yamnet_result.png
   :align: center
   :width: 80%

   AM62D Web GUI — YAMNet classification result

.. figure:: /images/am62dx_web_gui_audio_classification_vggish_result.png
   :align: center
   :width: 80%

   AM62D Web GUI — VGGish classification result

Using Linux Inference Application
==================================

The ``rpmsg_inference_example`` C++ application provides a command-line interface to
run the same inference pipelines. For full details on building and running the application,
refer to :ref:`Audio Inference Application (C++ Runtime) <am62dx_linux_audio_inference_app>`.

#. Flash an SD card with the :file:`tisdk-edgeai-image-am62dxx-evm.rootfs.wic.xz`
   image and boot the EVM as described above.

#. Run speech enhancement (GCRN):

   .. code-block:: console

      root@am62dxx-evm:~# rpmsg_inference_example \
        /usr/share/tvm_inference/json/pipeline_speech_enhancement.json

#. Run audio classification (YAMNet):

   .. code-block:: console

      root@am62dxx-evm:~# rpmsg_inference_example \
        /usr/share/tvm_inference/json/pipeline_audio_classification_yamnet.json

#. Run audio classification (VGGish):

   .. code-block:: console

      root@am62dxx-evm:~# rpmsg_inference_example \
        /usr/share/tvm_inference/json/pipeline_audio_classification_vggish.json

For live ALSA input (classification pipelines only):

   .. code-block:: console

      root@am62dxx-evm:~# rpmsg_inference_example \
        /usr/share/tvm_inference/json/pipeline_audio_classification_yamnet.json \
        --device plughw:0,0

For raw PCM from stdin:

   .. code-block:: console

      root@am62dxx-evm:~# arecord -t raw -f S16_LE -c 1 -r 16000 | \
        rpmsg_inference_example \
          /usr/share/tvm_inference/json/pipeline_audio_classification_yamnet.json \
          --stream

*************************
How to build Edge AI demo
*************************

Building Edge AI image from Yocto
=================================

- To build the Edge AI image, refer :ref:`Processor SDK - Building the SDK with Yocto <building-the-sdk-with-yocto>`

Building the Linux inference application from sources
=====================================================

#. The source code is available as part of the `rpmsg-dma <https://github.com/TexasInstruments/rpmsg-dma/tree/main>`__ repository.

   .. code-block:: console

      host# git clone https://github.com/TexasInstruments/rpmsg-dma.git -b main

#. Download and Install the AM62D Linux SDK from |__SDK_DOWNLOAD_URL__| following
   the steps mentioned at :ref:`Download and Install the SDK <download-and-install-sdk>`.

#. Prepare the environment for cross compilation.

   .. code-block:: console

      host# source <path to linux installer>/linux-devkit/environment-setup

#. Compile the source:

   .. code-block:: console

      [linux-devkit]:> cd <path to rpmsg-dma source>
      [linux-devkit]:> cmake -S . -B build -DBUILD_EDGE_AI_EXAMPLE=ON \
                         -DBUILD_AUDIO_OFFLOAD_EXAMPLE=OFF \
                         -DBUILD_2DFFT_OFFLOAD_EXAMPLE=OFF \
                         -DBUILD_SIGNAL_CHAIN_BIQUAD_EXAMPLE=OFF
      [linux-devkit]:> cmake --build build

   - This builds:

     - The inference application :file:`rpmsg_inference_example`
     - The model daemon :file:`tvm_model_daemon`

   - Transfer the generated files to the EVM:

     .. code-block:: console

        host# scp build/example/edge-ai/rpmsg_inference_example root@<EVM_IP>:/usr/bin/
        host# scp build/example/edge-ai/tvm_model_daemon root@<EVM_IP>:/usr/bin/

Building the DSP firmware from sources
======================================

- Refer to the `MCU+ SDK Documentation <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62DX/12_00_00_22/exports/docs/api_guide_am62dx/GETTING_STARTED_BUILD.html>`__
- Refer to the `Edge AI TVM + DSP Multi-Model Signal Chain <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62DX/12_00_00_22/exports/docs/api_guide_am62dx>`__
