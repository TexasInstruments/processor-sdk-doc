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

McASP Configuration
^^^^^^^^^^^^^^^^^^^

TI EVMs include a default McASP configuration in the device tree that defines
the sound topology connecting McASP to the onboard codec(s). For custom designs
using a different sound topology—such as different codec connections or a
different codec—the McASP configuration parameters described in this section
can be modified accordingly in the device tree.

The Multichannel Audio Serial Port (McASP) is a highly configurable audio
interface that supports various audio protocols including I2S, TDM, and S/PDIF,
and a flexible clocking scheme, which allows for complete
independence between the receive and transmit ports.

McASP serializers are connected to data pins, referred to as AXR pins. The name
stands for "Audio Transmit/Receive" (AXR), reflecting the fact that any McASP data
pin can be configured to function as either an input or an output. As such, the
terms "serializer" and "AXR pin" are used interchangeably throughout this documentation.

Device Tree Properties
""""""""""""""""""""""

McASP nodes are typically defined in the SoC-level device tree (.dtsi) first with
base properties like ``compatible``, ``reg``, ``interrupts``, and ``dmas``,
which stay the same regardless of audio configuration.

Board-level device trees then customize the McASP configuration using the
properties below. Together they form the complete McASP node definition.

The following table briefly describes the McASP-specific properties configured
in board-level device trees:

.. list-table::
   :header-rows: 1
   :widths: 20 12 8 60

   * - Property
     - Type
     - Required
     - Description
   * - **op-mode**
     - uint32
     - Yes
     - | Operation mode:
       | • 0 for I2S/TDM mode
       | • 1 for DIT mode (Transmitter-only mode for self-encoding formats like S/PDIF)
   * - **tdm-slots**
     - uint32
     - Yes, for I2S/TDM mode
     - | Number of TDM slots for TX (and RX if ``tdm-slots-rx`` not specified). Range: 2-32.
       | Ignored in DIT mode.
   * - **auxclk-fs-ratio**
     - uint32
     - No :sup:`1`
     - | A fixed multiplier to sampling rate (𝑓\ :sub:`s`) for a given AUXCLK frequency for TX (and RX if ``auxclk-fs-ratio-rx`` not specified).
       | :sup:`1` If not specified, dividers are calculated from ``.set_sysclk`` via the ASoC machine driver. (For common machine driver such as simple-audio-card or audio-graph-card, this is set via the ``system-clock-frequency = <>`` property in the DAI link).
       | Only applicable when McASP is the master which produces the bit clock.
       | See :ref:`Configuration Guidelines <mcasp-configuration-guidelines>` for details on usage and calculation.
   * - **serial-dir**
     - uint32 array
     - Yes
     - | Serializer pin configuration.
       | For each AXR pin:
       | 0 = Inactive,
       | 1 = TX,
       | 2 = RX.
       | Must include all AXR pins available on the McASP instance.
   * - **ti,async-mode**
     - boolean
     - No
     - | Enables independent TX and RX clocking, allowing different sample rates (𝑓\ :sub:`s`) and bits per frame for playback and capture.
       | Ignored in DIT mode.
   * - **tdm-slots-rx**
     - uint32
     - No
     - | Number of TDM slots for RX, allowing independent RX slot count. Range: 2-32.
       | Requires ``ti,async-mode``.
   * - **auxclk-fs-ratio-rx**
     - uint32
     - No
     - | Multiplier to sampling rate for a given AUXCLK frequency for RX.
       | Requires ``ti,async-mode``.
   * - **tx-num-evt**
     - uint32
     - No
     - WFIFO threshold for TX. Enables TX FIFO buffering when non-zero. Disabled by default.
   * - **rx-num-evt**
     - uint32
     - No
     - RFIFO threshold for RX. Enables RX FIFO buffering when non-zero. Disabled by default.

.. note::

   | In the latest K3 family of SoCs (Sitara™ AM6x, Jacinto™ J4x platforms etc.), McASP FIFOs are disabled by default to achieve low latency, since K3 DMA already provides internal buffering.
   | Enabling McASP FIFOs is generally not required and should be considered for specific use cases that need additional buffering at the McASP level, such as:
   | • Scenarios with slow DMA throughput
   | • High DDR bandwidth utilization where additional buffering helps system stability
   | • Applications requiring extra data buffering to compensate for overall system latency

For more detail, refer to `davinci-mcasp-audio.yaml <https://www.kernel.org/doc/Documentation/devicetree/bindings/sound/davinci-mcasp-audio.yaml>`__ and `davinci-mcasp-audio.txt <https://www.kernel.org/doc/Documentation/devicetree/bindings/sound/davinci-mcasp-audio.txt>`__ in the Linux kernel source.

Capabilities Overview
"""""""""""""""""""""

