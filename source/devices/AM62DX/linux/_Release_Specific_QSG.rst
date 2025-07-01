.. rubric:: Quick Start Guide

Thanks for your interest in |__SDK_FULL_NAME__|.
In this section, we describe the basic steps needed to start development using the SDK.

For more detailed documentation, refer to :ref:`overview-getting-started`

.. rubric:: Steps for SDK installation

Refer to section :ref:`download-and-install-sdk`
for instructions on running the SDK installer.

.. rubric:: Setting up host environment

Once the installer is run, you can setup your host environment with a few steps.
Run the following scripts to achieve this:

* :file:`setup.sh` to install all host packages needed for development.

Detailed steps are described at :ref:`run-setup-scripts`

.. rubric:: Hardware EVM setup

The AM62D EVM is a software kit that combines the AM62D
SOC and other important platform specific hardware like PMIC, DDR memory,
etc, on a single board.

Detailed instructions for EVM setup with image illustration can be found at
:ref:`hardware-evm-setup`.
Refer to this to setup your EVM as well as for instructions for booting with the default card.

The preferred way for starting SDK development is SD card boot. The section referenced above
describes pin settings to set the EVM in SD boot mode.

.. rubric:: Running out of the box demo

By default, the SD card comes with pre-built Linux SDK binaries flashed. This will allow
you to quickly verify the EVM functionality with just a monitor with an HDMI port.

Insert the SD card with pre-built binaries and boot the EVM. After successful bootup,
you should see a welcome message on the display wallpaper.

.. rubric:: Flashing release binaries
   :name: qsg-flashing-release-binaries

The SDK Installer packages latest pre-built binaries and filesystem for the target.
For detailed steps on flashing these binaries on the SD card, refer to the section
format your SD card and flash all the pre-built binaries from the SDK release,
:ref:`processor-sdk-linux-create-sd-card`.

You should be able to verify the same out of box demo after flashing the SD card.
This step should be used only when you want to completely overwrite the card with
release binaries.

.. rubric:: Illustration for simple kernel build and install to target

For most users, an important step in development is the ability to customize
baseport software components like bootloader, Linux kernel, hypervisor, etc.
This SDK allows you to build these components and install the built binaries
for target EVM. This step allows you to verify that your host environment
is configured correctly, and you can build and install these components.

For detailed instructions on building BSP components, refer to the section
:ref:`top-level-makefile`.
You should run the following commands in the installer directory:

* Build all components using :code:`make all`
* Follow the section **Installing to SD card rootfs**
* Follow the section **Installing boot binaries**

After you build and copy all the binaries to your SD card, you can boot the
EVM with binaries built on your host. Upon successful bootup, you should see
a different wallpaper on the display. This should confirm that your updates
are copied correctly in the SD card. Also, you can run the following command
on the target to verify that you are using the newly-built Linux kernel.

.. code-block:: console

   root@<machine>:~# cat /proc/version

The output should indicate the build date, host PC name, etc. This verifies
that your SDK has been setup correctly, enabling you to start development.
