.. _Audio_User_Guide:

Audio
---------------------------------

Introduction
^^^^^^^^^^^^

The audio subsystem present on various TI SoCs consists of two major components:

#. **Multi-channel Audio Serial Port (McASP)** - Provides a full-duplex
   serial interface between the host processor and external audio peripherals
   like codecs over industry-standard protocols like Inter-IC sound (I2S).

#. **System DMA engine** - Provides McASP with direct access to system
   memory to read audio samples from (for playback) or store audio samples to
   (for capture).

Along with the above, most TI EVMs and SKs have line input/output jack(s) wired
to an on-board codec that can convert between the analog signals and the
digital protocol supported by McASP.

Software Architecture
^^^^^^^^^^^^^^^^^^^^^

All the hardware components are exposed to userspace applications using the
Linux ALSA (Advance Linux Sound Architecture) framework, which allows control
and configuration of the hardware through common APIs. For more details check
the `links below <#additional-information>`__.

Within the kernel there are separate drivers for each component. For each
board a sound-card instance is created, usually using the :code:`sound {}`
device tree node, that links together various components like different McASP
instances to a codec or an HDMI bridge.

.. Image:: /images/audio-asoc-arch.png

Generic commands and instructions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. ifconfig:: CONFIG_part_variant in ('AM62DX')

    .. note::

        Only Audio playback with static DAC confgiuration is supported.
        Recording feature is not supported.

Most of the boards have simple audio setup which means we have one
sound card with one playback and one capture PCM.
To list the available sound cards and PCMs for playback:

.. code-block:: text

    aplay -l

To list the available sound cards and PCMs for capture:

.. code-block:: text

    arecord -l

In most cases ``-Dplughw:0,0`` is the device we want to use for audio
but in case we have several audio devices (onboard + USB for example)
one need to specify which device to use for audio:

.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family')

    ``-Dplughw:omap5uevm,0`` will use the onboard audio on OMAP5-uEVM
    board.

.. ifconfig:: CONFIG_part_variant in ('J721E')

    ``-Dplughw:j721ecpb,0`` will use the onboard audio on J721E-EVM
    board.

.. ifconfig:: CONFIG_part_variant in ('J784S4','J742S2')

    ``-Dplughw:j784s4cpb,0`` will use the onboard audio on J721E-EVM
    board.

To play audio on card0's PCM0 and let ALSA to decide if resampling is
needed:

.. code-block:: text

    aplay -Dplughw:0,0 <path to wav file>

To record audio to a file:

.. code-block:: text

    arecord -Dplughw:0,0 -t wav <path to wav file>

To test full duplex audio (play back the recorded audio w/o intermediate
file):

.. code-block:: text

    arecord -Dplughw:0,0 | aplay -Dplughw:0,0

To request specific audio format to be used for playback/capture take a look
at the help of aplay/arecord.   For example, one can specify the format with ``-f``,
the sampling rate with ``-r``, or the number of channels with ``-c``.
In this case, one should open the hw device (not the plughw) via ``-Dhw:0,0``.
For example, record 48KHz, stereo 16bit audio:

.. code-block:: text

    arecord -Dhw:0,0 -fdat -t wav record_48K_stereo_16bit.wav

Or to record record 96KHz, stereo 24bit audio:

.. code-block:: text

    arecord -Dhw:0,0 -fS24_LE -c2 -r96000 -t wav record_96K_stereo_24bit.wav

It is a good practice to save the mixer settings found to be good and
reload them after every boot (if your distribution is not doing this
already)

.. code-block:: text

    Set the mixers for the board with amixer, alsamixer
    alsactl -f board.aconf store

After booting up the board it can be restored with a single command:

.. code-block:: text

    alsactl -f board.aconf restore

Board-specific instructions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. ifconfig:: CONFIG_part_family in ('AM335X_family')

    .. rubric:: AM335x EVM
       :name: am335x-evm-audio

    | The board uses **tlv320aic3106 codec** connected through **McASP1
      [AXR2 for playback, AXR3 for Capture]** for audio. The board features
      two 3.5mm jack for **Headphone** and **Line In**

    .. rubric:: Kernel config
       :name: kernel-config-2

    .. code-block:: text

        Device Drivers  --->
          Sound card support  --->
            Advanced Linux Sound Architecture  --->
              ALSA for SoC audio support  --->
                Audio support for Texas Instruments SoCs  --->
                  <*> Multichannel Audio Serial Port (McASP) support
                CODEC drivers  --->
                  <*> Texas Instruments TLV320AIC3x CODECs
                <*>   ASoC Simple sound card support

    .. rubric:: User space
       :name: user-space-2

    The hardware defaults are correct for audio playback, the routing is OK
    and the volume is 'adequate' but in case the volume is not correct:

    .. code-block:: text

        amixer -c AM335xEVM sset PCM 90                            # Master Playback volume

    For audio capture trough stereo microphones:

    .. code-block:: text

        amixer sset 'Right PGA Mixer Line1R' on
        amixer sset 'Right PGA Mixer Line1L' on
        amixer sset 'Left PGA Mixer Line1R' on
        amixer sset 'Left PGA Mixer Line1L' on

    In addition to previois commands for line in capture run also these:

    .. code-block:: text

        amixer sset 'Left Line1L Mux' differential
        amixer sset 'Right Line1R Mux' differential

