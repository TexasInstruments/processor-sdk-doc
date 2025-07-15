K3 Resource Partitioning Tool
=============================

The Keystone3 Resource Partitioning tool partitions various system
resources among different software components in a multi-core SoC.
Texas Instruments developed this tool based on their SysConfig tool.

System integrators typically use this tool to assign **resources**
to different software parts. These resources include Direct Memory
Access (DMA) channels, rings, proxies, interrupts, and more.

The tool also supports Quality of Service (QoS) and firewall
settings to help partition **peripheral devices** for different
software components.

Getting started
---------------

The K3 Resource Partitioning Tool is available on the TI Developer Zone
as K3 Resource Configuration. You can use the tool online and locally
within the SDK.

Accessing the tool online
^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   We recommend using this method.

To access the tool, follow these steps:

1. **Open the Tool**: Go to https://dev.ti.com/sysconfig/?product=K3-RESOURCE-CONFIGURATION
   to open the tool. Log in to your TI account if needed.

   .. figure:: /images/k3_resource_config_startpage.png
      :scale: 75%
      :align: center

2. **Select Your Device**: Choose your device from the list.

   .. figure:: /images/k3_resource_config_device_selection.png
      :scale: 75%
      :align: center

3. **Start Configuring Resources**: Click ``Latest Baseline Design`` to set
   up resources using the latest baseline for your device. Or pick a
   Processor SDK version-specific Baseline Design to match a specific SDK
   release.

   .. figure:: /images/k3_resource_config_device_selected.png
      :scale: 75%
      :align: center

   .. figure:: /images/am62px_respart_tool_main.png
      :scale: 70%
      :align: center

Accessing the tool locally
^^^^^^^^^^^^^^^^^^^^^^^^^^

To use the tool locally, follow these instructions:

1. **Download and Install SysConfig**: Download and install the latest
   SysConfig tool from the `SysConfig release download link
   <https://www.ti.com/tool/download/SYSCONFIG>`__
2. **Locate the Tool**: Find the **k3-respart-tool** folder in your SDK.
3. **Open SysConfig GUI**: Start the SysConfig. In the GUI, select the
   **software product** by browsing to your **k3-respart-tool** location.

   .. figure:: /images/k3_resource_config_product_selection_local.png
      :scale: 75%
      :align: center

   .. figure:: /images/k3_resource_config_product_selected_local.png
      :scale: 75%
      :align: center

4. **Select Your Device**: Pick your target device from the list.

   .. figure:: /images/k3_resource_config_device_selection_local.png
      :scale: 75%
      :align: center

5. **Start Configuring Resources**: Click ``Latest Baseline Design`` to set
   up resources using the latest baseline for your device. Or pick a
   Processor SDK version-specific Baseline Design to match a specific SDK
   release.

   .. figure:: /images/k3_resource_config_device_selected_local.png
      :scale: 75%
      :align: center

   .. figure:: /images/am62px_respart_tool_main_local.png
      :scale: 70%
      :align: center

Usage
-----

After the design loads, you can use the Resource Partitioning, Bandwidth (BW)
Limiter, and Quality of Service (QoS) Configuration modules.

Resource partitioning
^^^^^^^^^^^^^^^^^^^^^

The resource partitioning module divides resources among different hosts in
the system. A **host** is a software part that communicates with **System
Firmware** (SYSFW) using its own context. The module create a **Resource
Management Board Configuration** file, which defines the resource partitioning.
The boot loader passes this file to System Firmware during boot.

In the left pane of GUI, you see the available hosts and what resources each
one has. There are different resource **groups**, where you set the required
**count** for each resource. The tool assigns resources based on the counts
you set for all hosts. Besides allocating resources, you can configure
different **host capabilities**. Click the **?** next to a host's name to read
the detailed documentation for that host module.

.. _resource_totals:

Review resource allocation
^^^^^^^^^^^^^^^^^^^^^^^^^^

You can check the current resource split at any time. Select the **Resource
Allocation Table** from the three dots at the top right of the tool. This
section shows an HTML table of hosts and their allocated resources.
Each row shows a certain resource. Each column shows the resource ranges
assigned to a certain host.

Resource totals
^^^^^^^^^^^^^^^

The last column, labeled ``ALL``, represents the total number of
resources available to all hosts. This column is for the ``HOST_ID_ALL``
value.

Certain hardware have some resources, such as ``GPIO interrupts`` and ``Virtual
interrupts``, tied to them. For example, ``DMASS Interrupt Aggregator
Virtual Interrupts`` connect directly to specific cores, so those interrupts
cannot go to just any core. The tool only assign resources in ways that match
the hardware.

The tool does not adjust the ``ALL`` column for host-specific resources.

Bandwidth limiters configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This BW limiters configuration module helps you set up rate limiters for the SoC.
Each rate limiter connects to a source VBUSM interface. You can set limits for
reads, writes, and outstanding transactions. You can set these limits separately.

In the GUI, pick a device and turn on bandwidth or transaction limits as needed.
The tool creates an address-value pair data structure in the **<soc>_qos_uboot.c**
file. Software (usually the boot loader) uses this file to set the limits in the
correct registers.

Quality of service configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This QoS configuration module helps you set up Central Bus Architecture Subsystem
(CBASS) QoS endpoints. QoS configuration includes two types of parameters. QoS
settings include parameters that tune DMA performance in the interconnect and set
up Input/Output Memory Management Unit (IOMMU) paths for masters. Each device can
use different Channel IDs for DMA requests. You can set a unique QoS for each channel.

In the GUI, pick a device, endpoints, and channels to set their QoS. You can add
more than one QoS module for the same device provided that endpoints and channels
do not overlap. The tool creates a simple address-value pair data structure in the
**<soc>_qos_uboot.c** file. Software (such as the boot loader) uses this file to set
all QoS settings.

