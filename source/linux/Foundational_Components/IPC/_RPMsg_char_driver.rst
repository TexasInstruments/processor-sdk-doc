RPMsg Char Driver
-----------------

The below picture depicts the kernel driver components and the user space device
model for using RPMsg Char driver for communicating with the remote processor.

.. Image:: /images/RPMsgstack-linux.png

The RPMsg char driver exposes RPMsg endpoints to user-space processes. Multiple
user-space applications can use one RPMsg device uniquely by requesting
different interactions with the remote service. The RPMsg char driver supports
the creation of multiple endpoints for each probed RPMsg char device, enabling
the use of the same device for different instances.

.. rubric:: RPMsg devices

Each created endpoint device shows up as a single character device in /dev.

The RPMsg bus sits on top of the VirtIO bus. Each virtio name service
announcement message creates a new RPMsg device, which is supposed to bind to a
RPMsg driver. RPMsg devices are created dynamically:

The remote processor announces the existence of a remote RPMsg service by
sending a name service announcement message containing the name of the service
(i.e. name of the device), source and destination addresses. The message is
handled by the RPMsg bus, which dynamically creates and registers an RPMsg
device which represents the remote service. As soon as a relevant RPMsg driver
is registered, it is immediately probed by the bus and the two sides can start
exchanging messages.

.. rubric:: The control interface

The RPMsg char driver provides control interface (in the form of a character
device under /dev/rpmsg_ctrlX) allowing user-space to export an endpoint
interface for each exposed endpoint. The control interface provides a
dedicated ioctl to create an endpoint device.

ti-rpmsg-char library
---------------------
The ti-rpmsg-char package is located at the `ti-rpmsg-char git repo
<https://git.ti.com/cgit/rpmsg/ti-rpmsg-char>`.

A thin userspace rpmsg char library is provided. The library abstracts the rpmsg
char driver usage from userspace. This library provides an easy means to
identify and open rpmsg character devices created by the kernel rpmsg-char
driver.

This library support TI K3 family of devices including |__PART_FAMILY_DEVICE_NAMES__|.

The library provides 4 basic APIs wrapping all the rpmsg char driver calls.
`Please check documentation in 'include/ti_rpmsg_char.h' for details.
<https://git.ti.com/cgit/rpmsg/ti-rpmsg-char/tree/include/ti_rpmsg_char.h>`__.

rpmsg_char_init()
    This function checks that the needed kernel drivers (remoteproc. rpmsg,
    virtio) are installed and accessible from the user space. Further it
    also checks the SoC device supports the requested remote processor.

rpmsg_char_exit()
    This function finalizes and performs all the de-initialization and any
    cleanup on the library. This is the last function that needs to be invoked
    after all usage is done as part of the application's cleanup. This only need
    to be invoked once in an application, there is no reference counting. The
    function also needs to be invoked in any application's signal handlers to
    perform the necessary cleanup of stale rpmsg endpoint devices.

rpmsg_char_open()
    Function to create and access a rpmsg endpoint device for a given rpmsg
    device.

rpmsg_char_close()
    Function to close and delete a previously created local endpoint

`All remote proc ids are defined in rproc_id.h <https://git.ti.com/cgit/rpmsg/ti-rpmsg-char/tree/include/rproc_id.h>`__

.. ifconfig:: CONFIG_part_variant in ('J721S2')

	The below table lists the device enumerations as defined in the
	rpmsg_char_library. The validity of the enumerations wrt J721S2 is also
	specified.

	.. code-block:: text

		+------------------+--------------------+---------+-----------------------------------+
		| Enumeration ID   | Device Name        | Valid   | Description                       |
		+==================+====================+=========+===================================+
		| R5F_MAIN0_0      | 5c00000.r5f        | Yes     | R5F core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| R5F_MAIN0_1      | 5d00000.r5f        | Yes     | R5F core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| R5F_MAIN1_0      | 5e00000.r5f        | Yes     | R5F core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| R5F_MAIN1_1      | 5f00000.r5f        | Yes     | R5F core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| R5F_MCU0_0       | 41000000.r5f       | Yes     | R5F core in MCU Domain            |
		+------------------+--------------------+---------+-----------------------------------+
		| R5F_MCU0_1       | 41400000.r5f       | Yes     | R5F core in MCU Domain            |
		+------------------+--------------------+---------+-----------------------------------+
		| DSP_c71_0        | 64800000.dsp       | Yes     | DSP core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| DSP_c71_0        | 65800000.dsp       | Yes     | DSP core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+


.. ifconfig:: CONFIG_part_variant in ('J784S4')

	The below table lists the device enumerations as defined in the
	rpmsg_char_library. The validity of the enumerations wrt J784S4 is also
	specified.

	.. code-block:: text

		+------------------+--------------------+---------+-----------------------------------+
		| Enumeration ID   | Device Name        | Valid   | Description                       |
		+==================+====================+=========+===================================+
		| R5F_MAIN0_0      | 5c00000.r5f        | Yes     | R5F core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| R5F_MAIN0_1      | 5d00000.r5f        | Yes     | R5F core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| R5F_MAIN1_0      | 5e00000.r5f        | Yes     | R5F core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| R5F_MAIN1_1      | 5f00000.r5f        | Yes     | R5F core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| R5F_MAIN2_0      | 5900000.r5f        | Yes     | R5F core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| R5F_MAIN2_1      | 5a00000.r5f        | Yes     | R5F core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| R5F_MCU0_0       | 41000000.r5f       | Yes     | R5F core in MCU Domain            |
		+------------------+--------------------+---------+-----------------------------------+
		| R5F_MCU0_1       | 41400000.r5f       | Yes     | R5F core in MCU Domain            |
		+------------------+--------------------+---------+-----------------------------------+
		| DSP_c71_0        | 64800000.dsp       | Yes     | DSP core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| DSP_c71_1        | 65800000.dsp       | Yes     | DSP core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| DSP_c71_2        | 66800000.dsp       | Yes     | DSP core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| DSP_c71_3        | 67800000.dsp       | Yes     | DSP core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+

.. ifconfig:: CONFIG_part_variant in ('J742S2')

	J742S2 is a subset device of J784S4 and hence reuses the device enumerations
	from J784S4. The below table lists the device enumerations as defined in the
	rpmsg_char_library. The validity of the enumerations wrt J742S2 is also
	specified.

	.. code-block:: text

		+------------------+--------------------+---------+-----------------------------------+
		| Enumeration ID   | Device Name        | Valid   | Description                       |
		+==================+====================+=========+===================================+
		| R5F_MAIN0_0      | 5c00000.r5f        | Yes     | R5F core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| R5F_MAIN0_1      | 5d00000.r5f        | Yes     | R5F core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| R5F_MAIN1_0      | 5e00000.r5f        | Yes     | R5F core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| R5F_MAIN1_1      | 5f00000.r5f        | Yes     | R5F core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| R5F_MAIN2_0      | 5900000.r5f        | Yes     | R5F core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| R5F_MAIN2_1      | 5a00000.r5f        | Yes     | R5F core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| R5F_MCU0_0       | 41000000.r5f       | Yes     | R5F core in MCU Domain            |
		+------------------+--------------------+---------+-----------------------------------+
		| R5F_MCU0_1       | 41400000.r5f       | Yes     | R5F core in MCU Domain            |
		+------------------+--------------------+---------+-----------------------------------+
		| DSP_c71_0        | 64800000.dsp       | Yes     | DSP core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| DSP_c71_1        | 65800000.dsp       | Yes     | DSP core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| DSP_c71_2        | 66800000.dsp       | Yes     | DSP core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| DSP_c71_3        | 67800000.dsp       | No      | DSP core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+

