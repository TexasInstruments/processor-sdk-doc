.. _pm_upstream:

###############
Upstream Status
###############

At TI, developers practice an upstream-first mindset where all patches in the
SDK should be available in the upstream repositories as soon as possible.
However, because of the extensive community review process, getting patches
into the upstream repositories can take a long time, so features might appear
in the SDK before upstream.

This page tracks the status of all low power features in upstream. We encourage
users to review any pending series listed.

We update this page with each SDK release, so it might fall out of date as the
upstream community accepts new patches.

.. note::

   Upstream support for a wakeup source does not guarantee device tree
   configuration. Refer to the
   :ref:`"Wakeup Sources" <pm_wakeup_sources>` section for more information
   about how to configure wakeup sources.

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   .. list-table:: Feature Upstream Status
      :widths: auto
      :header-rows: 1

      * - Feature
        - Upstream
        - Notes
      * - DeepSleep
        - Yes
        - Remoteproc graceful shutdown is not upstream. See additional steps below.
      * - MCU Only
        - Yes
        - Same remoteproc limitation as DeepSleep.
      * - Partial I/O
        - Yes
        -
      * - Dynamic Frequency Scaling
        - Yes
        -
      * - Standby
        - No
        -
      * - Runtime PM
        - Yes
        -

   .. list-table:: Wakeup Source Upstream Status
      :widths: auto
      :header-rows: 1

      * - Wakeup Source
        - DeepSleep
        - MCU Only
        - Partial I/O
        - Notes
      * - Real-Time Clock (RTC)
        - Yes
        - Yes
        -
        -
      * - MCU (WKUP) GPIO
        - Yes
        - Yes
        -
        -
      * - Main I/O Daisy Chain
        - Partial
        - Partial
        -
        - Upstream includes Main UART wakeup but not Main GPIO wakeup.
      * - USB
        - Yes
        - Yes
        -
        -
      * - WKUP UART
        - Yes
        - Yes
        -
        -
      * - MCU IPC
        -
        - Yes
        -
        -
      * - CAN I/O Daisy Chain
        - No
        - No
        - Yes
        - 

.. ifconfig:: CONFIG_part_variant in ('AM62AX', 'AM62DX', 'AM62PX')

   .. list-table:: Feature Upstream Status
      :widths: auto
      :header-rows: 1

      * - Feature
        - Upstream
        - Notes
      * - DeepSleep
        - Yes
        -
      * - MCU Only
        - Yes
        -
      * - Partial I/O
        - Yes
        -
      * - I/O Only Plus DDR
        - In progress
        - Linux and U-Boot patches are pending review.
      * - Dynamic Frequency Scaling
        - Yes
        -
      * - Standby
        - No
        -
      * - Runtime PM
        - Yes
        -

   .. list-table:: Wakeup Source Upstream Status
      :widths: auto
      :header-rows: 1

      * - Wakeup Source
        - DeepSleep
        - MCU Only
        - Partial I/O
        - I/O Only Plus DDR
        - Notes
      * - Real-Time Clock (RTC)
        - Yes
        - Yes
        -
        -
        -
      * - WKUP GPIO
        - Yes
        - Yes
        -
        -
        -
      * - Main I/O Daisy Chain
        - Partial
        - Partial
        -
        -
        - Upstream includes Main UART wakeup but not Main GPIO wakeup.
      * - USB
        - Yes
        - Yes
        -
        -
        -
      * - WKUP UART
        - Yes
        - Yes
        -
        -
        -
      * - MCU IPC
        -
        - Yes
        -
        -
        -
      * - CAN I/O Daisy Chain
        - No
        - No
        - Yes
        - In progress
        - I/O Only Plus DDR patches are in progress.

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   .. important::

      TI has not yet upstreamed all low power mode features in Arm Trusted
      Firmware. The following list applies to upstream Linux only when using
      the TI fork for TF-A. Refer to
      :ref:`Arm Trusted Firmware <foundational-components-atf>` section for how
      to use the TI TF-A fork.

   .. list-table:: Feature Upstream Status
      :widths: auto
      :header-rows: 1

      * - Feature
        - Upstream
        - Notes
      * - DeepSleep
        - Yes
        -
      * - RTC + I/O + DDR
        - In progress
        - Linux patches pending review.
      * - RTC Only
        - In progress
        -
      * - Standby
        - In progress
        - Linux patches pending review.
      * - Dynamic Frequency Scaling
        - Yes
        -
      * - Runtime PM
        - Yes
        -
      * - Wakeup source detection
        - No
        -

   .. list-table:: Wakeup Source Upstream Status
      :widths: auto
      :header-rows: 1

      * - Wakeup Source
        - DeepSleep
        - RTC + I/O + DDR
        - RTC Only
        - Notes
      * - Real-Time Clock (RTC)
        - No
        - No
        - No
        -
      * - WKUP GPIO
        - Yes
        -
        -
        -
      * - Main I/O Daisy Chain
        - Partial
        -
        -
        - Upstream includes Main UART wakeup but not Main GPIO wakeup.
      * - WKUP I/O Daisy Chain
        - Yes
        - Yes
        -
        -
      * - WKUP UART
        - Yes
        -
        -
        -
      * - USB
        - Yes
        -
        -
        -
      * - RTC I/O
        - No
        - No
        - No
        -

