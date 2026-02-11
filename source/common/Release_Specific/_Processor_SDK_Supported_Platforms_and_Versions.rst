.. _release-specific-supported-platforms-and-versions:

********************************
Supported Platforms and Versions
********************************

.. rubric:: Supported Host Operating Systems
   :name: supported-host-operating-systems

The following operating systems have been validated to work with our
SDK.

.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family')

    -  **Linux SDK**

    +---------------------------+-------------------------+
    | **Operating System**      | | **Version**           |
    +---------------------------+-------------------------+
    | Ubuntu                    | | 22.04 (64-bit)        |
    +---------------------------+-------------------------+

.. ifconfig:: CONFIG_sdk in ('JACINTO','j7_foundational')

    -  **Linux SDK**

    +---------------------------+-------------------------+
    | **Operating System**      | | **Version**           |
    +---------------------------+-------------------------+
    | Ubuntu                    | | 22.04 (64-bit)        |
    +---------------------------+-------------------------+

    -  **RTOS SDK**

    +---------------------------+-------------------------+
    | **Operating System**      | | **Version**           |
    +---------------------------+-------------------------+
    | Ubuntu                    | | 22.04 (64-bit)        |
    +---------------------------+-------------------------+

|

.. rubric:: Supported Platforms and EVMs
   :name: supported-platforms-and-evms

The following platforms and EVMs are supported with Processor SDK.

