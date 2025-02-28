.. _selinux_guide:

####################
SELinux - User Guide
####################

Introduction
************

Security-Enhanced Linux (`SELinux <https://github.com/SELinuxProject>`_) is a project to implement mandatory access control under Linux. It is a set of kernel modifications and user-space tools that provide a mechanism for supporting access control security policies. This project was initially developed by the National Security Agency (NSA), as a reference implementation.

SELinux can run in one of three modes: *enforcing*, *permissive*, or *disabled*.

- Enforcing mode is the recommended mode of operation where SELinux operates normally, enforcing the loaded security policy on the entire system.
- In permissive mode, the system acts as if SELinux is enforcing the loaded security policy, including labeling objects and emitting access denial entries in the logs, but it does not actually deny any operations. While not recommended for production systems, permissive mode can be helpful for SELinux policy development and debugging.
- Disabled mode is strongly discouraged; not only does the system avoid enforcing the SELinux policy, it also avoids labeling any persistent objects such as files, making it difficult to enable SELinux in the future.

.. note::

   This guide assumes that the user understands how to build the Linux Kernel and, Yocto or Debian distribution.

Filesystem Setup
****************

Yocto
=====

The following steps describe how to build SELinux user-space tools and configuration on Yocto. Please use :ref:`Processor SDK - Building the SDK with Yocto <building-the-sdk-with-yocto>` as reference.

1. On a fresh build, update the config file to use :file:`configs/arago-scarthgap-selinux-config.txt`. This config includes the opensource `meta-selinux` layer into the build and also adds additional features for the filesystem such as the kernel configs listed below:

   .. code-block:: kconfig

      CONFIG_AUDIT=y
      CONFIG_NETWORK_SECMARK=y
      CONFIG_EXT2_FS_SECURITY=y
      CONFIG_EXT3_FS_SECURITY=y
      CONFIG_EXT4_FS_SECURITY=y
      CONFIG_JFS_SECURITY=y
      CONFIG_REISERFS_FS_SECURITY=y
      CONFIG_JFFS2_FS_SECURITY=y
      CONFIG_SECURITY=y
      CONFIG_SECURITYFS=y
      CONFIG_SECURITY_NETWORK=y
      CONFIG_SECURITY_SELINUX=y
      CONFIG_SECURITY_SELINUX_BOOTPARAM=y
      CONFIG_SECURITY_SELINUX_DEVELOP=y
      CONFIG_SECURITY_SELINUX_AVC_STATS=y
      CONFIG_AUDIT_GENERIC=y

   .. note::

      The default policy is targeted. If you want to update it, add the variable ``PREFERRED_PROVIDER_virtual/refpolicy = "refpolicy-<your_choice>"`` to the :file:`local.conf` where ``<your_choice>`` is targeted, mls, mcs.

2. Build the :file:`tisdk-default-image`. Note that other recipes do not package selinux features for now.

   .. code-block:: console

      $ MACHINE=<machine> bitbake -k tisdk-default-image

3. Your newly built wic image will be generated in ``deploy-ti`` directory. Use :ref:`Linux SD Card Creation Guide <processor-sdk-linux-create-sd-card>` to flash this generated image onto your SD card. By default, SELinux functionality is in the disabled state.

Debian
======

The following steps describe how to install and configure SELinux together with the default policy which enables SELinux for the most important parts of your Debian filesystem. This guide does not describe how to build the filesystem using Debian.

1. The default Debian image provided by TI (:file:`tisdk-debian-trixie-<machine>-<version>.wic.xz`) packages necessary kernel configs to enable SELinux. If you are not using the standard linux kernel provided by debian with an ext2/3/4/xfs/btrfs filesystem, you have to make sure that you are using a SELinux capable kernel and filesystem. For ext2/3/4 there is nothing special to be aware of, but for other filesystems there are still some quirks.

2. On the target machine, get the default policy and the basic set of SELinux utilities by running

   .. code-block:: console

      $ sudo apt-get install selinux-basics selinux-policy-default auditd

Permissive mode Setup
*********************

It is intended to go into Permissive mode, log the accesses, create the access policy and only then jump to Enforcing mode. Skipping this step would lead to a login failure due to lack of access.

