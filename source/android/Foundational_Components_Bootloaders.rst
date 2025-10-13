###################
Android Bootloaders
###################

**Getting toolchain for u-boot builds**

The toolchains are automatically downloaded by the build scripts.

**Install OPTEE-OS build dependencies**

Check OPTEE-OS docs to know list of dependencies needed to be installed :
https://optee.readthedocs.io/en/latest/building/prerequisites.html


**Install additional dependencies**

.. code-block:: console

   $ sudo apt install bc bison build-essential curl u-boot-tools flex git libssl-dev python3 python3-pip wget -y
   $ pip3 install pycryptodome pyelftools shyaml --user


.. _android-download-bootloaders:

*******************
Downloading sources
*******************

Fetch the code using ``repo``:

.. code-block:: console

   $ mkdir ${YOUR_PATH}/ti-bootloader-aosp/ && cd $_
   $ repo init -u https://git.ti.com/git/android/manifest.git -b android16-release -m releases/RLS_11_00_Bootloader.xml
   $ repo sync

For more information about ``repo``, visit `Android's official
documentation <https://source.android.com/setup/build/downloading>`__

.. _android-build-bootloaders:

******************
Build Instructions
******************

#. Build bootloaders images using:

   .. code-block:: console

      $ cd ${YOUR_PATH}/ti-bootloader-aosp/
      $ ./build/build_all.sh --config=build/config/boards/am62x-sk.yaml

   This will generate all the required bootloaders in :file:`out/am62x-sk/release`:

   .. code-block:: console

      $ tree out
      out/am62x-sk/
      └── release
          ├── bl31-release.bin
          ├── tee-release.bin
          ├── tiboot3-release-gp.bin
          ├── tiboot3-release-hsfs.bin
          ├── tispl-release.bin
          └── u-boot-release.img

   These binaries are valid for an AM62X SoC.
   To build for other boards, look at :file:`build/config/boards`.
   We can see the following valid combinations:

   .. ifconfig:: CONFIG_part_variant in ('AM62X')

      .. list-table::
         :header-rows: 1

         * - Name
           - Description

         * - am625-beagleplay-dfu.yaml
           - BeaglePlay board with DFU boot enabled (usage with snagboot)

         * - am625-beagleplay.yaml
           - BeaglePlay board (regular eMMC boot)

         * - am62x-lp-sk-dfu.yaml
           - AM62x LP board with DFU boot enabled (usage with snagboot)

         * - am62x-lp-sk.yaml
           - AM62x LP board (regular eMMC boot)

         * - am62x-sk-dfu.yaml
           - AM62x board with DFU boot enabled (usage with snagboot)

         * - am62x-sk.yaml
           - AM62x board (regular eMMC boot)

   .. ifconfig:: CONFIG_part_variant in ('AM62PX')

      .. list-table::
         :header-rows: 1

         * - Name
           - Description

         * - am62p-sk-dfu.yaml
           - AM62Px board with DFU boot enabled (usage with snagboot)

         * - am62p-sk.yaml
           - AM62Px board (regular eMMC boot)

#. From :file:`out/am62x-sk/release`, copy the :file:`tiboot3.bin`, :file:`tispl.bin`
   and :file:`u-boot.img` generated to
   :file:`${YOUR_PATH}/ti-aosp-16/vendor/ti/am62x/bootloader`.

   If not copied, the prebuilt bootloader binaries already present
   in :file:`vendor/ti/am62x/bootloader` will get used by :file:`flashall.sh` flashing script.

   .. ifconfig:: CONFIG_part_variant in ('AM62X')

      For picking the correct filenames, refer to the `upstream documentation <https://docs.u-boot.org/en/latest/board/ti/am62x_sk.html#target-images>`__.

   .. ifconfig:: CONFIG_part_variant in ('AM62PX')

      For picking the correct filenames, refer to the `upstream documentation <https://docs.u-boot.org/en/latest/board/ti/am62px_sk.html#target-images>`__.

#. Finally, rebuild Android by following :ref:`android-build-aosp`.

.. warning::

   If you also modify Trusted Applications (TA), it's recommended to use the :file:`release_android.sh`
   script to avoid copying all the TAs manually as it's quite error prone.

********************
Release Instructions
********************

In addition to building and copying manually to :file:`${YOUR_PATH}/ti-aosp-16`,
it's also possible to automatically build **all supported variants** and copy them to Android.

Assuming Android has already been downloaded following
:ref:`android-download-aosp`, This can be done using:

.. code-block:: console

   $ cd ${YOUR_PATH}/ti-bootloader-aosp/
   $ ./build/release_android.sh --aosp=${YOUR_PATH}/ti-aosp-16 --commit
   # [...] lots of build logs later

After that, rebuild Android by following :ref:`android-build-aosp` to use the new bootloaders.

.. tip::

   To only release for a particular board, pass the ``--config`` option to :file:`release_android.sh`.
