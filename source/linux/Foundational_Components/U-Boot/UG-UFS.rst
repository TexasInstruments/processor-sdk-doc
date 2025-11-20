UFS
---

Universal Flash Subsystem (UFS) devices show up as scsi devices similar to SATA
in the :ref:`previous section <UG-SATA>`. One additional command to initialize
all ufs devices is:

.. code-block:: console

   => ufs init
   Device at ufs@4e84000 up at:[RX, TX]: gear=[3, 3], lane[2, 2], pwr[FAST MODE, FAST MODE], rate = 2

Then we can go ahead with 'scsi scan' to see the attached devices:

.. code-block:: console

   => scsi scan
   scanning bus for devices...
   Device 0: (0:0) Vendor: TOSHIBA Prod.: THGAF8G8T23BAILB Rev: 0300
            Type: Hard Disk
            Capacity: 31.9 MB = 0.0 GB (8191 x 4096)
   Device 0: (0:1) Vendor: TOSHIBA Prod.: THGAF8G8T23BAILB Rev: 0300
            Type: Hard Disk
            Capacity: 30499.9 MB = 29.7 GB (7807999 x 4096)

All the remaining scsi commands detailed in the :ref:`previous section <UG-SATA>` are
also applicable.

For more information about UFS see :ref:`Kernel UFS Guide <KERNEL-SATA>`.
