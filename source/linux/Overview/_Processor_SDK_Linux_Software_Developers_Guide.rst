Thank you for choosing to evaluate one of our `TI Processors
<https://www.ti.com/microcontrollers-mcus-processors/overview.html>`__. It is designed to quickly
provide the information you need most while evaluating a TI
microprocessor, specifically running one of the Software Architectures
available, embedded Linux. We are always striving to improve this
product. Please let us know if you have ideas or
suggestions at `E2E <https://e2e.ti.com/>`__.

.. ifconfig:: CONFIG_sdk in ('SITARA')

    +------------------------------------------------------------------------+-------------------------------------------------------------------------------+
    | **Processor SDK Linux**                                                                                                                                |
    +========================================================================+===============================================================================+
    | |___Getting Started Guide___|  <-- **Start Here**                      | |___How To Guides___|                                                         |
    +------------------------------------------------------------------------+-------------------------------------------------------------------------------+
    | |___Supported Platforms and Versions___|                               | |___Building the SDK___|                                                      |
    +------------------------------------------------------------------------+-------------------------------------------------------------------------------+
    | |___Directory Structure Overview___|                                   | |___GPLv3 Disclaimer___|                                                      |
    +------------------------------------------------------------------------+-------------------------------------------------------------------------------+
    | |___Release Notes___|                                                  | |___Migration Guide___|                                                       |
    +------------------------------------------------------------------------+-------------------------------------------------------------------------------+
    | |___Technical Support___|                                              | `Training <https://training.ti.com/processor-sdk-training-series>`__          |
    +------------------------------------------------------------------------+-------------------------------------------------------------------------------+

    .. |___Getting Started Guide___| replace:: :ref:`Getting Started Guide <overview-getting-started>`
    .. |___Directory Structure Overview___| replace:: :ref:`Directory Structure Overview <overview-directory-structure>`
    .. |___Building the SDK___| replace:: :ref:`Building the SDK with Yocto <overview-building-the-sdk>`
    .. |___GPLv3 Disclaimer___| replace:: :ref:`GPLv3 Disclaimer <overview-gplv3-disclaimer>`
    .. |___Technical Support___| replace:: :ref:`Technical Support <overview-technical-support>`
    .. |___Supported Platforms and Versions___| replace:: :ref:`Supported Platforms and Versions <release-specific-supported-platforms-and-versions>`
    .. |___Migration Guide___| replace:: :ref:`Migration Guide <release-specific-migration-guide>`
    .. |___How To Guides___| replace:: :ref:`How To Guides <how-to-guides>`
    .. |___Release Notes___| replace:: :ref:`Release Notes <Release-note-label>`


.. ifconfig:: CONFIG_sdk in ('JACINTO','j7_foundational')

    +-----------------------------------------------------------------------+----------------------------------------------------------------------+
    |           **Processor SDK Linux**                                     |                                                                      |
    +=======================================================================+======================================================================+
    | |__Getting Started Guide__|  <-- **Start Here**                       | |__Directory Structure Overview__|                                   |
    +-----------------------------------------------------------------------+----------------------------------------------------------------------+
    | |__Release Notes__|                                                   | |__How To Guides__|                                                  |
    +-----------------------------------------------------------------------+----------------------------------------------------------------------+
    | |__Technical Support__|                                               | |__Building the SDK__|                                               |
    +-----------------------------------------------------------------------+----------------------------------------------------------------------+
    | |__Linux Software Stack__|                                            | |__GPLv3 Disclaimer__|                                               |
    +-----------------------------------------------------------------------+----------------------------------------------------------------------+
    | `Training <https://training.ti.com/processor-sdk-training-series>`__  |                                                                      |
    +-----------------------------------------------------------------------+----------------------------------------------------------------------+

    .. |__Getting Started Guide__| replace:: :ref:`Getting Started Guide <overview-getting-started>`
    .. |__Directory Structure Overview__| replace:: :ref:`Directory Structure Overview <overview-directory-structure>`
    .. |__Building the SDK__| replace:: :ref:`Building the SDK with Yocto <overview-building-the-sdk>`
    .. |__GPLv3 Disclaimer__| replace:: :ref:`GPLv3 Disclaimer <overview-gplv3-disclaimer>`
    .. |__Technical Support__| replace:: :ref:`Technical Support <overview-technical-support>`
    .. |__Supported Platforms and Versions__| replace:: :ref:`Supported Platforms and Versions <release-specific-supported-platforms-and-versions>`
    .. |__Linux Software Stack__| replace:: :ref:`Linux Software Stack <overview-software-stack>`
    .. |__Migration Guide__| replace:: :ref:`Migration Guide <release-specific-migration-guide>`
    .. |__How To Guides__| replace:: :ref:`How To Guides <how-to-guides>`
    .. |__Release Notes__| replace:: :ref:`Release Notes <Release-note-label>`


