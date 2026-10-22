.. _am62dx_linux_audio_inference_app:

##########################################
How to run Linux C++ Inference Application
##########################################

Introduction
============

The AM62DX audio inference application (``rpmsg_inference_example``) is a C++ application
for running configurable audio and tensor pipelines across Linux and the C7x DSP. It is part
of the `rpmsg-dma <https://github.com/TexasInstruments/rpmsg-dma>`__ repository. The
application enables:

- **Real-time Audio Processing** — Process live ALSA audio devices or WAV file inputs
- **DSP Offload** — Offload STFT, ISTFT and deinterleave/interleave to the C7x DSP over RPMsg-DMA
- **TVM Inference** — Run TVM-compiled deep learning models on the C7x NPU
- **Flexible I/O** — WAV files, live ALSA capture, raw PCM streams, or binary tensors
- **JSON Pipeline Configuration** — Define processing chains via JSON files
- **Model Daemon Mode** — Persistent TVM model daemon to avoid repeated artifact loading

Supported Pipelines
===================

.. list-table::
   :header-rows: 1
   :widths: 30 30 20 20

   * - Pipeline
     - JSON file
     - Default input
     - Output
   * - Speech enhancement (GCRN)
     - ``pipeline_speech_enhancement.json``
     - ``input_audio.wav``
     - Enhanced WAV file
   * - Audio classification (YAMNet)
     - ``pipeline_audio_classification_yamnet.json``
     - ``speech_whistling2.wav``
     - Top-k class names and scores
   * - Audio classification (VGGish)
     - ``pipeline_audio_classification_vggish.json``
     - ``urbansound_16k.wav``
     - Top-k class names and scores

Prerequisites
=============

All runtime libraries, model artifacts, sample audio files, model daemon, and DSP firmware
verification are pre-packaged in the AM62DX EdgeAI image. See
:ref:`Models, Artifacts and Setup <am62dx_edgeai_models_artifacts_and_setup>` for details.

To build the application from source, the following host tools are required:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Tool
     - Purpose
   * - ARM Clang Toolchain
     - From Processor SDK Linux devkit; for cross-compilation
   * - CMake 3.10 or higher
     - Build system
   * - ``make``, ``git``
     - Build utilities
   * - Neo-TVM headers (``TVM_ROOT``)
     - Refer to `TI TVM Documentation <http://tvm-tidl-04.dhcp.ti.com:9090/index.html>`__

*******************************
Building on AUDIO-AM62D-EVM
*******************************

The application is pre-installed on the AM62DX EdgeAI image. If you need to rebuild it
natively on the AUDIO-AM62D-EVM, clone the source and build:

.. code-block:: console

   root@am62dxx-evm:~# git clone https://github.com/TexasInstruments/rpmsg-dma.git -b main
   root@am62dxx-evm:~# cd rpmsg-dma

The example is under ``example/edge-ai/`` and contains:

.. code-block:: text

   example/edge-ai/
   ├── CMakeLists.txt
   ├── src/                  application source files
   ├── include/              header files
   ├── json_files/           pipeline JSON configurations
   ├── labels/               classification label files
   ├── input_audio/          sample WAV input files
   ├── tvm-model-daemon.service
   └── tvm-model-preload.service

.. code-block:: console

   root@am62dxx-evm:~/rpmsg-dma# cmake -S . -B build -DBUILD_EDGE_AI_EXAMPLE=ON \
                      -DBUILD_AUDIO_OFFLOAD_EXAMPLE=OFF \
                      -DBUILD_2DFFT_OFFLOAD_EXAMPLE=OFF \
                      -DBUILD_SIGNAL_CHAIN_BIQUAD_EXAMPLE=OFF
   root@am62dxx-evm:~/rpmsg-dma# cmake --build build

**********************
Building on Host
**********************

#. Download and install the AM62DX Linux SDK from |__SDK_DOWNLOAD_URL__|.
   Extract the SDK tarball and run the installer script on your development host.

#. Prepare the environment for cross compilation:

   .. code-block:: console

      host# source <path to linux installer>/linux-devkit/environment-setup

#. Set the Neo-TVM path. Either pass it directly to CMake or export it as an
   environment variable:

   .. code-block:: console

      host# export NEO_TVM_PATH=/path/to/neo-tvm

   Or pass it on the CMake command line:

   .. code-block:: console

      host# cmake -S . -B build -DTVM_ROOT=/path/to/neo-tvm

   If the TVM runtime library is not at ``${TVM_ROOT}/libtvm_runtime.so``, specify
   it explicitly:

   .. code-block:: console

      host# cmake -S . -B build \
              -DTVM_ROOT=/path/to/neo-tvm \
              -DTVM_RUNTIME_LIB=/path/to/aarch64/libtvm_runtime.so

