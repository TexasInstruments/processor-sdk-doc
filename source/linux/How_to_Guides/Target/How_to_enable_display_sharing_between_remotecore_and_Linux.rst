.. _display-sharing-between-remotecore-and-linux:

How to enable display sharing between remote core and Linux
===========================================================

Introduction
------------

The AM62P SoC supports display sharing where multiple processing cores can simultaneously utilize display resources as desrcibed in `DSS driver documentation <../../Foundational_Components/Kernel/Kernel_Drivers/Display/DSS7.html#supported-features>`__

The DSS partitioning scheme can be tailored based on the end-use case requirement and the display sharing properties can be set accordingly as demonstrated in below examples :

Examples
--------

Linux owning one video plane
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. Image:: /images/DSS7_linux_own_one_pipe.png
     :align: center

+----------+----------+------------+
| Resource | Linux    | Remote Core|
+==========+==========+============+
| Register | Common1  | Common     |
| space    |          |            |
+----------+----------+------------+
| Video    | VP1      | VP1        |
| port     | (shared) | (owned)    |
+----------+----------+------------+
| Video    | Vid      | Vidl       |
| Pipeline |          |            |
+----------+----------+------------+
| Zorder   | 0        | 1          |
|          |          |            |
+----------+----------+------------+

For this scenario where Linux owns one video pipeline and remote core controls rest of the display resources, user can update the display hardware device tree node as shown below :

.. code-block:: text

        &dss0 {
                ti,dss-shared-mode;
                ti,dss-shared-mode-vp = "vp1";
                ti,dss-shared-mode-vp-owned = <0>;
                ti,dss-shared-mode-common = "common1";
                ti,dss-shared-mode-planes = "vid";
                ti,dss-shared-mode-plane-zorder = <0>;
                interrupts = <GIC_SPI 85 IRQ_TYPE_LEVEL_HIGH>;
        };

This scheme is useful for scenario where both Linux and remote core want to display over same peripheral using different video planes.

.. note::
   Here it is assumed that remote core is running firmware which honors above display partitioning scheme by programming video port using a separate register region i.e. "common" and using separate video pipeline i.e. vidl.

.. note::
   There is an out of box example available which uses this configuration to demonstrate display sharing between Linux and RTOS using display supported RTOS firmware and Linux devicetree overlay file `k3-am62p5-sk-dss-shared-mode.dtbo <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-am62p5-sk-dss-shared-mode.dtso?h=09.01.00.008>`_

   For more details please refer :ref:`display-cluster-user-guide`

Linux owning one full pipeline
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. Image:: /images/DSS7_linux_own_one_vp.png
     :align: center

+----------+----------+------------+
| Resource | Linux    | Remote Core|
+==========+==========+============+
| Register | Common1  | Common     |
| space    |          |            |
+----------+----------+------------+
| Video    | VP1      | VP2        |
| port     | (Owned)  | (Owned)    |
+----------+----------+------------+
| Video    | Vid      | Vidl       |
| Pipeline |          |            |
+----------+----------+------------+
| Zorder   | 0        | 1          |
|          |          |            |
+----------+----------+------------+

For this scenario where Linux owns one full display pipeline involving a video port, overlay manager and a video pipeline with remote core also controlling full display pipeline with albeit using a separate video port, below device tree node configuration can be used :

.. code-block:: text

        &dss0 {
                ti,dss-shared-mode;
                ti,dss-shared-mode-vp = "vp1";
                ti,dss-shared-mode-vp-owned = <1>;
                ti,dss-shared-mode-common = "common1";
                ti,dss-shared-mode-planes = "vid";
                ti,dss-shared-mode-plane-zorder = <0>;
                interrupts = <GIC_SPI 85 IRQ_TYPE_LEVEL_HIGH>;
        };

.. note::
   Here it is assumed that remote core is running a custom firmware which honors above display partitioning scheme by programming a separate video port using a separate register region i.e. "common" and using separate video pipeline i.e. vidl.
