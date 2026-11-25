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
   * - GCRN-mod-g16
     - Speech enhancement (VoiceBank-DEMAND-16k)
     - ``ase-0212``
     - C7\ |trade| NPU (TVM-RT + TIDL, 16-bit; LSTM FP32)
     - Script + notebook
   * - GTCRN
     - Speech enhancement (VoiceBank-DEMAND-16k)
     - ``ase-0100``
     - Arm CPU (ONNX Runtime, FP32)
     - Script + notebook

VGGish11, YAMNet, and GCRN-mod-g16 each ship a pre-compiled TVM-RT + TIDL
artifact and run offloaded to the C7\ |trade| NPU. GTCRN needs no compilation: it
ships as the ONNX model only and runs in FP32 on the Arm CPU through ONNX Runtime,
already faster than real time.

GCRN-mod-g16 is a GCRN variant modified by TI for TIDL. It keeps the grouped LSTM
of the original GCRN (16 groups), and rewrites only the encoder and decoder
layers with exact transforms that keep the trained weights. The whole model
offloads to the C7\ |trade| NPU as a single TIDL subgraph, with no layers left
for TVM code generation. The encoder and decoder layers are quantized to 16 bits.
The LSTM layers run in FP32: TIDL runs an LSTM in fixed point only when both its
hidden size and its input size are greater than 64, and each of the 16 LSTM
groups has size 64. :ref:`Model Compile and Evaluate <edgeai_compile_evaluate>`
also covers GCRN-mod-g8, whose 8 wider LSTM groups are quantized to 16 bits.

Model cards
===========

Each model directory in the repository has a model card,
:file:`inference/<model>/README.md`. A model card lists the parameter and MAC
counts, input and output shapes, precision and TIDL offload, the model origin
and paper, the architecture, the pre-processing settings, any TI modifications,
and the reference accuracy:

.. list-table::
   :header-rows: 1
   :widths: 22 40

   * - Model
     - Model card
   * - GCRN-mod-g16
     - :file:`inference/gcrn_se/README.md`
   * - GTCRN
     - :file:`inference/gtcrn_se/README.md`
   * - VGGish11
     - :file:`inference/vggish11_sc/README.md`
   * - YAMNet
     - :file:`inference/yamnet_sc/README.md`

The repository :file:`README.md` also has a model summary table that compares
the four models.

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
   TVM-RT + TIDL artifacts (VGGish11, YAMNet, GCRN-mod-g16) and the GTCRN ONNX model:

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
models ship a command-line script. Each script prints its results and the
inference time to the console.

YAMNet (sound classification)
=============================

.. code-block:: console

   $ cd ~/tidl/audioai-modelzoo/inference/yamnet_sc
   $ python3 yamnet_infer_audio.py --audio-file samples/miaow_16k.wav

The script converts the audio into log-mel patches, runs each patch through
the TVM-RT + TIDL session, and averages the per-patch scores. For the bundled
:file:`miaow_16k.wav` clip the top classes are cat/animal sounds.

A second sample, :file:`samples/speech_whistling2.wav`, is also included.

VGGish11 (sound classification)
===============================

.. code-block:: console

   $ cd ~/tidl/audioai-modelzoo/inference/vggish11_sc
   $ python3 vggish_infer_audio.py --audio-file sample_wav/139951-9-0-9.wav

The script prints the top class and its score, followed by the inference time
and real-time factor (RTF). The bundled clip is UrbanSound8K class 9 (street
music).

GCRN-mod-g16 (speech enhancement)
=================================

.. code-block:: console

   $ cd ~/tidl/audioai-modelzoo/inference/gcrn_se
   $ python3 gcrn_infer_audio.py --input sample_wav/noisy.wav

The script writes the enhanced audio to :file:`enhanced.wav` beside the input and a
per-block timing report to :file:`gcrn-benchmark.md`. Pass ``--output`` to change
the destination wav. The script processes the file in 4-second chunks that
overlap by 1 second and reports two real-time factors: the model RTF divides the
inference time by the audio actually processed (all chunks), and the file RTF
divides it by the duration of the input file.

GTCRN (speech enhancement)
==========================

.. code-block:: console

   $ cd ~/tidl/audioai-modelzoo/inference/gtcrn_se
   $ python3 gtcrn_infer_audio.py --input sample_wav/mix.wav

The script runs the ONNX model on the Arm CPU through ONNX Runtime; no TIDL
artifact is involved. It writes the enhanced audio to :file:`enh_onnx.wav` beside
the input and prints a per-block timing table. Pass ``--output`` to change the
destination wav.

.. _edgeai_model_zoo_notebooks:

**********************
Jupyter notebook demos
**********************

All four models have a Jupyter notebook demo. Start Jupyter Lab from
the activated venv:

.. code-block:: console

   $ cd ~/tidl/audioai-modelzoo
   $ ./jupyter_lab_venv.sh

The launcher prints a highlighted access URL. Open the URL in a browser on a
machine that can reach the target and enter the token ``tidl`` when prompted:

.. code-block:: text

   Access URL: http://<target-ip>:8888/lab?token=tidl

Jupyter Lab opens with the GCRN-mod-g16 notebook loaded. To run a different model, pick
its notebook from the file browser in the left sidebar. The notebooks are:

.. list-table::
   :header-rows: 1
   :widths: 22 40

   * - Model
     - Notebook
   * - GCRN-mod-g16
     - ``inference/gcrn_se/gcrn_inference.ipynb``
   * - VGGish11
     - ``inference/vggish11_sc/vggish_inference.ipynb``
   * - GTCRN
     - ``inference/gtcrn_se/gtcrn_inference.ipynb``
   * - YAMNet
     - ``inference/yamnet_sc/yamnet_inference.ipynb``

******************
Compiled artifacts
******************

:file:`download_models.sh` places the artifacts under
:file:`model_artifacts/<TIDL_VER>/am62d/`. Each model gets its own directory,
named after its model ID, containing a ``model/`` folder (the trained ONNX
model) and, where applicable, an ``artifacts/`` folder (the compiled model
artifacts). VGGish11, YAMNet, and GCRN-mod-g16 each get a pre-compiled TVM-RT + TIDL
artifact:

- ``ac-0101`` - ``ac-0101_tvmrt_audio_classification_urbansound8k_vggish11_onnx`` (VGGish11)
- ``ac-0201`` - ``ac-0201_tvmrt_audio_classification_urbansound8k_yamnet_onnx`` (YAMNet)
- ``ase-0212`` - ``ase-0212_tvmrt_speech_enhancement_voicebank_demand_16k_gcrn_mod_g16_fixed_4sec_onnx`` (GCRN-mod-g16)

GTCRN runs through ONNX Runtime, so its directory holds only the ONNX model
(:file:`model/gtcrn_dns3.onnx`) and no compiled artifacts:

- ``ase-0100`` - ``ase-0100_onnxrt_speech_enhancement_voicebank_demand_16k_gtcrn_dns3_onnx`` (GTCRN)

Each of those artifact directories' :file:`artifacts/` folder holds the TVM-RT
deployment artifacts (:file:`deploy_lib.so`, :file:`deploy_graph.json`, :file:`deploy_param.params`)
in both target (``.evm``, aarch64) and host (``.pc``, x86) variants. The demo
scripts and notebooks select the ``.evm`` variant automatically on the target.
