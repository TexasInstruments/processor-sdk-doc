.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_MCASP

Overview
--------

Introduction
^^^^^^^^^^^^

The multichannel audio serial port (McASP) functions as a
general-purpose audio serial port optimized for the needs of
multichannel audio applications. The McASP is useful for time-division
multiplexed (TDM) stream, Inter-Integrated Sound (I2S) protocols, and
intercomponent digital audio interface transmission (DIT).The
multichannel buffered serial port (McASP) peripheral allows direct
interface to other TI DSPs, codecs, and other devices in a system. The
following sub sections explain the hardware (McASP peripheral) and
software context of the McASP LLD.

The device driver exposes a set of well-defined APIs which are used by
the application layer to send and receive data via the McASP peripheral.
The driver also exposes a set of well-defined OS abstraction APIs which
are used to ensure that the driver is OS independent and portable. The
McASP driver uses the CSL McASP register layer for all McASP MMR access.
The McASP driver also interfaces with the EDMA3/UDMA library to be able to
transfer data to and from McASP peripheral and data memory.

User Interface
--------------

Driver Configuration
^^^^^^^^^^^^^^^^^^^^^

The McASP driver provides a sample implementation sequence which
initializes the MCASP IP block. The McASP Device initialization API is
implemented as a sample prototype:

::

    void McaspDevice_init (void)

The function initializes all the instance specific information like base
address of instance CFG registers, FIFO address for the instance, TX and
RX CPU event numbers, TX and RX EDMA event numbers etc.

For details about individual fields of this structure, see the Doxygen
help by opening
PDK_INSTALL_DIR\Packages\ti\drv\mcasp\docs\doxygen\html\index.html.

::

     int32_t Mcasp_socGetInitCfg(uint32_t index, Mcasp_HwInfo *cfg)

The function obtains the soc configuration parameters such as interrupt
numbers, mux configuration parameters etc.

::

     int32_t Mcasp_socSetInitCfg(uint32_t index, const Mcasp_HwInfo *cfg)

The function set the soc configuration parameters such as interrupt
numbers, mux configuration parameters etc.

APIs
^^^^^

Refer to below API files:

::

    #include <ti/drv/mcasp/mcasp_drv.h>
    #include <ti/drv/mcasp/soc/mcasp_soc.h>

.. rubric:: McASP Buffer formats
   :name: mcasp-buffer-formats

The McASP driver provides various buffer formats for sending the data
to/from the audio device. The differences between these formats arise
from the way the audio samples are collected from various serializers
and their timeslots and arranged in the system's memory. This way the
application can choose to run audio processing algorithms over the data
without the need for re-arranging those data every frame. The buffer
format is provided in the **Mcasp_ChanParams.dataFormat** in the form of
**Mcasp_BufferFormat** defined in mcasp_drv.h The below section provides
an overview of the various formats. In the explanatory diagrams in each
section, McASP controller recieves samples in frame intervals denoted by
t1,t2..tn. The McASP driver collects these and arranges those samples in
the memory in various formats in to the host's System memory. We have
chosen 32 bit samples and 32-bit word addresses throughout for
simplicity.

.. rubric:: Mcasp_BufferFormat_1SER_1SLOT
   :name: mcasp_bufferformat_1ser_1slot

This is applicable if only one serializer and one timeslot is used. The
samples are ordered in the order they received or sent.

.. Image:: /images/1SLOT_1SER.PNG

.. rubric:: Mcasp_BufferFormat_1SER_MULTISLOT_INTERLEAVED
   :name: mcasp_bufferformat_1ser_multislot_interleaved

This is applicable if multiple slots are used with one serializer. The
samples from the different timeslots are stored interleaved in the
memory as below. Different timeslots' samples are denoted by different
colors and are labelled t1,t2..tn according to the time they arrive at
the serializer.

.. Image:: /images/1SER_MULTISLOT_INTERLEAVED.PNG

.. rubric:: Mcasp_BufferFormat_1SER_MULTISLOT_NON_INTERLEAVED
   :name: mcasp_bufferformat_1ser_multislot_non_interleaved

This is applicable if multiple slots are used with one serializer. The
samples from the different timeslots are grouped together on the basis
of the timeslot and stored in the memory as shown below. Different
timeslots' samples are denoted by different colors and are labelled
t1,t2..tn according to the time they arrive at the serializer.

.. Image:: /images/1SER_MULTISLOT_NON_INTERLEAVED.PNG

NOTE: if the non-interleaved format is used, the Mcasp_ChanParams->
hwFifoEventDMARatio must be set to 1.