#. Clone the source and build only the edge-ai example:

   .. code-block:: console

      host# git clone https://github.com/TexasInstruments/rpmsg-dma.git -b main
      host# cd rpmsg-dma

   .. code-block:: console

      [linux-devkit]:> cmake -S . -B build -DBUILD_EDGE_AI_EXAMPLE=ON \
                         -DBUILD_AUDIO_OFFLOAD_EXAMPLE=OFF \
                         -DBUILD_2DFFT_OFFLOAD_EXAMPLE=OFF \
                         -DBUILD_SIGNAL_CHAIN_BIQUAD_EXAMPLE=OFF
      [linux-devkit]:> cmake --build build

#. This builds:

   - ``build/example/edge-ai/rpmsg_inference_example`` — main inference application
   - ``build/example/edge-ai/tvm_model_daemon`` — persistent model daemon

#. Install to a staging directory and transfer to the AUDIO-AM62D-EVM:

   .. code-block:: console

      [linux-devkit]:> cmake --install build --prefix /tmp/edge-ai-install

   Transfer to the AUDIO-AM62D-EVM:

   .. code-block:: console

      host# scp /tmp/edge-ai-install/bin/rpmsg_inference_example root@<EVM_IP>:/usr/bin/
      host# scp /tmp/edge-ai-install/bin/tvm_model_daemon root@<EVM_IP>:/usr/bin/
      host# scp -r /tmp/edge-ai-install/share/tvm_inference/ root@<EVM_IP>:/usr/share/

   Or copy directly to a mounted SD card:

   .. code-block:: console

      host# cp /tmp/edge-ai-install/bin/rpmsg_inference_example /mnt/rootfs/usr/bin/
      host# cp -r /tmp/edge-ai-install/share/tvm_inference/ /mnt/rootfs/usr/share/

*************************************
Running Pipelines
*************************************

Basic Syntax
============

.. code-block:: console

   rpmsg_inference_example <pipeline.json> [options]

Additional options:

.. code-block:: console

   rpmsg_inference_example --help
   rpmsg_inference_example --version
   rpmsg_inference_example <pipeline.json> --debug

******************************************
GCRN based Speech Enhancement
******************************************

Speech enhancement removes background noise from a recording while keeping the speech
intelligible — useful for voice calls, meeting recordings, hearables, and any product
that captures speech in a noisy environment.

**************************************************
How to run Linux C++ based GCRN Speech Enhancement
**************************************************

Run with the default WAV file input:

.. code-block:: console

   root@am62dxx-evm:~# rpmsg_inference_example \
     /usr/share/tvm_inference/json/pipeline_speech_enhancement.json

******************************************
YAMNet & VGGish based Audio Classification
******************************************

Audio event classification identifies *what* sound is present in a clip — a siren,
glass breaking, a dog barking, a machine running. YAMNet recognizes 521 general sound
classes, while VGGish is a smaller 10-class model. Pick YAMNet for broad coverage, or
VGGish when you need a lighter model for a fixed set of sounds.

******************************************************
How to run Linux C++ based YAMNet Audio Classification
******************************************************

Run with the default WAV file input:

.. code-block:: console

   root@am62dxx-evm:~# rpmsg_inference_example \
     /usr/share/tvm_inference/json/pipeline_audio_classification_yamnet.json \
     --input-file /usr/share/tvm_inference/input/speech_whistling2.wav

Live ALSA device input:

.. code-block:: console

   root@am62dxx-evm:~# rpmsg_inference_example \
     /usr/share/tvm_inference/json/pipeline_audio_classification_yamnet.json \
     --device plughw:0,0

Stream raw PCM from stdin (mono, S16_LE, 16 kHz):

.. code-block:: console

   root@am62dxx-evm:~# arecord -t raw -f S16_LE -c 1 -r 16000 | \
     rpmsg_inference_example \
       /usr/share/tvm_inference/json/pipeline_audio_classification_yamnet.json \
       --stream

******************************************************
How to run Linux C++ based VGGish Audio Classification
******************************************************

Run with the default WAV file input:

.. code-block:: console

   root@am62dxx-evm:~# rpmsg_inference_example \
     /usr/share/tvm_inference/json/pipeline_audio_classification_vggish.json \
     --input-file /usr/share/tvm_inference/input/urbansound_16k.wav
