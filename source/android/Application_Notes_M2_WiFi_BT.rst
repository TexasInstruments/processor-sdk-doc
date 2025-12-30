.. _android-m2-wifi-bt:

####################################
M.2 Wi-Fi and Bluetooth module setup
####################################

This application note describes the Android build system modifications required
to integrate third-party M.2 Wi-Fi and Bluetooth modules.

.. warning::

   This guide assumes the kernel already includes the required drivers and
   device tree overlays. For kernel configuration, see :ref:`android-build-kernel`.

************
Introduction
************

The AM62Px-SK and AM62x-SK Evaluation Modules (EVMs) include an M.2 Key E
connector that supports Wi-Fi and Bluetooth combo modules. These modules
typically use:

- Secure Digital Input/Output (SDIO) interface for Wi-Fi
- Universal Asynchronous Receiver-Transmitter (UART) interface for Bluetooth

This guide lists the files you need to change in the Android build system
to add support for a new Wi-Fi and Bluetooth module.


********************
Wi-Fi firmware setup
********************

.. note::

   Depending on your Wi-Fi module, you might also need to change the Wi-Fi
   Hardware Abstraction Layer (HAL) configuration in :file:`device/ti/am62x/shared/wifi/`.
   The default configuration uses TI-specific libraries (``lib_driver_cmd_ti``).
   For other modules, you might need to update :file:`BoardConfig.mk` to use the appropriate driver library
   (e.g., ``lib_driver_cmd_nl80211`` for generic NL80211 drivers).

Adding firmware files
=====================

Copy the firmware files to the appropriate directory:

.. code-block:: console

   $ cp <firmware_file> \
       ${YOUR_PATH}/ti-aosp-16/vendor/ti/am62x/wifi/vendor/firmware/<vendor_dir>/

Common vendor directories:

- ``mrvl/`` for Marvell (now NXP Semiconductors)
- ``ti-connectivity/`` for TI
- ``brcm/`` for Broadcom/Cypress
- ``nxp/`` for NXP Semiconductors Bluetooth firmware


Change Android.bp
=================

Edit :file:`vendor/ti/am62x/wifi/Android.bp` and add a ``prebuilt_firmware`` module.

.. code-block:: text

   prebuilt_firmware {
       name: "<package_name>",
       vendor: true,
       src: "vendor/firmware/<vendor_dir>/<firmware_file>",
       filename: "<firmware_file>",
       sub_dir: "<vendor_dir>",
       proprietary: true,
   }


Change the product Makefile
===========================

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   Edit :file:`vendor/ti/am62x/am62p.mk` and add the firmware to PRODUCT_PACKAGES.

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   Edit :file:`vendor/ti/am62x/am62x.mk` and add the firmware to PRODUCT_PACKAGES.

.. code-block:: makefile

   PRODUCT_PACKAGES += \
       <package_name>


***********************
Bluetooth configuration
***********************

M.2 Wi-Fi and Bluetooth combo modules typically use UART for Bluetooth communication.
Change the following files to enable Bluetooth.


Change device_vendor.mk
=======================

Edit :file:`device/ti/am62x/shared/bluetooth/device_vendor.mk` to enable Bluetooth
permissions and HAL.

Change from disabled Bluetooth:

.. code-block:: makefile

   PRODUCT_COPY_FILES += \
       device/generic/car/common/android.hardware.disable.xml:$(TARGET_COPY_OUT_VENDOR)/etc/permissions/android.hardware.bluetooth.xml \
       device/generic/car/common/android.hardware.disable.xml:$(TARGET_COPY_OUT_VENDOR)/etc/permissions/android.hardware.bluetooth_le.xml

To enabled Bluetooth:

.. code-block:: makefile

   # Bluetooth configuration

   # Enable Bluetooth permissions
   PRODUCT_COPY_FILES += \
       frameworks/native/data/etc/android.hardware.bluetooth.xml:$(TARGET_COPY_OUT_VENDOR)/etc/permissions/android.hardware.bluetooth.xml \
       frameworks/native/data/etc/android.hardware.bluetooth_le.xml:$(TARGET_COPY_OUT_VENDOR)/etc/permissions/android.hardware.bluetooth_le.xml

   # Bluetooth HAL (AIDL)
   PRODUCT_PACKAGES += \
       android.hardware.bluetooth-service.default


Change product.prop
===================

Edit :file:`device/ti/am62x/product.prop` and add Bluetooth properties.

Example configuration (adjust profiles based on your module capabilities):

