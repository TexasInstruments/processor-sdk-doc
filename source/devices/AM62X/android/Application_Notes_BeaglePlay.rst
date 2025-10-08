.. _beagleplay-app-note:

###########
Beagle Play
###########

The Beagle Play is very similar to the AM62x SK EVM.
Therefore, the AM62x SDK can be installed on the Beagle Play as well.

This application note contains steps to install the AM62x SDK on the Beagle Play board.

**************************
Initial Flashing procedure
**************************

Flashing Android the first time requires booting from DFU.

First, install snagboot 1.3.0 following the `official instructions <https://github.com/bootlin/snagboot>`_
Make sure to install the udev rules as documented:

.. code-block:: console

   $ snagrecover --udev > 50-snagboot.rules
   $ sudo cp 50-snagboot.rules /etc/udev/rules.d/
   $ sudo udevadm control --reload-rules
   $ sudo udevadm trigger

Then, the following steps are required:

1. Make sure the board is powered down. No SD card is present.

2. Plug in the serial connector to view debug logs. In a terminal, open:

   .. code-block:: console

      $ sudo picocom -b 115200 -r -l /dev/ttyUSB0

3. Hold the ``USR`` button. While holding the button, insert ``USB`` cable from PC to board.

4. Wait for DFU mode to come up. DFU mode is a backup boot mode for the Beagle Play.
   To check if the device enumerates via DFU, run ``dfu-util -l``:

   .. code-block:: console

      $ dfu-util -l

      Found DFU: [0451:6165] ver=0200, devnum=99, cfg=1, intf=0, path="1-1", alt=1, name="SocId", serial="01.00.00.00"
      Found DFU: [0451:6165] ver=0200, devnum=99, cfg=1, intf=0, path="1-1", alt=0, name="bootloader", serial="01.00.00.00"

5. Run ``snagrecover`` to load the bootloaders:

   .. code-block:: console

      # run from out/target/product/am62x
      $ snagrecover -s am625 -f ./am625-beagleplay.yaml

   The debug console will show:

   .. code-block:: console

      Press SPACE to abort autoboot in 2 seconds
      =>

6. In the debug console, hit the SPACE key to halt in U-Boot

7. Make sure the default U-Boot environment is configured:

   .. code-block:: console

      => env default -a -f
      => saveenv

8. Start fastboot::

      => fastboot usb 0

9. Run the flashing script:

   .. code-block:: console

      # run from out/target/product/am62x
      $ sudo ./flashall.sh --board am625-beagleplay

10. Unplug USB power and replug to switch to normal boot mode.


******************
External resources
******************

- https://docs.beagleboard.org/latest/boards/beagleplay/index.html
- https://www.beagleboard.org/boards/beagleplay