.. ifconfig:: CONFIG_part_family in ('AM335X_family')

    .. rubric:: AM335x EVM-SK
       :name: am335x-evm-sk

    | The board uses **tlv320aic3106 codec** connected through **McASP1
      [AXR2 for playback]** for audio and only playback is supported on the
      board via the lone 3.5mm jack.
    | ``NOTE: The Headphone jack wires are swapped. This means that the channels will be swapped on the output (Left channel -> Right HP, Right channel -> Left HP)``

    .. rubric:: Kernel config
       :name: kernel-config-3

    .. code-block:: text

        Device Drivers  --->
          Sound card support  --->
            Advanced Linux Sound Architecture  --->
              ALSA for SoC audio support  --->
                Audio support for Texas Instruments SoCs  --->
                  <*> Multichannel Audio Serial Port (McASP) support
                CODEC drivers  --->
                  <*> Texas Instruments TLV320AIC3x CODECs
                <*>   ASoC Simple sound card support

    .. rubric:: User space
       :name: user-space-3

    The hardware defaults are correct for audio playback, the routing is OK
    and the volume is 'adequate' but in case the volume is not correct:

    .. code-block:: text

        amixer -c AM335xEVMSK sset PCM 90                            # Master Playback volume

.. ifconfig:: CONFIG_part_family in ('AM437X_family')

    .. rubric:: AM43x-EPOS-EVM
       :name: am43x-epos-evm

    | The board uses **tlv320aic3111 codec** connected through **McASP1
      [AXR0 for playback, AXR1 for Capture]** for audio. The board features
      internal stereo speakers and two 3.5mm jack for **Headphone** and
      **Mic In**

    .. rubric:: Kernel config
       :name: kernel-config-4

    .. code-block:: text

        Device Drivers  --->
          Sound card support  --->
            Advanced Linux Sound Architecture  --->
              ALSA for SoC audio support  --->
                Audio support for Texas Instruments SoCs  --->
                  <*> Multichannel Audio Serial Port (McASP) support
                CODEC drivers  --->
                  <*> Texas Instruments TLV320AIC31xx CODECs
                <*>   ASoC Simple sound card support

    .. rubric:: User space
       :name: user-space-4

    .. note::

     Before audio playback ALSA mixers must be configured for either Headphone or Speaker output. The audio will not work with non correct mixer configuration!

    To play audio through headphone jack run:

    .. code-block:: text

        amixer sset 'DAC' 127
        amixer sset 'HP Analog' 66
        amixer sset 'HP Driver' 0 on
        amixer sset 'HP Left' on
        amixer sset 'HP Right' on
        amixer sset 'Output Left From Left DAC' on
        amixer sset 'Output Right From Right DAC' on

    To play audio through internal speakers run:

    .. code-block:: text

        amixer sset 'DAC' 127
        amixer sset 'Speaker Analog' 127
        amixer sset 'Speaker Driver' 0 on
        amixer sset 'Speaker Left' on
        amixer sset 'Speaker Right' on
        amixer sset 'Output Left From Left DAC' on
        amixer sset 'Output Right From Right DAC' on

    To capture audio from both microphone channels run:

    .. code-block:: text

        amixer sset 'MIC1RP P-Terminal' 'FFR 10 Ohm'
        amixer sset 'MIC1LP P-Terminal' 'FFR 10 Ohm'
        amixer sset 'ADC' 40
        amixer cset name='ADC Capture Switch' on

    If the captured audio has low volume you can try higer values for 'Mic
    PGA' mixer, for instance:

    .. code-block:: text

        amixer sset 'Mic PGA' 50

    Note: The codec on has only one channel ADC so the captured audio is
    dual channel mono signal.