.. ifconfig:: CONFIG_part_family in ('General_family')

    +------------------+------------------------+----------------------------+----------------------------+
    | **Foundational Components** (more information on each piece of the distribution)                    |
    +==================+========================+============================+============================+
    | |__U-Boot__|     | |__Boot Monitor__|     | |__Kernel__|               | |__Filesystem__|           |
    +------------------+------------------------+----------------------------+----------------------------+
    | |__Tools__|      | |__OpenCL__|           | |__OpenCV__|               | |__Graphics & Display__|   |
    +------------------+------------------------+----------------------------+----------------------------+
    | |__Multimedia__| | |__Examples & Demos__| | |__PRU Subsystem__|        | |__Virtualization__|       |
    +------------------+------------------------+----------------------------+----------------------------+
    | |__IPC__|        | |__OpenVX__|           | |__CMEM__|                 | |__Machine Learning__|     |
    +------------------+------------------------+----------------------------+----------------------------+
    | |__ATF__|        | |__OPTEE__|            |                            |                            |
    +------------------+------------------------+----------------------------+----------------------------+

    .. |__Boot Monitor__| replace:: :ref:`Boot Monitor  <foundational-components-boot-monitor>`
    .. |__OpenCL__| replace:: `OpenCL <http://downloads.ti.com/mctools/esd/docs/opencl/index.html>`__
    .. |__OpenCV__| replace:: :ref:`OpenCV <foundational-components-opencv>`
    .. |__Multimedia__| replace:: :ref:`Multimedia <foundational-components-multimedia>`
    .. |__Virtualization__| replace:: :ref:`Virtualization <foundational-components-virtualization>`
    .. |__IPC__| replace:: :ref:`IPC <foundational-components-ipc>`
    .. |__OpenVX__| replace:: :ref:`OpenVX <foundational-components-openvx>`
    .. |__CMEM__| replace:: :ref:`CMEM <foundational-components-cmem>`
    .. |__Machine Learning__| replace:: :ref:`Machine Learning <foundational-components-machine-learning>`
    .. |__ATF__| replace:: :ref:`ATF <foundational-components-atf>`
    .. |__OPTEE__| replace:: :ref:`OPTEE <foundational-components-optee>`


.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family', 'AM57X_family')

    +--------------------------+------------------------+----------------------------+-------------+
    | **Foundational Components** (more information on each piece of the distribution)             |
    +==========================+========================+============================+=============+
    | |__U-Boot__|             | |__Kernel__|           | |__Filesystem__|           | |__Tools__| |
    +--------------------------+------------------------+----------------------------+-------------+
    | |__Graphics & Display__| | |__Examples & Demos__| | |__PRU Subsystem__|        |             |
    +--------------------------+------------------------+----------------------------+-------------+

    .. |__U-Boot__| replace:: :ref:`U-Boot <foundational-components-u-boot>`
    .. |__Kernel__| replace:: :ref:`Kernel <foundational-components-kernel>`
    .. |__Filesystem__| replace:: :ref:`Filesystem <foundational-components-filesystem>`
    .. |__Tools__| replace:: :ref:`Tools <foundational-components-tools>`
    .. |__Graphics & Display__| replace:: :ref:`Graphics & Display <foundational-components-graphics-and-display>`
    .. |__Examples & Demos__| replace:: :ref:`Examples, Demos <examples-and-demos>`
    .. |__PRU Subsystem__| replace:: :ref:`PRU Subsystem <foundational-components-pru-subsystem>`


.. ifconfig:: CONFIG_sdk in ('SITARA')

    .. ifconfig:: CONFIG_part_variant not in ('AM62LX', 'AM62X', 'AM62AX', 'AM62PX', 'AM335X', 'AM437X', 'AM65X')

        +-----------------+------------------------+------------------+-----------------------------------+
        | **PRU-ICSS / PRU_ICSSG Protocols** (more information on each piece of the distribution)         |
        +=================+========================+==================+===================================+
        | |__DUAL_EMAC__| | |__HSR_PRP__|          | |__PTP__|        | |__RSTP__|                        |
        +-----------------+------------------------+------------------+-----------------------------------+
        | |__CCLINK__|    | |__SORTE__|            | |__OPCUA__|      |                                   |
        +-----------------+------------------------+------------------+-----------------------------------+

        .. |__DUAL_EMAC__| replace:: :ref:`DUAL_EMAC <industrial-protocols-dual-emac>`
        .. |__HSR_PRP__| replace:: :ref:`HSR_PRP <industrial-protocols-hsr-prp>`
        .. |__PTP__| replace:: :ref:`PTP <industrial-protocols-ptp>`
        .. |__RSTP__| replace:: :ref:`RSTP <industrial-protocols-rstp>`
        .. |__CCLINK__| replace:: :ref:`CCLINK <industrial-protocols-cclink>`
        .. |__SORTE__| replace:: :ref:`SORTE <industrial-protocols-sorte>`
        .. |__OPCUA__| replace:: :ref:`OPC/UA <industrial-protocols-opcua>`