Firewall configuration
^^^^^^^^^^^^^^^^^^^^^^

.. note::

   Currently u-boot cannot use the generated firewall files directly.
   The firewall support in u-boot is not added officially.

The Firewall configuration module creates the data you need to control firewalls.
Firewalls control a host's access to a peripheral. Each firewall has a region.
Pick a firewall and set the address range for the rules. Each region can have up
to three permission slots. Each slot takes a name, Priv ID, and permissions. Many
CPUs can share a Priv ID, so one slot can cover several CPUs. These slots decide
what each CPU can do based on security level, privilege, and transaction type. For
example, allow secure reads and writes but block insecure writes from A72 to
Multimedia Card (MMC).

By default, the tool sets the start and end addresses in the region, but you can
set a custom region if needed. You can also pick a host's name and the tool fills
in the Priv ID. With this data, the tool creates an array of Texas Instruments
System Controller Interface (TISCI) message data to send to SYSFW for firewall
setup.

Generating output files
^^^^^^^^^^^^^^^^^^^^^^^

The tool creates different files with RM board config data, QoS settings, and
firewall settings. Here is how you use these files:

.. list-table::
   :header-rows: 1
   :widths: 20 15 30 35

   * - Filename
     - Used by
     - Output destination
     - Comments
   * - :file:`rm-cfg.c`
     - k3-image-gen
     - :file:`soc/<soc>/<profile>/`
     - e.g. - :file:`k3-image-gen/soc/j721e/evm/rm-cfg.c`
   * - :file:`sciclient_defaultBoardcfg_rm.c`
     - PDK sciclient
     - :file:`packages/ti/drv/sciclient/soc/V<X>/`
     - e.g. - :file:`pdk/packages/ti/drv/sciclient/soc/V1/sciclient_defaultBoardcfg_rm.c`
   * - :file:`sciclient_defaultBoardcfg_rm_mcusdk.c`
     - MCU+ SDK sciclient
     - :file:`source/drivers/sciclient/sciclient_default_boardcfg/am62x/`
     - e.g. - :file:`mcu_plus_sdk/source/drivers/sciclient/sciclient_default_boardcfg/am62x/sciclient_defaultBoardcfg_rm.c` (Drop :file:`_mcusdk` from filename)
   * - :file:`sciclient_defaultBoardcfg_tifs_rm.c`
     - PDK sciclient
     - :file:`packages/ti/drv/sciclient/soc/V<X>/`
     - e.g. - :file:`pdk/packages/ti/drv/sciclient/soc/V2/sciclient_defaultBoardcfg_tifs_rm.c`
   * - :file:`tifs-rm-cfg.c`
     - k3-image-gen
     - :file:`soc/<soc>/<profile>/`
     - e.g. - :file:`k3-image-gen/soc/j721e/evm/tifs-rm-cfg.c`
   * - :file:`<soc>_qos.h`
     - U-boot
     - :file:`ti-u-boot/arch/arm/mach-k3/r5/<soc>/<soc>_qos.h`
     - e.g. - :file:`ti-u-boot/arch/arm/mach-k3/r5/am62ax/am62a_qos.h`
   * - :file:`<soc>_qos_uboot.c`
     - U-boot
     - :file:`ti-u-boot/arch/arm/mach-k3/r5/<soc>/`
     - e.g. - :file:`ti-u-boot/arch/arm/mach-k3/r5/am62ax/am62a_qos_uboot.c`
   * - :file:`<soc>_qos_data.c`
     - MCU+ SDK / PDK QoS
     - :file:`source/drivers/qos/v0/soc/<soc>/qos_data.h` and :file:`packages/ti/boot/sbl/soc/k3/<soc>_qos_data.c`
     - e.g. - :file:`source/drivers/qos/v0/soc/am62ax/qos_data.h` and :file:`packages/ti/boot/sbl/soc/k3/j721s2_qos_data.c`
   * - :file:`<soc>-firewall-config.c`
     - U-boot
     - Not yet supported
     -
   * - :file:`<soc>-firewall-config.c`
     - SBL
     - Not yet supported
     -
   * - :file:`sciclient_defaultBoardcfg.c`
     - PDK sciclient
     - :file:`packages/ti/drv/sciclient/soc/V<X>/`
     - e.g. - :file:`pdk/packages/ti/drv/sciclient/soc/V1/sciclient_defaultBoardcfg.c`
   * - :file:`sysfw_img_cfg.h`
     - k3-image-gen
     - :file:`soc/<soc>/<profile>/`
     - e.g. - :file:`k3-image-gen/soc/j721e/evm/sysfw_img_cfg.h`
   * - :file:`rm-cfg.yaml`
     - U-boot
     - :file:`ti-u-boot/board/ti/<soc>/`
     - e.g. - :file:`ti-u-boot/board/ti/am62ax/rm-cfg.yaml`
   * - :file:`tifs-rm-cfg.yaml`
     - U-boot
     - :file:`ti-u-boot/board/ti/<soc>/`
     - e.g. - :file:`ti-u-boot/board/ti/am62ax/tifs-rm-cfg.yaml`

Troubleshooting
---------------

- If you see **No product with name "K3-Respart-Tool" and version 1.0.0 found**,
  you likely missed the step to select the **software product**.
- If you get error ``XYZ`` **is not generated when configuration errors exist**,
  your resource split has errors. Adjust the allocation to fix them, then generate
  the output files.
- If you remove resources from a core and the ``ALL`` column in the "Resource
  Allocation Table" does not change, those resources belong only to that core.
  :ref:`See "Resource Totals" under "Review Resource Allocation" for more details
  <resource_totals>`.

