########
UniFlash
########

UniFlash is a tool included with Code Composer Studio (CCS) for programming the
flash memory attached to a TI AM335x or AM437x processor. It supports both
Not-And (NAND) and Not-Or (NOR) Flash connected over Serial Peripheral Interface
(SPI) and Octal Serial Peripheral Interface (QSPI) in addition to embedded
MultiMediaCard (eMMC).

This is possible using either the Ethernet interface or the USB device interface
available on the AMXXXx SoC connected to a host computer.

There are two distinct stages to flashing a device:

   #. Create the production image and a separate flash image for programming
      from the AM335x or AM437x SoC. This is usually done by the Linux
      developer responsible for creating the images.

   #. Programming the images using UniFlash v3. This tool runs on a Windows
      computer and serves the images to the target board that is being
      programmed.

UniFlash is one part of an overall system that includes:

   #. The Windows computer on which UniFlash runs
   #. A target board including an AM335x/AM437x Sitara Processor and flash
      memory.
   #. A USB or Ethernet connection between the two.

This guide assumes that the flash on the target board is blank, or needs to be
overwritten. Therefore, the target board has nothing that it can run except
the boot loader stored in the ROM on the AM335x or AM437x SoC.

The ROM boot loader will either use USB or Ethernet to request files served by
UniFlash on the host computer run them on the target board.

.. figure:: /images/Flash_programming_block_diagram.png

Take notice of the files stored on the computer. There are really 2 different
images:

   #. The image to write the flash on the target board, containing the SPL,
      U-Boot, and flasher files. These get pulled over by the boot loader in
      ROM when the target board boots (assuming USB or Ethernet boot are
      active).

   #. The target image. Labeled as just "Image", this gets pulled over from the
      host computer. Once on the target, the flasher splits the image into
      pieces and writes it to the appropriate places in flash as determined
      by the flasher script. This image will also contain an SPL and U-Boot,
      but it will likely also contain a kernel (:file:`zImage`) and Root
      Filesystem. This is the image that will run from the flash media. It
      will vary depending the needs of the target board.

The flashing process involves a Client and Server setup where a host computer
serves the images and the target board based on the AM335x or AM437x SoC is the
client. The connection between the two can either be USB or Ethernet based.
Since the USB protocol supported is Remote Network Driver Interface
Specification (RNDIS) is also TCP/IP based, both processes will be fairly
similar.

In either configuration, the host computer provides the following services to
the target through the UniFlash tool:

   - Bootstrap Protocol (BOOTP) Server: offer an IP address and image name based
     on the Vendor ID requested by the AM335x/AM437x ROM code
   - Dynamic Host Configuration Protocol (DHCP) Server: offer an IP address to
     the target
   - Trivial File Transfer Protocol (TFTP) Server: offer images located on the
     host computer requested by the target board
   - Graphical User Interface: friendly GUI environment for configuration and
     status

Here are some step by step instructions to configure a setup to flash target
boards with a Windows computer. These steps are valid under Windows 7, however
the steps should be similar for other versions of Windows.

****************
Install UniFlash
****************

UniFlash is a tool provided by Texas Instruments that supports many platforms
and flash configurations. Support for Sitara devices is present in UniFlash
version 3.0 and beyond.

   #. `Download UniFlash <https://www.ti.com/tool/UNIFLASH>`__.
   #. Run the UniFlash Setup program.
   #. Click **Next** to accept the terms of the license agreement.
   #. Click **Next** to install into the default directory, :file:`c:\ti`, or
      **Browse** to install somewhere else.
   #. Select **Custom** under type of Setup and click **Next**.

      .. figure:: /images/Uniflashv3_setup_custom.png

   #. Select **Sitara AMxxxx processors** and click **Next**.

      .. figure:: /images/Uniflashv3_setup_sitara.png

   #. Select **Sitara Flash Connection Support**.

      .. figure:: /images/Uniflashv3_setup_sitara_flash_connection.png

   #. Click **Next** to verify your choices.
   #. Wait while UniFlash installs.
   #. Choose what options you prefer to have to start UniFlash (place on
      desktop, quick start, and so on)

UniFlash is now installed and you should see something similar to this:

   .. figure:: /images/Uniflashv3_setup_complete.png

*********************************
Preparing to flash a target board
*********************************

Once installed, UniFlash needs to know how to serve up the files needed to flash
a target board. It needs to know where these files are and how to send them to
the target through either USB or Ethernet.

Here are the options for the Flash Servers Configuration that need to be
properly set up:

   -  Network Interface IP - IP address that the host computer will use.
      Needs to correspond to the values used below to set up the Network
      Interface. The default value, 192.168.2.1, should be fine for most
      environments as it is a local IP Address.
   -  IP Lease - Amount of time an IP Address given to a target board is
      held for.
   -  DHCP IP Range Low - The minimum IP address in a range to give to a
      target board. Must be on the same subnet as the Network Interface IP
      of the host computer.
   -  DHCP IP Range High - The maximum IP address in a range to give to
      a target board. Must be on the same subnet as the Network Interface
      IP of the host computer.
   -  TFTP Server IP - Should be the same as the Network Interface IP of
      the host computer.
   -  TFTP home folder - Folder on the host computer where the files to be
      served to the target board are.
   -  Control Port - Socket used to allow the GUI to interact with servers.
      The default value is fine.