.. ifconfig:: CONFIG_part_variant in ('J722S')

	The below table lists the device enumerations as defined in the
	rpmsg_char_library. The validity of the enumerations wrt J722S is also
	specified.

	.. code-block:: text

		+------------------+--------------------+---------+-----------------------------------+
		| Enumeration ID   | Device Name        | Valid   | Description                       |
		+==================+====================+=========+===================================+
		| R5F_MAIN0_0      | 78400000.r5f       | Yes     | R5F core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| R5F_MCU0_0       | 79000000.r5f       | Yes     | R5F core in MCU Domain            |
		+------------------+--------------------+---------+-----------------------------------+
		| DSP_c71_0        | 7e000000.dsp       | Yes     | DSP core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| DSP_c71_1        | 7e200000.dsp       | Yes     | DSP core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+


.. ifconfig::  CONFIG_part_variant in ('J721E')

	The below table lists the device enumerations as defined in the
	rpmsg_char_library. The validity of the enumerations wrt J721E is also
	specified.

	.. code-block:: text

		+------------------+--------------------+---------+-----------------------------------+
		| Enumeration ID   | Device Name        | Valid   | Description                       |
		+==================+====================+=========+===================================+
		| R5F_MCU0_0       | 41000000.r5f       | Yes     | R5F core(MCU domain)              |
		+------------------+--------------------+---------+------------+----------------------+
		| R5F_MCU0_1       | 41400000.r5f       | Yes     | R5F core(MCU domain)              |
		+------------------+--------------------+---------+------------+----------------------+
		| R5F_MAIN0_0      | 5c00000.r5f        | Yes     | R5F core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| R5F_MAIN0_1      | 5d00000.r5f        | Yes     | R5F core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| R5F_MAIN1_0      | 5e00000.r5f        | Yes     | R5F core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| R5F_MAIN1_1      | 5f00000.r5f        | Yes     | R5F core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| DSP_C66_0        | 4d80800000.dsp     | Yes     | DSP core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| DSP_C66_1        | 4d81800000.dsp     | Yes     | DSP core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| DSP_c71_0        | 64800000.dsp       | Yes     | DSP core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+
		| DSP_c71_1        | 65800000.dsp       | Yes     | DSP core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+

.. ifconfig::  CONFIG_part_variant in ('J7200')

	The below table lists the device enumerations as defined in the
	rpmsg_char_library. The validity of the enumerations wrt J7200 is also
	specified.

	.. code-block:: text

		+------------------+--------------------+---------+-----------------------------------+
		| Enumeration ID   | Device Name        | Valid   | Description                       |
		+==================+====================+=========+===================================+
		| R5F_MCU0_0       | 41000000.r5f       | Yes     | R5F core(MCU domain)              |
		+------------------+--------------------+---------+------------+----------------------+
		| R5F_MCU0_1       | 41400000.r5f       | Yes     | R5F core(MCU domain)              |
		+------------------+--------------------+---------+------------+----------------------+
		| R5F_MAIN0_0      | 5c00000.r5f        | Yes     | R5F core(MAIN domain)             |
		+------------------+--------------------+---------+------------+----------------------+
		| R5F_MAIN0_1      | 5d00000.r5f        | Yes     | R5F core(MAIN domain)             |
		+------------------+--------------------+---------+------------+----------------------+


.. ifconfig:: CONFIG_part_variant in ('AM62X')

	The below table lists the device enumerations as defined in the
	rpmsg_char_library. The validity of the enumerations wrt AM62x is also
	specified.

	.. code-block:: text

		+------------------+--------------------+---------+-----------------------------------+
		| Enumeration ID   | Device Name        | Valid   | Description                       |
		+==================+====================+=========+===================================+
		| M4F_MCU0_0       | 5000000.m4f        | Yes     | M4F core in MCU Domain            |
		+------------------+--------------------+---------+-----------------------------------+
		| R5F_WKUP0_0      | 78000000.r5f       | Yes     | R5F core in Wakeup Domain         |
		+------------------+--------------------+---------+-----------------------------------+


.. ifconfig:: CONFIG_part_variant in ('AM62AX')

	The below table lists the device enumerations as defined in the
	rpmsg_char_library. The validity of the enumerations wrt AM62Ax is also
	specified.

	.. code-block:: text

		+------------------+--------------------+---------+-----------------------------------+
		| Enumeration ID   | Device Name        | Valid   | Description                       |
		+==================+====================+=========+===================================+
		| R5F_WKUP0_0      | 78000000.r5f       | Yes     | R5F core in Wakeup Domain         |
		+------------------+--------------------+---------+-----------------------------------+
		| R5F_MCU0_0       | 79000000.r5f       | Yes     | R5F core in MCU Domain            |
		+------------------+--------------------+---------+-----------------------------------+
		| DSP_c71_0        | 7e000000.dsp       | Yes     | DSP core in Main Domain           |
		+------------------+--------------------+---------+-----------------------------------+


RPMsg examples:
---------------

.. rubric:: RPMsg user space example

.. note::
	These steps were tested on Ubuntu 18.04.
	Later versions of Ubuntu may need different steps

.. note::
	rpmsg_char_simple comes prepackaged in prebuilt SDK wic images (e.g. tisdk-default-image-j721s2-evm.wic.xz)
	that comes with the release and below example can be directly run (Step 6) if using the prebuilt wic images

Access source code in the git repo `here <https://git.ti.com/cgit/rpmsg/ti-rpmsg-char>`__.
rproc_id is defined at `include/rproc_id.h <https://git.ti.com/cgit/rpmsg/ti-rpmsg-char/tree/include/rproc_id.h>`__.

Build the Linux Userspace example for Linux RPMsg by following the steps
in the top-level README:

#. Download the git repo

#. Install GNU autoconf, GNU automake, GNU libtool, and v8 compiler as per the
   README

#. Perform the Build Steps as per the README

Linux RPMsg can be tested with prebuilt binaries that are packaged in the
SDK wic image filesystem:

#. Copy the Linux RPMsg Userspace application from
   <ti-rpmsg-char_repo>/examples/rpmsg_char_simple into the board's Linux
   filesystem.

#. Ensure that the remote core symbolic link points to the desired binary file
   in /lib/firmware/ti-ipc/j7xx/. Update the symbolic link if needed. Reference
   section :ref:`booting_remote_cores_from_Linux_console` for more information.

#. Run the example on the board:

.. code-block:: console

  Usage: rpmsg_char_simple [-r <rproc_id>] [-n <num_msgs>] [-d <rpmsg_dev_name] [-p <remote_endpt]
      Defaults: rproc_id: 0 num_msgs: 100 rpmsg_dev_name: NULL remote_endpt: 14

  For remote proc ids, please refer to : 'https://git.ti.com/cgit/rpmsg/ti-rpmsg-char/tree/include/rproc_id.h'

