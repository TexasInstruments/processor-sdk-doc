###########
Android OTA
###########

This application note contains steps to test the OTA (Over The Air) feature on Android.

There are 2 ways of applying an OTA update:

1. :ref:`android-ota-sideload`
2. :ref:`android-ota-update-engine`


.. _android-ota-sideload:

************************
OTA via ``adb sideload``
************************

1. Build and flash android images following :ref:`android-build-aosp` instructions.

2. Build OTA package

   .. code-block:: console

      $ cd ${YOUR_PATH}/ti-aosp-15
      $ source build/envsetup.sh
      $ lunch <BUILD_TARGET>
      $ export DIST_DIR=./dist_output
      $ m dist

3. `Enable adb debugging on your device <https://developer.android.com/studio/command-line/adb#Enabling>`__

4. Reboot to recovery and apply OTA

   .. code-block:: console

      $ adb reboot sideload
      $ adb wait-for-sideload
      $ adb sideload $DIST_DIR/am62x-ota-eng.${USER}.zip
      $ adb reboot


.. _android-ota-update-engine:

*********************
OTA via Update Engine
*********************

1. Build the OTA package

   .. code-block:: console

      $ source build/envsetup.sh
      $ lunch <BUILD_TARGET>
      $ export DIST_DIR=./dist_output
      $ m
      $ m dist

2. Set your ``PYTHONPATH``.

   Some dependent python modules for :file:`gen_update_config.py` are part of AOSP tree or
   part of the build output.

   .. code-block:: console

      $ cd $ANDROID_BUILD_TOP
      $ apex_manifest_pb2_path=$(find out -name 'apex_manifest_pb2.py' -print -quit)
      $ PYTHONPATH=$ANDROID_BUILD_TOP/$(dirname ${apex_manifest_pb2_path}):$PYTHONPATH
      $ PYTHONPATH=$ANDROID_BUILD_TOP/build/make/tools/releasetools:$PYTHONPATH
      $ PYTHONPATH=$ANDROID_BUILD_TOP/system/apex/apexer/:$PYTHONPATH
      $ export PYTHONPATH

3. Patch the :file:`gen_update_config.py` script to be compatible with Android 15.
   In :file:`bootable/recovery`, apply the following change:

   https://android-review.googlesource.com/c/platform/bootable/recovery/+/2837717

   This can be done with:

   .. code-block:: console

      $ cd $ANDROID_BUILD_TOP/bootable/recovery
      $ git fetch https://android.googlesource.com/platform/bootable/recovery refs/changes/17/2837717/1
      $ git cherry-pick FETCH_HEAD

4. Update the ota config file. Feel free to change ``$DIST_DIR`` to match your developer environment.

   .. code-block:: console

      $ source build/envsetup.sh
      $ lunch <BUILD_TARGET>
      $ DIST_DIR=dist_output
      $ BOARD=am62x
      $ bootable/recovery/updater_sample/tools/gen_update_config.py --ab_install NON_STREAMING $DIST_DIR/$BOARD-ota-eng.${USER}.zip $DIST_DIR/$BOARD-ota-eng.${USER}.json file:///data/user/0/com.example.android.systemupdatersample/files/packages/$BOARD-ota-eng.${USER}.zip

   .. warning::

      Be careful, last line is **one single** very long line.

5. Run the SystemUpdaterSample app once:

   .. code-block:: console

      $ adb root
      $ adb shell setenforce 0
      $ adb shell am start com.example.android.systemupdatersample/com.example.android.systemupdatersample.ui.MainActivity

6. Push the files on the board:

   .. code-block:: console

      $ adb root
      $ adb shell mkdir /data/user/0/com.example.android.systemupdatersample/files/configs
      $ adb shell mkdir /data/user/0/com.example.android.systemupdatersample/files/packages
      $ adb push $DIST_DIR/$BOARD-ota-eng.${USER}.json /data/user/0/com.example.android.systemupdatersample/files/configs/
      $ adb push $DIST_DIR/$BOARD-ota-eng.${USER}.zip /data/user/0/com.example.android.systemupdatersample/files/packages/

7. Change SELinux label:

   .. code-block:: console

      $ adb shell chcon -R u:object_r:ota_package_file:s0 /data/user/0/com.example.android.systemupdatersample/


8. Change Unix permisssions:

   .. code-block:: console

      $ adb shell chmod -R 777 /data/user/0/com.example.android.systemupdatersample/

9. Run the update on the UI:

   - Tap on ``RELOAD`` to load the config
   - Tap on ``APPLY`` to apply the OTA
   - Tap ``OK`` to confirm application
   - Wait for progress bar to complete
   - Tap on ``SWITCH SLOT`` to finish update (scroll downwards to see the button)
   - Wait for verification

10. Reboot the device with:

    .. code-block:: console

       $ adb shell svc power reboot

11. Confirm that booting on slot b

    .. code-block:: console

       $ adb root
       $ adb shell grep -o 'androidboot.slot_suffix=[_ab]*' /proc/cmdline
       androidboot.slot_suffix=_b


Troubleshooting
===============

Python 3.12 is not supported, because it removed the ``imp`` module and also comes with a
too recent version of ``protobuf``.

To install and older version, use ``virtualenv``:

.. code-block:: console

   $ pip install virtualenv # make sure python3.11 is installed on your system
   $ virtualenv --py 3.11 venv_ota_build

   $ source venv_ota_build/bin/activate
   $ pip install protobuf==3.20

From here, you should be able to invoke :file:`gen_update_config.py`.
