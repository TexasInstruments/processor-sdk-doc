.. _edgeai_model_inspector:

###############
Model Inspector
###############

Model Inspector turns a compiled model into a single interactive report that you
open in a web browser. It shows the parts of your model that run on the C7x Neural
Processing Unit (NPU), how much accuracy the compiled model keeps, and where its
time and memory go. It runs on the
x86 PC, uses the same edgeai-tidlrunner installation described in
:ref:`Setup <edgeai-am62d-setup>`, and is created by the same commands you use to
:ref:`compile and evaluate <edgeai_compile_evaluate>` a model.

********
Overview
********

About Model Inspector
=====================

After a model is compiled, three questions usually come up:

- **What runs on the C7x NPU, and what falls back to the Arm core?**
- **How much accuracy is lost to quantization?**
- **Where do the time and memory go?**

Model Inspector answers all three in one **self-contained HTML report**. Nothing
extra needs to be installed and no server is needed: copy :file:`modelinspector.html` to
any computer and open it in Google Chrome, Mozilla Firefox, or Microsoft Edge. A :file:`modelinspector.json`
data file with the same information is saved next to it.

.. _edgeai_model_inspector_generate:

When the report is created and updated
======================================

You do not need a separate step to get a report. The commands you already use
create it and keep it up to date, and it becomes more detailed as you run more
commands on the same model:

.. list-table::
   :header-rows: 1
   :widths: 18 82

   * - Command
     - What happens to the report
   * - ``compile``
     - **Creates** the report. It shows the model structure, the layers that
       the NPU accelerates, the layers that fall back to the Arm core, and the compiler's
       *estimated* time, cycles and memory for each layer.
   * - ``infer``
     - **Refreshes** the report. If the run captures performance data (see
       `Measured performance`_), those numbers replace the estimates for the
       layers they cover.
   * - ``evaluate``
     - **Refreshes** the report. When run on the |__PART_FAMILY_NAME__| evaluation module (EVM), the measured accuracy
       is added as well.
   * - ``inspect``
     - **Creates the complete report**, including the layer-by-layer
       quantization analysis. See `What the inspect command does`_.

Report generation never interrupts your work. If something the report needs is
not available, the command prints an ``INFO`` message, skips the report, and
finishes normally.

Two things are worth knowing:

- Running ``compile`` again starts a **fresh** report, because ``compile`` clears
  the model's existing work folder. Run ``infer`` or ``evaluate`` again afterward
  if you want measured data back in the report.
- Running ``infer`` or ``evaluate`` never discards what ``compile`` produced. It
  only adds to it.

.. _edgeai_model_inspector_inspect:

What the inspect command does
=============================

``compile`` shows how the compiler *sees* your model. ``inspect`` goes further and
shows how well the compiled model actually *behaves*, by comparing it against a
full precision reference. Run it when you want to see where quantization
costs accuracy:

.. code-block:: console

   $ tidlrunner-cli inspect --config_path $CFG

``inspect`` is a one-command pipeline. In order, it:

1. **Compiles and runs the model for the C7x NPU** at its normal precision (for
   example 8-bit). This is the model you would deploy.
2. **Compiles and runs a reference copy on the Arm core only**, in full
   floating point precision. Its results are the "ground truth".
3. **Compiles and runs a 32-bit version on the C7x NPU.** This helps separate the
   error caused by quantization from other differences between the NPU and the
   Arm core.
4. **Compares the results layer by layer** between the deployed model, the 32-bit
   version and the reference. For every layer it measures:

   - **Signal-to-noise ratio (SNR), in dB** - a larger value means the NPU result is
     closer to the reference. A sharp drop at one layer points to where accuracy
     is being lost.
   - **Mean, median and maximum difference** - the average, typical and
     worst-case gap from the reference.

5. **Builds the report**, including the activation histograms and scatter plots
   used in the *Subgraphs* and *Analysis* tabs.

The comparison numbers are also saved as :file:`analyze.xlsx` in the model's work
folder, in case you want to open them in a spreadsheet.

You do not need to run ``compile`` or ``infer`` first; ``inspect`` performs every
step itself.

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * - Option
     - Effect
   * - ``--num_frames``
     - Number of input samples to run. The default is ``1``. The layer-by-layer
       view in the report is drawn from the first sample.
   * - ``--act_data=false``
     - Omit the activation histograms and scatter plots. The report is
       faster to generate and much smaller, but the quantization-analysis views
       are empty. Use this when you only need performance information.
   * - ``--debug_level``
     - ``inspect`` uses ``4`` by default, which enables the layer-by-layer
       comparison. Below ``4``, only the final model outputs are compared.

.. _edgeai_model_inspector_measured:

Measured performance
====================

A model compiled with TVM-RT can contain two kinds of layers that run on the
C7x NPU, and the *Performance* tab gets its numbers for each kind at a different
time. In the *Subgraphs* tab you can tell them apart by name: ``tidl_<N>`` entries
are **TIDL-accelerated** layers and ``tvmgen_...`` entries are **TVM-accelerated**
layers. Layers that stay on the Arm core have no performance data.

