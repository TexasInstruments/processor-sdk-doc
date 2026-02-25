.. http://processors.wiki.ti.com/index.php/AM335x_ICEv2_flash_erase

AM335x ICEv2 flash erase
===============================
.. rubric:: Introduction
   :name: introduction-flash-erase

The AM3359 ICE development board from Texas Instruments comes pre-loaded
with a default application in the on-board SPI flash device. In order to
boot Linux from the SD card you will need to clear the SPI flash so that
the boot process will fall back to SD card boot mode. The following
steps will clear the SPI flash. I performed these steps with CCS v6.1.3
on a Ubuntu 14.04 host system

.. rubric:: Steps
   :name: steps-flash-erase

#. Mare sure pins 1 and 2 of Jumper J5 (sysboot) are connected on the
   board
#. Make sure that USB cable is connected from the AM3359 ICE board to
   your host development machine
#. Launch Code Composer Studio (CCS)

   -  If you do not have CCS, download it here: `CCS
      Download <https://www.ti.com/tool/download/CCSTUDIO>`__

#. Create a target configuration file in CCS to connect to the AM3359
   ICE board

   .. note::

      If you already have a target configuration for your AM3359 ICE board
      you may skip this step

   -  Click **File -> New-> Target Configuration File**
   -  Filename : AM3359-ice-v2.ccxml. Check "Use shared location" to be
      available to anyone who uses the workspace. Click Finish. A window
      opens up which is to configure the connection details

      -  Connection: "Texas Instruments XDS100v2 USB Debug Probe"
      -  Device: ICE\_AM3359
      -  Click Save

#. Launch your AM3359 ICE Target Configuration

   -  Click **Window -> Show View -> Target Configurations**
   -  Right click on the **AM3359-ice-v2.ccxml** file and the click
      **Launch Selected Configuration**
   -  This should switch your current perspective to the **CCS Debug**
      perspective. If it doesn't, click **View -> Debug** to get to the
      **CCS Debug** perspective

#. Connect the debugger to the CortexA8 core

   -  Right click on **Texas Instruments XDS100v2 USB Debug
      Probe\_0/CortxA8** listed in the Debug view and select **Connect
      Target**

#. Load the SPI flash programmer into the CortexA8 core

   -  Download the SPI flash programmer and unzip it: :download:`Isdk spi
      flasher.zip </files/Isdk_spi_flasher.zip>`
   -  Highlight the **Texas Instruments XDS100v2 USB Debug
      Probe\_0/CortxA8** by clicking on it
   -  Click **Run -> Load -> Load Program**
   -  Browse to the **isdk\_spi\_flasher.out** file (that you just
      downloaded and unzipped) and click **OK**

#. Run the SPI flash programmer on the CortexA8

   -  Highlight the **Texas Instruments XDS100v2 USB Debug
      Probe\_0/CortxA8** by clicking on it
   -  Click **Run -> Resume**

#. At this point the SPI flash programmer is running on the CortexA8 and
   we just need to follow the prompts to clear the flash

   -  If it isn't opened already, open the **Console** view by clicking
      **Window -> Show View -> Console**
   -  The program will give you the following prompts, type the
      responses and press Enter

      -  Enter Operation [1 - Flash ] [2 - Erase] : 2
      -  Enter the offset [in Hex]: 0
      -  Enter size to be erased in Kilo bytes: 64

Once the program outputs 'Erase complete. Exiting' then you are
finished! You can now disconnect the debugger and close CCS. Then, power
down the board, and connect back pins 2 and 3 on Jumper J5 (sysboot).
After that, you can put your SD card loaded with Linux into the ICE
board and reset it to boot Linux.