The McASP driver supports multiple audio protocols and operational modes:

**Operation Modes:**

* **I2S/TDM Mode (op-mode = 0)**

  - Supports 2 to 32 TDM slots (channels)
  - Full-duplex operation (simultaneous TX and RX)
  - Can operate in synchronous or asynchronous mode

* **DIT Mode (op-mode = 1)**

  - Transmit-only operation
  - Hardware-generated S/PDIF encoding
  - The ``tdm-slots``, ``ti,async-mode`` properties are ignored
  - Only inactive or TX serializers (values 0, 1) should be configured in ``serial-dir``

**Clock Modes:**

* **Synchronous Mode** (default): TX and RX share the same bit clock and frame sync signals,
  requiring identical sample rates and bits per frame for both directions

   * Suited for simple, single-codec designs where ADC and DAC bit clocks and frame sync need to be synchronized

* **Asynchronous Mode** (``ti,async-mode``): Independent TX and RX clocking,
  allowing different sample rates, bits per frame, and TDM slot counts for
  playback and capture

   * Enables simultaneous playback and capture with independent audio settings
   * Allows flexibility in multi-sound topology designs with various ASoC codec-class drivers connected to the same McASP instance

.. important::

   | To fully support asynchronous mode, the codec driver must also support independent clocking for playback/capture and should not impose such restrictions on ASoC framework.
   | For instance, ``.symmetric_rate`` should not be set in the codec driver's snd_soc_dai_driver struct. Otherwise, opening streams with different audio settings will fail with errors similar to the following:

   .. code-block:: console

      [  146.186314]  davinci-mcasp.0-pcmdevice-codec: ASoC: unmatched rate symmetry: 2b20000.au
      dio-controller:44100 - soc_pcm_params_symmetry:48000
      [  146.187012]  davinci-mcasp.0-pcmdevice-codec: ASoC: error at __soc_pcm_hw_params on dav
      inci-mcasp.0-pcmdevice-codec: -22
      arecord: set_params:1456: Unable to install hw params:
      ...

**Key Features:**

* Multiple serializers (up to 16) for multi-channel audio
* Configurable McASP FIFO buffering (tx-num-evt, rx-num-evt)
* Fixed clock generation with auxclk-fs-ratio or dynamic machine driver sysclk settings
* Support for master and slave clock modes (via DAI link configuration)

