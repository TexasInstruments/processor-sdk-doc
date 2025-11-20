.. _UG-SATA:

SATA
------------------------------------

.. note::
    SATA is not supported on J721E platform.

SATA and eSATA devices show up as SCSI devices in U-boot.

Viewing SATA Devices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To view all SCSI devices that U-boot sees the command "scsi info" can be
used.

Output of this command when ran on AM57x General Purpose EVM can be seen
below.

::

    scsi part
    Device 0: (0:0) Vendor: ATA Prod.: PLEXTOR PX-64M6M Rev: 1.08
                Type: Hard Disk
                Capacity: 61057.3 MB = 59.6 GB (125045424 x 512)

Device 0 represents the instance of the scsi device. Therefore, in later
commands when a "<dev>" parameter is seen replace it with the
appropriate device number.

Viewing Partitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To view all the partitions found on the SATA device the command "scsi
part <dev>" can be used.

Output of this command when ran on AM57x General Purpose EVM can be seen
below.

::

    Partition Map for SCSI device 0  --   Partition Type: DOS

    Part    Start Sector    Num Sectors     UUID            Type
      1     2048            161793          6cc50771-01     0c Boot
      2     165888          33552385        6cc50771-02     83
      3     33720320        91325104        6cc50771-03     83

All entries above represent different partitions that exist on the
particular scsi device. To reference a particular partition a user will
reference it the part number shown above. In commands shown below <part>
should be replaced with the appropriate partition number seen from this
table.

Identifying Partition Filesystem Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As shown above the "scsi part <dev>" command can be used to view all the
partitions available on the particular scsi device. However, the proper
commands to use depend on the filesystem type each partition have been
formatted to.

In the "scsi part <dev>" command the partition type can be found under
the type column. The values under the Type column are referred to as
partition id. Depending on the partition id will dedicate which commands
to use to read and write partition. Partition id of "0c" refers to a
FAT32 partition. Partition id of "83" refers to a native Linux file
system which ext2,ext3 and ext4 fall under. Go
`here <https://en.wikipedia.org/wiki/Partition_type#List_of_partition_IDs>`__
to find a complete list of partition ids.

|

Viewing, Reading and Writing to Partition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Depending on the filesystem type of the partition will depend on the
exact commands to use to read and write to the partition. The two most
common partitions are FAT32, EXT2 and EXT4. Luckily the commands to
view, read and write to the partition all look the same. Viewing
partition uses <prefix>ls, reading files is <prefix>load and writing
files is <prefix>write. Replace <prefix> with fat, ext2 and ext4
depending on the filesystem type.

View Partition Contents
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To view the contents of a FAT32 partition the user would use "fatls scsi
<dev>:<partition>"

Below command list the contents of SCSI device 0 partition 1 on AM57x
General Purpose EVM:

::

    => fatls scsi 0:1
       110578   test
    1 file(s), 0 dir(s)

.. rubric:: Write File to Partition
   :name: write-file-to-partition

To write a file on a EXT4 partition the user must have first read the
file to be written into memory and then also know the size of the file.
Luckily U-boot automatically sets the environment variable "filesize" to
the filesize of a file that was loaded into memory via U-boot load
command.

To write to a ext4 partition the user would execute the below command:
ext4write scsi <dev>:<partition> <ddr address> <absolute filename path>
<filesize>

In the above command <ddr address> refers to the address in memory the
file has already been loaded into. Absolute filename path must start
with / to indicate the root. Filesize is the amount in bytes to be
written.

Below is an example of writing the file "tester" previously loaded into
memory onto a EXT4 partition

::

    => ext4write scsi 0:3 ${loadaddr} /tester ${filesize}
    File System is consistent
    update journal finished
    110578 bytes written in 2650 ms (40 KiB/s)