.. ifconfig:: CONFIG_part_variant in ('J721S2')

    .. code-block:: console

		# MCU R5F<->A72_0 IPC
		root@j721s2-evm:~# rpmsg_char_simple -r0 -n10
		Created endpt device rpmsg-char-0-1100, fd = 3 port = 1024
		Exchanging 10 messages with rpmsg device ti.ipc4.ping-pong on rproc id 0 ...

		Sending message #0: hello there 0!
		Receiving message #0: hello there 0!
		Sending message #1: hello there 1!
		Receiving message #1: hello there 1!
		Sending message #2: hello there 2!
		Receiving message #2: hello there 2!
		Sending message #3: hello there 3!
		Receiving message #3: hello there 3!
		Sending message #4: hello there 4!
		Receiving message #4: hello there 4!
		Sending message #5: hello there 5!
		Receiving message #5: hello there 5!
		Sending message #6: hello there 6!
		Receiving message #6: hello there 6!
		Sending message #7: hello there 7!
		Receiving message #7: hello there 7!
		Sending message #8: hello there 8!
		Receiving message #8: hello there 8!
		Sending message #9: hello there 9!
		Receiving message #9: hello there 9!

		Communicated 10 messages successfully on rpmsg-char-0-1100

		TEST STATUS: PASSED

		# C7x<->A72_0 IPC
		root@j721s2-evm:~# rpmsg_char_simple -r8 -n10
		Created endpt device rpmsg-char-8-1107, fd = 3 port = 1024
		Exchanging 10 messages with rpmsg device ti.ipc4.ping-pong on rproc id 8 ...

		Sending message #0: hello there 0!
		Receiving message #0: hello there 0!
		Sending message #1: hello there 1!
		Receiving message #1: hello there 1!
		Sending message #2: hello there 2!
		Receiving message #2: hello there 2!
		Sending message #3: hello there 3!
		Receiving message #3: hello there 3!
		Sending message #4: hello there 4!
		Receiving message #4: hello there 4!
		Sending message #5: hello there 5!
		Receiving message #5: hello there 5!
		Sending message #6: hello there 6!
		Receiving message #6: hello there 6!
		Sending message #7: hello there 7!
		Receiving message #7: hello there 7!
		Sending message #8: hello there 8!
		Receiving message #8: hello there 8!
		Sending message #9: hello there 9!
		Receiving message #9: hello there 9!

		Communicated 10 messages successfully on rpmsg-char-8-1107

		TEST STATUS: PASSED

.. ifconfig:: CONFIG_part_variant in ('J784S4','J742S2')

    .. code-block:: console

		# MCU R5F<->A72_0 IPC
		root@j784s4-evm:~# rpmsg_char_simple -r0 -n10
		Created endpt device rpmsg-char-0-795, fd = 4 port = 1026
		Exchanging 10 messages with rpmsg device ti.ipc4.ping-pong on rproc id 0 ...

		Sending message #0: hello there 0!
		Receiving message #0: hello there 0!
		Sending message #1: hello there 1!
		Receiving message #1: hello there 1!
		Sending message #2: hello there 2!
		Receiving message #2: hello there 2!
		Sending message #3: hello there 3!
		Receiving message #3: hello there 3!
		Sending message #4: hello there 4!
		Receiving message #4: hello there 4!
		Sending message #5: hello there 5!
		Receiving message #5: hello there 5!
		Sending message #6: hello there 6!
		Receiving message #6: hello there 6!
		Sending message #7: hello there 7!
		Receiving message #7: hello there 7!
		Sending message #8: hello there 8!
		Receiving message #8: hello there 8!
		Sending message #9: hello there 9!
		Receiving message #9: hello there 9!

		Communicated 10 messages successfully on rpmsg-char-0-795

		TEST STATUS: PASSED

		# R5F_MAIN0_1<->A72_0 IPC
		root@j784s4-evm:~# rpmsg_char_simple -r3 -n10
		Created endpt device rpmsg-char-3-801, fd = 4 port = 1026
		Exchanging 10 messages with rpmsg device ti.ipc4.ping-pong on rproc id 3 ...

		Sending message #0: hello there 0!
		Receiving message #0: hello there 0!
		Sending message #1: hello there 1!
		Receiving message #1: hello there 1!
		Sending message #2: hello there 2!
		Receiving message #2: hello there 2!
		Sending message #3: hello there 3!
		Receiving message #3: hello there 3!
		Sending message #4: hello there 4!
		Receiving message #4: hello there 4!
		Sending message #5: hello there 5!
		Receiving message #5: hello there 5!
		Sending message #6: hello there 6!
		Receiving message #6: hello there 6!
		Sending message #7: hello there 7!
		Receiving message #7: hello there 7!
		Sending message #8: hello there 8!
		Receiving message #8: hello there 8!
		Sending message #9: hello there 9!
		Receiving message #9: hello there 9!

		Communicated 10 messages successfully on rpmsg-char-3-801

		TEST STATUS: PASSED

		# DSP_C71_2<->A72_0 IPC
		root@j784s4-evm:~# rpmsg_char_simple -r13 -n10
		Created endpt device rpmsg-char-13-799, fd = 4 port = 1026
		Exchanging 10 messages with rpmsg device ti.ipc4.ping-pong on rproc id 13 ...

		Sending message #0: hello there 0!
		Receiving message #0: hello there 0!
		Sending message #1: hello there 1!
		Receiving message #1: hello there 1!
		Sending message #2: hello there 2!
		Receiving message #2: hello there 2!
		Sending message #3: hello there 3!
		Receiving message #3: hello there 3!
		Sending message #4: hello there 4!
		Receiving message #4: hello there 4!
		Sending message #5: hello there 5!
		Receiving message #5: hello there 5!
		Sending message #6: hello there 6!
		Receiving message #6: hello there 6!
		Sending message #7: hello there 7!
		Receiving message #7: hello there 7!
		Sending message #8: hello there 8!
		Receiving message #8: hello there 8!
		Sending message #9: hello there 9!
		Receiving message #9: hello there 9!

		Communicated 10 messages successfully on rpmsg-char-13-799

		TEST STATUS: PASSED