.. ifconfig:: CONFIG_part_family in ('AM437X_family')

    .. rubric:: AM437x-GP-EVM
       :name: am437x-gp-evm

    | The board uses **tlv320aic3106 codec** connected through **McASP1
      [AXR2 for playback, AXR3 for Capture]** for audio. The board features
      two 3.5mm jack for **Headphone** and **Line In**.

    .. rubric:: Kernel config
       :name: kernel-config-5

    .. code-block:: text

        Device Drivers  --->
          Sound card support  --->
            Advanced Linux Sound Architecture  --->
              ALSA for SoC audio support  --->
                Audio support for Texas Instruments SoCs  --->
                  <*> Multichannel Audio Serial Port (McASP) support
                CODEC drivers  --->
                  <*> Texas Instruments TLV320AIC3x CODECs
                <*>   ASoC Simple sound card support

    .. rubric:: User space
       :name: user-space-5

    The hardware defaults are correct for audio playback, the routing is OK
    and the volume is 'adequate' but in case the volume is not correct:

    .. code-block:: text

        amixer -c AM437xGPEVM sset PCM 90                            # Master Playback volume

    Playback to Headphone only:

    .. code-block:: text

        amixer -c AM437xGPEVM sset 'Left HP Mixer DACL1' on               # HP Left route enable
        amixer -c AM437xGPEVM sset 'Right HP Mixer DACR1' on              # HP Right route enable
        amixer -c AM437xGPEVM sset 'Left Line Mixer DACL1' off            # Line out Left disable
        amixer -c AM437xGPEVM sset 'Right Line Mixer DACR1' off           # Line out Right disable
        amixer -c AM437xGPEVM sset 'HP DAC' 90                            # Adjust HP volume

    Record from Line In:

    .. code-block:: text

        amixer -c AM437xGPEVM sset 'Left PGA Mixer Line1L' on             # Line in Left enable
        amixer -c AM437xGPEVM sset 'Right PGA Mixer Line1R' on            # Line in Right enable
        amixer -c AM437xGPEVM sset 'Left PGA Mixer Mic3L' off             # Analog mic Left disable
        amixer -c AM437xGPEVM sset 'Right PGA Mixer Mic3R' off            # Analog mic Right disable
        amixer -c AM437xGPEVM sset 'PGA' 40                               # Adjust Capture volume

.. ifconfig:: CONFIG_part_variant in ('J721E')

    .. rubric:: J721e Common Processor Board
       :name: j721e-cpb

    | The board uses **pcm3168a codec** connected through **McASP10 [AXR0-3 for playback, AXR4-6 for capture]**.
      The codec receives its SCKI clock from the AUDIO_EXT_REFCLK2 pin output of the j721e.
    | PLL4 is configured to 1179648000 Hz for the 48KHz sampling rate family.
    | PLL15 is configured to 1083801600 Hz for the 44.1KHz sampling rate family.
    | The board has seven stereo jacks, including four jacks for playback and three jacks for capture.
    |

    The audio channel mapping to jacks depends on the number of channels (slots) in the audio stream:

    .. code-block:: text

               |o|c1  |o|p1  |o|p3
         _     | |    | |    | |
        |o|c3  |o|c2  |o|p4  |o|p2
        --------------------------

        c1/2/3 - capture jacks (3rd is line input)
        p1/2/3/4 - playback jacks (4th is line output)

        2 channel audio (stereo):
        -------------------------
        0 (left):  p1/c1 left
        1 (right): p1/c1 right

        4 channel audio:
        ----------------
        0: p1/c1 left
        1: p2/c2 left
        2: p1/c1 right
        3: p2/c2 right

        6 channel audio:
        ----------------
        0: p1/c1 left
        1: p2/c2 left
        2: p3/c3 left
        3: p1/c1 right
        4: p2/c2 right
        5: p3/c3 right

        8 channel audio:
        ----------------
        0: p1/c1 left
        1: p2/c2 left
        2: p3/c3 left
        3: p4 left
        4: p1/c1 right
        5: p2/c2 right
        6: p3/c3 right
        7: p4 right

    For example, if the playback is opened in **8-channel** mode and **stereo** audio is
    desired on the **line output (p4)**,  then the **left channel** of the 8-channel stream should
    be placed to **time slot 3**, and the **right channel** of the 8-channel stream should be placed in **time slot 7**.

    .. rubric:: Kernel config
       :name: kernel-config-8

    .. code-block:: text

        Device Drivers  --->
          Sound card support  --->
            Advanced Linux Sound Architecture  --->
              ALSA for SoC audio support  --->
                Audio support for Texas Instruments SoCs  --->
                  <*> SoC Audio support for j721e EVM

    .. rubric:: User space
       :name: user-space-8-kernel-audio

    ``NOTE: Playback volume is HIGH after boot. Do not use headset without lowering it!!!``

    .. code-block:: text

        amixer -c j721ecpb sset 'codec1 DAC1' 141  # Playback volume for p1 jack
        amixer -c j721ecpb sset 'codec1 DAC2' 141  # Playback volume for p2 jack
        amixer -c j721ecpb sset 'codec1 DAC3' 141  # Playback volume for p3 jack
        amixer -c j721ecpb sset 'codec1 DAC4' 141  # Playback volume for p4 jack

    Master volume control is disabled by default. It can be enabled by:

    .. code-block:: text

        amixer -c j721ecpb sset 'codec1 DAC Volume Control Type' 'Master + Individual'

    Then, a master gain control can be applied to all outputs:

    .. code-block:: text

        amixer -c j721ecpb sset 'codec1 Master' 141  # Master Playback volume for p1/2/3/4 jack

