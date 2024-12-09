How to verify IPC between Linux and MCU R5 in Keystone devices?
==================================================================

Automotive applications have different memory needs and use a different memory
map defined in the auto-common.dtbo file. Therefore, the default |__SDK_FULL_NAME__|
is shipped with firmwares for only a few auxiliary cores in the Keystone devices.

Although the out-of-the-box experience does not allow to verify the
interprocessor communication (IPC) between Linux and the MCU R5,
the following steps describe how this can be done using the SDK.

.. rubric:: Steps to build IPC echotest binaries
   :name: faq-steps-to-build-ipc-echotest-binaries

All the IPC echotest binaries are built as a Yocto package **ipc-lld-fw**.
Since these binaries conflict with the automotive demos, this package is not
built in the SDK installed by default. This can be built using Yocto and installed
into the filesystem on target.

Make sure that you have setup the Yocto build environment for this. Refer to
`Building the SDK <../../Overview_Building_the_SDK.html>`__ section for all details.

Once the Yocto build is setup, use bitbake to build the specific package ipc-lld-fw
as shown below:

::

    TOOLCHAIN_BASE=<PATH_TO_TOOLCHAIN> MACHINE=<machine> bitbake -k ipc-lld-fw

This will create the firmware package for all the remoteproc cores in the system
where the IPC echotest functionality is implemented. The package will be located
at the directory **<Yocto work directory>/j7_evm-linux/ipc-lld-fw/<version>/deploy-ipks/**.

.. rubric:: Installing the IPC echotest binaries
   :name: faq-installing-ipc-echotest-binaries


Once the package is built on the host machine, copy it to the target filesystem.
Run thethe  following commands to install the package to target filesystem.

The **update-alternatives** command in the below instructions will set the priority
for the IPC firmware very high. This is to ensure that the symlinks are updated
appropriately. Typical firmwares will have priorities up to 20, setting the IPC
firmware priority to 100 gives it highest priority.

.. note::

    priority override is done only for the automotive firmwares like ethernet firmware
    and display sharing firmware. If you have installed additional firmwares,
    you should do it for others as well.

::

    opkg install ipc-lld-fw*.ipk
    update-alternatives --install /lib/firmware/j7-main-r5f0_0-fw j7-main-r5f0_0-fw /lib/firmware/pdk-ipc/ipc_echo_test_mcu2_0_release.strip.xer5f 100
    update-alternatives --install /lib/firmware/j7-main-r5f0_1-fw j7-main-r5f0_1-fw /lib/firmware/pdk-ipc/ipc_echo_test_mcu2_1_release.strip.xer5f 100


After this, make sure that all the firmwares are pointing to the pdk-ipc/
version of the binaries by running the following:

::

    ls -l /lib/firmware/j7*

Reboot the board and you will see the IPC echotest binaries loaded onto different
CPU cores.