.. ifconfig:: CONFIG_part_variant in ('J722S')

    .. code-block:: console

		root@j722s-evm:~/ti-rpmsg-char/examples# ./rpmsg_char_simple -r 15 -n 10
		Created endpt device rpmsg-char-15-628, fd = 4 port = 1025
		Exchanging 10 messages with rpmsg device ti.ipc4.ping-pong on rproc id 15 ...

		Sending message #0: hello there 0!
		Receiving message #0: hello there 0!
		Sending message #1: hello there 1!
		Receiving message #1: hello there 1!
		Sending message #2: hello there 2!
		Receiving message #2: hello there 2!
		Sending message #3: hello there 3!
		Receiving message #3: hello there 3!
		Sending message #4: hello there 4!
		Receiving message #4: hello there 4!
		Sending message #5: hello there 5!
		Receiving message #5: hello there 5!
		Sending message #6: hello there 6!
		Receiving message #6: hello there 6!
		Sending message #7: hello there 7!
		Receiving message #7: hello there 7!
		Sending message #8: hello there 8!
		Receiving message #8: hello there 8!
		Sending message #9: hello there 9!
		Receiving message #9: hello there 9!

		Communicated 10 messages successfully on rpmsg-char-15-628

		TEST STATUS: PASSED
		root@j722s-evm:~/ti-rpmsg-char/examples# ./rpmsg_char_simple -r 0 -n 10
		Created endpt device rpmsg-char-0-630, fd = 4 port = 1025
		Exchanging 10 messages with rpmsg device ti.ipc4.ping-pong on rproc id 0 ...

		Sending message #0: hello there 0!
		Receiving message #0: hello there 0!
		Sending message #1: hello there 1!
		Receiving message #1: hello there 1!
		Sending message #2: hello there 2!
		Receiving message #2: hello there 2!
		Sending message #3: hello there 3!
		Receiving message #3: hello there 3!
		Sending message #4: hello there 4!
		Receiving message #4: hello there 4!
		Sending message #5: hello there 5!
		Receiving message #5: hello there 5!
		Sending message #6: hello there 6!
		Receiving message #6: hello there 6!
		Sending message #7: hello there 7!
		Receiving message #7: hello there 7!
		Sending message #8: hello there 8!
		Receiving message #8: hello there 8!
		Sending message #9: hello there 9!
		Receiving message #9: hello there 9!

		Communicated 10 messages successfully on rpmsg-char-0-630

		TEST STATUS: PASSED
		root@j722s-evm:~/ti-rpmsg-char/examples# ./rpmsg_char_simple -r 2 -n 10
		Created endpt device rpmsg-char-2-632, fd = 4 port = 1025
		Exchanging 10 messages with rpmsg device ti.ipc4.ping-pong on rproc id 2 ...

		Sending message #0: hello there 0!
		Receiving message #0: hello there 0!
		Sending message #1: hello there 1!
		Receiving message #1: hello there 1!
		Sending message #2: hello there 2!
		Receiving message #2: hello there 2!
		Sending message #3: hello there 3!
		Receiving message #3: hello there 3!
		Sending message #4: hello there 4!
		Receiving message #4: hello there 4!
		Sending message #5: hello there 5!
		Receiving message #5: hello there 5!
		Sending message #6: hello there 6!
		Receiving message #6: hello there 6!
		Sending message #7: hello there 7!
		Receiving message #7: hello there 7!
		Sending message #8: hello there 8!
		Receiving message #8: hello there 8!
		Sending message #9: hello there 9!
		Receiving message #9: hello there 9!

		Communicated 10 messages successfully on rpmsg-char-2-632

		TEST STATUS: PASSED
		root@j722s-evm:~/ti-rpmsg-char/examples# ./rpmsg_char_simple -r 8 -n 10
		Created endpt device rpmsg-char-8-633, fd = 4 port = 1025
		Exchanging 10 messages with rpmsg device ti.ipc4.ping-pong on rproc id 8 ...

		Sending message #0: hello there 0!
		Receiving message #0: hello there 0!
		Sending message #1: hello there 1!
		Receiving message #1: hello there 1!
		Sending message #2: hello there 2!
		Receiving message #2: hello there 2!
		Sending message #3: hello there 3!
		Receiving message #3: hello there 3!
		Sending message #4: hello there 4!
		Receiving message #4: hello there 4!
		Sending message #5: hello there 5!
		Receiving message #5: hello there 5!
		Sending message #6: hello there 6!
		Receiving message #6: hello there 6!
		Sending message #7: hello there 7!
		Receiving message #7: hello there 7!
		Sending message #8: hello there 8!
		Receiving message #8: hello there 8!
		Sending message #9: hello there 9!
		Receiving message #9: hello there 9!

		Communicated 10 messages successfully on rpmsg-char-8-633

		TEST STATUS: PASSED
		root@j722s-evm:~/ti-rpmsg-char/examples# ./rpmsg_char_simple -r 10 -n 10
		Created endpt device rpmsg-char-10-634, fd = 4 port = 1025
		Exchanging 10 messages with rpmsg device ti.ipc4.ping-pong on rproc id 10 ...

		Sending message #0: hello there 0!
		Receiving message #0: hello there 0!
		Sending message #1: hello there 1!
		Receiving message #1: hello there 1!
		Sending message #2: hello there 2!
		Receiving message #2: hello there 2!
		Sending message #3: hello there 3!
		Receiving message #3: hello there 3!
		Sending message #4: hello there 4!
		Receiving message #4: hello there 4!
		Sending message #5: hello there 5!
		Receiving message #5: hello there 5!
		Sending message #6: hello there 6!
		Receiving message #6: hello there 6!
		Sending message #7: hello there 7!
		Receiving message #7: hello there 7!
		Sending message #8: hello there 8!
		Receiving message #8: hello there 8!
		Sending message #9: hello there 9!
		Receiving message #9: hello there 9!

		Communicated 10 messages successfully on rpmsg-char-10-634

		TEST STATUS: PASSED

.. ifconfig:: CONFIG_part_variant in ('J721E')

    .. code-block:: console

		# MCU R5F<->A72_0 IPC
		root@j721e-evm:~# rpmsg_char_simple -r0 -n10
		Created endpt device rpmsg-char-0-920, fd = 4 port = 1025
		Exchanging 10 messages with rpmsg device ti.ipc4.ping-pong on rproc id 0 ...

		Sending message #0: hello there 0!
		Receiving message #0: hello there 0!
		Sending message #1: hello there 1!
		Receiving message #1: hello there 1!
		Sending message #2: hello there 2!
		Receiving message #2: hello there 2!
		Sending message #3: hello there 3!
		Receiving message #3: hello there 3!
		Sending message #4: hello there 4!
		Receiving message #4: hello there 4!
		Sending message #5: hello there 5!
		Receiving message #5: hello there 5!
		Sending message #6: hello there 6!
		Receiving message #6: hello there 6!
		Sending message #7: hello there 7!
		Receiving message #7: hello there 7!
		Sending message #8: hello there 8!
		Receiving message #8: hello there 8!
		Sending message #9: hello there 9!
		Receiving message #9: hello there 9!

		Communicated 10 messages successfully on rpmsg-char-0-920

		TEST STATUS: PASSED

		# R5F_MAIN0_1<->A72_0 IPC
		root@j721e-evm:~# rpmsg_char_simple -r3 -n10
		Created endpt device rpmsg-char-3-925, fd = 4 port = 1025
		Exchanging 10 messages with rpmsg device ti.ipc4.ping-pong on rproc id 3 ...

		Sending message #0: hello there 0!
		Receiving message #0: hello there 0!
		Sending message #1: hello there 1!
		Receiving message #1: hello there 1!
		Sending message #2: hello there 2!
		Receiving message #2: hello there 2!
		Sending message #3: hello there 3!
		Receiving message #3: hello there 3!
		Sending message #4: hello there 4!
		Receiving message #4: hello there 4!
		Sending message #5: hello there 5!
		Receiving message #5: hello there 5!
		Sending message #6: hello there 6!
		Receiving message #6: hello there 6!
		Sending message #7: hello there 7!
		Receiving message #7: hello there 7!
		Sending message #8: hello there 8!
		Receiving message #8: hello there 8!
		Sending message #9: hello there 9!
		Receiving message #9: hello there 9!

		Communicated 10 messages successfully on rpmsg-char-3-925

		TEST STATUS: PASSED

		# C6x<->A72_0 IPC
		root@j721e-evm:~# rpmsg_char_simple -r6 -n10
		Created endpt device rpmsg-char-6-929, fd = 4 port = 1025
		Exchanging 10 messages with rpmsg device ti.ipc4.ping-pong on rproc id 6 ...

		Sending message #0: hello there 0!
		Receiving message #0: hello there 0!
		Sending message #1: hello there 1!
		Receiving message #1: hello there 1!
		Sending message #2: hello there 2!
		Receiving message #2: hello there 2!
		Sending message #3: hello there 3!
		Receiving message #3: hello there 3!
		Sending message #4: hello there 4!
		Receiving message #4: hello there 4!
		Sending message #5: hello there 5!
		Receiving message #5: hello there 5!
		Sending message #6: hello there 6!
		Receiving message #6: hello there 6!
		Sending message #7: hello there 7!
		Receiving message #7: hello there 7!
		Sending message #8: hello there 8!
		Receiving message #8: hello there 8!
		Sending message #9: hello there 9!
		Receiving message #9: hello there 9!

		Communicated 10 messages successfully on rpmsg-char-6-929

		TEST STATUS: PASSED

		# C7x<->A72_0 IPC
		root@j721e-evm:~# rpmsg_char_simple -r8 -n10
		Created endpt device rpmsg-char-8-927, fd = 4 port = 1025
		Exchanging 10 messages with rpmsg device ti.ipc4.ping-pong on rproc id 8 ...

		Sending message #0: hello there 0!
		Receiving message #0: hello there 0!
		Sending message #1: hello there 1!
		Receiving message #1: hello there 1!
		Sending message #2: hello there 2!
		Receiving message #2: hello there 2!
		Sending message #3: hello there 3!
		Receiving message #3: hello there 3!
		Sending message #4: hello there 4!
		Receiving message #4: hello there 4!
		Sending message #5: hello there 5!
		Receiving message #5: hello there 5!
		Sending message #6: hello there 6!
		Receiving message #6: hello there 6!
		Sending message #7: hello there 7!
		Receiving message #7: hello there 7!
		Sending message #8: hello there 8!
		Receiving message #8: hello there 8!
		Sending message #9: hello there 9!
		Receiving message #9: hello there 9!

		Communicated 10 messages successfully on rpmsg-char-8-927

		TEST STATUS: PASSED

