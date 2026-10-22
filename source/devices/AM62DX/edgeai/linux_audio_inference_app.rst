.. _am62dx_linux_audio_inference_app:

#########################################
Audio Inference Application (C++ Runtime)
#########################################

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

*********************
Building on AM62D EVM
*********************

The application is pre-installed on the AM62DX EdgeAI image. If you need to rebuild it
natively on the AM62D EVM, clone the source and build:

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

****************
Building on Host
****************

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

#. Install to a staging directory and transfer to the AM62D EVM:

   .. code-block:: console

      [linux-devkit]:> cmake --install build --prefix /tmp/edge-ai-install

   Transfer to the AM62D EVM:

   .. code-block:: console

      host# scp /tmp/edge-ai-install/bin/rpmsg_inference_example root@<EVM_IP>:/usr/bin/
      host# scp /tmp/edge-ai-install/bin/tvm_model_daemon root@<EVM_IP>:/usr/bin/
      host# scp -r /tmp/edge-ai-install/share/tvm_inference/ root@<EVM_IP>:/usr/share/

   Or copy directly to a mounted SD card:

   .. code-block:: console

      host# cp /tmp/edge-ai-install/bin/rpmsg_inference_example /mnt/rootfs/usr/bin/
      host# cp -r /tmp/edge-ai-install/share/tvm_inference/ /mnt/rootfs/usr/share/

Basic Syntax
============

.. code-block:: console

   rpmsg_inference_example <pipeline.json>                       # file input from JSON
   rpmsg_inference_example <pipeline.json> --device <alsa-dev>   # live ALSA capture
   rpmsg_inference_example <pipeline.json> --input-file <path>   # override input file
   rpmsg_inference_example <pipeline.json> --stream              # raw PCM from stdin
   rpmsg_inference_example <pipeline.json> --debug               # enable per-batch logs
   rpmsg_inference_example --preload                             # preload default model
   rpmsg_inference_example --version
   rpmsg_inference_example --help

*****************************
GCRN based Speech Enhancement
*****************************

Speech enhancement removes background noise from a recording while keeping the speech
intelligible — useful for voice calls, meeting recordings, hearables, and any product
that captures speech in a noisy environment.

Speech Enhancement Pipeline using GCRN
--------------------------------------

Run with the default WAV file input:

.. code-block:: console

   am62dxx-evm:~# rpmsg_inference_example /usr/share/tvm_inference/json/pipeline_speech_enhancement.json
   edge-ai v0.0.4 (built Sep 21 2026 10:14:19)
   ===========================================
   RPMsg Inference Example
   ===========================================

   [App] Pipeline type: speech_enhancement
   [App] Description: GCRN 3-stage speech pipeline: STFT analyze -> TVM inference -> ISTFT synthesize
   [App] TVM artifacts configured: /usr/share/tvm_inference/artifacts/gcrn
   [App] Model changed (/usr/share/tvm_inference/artifacts/yamnet -> /usr/share/tvm_inference/artifacts/gcrn), requesting daemon reload...
   [App] Daemon reloaded model: /usr/share/tvm_inference/artifacts/gcrn
   [App] Input configured: /usr/share/tvm_inference/input/input_audio.wav
   [App] Stages: 5
   [App] STFT parameters:  HOP=160 MODEL_ELEMS=322 BATCH_N=64 TOTAL_FRAMES=401
   [App] ISTFT parameters: HOP=160 MODEL_ELEMS=322 BATCH_N=64 TOTAL_FRAMES=401
   [App]   STFT spectral buffer: 516488 bytes
   [App]   ISTFT spectral buffer: 516488 bytes
   [App] Audio file info: 156302 samples, 16000Hz, 1 channel(s)
   [App] Loaded 156302 audio samples (9.76887 seconds)
   eptdev = rpmsg-char-8-1303
   Created endpt device rpmsg-char-8-1303, fd = 4 port = 1027
   [App] DMA buffers (reused across sequential stages):
   [App]   A (PCM / planar):  phys=0xc0600000 size=516488
   [App]   B (interleaved):   phys=0xc0680000 size=516488
   [App] Overlap-save chunking:
   [App]   TOTAL_FRAMES=401 OVERLAP_FRAMES=100 HOP_FRAMES=301 n_chunks=3
   [TVM] Connected to model daemon at /var/run/tvm-inference.sock
   [App] TVM initialized, input shape [1,2,401,161]
   [App] Chunk 1/3 [keep samples 0..56160] | STFT=17.3ms TVM=6782.4ms ISTFT=18.4ms total=6821.0ms
   [App] Chunk 2/3 [keep samples 8000..56160] | STFT=16.3ms TVM=6781.0ms ISTFT=17.7ms total=6817.6ms
   [App] Chunk 3/3 [keep samples 8000..59982] | STFT=16.3ms TVM=6780.0ms ISTFT=18.2ms total=6817.3ms
   [App] All chunks done | total=20456.2ms | 976 output frames (156302 samples)
   [App] Saving audio to: processed_output.wav
   [App] Output file info: 156302 samples, 16000Hz, 1 channel(s)
   [App] Successfully saved 156302 samples to processed_output.wav
   [App] Duration: 9.8 seconds
   [App] Saved to processed_output.wav
   PASSED

