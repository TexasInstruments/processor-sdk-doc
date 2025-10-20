.. http://processors.wiki.ti.com/index.php/WL127x_WLAN_and_Bluetooth_Demos
.. rubric:: Introduction
   :name: introduction-wlan-bt

This page is a landing page for the entire set of WLAN and Bluetooth
Demos available for the WL127x. Many of the demos are platform-agnostic,
others apply specifically to a single platform.

The WL127x's dual mode 802.11 b/g/n and *Bluetooth* transceiver
gives users a robust selection of applications. A list of some basic use
cases preloaded on the EVMs can be seen below:

|

+------------------------------------+----------------------------------------------------------------------------------------------+
| Senario                            | Description                                                                                  |
+====================================+==============================================================================================+
| *Bluetooth* A2DP profile           | Play a \*.wav music file from the EVM on a stereo headset                                    |
+------------------------------------+----------------------------------------------------------------------------------------------+
| *Bluetooth* OPP profile            | Send a \*.jpg image from the EVM to a cellular phone via OPP profile                         |
+------------------------------------+----------------------------------------------------------------------------------------------+
| *Bluetooth* FTP profile            | Sends a text file from the EVM to a PC via FTP profile                                       |
+------------------------------------+----------------------------------------------------------------------------------------------+
| Wireless LAN ping                  | Connect to an Access Point and perform a ping test                                           |
+------------------------------------+----------------------------------------------------------------------------------------------+
| Wireless LAN throughput            | Test UDP downstream throughput using the iPerf tool                                          |
+------------------------------------+----------------------------------------------------------------------------------------------+
| Web browsing through the WLAN      | Browse the web over WLAN using a PC connected to the EVM Ethernet port                       |
+------------------------------------+----------------------------------------------------------------------------------------------+
| *Bluetooth* and WLAN coexistence   | Play a \*.wav music file from the EVM on a stereo headset while browsing the web over WLAN   |
+------------------------------------+----------------------------------------------------------------------------------------------+

.. rubric:: Bluetooth Demos
   :name: bluetooth-demos

.. rubric:: Classic Bluetooth
   :name: classic-bluetooth

-  `Demos using
   GUI <http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_Bluetooth_GUI>`__

-  `SPP <http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_Bluetooth_GUI#The_SPP_View>`__
-  `HID <http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_Bluetooth_GUI#The_HID_View>`__
-  `A2DP <http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_Bluetooth_GUI#The_Audio_View>`__

-  `Bluetooth Demos using Command Line in
   Linux <http://processors.wiki.ti.com/index.php/NLCP_Bluetooth_Command_Lines>`__
-  `Bluetooth Demos using Command Line in
   Windows <http://processors.wiki.ti.com/index.php/NLCP_Bluetooth_Terminal_with_Windows>`__

.. rubric:: Bluetooth Low-Energy (BLE)
   :name: bluetooth-low-energy-ble

-  `Enabling BLE on the
   WL127xL <http://processors.wiki.ti.com/index.php/BTS_with_BLE_enabled_for_WL127xL>`__

|

.. rubric:: WLAN Demos
   :name: wlan-demos

.. rubric:: First Time
   :name: first-time

If running the WLAN demos on an EVM for the first time, it is
recommended that you first complete the two steps below:

-  Step 1: Calibration – Calibration is a one-time procedure, performed
   before any WLAN operation. Calibration is performed once after the
   board assembly, or in case the 12xx connectivity daughtercard or EVM
   are replaced (refer to `Calibration
   Process <http://processors.wiki.ti.com/index.php/WL12xx_NLCP_Calibration_Proccess>`__).

You may refer to `Linux Wireless
Calibrator <http://linuxwireless.org/en/users/Drivers/wl12xx/calibrator>`__
page for more instruction.

-  Step 2: MAC address settings - This is a one-time procedure, done
   after the calibration, and before any WLAN operation is performed
   (refer to: <`modifying WLAN MAC
   address <http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_Station_MAC_Change>`__>)

.. rubric:: WLAN Station Demos
   :name: wlan-station-demos

-  **Connect to AP (Ping Test)**

-  `QT
   GUI <http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_WLAN_Station_demo_NLCP_GUI>`__
-  `Command line - IW
   commands <http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_WLAN_Station_Connect_to_non_secured_network>`__
