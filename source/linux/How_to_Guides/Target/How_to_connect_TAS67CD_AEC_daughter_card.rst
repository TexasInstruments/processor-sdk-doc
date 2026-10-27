.. _tas67cd-aec-daughter-card:

***********************************
TAS67CD-AEC daughter card setup
***********************************

AM62D-EVM includes 2 Audio Expansion Connectors (AEC1 and AEC2), which you can
use to connect to an audio daughter card such as TAS67CD-AEC.

TAS67CD-AEC is a daughter card that carries two **TAS67524** 50W quad-channel
Class-D amplifiers, referred to as TAS0 and TAS1. Together, they expose 8
channels of audio playback or 8 channels of active noise cancellation (ANC)
low-latency playback. They also provide optional sensing capture, with 8
channels of Vpredict and 8 channels of Isense across the two amplifiers.

Hardware connections
====================

To set up the hardware, connect the TAS67CD-AEC daughter card to the AEC1
connector of the AM62D-EVM. Then connect the external PVDD supply through banana
plugs to the PVDD and GND terminals on the lower left of the daughter card, as
shown in the following figure:

.. figure:: /images/AM62D_TAS67CD_AEC_setup.jpg
   :align: center
   :width: 80%

   TAS67CD-AEC daughter card connected to the AEC1 header of the AM62D-EVM

Set the S1 RESET switch to PORZ instead of STATZ. All three LEDs on the lower
left corner of the daughter card must be lit for the card to operate properly.
The LEDs indicate the following:

* **IOVDD**: 1.8V power rail that the AM62D-EVM supplies to the daughter card.
  This LED lights when you power on the AM62D-EVM and connect it to the daughter
  card.
* **PVDD**: The external power supply through the banana plugs. This LED lights
  when you connect the external supply and it is within the operating range of
  the daughter card (4.25V to 18.5V).
* **PORZ**: Power-on-reset signal. This LED lights when the ASoC codec driver
  brings the amplifiers out of reset as part of its initialization sequence.

The overlay defines the ``GPIO1`` pin of each amplifier as a mute input
(``ti,gpio1-function = "mute"``). Switch SW4 on the daughter card controls the
TAS0 mute, and switch SW2 controls the TAS1 mute. Set the switch to HIGH to
unmute and LOW to mute. You can also adjust the overlay to use any other
supported ``gpio1-function``.

.. figure:: /images/AM62D_TAS67CD_AEC_mute_switches.png
   :align: center
   :width: 40%

   Status LEDs and GPIO1 (mute) switches of TAS0 and TAS1 on the daughter card. HIGH to unmute.

Overlay enablement
==================

The SDK includes the overlay :file:`k3-am62d-evm-tas67cd-aec.dtbo` to enable
the daughter card on the AM62D-EVM.

#. Follow the :ref:`How to enable DT overlays in Linux <howto_dt_overlays>`
   guide for steps on building and adding the overlay in your SD card.

   (You can skip this step if the overlay is already present in
   :file:`/boot/dtb/ti` under the root partition of your SD card)

#. Enable the overlay by updating the ``name_overlays`` variable in the
   :file:`uEnv.txt` file under the BOOT partition on your SD card.

   .. code-block:: text

      name_overlays=ti/k3-am62d-evm-tas67cd-aec.dtbo

#. Reboot the board. The ASoC driver registers the card as ``TAS67CD-AEC``, which
   you can check with :command:`aplay` and :command:`arecord`:

   .. code-block:: console

      root@am62dxx-evm:~# aplay -l
      root@am62dxx-evm:~# arecord -l

.. note::

    This overlay uses the AEC1 connector, as AEC2 shares the same McASP2 pins
    with the onboard TAD5212 DACs and PCM6240 ADCs. An AEC2 overlay is not
    provided, but you can create one by modifying the AEC1 overlay to use McASP2
    instead and disabling the onboard TAD5212 and PCM6240 nodes.

Overlay configuration
=====================