******************************************
YAMNet & VGGish based Audio Classification
******************************************

Audio event classification identifies *what* sound is present in a clip — a siren,
glass breaking, a dog barking, a machine running. YAMNet recognizes 521 general sound
classes, while VGGish is a smaller 10-class model. Pick YAMNet for broad coverage, or
VGGish when you need a lighter model for a fixed set of sounds.

Audio Classification pipeline using YAMNet
------------------------------------------

Run with the default WAV file input:

.. code-block:: console

   root@am62dxx-evm:~# rpmsg_inference_example /usr/share/tvm_inference/json/pipeline_audio_classification_yamnet.json
   edge-ai v0.0.4 (built Sep 21 2026 10:14:19)
   ===========================================
   RPMsg Inference Example
   ===========================================

   [App] Pipeline type: audio_classification
   [App] Description: YAMNet: speech -> STFT log-mel spectrogram -> TVM classification (521 classes)
   [App] TVM artifacts configured: /usr/share/tvm_inference/artifacts/yamnet
   [App] Model changed (/usr/share/tvm_inference/artifacts/vggish -> /usr/share/tvm_inference/artifacts/yamnet), requesting daemon reload...
   [App] Daemon reloaded model: /usr/share/tvm_inference/artifacts/yamnet
   [App] Input configured: /usr/share/tvm_inference/input/speech_whistling2.wav
   [App] Stages: 2
   [App] STFT parameters: HOP=160 MODEL_ELEMS=64 BATCH_N=64 TOTAL_FRAMES=96
   [TVM] Connected to model daemon at /var/run/tvm-inference.sock
   [App] TVM initialized, input shape [1,1,96,64]
   [App] Loaded 521 class labels from /usr/share/tvm_inference/labels/yamnet_label_list.txt
   [App] Audio file info: 78720 samples, 16000Hz, 1 channel(s)
   [App] Loaded 78720 audio samples (4.92 seconds)
   eptdev = rpmsg-char-8-1298
   Created endpt device rpmsg-char-8-1298, fd = 5 port = 1027
   [App] DMA buffers:
   [App]   audio in: phys=0xc01b8000 size=20480
   [App]   mel out:  phys=0xc01d8000 size=24576
   [App] Total frames: 492 | Full chunks: 5
   [App] Chunk 1/5 STFT=21.9ms TVM=26.1ms total=48.0ms
   [App] Chunk 1 top-5:
   [App]   1. 4.7947  Speech
   [App]   2. -2.6637  Narration, monologue
   [App]   3. -3.7292  Speech synthesizer
   [App]   4. -3.7292  Conversation
   [App]   5. -4.7947  Inside, small room
   [App] Chunk 2/5 STFT=9.4ms TVM=25.8ms total=35.2ms
   [App] Chunk 2 top-5:
   [App]   1. -1.5982  Animal
   [App]   2. -1.5982  Bird
   [App]   3. -1.5982  Whistling
   [App]   4. -2.1310  Wild animals
   [App]   5. -2.6637  Domestic animals, pets
   [App] Chunk 3/5 STFT=9.4ms TVM=26.0ms total=35.4ms
   [App] Chunk 3 top-5:
   [App]   1. 3.1965  Whistling
   [App]   2. -3.1965  Whistle
   [App]   3. -3.7292  Alarm
   [App]   4. -5.3275  Inside, small room
   [App]   5. -5.8602  Bird
   [App] Chunk 4/5 STFT=9.4ms TVM=26.3ms total=35.7ms
   [App] Chunk 4 top-5:
   [App]   1. 0.0000  Whistling
   [App]   2. -1.0655  Whistle
   [App]   3. -1.5982  Alarm
   [App]   4. -5.8602  Inside, small room
   [App]   5. -6.9257  Water
   [App] Chunk 5/5 STFT=9.4ms TVM=26.0ms total=35.4ms
   [App] Chunk 5 top-5:
   [App]   1. 2.6637  Whistle
   [App]   2. 1.0655  Alarm
   [App]   3. 0.5327  Whistling
   [App]   4. -5.3275  Inside, small room
   [App]   5. -5.8602  Steam whistle
   [App] Done: 492 mel frames | 5 TVM chunks | 190.3ms
   PASSED
   [App] Application exited with code 0

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

