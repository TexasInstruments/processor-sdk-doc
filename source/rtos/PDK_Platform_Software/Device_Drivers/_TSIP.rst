.. include:: <isonum.txt>

.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_TSIP

Overview
--------

Introduction
^^^^^^^^^^^^

The TSIP is a multi-link serial interface consisting of a maximum of
eight transmit data signals (or links), eight receive data signals (or
links), two frame sync input signals, and two serial clock inputs.
Internally the TSIP offers multiple channels of timeslot data management
and multi-channel DMA capability that allow individual timeslots to be
selectively processed.

The module can be configured to use the frame sync signals and the
serial clocks as redundant sources for all transmit and receive data
signals, or one frame sync and serial clock for transmit and the second
frame sync and clock for receive. The standard serial data rate for each
TSIP transmit and receive data signal is 8.192 Mbps. The standard frame
sync is a one or more bit wide pulse that occurs once every 125 |micro|\ s or a
minimum of one serial clock period every 1024 serial clocks.

At the standard rate and default configuration there are eight transmit
and eight receive links that are active. Each serial interface link
supports up to 128 8-bit timeslots. This corresponds to an H-MVIP or
H.110 serial data rate interface. The serial interface clock frequency
can be either 16.384 MHz (default) or 8.192 MHz. The data rate for the
serial interface links can also be set to 16.384 Mbps or 32.768 Mbps.
The maximum number of active serial links is reduced to four and two,
respectively, in these configurations. The serial interface clock
frequency can be either 32.768 MHz or 16.384 MHz for 16.384 Mbps serial
links, and 65.536 MHz or 32.768 MHz for 32.768 Mbps serial links.
Maximum occupation of the serial interface links for the entire TSIP is
1024 transmit and receive timeslots in all configurations.

User Interface
--------------

Driver Configuration
^^^^^^^^^^^^^^^^^^^^^

TSIP configuration involves configurations for desired stagger phase of
a TSIP timeout, using Tsip_configPhase() API. For details about
individual fields of this structure, see the Doxygen help by opening
PDK_INSTALL_DIR\\Packages\\ti\\drv\\TSIP\\docs\\doxygen\\html\\index.html.

APIs
^^^^^

API reference for application:

::

    #include <ti/drv/tsip/tsip.h>

Application
------------

Examples
^^^^^^^^

+-----------------------+-----------------------+-----------------------+
| Name                  | Description           | Expected Results      |
+=======================+=======================+=======================+
| tsip_Example          | | Example             | | User observes the   |
| application           |   demonstrating       |   output printed over |
|                       |   *sample tsip* test. |   the CCS console     |
|                       |   Reference example   |                       |
|                       |   for developers      |                       |
+-----------------------+-----------------------+-----------------------+
| tsip_UnitTestApplicat | | Unit Test           | | User observes the   |
| ion                   |   application to test |   output printed over |
|                       |   all APIs            |   the CCS console     |
+-----------------------+-----------------------+-----------------------+

Additional References
---------------------

+-----------------------------------+-----------------------------------------+
| **Document**                      | **Location**                            |
+-----------------------------------+-----------------------------------------+
| API Reference Manual              | $(TI_PDK_INSTALL_DIR)\\packages\\ti     |
|                                   | \\drv\\TSIP\\docs\\doxygen\\html\\index |
|                                   | .html                                   |
+-----------------------------------+-----------------------------------------+
| Release Notes                     | $(TI_PDK_INSTALL_DIR)\\packages\\ti     |
|                                   | \\drv\\TSIP\\docs\ReleaseNotes_TSIP.    |
|                                   | pdf                                     |
+-----------------------------------+-----------------------------------------+

|

