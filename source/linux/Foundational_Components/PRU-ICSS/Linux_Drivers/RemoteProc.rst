.. _pru_remoteproc:

RemoteProc
----------

.. rubric:: Introduction
   :name: introduction-pru-icss-remoteproc-rpmsg

.. Image:: /images/Overview.PNG

The host processor on TI's Sitara family of devices is an ARM Cortex-A
processor. Typically the ARM core is running Linux based on the
:ref:`Processor SDK Linux <linux-index>`.
TI has developed custom pruss and pru_rproc (PRU Subsystem Remote
Processor) drivers which will plug into this kernel. This provides an
interface for the kernel to load firmware into the PRU core(s) and
provides basic control such as start and halt.

.. rubric:: What do we need Linux to do?
   :name: what-do-we-need-linux-to-do

The following is a list of services that Linux needs to provide in order
to enable the PRU cores:

-  Load firmware into the PRU cores
-  Control PRU execution (start, stop, etc.)
-  Manage resources (memory, interrupt mappings, etc.)

All of these services are provided through a combination of the pruss,
and pru_rproc Linux drivers that TI provides in the
:ref:`Processor SDK Linux <linux-index>`.

.. rubric:: Remoteproc
   :name: remoteproc

.. rubric:: Overview
   :name: overview-remoteproc

Remoteproc is a framework that allows the ARM host processor(s) to load
firmware into PRU cores, start the PRU cores, stop the PRU cores, and
configure resources that the PRUs might need during their execution
(such as configuring the PRUSS INTC module and providing shared buffers
in DDR memory for message passing). The next section will discuss the
process that happens when the remoteproc module loads the PRU cores with
a firmware. Most of this happens transparently to the user when the
pruss and pru_rproc modules are inserted but an understanding of the
concepts below should help users to better understand how to debug
problems with remoteproc should they arise.

.. rubric:: Load Procedure
   :name: load-procedure

This section will walk through each step that the drivers takes as they
load firmwares into the PRU cores and then run them.

.. rubric:: Step 0
   :name: step-0

.. Image:: /images/Step0_2_0_2_11.PNG

The four blocks in the image to right represent: The ARM core running
Linux, the Linux filesystem where the PRU firmware binaries are
initially stored, the PRU subsystem, and DDR memory. This image shows
the initial state of the system before the pruss_remoteproc module is
inserted.

-  Remoteproc driver is included as a kernel driver. This is a core
   remoteproc driver that provides the load/run/halt/etc API to other
   more specific remoteproc drivers.
-  A sysfs interface is also exposed to User Space to start/stop the PRU
   cores as well as specify the firmware file to load.

   -  The sysfs interface is found at
      **/sys/class/remoteproc/remoteprocN/** (e.g. remoteproc1 is PRU0
      and remoteproc2 is PRU1 on the AM335x device (remoteproc0 is the
      M3 core used for power management functions)).

-  PRU firmware binaries exist in the filesystem in the
   **/lib/firmware/** directory.

|

--------------

.. rubric:: Step 1
   :name: step-1

.. Image:: /images/Step1_2_0_2_11.PNG

| In this step, the sysfs interface (mentioned above in step 0) is used
  to specify the name of the firmware to be loaded as well as to signal
  that the user wants to load and start the PRU cores
| ``echo 'am335x-pru0-fw' > /sys/class/remoteproc/remoteproc1/firmware``
| ``echo 'am335x-pru1-fw' > /sys/class/remoteproc/remoteproc2/firmware``
| ``echo 'start' > /sys/class/remoteproc/remoteproc1/state``
| ``echo 'start' > /sys/class/remoteproc/remoteproc2/state``

|

--------------

.. rubric:: Step 2
   :name: step-2

.. Image:: /images/Step2_2_0_2_11.PNG

The pru_rproc module verifies two things before it proceeds with the
firmware loading process.

-  The pru_rproc modules checks for the existence of PRU firmware
   binaries in the filesystem (as specified by the firmware entry in the
   sysfs in step 1 above)

   -  These binaries must be located in the /lib/firmware/ directory
   -  am335x-pru0-fw and am335x-pru1-fw are the default names used for
      the AM335x device but any name can be used as long as the firmware
      exists in /lib/firmware/

-  The pru_rproc module also parses the firmware binaries looking for a
   section named **.resource_table**

   -  This **.resource_table** section of the firmware specifies the
      system resources that the PRUs will need during their program
      execution

|

--------------

|

.. rubric:: Step 3
   :name: step-3

.. Image:: /images/Step3_2_0_2_11.PNG

-  The pru_rproc module configures all of the resources that are being
   requested by the firmwares
-  In this case, that includes creating vrings in DDR memory for
   communication as well as setting up the interrupt mapping in the PRU
   subsystem INTC module

|

--------------

.. rubric:: Step 4
   :name: step-4

.. Image:: /images/Step4_2_0_2_11.PNG

| The pru_rproc module then loads the binary into the instruction RAM
  of the PRUs and also copies the resource table into the PRUs data RAM
  space
| **Note: Configuration details can be shared from the ARM to the PRUs
  through the resource table that gets copied into the data RAM of each
  PRU**

|

--------------

|

.. rubric:: Step 5
   :name: step-5

.. Image:: /images/Step5_2_0_2_11.PNG

Now that everything is configured and the application code is in place,
the pru_rproc module instructs the PRU cores to begin execution.

| **Notice that the PRU state was previously set to 'Halted' but now it
  is 'Run'**