Configuration Scenarios
"""""""""""""""""""""""

The examples below show typical board-level McASP configurations. Base properties
like ``compatible``, ``reg``, ``interrupts``, and ``dmas`` are inherited from the
SoC-level dtsi file and are not shown here.

**I2S/TDM Mode - Synchronous, Stereo (2 slots)**

For stereo audio (2 TDM slots) with synchronized TX/RX clocking:

.. code-block:: devicetree

   /* Example from AM62x-SK (k3-am62x-sk-common.dtsi) */
   &mcasp1 {
      status = "okay";
      #sound-dai-cells = <0>;

      pinctrl-names = "default";
      pinctrl-0 = <&main_mcasp1_pins_default>;

      op-mode = <0>;          /* MCASP_IIS_MODE */
      tdm-slots = <2>;
      auxclk-fs-ratio = <256>;
      serial-dir = <  /* 0: INACTIVE, 1: TX, 2: RX */
            1 0 2 0
            0 0 0 0
            0 0 0 0
            0 0 0 0
      >;
  };

**I2S/TDM Mode - Synchronous, Multiple TX Serializers**

For stereo audio (2 TDM slots) with multiple TX serializers and auxclk-fs-ratio
(synchronized TX/RX clocking):

.. code-block:: devicetree

   /* Example from J721S2 (k3-j721s2-common-proc-board.dts) */
   &mcasp4 {
      status = "okay";
      #sound-dai-cells = <0>;

      pinctrl-names = "default";
      pinctrl-0 = <&mcasp4_pins_default>;

      op-mode = <0>;          /* MCASP_IIS_MODE */
      tdm-slots = <2>;
      auxclk-fs-ratio = <256>;
      serial-dir = <	/* 0: INACTIVE, 1: TX, 2: RX */
         0 2 1 1
         0 0 0 0
         0 0 0 0
         0 0 0 0
      >;
   };

**I2S/TDM Mode - Asynchronous (Independent TX/RX)**

For I2S/TDM mode with asynchronous clocking, enabling independent TX and RX
configurations with different slot counts and sample rates. This contrasts with
the synchronous I2S/TDM modes above where TX and RX share the same clocking:

.. code-block:: devicetree

   /* Example from AM62D-EVM (k3-am62d2-evm.dts) */
   &mcasp2 {
      status = "okay";
      #sound-dai-cells = <0>;

      pinctrl-names = "default";
      pinctrl-0 = <&main_mcasp2_pins_default>;

      auxclk-fs-ratio = <2177>;
      op-mode = <0>;          /* MCASP_IIS_MODE */
      tdm-slots = <2>;        /* DAC Codec configured for stereo playback */
      tdm-slots-rx = <4>;     /* ADC Codec configured for 4-channel capture */
      ti,async-mode;
      serial-dir = <	/* 0: INACTIVE, 1: TX, 2: RX */
            1 1 0 1
            1 0 0 0
            0 0 0 0
            0 0 2 0
      >;
   };

**DIT Mode (S/PDIF)**

For S/PDIF digital audio output (transmit-only):

.. code-block:: devicetree

   /* Example from OMAP4 device (omap4-l4-abe.dtsi) */
   &mcasp0 {
      status = "okay";
      #sound-dai-cells = <0>;

      pinctrl-names = "default";
      pinctrl-0 = <&main_mcasp0_pins_default>;

      op-mode = <1>;	/* MCASP_DIT_MODE */
      serial-dir = < 1 >;
   };

.. _mcasp-configuration-guidelines:

Configuration Guidelines
""""""""""""""""""""""""

This section provides rules and guidelines when configuring certain McASP device tree properties.

**auxclk-fs-ratio**

This property defines the ratio between the AUXCLK (reference clock) and the sampling rate, as a means to statically
configure its internal clock dividers. Giving a hint to the driver to pick the specific sampling rate whenever possible at runtime.

Alternatively, a fixed clock source frequency can be specified via the DAI-link property
``system-clock-frequency = <>`` or via a custom machine driver's ``.set_sysclk()`` callback,
allowing the driver to dynamically calculate dividers for any McASP-supported sampling rate.

Either or both properties may be defined. But at least one must be provided: ``auxclk-fs-ratio`` to specify the clock divider, or ``system-clock-frequency`` to specify the reference clock frequency directly.

When using **auxclk-fs-ratio**, calculate the ratio as follows:

For example, given a desired sampling rate of 44.1kHz with a 96MHz AUXCLK, the auxclk-fs-ratio would be: :math:`96000000 / 44100 = 2177`.
This ratio is also applicable to other standard sampling rates McASP supports, as long as the produced bit clock is within acceptable tolerance.

The same applies to **auxclk-fs-ratio-rx**.

Refer to the :ref:`Runtime Behavior <mcasp-runtime-behavior>` section below for tolerance calculation details.

**serial-dir**

The ``serial-dir`` array size must match the hardware (e.g., 16 AXR pins for McASP0 means array must have 16 entries).
Each McASP instance may have up to 16 AXR pins, please refer to device-specific data sheet and TRM.

.. code-block:: devicetree

   serial-dir = <  /* 0: INACTIVE, 1: TX, 2: RX */
         1 0 2 0  /* AXR0-3:  TX, Inactive, RX, Inactive */
         0 0 0 0  /* AXR4-7:  All inactive */
         0 0 0 0  /* AXR8-11: All inactive */
         0 0 0 0  /* AXR12-15: All inactive */
   >;

Codec Integration
"""""""""""""""""

The McASP configuration described above defines the hardware interface.
To create a functional audio device, the McASP node needs to be connected to `codec class driver(s) <https://docs.kernel.org/sound/soc/codec.html>`__
via a sound card definition in the device tree.

