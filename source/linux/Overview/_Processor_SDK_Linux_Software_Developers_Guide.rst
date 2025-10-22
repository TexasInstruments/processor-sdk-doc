Thank you for choosing to evaluate one of our `TI Processors
<https://www.ti.com/microcontrollers-mcus-processors/overview.html>`__. It is designed to quickly
provide the information you need most while evaluating a TI
microprocessor, specifically running one of the Software Architectures
available, embedded Linux. We are always striving to improve this
product. Please let us know if you have ideas or
suggestions at `E2E <https://e2e.ti.com/>`__.

.. ifconfig:: CONFIG_sdk in ('SITARA')

   .. list-table::
      :header-rows: 1

      * - Processor SDK Linux
        -
      * - :ref:`Getting Started Guide <overview-getting-started>` <-- **Start Here**
        - :ref:`How To Guides <how-to-guides>`
      * - :ref:`Supported Platforms and Versions <release-specific-supported-platforms-and-versions>`
        - :ref:`Building the SDK with Yocto <overview-building-the-sdk>`
      * - :ref:`Directory Structure Overview <overview-directory-structure>`
        - :ref:`GPLv3 Disclaimer <overview-gplv3-disclaimer>`
      * - :ref:`Release Notes <Release-note-label>`
        - :ref:`Migration Guide <release-specific-migration-guide>`
      * - :ref:`Technical Support <overview-technical-support>`
        - `Training <https://training.ti.com/processor-sdk-training-series>`__


.. ifconfig:: CONFIG_sdk in ('JACINTO','j7_foundational')

   .. list-table::
      :header-rows: 1

      * - Processor SDK Linux
        -
      * - :ref:`Getting Started Guide <overview-getting-started>` <-- **Start Here**
        - :ref:`Directory Structure Overview <overview-directory-structure>`
      * - :ref:`Release Notes <Release-note-label>`
        - :ref:`How To Guides <how-to-guides>`
      * - :ref:`Technical Support <overview-technical-support>`
        - :ref:`Building the SDK with Yocto <overview-building-the-sdk>`
      * - :ref:`Linux Software Stack <overview-software-stack>`
        - :ref:`GPLv3 Disclaimer <overview-gplv3-disclaimer>`
      * - `Training <https://training.ti.com/processor-sdk-training-series>`__
        -


.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family', 'AM57X_family')

   .. list-table::
      :header-rows: 1

      * - Foundational Components
        -
        -
        -
      * - :ref:`U-Boot <foundational-components-u-boot>`
        - :ref:`Kernel <foundational-components-kernel>`
        - :ref:`Filesystem <foundational-components-filesystem>`
        - :ref:`Tools <foundational-components-tools>`
      * - :ref:`Graphics & Display <foundational-components-graphics-and-display>`
        - :ref:`Examples, Demos <examples-and-demos>`
        - :ref:`PRU Subsystem <foundational-components-pru-subsystem>`
        -


.. ifconfig:: CONFIG_part_variant in ('AM64X')

   .. list-table::
      :header-rows: 1

      * - PRU-ICSS / PRU_ICSSG Protocols
        -
        -
        -
      * - :ref:`DUAL_EMAC <industrial-protocols-dual-emac>`
        - :ref:`HSR_PRP <industrial-protocols-hsr-prp>`
        - :ref:`PTP <industrial-protocols-ptp>`
        - :ref:`RSTP <industrial-protocols-rstp>`
      * - :ref:`CCLINK <industrial-protocols-cclink>`
        - :ref:`SORTE <industrial-protocols-sorte>`
        - :ref:`OPC/UA <industrial-protocols-opcua>`
        -