Given these definitions, set the values in UniFlash to match your environment.
**Note: that in most instances the recommended default values should be fine.**

You must place the files served by the host computer in the TFTP home folder
directory. In most cases, you should have the following files to serve to the
target board by the Linux development team (these files can vary and are just an
example):

   - An MLO or SPL
   - A U-boot image
   - A kernel image (if using a Linux kernel for flashing) and associated
     device tree file
   - A :file:`debrick.scr` or :file:`flasher.sh` script
   - Flash image files (has the images to write on the target board)

AM437x additional setup
=======================

If you are using an AM437x device, there are a couple of extra steps to pair
UniFlash with the AM437x ROM code.

   -  After installing UniFlash, open the :file:`opendhcp.cfg` file under the
      install directory, in the :file:`third_party\sitara` folder using a text
      editor such as Notepad.
   -  Add the two lines below to the ``[VENDOR_ID_TO_BOOTFILE_MAP]``
      section toward the top of the file:

      .. code-block:: text

         AM43xx ROM=u-boot-spl-restore.bin
         AM43xx U-B=u-boot-restore.img

      .. note::

         The 10 characters before the ``=`` must be exact as this is what ROM
         sends to request the next file in the flash procedure. The ``x``'s in
         the AM43xx part are lower-case.

*******************************
Flashing a Board using Ethernet
*******************************

To program a board with an Ethernet interface between the host computer and the
target board, a private network between the two is a prerequisite.

The host computer should have a static IP address on one Network Interface Card
(NIC) and connected to an ethernet switch or directly to the target board. A
router that assigns IP addresses will not work without additional configuration.

Here is what you will need:

   -  A host computer with UniFlash installed and an available ethernet port.
   -  The files used to program the board put in the TFTP home folder set
      up in UniFlash.
   -  Two ethernet cables if using a switch and one if using a direct
      connection.
   -  An ethernet switch (optional).

      .. note::

         This should not be a router, as the host computer needs to use a static
         IP addresses.

   -  Target board(s) to program.

Here is an example of the different connections in this set up:

   .. figure:: /images/Ethernet_block_diagram.png

Once you have connected the device to the host, proceed to
:ref:`common_uniflash_section`.

To flash another target board, simply make a connection between it and the host
computer through the switch. The board should start flashing automatically if
powered and connected properly.

**************************
Flashing a Board using USB
**************************

To program a board with a USB interface between the host computer and the target
board, the RNDIS protocol will create a network connection over USB. This will
establish a private network between the two. The host computer will need a
static IP address on one USB interface that ends up looking similar to a
dedicated NIC connected directly to the target board.

Here is what you will need:

   -  A host computer with UniFlash installed and an available USB port.
   -  The files used to program the board put in the TFTP home folder as
      set up in UniFlash.
   -  A appropriate USB cable to connect the host computer and target board.
   -  A target board to program.

Here is an example of the different connections in this set up:

   .. figure:: /images/Usb_block_diagram.png

To establish a USB based RNDIS connection between the host and target, an
appropriate driver must be preset on the host. A RNDIS driver is present in
Windows. Make sure associate this driver with this device. There are 2 different
steps in the flashing process that might require having to install this driver
again.

As the Sitara Processor on the target board moves through different stages of
flashing process, it looks like a different USB device to Windows. The driver
might need to be re-associated with the device for each step. If it is not, the
stage in the process will not be able to communicate over RNDIS and the process
will fail.

This driver association is automatic for AM335x. For AM43xx devices or any
issues with automatic association, a manual association process follows.

To setup the device:

   #. Connect the host computer to the powered target board using an appropriate
      USB cable.

   #. This will prompt Windows to install a USB driver if a target board
      has never connected to that particular computer and that particular
      USB port on that computer. More than likely for the AM437x devices, this
      will fail.

      .. figure:: /images/Usb_driver_didnt_install.png

   #. Use Device Manager to install a USB driver. To open Device Manager,
      click **Start --> All Programs --> Right Click Computer and
      Select Properties**.

      .. figure:: /images/Open_device_manager.png

   #. Click Device Manager in the window that opens.

      .. figure:: /images/Device_manager.png

   #. Find the **AM43xx1.2** Device listed in “Other Devices” per below. It will
      have a little exclamation point on it indicating there is currently a
      problem with the device. **Right click** it and select **Update Driver
      Software**.

      .. figure:: /images/Am43xx_device_properties.png

      .. note::

         If the device is not listed, it is probably because the
         operation has already timed out. Simply power cycle the target board
         to restart the process.

   #. In the Update Driver Software dialog, choose **Browse my computer for
      driver software**.

      .. figure:: /images/Update_USB_Driver_search.png

   #. Click **Let me pick from a list** in the next window:

      .. figure:: /images/Update_Driver_Software_pick.png

   #. Choose **Network Adapter** and click **Next**:

      .. figure:: /images/RNDIS_network_adapter.png

   #. Choose **Microsoft Corporation** as the Manufacturer and **Remote
      NDIS6 based Device** under adapter. Click **Next**:

      .. figure:: /images/RNDIS_network_adapter_RNDIS.png

   #. If you see the following warning, click **Yes**:

      .. figure:: /images/RNDIS_network_adapter_warning.png

   #. You should receive a confirmation when the driver is successfully
      installed. Finally click **Close**

      .. figure:: /images/RNDIS_network_adapter_success.png

   #. When the USB Driver for RNDIS is properly installed, it will create a
      new network interface. This is typically seen in the lower
      right corner of the toolbar:

      .. figure:: /images/New_network_connection.png