.. ifconfig:: CONFIG_part_family in ('AM335X_family')

    +--------------------------------------+--------------------------------------+----------+--------------------------------------------+----------------+
    |**Platform**                          |**EVM**                               |**Tested  |**Document**                                |**Processor SDK |
    |                                      |                                      |Version** |                                            |Linux**         |
    +--------------------------------------+--------------------------------------+----------+--------------------------------------------+----------------+
    |`AM335x <http://www.ti.com/lsds/ti/   |`AM335x EVM                           | 1.6A     |`Hardware User's Guide <http://             | X              |
    |processors/sitara/arm_cortex-a8/      |<http://www.ti.com/tool/              |          |processors.wiki.ti.com/index.php/AM335x_    |                |
    |am335x/overview.page>`__              |tmdxevm3358>`__                       |          |General_Purpose_EVM_HW_User_Guide>`__       |                |
    |                                      +--------------------------------------+----------+--------------------------------------------+----------------+
    |                                      |`AM335x SK                            | 1.2      |`Hardware User's Guide <http://             | X              |
    |                                      |<http://www.ti.com/tool/              |          |processors.wiki.ti.com/index.php/           |                |
    |                                      |tmdssk3358>`__                        |          |AM335xStarterKitHardwareUsersGuide>`__      |                |
    |                                      +--------------------------------------+----------+--------------------------------------------+----------------+
    |                                      |`BeagleBone Black                     | B6       |`Hardware User's Guide <https://github.com/ | X              |
    |                                      |<https://www.beagleboard.org/         |          |CircuitCo/BeagleBone-Black/blob/            |                |
    |                                      |boards/beaglebone-black>`__           |          |master/BBB_SRM.pdf?raw=true>`__             |                |
    |                                      +--------------------------------------+----------+--------------------------------------------+----------------+
    |                                      |`BeagleBone Grren Eco                 | 1.0      |`Hardware User's Guide <hhttps://www.ti.com/| X              |
    |                                      |<https://www.ti.com/tool/             |          |lit/ug/slvudi2/slvudi2.pdf>`__              |                |
    |                                      |BEAGL-BONE-GRN-ECO>`__                |          |                                            |                |
    +--------------------------------------+--------------------------------------+----------+--------------------------------------------+----------------+

.. ifconfig:: CONFIG_part_family in ('AM437X_family')

    +--------------------------------------+--------------------------------------+----------+--------------------------------------------+----------------+
    |**Platform**                          |**EVM**                               |**Tested  |**Document**                                |**Processor SDK |
    |                                      |                                      |Version** |                                            |Linux**         |
    +--------------------------------------+--------------------------------------+----------+--------------------------------------------+----------------+
    |`AM437x <http://www.ti.com/lsds/ti/   |`AM437x EVM                           | 1.5B     |`Hardware User's Guide <http://             | X              |
    |processors/sitara/arm_cortex-a9/      |<http://www.ti.com/tool/              |          |processors.wiki.ti.com/index.php/AM437x_    |                |
    |am437x/overview.page>`__              |TMDXEVM437X>`__                       |          |General_Purpose_EVM_HW_User_Guide>`__       |                |
    |                                      +--------------------------------------+----------+--------------------------------------------+----------------+
    |                                      |`AM437x SK                            | 1.1A     |`Hardware User's Guide <http://             | X              |
    |                                      |<http://www.ti.com/tool/              |          |www.ti.com/lit/pdf/spruhw8>`__              |                |
    |                                      |TMDXSK437X>`__                        |          |                                            |                |
    +--------------------------------------+--------------------------------------+----------+--------------------------------------------+----------------+

.. ifconfig:: CONFIG_part_family in ('J7_family')

    +--------------+-----------+-----------+-----------------------+-------------------+------------------+
    | **Platform** | **EVM**   | **Tested  | **Document**          | **Processor SDK   | **Processor SDK  |
    |              |           | Version** |                       | Linux Automotive**| RTOS Automotive**|
    +--------------+-----------+-----------+-----------------------+-------------------+------------------+
    | J721e/DRA829 | J721e EVM | Alpha     | Hardware User's Guide | Y                 | Y                |
    +--------------+-----------+-----------+-----------------------+-------------------+------------------+
    | J721e/DRA829 | J721e EVM | Beta      | Hardware User's Guide | Y                 | Y                |
    +--------------+-----------+-----------+-----------------------+-------------------+------------------+
    | J7200/DRA821 | J7200 EVM | Alpha     | Hardware User's Guide | Y                 | Y                |
    +--------------+-----------+-----------+-----------------------+-------------------+------------------+

.. ifconfig:: CONFIG_part_family in ('AM57X_family')

    +--------------+------------+-----------+-------------------+------------------+
    | **Platform** | **EVM**    | **Tested  | **PSDK Linux**    | **PSDK RTOS**    |
    |              |            | Version** |                   |                  |
    +--------------+------------+-----------+-------------------+------------------+
    | AM57X        | AM572x EVM | A3        | Y                 | Y                |
    +--------------+------------+-----------+-------------------+------------------+
    | AM57X        | AM572x EVM | 1.3A      | Y                 | Y                |
    +--------------+------------+-----------+-------------------+------------------+
    | AM57         | AM571x IDK | 1.3A      | Y                 | Y                |
    +--------------+------------+-----------+-------------------+------------------+
    | AM57         | AM574x IDK | 1.0A      | Y                 | Y                |
    +--------------+------------+-----------+-------------------+------------------+

    Document reference:

    +------------------------------------------------------+----------------------------------------------------------------+
    | **EVM**                                              | **Document**                                                   |
    +------------------------------------------------------+----------------------------------------------------------------+
    | `AM572x EVM <https://www.ti.com/tool/TMDSEVM572X>`__ | `Hardware User's Guide <https://www.ti.com/lit/pdf/spruig1>`__ |
    +------------------------------------------------------+----------------------------------------------------------------+
    | `AM572x IDK <https://www.ti.com/tool/TMDXIDK5728>`__ | `Hardware User's Guide <https://www.ti.com/lit/pdf/sprui64>`__ |
    +------------------------------------------------------+----------------------------------------------------------------+
    | `AM571x IDK <https://www.ti.com/tool/tmdxidk5718>`__ | `Hardware User's Guide <https://www.ti.com/lit/pdf/sprui97>`__ |
    +------------------------------------------------------+----------------------------------------------------------------+
    | `AM574x IDK <https://www.ti.com/tool/TMDSIDK574>`__  | `Hardware User's Guide <https://www.ti.com/lit/pdf/spruij9>`__ |
    +------------------------------------------------------+----------------------------------------------------------------+
