##########################################
SDK File System Optimization/Customization
##########################################

The purpose of this article is to explain the file system that is
delivered as part of the |__SDK_FULL_NAME__| and how this file system
can be modified to customize it for your use case. The tools discussed
in this article are installed by default in the |__SDK_FULL_NAME__| file
system for your convenience.

There are different filesystem tarball provided in the SDK. Refer :ref:`Foundational_Components/Filesystems <List-of-filesystems-in-SDK>` for more details.
All of these filesystems contain the :command:`opkg` package manager and can be used as a starting point for system optimization as discussed in the next sections.

******************
The Basics of OPKG
******************

List all available options of opkg
==================================

:command:`opkg` is the package manager used in the SDK file system to install
and remove packages. You can get a list of the full commands supported
by :command:`opkg` by running the following command on the target device:

.. code-block:: console

   root@<machine>:~# opkg

To check the version of :command:`opkg` packaged in filesystem,

.. code-block:: console

   root@<machine>:~# opkg --version
   opkg version 0.6.3 (libsolv 0.7.28)

Show all installed packages
===========================

To the list of packages are part of the file system and the version of
each package you can run the following command on the target device:

.. code-block:: console

   root@<machine>:~# opkg list-installed

.. important::

 This list only contains information about packages that were
 installed using the package manager. Applications that were built and
 copied to the file system and not installed as a .ipk package are not
 tracked by :command:`opkg`

Show package contents
=====================

Sometimes it is useful to know what files a package has installed. To do
this you can use the following command:

.. code-block:: console

   root@<machine>:~# opkg files <pkgname>

Where <pkgname> is the name of the package as given in the *opkg
list-installed* output. This command will produce a list of all the
files on the file system that belong to the given package.

Find a file owner
=================

Sometimes you may find a file on the target file system that you want to
remove, or just know where it came from. In this case you can use the
following command:

.. code-block:: console

   root@<machine>:~# opkg search <file>

This command will find which package installed the given file. This may
be useful later when you want to remove an particular file because this
command can help you find the package to remove.

Show packages which require the package as dependency
=====================================================

Sometimes when you want to remove a package it is useful to find out
what other packages depend on the package you are removing. While the
opkg remove command will tell you the immediate dependencies you can
find the longer list of dependencies using:

.. code-block:: console

   root@<machine>:~# opkg whatdepends <pkgname>

This command will print the list of packages the depend on the package
you entered, as well as the packages that depend on those packages, and
so forth.

Removing Packages or Deinstallation
===================================

One of the simplest ways to modify the contents of the file system is to
use the :command:`opkg` utility to remove packages (or install if you have
pre-built packages). Removing a package is often as simple as:

.. code-block:: console

   root@<machine>:~# opkg remove <pkgname>

However, sometimes a package is a DEPENDENCY of another package. In this
case you have the following options:

-  Use the ``--force-depends`` option

   -  This option will force the removal of the package but will leave
      any packages that depend on this package installed. This can be
      useful in the case that you want to remove a particular package,
      but that package is depended on by some other package that you do
      not want removed.

-  Use the ``--force-removal-of-dependent-packages`` option

   -  This option will go up the dependency list and remove all packages
      in the dependency chain. You should check all the packages being
      removed to make sure they are indeed packages you want to remove
      and do not contain other files you want.

-  Remove the individual packages that depend on this package first

   -  This way you can control exactly which dependent packages are
      removed and which are left in place.

.. code-block:: console

   root@<machine>:~# opkg remove --force-removal-of-dependent-packages <pkgname>

.. tip::

   opkg will print the packages that depend on the package being
   removed. It is usually a good idea to use the *opkg files* command for
   the packages that depend on the one being removed so that you can make
   sure that no files you really want to keep are going to be removed.

.. tip::

   You can also use the whatdepends option discussed above to see
   the dependency list for a package

By using the :command:`opkg remove` command in conjunction with the commands for
listing packages, finding file owners, and listing package contents, you
can quickly strip down a full file system into something smaller and
more optimized for your use case. However, once a package is removed it
cannot currently be re-installed without generating the .ipk file to
install it.

Install local packages
======================

In most cases installing additional applications can be as simple as
copying the the binary executable to the file system. However, if you
have built your own **.ipk packages** you can use opkg to install those ipks
into the target file system.

One major advantage of using the package manager is the ability to track the package and it's content with the
opkg package manager. More details about how to build & install your own packages is available at :ref:`Building the SDK with Yocto <building-the-sdk-recipes>`

To learn about Arago project, please visit `Arago/TI-SDK distribution <https://layers.openembedded.org/layerindex/branch/scarthgap/layer/meta-arago-distro/>`__.
