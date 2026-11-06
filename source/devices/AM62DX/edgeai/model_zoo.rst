.. include:: <isonum.txt>

.. _edgeai_model_zoo:

################
EdgeAI Model Zoo
################

The EdgeAI ModelZoo delivers out-of-box audio deep-learning demos that run
directly on the |__PART_FAMILY_NAME__| target. Each reference model ships as an
`ONNX <https://onnx.ai/>`__ graph plus, where applicable, a pre-compiled
TVM-RT + TIDL artifact, so you can reproduce these examples on the AM62D without
compiling anything yourself. Two demo front-ends are provided: standalone
Python inference scripts and Jupyter notebooks. The same on-target runtime hosts
your own compiled artifacts once you build them through the x86 flow. This
section runs entirely **on the target**; the x86 compile-and-evaluate flow is covered
in :ref:`Model Compile and Evaluate <edgeai_compile_evaluate>`.

.. note::

   The models in this repository are made available for experimentation and
   development. They are not intended for deployment in production.

**********
What ships
**********

.. list-table::
   :header-rows: 1
   :widths: 18 26 14 14 28

   * - Model
     - Task
     - Model ID
     - On target
     - Demo
   * - VGGish11
     - Sound classification (UrbanSound8K)
     - ``ac-0101``
     - C7\ |trade| NPU (TVM-RT + TIDL, 8-bit)
     - Script + notebook
   * - YAMNet
     - Sound classification (UrbanSound8K)
     - ``ac-0201``
     - C7\ |trade| NPU (TVM-RT + TIDL, 8-bit)
     - Script + notebook
   * - GCRN
     - Speech enhancement (VoiceBank-DEMAND-16k)
     - ``ase-0201``
     - C7\ |trade| NPU (TVM-RT + TIDL, 16-bit)
     - Script + notebook

VGGish11, YAMNet, and GCRN each ship a pre-compiled TVM-RT + TIDL artifact and
run offloaded to the C7\ |trade| NPU.

***************
On-target setup
***************

The steps below run on the AM62D target (aarch64), on the Linux command line of
the Processor SDK rootfs. The notebooks and scripts run in a Python virtual
environment that reuses the TIDL-enabled TVM runtime already present in the
rootfs.

