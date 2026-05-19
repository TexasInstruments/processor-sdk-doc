.. _release-specific-supported-platforms-and-versions:

************************************
Supported Platforms and Versions
************************************

.. rubric:: Supported Host Operating Systems

The following operating systems have been validated to work with our
SDK.

-  **Linux SDK**

+---------------------------+-------------------------+
| **Operating System**      | | **Version**           |
+---------------------------+-------------------------+
| Ubuntu                    | | 22.04 (64-bit)        |
+---------------------------+-------------------------+

|

.. rubric:: Supported Platforms and EVMs

The following platforms and EVMs are supported with Processor SDK.

.. ifconfig:: CONFIG_sdk in ('JACINTO')

   .. ifconfig:: CONFIG_part_variant in ('J722S')

      +--------------+------------+-----------+-----------------------+-------------------+------------------+
      | **Platform** | **EVM**    | **Tested  | **Document**          | **Processor SDK   | **Processor SDK  |
      |              |            | Version** |                       | Linux**           | RTOS**           |
      +--------------+------------+-----------+-----------------------+-------------------+------------------+
      |     J722S    | J722S EVM  |   Alpha   | Hardware User's Guide | Y                 |                  |
      +--------------+------------+-----------+-----------------------+-------------------+------------------+
