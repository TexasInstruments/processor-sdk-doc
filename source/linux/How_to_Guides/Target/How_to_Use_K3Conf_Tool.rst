How to Use K3Conf Tool
======================

Overview
--------

k3conf is standalone application designed to offer as a quick and easy way to
diagnose, debug and audit TI K3 architecture based processors configuration at
runtime, with no particular kernel dependency.

k3conf is designed to be platform-agnostic, being able to
run on any Linux platform and easily ported to other OS.
Even if k3conf today focuses mainly on TISCI related functionality, it is
intended to be extended to any other area.

.. _How-to-use-k3conf-label:

How to use
----------

k3conf is part of yocto build and SDK installer. On target user needs to use command :command:`k3conf`

Type ``k3conf --help`` to get complete list of available commands and options.

.. attention::

  K3CONF currently supports AM654, J721E, J7200, AM64x, AM62x, AM62P, J721S2, J784S4, AM62Ax and AM62Lx devices.

Source code for k3conf tool is available at `git.ti.com/k3conf <https://git.ti.com/cgit/k3conf/k3conf/>`__
and the Yocto recipe to package in filesystem is available at `git.ti.com/meta-ti <https://git.ti.com/cgit/arago-project/meta-ti/tree/meta-ti-bsp/recipes-devtools/k3conf/k3conf_git.bb?h=scarthgap>`__

