Processor SDK RTOS
==================

Processor SDK RTOS is a companion SDK to Processor SDK Linux on
the |__PART_FAMILY_NAME__| family of devices.  In order to use some SoC
features from the core running Linux, one needs to download and install the PSDK RTOS package.

.. ifconfig:: CONFIG_part_variant in ('J721E')

    Refer to the  `PSDK RTOS top level user guide online
    <http://software-dl.ti.com/jacinto7/esd/processor-sdk-rtos-jacinto7/latest/exports/docs/psdk_rtos/docs/user_guide/index.html>`__
    or after downloading the installer at ${PSDK_RTOS_PATH}/index.html, for more details.

.. ifconfig:: CONFIG_part_variant in ('J7200')

    Refer to the  `PSDK RTOS top level user guide online
    <https://software-dl.ti.com/jacinto7/esd/processor-sdk-rtos-j7200/latest/exports/docs/psdk_rtos/docs/user_guide/index.html>`__
    or after downloading the installer at ${PSDK_RTOS_PATH}/index.html, for more details.

.. ifconfig:: CONFIG_part_variant in ('J721E')

    Features provided by PSDK RTOS that can be accessed from Linux A72 core on
    Jacinto 7 family of devices are listed below:

    -   TIDL on C7x
    -   Vision pre/post processing functions on C6x
    -   Vision HW accelerators (VPAC/DMPAC) on R5F
    -   CSI2RX on R5F
    -   Remote display on R5F
    -   Ethernet switch on R5F
    -   MCU/AutoSAR MCAL on R5F
    -   OpenVX on Linux A72 and RTOS C6x, C7x, R5F
    -   Deep learning demos on Linux A72
    -   Surround view demos on Linux A72

.. ifconfig:: CONFIG_part_variant in ('J7200')

    Features provided by PSDK RTOS that can be accessed from Linux A72 core on
    Jacinto 7 family of devices are listed below:

    -   Ethernet switch on R5F
    -   MCU/AutoSAR MCAL on R5F

.. important::
    This package is NOT included in PSDK Linux installer and needs to be downloaded separately.

