.. _release-specific-supported-platforms-and-versions:

************************************
Supported Platforms and Versions
************************************

.. rubric:: Supported Host Operating Systems
   :name: supported-host-operating-systems

The following operating systems have been validated to work with our
SDK.

.. ifconfig:: CONFIG_sdk in ('PSDKL')

    -  **Linux SDK**

    +---------------------------+-------------------------+
    | **Operating System**      | | **Version**           |
    +---------------------------+-------------------------+
    | Ubuntu                    | | 22.04 (64-bit)        |
    +---------------------------+-------------------------+

|

.. rubric:: Supported Platforms and EVMs
   :name: supported-platforms-and-evms

The following platforms and SKs are supported with Processor SDK.

.. ifconfig:: CONFIG_part_family in ('J7_family')

    +--------------+-----------+-----------+-----------------------+-------------------+
    | **Platform** | **EVM**   | **Tested  | **Document**          | **Processor SDK   |
    |              |           | Version** |                       | Linux Automotive**|
    +--------------+-----------+-----------+-----------------------+-------------------+
    | J721e/DRA829 | J721e EVM | Alpha     | Hardware User's Guide | Y                 |
    +--------------+-----------+-----------+-----------------------+-------------------+