The overlay uses the following AM62D-EVM resources:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Resource
     - Configuration
   * - Audio interface
     - McASP1 on AEC1, ``dsp_b`` format, 16 time-division multiplexing (TDM) slots, McASP is bit clock and frame provider
   * - Clock
     - McASP routes from CDCE6214 output 1 (``&cdce6214 3``)
   * - Control
     - I2C2: TAS0 at ``0x70``, TAS1 at ``0x71``
   * - Playback data
     - AXR0 (shared by TAS0 and TAS1)
   * - Capture data
     - AXR2 (TAS0 sense data), AXR3 (TAS1 sense data)
   * - Standby GPIOs
     - TAS0: GPIO0_33, TAS1: GPIO0_34
   * - Supplies
     - DVDD from the EVM PMIC ``buck3`` (1.8 V). PVDD comes from an external supply, which also feeds VBAT

Each amplifier exposes three digital audio interfaces (DAIs): audio playback,
ANC low-latency playback, and a feedback capture DAI that returns real-time
voltage (Vpredict) and current (Isense) sense data. The playback and capture
streams share the same SCLK and FSYNC pair in the TAS67524, so both use the same
16-slot TDM layout. Capture uses only 8 of the 16 slots. The following table
summarizes the slot assignment:

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Slots
     - Playback
     - Capture
   * - 0-3
     - TAS0 audio (AXR0)
     - Vpredict (AXR2: TAS0, AXR3: TAS1)
   * - 4-7
     - TAS1 audio (AXR0)
     - Isense (AXR2: TAS0, AXR3: TAS1)
   * - 8-11
     - TAS0 ANC low-latency (AXR0)
     - Not used
   * - 12-15
     - TAS1 ANC low-latency (AXR0)
     - Not used

For the purpose of evaluation, the overlay routes both normal playback and ANC
low-latency playback to different TDM slots on the same AXR0 pin. To use ANC
low-latency playback, enable the low-latency playback (LLP) mode and the
``ANC Path`` switch with :command:`amixer`.

Audio card topology
-------------------

The card is an ``audio-graph-card2`` DPCM sound card. One front-end playback
stream on McASP1 fans out to the audio and ANC back-end DAIs of both
amplifiers, and the feedback back-end DAIs of both amplifiers fan in to one
front-end capture stream. The overlay source and a description of each node are
in the DPCM example under :ref:`DPCM topology <mcasp-dpcm-topology>`.

Playing audio on the TAS67CD-AEC daughter card
==============================================

Make sure that you set the mute switches of TAS0 and TAS1 to HIGH. The
``TAS67CD-AEC`` card exposes two PCM devices, both on McASP1. The kernel numbers
the PCM devices in the order of the front-ends (FE) in the ``links`` property of
the sound card node. FE0 handles playback, so ``hw:<card>,0`` is the playback
device. FE1 handles capture, so ``hw:<card>,1`` is the capture device. The audio,
ANC and feedback DAIs of the amplifiers are internal back-ends.
:command:`aplay -l` and :command:`arecord -l` do not list them.

#. Play back a .WAV or raw PCM file on the TAS67CD-AEC playback device by using
   :command:`aplay`:

   .. code-block:: console

      root@am62dxx-evm:~# aplay -D hw:<card>,0 <path_to_wav_file>

   Replace ``<card>`` with the card number or ID that :command:`aplay -l`
   shows for the ``TAS67CD-AEC`` card.

   You can also check out the :ref:`Audio Linux Driver Guide <Audio_User_Guide>`
   for more information about using :command:`aplay`.

#. To record the voltage and current feedback data from both amplifiers, use
   :command:`arecord` on the TAS67CD-AEC capture device:

   .. code-block:: console

      root@am62dxx-evm:~# arecord -D hw:<card>,1 -c <channels> -r 48000 -f <format> feedback.wav

   The capture sampling rate must match the ongoing playback rate. Vpredict is
   only available at 48 kHz.