The **simple-audio-card** is a generic machine driver and establishes Digital Audio Interface (DAI)
links that connect the McASP (CPU-side) to codec(s). These DAI links operate within the ASoC framework, which constitutes part of the ALSA stack.
Most TI EVMs use simple-audio-card for its simplicity, though audio-graph-card or custom machine drivers are also supported.
All DAI link properties McASP relies on are part of the generic ASoC framework, not specific to any particular machine driver.

The DAI link configuration provides the following intrinsics to the McASP driver:

* Link McASP instance(s) to codec instance(s)
* Mapping of McASP serializers to DAI links

  * e.g., McASP assumes the first TX AXR pin is mapped to the first playback-enabled DAI link and outputs data to the first available TX TDM slot; see :ref:`Channel Mapping <mcasp-channel-mapping>`

* Master/slave clocking roles for bit clock and frame sync signals

  * If McASP is the master, ``system-clock-direction-out`` must be declared in the CPU DAI for McASP to generate clocks

* Data alignment format

  * e.g., "dsp_a", "dsp_b", "i2s"

* Polarity of bit clock and frame sync signals via ``bitclock-inversion`` and ``frame-inversion``
* Optional dai-link properties:

  * ``system-clock-frequency``
  * ``dai-tdm-slot-width``
  * ``dai-tdm-slot-num``
  * ``dai-tdm-slot-tx-mask``
  * ``dai-tdm-slot-rx-mask``

.. attention::

   Due to ASoC and driver limitations, the data alignment format must remain the same for every DAI link connected to the same McASP node, even in asynchronous mode where the hardware is capable of having independent playback and capture settings.

Optional ``dai-link`` Properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**system-clock-frequency** *(Type = uint32)*

When McASP is the bit clock master, this property provides a fixed reference clock frequency to the McASP driver, refer to the :ref:`Runtime Behavior <mcasp-runtime-behavior>` section below.

**dai-tdm-slot-width** *(Type = uint32)*

In the McASP driver logic, audio bit widths are dynamically configured at runtime, unless constrained by the optional ``dai-tdm-slot-width`` property. When specified, this property limits the hardware TDM slot width on the bus, restricting the maximum format width (bit depth) while still allowing dynamic selection within that constraint.
For instance, setting ``dai-tdm-slot-width = <24>`` allows audio bit depth of 8, 16, or 24 per sample, but not 32 bits.

On the specifics of how the driver handles audio format negotiation at runtime, refer to the :ref:`Runtime Behavior <mcasp-runtime-behavior>` section below.

**dai-tdm-slot-num** *(Type = uint32)*

Applying ``dai-tdm-slot-num`` by itself is not advised, as McASP already derives the TDM slot count from ``tdm-slots`` or ``tdm-slots-rx`` properties in the McASP device tree node.
The property is to be used in conjunction with ``dai-tdm-slot-width`` to accommodate the standard ASoC API.

.. attention::
   | When supplying the ``dai-tdm-slot-width`` property to a DAI link, ensure ``dai-tdm-slot-num`` is also provided, to avoid slot count mismatches set by ASoC API.
   |
   | For a playback-enabled DAI link, the value of ``dai-tdm-slot-num`` must match the ``tdm-slots`` defined in the McASP node.
   | For a capture-enabled DAI link, the value of ``dai-tdm-slot-num`` must match the ``tdm-slots``, or ``tdm-slots-rx`` if supplied.

**dai-tdm-slot-tx-mask** and **dai-tdm-slot-rx-mask** *(Type = uint32 array)*

``dai-tdm-slot-tx-mask`` and ``dai-tdm-slot-rx-mask`` allow masking out specific TDM slots on the bus for TX stream and RX stream, respectively, providing finer control over which slots are active for audio data transfer.

The properties are type `uint32 array`, where each bit represents a TDM slot on the bus. A bit value of 1 indicates the corresponding slot is active, while 0 means inactive. The size of the array must match the number of TDM slots defined in the McASP node.

**playback-only** and **capture-only** *(Type = boolean)*

A DAI link is deemed playback-enabled if both CPU (McASP) and codec DAI support playback (TX), and capture-enabled if both support capture (RX).

Since McASP supports both TX and RX, the ``playback-only`` and ``capture-only`` properties can restrict a DAI link's direction when the codec driver also supports both directions.
The restricted direction will not be exposed as an ALSA PCM subdevice.