.. ifconfig:: CONFIG_part_variant in ('J7200')

    .. code-block:: console

		# MCU R5F<->A72_0 IPC
		root@j7200-evm:~# rpmsg_char_simple -r0 -n10
		Created endpt device rpmsg-char-0-720, fd = 4 port = 1026
		Exchanging 10 messages with rpmsg device ti.ipc4.ping-pong on rproc id 0 ...

		Sending message #0: hello there 0!
		Receiving message #0: hello there 0!
		Sending message #1: hello there 1!
		Receiving message #1: hello there 1!
		Sending message #2: hello there 2!
		Receiving message #2: hello there 2!
		Sending message #3: hello there 3!
		Receiving message #3: hello there 3!
		Sending message #4: hello there 4!
		Receiving message #4: hello there 4!
		Sending message #5: hello there 5!
		Receiving message #5: hello there 5!
		Sending message #6: hello there 6!
		Receiving message #6: hello there 6!
		Sending message #7: hello there 7!
		Receiving message #7: hello there 7!
		Sending message #8: hello there 8!
		Receiving message #8: hello there 8!
		Sending message #9: hello there 9!
		Receiving message #9: hello there 9!

		Communicated 10 messages successfully on rpmsg-char-0-720

		TEST STATUS: PASSED

		# R5F_MAIN0_1<->A72_0 IPC
		root@j7200-evm:~# rpmsg_char_simple -r3 -n10
		Created endpt device rpmsg-char-3-738, fd = 4 port = 1026
		Exchanging 10 messages with rpmsg device ti.ipc4.ping-pong on rproc id 3 ...

		Sending message #0: hello there 0!
		Receiving message #0: hello there 0!
		Sending message #1: hello there 1!
		Receiving message #1: hello there 1!
		Sending message #2: hello there 2!
		Receiving message #2: hello there 2!
		Sending message #3: hello there 3!
		Receiving message #3: hello there 3!
		Sending message #4: hello there 4!
		Receiving message #4: hello there 4!
		Sending message #5: hello there 5!
		Receiving message #5: hello there 5!
		Sending message #6: hello there 6!
		Receiving message #6: hello there 6!
		Sending message #7: hello there 7!
		Receiving message #7: hello there 7!
		Sending message #8: hello there 8!
		Receiving message #8: hello there 8!
		Sending message #9: hello there 9!
		Receiving message #9: hello there 9!

		Communicated 10 messages successfully on rpmsg-char-3-738

		TEST STATUS: PASSED