***********************
Pending Upstream Series
***********************

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   Currently, there are no pending upstream series for
   |__PART_FAMILY_DEVICE_NAMES__|.

.. ifconfig:: CONFIG_part_variant in ('AM62AX', 'AM62DX', 'AM62PX')

   .. list-table:: Pending Upstream Series
      :widths: auto
      :header-rows: 1

      * - Series
        - Feature Covered
        - Codebase
      * - `arm64: dts: ti: k3-am62a7-sk: Split r5f memory region <https://lore.kernel.org/all/20260701-topic-am62a-ioddr-dt-v6-19-v7-0-e9db8b16821a@baylibre.com/>`__
        - I/O Only Plus DDR
        - `Linux <https://github.com/torvalds/linux>`__
      * - `am62: IO+DDR resume support <https://lore.kernel.org/all/20260105-topic-am62-ioddr-v2025-04-rc1-v9-0-7e33f2c77dbf@baylibre.com/>`__
        - I/O Only Plus DDR
        - `U-Boot <https://git.u-boot-project.org/u-boot/u-boot/-/tree/main>`__
      * - `IO+DDR low power mode bugfixes for AM62P and AM62A <https://lore.kernel.org/u-boot/20260310100614.951573-1-a-kaur@ti.com/>`__
        - I/O Only Plus DDR
        - `U-Boot <https://git.u-boot-project.org/u-boot/u-boot/-/tree/main>`__

   Enable I/O Only Plus DDR in upstream by applying these patches to the
   corresponding codebase.

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   .. list-table:: Pending Upstream Series
      :widths: auto
      :header-rows: 1

      * - Series
        - Feature Covered
        - Codebase
      * - `PM: QoS/pmdomains: support resume latencies for system-wide PM <https://lore.kernel.org/linux-pm/20260611-topic-lpm-pmdomain-device-constraints-v3-0-75d69438518b@baylibre.com/>`__
        - RTC + I/O + DDR, standby
        - `Linux <https://github.com/torvalds/linux>`__

   This is not the complete list of patches needed to enable RTC + I/O + DDR
   and standby. Additional series will be sent in the future.

***********
Workarounds
***********

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   Remoteproc suspend/resume and graceful shutdown are not present upstream,
   which prevents Linux from suspend/resume to low power states. To enable
   suspend/resume on Linux remove the M4 remoteproc module by entering the
   following command into the Linux console of the EVM:

   .. code-block:: console

      root@am62xx-evm:~# rmmod ti_k3_m4_remoteproc

.. ifconfig:: CONFIG_part_variant in ('AM62AX', 'AM62DX', 'AM62PX', 'AM62LX')

   No workarounds are needed for |__PART_FAMILY_DEVICE_NAMES__|.
