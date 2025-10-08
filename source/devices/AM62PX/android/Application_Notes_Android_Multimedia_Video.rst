.. _Android Multimedia Wave5:

########################################
Android Multimedia (Video encode/decode)
########################################

This application note describes video decoding/encoding using the onboard Wave5 chip
found in the Texas Instruments AM62Px SoC.

The Wave5 hardware is implemented via:

- the ``wave5`` driver, located in :file:`~/10_01_01/ti-kernel-aosp/common/drivers/media/platform/chips-media/wave5/`
- a firmware located in :file:`~/11_00_00/ti-aosp-16/vendor/ti/vendor/ti/am62x/firmware/vendor/firmware/cnm/`

The userspace associated component is based on the AOSP-provided ``v4l2_codec2`` HAL.
The source can be found in :file:`~/11_00_00/ti-aosp-16/external/v4l2_codec2`.


*******
Testing
*******

Using ``atest``
===============

Android provides all kind of tests to test the media framework.
We can run a sample playback via ``atest`` from a development tree.

.. code-block:: console

   # Standard Android build commands
   $ cd ${YOUR_PATH}/ti-aosp-15
   $ source build/envsetup.sh
   $ lunch <BUILD_TARGET>

   # install the required media files, downloads from network
   $ cts/tests/tests/media/player/
   $ ./copy_media.sh
   $ cd -

   # run the playback test
   $ atest android.media.player.cts.MediaPlayerTest#testLocalVideo_MP4_H264_480x360_500kbps_25fps_AAC_Stereo_128kbps_44110Hz

Using Gallery
=============

To play test videos, we can also use the Gallery app.

First, download the Big Buck Bunny test videos:

.. code-block:: console

   # 1080p, 60FPS, h264
   $ wget http://distribution.bbb3d.renderfarming.net/video/mp4/bbb_sunflower_1080p_60fps_normal.mp4

   # 4k, 30FPS, h264
   $ wget http://distribution.bbb3d.renderfarming.net/video/mp4/bbb_sunflower_2160p_30fps_normal.mp4

Then, push them in the :file:`Movies` folder:

.. code-block:: console

   $ adb push bbb_sunflower_1080p_60fps_normal.mp4 /sdcard/Movies
   $ adb push bbb_sunflower_2160p_30fps_normal.mp4 /sdcard/Movies

Finally, reboot the board:

.. code-block:: console

   $ adb reboot

Then run the Gallery app from the UI and play the videos.

Using ``screenrecord``
======================

To test video encoding, we can use the ``screenrecord`` command.

.. code-block:: console

   $ adb root
   $ adb shell 'screenrecord /data/screenrecord.mp4' # Do some screen activity, then hit Ctrl-C
   $ adb pull /data/screenrecord.mp4

.. tip::

   ``screenrecord`` only records frames when there is some user activity detected.
   Make sure to generate some activity to avoid empty video files.

**************
Debugging tips
**************

List available codecs
=====================

``dumpsys`` can be used to list the available codecs on an Android system.
To check that the v4l2 codecs are available, run:

.. code-block:: console

   $ adb shell dumpsys media.player | grep -A 10 v4l2
      Decoder "c2.v4l2.avc.decoder" supports
        aliases: []
        attributes: 0xa: [
          encoder: 0,
          vendor: 1,
          software-only: 0,
          hw-accelerated: 1 ]
        owner: "codec2::default"
        rank: 128
        profile/levels: [
              1/65536 (Baseline/5.2),
    --
      Decoder "c2.v4l2.hevc.decoder" supports
        aliases: []
        attributes: 0xa: [
          encoder: 0,
          vendor: 1,
          software-only: 0,
          hw-accelerated: 1 ]
        owner: "codec2::default"
        rank: 128
        profile/levels: [
              1/524288 (Main/High 5.2),
    --
      Encoder "c2.v4l2.avc.encoder" supports
        aliases: []
        attributes: 0xb: [
          encoder: 1,
          vendor: 1,
          software-only: 0,
          hw-accelerated: 1 ]
        owner: "codec2::default"
        rank: 128
        profile/levels: [
              1/32768 (Baseline/5.1),


Verbose logcat logging
======================

The logs in logcat from ``v4l2_codec2`` are not very verbose by default.
To enable more logs, ``v4l2_codec2`` should be rebuild. It's possible to enable all logs with:

.. code-block:: console

   $ cd ~/src/ti-aosp-15/external/v4l2_codec2
   $ sed -i 's#//\#define LOG_NDEBUG 0#\#define LOG_NDEBUG 0#' *.cpp