.. ifconfig:: CONFIG_part_variant in ('AM62X')

	.. code-block:: console

		# M4F<->A53_0 IPC
		root@am62xx-evm:~# rpmsg_char_simple -r 9 -n 10
		Created endpt device rpmsg-char-9-989, fd = 3 port = 1024
		Exchanging 10 messages with rpmsg device ti.ipc4.ping-pong on rproc id 9 ...

		Sending message #0: hello there 0!
		Receiving message #0: hello there 0!
		Sending message #1: hello there 1!
		Receiving message #1: hello there 1!
		Sending message #2: hello there 2!
		Receiving message #2: hello there 2!
		Sending message #3: hello there 3!
		Receiving message #3: hello there 3!
		Sending message #4: hello there 4!
		Receiving message #4: hello there 4!
		Sending message #5: hello there 5!
		Receiving message #5: hello there 5!
		Sending message #6: hello there 6!
		Receiving message #6: hello there 6!
		Sending message #7: hello there 7!
		Receiving message #7: hello there 7!
		Sending message #8: hello there 8!
		Receiving message #8: hello there 8!
		Sending message #9: hello there 9!
		Receiving message #9: hello there 9!

		Communicated 10 messages successfully on rpmsg-char-9-989

		# R5f<->A53_0 IPC
		root@am62xx-evm:~# rpmsg_char_simple -r 15 -n 10
		Created endpt device rpmsg-char-15-1506, fd = 3 port = 1024
		Exchanging 10 messages with rpmsg device ti.ipc4.ping-pong on rproc id 15 ...

		Sending message #0: hello there 0!
		Receiving message #0: hello there 0!
		Sending message #1: hello there 1!
		Receiving message #1: hello there 1!
		Sending message #2: hello there 2!
		Receiving message #2: hello there 2!
		Sending message #3: hello there 3!
		Receiving message #3: hello there 3!
		Sending message #4: hello there 4!
		Receiving message #4: hello there 4!
		Sending message #5: hello there 5!
		Receiving message #5: hello there 5!
		Sending message #6: hello there 6!
		Receiving message #6: hello there 6!
		Sending message #7: hello there 7!
		Receiving message #7: hello there 7!
		Sending message #8: hello there 8!
		Receiving message #8: hello there 8!
		Sending message #9: hello there 9!
		Receiving message #9: hello there 9!

		Communicated 10 messages successfully on rpmsg-char-15-1506

		TEST STATUS: PASSED
		root@am62xx-evm:~#

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

	.. code-block:: console

		# MCU R5F<->A53_0 IPC
		root@am62axx-evm:~# rpmsg_char_simple -r0 -n10
		Created endpt device rpmsg-char-0-1069, fd = 3 port = 1024
		Exchanging 10 messages with rpmsg device ti.ipc4.ping-pong on rproc id 0 ...

		Sending message #0: hello there 0!
		Receiving message #0: hello there 0!
		Sending message #1: hello there 1!
		Receiving message #1: hello there 1!
		Sending message #2: hello there 2!
		Receiving message #2: hello there 2!
		Sending message #3: hello there 3!
		Receiving message #3: hello there 3!
		Sending message #4: hello there 4!
		Receiving message #4: hello there 4!
		Sending message #5: hello there 5!
		Receiving message #5: hello there 5!
		Sending message #6: hello there 6!
		Receiving message #6: hello there 6!
		Sending message #7: hello there 7!
		Receiving message #7: hello there 7!
		Sending message #8: hello there 8!
		Receiving message #8: hello there 8!
		Sending message #9: hello there 9!
		Receiving message #9: hello there 9!

		Communicated 10 messages successfully on rpmsg-char-0-1069

		TEST STATUS: PASSED

		# for DM R5F<->A53 IPC, use the below command. For remote proc ids, please refer to : 'https://git.ti.com/cgit/rpmsg/ti-rpmsg-char/tree/include/rproc_id.h'
		root@am62axx-evm:~# rpmsg_char_simple -r15 -n10
		Created endpt device rpmsg-char-15-127176, fd = 3 port = 1024
		Exchanging 10 messages with rpmsg device ti.ipc4.ping-pong on rproc id 15 ...

		Sending message #0: hello there 0!
		Receiving message #0: hello there 0!
		Sending message #1: hello there 1!
		Receiving message #1: hello there 1!
		Sending message #2: hello there 2!
		Receiving message #2: hello there 2!
		Sending message #3: hello there 3!
		Receiving message #3: hello there 3!
		Sending message #4: hello there 4!
		Receiving message #4: hello there 4!
		Sending message #5: hello there 5!
		Receiving message #5: hello there 5!
		Sending message #6: hello there 6!
		Receiving message #6: hello there 6!
		Sending message #7: hello there 7!
		Receiving message #7: hello there 7!
		Sending message #8: hello there 8!
		Receiving message #8: hello there 8!
		Sending message #9: hello there 9!
		Receiving message #9: hello there 9!

		Communicated 10 messages successfully on rpmsg-char-15-127176

		TEST STATUS: PASSED

		# C7x<->A53_0 IPC
		root@am62axx-evm:~# rpmsg_char_simple -r8 -n10
		Created endpt device rpmsg-char-8-127180, fd = 3 port = 1024
		Exchanging 10 messages with rpmsg device ti.ipc4.ping-pong on rproc id 8 ...

		Sending message #0: hello there 0!
		Receiving message #0: hello there 0!
		Sending message #1: hello there 1!
		Receiving message #1: hello there 1!
		Sending message #2: hello there 2!
		Receiving message #2: hello there 2!
		Sending message #3: hello there 3!
		Receiving message #3: hello there 3!
		Sending message #4: hello there 4!
		Receiving message #4: hello there 4!
		Sending message #5: hello there 5!
		Receiving message #5: hello there 5!
		Sending message #6: hello there 6!
		Receiving message #6: hello there 6!
		Sending message #7: hello there 7!
		Receiving message #7: hello there 7!
		Sending message #8: hello there 8!
		Receiving message #8: hello there 8!
		Sending message #9: hello there 9!
		Receiving message #9: hello there 9!

		Communicated 10 messages successfully on rpmsg-char-8-127180

		TEST STATUS: PASSED

.. rubric:: RPMsg kernel space example

The kernel space example is in the Linux Processor SDK under
samples/rpmsg/rpmsg_client_sample.c

Build the kernel module rpmsg_client_sample:
 .. note::
  rpmsg_client_sample comes prepackaged in prebuilt SDK wic images (e.g. tisdk-default-image-j721s2-evm.wic.xz)
  that comes with the release and below example can be directly run (Step 5) if using the prebuilt wic images

#. Set up the kernel config to build the rpmsg client sample.

Use menuconfig to verify Kernel hacking > Sample kernel code > Build rpmsg client sample is M:

.. code-block:: console

    $ make ARCH=arm64 CROSS_COMPILE=aarch64-none-linux-gnu- distclean
    $ make ARCH=arm64 CROSS_COMPILE=aarch64-none-linux-gnu- defconfig ti_arm64_prune.config
    $ make ARCH=arm64 CROSS_COMPILE=aarch64-none-linux-gnu- menuconfig

.. code-block:: text

        Symbol: SAMPLE_RPMSG_CLIENT [=m]
          │ Type  : tristate
          │ Defined at samples/Kconfig:116
          │   Prompt: Build rpmsg client sample -- loadable modules only
          │   Depends on: SAMPLES [=y] && RPMSG [=y] && m && MODULES [=y]
          │   Location:
          │     -> Kernel hacking
          │       -> Sample kernel code (SAMPLES [=y])
          │ (1)     -> Build rpmsg client sample -- loadable modules only (SAMPLE_RPMSG_CLIENT [=m])

#. Make the kernel and modules. Multithreading with –j is optional:

.. code-block:: console

    $ make ARCH=arm64 CROSS_COMPILE=aarch64-none-linux-gnu- -j8

Linux RPMsg can be tested with prebuilt binaries that are packaged in the
SDK wic image filesystem:

#. Copy the Linux RPMsg kernel driver from
   <Linux_SDK>/board-support/linux-x.x.x/samples/rpmsg/rpmsg_client_sample.ko
   into the board's Linux filesystem.

#. Ensure that the remote core symbolic link points to the desired binary file
   in /lib/firmware/ti-ipc/j7xx/. Update the symbolic link if needed. Reference
   section :ref:`booting_remote_cores_from_Linux_console` for more information.

#. Run the example on the board:

.. ifconfig:: CONFIG_part_variant in ('J721S2', 'J722S')

	.. code-block:: console

		root@j721s2-evm:~# modprobe rpmsg_client_sample count=10
		[ 4736.351359] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: new channel: 0x400 -> 0xd!
		[ 4736.359820] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 4736.363653] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: new channel: 0x400 -> 0xd!
		[ 4736.369308] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 4736.377884] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: new channel: 0x400 -> 0xd!
		[ 4736.385918] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 4736.394413] rpmsg_client_sample virtio4.ti.ipc4.ping-pong.-1.13: new channel: 0x400 -> 0xd!
		[ 4736.402221] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 4736.411169] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: new channel: 0x400 -> 0xd!
		[ 4736.418692] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 4736.427660] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: new channel: 0x400 -> 0xd!
		[ 4736.435380] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 4736.444215] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: new channel: 0x400 -> 0xd!
		[ 4736.451872] rpmsg_client_sample virtio4.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 4736.468492] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 4736.477922] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 4736.486199] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 4736.494466] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 4736.502735] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 4736.511006] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 4736.519275] rpmsg_client_sample virtio4.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 4736.527548] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 4736.535812] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 4736.544072] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 4736.552335] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 4736.560605] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 4736.568869] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 4736.577130] rpmsg_client_sample virtio4.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 4736.585401] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 4736.593670] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 4736.601934] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 4736.610196] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 4736.618461] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 4736.626721] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 4736.634985] rpmsg_client_sample virtio4.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 4736.643279] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 4736.651569] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 4736.659839] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 4736.668110] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 4736.676376] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 4736.684643] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 4736.692907] rpmsg_client_sample virtio4.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 4736.701173] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 4736.709439] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 4736.717702] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 4736.725964] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 4736.734228] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 4736.742488] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 4736.750753] rpmsg_client_sample virtio4.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 4736.759015] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 4736.767284] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 4736.775553] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 4736.783820] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 4736.792092] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 4736.800356] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 4736.808615] rpmsg_client_sample virtio4.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 4736.816879] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 4736.825218] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: goodbye!
		[ 4736.831999] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 4736.840267] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 4736.848538] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 4736.856803] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 4736.865068] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 4736.873331] rpmsg_client_sample virtio4.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 4736.881595] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 4736.889855] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 4736.898121] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 4736.906382] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 4736.914723] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: goodbye!
		[ 4736.921503] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 4736.929764] rpmsg_client_sample virtio4.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 4736.938024] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 4736.946289] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 4736.954635] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: goodbye!
		[ 4736.961422] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 4736.969680] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 4736.977942] rpmsg_client_sample virtio4.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 4736.986279] rpmsg_client_sample virtio4.ti.ipc4.ping-pong.-1.13: goodbye!
		[ 4736.993058] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 4737.001392] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: goodbye!
		[ 4737.008180] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 4737.016515] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: goodbye!
		[ 4737.023296] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 4737.031630] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: goodbye!

.. ifconfig:: CONFIG_part_variant in ('J784S4','J742S2')

	.. code-block:: console

		root@j784s4-evm:~# modprobe rpmsg_client_sample count=10
		[ 1205.514152] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: new channel: 0x401 -> 0xd!
		[ 1205.522579] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 1205.525578] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: new channel: 0x401 -> 0xd!
		[ 1205.530882] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 1205.539249] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: new channel: 0x401 -> 0xd!
		[ 1205.547497] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 1205.555858] rpmsg_client_sample virtio4.ti.ipc4.ping-pong.-1.13: new channel: 0x401 -> 0xd!
		[ 1205.564077] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 1205.572437] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: new channel: 0x401 -> 0xd!
		[ 1205.580662] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 1205.589024] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: new channel: 0x401 -> 0xd!
		[ 1205.597244] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 1205.605604] rpmsg_client_sample virtio7.ti.ipc4.ping-pong.-1.13: new channel: 0x401 -> 0xd!
		[ 1205.613828] rpmsg_client_sample virtio4.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 1205.622184] rpmsg_client_sample virtio8.ti.ipc4.ping-pong.-1.13: new channel: 0x401 -> 0xd!
		[ 1205.630419] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 1205.638779] rpmsg_client_sample virtio9.ti.ipc4.ping-pong.-1.13: new channel: 0x401 -> 0xd!
		[ 1205.647009] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 1205.655374] rpmsg_client_sample virtio10.ti.ipc4.ping-pong.-1.13: new channel: 0x401 -> 0xd!
		[ 1205.663600] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 1205.672044] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: new channel: 0x401 -> 0xd!
		[ 1205.680267] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 1205.696972] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 1205.705265] rpmsg_client_sample virtio7.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 1205.715152] rpmsg_client_sample virtio4.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 1205.723420] rpmsg_client_sample virtio8.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 1205.731692] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 1205.739962] rpmsg_client_sample virtio9.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 1205.748232] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 1205.756500] rpmsg_client_sample virtio10.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 1205.764855] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 1205.773131] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 1205.781400] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 1205.789664] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 1205.797930] rpmsg_client_sample virtio7.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 1205.806198] rpmsg_client_sample virtio4.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 1205.814470] rpmsg_client_sample virtio8.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 1205.822737] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 1205.831002] rpmsg_client_sample virtio9.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 1205.839268] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 1205.847532] rpmsg_client_sample virtio10.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 1205.855882] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 1205.864147] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 1205.872411] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 1205.880676] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 1205.888941] rpmsg_client_sample virtio7.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 1205.897207] rpmsg_client_sample virtio4.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 1205.905499] rpmsg_client_sample virtio8.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 1205.913762] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 1205.922028] rpmsg_client_sample virtio9.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 1205.930294] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 1205.938557] rpmsg_client_sample virtio10.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 1205.946910] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 1205.955173] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 1205.963438] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 1205.971707] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 1205.979973] rpmsg_client_sample virtio7.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 1205.988241] rpmsg_client_sample virtio4.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 1205.996506] rpmsg_client_sample virtio8.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 1206.004769] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 1206.013034] rpmsg_client_sample virtio9.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 1206.021299] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 1206.029569] rpmsg_client_sample virtio10.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 1206.037922] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 1206.046186] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 1206.054452] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 1206.062716] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 1206.070980] rpmsg_client_sample virtio7.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 1206.079248] rpmsg_client_sample virtio4.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 1206.087511] rpmsg_client_sample virtio8.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 1206.095774] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 1206.104039] rpmsg_client_sample virtio9.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 1206.112303] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 1206.120567] rpmsg_client_sample virtio10.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 1206.128918] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 1206.137182] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 1206.145450] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 1206.153715] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 1206.161982] rpmsg_client_sample virtio7.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 1206.170246] rpmsg_client_sample virtio4.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 1206.178511] rpmsg_client_sample virtio8.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 1206.186775] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 1206.195117] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: goodbye!
		[ 1206.201898] rpmsg_client_sample virtio9.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 1206.210158] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 1206.218421] rpmsg_client_sample virtio10.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 1206.226771] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 1206.235035] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 1206.243299] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 1206.251563] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 1206.259831] rpmsg_client_sample virtio7.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 1206.268097] rpmsg_client_sample virtio4.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 1206.276361] rpmsg_client_sample virtio8.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 1206.284628] rpmsg_client_sample virtio9.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 1206.292893] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 1206.301157] rpmsg_client_sample virtio10.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 1206.309509] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 1206.317772] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 1206.326036] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 1206.334300] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 1206.342644] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: goodbye!
		[ 1206.349426] rpmsg_client_sample virtio7.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 1206.357688] rpmsg_client_sample virtio4.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 1206.365952] rpmsg_client_sample virtio8.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 1206.374223] rpmsg_client_sample virtio9.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 1206.382488] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 1206.390753] rpmsg_client_sample virtio10.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 1206.399104] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 1206.407448] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: goodbye!
		[ 1206.414229] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 1206.422490] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 1206.430754] rpmsg_client_sample virtio7.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 1206.439019] rpmsg_client_sample virtio4.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 1206.447363] rpmsg_client_sample virtio4.ti.ipc4.ping-pong.-1.13: goodbye!
		[ 1206.454144] rpmsg_client_sample virtio8.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 1206.462405] rpmsg_client_sample virtio9.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 1206.470670] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 1206.479016] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: goodbye!
		[ 1206.485800] rpmsg_client_sample virtio10.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 1206.494148] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 1206.502414] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 1206.510758] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: goodbye!
		[ 1206.517539] rpmsg_client_sample virtio7.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 1206.525879] rpmsg_client_sample virtio7.ti.ipc4.ping-pong.-1.13: goodbye!
		[ 1206.532659] rpmsg_client_sample virtio8.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 1206.541002] rpmsg_client_sample virtio8.ti.ipc4.ping-pong.-1.13: goodbye!
		[ 1206.547784] rpmsg_client_sample virtio9.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 1206.556125] rpmsg_client_sample virtio9.ti.ipc4.ping-pong.-1.13: goodbye!
		[ 1206.562907] rpmsg_client_sample virtio10.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 1206.571333] rpmsg_client_sample virtio10.ti.ipc4.ping-pong.-1.13: goodbye!
		[ 1206.578202] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 1206.586542] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: goodbye!