When the target receives the first file, it will take over execution on the
target board from the ROM. This will cause another instance of the USB RNDIS
driver to appear. Windows should use the earlier steps to associate the driver
to the device and create another network instance.

It is easy to watch this process in Device Manager by watching the Network
Adapters section. If this does not happen, and the device driver fails to
associate properly, you'll need to use the earlier steps to install the USB
driver for the new device.

Click "No" if asked to remove other static configurations. Windows will indicate
that using the same IP address for both RNDIS connections is generally not a
good idea. However, in this situation, both interfaces cannot be active at the
same time.

   .. Image:: /images/Microsoft_TCP_IP.png

Once you have connected the device to the host, proceed to
:ref:`common_uniflash_section`.

USB Flash Programming Notes
===========================

- The USB/RNDIS set up is specific to each port on a given computer. If you
  follow the process above using one specific port, only that port will allow
  connections. The above steps are necessary for any new port you want to use.
  Therefore, it is best to use the same USB port to avoid having to duplicate
  set ups.
- UniFlash v3.0 only supports programming one board at a time using USB.
- If you have trouble with RNDIS reporting problems in Device Manager,
  it might be necessary to delete the RNDIS Driver and follow the above
  steps again to re-install it.
- For this entire process to work, there has to be two USB devices
  associated and each of them need to have their network addresses set
  up correctly. Essentially, at different steps in the process, the USB
  connected target board looks differently to Windows and it needs to
  have a driver and network set up for each. You can check this using
  Device Manager for USB and Network Manager for networking.

.. _common_uniflash_section:

****************
Flashing a Board
****************

To begin flashing a target device:

   #. If UniFlash is not already running on the host computer, start it.

   #. **Click** on **New Target Configuration**.

      .. figure:: /images/UniFlash_new_target_configuration.png

   #. Set **Connection** to **Sitara Flash Connections** and **Board or
      Device** to **Sitara Flash Devices**. Click **OK**.

      .. figure:: /images/Uniflash_Create_CCXML_File.png

   #. Make sure the **Flash Server Configuration** is correct.

      .. figure:: /images/UniFlash_flash_server_configuration.png

   #. Connect the host computer to the network switch (or directly to the target
      board if using a direct connection).

   #. **Click** on the **Open Network and Sharing Center**.

      .. figure:: /images/Open_network_sharing_center.png

   #. **Click** on the Local Area Connection that corresponds to the
      ethernet connection. If you only have one, it should be the only one
      listed.

      .. figure:: /images/Internet_connection.png

   #. In the Connection Dialog, click **Properties**.

      .. figure:: /images/Local_Area_Connection_Status.png

   #. Select **Internet Protocol Version 4 (TCP/IPv4)** and choose
      **Properties**.

      .. figure:: /images/Tcpipv4_properties.png

   #. Set the port to use a Static IP Address by selecting **Use the
      following IP Address:** and changing the **IP Address:** to
      ``192.168.2.1``. This setting should correspond to the **Network
      Interface IP** setting in UniFlash.

      .. figure:: /images/Ip_address.png

   #. Verify that the **Subnet Mask** is ``255.255.255.0`` and click
      **OK**.

   #. Click **Close**.

      .. figure:: /images/Local_Area_Connection_Properties_close.png

   #. Click **Close** one more time to get back to the Network Manager.

      .. figure:: /images/Local_Area_Connection_Status_close.png

   #. In UniFlash, enable the flashing capability by clicking on **Start
      Flashing**.

      .. figure:: /images/Uniflash_start_flashing.png

   #. Depending on your Windows Firewall settings, you might get the below two
      warnings for ``opendhcp`` and ``opentftp``. If so, click **Allow
      access** for both.

      .. figure:: /images/Windows_Security_Alert_opendhcp.png

      .. figure:: /images/Windows_Security_Alert_opentftp.png

   #. Make sure the target board has power and connect it via ethernet to
      the network switch (or directly).

   #. If everything is working correctly, the flashing process should start
      automatically on the board. You should see status feedback appear in
      UniFlash as the process progresses.

         .. figure:: /images/UniFlash_status_start.png

      Until it completes:

         .. figure:: /images/UniFlash_status_done.png

      The time the process takes to complete will vary considerably
      depending on several factors including:

         #. The amount of data to transfer to the target
         #. The speed of the interface between the host and the target
         #. the amount of data to write
         #. the write speed of the memory to write to