1. Boot the target (in disabled state), Run

   .. code-block:: console

      root@<machine>:~# fixfiles -F onboot

   or

   .. code-block:: console

      root@<machine>:~# touch /.autorelabel

   to ensure that files are relabeled upon next reboot.

   .. warning::

      When systems run SELinux in permissive mode, users and processes might label various file-system objects incorrectly. File-system objects created while SELinux is disabled are not labeled at all. This behavior causes problems when changing to enforcing mode because SELinux relies on correct labels of file-system objects.

   To prevent incorrectly labeled and unlabeled files from causing problems, SELinux automatically relabels file systems when changing from the disabled state to permissive or enforcing mode.

2. Open :file:`/etc/selinux/config` and edit it to ``SELINUX=permissive`` and the policy type you are using.

3. Restart the system. If using U-Boot, add ``security=selinux`` to the boot parameters by stopping at the U-Boot prompt and adding,

   .. code-block:: console

      => setenv optargs "security=selinux"

4. If the previous steps were executed correctly, it will take a while to label the filesystems on boot and then it will automatically reboot a second time when that is complete.

   .. warning::

      If you are using the optargs step, every boot will require you to stop at U-Boot prompt, set optargs and proceed. Not doing so will force SELinux to go back to *disabled* state and you will have to restart the setup.

5. You should now have a working SELinux system, which is in permissive mode. This means that the selinux policy is not enforced, but denials are logged. You can see all would-be denials since the last reboot with a small explanation for each with ``audit2why -al``.

6. Verify your status by running ``sestatus`` or ``getenforce``.

   .. code-block:: console

      root@<machine>:~# sestatus
      SELinux status:                 enabled
      SELinuxfs mount:                /sys/fs/selinux
      SELinux root directory:         /etc/selinux
      Loaded policy name:             targeted
      Current mode:                   permissive
      Mode from config file:          permissive
      Policy MLS status:              disabled
      Policy deny_unknown status:     allowed
      Memory protection checking:     actual (secure)
      Max kernel policy version:      31

Enforcing mode Setup
********************

This guide serves as a reference implementation and will not be diving into custom policy writing or analysing and fixing SELinux denial details.

1. Assuming you are now in permissive mode, use ``audit2why -al`` to list all the policy violations that occured since booting up.

2. We will be using the ``audit2allow`` tool to generate a local policy and resolve all the violations seen. Run:

   .. code-block:: console

      root@<machine>:~# audit2allow -a -M myPolicy

   Follow the instructions generated by the tool to activate the policy.

   .. warning::

      It is not recommended to use ``audit2allow`` to generate a local policy module as your first option when you see an SELinux denial. Troubleshooting should start with a check if there is a labeling problem. The second most often case is that you have changed a process configuration, and you forgot to tell SELinux about it

3. Update :file:`/etc/selinux/config` to ``SELINUX=enforcing``, save and reboot.

   .. note::

      Remember that boot parameter ``security=selinux`` must always be present otherwise you will have to begin anew.

4. Verify your status by using ``sestatus`` or ``getenforce``.

   .. code-block:: console

      root@<machine>:~# sestatus
      SELinux status:                 enabled
      SELinuxfs mount:                /sys/fs/selinux
      SELinux root directory:         /etc/selinux
      Loaded policy name:             targeted
      Current mode:                   enforcing
      Mode from config file:          enforcing
      Policy MLS status:              enabled
      Policy deny_unknown status:     allowed
      Memory protection checking:     actual (secure)
      Max kernel policy version:      31

Integrating into Yocto for production
*************************************

The above steps are useful during development but unusable in a production environment. The following are pointers to help build a final image which does not require the above steps.

1. ``security=selinux`` can be added into :file:`sources/meta-arago/meta-arago-distro/recipes-tisdk/tisdk-uenv/tisdk-uenv/uEnv.txt` to make it default.

2. To relabel on first boot, add ``FIRST_BOOT_RELABEL="1"`` in :file:`local.conf`

3. To set the default selinux mode, add ``DEFAULT_ENFORCING="<mode>"`` in :file:`local.conf`, where <mode> is disabled/permissive/enforcing.

4. Once the policy has been created, there are multiple ways to install it. This post_install section can be added into your recipe, myPolicy.pp is the policy that is placed in the meta-selinux directory:

   .. code-block:: console

      SRC_URI += "file://myPolicy.pp"

      do_install:append() {
         install -d ${D}/etc/selinux/targeted/modules/active/modules
         install -m 0644 ${WORKDIR}/myPolicy.pp ${D}/etc/selinux/targeted/modules/active/modules/
      }

      pkg_postinst_ontarget:${PN}() {
         #!/bin/bash
         /usr/sbin/semodule -i /etc/selinux/targeted/modules/active/modules/myPolicy.pp
      }