.. rubric:: Mcasp_BufferFormat_MULTISER_1SLOT_SER_INTERLEAVED
   :name: mcasp_bufferformat_multiser_1slot_ser_interleaved

This is applicable if multiple serializers are used with one time slot
is used for each of the serializers. The samples from the different
serializers are stored in the memory in interleaved fashion as shown
below Different serializers' samples are denoted by different colors and
are labelled S1,S2..Sn according to the time they arrive at the
serializer.

.. Image:: /images/1SER_MULTISER_1SLOT_SER_INTERLEAVED_2.PNG

|

.. rubric:: Mcasp_BufferFormat_MULTISER_1SLOT_SER_NON_INTERLEAVED
   :name: mcasp_bufferformat_multiser_1slot_ser_non_interleaved

This is applicable if multiple serializers are used with one timeslots
each per serializer. The samples from the different timeslots are
grouped together on the basis of the serializer and stored in the memory
as shown below Different serializers' samples are denoted by different
colors and are labelled S1,S2..Sn according to the time they arrive at
the serializer.

.. Image:: /images/1SER_MULTISER_1SLOT_SER_NON_INTERLEAVED.PNG

.. rubric:: Mcasp_BufferFormat_MULTISER_MULTISLOT_SEMI_INTERLEAVED_1
   :name: mcasp_bufferformat_multiser_multislot_semi_interleaved_1

This is applicable if multiple serializers are used and each serializer
containing multiple timeslots. The samples are stored in the memory
interleaved based on serializer and timeslots as shown below. In this
example, there are 3 serializers and 2 timeslots per serializers whose
samples are noted by Ln (left) and Rn (right). Different serializers'
samples are denoted by different colors.

.. Image:: /images/1SER_MULTISER_MULTISLOT_SEMI_INTERLEAVED_1_UPDATED.PNG

.. rubric:: Mcasp_BufferFormat_MULTISER_MULTISLOT_SEMI_INTERLEAVED_2
   :name: mcasp_bufferformat_multiser_multislot_semi_interleaved_2

This is applicable if multiple serializers are used and each serializer
containing multiple timeslots. The samples are grouped based on the
serializer and within one serializer, the timeslots are interleaved as
shown below. In this example, there are 3 serializers and 2 timeslots
per serializers whose samples are noted by Ln (left) and Rn
(right).Different serializers' samples are denoted by different colors.

.. Image:: /images/1SER_MULTISER_MULTISLOT_SEMI_INTERLEAVED_2.PNG

NOTE: if the non-interleaved format is used, the Mcasp_ChanParams->
hwFifoEventDMARatio must be set to 1.

.. rubric:: Mcasp WordBits Selection
   :name: mcasp-wordbits-selection

With all the frame formats explained above, there is an option to choose
which bits to pack from the 32-bit serializer data obtained from/to the
McASP serializer, when the word size is less than the slot size. This
option is exercised by setting the Mcasp_chanParams->wordBitsSelect to
Mcasp_wordBitsSelect_LSB/Mcasp_wordBitsSelect_MSB.

If the default Mcasp_wordBitsSelect_LSB option is selected, the LSBs are
packed in to the system memory.

Below is an example of word size = 16bits and slot size = 32 bits and
the Mcasp_wordBitsSelect_LSB option is used. On the receiving side, the
serializer holds the 32 bit data whose LSB 16 bits are picked up and
packed in to the system memory. The MSB 16 bits are ignored.

.. Image:: /images/WordSelect_LSB.PNG

If the Mcasp_wordBitsSelect_MSB option is used, the serializer's
MSB-16bits are packed in to the system memory. The LSBs are ignored.

.. Image:: /images/WordSelect_MSB.PNG

.. rubric:: Priming
   :name: priming

Applications using McASP driver often might send/receive one or two
transfers via McASP before sending the application data in/out of McASP
through the driver. This would internally set up transfer request queues
so that the application can seamlessly send/receive data without the
possibility of underrun. This process, a.k.a priming is used in the
example application provided with the Processor SDK. In this example two
frames are sent/received prior to submitting the application's audio
data to the McASP driver. The number of transfer requests to prime is
application dependent and some applications where there may be a lot of
delay between transfer requests, enough to cause an underrun, the
priming factor could be higher.

Application
------------

Examples & Unit tests
^^^^^^^^^^^^^^^^^^^^^