.. ifconfig:: CONFIG_part_variant in ('J721E')

	.. code-block:: console

		root@j721e-evm:~# modprobe rpmsg_client_sample count=10
		[ 1441.103962] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: new channel: 0x401 -> 0xd!
		[ 1441.112364] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 1441.115950] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: new channel: 0x401 -> 0xd!
		[ 1441.122109] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 1441.130666] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: new channel: 0x401 -> 0xd!
		[ 1441.138198] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 1441.147073] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: new channel: 0x401 -> 0xd!
		[ 1441.154716] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 1441.164037] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: new channel: 0x401 -> 0xd!
		[ 1441.171397] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 1441.180450] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: new channel: 0x401 -> 0xd!
		[ 1441.187887] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 1441.196879] rpmsg_client_sample virtio7.ti.ipc4.ping-pong.-1.13: new channel: 0x401 -> 0xd!
		[ 1441.204558] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 1441.220377] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 1441.229136] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 1441.238574] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 1441.246843] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 1441.255107] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 1441.263372] rpmsg_client_sample virtio7.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 1441.271633] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 1441.279894] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 1441.288151] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 1441.296410] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 1441.304674] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 1441.312933] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 1441.321191] rpmsg_client_sample virtio7.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 1441.329451] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 1441.337709] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 1441.345965] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 1441.354225] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 1441.362493] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 1441.370770] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 1441.379031] rpmsg_client_sample virtio7.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 1441.387289] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 1441.395550] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 1441.403808] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 1441.412067] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 1441.420325] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 1441.428588] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 1441.436846] rpmsg_client_sample virtio7.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 1441.445104] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 1441.453361] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 1441.461619] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 1441.469876] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 1441.478134] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 1441.486401] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 1441.494667] rpmsg_client_sample virtio7.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 1441.502925] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 1441.511184] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 1441.519443] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 1441.527702] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 1441.535959] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 1441.544218] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 1441.552480] rpmsg_client_sample virtio7.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 1441.560740] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 1441.568996] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 1441.577333] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: goodbye!
		[ 1441.584108] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 1441.592365] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 1441.600624] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 1441.608887] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 1441.617152] rpmsg_client_sample virtio7.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 1441.625412] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 1441.633797] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 1441.642070] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 1441.650332] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 1441.658594] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 1441.666931] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: goodbye!
		[ 1441.673715] rpmsg_client_sample virtio7.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 1441.681972] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 1441.690232] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 1441.698496] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 1441.706848] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: goodbye!
		[ 1441.713632] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 1441.721889] rpmsg_client_sample virtio7.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 1441.730147] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 1441.738488] rpmsg_client_sample virtio3.ti.ipc4.ping-pong.-1.13: goodbye!
		[ 1441.745265] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 1441.753598] rpmsg_client_sample virtio5.ti.ipc4.ping-pong.-1.13: goodbye!
		[ 1441.760373] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 1441.768842] rpmsg_client_sample virtio6.ti.ipc4.ping-pong.-1.13: goodbye!
		[ 1441.775638] rpmsg_client_sample virtio7.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 1441.783976] rpmsg_client_sample virtio7.ti.ipc4.ping-pong.-1.13: goodbye!

.. ifconfig:: CONFIG_part_variant in ('J7200')

	.. code-block:: console

		root@j7200-evm:~# modprobe rpmsg_client_sample count=10
		[  700.542444] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: new channel: 0x401 -> 0xd!
		[  700.550889] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: new channel: 0x401 -> 0xd!
		[  700.559291] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[  700.568127] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[  700.578876] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[  700.587202] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[  700.595498] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[  700.603788] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[  700.612057] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[  700.620334] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[  700.628596] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[  700.636867] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[  700.645167] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[  700.653458] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[  700.661770] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[  700.670075] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[  700.678365] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[  700.686656] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[  700.694949] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[  700.703249] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[  700.711540] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[  700.719918] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: goodbye!
		[  700.726733] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[  700.735092] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: goodbye!

.. ifconfig:: CONFIG_part_variant in ('AM62X')

	.. code-block:: console

		root@am62xx-evm:~# modprobe rpmsg_client_sample count=10
		[18124.495957] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: new channel: 0x400 -> 0xd!
		[18124.504422] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[18124.505183] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: new channel: 0x400 -> 0xd!
		[18124.512811] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[18124.529509] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[18124.537888] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[18124.547779] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[18124.556072] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[18124.564376] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[18124.572689] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[18124.580989] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[18124.589273] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[18124.597566] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[18124.605844] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[18124.614134] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[18124.622557] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[18124.630865] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[18124.639227] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: goodbye!
		[18124.646048] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[18124.654540] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[18124.662915] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[18124.671265] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[18124.679645] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 10

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

	.. code-block:: console

		root@am62axx-evm:/lib/firmware# modprobe rpmsg_client_sample count=10
		[ 2081.593551] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: new channel: 0x400 -> 0xd!
		[ 2081.602005] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 2081.602092] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: new channel: 0x400 -> 0xd!
		[ 2081.612625] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 2081.619039] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: new channel: 0x400 -> 0xd!
		[ 2081.628769] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 2081.644037] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 2081.655179] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 1 (src: 0xd)
		[ 2081.663550] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 2081.671991] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 2081.680333] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 2 (src: 0xd)
		[ 2081.688807] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 2081.697141] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 2081.705553] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 3 (src: 0xd)
		[ 2081.713878] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 2081.722297] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 2081.730617] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 4 (src: 0xd)
		[ 2081.739021] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 2081.747344] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 2081.755746] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 5 (src: 0xd)
		[ 2081.764092] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 2081.772514] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 2081.780834] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 6 (src: 0xd)
		[ 2081.789263] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 2081.797633] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 2081.806046] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 7 (src: 0xd)
		[ 2081.814375] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 2081.822851] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 2081.831239] rpmsg_client_sample virtio0.ti.ipc4.ping-pong.-1.13: goodbye!
		[ 2081.838223] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 8 (src: 0xd)
		[ 2081.846559] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 2081.855040] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 9 (src: 0xd)
		[ 2081.863369] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 2081.871858] rpmsg_client_sample virtio1.ti.ipc4.ping-pong.-1.13: goodbye!
		[ 2081.878713] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: incoming msg 10 (src: 0xd)
		[ 2081.887258] rpmsg_client_sample virtio2.ti.ipc4.ping-pong.-1.13: goodbye!