.. ifconfig:: CONFIG_part_variant in ('J784S4','J742S2')

    .. rubric:: J784S4 Evaluation Board
       :name: j784s4-evm

    | The board uses **pcm3168a codec** connected through **McASP0 [AXR3 for playback, AXR4 for capture]**.
      The codec receives its SCKI clock from the AUDIO_EXT_REFCLK1 pin output of the j784s4.
    | PLL4 is configured to 1179648000 Hz for the 48KHz sampling rate family.
    | The board has two stereo jacks, one for playback and one for capture.
    |

    .. code-block:: text

        |o|c1
        | |
        |o|p1
        --------------------------

        c1 - capture jack
        p1 - playback jack

    .. rubric:: Kernel config

    .. code-block:: text

        Device Drivers  --->
          Sound card support  --->
            Advanced Linux Sound Architecture  --->
              ALSA for SoC audio support  --->
                Audio support for Texas Instruments SoCs  --->
                  <*> SoC Audio support for j721e EVM

    .. rubric:: ~/.asoundrc file needed for audio playback
       :name: asoundrc-file-1

    .. code-block:: text

        pcm_slave.j784s4-evm {
          pcm "hw:0,0"
          format S16_LE
          channels 2
          rate 48000
        }

        pcm.j784s4-playback {
          type plug
          slave j784s4-evm
        }

    .. rubric:: User space

    ``NOTE: Playback volume is HIGH after boot. Do not use headset without lowering it!!!``

    Master volume control is disabled by default. It can be enabled by:

    .. code-block:: text

        amixer -c j784s4cpb sset 'codec1 DAC Volume Control Type' 'Master + Individual'

    Then, a master gain control can be applied to all outputs:

    .. code-block:: text

        amixer -c j784s4cpb sset 'codec1 Master' 141  # Master Playback volume for p1 jack

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX', 'AM62PX', 'J722S')

    .. rubric:: SK-AM62x, SK-AM62Ax, SK-AM62Px, J722S-EVM
       :name: sk-am62x

    | The board uses **tlv320aic3106 codec** connected through **McASP1
      [AXR0 for playback, AXR2 for Capture]** for audio. The board features
      one TRRS 3.5mm jack, that can be used for simultaneous stereo playback
      and mono recording. Same McASP1 lines are also muxed to the **sii9022
      HDMI bridge**.

    .. rubric:: Kernel config
       :name: kernel-config-9

    .. code-block:: text

        Device Drivers  --->
          Sound card support  --->
            Advanced Linux Sound Architecture  --->
              ALSA for SoC audio support  --->
                Audio support for Texas Instruments SoCs  --->
                  <*> Multichannel Audio Serial Port (McASP) support
                CODEC drivers  --->
                  <*> Texas Instruments TLV320AIC3x CODECs
                <*>   ASoC Simple sound card support

    .. rubric:: User space
       :name: user-space-9

    The hardware defaults are correct for audio playback, the routing is OK
    and the volume is 'adequate' but in case the volume is not correct:

    .. code-block:: text

        amixer sset PCM 90%

    For recording using the mic pin on the 3.5mm jack, you will need to unmute
    MIC3R on the codec, and increase the capture volume:

    .. code-block:: text

        amixer sset 'Left PGA Mixer Mic3R' on
        amixer sset 'Right PGA Mixer Mic3R' on
        amixer sset PGA 90%

    To switch to using HDMI for playback you can refer to: :ref:`hdmi-audio`.

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

    .. rubric:: SK-AM62L
       :name: sk-am62l

    | The board uses **tlv320aic3106 codec** connected through **McASP0
      [AXR0 for playback, AXR1 for Capture]** for audio. The board features
      one TRRS 3.5mm jack, that can be used for simultaneous stereo playback
      and mono recording. Same McASP0 lines are also muxed to the **sii9022
      HDMI bridge**.

    .. rubric:: Kernel config

    .. code-block:: text

        Device Drivers  --->
          Sound card support  --->
            Advanced Linux Sound Architecture  --->
              ALSA for SoC audio support  --->
                Audio support for Texas Instruments SoCs  --->
                  <*> Multichannel Audio Serial Port (McASP) support
                CODEC drivers  --->
                  <*> Texas Instruments TLV320AIC3x CODECs
                <*>   ASoC Simple sound card support

    .. rubric:: User space