+------------------------------------+---------------------------+-----------------------+----------+-------------+
| Name                               || Description              | | Expected Results    |  SOCs    | Build type  |
+====================================+===========================+=======================+==========+=============+
| Audio_ExampleProject               | | Example                 | | Audio sent in to    | AM335X   | CCS Project |
|                                    |   demonstrating           |   the EVM being       | AM437x   |             |
|                                    |   sample McASP            |   played out via the  | AM572x   |             |
|                                    |   loopback using AIC31    |   stereo output of    | K2G      |             |
|                                    |   codec. Reference example|   the EVM             | OMAPL137 |             |
|                                    |   for developers          |                       | OMAPL138 |             |
+------------------------------------+---------------------------+-----------------------+----------+-------------+
| Audio_SMP_ExampleProject           | | Example                 | | Audio sent in to    | AM572x-  | CCS Project |
|                                    |   demonstrating           |   the EVM being       | EVM      |             |
|                                    |   sample McASP            |   played out via the  |          |             |
|                                    |   loopback using AIC31    |   stereo output of    |          |             |
|                                    |   codec. Reference example|   the EVM             |          |             |
|                                    |   for developers with SMP |                       |          |             |
|                                    |   enabled.(A15 core only) |                       |          |             |
+------------------------------------+---------------------------+-----------------------+----------+-------------+
| DeviceLoopback_ExampleProject      | | Example                 | | Digital ramp        | AM335X   | CCS Project |
|                                    |   demonstrating           |   pattern sent to     | AM437x   |             |
|                                    |   sample McASP device     |   McASP and getting   | AM571x   |             |
|                                    |   loopback .              |   looped back         | AM572x   |             |
|                                    |   Reference example       |   internally using    | AM574x   |             |
|                                    |   for developers          |   device loopback     | K2G      |             |
+------------------------------------+---------------------------+-----------------------+----------+-------------+
| AudioEQ_ExampleProject             | | Example                 | | Three band          | AM572x   | CCS Project |
|                                    |   demonstrating           |   Equalization of     | K2G      |             |
|                                    |   stereo audio            |   stereo channel      |          |             |
|                                    |   using biquad            |   filters with gain   |          |             |
|                                    |   filters . Reference     |   control using       |          |             |
|                                    |   design for              |   serial console      |          |             |
|                                    |   developers. **TI        |   inputs              |          |             |
|                                    |   Design Guide**:         |                       |          |             |
|                                    |   `TIDEP0069`_            |                       |          |             |
+------------------------------------+---------------------------+-----------------------+----------+-------------+
| DeviceLoopback_TestApp             | | Unit test               | | Digital ramp        | AM65x    | Makefile    |
|                                    |   demonstrating           |   pattern sent to     | J721e    |             |
|                                    |   sample McASP device     |   McASP and getting   |          |             |
|                                    |   loopback .              |   looped back         |          |             |
+------------------------------------+---------------------------+-----------------------+----------+-------------+
| DeviceLoopback_SMP_TestApp         | | Unit test               | | Digital ramp        | AM65x    | Makefile    |
|                                    |   demonstrating           |   pattern sent to     | J721e    |             |
|                                    |   sample McASP device     |   McASP and getting   |          |             |
|                                    |   loopback with SMP       |   looped back         |          |             |
|                                    |   enabled (A53 core only).|                       |          |             |
+------------------------------------+---------------------------+-----------------------+----------+-------------+
| DeviceLoopback_Regression_TestApp  | | Regression unit test    | | Menu Driven test    | AM65x    | Makefile    |
|                                    |   which tests various     |   sending digital ramp| J721e    |             |
|                                    |   features/configurations |   and getting looped  |          |             |
|                                    |   of the MCASP driver     |   back in various     |          |             |
|                                    |   This is a menu based    |   configurations      |          |             |
|                                    |   test application        |                       |          |             |
+------------------------------------+---------------------------+-----------------------+----------+-------------+

AudioEQ_ExampleProject
^^^^^^^^^^^^^^^^^^^^^^^

This example demonstrates stereo audio equalizer using biquad filters.

-  Filter default configurations are:

	-  Low_Fc       = 250.0   (Low Shelf cutoff frequency in Hz)
	-  High_Fc      = 1000.0  (High Shelf cutoff frequency in Hz)
	-  Sample_Rate  = 44100.0 (Number of samples per second)
	-  Q_Factor     = 0.707   (Bandwidth of frequency that will be affected by an equalizer)
	-  Default_Gain = 0.0     (increase or decrease in audio signal strength, expressed in dB)

-  The default Gain has been set to 0, in order to suppress any noise.
   The default Gain can be changed based on the test case requirement at, ti/drv/mcasp/example/src/audioEQ.c 'defaultGain = 0.0'.

-  The filter gains can be tuned from the uart console based on the test case requirement.

