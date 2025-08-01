.. _u-boot-build-guide-environment-k3:

###########
Environment
###########

******************
U-Boot Environment
******************

.. note::

   SDK 9.0 will not default to the environments that are saved on the boards,
   It will default to the ones that are given with the particular uboot in
   the release.

By default the SDK builds will have the default environments whenever being
run, to have some custom environments, one needs to rely on uEnv.txt
file.

The added benefit of using uEnv.txt is that it is more granular than the
saveenv counterpart as we can choose to store the variables that are
actually being set during the development workflow.

**Writing to MMC/EMMC**

.. code-block:: console

  => env export -t $loadaddr <list of variables>
  => fatwrite mmc ${mmcdev} ${loadaddr} ${bootenvfile} ${filesize}

The following will update the uEnv.txt file on the bootmedia and then
whenever "run envboot" is run on the board, uEnv.txt will be read based on
mmcdev value to be read either from emmc/sd card.

You can specifically choose the variables that you are changing in your
development process so that the other variables are not affected due to the
whole environment being saved. Optionally, one can save the full
environment too in uEnv.txt by not specifying <list of variables> this
will have some issues with the ethernet mac addresses not being overridden
but other things will be set.

**Reading from MMC/EMMC**

By default run envboot will read it from the MMC/EMMC partition ( based on
mmcdev) and set the environments.

If manually needs to be done then the environment can be read from the
filesystem and then imported

.. code-block:: console

  => fatload mmc ${mmcdev} ${loadaddr} ${bootenvfile}
  => env import -t ${loadaddr} ${filesize}

For production environments if one needs to rely on saveenv counterpart
then they can always refer to the `commit <https://source.denx.de/u-boot/u-boot/-/commit/a5e8678e0a32f85ad012aea7641e9534ada5c0fe>`__

.. rubric:: Networking Environment
   :name: networking-environment

When using a USB-Ethernet dongle a valid MAC address must be set in the
environment. To create a valid address please read `**this
page** <https://github.com/u-boot/u-boot/blob/v2024.04/doc/README.usb#L208>`__.
Then issue the following command:

.. code-block:: console

   => setenv usbethaddr value:from:link:above

You can use the **printenv** command to see if **usbethaddr** is already
set.

Then start the USB subsystem:

.. code-block:: console

   => usb start

The default behavior of U-Boot is to utilize all information that a DHCP
server passes to us when the user issues the **dhcp** command. This will
include the dhcp parameter *next-server* which indicates where to fetch
files from via TFTP. There may be times however where the dhcp server on
your network provides incorrect information and you are unable to modify
the server. In this case the following steps can be helpful:

.. code-block:: console

   => setenv autoload no
   => dhcp
   => setenv serverip correct.server.ip
   => tftp

Another alternative is to utilize the full syntax of the tftp command:

.. code-block:: console

   => setenv autoload no
   => dhcp
   => tftp ${loadaddr} server.ip:fileName
