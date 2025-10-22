.. http://processors.wiki.ti.com/index.php/How_to_Change_dtb_File

How to change dtb files
=========================================

.. rubric:: Introduction
   :name: introduction-change-dtb-file

.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family', 'AM57X_family')

    In some scenarios, it is required to manually change the dtb file used
    by the target. For example, AM437X GP EVM uses LCD display by default.
    But it also supports HDMI display. In order to switch from LCD display
    to HDMI display, user needs to set the dtb file as desired.

.. ifconfig:: CONFIG_part_family in ('J7_family')

    In some scenarios, it is required to manually change the dtb file used
    by the target. For example, J721E GP EVM uses HDMI and Display port displays.
    In order to use these displays, user needs to use desired device tree overlay (dtbo)

.. rubric:: Specify dtb File
   :name: specify-dtb-file

.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family', 'AM57X_family')

    The dtb files are located on the target filesystem under "/boot/dtb"
    directory. First, identify the dtb file to be used, e.g.,
    am437x-gp-evm-hdmi.dtb for AM437X GP EVM with HDMI display.

    Then, modify "uEnv.txt" on the boot partition ("/run/media/mmcblk0p1"
    directory on filesystem) to specify fdtfile with the desired dtb file
    name.

    Using AM4 as the example, the default uEnv.txt has the lines below.
    Follow the instructions to set fdtfile so that HDMI display can be
    enabled. In order to go back to LCD dispaly, unset fdtfile to use the
    default am437x-gp-evm.dtb.

    ::

        # Uncomment the following line to enable HDMI display and disable LCD display.
        #fdtfile=am437x-gp-evm-hdmi.dtb

    After the dtb file is changed, reboot the EVM so that the new dtb file
    will be used for booting the EVM.

.. ifconfig:: CONFIG_part_family in ('J7_family')

    The dtb and dtbo files are located on the target filesystem under "/boot"
    directory. First, identify the dtb file to be used, e.g.,
    k3-j721e-common-proc-board.dtb for J721E GP EVM. Then identify a list of
    dtbo to be used e.g. k3-j721e-common-proc-board-infotainment.dtbo for
    infotainment daughter card.

    Then, modify "uEnv.txt" on the boot partition to specify fdtfile
    with the desired dtb file name, and overlay_files with list of dtbo files.

    After the dtb file is changed, reboot the EVM so that the new dtb file
    will be used for booting the EVM.

    .. rubric:: Device tree options
       :name: device-tree-options

    Depending on the use case, user would want to pass different device trees to
    the kernel. Starting with 4.19 kernel, device tree overlay support has been
    added. This allows supplying additional device tree fragments (aka overlays)
    to be applied on top of the base device tree.

    Typically, base dtb describes the base board on which the kernel is supposed
    to run. It contains the hardware description of the SoC, i.e. embedded interconnect,
    all peripherals,registers, memories, interrupts, etc. Also, it contains any
    board specific hardware description like pinmux, board mux, PHYs, PMIC, etc.

    All the additional daughter cards are modelled as separate device tree overlay.
    It contains the hardware description of all the peripherals available on the
    adapter card. Bootloader does not support auto loading of these overlays, so
    user has to specify the list of overlays, i.e. dtbo files to be applied before
    passing the final device tree to kernel.

    Typical usage for device tree has been to describe the hardware using standard
    bindings. However, for the application use cases, you may want to pass additional
    data to the kernel drivers. e.g. In a virtualized environment, you may want
    to describe which display pipelines are to be used by the display driver.
    Device nodes is a good way to to this. Processor SDK has few use case specific
    dtbo files which describe these additional properties.

    Following table describes list of device tree blob (dtb) and device tree overlay(dtbo)
    files available for different platforms and any associated dependencies.

    +-----+--------------------------------------------------------------+---------------------------------------------------------+---------------------------------------------------+
    | No  |                         Name of file                         |                       Description                       |                   dependencies                    |
    +=====+==============================================================+=========================================================+===================================================+
    | 1   | k3-j721e-common-proc-board.dtb                               | Base DTB for J721e EVM beta version                     | N/A                                               |
    +-----+--------------------------------------------------------------+---------------------------------------------------------+---------------------------------------------------+
    | 2   | k3-j721e-proc-board-tps65917.dtb                             | Base DTB for J721e EVM alpha version                    | N/A                                               |
    +-----+--------------------------------------------------------------+---------------------------------------------------------+---------------------------------------------------+
    | 3   | k3-j721e-common-proc-board-infotainment.dtbo                 | Overlay for IVI adapter card                            | IVI card needs to be connected                    |
    +-----+--------------------------------------------------------------+---------------------------------------------------------+---------------------------------------------------+
    | 4   | k3-j721e-common-proc-board-infotainment-display-sharing.dtbo | Overlay for sharing DSS with Linux and RTOS             | #3 DTBO should be applied before this             |
    +-----+--------------------------------------------------------------+---------------------------------------------------------+---------------------------------------------------+
    | 5   | k3-j721e-vision-apps.dtbo                                    | Overlay for running Processor SDK RTOS demos            | N/A                                               |
    +-----+--------------------------------------------------------------+---------------------------------------------------------+---------------------------------------------------+
    | 6   | k3-j721e-pcie-backplane.dtbo                                 | Overlay for running PCIe Backplane demo                 | N/A                                               |
    +-----+--------------------------------------------------------------+---------------------------------------------------------+---------------------------------------------------+
    | 7   | k3-j7200-common-proc-board.dtb                               | Base DTB for J7200 EVM                                  | N/A                                               |
    +-----+--------------------------------------------------------------+---------------------------------------------------------+---------------------------------------------------+

    .. rubric:: uEnv.txt options
       :name: uEnv.txt-options

    uEnv.txt file from the boot partition of SD card describes the base DTB to
    be used and any other overlay DTBOs to be applied additionally. Processor SDK
    comes with few ready made uEnv.txt files for quick consumption to run certain
    application demos.

    Following table describes usage of uenv.txt and associated dependencies
    for booting the board in different scenarios. Note that the u-boot supports
    detecting the right version of the board (alpha/beta) and can load the required
    base dtb file correctly. There is no need to specify the fdtfile in the uenv.txt.

    +----------------------------+-------------------------------------------------------------------------------+------------------------------------------------------------+
    |     Name of file           |                                Usage scenario                                 |                        Dependencies                        |
    +============================+===============================================================================+============================================================+
    | uenv.txt.base              | Use for booting the common processor board without support for daugter cards. |                                                            |
    |                            | Even if you have daughter cards connected, you can boot using this,           |                                                            |
    |                            | kernel will not use the extra device functionality.                           | N/A                                                        |
    +----------------------------+-------------------------------------------------------------------------------+------------------------------------------------------------+
    | uenv.txt.disp_sharing      | Use for running shared display use cases with Linux and RTOS                  | HDMI monitor connected via infotainment daughter card.     |
    |                            |                                                                               |                                                            |
    +----------------------------+-------------------------------------------------------------------------------+------------------------------------------------------------+
    | uenv.txt.jailhouse         | Use for running hypervisor use cases.                                         | HDMI monitor connected via infotainment daughter card.     |
    |                            |                                                                               | DP monitor connected to DISPLAY0 Display Port.             |
    +----------------------------+-------------------------------------------------------------------------------+------------------------------------------------------------+
    | uenv.psdkra                | Use for running Processor SDK RTOS demos.                                     | All the R5 and C6x firmware symlinks updated in filesystem |
    +----------------------------+-------------------------------------------------------------------------------+------------------------------------------------------------+

