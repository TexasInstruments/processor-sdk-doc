#!/bin/bash

# Author: Dhiren Wijesinghe 
# This script helps the automation of the partitioning and formatting of the
# eMMC in a Beaglebone Black. 

# Copyright (C) 2018 Texas Instruments Incorporated - http://www.ti.com/
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the
# distribution.
#
# * Neither the name of Texas Instruments Incorporated nor the names of
# its contributors may be used to endorse or promote products derived
# from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

########################################################################

echo "Starting eMMC Flashing Script..."

# Format eMMC
echo " " 
echo "Partitioning eMMC"

read -p "Do you want to continue [y/n]? " -n 1 -r
echo " "  
if [[ $REPLY =~ ^[Nn]$ ]]
then
   echo " " 
   echo "Exiting script" 
   exit 1
fi

echo " "
fdisk /dev/mmcblk1 << EOM
o
p
n
p
1
2048
+16M
y
t
e
a
n
p
2


y
p
w
EOM

# Format first partition
echo "Formatting first partition"
umount /dev/mmcblk1p1; mkfs.vfat -F 16 /dev/mmcblk1p1

#Format second partition
echo " " 
echo "Formatting second partition"
echo " " 
umount /dev/mmcblk1p2; mkfs.ext4 /dev/mmcblk1p2


echo "Copying boot partition"
mkdir /home/root/boot                                   	# Make boot directory
mount /dev/mmcblk1p1 /home/root/boot                    	# Mount first partition to boot
cp /run/media/mmcblk0p1/MLO /home/root/boot             	# Copy MLO to boot
echo " "
echo "MLO copied"
echo " " 
cp /run/media/mmcblk0p1/u-boot.img /home/root/boot      	# Copy u-boot image to boot
echo "u-boot.img" copied"
echo " " 
umount /home/root/boot                                  	# Unmount boot partition

echo "Copying rootfs partition"
echo "Will take minutes..."
echo " " 
mkdir /home/root/root                                   	# Make root directory
mount /dev/mmcblk1p2 /home/root/root                    	# Mount second partition to root
tar -xf tisdk-rootfs-image-am335x-evm.tar.xz -C /home/root/root	# Create filesystem from existing tarball

umount /home/root/root/                                 	# Unmount root

echo " "
echo "eMMC Flash complete! Please reboot EVM from eMMC"
echo " "
