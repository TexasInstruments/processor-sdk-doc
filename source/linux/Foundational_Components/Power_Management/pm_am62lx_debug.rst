.. _pm_debug:

#################
Debug Information
#################

***************
Low Power Modes
***************

Overview
========

Implementing Low Power Modes (LPM) requires synchronization between many
software parts. Debugging an LPM issue requires finding out which
part (Linux, TF-A or TIFS) might be at fault.

The comprehensive way of debugging LPM starts by looking at all
the commands that the TIFS and TF-A firmware executed.

The TI Foundational Security (TIFS) and TF-A firmware trace the low power mode sequence and dump a series of
representative hex values. These hex values are not in human-readable form, so the System Firmware (SYSFW) Trace
Parser Script :ref:`sysfw-trace-parser` converts the hex values into a readable format.

The Wakeup (WKUP) UART port (``/dev/ttyUSB2``) displays these hex values.

Prerequisites
=============

Before using the parser, enable the SYSFW trace to include
Low Power Mode sequencing with the following steps:

1. Enable low power logs in the board configuration file
2. Remove isolation from I/Os and enable appropriate log level in TF-A

Step 1: Enable Low Power Logs in Board Configuration
====================================================

Apply the following patch in the U-Boot source code to enable trace logs.

File location: :file:`<SDK Install Directory>/board-support/ti-u-boot-<version>/board/ti/am62lx/board-cfg.yaml`

Patch to apply:

.. code-block:: diff

   diff --git a/board/ti/am62lx/board-cfg.yaml b/board/ti/am62lx/board-cfg.yaml
   index a0297c284a6..a535a73734d 100644
   --- a/board/ti/am62lx/board-cfg.yaml
   +++ b/board/ti/am62lx/board-cfg.yaml
   @@ -28,5 +28,5 @@ board-cfg:
      subhdr:
         magic: 0x020C
         size: 8
   -    trace_dst_enables: 0x00
   -    trace_src_enables: 0x00
   +    trace_dst_enables: 0x0D
   +    trace_src_enables: 0x7F

After applying the patch, re-build U-Boot following the instructions in :ref:`u-boot-build-guide-build-k3`.

Make sure to copy the target images to your boot media.

Step 2: Remove I/O Isolation and Enable Logging in TF-A
=======================================================

Apply the following patch in the TF-A (Arm Trusted Firmware) source code to disable I/O isolation.

File location: :file:`<SDK Install Directory>/board-support/arm-trusted-firmware-<version>/plat/ti/k3/common/am62l_psci.c`

Patch to apply:

.. code-block:: diff

   diff --git a/plat/ti/k3/common/am62l_psci.c b/plat/ti/k3/common/am62l_psci.c
   index 3df4986e5..bd20c8413 100644
   --- a/plat/ti/k3/common/am62l_psci.c
   +++ b/plat/ti/k3/common/am62l_psci.c
   @@ -329,7 +329,7 @@ static void am62l_pwr_domain_suspend(const psci_power_state_t *target_state)
           if ((mode == 0) || (mode == 6)) {
                   INFO("Started Suspend Sequence in ATF\n");
                   /* Isolate the I/Os to allow I/O Daisy chain wakeup */
   -               k3_lpm_set_io_isolation(true);
   +               // k3_lpm_set_io_isolation(true);
                   k3_lpm_config_magic_words(mode);
                   ti_sci_prepare_sleep(mode, context_save_addr, 0);
                   INFO("sent prepare message\n");

.. important::

   Modifying the I/O isolation code impacts the functionality of any wake-up source that uses
   I/O Daisy Chain, such as Main Domain UART. See the `Technical Reference Manual (TRM) <https://www.ti.com/lit/ug/sprujb4a/sprujb4a.pdf>`__
   section 6.2.3.11 I/O Power Management and Daisy Chaining for more information.

After applying the patch, re-compile TF-A with ``LOG_LEVEL=20`` (LOG_LEVEL_INFO). Follow the
instructions in :ref:`foundational-components-atf` for building TF-A.

Make sure to copy the new :file:`bl31.bin` image to your boot media.

Generating logs and running the parser script
=============================================

Boot the device with the new changes made. To isolate the low power mode related logs, start
running the parser script right before entering low power mode.

Step 1: Prepare the EVM terminal
--------------------------------

On the Evaluation Module (EVM) terminal, get it ready to enter low power mode:

.. code-block:: console

   root@am62lxx-evm:~# echo mem > /sys/power/state

Step 2: Set up the parser script on host
----------------------------------------

On the Host terminal, setup the script:

.. code-block:: console

   HOST:~$ cd <SDK Install Directory>/bin
   HOST:~$ python3 sysfw_trace_parser.py -d /dev/ttyUSB2 -o <output file> -Tv <version>

For example, using version ``0x03007``:

.. code-block:: console

   HOST:~$ python3 sysfw_trace_parser.py -d /dev/ttyUSB2 -o am62lx_lpm_trace.txt -Tv 0x03007

Step 3: Run and capture logs
----------------------------

Once both terminals are ready:

1. Run the Parser Script on the host terminal
2. Run the low power command on the EVM terminal
3. Send a keyboard interrupt (``Ctrl + C``) to the parser script once the device wakes up

The script saves the human-readable logs in the designated output file.

Alternative: Direct terminal output
-----------------------------------

The parser script can also write the log output directly to the terminal instead of
a file:

.. code-block:: console

   HOST:~$ python3 sysfw_trace_parser.py -d /dev/ttyUSB2 -O -Tv 0x03007

Troubleshooting: Parser errors
==============================

Sometimes the parser results in an error:

.. code-block:: text

   invalid literal for int() with base 16: '0x6C001700H0x6C001820'

**Workaround:** Copy the logs directly from ``/dev/ttyUSB2`` and save them as an input file.
The hex values not creating a new line cause this error.

When using the workaround with a saved log file, run the parser script as follows:

.. code-block:: console

   HOST:~$ python3 sysfw_trace_parser.py -l <input hex log file> -o <output file> -Tv 0x03007

For direct terminal output:

.. code-block:: console

   HOST:~$ python3 sysfw_trace_parser.py -l <input hex log file> -O -Tv 0x03007

Interpreting the logs
=====================

The generated logs contain detailed information about the low power mode sequence execution.

.. note::

   For detailed information about interpreting the logs, see the `low power mode sequence documentation <https://software-dl.ti.com/tisci/esd/latest/4_trace/trace.html#low-power-mode-sequence-id>`__.

The logs show:

- Security management action IDs and their status
- Sequence of operations during suspend and resume
- Any errors or warnings during the low power mode change

Additional information: Decoding driver failures during suspend
===============================================================

Sometimes the suspend does not go through. In that case, delay the console suspend to get the logs at
low power mode suspend time by using the following command:

.. code-block:: console

   root@am62lxx-evm:~# echo N | sudo tee /sys/module/printk/parameters/console_suspend
   root@am62lxx-evm:~# echo mem > /sys/power/state

Use this to debug whether any drivers in Linux failed to enter suspend.