-  `Command line - configuration
   file <http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_Station_Connect_to_non_Secured_AP_using_WPA_Supplicant_Configuration_file>`__
-  `Command line - WPA supplicant
   scripts <http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_WLAN_Station_demo_NLCP>`__

-  **WLAN Throughput Test Utility (Command line)**

-  `WLAN Throughput Test <http://processors.wiki.ti.com/index.php/WLAN_Throughput_Test>`__

-  **WLAN Low Power Use Case Demo (Magic Packet visibly wakes up
   system)**

-  AM37x platform:

-  `Shut Down
   Mode <http://processors.wiki.ti.com/index.php/AM37x_Wireless_Connectivity_Suspend_Resume_Operation>`__
-  `WOWLAN (Wake On LAN)
   Mode <http://processors.wiki.ti.com/index.php/AM37x_Wireless_Connectivity_Suspend_Resume_WOWLAN_Operation>`__

-  AM18x platform:

-  `Shut Down
   Mode <http://processors.wiki.ti.com/index.php/AM18x_Wireless_Connectivity_Suspend_Resume_Operation>`__

-  AM335x platform:

-  Currently Not Supported

.. rubric:: WLAN Soft AP Demos
   :name: wlan-soft-ap-demos

-  `Soft AP - no security Demo (Command
   Line) <http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_WLAN_AP_No_Security>`__
-  `Soft AP Configuration Utility (QT
   GUI) <http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_WLAN_AP_demo_NLCP_GUI>`__
-  `Soft AP Wireless
   Gateway <http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_WLAN_AP_demo_NLCP_GUI>`__

.. rubric:: WLAN - WiFi Direct Demos
   :name: wlan---wifi-direct-demos

-  `WiFi Direct Demos (Command
   line) <http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_NLCP_WiFi_Direct_Configuration_Scripts>`__

-  `Generating P2P Group using Push
   button <http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_NLCP_WiFi_Direct_Configuration_Scripts#Create_1:2_P2P_Group_-_Connect_in_pbc_.28Push_button_Control.29>`__
-  `Generating Autonomous P2P Group - Push
   Button <http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_NLCP_WiFi_Direct_Configuration_Scripts#Create_Autonomous_1:2_P2P_Group_.28Push_button_Control.29>`__
-  `Generating P2P Group using Pin
   Code <http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_NLCP_WiFi_Direct_Configuration_Scripts#Create_1:2_P2P_Group_-_Connect_with_PIN_code>`__

-  `WiFi Direct Battleship
   Demo <http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_Battleship_Game_demo>`__

.. rubric:: Miscellaneous WLAN Demos
   :name: miscellaneous-wlan-demos

-  **`WLAN Code Descriptions and
   Examples <http://processors.wiki.ti.com/index.php/OMAP35x_Wireless_Connectivity_Code_Descriptions_and_Examples>`__**

-  `Enabling Multiple WLAN Roles on the
   WL127x <http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_NLCP_Multi_Role_Configuration>`__
-  `How-to configure Ethernet to WLAN
   Gateway <http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_Ethernet_WLAN_Gateway>`__
-  `How-to configure Ethernet to WLAN
   Bridge <http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_Ethernet_WLAN_Bridge>`__

|

.. rubric:: Miscellaneous Demos
   :name: miscellaneous-demos

-  `Setting Host CPU
   clock <http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_CPU_Clock_Setup#CPU_Clock>`__
-  `AM37x Wlan Throughput
   Measurement <http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_AM37x_WLAN_Throughput_Measurement>`__
-  `Suspend Resume
   Operation <http://processors.wiki.ti.com/index.php/Open_Source_Wireless_Connectivity_Guide#Suspend_Resume>`__
-  `How to work with A
   band <http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_A_band_support>`__

.. rubric:: Regulatory Domain
   :name: regulatory-domain

-  `WLAN
   rates <http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_WLAN_rates>`__
-  `WLAN
   channels <http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_WLAN_channels>`__
-  `How to control Regulatory
   Domain <http://processors.wiki.ti.com/index.php/OMAP_Wireless_Connectivity_Regulatory_Domain>`__
-  External links:

-  `Regulatory Domain -
   General <http://linuxwireless.org/en/developers/Regulatory>`__
-  `Regulatory
   rules <http://linuxwireless.org/en/developers/Regulatory/processing_rules>`__

