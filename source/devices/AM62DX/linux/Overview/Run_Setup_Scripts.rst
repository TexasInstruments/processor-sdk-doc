.. _run-setup-scripts:

Run Setup Scripts
=================

.. rubric:: Overview
   :name: processor-sdk-linux-setup-script-overview

After installation of the SDK on the Linux host, the setup script
should be run to prepare the host for software development. Some of
the tasks require administrator privileges. The script will prompt you
when these administrator privileges are required. The setup script
does the following things:

-  Verification that the Linux host is the recommended Ubuntu LTS
   version
-  Installation of required host packages
-  Target FileSystem installation
-  NFS setup
-  TFTP setup
-  Minicom setup
-  uboot setup
-  Load uboot script

.. note::
    The host setup is common to all TI platforms.

.. Image:: /images/Linux_Host_Development_System.png


.. rubric:: How to run the setup script
   :name: how-to-run-the-setup-script

The Setup Script (**setup.sh**) is located in the |__SDK_FULL_NAME__| installation
directory. By default, this directory has a name that has the form
|__SDK_INSTALL_DIR__|.


Change to that ti-processor-sdk-linux install directory.
Then run the script:

**./setup.sh**

.. note::
    The Setup Script will first check to see if the user is running the
    recommended Ubuntu Long Term Support (LTS) distribution, if not it will
    exit. If the user is running on a different Ubuntu version or another
    Linux distribution, they are encouraged to modify the environment setup
    script to match their distribution. The 22.04 version of Ubuntu is
    currently supported.

.. rubric:: Detailed step by step description through the setup script
   :name: detailed-step-by-step-description-through-the-setup-script

The following sections describe in more detail how to run the script and
what it is doing.

.. rubric:: Installation of Required Host Packages
   :name: installation-of-required-host-packages

This section will check to make sure you have the proper host support
packages to allow you do the following tasks:

-  telnet
-  open menuconfig, the kernel configuration tool
-  mounting filesystem via nfs
-  tftp
-  open minicom
-  rebuild u-boot

If your host lacks any of the needed packages, they will automatically
be installed in this step.

.. note::
    This command requires you to have administrator priviliges (sudo access)
    on your host.

The command below is an example of what this script is doing. The actual
packages may vary for different releases:

**sudo apt-get install xinetd tftpd nfs-kernel-server minicom build-essential libncurses5-dev autoconf automake dos2unix screen lrzsz lzop u-boot-tools**

.. rubric:: Add to Dialout Group
   :name: add-to-dialout-group

.. note::
    This part requires you to have administrator priviliges (sudo access).

This step is required for users using Ubuntu 12.04+. By default the
user does not have the proper permissions to access a serial device ( ex
ttyS0, ttyUSB0, etc...). A user must be apart of a "dialout" group to
access these serial device without root privileges.

During this step the script will check if the current Linux user is
apart of the dialout group. If not the current Linux user will
automatically be added to the dialout group. The Linux user will still
be required to use sudo when accessing the serial device until the user
logs out and then logs back in.

.. rubric:: Target FileSystem Installation
   :name: target-filesystem-installation

This step will extract the target filesystem.

.. note::
    This part requires you to have administrator priviliges (sudo access).

The default location is:
/home/user/|__SDK_INSTALL_DIR__|/targetNFS

.. ifconfig:: CONFIG_sdk in ('SITARA')

    .. code-block:: text

        In which directory do you want to install the target filesystem?(if this directory does not exist it will be created)
        [ /home/user/ti-processor-sdk-linux-am62lxx-evm-<version>/targetNFS ]

You can override the default location by typing in another location or
by hitting <Enter> you can accept the default location. This can take a
little time to extract and unzip the filesytem.

If you have run this script more than once and the filesystem already
exists, you will be asked to either:

-  rename the filesystem
-  overwrite the filesystem
-  skip filesystem extraction

.. rubric:: NFS Setup
   :name: nfs-setup

This step will allow you to export your filesystem which was extracted
in the previous step.

.. note::
    This command requires you to have administrator priviliges (sudo
    access).

-  This step adds the path to root filesystem from the previous step to
   the file /etc/exports on your host.
-  The NFS kernel daemon is then stopped and then restarted to make sure
   the exported file system is recognized.

.. rubric:: TFTP Setup
   :name: tftp-setup

This section will setup tftp access on your host.

.. note::
    This command requires you to have administrator priviliges (sudo access)
    on your host.

.. code-block:: text

    Which directory do you want to be your tftp root directory?(if this directory does not exist it will be created for you)
    [ /tftpboot ]

The default location is /tftpboot which is off of the root directory on
your linux host and requires administrator privileges. You can hit
<Enter> to select the default location or type in another path to
override the default. Then the following task occur:

-  A tftp config file is created for you on your host at
   /etc/xinetd.d/tftp
-  The tftp server is stopped and then restarted to insure the changes
   are picked up.

If you have run this script more than once or the filename already
exists, you will be asked to select one of the following options.

-  rename the filesystem
-  overwrite the filesystem
-  skip filesystem extraction

Repeat this for any additional prompts about /tftpboot files.

.. rubric:: Minicom Setup
   :name: minicom-setup

This step will set up minicom (serial communication application) for SDK
development.

.. code-block:: text

    Which serial port do you want to use with minicom?
    [ /dev/ttyUSB0 ]

For most boards, the default /dev/ttyUSB0 should be selected.

.. note::
    If you are using a USB-to-Serial converter, your port should be
    configured for /dev/ttyUSBx.

.. ifconfig:: CONFIG_sdk in ('SITARA')

    .. rubric:: uboot Setup
       :name: uboot-setup

    This section will create the necessary u-boot commands to boot up your
    board.

    The script will detect your ip address and display it. You can override
    the detected value by entering an alternate value.

    ::

        This step will set up the u-boot variables for booting the EVM.
        Autodetected the following ip address of your host, correct it if necessary
        [ xxx.xxx.xxx.xxx ]

    Next, you will be prompted where you prefer your kernel and file system
    to be located.

    -  Kernel location

       -  TFTP - located on your Host in your designated /tftpboot directory
       -  SD card - located in the 1st partition named "boot" of your SD
          card

    -  Filesystem location

       -  NFS - located on your Host. The location is where the file system
          was extracted in an earlier step.
       -  SD card - located on the 2nd partition named "rootfs" of your SD
          card.


    Next if you have selected TFTP, you will be prompted which uImage you
    want to boot using TFTP. You will be given a list of existing uImage's
    and you can type one in from the list or hit <Enter> to select the
    default option. The default option will be the uImage corresponding to
    the SDK installation. This will be used in the next step to create the
    necessary u-boot options to boot up your device.

    .. rubric:: Load uboot Script
       :name: load-uboot-script

    This section creates a minicom script or a uEnv.txt file which will be
    used by u-boot to provide the necessary commands to boot up in the
    preferred configuration.

    -  For boards like AM62Px SK with a USB-to-Serial configuration, then a
       uEnv.txt script is created and placed in the /boot partition of the
       SD card.

    .. note::
        For devices which create a uEnv.txt, the device must already be booted
        up with the USB-to-Serial connector attached to the Host. Further the
        Host must recognize the boot and START\_HERE partitions.

|