Sample log for the Audio Equalizer test is shown below

::

    ******** Audio EQ Demo ********
    NUM_BUFS=2
    PRIME_COUNT=2

    EDMA driver initialization successful.


    ======================================================

     Currently playing Audio effect Demo.
     Make sure a stereo input is connected to Line In and
     Connect an headphone or a speaker to LineOut.

    ======================================================

    Initialization complete. priming about to begin
     Demo currently shows 3 band equalization using shelving biquad filters
     * low band = 0Hz to 250Hz
     * mid band = 250Hz to 1000Hz,
     * high band = 1000Hz to 22000Hz
      All bands are boosted with a 8db Peak Gain


    Do you wish to keep the equalization ON ? (y or n)
    y

    ======================================================

    Press 0 and hit Enter to print current gain settings

    OR

    Select the Frequency Band to adjust the gain

    *   Press 1 for Low  and hit Enter
    *   Press 2 for High  and hit Enter
    *   Press 3 for Mid and hit Enter
    All other input will not have any effect

    ======================================================

    1

    Enter the value of gain in dB (Recommendation -8 to 8)
    4
    Gain updated


    Do you wish to keep the equalization ON ? (y or n)
    n
    Equalization OFF


    Do you wish turn ON the equalization? (y or n)

|

Building CCS projects based examples
----------------------------------------------

CCS Projects mentioned in the above table are built using pdkProjectCreate.bat/sh as explained in
`PDK Example and Test Project Creation <index_overview.html#pdk-example-and-test-project-creation>`__

Building MCASP Test applications via makefiles
----------------------------------------------

- MCASP Test applications and dependent libraries are built from the top level
  mcasp makefile

- Refer to the `Processor SDK RTOS Getting Started Guide
  <index_overview.html#setup-environment>`__  for details of how to setup the
  build environment. Once you have setup the build environment, issue the
  following commands:

   -  cd <pdk>/packages/

   -  To build: make mcasp

   -  To clean: make mcasp_clean

- Similarly, to build at the module level, issue the following commands for
  rebuilding :

   - cd <pdk>/packages/ti/drv/mcasp

   - To build: make all

   - To clean: make clean

.. _AudioEQ example: http://www.ti.com/tool/tidep0069

.. _TIDEP0069: http://www.ti.com/lit/ug/tidubq2/tidubq2.pdf


.. rubric:: Introduction
   :name: introduction-1

The sample application demonstrates the use of the MCASP driver for
audio playback. The application uses McASP LLD, and programs the AIC
codec on the EVM to send and receive the audio input. The audio received
from the AIC codec is loop back-ed at the application and sent back to
the AIC codec via MCASP LLD.

.. rubric:: Audio test setup
   :name: audio-test-setup

Please ensure the below before running the demo

#. Connect the EVM’s stereo audio input to the PC’s stereo audio output
#. Connect the EVM’s stereo audio output to powered speakers. Please
   make sure the amplification on the speakers is high enough for the
   audio output to be heard

.. rubric:: Building and running the Example
   :name: building-and-running-the-example

#. Run pdkProjectCreate to create the
   MCASP_Audio_<evm>_<device>ExampleProject
#. Load the project on to CCS and build the same.
#. Build the example
#. Load the MCASP_Audio_<evm>_<device>ExampleProject
#. Run the example

.. rubric:: Testing the example
   :name: testing-the-example

#. Play an audio file on the PC.
#. You should be able to hear the same audio on the speakers connected
   to the EVM. It is the PC’s audio output which is loop backed at the
   EVM’s MCASP example outputted to the speakers.

NOTE: Please make sure the speakers’ output volume is high enough for
the audio to be audible.

Additional References
---------------------

+-----------------------------------+----------------------------------------+
| **Document**                      | **Location**                           |
+-----------------------------------+----------------------------------------+
| API Reference Manual              | $(TI_PDK_INSTALL_DIR)\\packages\\ti    |
|                                   | \\drv\\mcasp\\docs\\doxygen\\html\\inde|
|                                   | x.html                                 |
+-----------------------------------+----------------------------------------+
| Release Notes                     | $(TI_PDK_INSTALL_DIR)\\packages\\ti    |
|                                   | \\drv\\mcasp\\docs\\ReleaseNotes_MCAS  |
|                                   | P_LLD.pdf                              |
+-----------------------------------+----------------------------------------+
| Software design Specification     | $(TI_PDK_INSTALL_DIR)\\packages\\ti    |
|                                   | \\drv\\mcasp\\docs\\MCASP_LLD_SDS.pdf  |
+-----------------------------------+----------------------------------------+