.. _hdmi_audio:
    The hardware defaults are correct for audio playback, the routing is OK
    and the volume is 'adequate' but in case the volume is not correct:

    .. code-block:: text

        amixer sset PCM 90%

    For recording using the mic pin on the 3.5mm jack, you will need to unmute
    MIC3R on the codec, and increase the capture volume:

    .. code-block:: text

        amixer sset 'Left PGA Mixer Mic3R' on
        amixer sset 'Right PGA Mixer Mic3R' on
        amixer sset PGA 90%

    To switch to using HDMI for playback you can refer to: :ref:`hdmi-audio`.

Potential issues
^^^^^^^^^^^^^^^^

.. rubric:: In case of XRUN (under or overrun)
   :name: in-case-of-xrun-under-or-overrun

| The underrun can happen when an application does not feed new samples
  in time to alsa-lib (due CPU usage). The overrun can happen when an
  application does not take new captured samples in time from alsa-lib.
| There could be several reasons for XRUN to happen, but it usually
  points to system latency issues connected to CPU utilization or
  latency caused by the storage device.
| Things to try:

-  Increase the buffer size (ALSA buffer and period size)
-  Try to cache the file to be played in memory
-  Try to use application which uses threads for interacting with ALSA
   and with the filesystem

Additional Information
^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: ALSA links
   :name: additional-information-alsa-links

#. `ALSA SoC Project
   Homepage <http://www.alsa-project.org/main/index.php/ASoC>`__
#. `ALSA Project
   Homepage <http://www.alsa-project.org/main/index.php/Main_Page>`__
#. `ALSA User Space
   Library <http://www.alsa-project.org/alsa-doc/alsa-lib/>`__
#. `Using ALSA Audio
   API <http://www.equalarea.com/paul/alsa-audio.html>`__ Author: Paul
   Davis

.. rubric:: Software Help
   :name: additional-information-software-help

.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family')

    #. `Tools and Techniques for Audio Debugging
       <https://www.ti.com/lit/an/sprac10/sprac10.pdf>`__
    #. `Interfacing DRA7xx Audio to Analog Codecs
       <http://www.ti.com/lit/an/sprac09a/sprac09a.pdf>`__

.. ifconfig:: CONFIG_part_family in ('J7_family', 'AM62X_family', 'AM62AX_family', 'AM62DX_family', 'AM62PX_family', 'AM62LX_family')

    #. `Tools and Techniques for Audio Debugging
       <https://www.ti.com/lit/an/sprac10/sprac10.pdf>`__

.. rubric:: Audio hardware codecs
   :name: additional-information-audio-hardware-codecs

.. ifconfig:: CONFIG_part_variant in ('AM335X', 'AM437X', 'AM62X', 'AM62AX', 'AM62PX', 'J722S', 'AM62LX')

    #. `TLV320AIC31 - Low-Power Stereo CODEC with HP
       Amplifier <http://www.ti.com/lit/ds/symlink/tlv320aic31.pdf>`__
    #. `TLV320AIC3104 - Low-Power Stereo CODEC with HP
       Amplifier <http://www.ti.com/lit/ds/symlink/tlv320aic3104.pdf>`__
    #. `TLV320AIC3111 - Low-Power Stereo CODEC with Embedded miniDSP
       and Stereo Class-D Speaker Amplifier <http://www.ti.com/lit/ds/symlink/tlv320aic3111.pdf>`__
    #. `TLV320AIC3106 - Low-Power Stereo Audio CODEC
       <http://www.ti.com/lit/ds/symlink/tlv320aic3106.pdf>`__

.. ifconfig:: CONFIG_part_variant in ('J721E', 'J784S4','J742S2')

    #. `PCM3168A - 24-Bit, 96kHz/192kHz, 6-In/8-Out Audio CODEC with
       Differential Input/Output
       <http://www.ti.com/lit/ds/symlink/pcm3168a.pdf>`__

.. ifconfig:: CONFIG_part_variant in ('AM62DX')

    #. `TAD52512 - High-performance stereo audio DAC
       <https://www.ti.com/lit/ds/symlink/tad5212.pdf>`__