#. **Clone the repository.** Clone the AudioAI ModelZoo repository
   (https://github.com/TexasInstruments/audioai-modelzoo):

   .. code-block:: console

      $ mkdir -p ~/tidl && cd ~/tidl
      $ git clone https://github.com/TexasInstruments/audioai-modelzoo.git
      $ cd audioai-modelzoo

#. **Download the model artifacts.** Downloads the three pre-compiled
   TVM-RT + TIDL artifacts (VGGish11, YAMNet, GCRN)

   .. code-block:: console

      $ ./download_models.sh -y

   The script defaults to an interactive selection menu; the ``-y`` flag
   downloads everything non-interactively. Add ``-l`` to print the source URLs
   without downloading.

#. **Create the virtual environment.** Creates the venv at
   ~/venv/modelzoo with ``--system-site-packages`` so the TIDL-enabled
   runtime from the rootfs is visible:

   .. code-block:: console

      $ ./setup_venv.sh

#. **Activate the venv.** Activate it in every new shell before running the
   demos:

   .. code-block:: console

      $ source ~/venv/modelzoo/bin/activate

**********************
Inference script demos
**********************

Run each script from its own model directory in the activated venv. All four
models ship a command-line script.

YAMNet (sound classification)
=============================

.. code-block:: console

   $ cd ~/tidl/audioai-modelzoo/inference/yamnet_sc
   $ python3 yamnet_infer_audio.py --audio-file samples/miaow_16k.wav

The script converts the audio into log-mel patches, runs each patch through
the TVM-RT + TIDL session, and averages the per-patch scores. For the bundled
:file:`miaow_16k.wav` clip the top classes are cat/animal sounds. Expected output
(abridged):

.. code-block:: text

   ======================================================================
   YAMNET INFERENCE SUMMARY
   ======================================================================

   Audio File: miaow_16k.wav
   Artifacts: ac-0201_tvmrt_audio_classification_urbansound8k_yamnet_onnx
   Audio Duration: 6.73 seconds
   Number of Patches: 7

   ======================================================================
   TOP 10 PREDICTIONS (averaged across all patches):
   ======================================================================
   Rank   Score      Class
   ----------------------------------------------------------------------
   1      ...        Cat
   2      ...        Animal
   ...
   ======================================================================
   PERFORMANCE METRICS:
   ======================================================================
   Inference Time (all patches): 17.53 ms total | 7 patches
   RTF = 0.0026 (0.018s / 6.73s)
   ======================================================================

A second sample, :file:`samples/speech_whistling2.wav`, is also included.

VGGish11 (sound classification)
===============================

.. code-block:: console

   $ cd ~/tidl/audioai-modelzoo/inference/vggish11_sc
   $ python3 vggish_infer_audio.py --audio-file sample_wav/139951-9-0-9.wav

The bundled clip is UrbanSound8K class 9 (street music). Expected
output (abridged):

.. code-block:: text

   ======================================================================
   VGGISH11 INFERENCE SUMMARY
   ======================================================================

   Audio File: 139951-9-0-9.wav
   Artifacts: ac-0101_tvmrt_audio_classification_urbansound8k_vggish11_onnx
   Audio Duration: 4.00 seconds
   Top Class: Street music (Class 9) - Score: ...

   Performance:
     Inference: 8.88 ms
     Throughput: RTF = 0.0022 (0.009s / 4.00s)
   ======================================================================

GCRN (speech enhancement)
=========================

.. code-block:: console

   $ cd ~/tidl/audioai-modelzoo/inference/gcrn_se
   $ python3 gcrn_infer_audio.py --input sample_wav/noisy.wav

The script writes the enhanced audio to :file:`enhanced.wav` beside the input and a
per-block timing report to :file:`gcrn-benchmark.md`. Pass ``--output`` to change
the destination wav. Expected output (abridged):

.. code-block:: text

   Machine: aarch64  SOC: am62d  TIDL_VER: ...
   Loading TVM + TIDL session...
   Running inference on noisy.wav (9.77s)...
   Wrote enhanced audio to sample_wav/enhanced.wav

   GCRN TVM+TIDL benchmark (3 chunk(s), 9.77s audio)

   block                    total (ms)  per-chunk (ms)
   ...
   Real-Time Factor (inference / audio) = 3.9500

   Wrote benchmark report to sample_wav/gcrn-benchmark.md

.. _edgeai_model_zoo_notebooks:

**********************
Jupyter notebook demos
**********************

All four reference models have a Jupyter notebook demo. Start Jupyter Lab from
the activated venv:

.. code-block:: console

   $ cd ~/tidl/audioai-modelzoo
   $ ./jupyter_lab_venv.sh

The launcher prints a highlighted access URL. Open the URL in a browser on a
machine that can reach the target and enter the token ``tidl`` when prompted:

.. code-block:: text

   Access URL: http://<target-ip>:8888/lab?token=tidl

Jupyter Lab opens with the GCRN notebook loaded. To run a different model, pick
its notebook from the file browser in the left sidebar. The notebooks are:

.. list-table::
   :header-rows: 1
   :widths: 22 40

   * - Model
     - Notebook
   * - GCRN
     - ``inference/gcrn_se/gcrn_inference.ipynb``
   * - VGGish11
     - ``inference/vggish11_sc/vggish_inference.ipynb``
   * - YAMNet
     - ``inference/yamnet_sc/yamnet_inference.ipynb``

******************
Compiled artifacts
******************

:file:`download_models.sh` places the artifacts under
:file:`model_artifacts/<TIDL_VER>/am62d/`. Each model gets its own directory,
named after its model ID, containing a ``model/`` folder (the trained ONNX
model) and, where applicable, an ``artifacts/`` folder (the compiled model
artifacts). VGGish11, YAMNet, and GCRN each get a pre-compiled TVM-RT + TIDL
artifact:

- ``ac-0101`` - ``ac-0101_tvmrt_audio_classification_urbansound8k_vggish11_onnx`` (VGGish11)
- ``ac-0201`` - ``ac-0201_tvmrt_audio_classification_urbansound8k_yamnet_onnx`` (YAMNet)
- ``ase-0201`` - ``ase-0201_tvmrt_speech_enhancement_voicebank_demand_16k_gcrn_fixed_4sec_onnx`` (GCRN)

Each of those artifact directories' :file:`artifacts/` folder holds the TVM-RT
deployment artifacts (:file:`deploy_lib.so`, :file:`deploy_graph.json`, :file:`deploy_param.params`)
in both target (``.evm``, aarch64) and host (``.pc``, x86) variants. The demo
scripts and notebooks select the ``.evm`` variant automatically on the target.
