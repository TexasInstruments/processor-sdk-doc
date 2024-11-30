Moving Files to the Target System
=================================

.. rubric:: Introduction
   :name: introduction-linux-moving-files-to-fs

This guide discusses how applications or other files can be moved to the
target file system of the EVM.

.. rubric:: File System on SD card
   :name: file-systemon-sd-card

The SD card wic image which comes with the TI SDK has a Linux ext4 partition that is used as the target file system.
This partition is readable from a Linux host. In Ubuntu |__LINUX_UBUNTU_VERSION_LONG__| this partition will be mounted on
:file`/media/$USER/rootfs` when the card is used with an SD card reader inserted into a USB port on the Ubuntu host. 

When the SD card is mounted with a card reader in the Linux host it is possible to perform :command:`cp` commands from the host into sub-directories
under :file:`/media/$USER/rootfs` or just use a browser window to drag and drop the files from the host to the SD card.

Switching the SD card back and forth from the EVM to the SD card reader
is time consuming during development.  Using a NFS during development is
the preferred method and makes moving files between the host and target
trivial.

.. rubric:: File System on Network File System (NFS)
   :name: file-system-on-network-file-system-nfs

When the target file system is served from the Linux development host
machine it is trivial to move files between the host and target.  The
NFS directory is set up on the host machine by the SDK installer.  The
default location in the SDK environment is :file:`${PSDK_PATH}/targetNFS`
This could vary depending on the version of the SDK and how it was installed.
An :command:`ls -l` of this directory in the host system will show what will be the root
directory of the target when it boots up.

.. code-block:: console

    user@U1004GT:~/ti-sdk-AM3715-evm-4.0.0.0/filesystem$ pwd
    /home/user/ti-sdk-AM3715-evm-4.0.0.0/filesystem
    user@U1004GT:~/ti-sdk-AM3715-evm-4.0.0.0/filesystem$ ls -l
    total 68
    drwxr-xr-x  2 root root 4096 Mar  9  2018 bin
    drwxr-xr-x  4 root root 4096 Mar  9  2018 boot
    drwxr-xr-x  2 root root 4096 Mar  9  2018 dev
    drwxr-xr-x 55 root root 4096 Mar  9  2018 etc
    drwxr-xr-x  4 root root 4096 Mar  9  2018 home
    drwxr-xr-x 10 root root 4096 Mar  9  2018 lib
    lrwxrwxrwx  1 root root   19 Mar  9  2018 linuxrc -> /bin/busybox.nosuid
    drwxr-xr-x  2 root root 4096 Mar  9  2018 media
    drwxr-xr-x  2 root root 4096 Mar  9  2018 mnt
    drwxr-xr-x 14 root root 4096 Mar  9  2018 opt
    dr-xr-xr-x  2 root root 4096 Mar  9  2018 proc
    drwxr-xr-x  2 root root 4096 Mar  9  2018 run
    drwxr-xr-x  2 root root 4096 Mar  9  2018 sbin
    drwxr-xr-x  2 root root 4096 Mar  9  2018 srv
    dr-xr-xr-x  2 root root 4096 Mar  9  2018 sys
    drwxrwxrwt  2 root root 4096 Mar  9  2018 tmp
    drwxr-xr-x 12 root root 4096 Mar  9  2018 usr
    drwxr-xr-x  9 root root 4096 Mar  9  2018 var

So from the perspective of the host, the target filesystem is just a
sub-directory of the host.  If the file is in :file:`./targetNFS` on the host,
then the same file will show up in the root directory of the target
after the target boots into the NFS.  And if the file is in a
subdirectory of :file:`./targetNFS` (example :file:`./targetNFS/{sub-dir}/`) then it will
show up in the /sub-dir directory of the target after the target boots
into the NFS.

The top level makefile of the TI SDK supports an install target that
will copy applications into the NFS of the SDK. See the README file at
the top level of the SDK for information about the install target.