.. list-table::
   :header-rows: 1
   :widths: 22 39 39

   * - Layer type
     - After ``compile``
     - After ``infer --debug_level 2``
   * - **TIDL-accelerated**
     - Time, cycles (total, data transfer, compute) and memory (MSMC, DDR),
       all estimated by the compiler.
     - Compiler estimates are kept for the models in this guide.
   * - **TVM-accelerated**
     - No performance data.
     - Cycle count per layer. On the PC these come from host emulation; on the
       EVM they are measured on the hardware.

After ``compile`` alone, TIDL-accelerated layers already show their time,
cycles and memory, while TVM-accelerated layers stay blank. To add data for the
TVM layers, run ``infer`` with ``--debug_level 2`` (or ``3``) on the model you already
compiled:

.. code-block:: console

   $ tidlrunner-cli infer --config_path $CFG --debug_level 2

On the |__PART_FAMILY_NAME__| EVM, use the same ``--debug_level 2`` setting with the target device
selected. The report additionally gets the whole-model inference time measured on
the real hardware:

.. code-block:: console

   $ tidlrunner-cli infer --config_path $CFG --target_device AM62D --debug_level 2

Running ``evaluate`` on the EVM also records the measured accuracy.

Open :file:`modelinspector.html` again afterward and the *Performance* tab shows the
new values. A layer with no measurement is left blank rather than shown as zero,
and sections with no data are hidden.

Output location
===============

The report is saved next to the compiled model:

.. code-block:: text

   work_dirs/compile/<target_device>/<bits>/<model_id>/inspect/modelinspector.html
   work_dirs/compile/<target_device>/<bits>/<model_id>/inspect/modelinspector.json

:file:`<bits>` is the tensor precision the model was compiled with, such as :file:`8bits`
or :file:`16bits`. :file:`modelinspector.html` is the only file you need to share.

***********
Report tabs
***********

The report has four tabs.

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Tab
     - What it shows
   * - **Model Summary**
     - How much of the model runs on the C7x NPU versus the Arm core, the input
       and output specifications, and an interactive graph of the whole model.
       Click any layer to see its type, shapes, and whether it is accelerated -
       and, if it is not, why.
   * - **Subgraphs**
     - Each group of layers offloaded to the C7x NPU, with the details of every
       layer. Layers that have a reference comparison also show the quantization
       analysis: activation histograms and scatter plots of the 8-bit result
       against the floating point reference.
   * - **Performance**
     - Processing time per layer, the NPU cycle breakdown (total, data transfer
       and compute), memory use per layer (DDR and MSMC, in KB), and the SNR and
       difference metrics.
   * - **Analysis**
     - All layers from all subgraphs in one sortable, searchable table, with the
       SNR, histogram and scatter plot of each layer side by side. Sort by SNR to
       find the layers where accuracy drops most.

.. note::

   Values for TIDL-accelerated layers are **compiler estimates**, and TVM-accelerated
   layers show nothing until you run ``infer`` with ``--debug_level 2`` or ``3``, as
   described in `Measured performance`_. Model Inspector requires TIDL tools
   **11.02 or later**.

GCRN showcase - an offloaded NPU subgraph
=========================================

GCRN compiles with ``tidl_offload: true`` on |__PART_FAMILY_NAME__|. Its report shows a **real
C7x NPU subgraph** rather than an all-Arm model. The *Subgraphs* tab lists one
offloaded subgraph (16-bit) with its layer mapping. The *Performance* tab
breaks that subgraph down by cycles and memory. Generate it with the
|__PART_FAMILY_NAME__| environment sourced (see :ref:`Setup <edgeai-am62d-setup>`):

.. code-block:: console

   $ CFG=data/configs/samples/models/audio/speech_enhancement/voicebank_demand_16k/gcrn_fixed_4sec_tvmrt_config.yaml
   $ tidlrunner-cli inspect --config_path $CFG

For contrast, running ``inspect`` on the GTCRN (ONNX-RT) config produces a report
with **no** NPU subgraph. Every layer runs on the Arm core, as a non-offloaded
model does in the inspector. GTCRN is compiled with
``tidl_offload: false``, so its work folder uses a :file:`notidl` segment in place of
the :file:`<bits>` shown above, for example
:file:`work_dirs/compile/AM62D/notidl/<model_id>/...`.

Learn more
==========

This page is a short overview. For a walk through every tab of the report with
screenshots, see the `Model Inspector README
<https://github.com/TexasInstruments/edgeai-tidlrunner/blob/main/tidlrunner/edgeai_tidlrunner/modelinspector/README.md>`__
on GitHub.

For every ``inspect`` command-line option, see
`options.md <https://github.com/TexasInstruments/edgeai-tidlrunner/blob/main/tidlrunner/docs/options.md>`__
in the `edgeai-tidlrunner repository
<https://github.com/TexasInstruments/edgeai-tidlrunner>`__.

.. _edgeai_model_inspector_disable:

Turning the report off
======================

To skip the report for a run, add ``--no_inspector`` to any command
(``compile``, ``infer``, ``evaluate`` or ``inspect``):

.. code-block:: console

   $ tidlrunner-cli compile --config_path $CFG --no_inspector

No report is created or updated during that run. A report that already exists is
left exactly as it is.
