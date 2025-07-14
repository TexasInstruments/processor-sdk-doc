.. _enable_m2cc3301:

#################################
How to Enable M.2-CC33x1 in Linux
#################################

Processor SDK 10.0 introduces support for the CC33XX family of devices.
These devices feature Wi-Fi 6 (802.11ax) for the 2.4 and 5GHz frequency bands,
and can be attached to embedded linux devices communicating over SDIO.
The CC3351 supports both 2.4 and 5GHz frequencies, while the CC3301 supports only 2.4GHz.
Find more information about the `CC3301 here <https://www.ti.com/product/CC3301>`_.

Because the AM6x starter kits now feature an M.2 Key-E connector, an M.2 card has been
developed for evaluation purposes. `Order the M.2-CC3301 board from here <https://www.ti.com/tool/M2-CC3301>`_.
The M.2-CC3351 is also interchangeable and uses the exact same instructions below.

By default, the Processor SDK includes support for the M.2-CC33x1 on the following starter kits:

* SK-AM62B-P1
* SK-AM62A-LP
* SK-AM62P-LP
* AM62L-EVM

*********************
Hardware Installation
*********************

To install the M.2-CC33x1, remove the screw from the Starter Kit's M.2 connector. Place the M.2-CC33x1 into the
Key-E slot. Place the M.2 card into the Starter Kit's slot, and insert the screw such that the edge of the
M.2 card is held down by the screw. The end result should be as shown in the image below.

.. Image:: /images/m2-cc3351.jpg
     :align: center
     :height: 360

********************************
Enable DT Overlay for M.2-CC33x1
********************************

.. ifconfig:: CONFIG_sdk in ('SITARA')

    After flashing the SD card with the :file:`tisdk-default-image`, mount the SD card onto a host computer, if not done already.

.. ifconfig:: CONFIG_sdk in ('DebianSDK')

    After flashing the SD card with the :file:`tisdk-debian-trixie-image`, mount the SD card onto a host computer, if not done already.

On the boot partition of the SD card, add one of the following variables, corresponding to the starter kit,
into the :file:`uEnv.txt` file. This will let u-boot enable the m.2-cc33x1 devicetree overlay. The :file:`uEnv.txt` file can be found on the ``boot``
partition of the SD card.

For SK-AM62B-P1:

    .. code-block:: console

        name_overlays=ti/k3-am625-sk-m2-cc3351.dtbo

For SK-AM62A-LP:

    .. code-block:: console

        name_overlays=ti/k3-am62a7-sk-m2-cc3351.dtbo

For SK-AM62P-LP:

    .. code-block:: console

        name_overlays=ti/k3-am62p5-sk-m2-cc3351.dtbo

For AM62L-EVM:

   .. code-block:: console

         name_overlays=ti/k3-am62l3-evm-m2-cc3351.dtbo

.. note::

    Though the name of the file ends with `m2-cc3301.dtbo`, the same file applies for the M.2-CC3351 board.
    Do not change the name of this file in the :file:`uEnv.txt` regardless of which M.2 card that is being used.


****************
Connect to Wi-Fi
****************

.. ifconfig:: CONFIG_sdk in ('SITARA')

   Using scripts provided in the SDK makes connecting to an Access Point or router straightforward.
   The following are steps to connect to a WPA password-secured Access Point.

   .. code-block:: console

      cd /usr/share/cc33xx
      ./sta_start.sh
      ./sta_connect.sh -s WPA-PSK -n <SSID> -p <PASSWORD>
      udhcpc -i wlan0

.. ifconfig:: CONFIG_sdk in ('DebianSDK')

   TI's Debian SDK uses NetworkManager to connect to wifi. To connect, ensure that NetworkManager.service is running
   with the following command:

   .. code-block:: console

      systemctl status NetworkManager.service

   It should show status as "active". If it isn't active, activate it by running the following:

   .. code-block:: console

      systemctl restart NetworkManager.service

   Then, to actually connect to wifi, use `nmcli` as follows:

   .. code-block:: console

      nmcli device wifi connect "<SSID>" password "<password>"

For more information on the Wi-Fi capabilities of the CC33xx devices, please
see the documentation that can be found in the `CC33xx SDK <https://www.ti.com/tool/CC33XX-SOFTWARE>`_.