Audio Classification Pipeline using VGGish
------------------------------------------

Run with the default WAV file input:

.. code-block:: console

   root@am62dxx-evm:~# rpmsg_inference_example /usr/share/tvm_inference/json/pipeline_audio_classification_vggish.json
   edge-ai v0.0.4 (built Sep 21 2026 10:14:19)
   ===========================================
   RPMsg Inference Example
   ===========================================

   [App] Pipeline type: audio_classification
   [App] Description: VGGish: audio -> STFT log-mel spectrogram -> TVM classification (UrbanSound8K 10 classes)
   [App] TVM artifacts configured: /usr/share/tvm_inference/artifacts/vggish
   [App] Model changed (/usr/share/tvm_inference/artifacts/gcrn -> /usr/share/tvm_inference/artifacts/vggish), requesting daemon reload...
   [App] Daemon reloaded model: /usr/share/tvm_inference/artifacts/vggish
   [App] Input configured: /usr/share/tvm_inference/input/urbansound_16k.wav
   [App] Stages: 2
   [App] STFT parameters: HOP=512 MODEL_ELEMS=64 BATCH_N=64 TOTAL_FRAMES=126
   [TVM] Connected to model daemon at /var/run/tvm-inference.sock
   [App] TVM initialized, input shape [1,1,126,64]
   [App] Loaded 10 class labels from /usr/share/tvm_inference/labels/vggish_label_list.txt
   [App] Audio file info: 128000 samples, 16000Hz, 1 channel(s)
   [App] Loaded 128000 audio samples (8 seconds)
   eptdev = rpmsg-char-8-1290
   Created endpt device rpmsg-char-8-1290, fd = 5 port = 1027
   [App] DMA buffers:
   [App]   audio in: phys=0xc02b0000 size=65536
   [App]   mel out:  phys=0xc01b8000 size=32256
   [App] Total frames: 250 | Full chunks: 1
   [App] Chunk 1/1 STFT=44.4ms TVM=31.1ms total=75.5ms
   [App] Chunk 1 top-5:
   [App]   1. 8.4112  Street music
   [App]   2. 8.2060  Children playing
   [App]   3. -4.5133  Air conditioner
   [App]   4. -5.1288  Dog bark
   [App]   5. -5.5391  Car horn
   [App] Done: 250 mel frames | 1 TVM chunks | 75.6ms
   PASSED
   [App] Application exited with code 0