.. code-block:: text

   # Bluetooth configuration
   # Set the Bluetooth Class of Device
   # Service Field: 0x5A -> 90
   #    Bit 17: Networking
   #    Bit 19: Capturing
   #    Bit 20: Object Transfer
   #    Bit 22: Telephony
   # MAJOR_CLASS: 0x01 -> 1 (Computer)
   # MINOR_CLASS: 0x04 -> 4 (Desktop workstation)
   bluetooth.device.class_of_device=90,1,4

   # Set supported Bluetooth profiles to enabled
   bluetooth.profile.asha.central.enabled?=true
   bluetooth.profile.a2dp.source.enabled?=true
   bluetooth.profile.avrcp.target.enabled?=true
   bluetooth.profile.gatt.enabled?=true
   bluetooth.profile.hfp.ag.enabled?=true
   bluetooth.profile.hid.device.enabled?=true
   bluetooth.profile.hid.host.enabled?=true
   bluetooth.profile.map.server.enabled?=true
   bluetooth.profile.opp.enabled?=true
   bluetooth.profile.pan.nap.enabled?=true
   bluetooth.profile.pan.panu.enabled?=true
   bluetooth.profile.pbap.server.enabled?=true

   # Disable LeAudio profiles (requires specific hardware support)
   bluetooth.profile.bap.broadcast.assist.enabled=false
   bluetooth.profile.bap.unicast.client.enabled=false
   bluetooth.profile.bas.client.enabled=false
   bluetooth.profile.ccp.server.enabled=false
   bluetooth.profile.csip.set_coordinator.enabled=false
   bluetooth.profile.hap.client.enabled=false
   bluetooth.profile.vcp.controller.enabled=false

.. note::

   The ``bluetooth.profile.*.enabled?=true`` syntax (with ``?``) enables the profile
   by default but allows overriding. Profiles disabled with ``=false``
   (without ``?``) cannot be overridden.


Change ueventd.rc
=================

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   Edit :file:`device/ti/am62x/am62p/ueventd.am62p.rc` and add UART permissions:

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   Edit :file:`device/ti/am62x/am62x/ueventd.am62x.rc` and add UART permissions:

.. code-block:: text

   # Bluetooth UART
   /dev/ttyS1    0660   bluetooth  bluetooth

.. note::

   The UART device name (``ttyS1``, ``ttyS2``, and so on) depends on your device tree
   overlay configuration.


Change file_contexts
====================

Edit :file:`device/ti/am62x/sepolicy/common/file_contexts` and add:

.. code-block:: text

   # Bluetooth UART
   /dev/ttyS1                      u:object_r:hci_attach_dev:s0


Adding SELinux policy
=====================

Create :file:`device/ti/am62x/sepolicy/common/hal_bluetooth_default.te`:

.. code-block:: text

   # Allow Bluetooth HAL to access UART device
   allow hal_bluetooth_default hci_attach_dev:chr_file rw_file_perms;


***************
Build and flash
***************

Rebuild the Android image
=========================

.. code-block:: console

   $ cd ${YOUR_PATH}/ti-aosp-16
   $ source build/envsetup.sh
   $ lunch <BUILD_TARGET>
   $ m

Flash the device
================

After building, flash the device again following the standard
flashing procedure documented in :ref:`android-flashing`.

Configure the device tree blob overlay (DTBO)
=============================================

After flashing, configure the DTBO index from U-Boot:

.. code-block:: console

   => env set adtbo_idx <your_dtbo_index>
   => saveenv
   => reset

See :ref:`android-dtbo` for the list of available DTBO overlays and their indices.


*******
Summary
*******

Change the following files to add Wi-Fi and Bluetooth support:

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   .. list-table::
      :header-rows: 1
      :widths: 50 50

      * - File
        - Purpose

      * - :file:`vendor/ti/am62x/wifi/Android.bp`
        - Add prebuilt_firmware module for Wi-Fi/BT firmware

      * - :file:`vendor/ti/am62x/am62p.mk`
        - Add firmware to PRODUCT_PACKAGES

      * - :file:`device/ti/am62x/shared/bluetooth/device_vendor.mk`
        - Enable Bluetooth permissions XML and HAL

      * - :file:`device/ti/am62x/product.prop`
        - Add Bluetooth properties (class of device, profiles)

      * - :file:`device/ti/am62x/am62p/ueventd.am62p.rc`
        - Set UART device permissions for Bluetooth

      * - :file:`device/ti/am62x/sepolicy/common/file_contexts`
        - Add SELinux context for Bluetooth UART

      * - :file:`device/ti/am62x/sepolicy/common/hal_bluetooth_default.te`
        - Add SELinux policy for Bluetooth HAL UART access

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   .. list-table::
      :header-rows: 1
      :widths: 50 50

      * - File
        - Purpose

      * - :file:`vendor/ti/am62x/wifi/Android.bp`
        - Add prebuilt_firmware module for Wi-Fi/BT firmware

      * - :file:`vendor/ti/am62x/am62x.mk`
        - Add firmware to PRODUCT_PACKAGES

      * - :file:`device/ti/am62x/shared/bluetooth/device_vendor.mk`
        - Enable Bluetooth permissions XML and HAL

      * - :file:`device/ti/am62x/product.prop`
        - Add Bluetooth properties (class of device, profiles)

      * - :file:`device/ti/am62x/am62x/ueventd.am62x.rc`
        - Set UART device permissions for Bluetooth

      * - :file:`device/ti/am62x/sepolicy/common/file_contexts`
        - Add SELinux context for Bluetooth UART

      * - :file:`device/ti/am62x/sepolicy/common/hal_bluetooth_default.te`
        - Add SELinux policy for Bluetooth HAL UART access
