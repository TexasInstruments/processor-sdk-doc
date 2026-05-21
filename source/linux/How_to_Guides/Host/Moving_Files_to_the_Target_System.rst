Moving Files to the Target System
=================================

.. rubric:: Introduction
   :name: introduction-linux-moving-files-to-fs

This guide discusses how applications or other files can be moved to the
target file system of the EVM.

.. rubric:: File System on SD card
   :name: file-systemon-sd-card

The SD card wic image which comes with the TI SDK has a Linux ext4 partition that is used as the target file system.
This partition is readable from a Linux host. In Ubuntu |__LINUX_UBUNTU_VERSION_LONG__| this partition will be mounted on
:file`/media/$USER/rootfs` when the card is used with an SD card reader inserted into a USB port on the Ubuntu host.

When the SD card is mounted with a card reader in the Linux host it is possible to perform :command:`cp` commands from the host into sub-directories
under :file:`/media/$USER/rootfs` or just use a browser window to drag and drop the files from the host to the SD card.

Switching the SD card back and forth from the EVM to the SD card reader
is time consuming during development.  Using a NFS during development is
the preferred method and makes moving files between the host and target
trivial.
