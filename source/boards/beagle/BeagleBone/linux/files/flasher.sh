#!/bin/sh

echo "************************************************************"
echo "Sitara Example Flashing Script v3.0 - 05/01/2020"
echo "This version is aligned with PROCESSOR-SDK-LINUX-AM335X v6.3"
echo "************************************************************"

STARTTIME=$(date +%s)

##---------Start of variables---------------------##

## Set Server IP here
SERVER_IP=$1

## Set MAC address here, passed from fetcher.sh and U-Boot
MAC_ADDR=$2

## Names of the images to grab from TFTP server
BOOT_PARTITION="boot_partition.tar.gz"

## Rename rootfs as needed depending on use of tar or img
ROOTFS_PARTITION="arago-base-tisdk-image-am335x-evm.tar.xz"

## Declare eMMC device name here
DRIVE="/dev/mmcblk1"

##----------End of variables-----------------------##

## TFTP files from host.  Edit the files and host IP address for your application.
## We are grabbing two files, one an archive with files to populate a FAT partion,
## which we will create.  Another for a filesystem image. This can either be a archive
## to be uncompressed to the partition, or an image to 'dd' onto an unmounted partition.
## Using a compressed tarball can be easier to implement, however, with a large file system
## with a lot of small files, we recommend a 'dd' image of the partition to speed up writes.
## The -b option in the TFTP command sets the packet size from the default 512 bytes to 
## 1468 bytes, the largest size that avoids IP packet fragmentation. Faster transfers 
## might be achieved with larger packet sizes, so experimentation and optimization is
## encouraged.
echo "Getting files from server: ${SERVER_IP}"
tftp -b 1468 -g -r ${BOOT_PARTITION} ${SERVER_IP} &
boot_pid=$!
tftp -b 1468 -g -r ${ROOTFS_PARTITION} ${SERVER_IP} &
rootfs_pid=$!

## Kill any partition info that might be there
dd if=/dev/zero of=$DRIVE bs=4k count=1
sync
sync

## Check to see if the eMMC partitions have automatically loaded from the old MBR.
## This might have occured during the boot process if the kernel detected a filesystem
## before we killed the MBR. We will need to unmount and kill them by writing 4k zeros to the
## partitions that were found.

check_mounted(){
  is_mounted=$(grep ${DRIVE}p /proc/mounts | awk '{print $2}')

  if grep -q ${DRIVE}p /proc/mounts; then
      echo "Found mounted partition(s) on " ${DRIVE}": " $is_mounted
      umount $is_mounted
      counter=1
      for i in $is_mounted; do \
          echo "4k erase on ${DRIVE}p${counter}"; 
          dd if=/dev/zero of=${DRIVE}p${counter} bs=4k count=1;
          counter=$((counter+1));
      done
  else
      echo "No partition found. Continuing."
  fi
}

check_mounted;

## Partitioning the eMMC using information gathered.
## Here is where you can add/remove partitions.
## We are building 2 partitions:
##  1. FAT32
##  2. Linux
##
## You will need to change the below to suit your needs.  Adding is similar,
## but you will need to be aware of partition sizes and boundaries.
## Also see <...>/ti-processor-sdk-linux-am335x-evm-06.03.00.106/bin/create-sdcard.sh
echo "Partitioning the eMMC..."
dd if=/dev/zero of=$DRIVE bs=1024 count=1024

SIZE=`fdisk -l $DRIVE | grep Disk | awk '{print $5}'`

echo DISK SIZE - $SIZE bytes

parted -s $DRIVE mklabel msdos
parted -s $DRIVE unit cyl mkpart primary fat32 -- 0 9
parted -s $DRIVE set 1 boot on
parted -s $DRIVE unit cyl mkpart primary ext2 -- 9 -2

## This sleep is necessary as there is a service which attempts
## to automount any filesystems that it finds as soon as sfdisk
## finishes partitioning.  We sleep to let it run.  May need to
## be lengthened if you have more partitions.
sleep 2

## Check here if there has been a partition that automounted.
## This will eliminate the old partition that gets
## automatically found after the sfdisk command.  It ONLY
## gets found if there was a previous file system on the same
## partition boundary.  Happens when running this script more than once.
## To fix, we just unmount and write some zeros to it.
check_mounted;

## Clean up the dos (FAT) partition as recommended by SFDISK
dd if=/dev/zero of=${DRIVE}p1 bs=512 count=1

## Make sure posted writes are cleaned up
sync
sync

## Format the eMMC into 2 partitions
echo "Formatting the eMMC into 2 partitions..."

## Format the boot partition to FAT32
mkfs.vfat -F 32 -n "boot" ${DRIVE}p1

## Format the rootfs to ext3 (or ext4, etc.) if using a tar file.
## We DO NOT need to format this partition if we are 'dd'ing an image
## Comment out this line if using 'dd' of an image.
mkfs.ext3 -L "rootfs" ${DRIVE}p2

## Make sure posted writes are cleaned up
sync
sync
echo "Formatting done."

## Make temp directories for mountpoints
mkdir tmp_boot

## Comment this line out if using 'dd' of an image. It is not needed.
mkdir tmp_rootfs

## Mount partitions for tarball extraction. NOT for 'dd'.
mount -t vfat ${DRIVE}p1 tmp_boot

## If 'dd'ing the rootfs, there is no need to mount it. Comment out the below.
mount -t ext3 ${DRIVE}p2 tmp_rootfs

echo "Waiting for ${BOOT_PARTITION} to finish tftp..."
wait $boot_pid
echo "Copying Files..."
time tar -xf ${BOOT_PARTITION} -C tmp_boot
sync
sync
umount ${DRIVE}p1
echo "Boot partition done."

echo "Waiting for ${ROOTFS_PARTITION} to finish tftp..."
wait $rootfs_pid
echo "Copying Files..."

## If using a tar archive, untar it with the below.
## If using 'dd' of an img, comment these lines out and use the below.
time tar -xf ${ROOTFS_PARTITION} -C tmp_rootfs
sync
sync
umount ${DRIVE}p2

## If using 'dd' of an img, uncomment these lines.
## If using a tar archive, comment out these lines and use the above.
## time gunzip -c ${ROOTFS_PARTITION} | dd of=${DRIVE}p2 bs=4k
## sync
## sync

echo "Rootfs partition done."

## The block below is only necessary if using 'dd'. 
## Force check the filesystem for consistency and fix errors if any.
## Resize partition to the length specified by the MBR.
## /sbin/e2fsck -fy ${DRIVE}p2
## /sbin/resize2fs ${DRIVE}p2

ENDTIME=$(date +%s)
echo "It took $(($ENDTIME - $STARTTIME)) seconds to complete this task..."

## The files that were transferred will NOT be cleaned up since this is a
## RAM Disk. They will automatically disappear with a reboot.

## A reboot could be initiated here, but it might be nice to have a "completion"
## signal so the user knows to do whatever is necessary for the next stage of
## programming/testing. For example, it may be necessary to do something to set the board
## to boot from the eMMC (or whatever was just programmed) and test the image that was
## just programmed. Or, turn on some LEDs on the board as a visual indicator of completion.

## If using Uniflash, the server is configured to mark completion of a flash
## process when receiving a TFTP get request like below.
tftp -g -r TargetProgrammingComplete:${MAC_ADDR} ${SERVER_IP} > /dev/null 2>&1

## Reboot

echo ""
echo "********************************************"
echo "Sitara Example Flash Script is complete."
echo "********************************************"
echo ""

