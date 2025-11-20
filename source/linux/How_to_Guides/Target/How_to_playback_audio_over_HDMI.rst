.. _hdmi-audio:

*******************************
How to playback audio over HDMI
*******************************

SK-|__PART_FAMILY_NAME__| supports audio playback over HDMI. This
requires shorting a jumper on the board, and applying an additional DT overlay
(.dtbo) file: :file:`k3-am62x-sk-hdmi-audio.dtbo`.

Steps to enable audio over HDMI
===============================

#. Toggle the FET switch that shares audio lines between the 3.5mm Jack and
   HDMI connector. For this you have to short a jumper on the
   SK-|__PART_FAMILY_NAME__|, at the location marked below:

    .. Image:: ../../../images/AM62x_HDMI_Audio_Jumper.jpg
            :scale: 10%

#. Follow the :ref:`How to enable DT overlays in linux <howto_dt_overlays>`
   guide for steps on building and adding the overlay in your SD card.

    (You may skip this step if the overlay is already present in
    :file:`/boot/dtb/ti` under the root partition of your SD card)

#. Enable the HDMI audio overlay by updating the ``name_overlays`` variable in
   the :file:`uEnv.txt` file under the BOOT partition on your SD card.

    .. code-block:: text

        name_overlays=ti/k3-am62x-sk-hdmi-audio.dtbo

#. Finally, reboot the board and playback a .WAV or raw PCM data using
   :command:`aplay`:

    .. code-block:: text

        aplay <path to wav file>

    You can also check out the :ref:`Audio Linux Driver Guide <Audio_User_Guide>` for
    more information on using :command:`aplay`.


.. note::

    To playback or capture audio on 3.5mm jack, you will need to remove the
    jumper cable and the overlay from :file:`uEnv.txt`. Only one of the
    peripherals can be used at any given time.
