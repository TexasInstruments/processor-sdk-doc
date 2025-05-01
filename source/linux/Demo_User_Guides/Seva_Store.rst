.. _Seva-Store-label:

Seva Store - User Guide
=======================

.. ifconfig:: CONFIG_sdk in ('SITARA')

   .. attention::

      This page is relevant for AM62x SK, AM62x-LP SK and BeaglePlay.

Overview
--------

Seva Store is TI developed Demo Gallery Tool which allows users to Download and Install demos on the go. Developers can host their Demos as Docker Images on any public Docker Registry and link them to Seva Design Gallery. The Seva Design Gallery interacts with the Seva Control Center to easily launch demos from a predetermined source using `docker-compose <https://docs.docker.com/compose/>`__. The Seva Control Center is built using Flutter and Go. To know more on how Seva Control Center exactly works refer `this <https://github.com/texasinstruments/seva#details>`__.

All of the necessary equipment requirement and instructions are provided here.

Hardware Prerequisites
----------------------

-  TI AM62x SK / TI AM62x-LP SK / BeaglePlay

-  PC (Windows or Linux, to use serial terminal console)

-  HDMI Monitor (to view the Demo on Display)

-  Ethernet Cable (to connect SK-EVM to internet)

-  Keyboard (to enter proxy settings if working under VPN)

-  Mouse (to control the Demo)

-  SD card (minimum 16GB)

.. _How-to-Launch-Seva-Store-via-TI-Apps-Launcher:

How to Launch Seva Store via TI Apps Launcher
---------------------------------------------

The TI Apps Launcher demo launches on Linux startup. To Launch Seva Store via TI Apps Launcher follow the below instructions.

1. Flash an SD card with the :file:`tisdk-default-image`. User can download the :file:`tisdk-default-image` wic image from |__SDK_DOWNLOAD_URL__|. Connect the display, ethernet cable, mouse & keyboard and power on the board after inserting an SD card. The TI Apps Launcher will launch when the SK-EVM is fully booted.

   .. ifconfig:: CONFIG_sdk in ('SITARA')

      .. Image:: /images/ti-apps-launcher-home-am62x.png
         :height: 400

   .. ifconfig:: CONFIG_sdk in ('j7_foundational')

      .. Image:: /images/ti-apps-launcher-j7.png
         :width: 950
         :height: 900

2. Once started, you will see an IP Address on the bottom left corner of TI Apps Launcher as shown below. This means your board is successfully connected to Internet.

   .. Image:: /images/ip-addr.jpg
      :height: 400

.. caution::

    If you have connected the SK-EVM to a proxy network, then before launching Seva Store you need to configure Docker and System proxies once per SD Card.
    
    **To set proxy settings you can click on the Settings button from the Left Hand Side Menu and provide the necessary HTTPS & NO PROXY inputs and click Set Proxy button**. Then, continue with Step 3.

    .. Image:: /images/webproxy-settings.jpg
       :height: 400

3. After you see an IP Address, Click on the `Seva Store` button from the Left Hand Side Menu to launch Seva Store.

   .. Image:: /images/seva-store-icon.jpg
      :height: 400

|

4. Click on the Launch Button which you see in centre.

   .. Image:: /images/seva-launch-button.jpg
      :height: 400

|

5. Once you click the Launch Button, Chromium browser launches in full screen with Seva Control Centre in first tab as shown in the figure below.

   .. Image:: /images/seva-control-center.png
      :height: 400

.. note:: It takes approximately **3-4 seconds** for Chromium browser to launch.

6. The Seva Control Centre has a widget in centre which shows the information of Demo you have selected from the Seva Design Gallery. Since, it's a first launch it displayed `No app selected`.

   .. Image:: /images/no-app-selected.jpg
      :height: 400

|

7. To Launch a Demo, you first need to visit the Seva Design Gallery. For that you need to click on the Bottom Right Store Icon as shown in Image below.

   .. Image:: /images/playstore-icon.jpg
      :height: 400

|

8. The Seva Design Gallery page launches in the second tab of the browser as shown below.

   .. ifconfig:: CONFIG_part_variant in ('AM62X')

      .. Image:: /images/seva-design-gallery.png
         :height: 400

   .. ifconfig:: CONFIG_part_variant in ('AM62PX')

      .. Image:: /images/seva-design-gallery-am62p.png
         :height: 400

9. Currently we have the Thermostat Demo Docker Image hosted on Seva Design Gallery. To launch the Thermostat Demo, click on the `Launch` Button as shown below.

   .. Image:: /images/demo-launch.jpg
      :height: 400

|

10. After Clicking Launch Button, you will see a popup which asks user to switch to the first tab (i.e. Seva Control Centre) to run the Demo.

   .. Image:: /images/seva-design-gallery-popup.png
      :height: 400

11. The Centre Widget of Seva Control Centre which displayed `No app selected` earlier in Step 6 will show the information of demo you have selected now (i.e Thermostat Demo).

   .. Image:: /images/demo-widget.jpg
      :height: 400

|

