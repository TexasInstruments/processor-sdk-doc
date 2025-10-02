.. _u-boot-build-guide-setup-k3:

#####
Setup
#####

*************************
Install host dependencies
*************************

To install host dependencies for building TI U-boot source (standalone)
on Ubuntu 22.04+, run the following command in the terminal prompt:

.. code-block:: console

   sudo apt install git xz-utils build-essential autoconf flex bison libssl-dev bc libncurses-dev \
   python3 python3-setuptools python3-dev python3-yaml python3-jsonschema python3-pyelftools \
   swig yamllint libgnutls28-dev

.. note::

   The recommended host machine for building U-Boot is Ubuntu 22.04.
   Users of Ubuntu 18.04 might need to install Python 3.7 or later. If using the default Python 3.6
   that is in Ubuntu 18.04, users might need to install these additional dependencies:

   .. code-block:: console

      pip install dataclasses pyelftools jsonschema yamllint importlib-resources

.. _Getting the U-Boot Source Code-label:

***********************
Getting the Source Code
***********************

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   .. note::

      AM62L devices use TF-A BL-1 boot loader to configure LPDDR4 to
      enable secondary program loader.

The easiest way to get access to the source code is by
downloading and installing the Processor SDK Linux. Once installed,
the source code is in the SDK at the path :file:`<path to tisdk>/board-support`.
For your convenience the sources also includes
git repositories including commit history.

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   Alternatively, BL-1 and U-Boot sources can directly be fetched from GIT. The GIT
   repo URL, branch and commit id can be found in the release notes:

   - ti-u-boot , OPTEE, TF-A and ti-linux-firmware version is at :ref:`release-specific-build-information`

.. ifconfig:: CONFIG_part_variant not in ('AM62LX')

   Alternatively, U-Boot sources can directly be fetched from GIT. The GIT
   repo URL, branch and commit id can be found in the release notes:

   - ti-u-boot version: :ref:`u-boot-release-notes`
   - ti-linux-firmware version: :ref:`ti-linux-fw-release-notes`
   - TF-A version: :ref:`tf-a-release-notes`
   - OP-TEE version: :ref:`optee-release-notes`
