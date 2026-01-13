.. _u-boot-build-guide-setup-omap:

#####
Setup
#####

*************************
Install host dependencies
*************************

.. ifconfig:: CONFIG_part_variant not in ('AM335X', 'AM437X')

   To install host dependencies for building TI U-boot source (standalone)
   on Ubuntu 22.04+, run the following command in the terminal prompt:

   .. code-block:: console

      sudo apt install git xz-utils build-essential autoconf flex bison libssl-dev bc libncurses-dev \
      python3 python3-setuptools python3-dev python3-yaml python3-jsonschema python3-pyelftools \
      swig yamllint libgnutls28-dev

.. note::

   The recommended host machine for building U-Boot is Ubuntu 22.04.
   Users of Ubuntu 18.04 may need to install Python 3.7 or higher. If using the default Python 3.6
   that comes with Ubuntu 18.04, users may need to install these additional dependencies:

   .. code-block:: console

      pip install dataclasses pyelftools jsonschema yamllint importlib-resources

.. _Getting the U-Boot Source Code-label:

***********************
Getting the Source Code
***********************

The easiest way to get access to the source code is by
downloading and installing the Processor SDK Linux. Once installed,
the source code is included in the SDK at the path :file:`<path to tisdk>/board-support`.
For your convenience the sources also includes
git repositories including commit history.

Alternatively, U-Boot sources can directly be fetched from GIT. The GIT
repo URL, branch and commit id can be found in the release notes:

- ti-u-boot version: :ref:`release-specific-build-information`

*******************************
Setup Cross Compile Environment
*******************************

.. include:: ../../Overview/GCC_ToolChain.rst
   :start-after: .. start_include_yocto_toolchain_host_setup
   :end-before: .. end_include_yocto_toolchain_host_setup