12. Click on the `Start Icon` which you see on the Centre Widget to start the Thermostat Demo as shown in the image below.

   .. Image:: /images/thermostat-demo-start-icon.jpg
      :height: 400

|

13. Once you click the `Start Icon` the Seva Control Centre will run the docker-compose file and start pulling the `Thermostat Demo` from `ghcr.io <https://github.com/TexasInstruments/seva-adocker/pkgs/container/app_thermostat_demo>`__ to launch it. The Seva Control Centre will
show the `Downloading Icon` as shown in the image below.

   .. Image:: /images/seva-buffering.png
      :height: 400

|

.. note:: The Thermostat Demo Docker Image that we provide is around 848 MB. Hence, docker pull time may vary based on your internet speed provided to SK-EVM.

14. Once the Docker Image of `Thermostat Demo` is pulled, the Seva Control Centre will auto launch the demo in full screen as shown below.

   .. Image:: /images/thermostat-demo.png
      :height: 400

15. To close `Thermostat Demo` and come back to Seva Store, click on the cross icon as shown below.

   .. Image:: /images/close-thermostat.jpg
      :height: 400

16. To launch another demo, you can follow from **Step 6**.

17. To close the Seva Store Application and return back to TI Apps Launcher, close the Chromium browser.


How to Launch Seva Store on Host Browser
----------------------------------------

.. important::

    Launching Seva Store on host browser is possible only if the SK-EVM and host PC are connected to the same local network.

1. Flash an SD card with the :file:`tisdk-default-image`. User can download the :file:`tisdk-default-image` wic image from |__SDK_DOWNLOAD_URL__|. Connect the display, ethernet cable, mouse & keyboard and power on the board after inserting an SD card. The TI Apps Launcher will launch when the SK-EVM is fully booted. Take a note of the IP address you see on the bottom left corner of TI Apps Launcher as it will be needed to launch Seva Store on host browser.

2. On host PC, launch your preferred browser and enter **http://<your-board-ip-address>:8007/**.

3. Refer **Step 6 to Step 17** from :ref:`How-to-Launch-Seva-Store-via-TI-Apps-Launcher` to understand how to use Seva Store to Launch a Demo.

How to Create & Host a Docker Image for your Demo
-------------------------------------------------

**How to Create a Docker Image of your Demo**

Docker can build images automatically by reading the instructions from a `Dockerfile <https://docs.docker.com/engine/reference/builder/>`__. A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image. For more details on how to create a Docker Image you can refer `Thermostat Demo Dockerfile <https://raw.githubusercontent.com/TexasInstruments/seva-adocker/main/app_thermostat_demo/Dockerfile>`__.

**How to Host a Docker Image of your Demo**

After building a Docker Image, to host it you can use a Docker Registry. A Docker registry is a storage and distribution system for named Docker images. A Docker registry is organized into Docker repositories, where a repository holds all the versions of a specific image. The same image might have multiple different versions, identified by their tags. The registry allows Docker users to pull images locally, as well as push new images to the registry (given adequate access permissions when applicable).

How to add your Demos in Seva Store
-----------------------------------

Once you have your Demo Docker Image hosted on a Docker Registry, you can refer the following steps to add you Demo in Seva Store,

1. For backend, create a new directory with the naming convention as **app_your-demo-name_demo** and create two new files named **metadata.json** and **docker-compose.yml** under the same directory. For reference you can check out `Thermostat Demo Metadata <https://raw.githubusercontent.com/TexasInstruments/seva-apps/main/app_thermostat_demo/metadata.json>`__ and `Thermostat Demo Docker Compose File <https://raw.githubusercontent.com/TexasInstruments/seva-apps/main/app_thermostat_demo/docker-compose.yml>`__. Once you have both the files tested at your end, create a PR on `seva-apps <https://github.com/TexasInstruments/seva-apps>`__.

2. For frontend, once your PR on `seva-apps <https://github.com/TexasInstruments/seva-apps>`__ is merged, to populate your Demo on Seva Store's Design Gallery you need to create a PR on `seva-design-gallery <https://github.com/TexasInstruments/seva-design-gallery/>`__ to add a `div class` for your Demo. You can refer the following template for the same.

.. code-block:: html

    <div class="ti_p-col-4">
       <div class="card bg-light mb-3 mt-3 h-100 d-flex flex-column align-items-start u-boxShadow-2 u-cardBorder-top-red">
          <p class="label">Your Organization Name</p>
          <img class="animated-gif" src="images/<A_GIF_image_for_your_demo>.gif" class="card-img-top" alt="...">
          <p class="lead text"> Your Demo Name </p>
          <p class="lead text" style="font-size: 14px;">Few Lines Description for your Demo</p>
          <footer>
             <input type="button" value="Launch" onclick="seva_send_message('app_your-demo-name_demo');" />
          </footer>
       </div>
    </div>

3. Once your above both PR's are merged, you will have your Demo added on Seva Store.

Contact Us
----------

If you need any further assistance, reach out to us on `E2E <https://e2e.ti.com/>`__.
