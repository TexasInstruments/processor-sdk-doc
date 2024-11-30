.. _pi-hdr-programming:

#############################
RPi 40-pin header programming
#############################

TI |__PART_FAMILY_NAME__| SK development board contain a 40 pin GPIO
header, similar to the 40 pin header in the Raspberry Pi. These GPIOs can be
controlled for digital input and output using the Python/CPP libraries provided in the
TI GPIO Library packages. The libraries have the same API as the RPi.GPIO
library for Raspberry Pi in order to provide an easy way to move applications
running on the Raspberry Pi to the TI board.

TI GPIO Libraries are packaged under ``/opt`` directory. Run the below script
to build and install the gpio libraries

.. code-block:: console

   /opt/edgeai-gst-apps# ./scripts/install_ti_gpio_libs.sh

By default, the 40-pin header is not enabled on |__PART_FAMILY_NAME__| SK board. This can be enabled by
specifying the dtb overlay file ``k3-am62p5-sk-rpi-hdr-ehrpwm.dtbo`` in
``/run/media/BOOT-mmcblk1p1/uEnv.txt`` as given below.

``name_overlays=ti/k3-am62p5-sk-rpi-hdr-ehrpwm.dtbo``

Reboot the board after editing and saving the file.

.. _pub_edgeai_default_pin_setup:

***********************************
40-pin header default configuration
***********************************

The default pin configuration on the |__PART_FAMILY_NAME__| SK board is as follows. Any deviation from this
needs modifications to the Linux DTBO. The table below lists pin numbers in all three
supported modes, namely BOARD, BCM, and SOC.

BOARD: **Physical Pin Number**
BCM  : **Broadcom SOC Numbering**
SOC  : **TI SOC Naming**

.. csv-table::
    :header: "BOARD","BCM","SOC","Function"

    "3",   "2",   "GPIO0_44",       "I2C2 SDA"
    "5",   "3",   "GPIO0_43",       "I2C2 SCL"
    "8",   "14",  "GPIO1_25",       "GPIO"
    "10",  "15",  "GPIO1_24",       "GPIO"
    "11",  "17",  "GPIO1_11",       "GPIO"
    "13",  "27",  "GPIO0_42",       "GPIO"
    "15",  "22",  "GPIO1_22",       "GPIO"
    "16",  "23",  "GPIO0_38",       "GPIO"
    "18",  "24",  "GPIO0_39",       "GPIO"
    "19",  "10",  "GPIO1_18",       "GPIO"
    "21",  "9",   "GPIO1_19",       "GPIO"
    "22",  "25",  "GPIO0_14",       "GPIO"
    "23",  "11",  "GPIO1_17",       "GPIO"
    "24",  "8",   "GPIO1_15",       "HW PWM"
    "26",  "7",   "GPIO1_16",       "HW PWM"
    "29",  "5",   "GPIO0_36",       "GPIO"
    "31",  "6",   "GPIO0_33",       "GPIO"
    "32",  "12",  "GPIO0_40",       "GPIO"
    "33",  "13",  "GPIO1_10",       "HW PWM"
    "36",  "16",  "GPIO1_09",       "HW PWM"
    "37",  "26",  "GPIO0_41",       "GPIO"

**NOTE**: Please refer to `SK-AM62P User's Guide <https://www.ti.com/lit/ug/spruja2/spruja2.pdf>`_
for details on the expansion header pin names and functionality.

************
Repositories
************

The Python and CPP projects are hosted on Texas Instruments GitHub. The links to the projects
are given below. The details on installation and testing can be found in the respective project
documentation.

**Python Library**: https://github.com/TexasInstruments/ti-gpio-py.git

**CPP Library**: https://github.com/TexasInstruments/ti-gpio-cpp.git

The above repositories are cloned and installed during the yocto build process under ``/opt/``.
The ``gpiozero`` library is also installed as a part of the yocto build.

*********************
Additional References
*********************

Please refer to the link below for information on the 40-pin header numbering and naming conventions:

| https://pinout.xyz/#