.. tip::

   The following example illustrate the optional dai-link properties discussed above.

   .. code-block:: devicetree

      sound0 {
         compatible = "simple-audio-card";
         simple-audio-card,name = "Demonstration";

         simple-audio-card,dai-link@0 {
            format = "dsp_a";
            bitclock-master = <&cpu_dai>;
            frame-master = <&cpu_dai>;

            cpu_dai: cpu {
                  sound-dai = <&mcasp0>;
                  system-clock-direction-out;

                  /* Configuration for 4 slots, each 24 bits wide max */
                  /* tdm-slots = <4>; in McASP node */
                  dai-tdm-slot-num = <4>;
                  dai-tdm-slot-width = <24>;

                  /* Bitmask to enable specific slots (e.g., 3rd tdm slot is inactive) */
                  dai-tdm-slot-tx-mask = <1 1 0 1>;
                  dai-tdm-slot-rx-mask = <1 1 0 1>;
            };

            codec {
                  sound-dai = <&tlv320aic32x4>;

                  /* Assume codec driver also implements the interface */
                  dai-tdm-slot-num = <4>;
                  dai-tdm-slot-width = <24>;
            };
         };
      };

Audio Card Examples
~~~~~~~~~~~~~~~~~~~

**Single Codec**

For simple stereo configurations with one codec, a single DAI link suffices:

.. code-block:: devicetree

   sound0 {
      compatible = "simple-audio-card";
      simple-audio-card,name = "AM62x-SKEVM";
      simple-audio-card,format = "i2s";

      simple-audio-card,cpu {
         sound-dai = <&mcasp1>;
      };

      simple-audio-card,codec {
         sound-dai = <&tlv320aic3106>;
      };
   };

In this single codec configuration:

* ``ti,async-mode`` should be disabled (synchronous mode) in McASP device tree node since playback and capture share the same codec and require identical clock settings

**Multiple Codecs**

When using multiple codecs, define separate DAI links for each codec.
The following syntax allows separate configurations for each DAI link:

.. code-block:: devicetree

   /* Example from AM62D-EVM (k3-am62d2-evm.dts) */
   sound0 {
      compatible = "simple-audio-card";
      simple-audio-card,name = "AM62D2-EVM";

      /* First DAI, McASP in master mode */
      simple-audio-card,dai-link@0 {
         format = "dsp_a";
         bitclock-master = <&master0>;
         frame-master = <&master0>;

         master0: cpu {
               sound-dai = <&mcasp2>;
               system-clock-direction-out;
         };

         codec@0 {
               sound-dai = <&pcm6240>;
         };
      };

      /* Second DAI, McASP in master mode */
      simple-audio-card,dai-link@1 {
         format = "dsp_a";
         bitclock-master = <&master1>;
         frame-master = <&master1>;

         master1: cpu {
               sound-dai = <&mcasp2>;
               system-clock-direction-out;
         };

         codec@1 {
               sound-dai = <&tad5212_dac1>;
               playback-only;
         };
      };

      /* Additional dai-link@2, @3, @4 for more codecs... */
   };

In this multi-codec configuration:

* Each DAI link connects the same McASP instance to different codecs and maps serializers/AXRs accordingly
* It is recommended to enable ``ti,async-mode`` in the McASP device tree node to allow more flexibility with independent TX/RX clocking
* The ``bitclock-master`` and ``frame-master`` properties specify which device (CPU or codec) drives the bit clock and frame sync signals
* ``system-clock-direction-out`` is required for McASP to generate clocks, which is required when McASP is driving the signals in master mode
* Since McASP is in master mode, ``auxclk-fs-ratio`` should be defined in the McASP node, otherwise ``system-clock-frequency`` must be set in the DAI link to provide a fixed clock source

For more information on DAI link configuration and ASoC machine drivers, refer to ALSA links in the :ref:`Additional Information <additional-information-alsa-links>` section below.

.. _mcasp-runtime-behavior:

Runtime Behavior
""""""""""""""""

The McASP driver makes dynamic runtime decisions when handling audio streams,
including serializer activation, channel-to-slot mapping, and supported audio formats.
These behaviors are determined by the interaction between hardware capabilities and
parameters requested by userspace through the ALSA framework.

.. note::

   The runtime behaviors described in this section apply to I2S/TDM mode (``op-mode = 0``) only.
   DIT mode (``op-mode = 1``) has fixed S/PDIF encoding behavior per specification.

.. _mcasp-channel-mapping:

Channel Mapping
~~~~~~~~~~~~~~~

When a playback or capture stream is opened, the ALSA framework passes the requested
number of audio channels from the userspace application to the McASP driver.

The driver activates TX or RX serializers (AXR pins) in the order they appear in the ``serial-dir``
device tree property. For each serializer, the driver maps channels to available TDM slots sequentially.
If ``dai-tdm-slot-tx-mask`` or ``dai-tdm-slot-rx-mask`` are configured, disabled slots are skipped.
This process continues across multiple serializers until all requested channels are mapped.
Unused TDM slots and AXR pins remain inactive.

The total TDM slot count on the bus (frame sync period) is always preserved as defined
by ``tdm-slots`` or ``tdm-slots-rx``, regardless of how many channels are actively used.

If the requested channels exceed the available capacity (:math:`active\_serializers \times slots\_per\_serializer`), the driver rejects the stream with an error.

Sample Rate and Bit Depth
~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This section only pertains to McASP configured as the bit clock master.
   When McASP is in slave mode, it accepts whatever combinations
   the codec provides without imposing constraints.

When a stream is opened and McASP is in master mode, the driver evaluates which
sample rate and bit depth combinations can be supported based on its ability to
generate the required bit clock frequency within ±1000 ppm tolerance (0.1%).

The driver uses ``auxclk-fs-ratio`` (if defined) to calculate the expected reference clock
frequency as ``rate × ratio`` for each sampling rate, and/or uses a fixed clock source frequency
from ``system-clock-frequency``/``.set_sysclk()`` for all rates. In both cases, it calculates
dividers to determine which bit clock frequencies can be achieved within tolerance.

:math:`error_{ppm} = \frac{actual\_freq - target\_freq}{target\_freq} \times 10^6`

Only combinations that can be accurately generated are provided as supported formats,
and ALSA subsequently selects the best configuration for the userspace application.

To support a specific sample rate and bit depth combination, ensure that:

* The ``auxclk-fs-ratio`` property or machine driver's ``.set_sysclk()`` configuration
  allows the McASP to generate the required bit clock frequency within tolerance
* The codec supports the desired combination
* If the source audio format differs, one may configure explicit resampling via :file:`~/.asoundrc`
  or :file:`/etc/asound.conf` ALSA config file in userspace.

Generic commands and instructions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Most of the boards have simple audio setup which means we have one
sound card with one playback and one capture PCM.
To list the available sound cards and PCMs for playback:

.. code-block:: text

    aplay -l

To list the available sound cards and PCMs for capture:

.. code-block:: text

    arecord -l

For McASP-based sound card, each DAI link instance is represented as a
separate subdevice.

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
       :name: kernel-config-8

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
       :name: user-space-8-kernel-audio

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

.. ifconfig:: CONFIG_part_variant in ('AM62DX')

   The board uses four **TAD52512 DAC** and two **PCM6240 ADC** connected through
   **McASP2 [AXR0,1,3 and 4 for playback, AXR14 for Capture]** for audio.
   The board features eight TRS 3.5mm jack, that can be used for
   simultaneous 8 channel playback and 4 channel recording.

   The AM62D2-EVM audio subsystem provides comprehensive playback and recording
   capabilities through dedicated DACs and ADCs. Use the following command to list
   available playback devices:

   .. code-block:: console

      root@am62dxx-evm:/opt/ltp# aplay -l
      **** List of PLAYBACK Hardware Devices ****
      card 0: AM62D2EVM [AM62D2-EVM], device 0: davinci-mcasp.0-pcmdevice-codec pcmdevice-codec-0 [davinci-mcasp.0-pcmdevice-codec pcmdevice-codec-0]
      Subdevices: 1/1
      Subdevice #0: subdevice #0
      card 0: AM62D2EVM [AM62D2-EVM], device 1: davinci-mcasp.0-tad5x1x-hifi-50 tad5x1x-hifi-50-1 [davinci-mcasp.0-tad5x1x-hifi-50 tad5x1x-hifi-50-1]
      Subdevices: 1/1
      Subdevice #0: subdevice #0
      card 0: AM62D2EVM [AM62D2-EVM], device 2: davinci-mcasp.0-tad5x1x-hifi-51 tad5x1x-hifi-51-2 [davinci-mcasp.0-tad5x1x-hifi-51 tad5x1x-hifi-51-2]
      Subdevices: 1/1
      Subdevice #0: subdevice #0
      card 0: AM62D2EVM [AM62D2-EVM], device 3: davinci-mcasp.0-tad5x1x-hifi-52 tad5x1x-hifi-52-3 [davinci-mcasp.0-tad5x1x-hifi-52 tad5x1x-hifi-52-3]
      Subdevices: 1/1
      Subdevice #0: subdevice #0
      card 0: AM62D2EVM [AM62D2-EVM], device 4: davinci-mcasp.0-tad5x1x-hifi-53 tad5x1x-hifi-53-4 [davinci-mcasp.0-tad5x1x-hifi-53 tad5x1x-hifi-53-4]
      Subdevices: 1/1
      Subdevice #0: subdevice #0

   Audio playback is handled by four TAD5212 codec devices. These devices provide
   multi-channel audio output capabilities through the davinci-mcasp interface.
   Audio recording is managed by two PCM6240 ADC devices. Each PCM6240 ADC
   supports four channel audio input with configurable profiles for different
   I2C addresses.

   **Playback Subsystem**

   The TAD5212 driver is located in the kernel configuration at:

   .. code-block:: text

      -> Device Drivers
       -> Sound card support (SOUND [=y])
        -> Advanced Linux Sound Architecture (SND [=y])
         -> ALSA for SoC audio support (SND_SOC [=y])
          -> CODEC drivers
           -> Texas Instruments TAC5X1X family driver based on I2C (SND_SOC_TAC5X1X_I2C [=m])

   To play audio on the AM62D2-EVM, use the aplay command.
   Audio playback is available through connectors J3 and J4.

   Example playback command:

   .. code-block:: console

      root@am62dxx-evm:~# aplay audio_file.wav

   **Recording Subsystem**

   Audio recording is performed through connectors J1 and J2. The two PCM6240
   devices corresponding to different I2C addresses.

   The PCM6240 driver is located in the kernel configuration at:

   .. code-block:: text

      -> Device Drivers
       -> Sound card support (SOUND [=y])
        -> Advanced Linux Sound Architecture (SND [=y])
         -> ALSA for SoC audio support (SND_SOC [=y])
          -> CODEC drivers
           -> Texas Instruments PCM6240 Family Audio chips based on I2C (SND_SOC_PCM6240 [=m])

   Choose active device between two PCM6240 ADC devices:

   .. code-block:: text

      Device 0: PCM6240 at I2C address 0x48 (Connector-J2)
      Device 1: PCM6240 at I2C address 0x49 (Connector-J1)

   To select Device 0 (I2C address 0x48) as an active device:

   .. code-block:: console

      root@am62dxx-evm:~# amixer cset name='pcm6240-2dev-reg PCM6240 i2c1 Profile id' 0
      numid=17,iface=MIXER,name='pcm6240-2dev-reg PCM6240 i2c1 Profile id'
      type=INTEGER,access=rw------,values=1,min=0,max=3,step=0
      values=0

   To select Device 1 (I2C address 0x49) as an active device:

   .. code-block:: console

      root@am62dxx-evm:~# amixer cset name='pcm6240-2dev-reg PCM6240 i2c1 Profile id' 1
      numid=17,iface=MIXER,name='pcm6240-2dev-reg PCM6240 i2c1 Profile id'
      type=INTEGER,access=rw------,values=1,min=0,max=3,step=0
      values=1

   To record 4-channel audio at 48kHz sample rate with 32-bit depth:

   .. code-block:: console

      root@am62dxx-evm:~# arecord -c 4 -r 48000 -f S32_LE test.wav

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

.. ifconfig:: CONFIG_part_variant in ('AM62DX')

   Following additional issues were observed for AM62D2-EVM in this release:

   - The device requires a restart if audio is missing or plays through
     only one channel during simultaneous playback and recording.
   - Starting playback while recording is active introduces a small glitch
     in the recording.

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
    #. `PCM6240 - Automotive, 4-channel audio ADC
       <https://www.ti.com/lit/ds/symlink/pcm6240-q1.pdf>`__

.. rubric:: McASP Documentation
   :name: additional-information-mcasp-docs

#. `McASP Hardware Design Guide
   <https://www.ti.com/lit/pdf/sprack0>`__