How to enable Microtips LVDS Panel
==================================

**Microtips Technology USA (13-101HIEB0HF0-S) 10.1"  WUXGA (1920x1200) TFT LCD panel**
is supported on platforms:

   - `AM62X SK <https://www.ti.com/tool/SK-AM62>`__
   - `AM62X LP SK <https://www.ti.com/tool/SK-AM62-LP>`__
   - `AM62P SK <https://www.ti.com/tool/SK-AM62P-LP>`__
   - `AM62B SK <https://www.ti.com/tool/SK-AM62B>`__
   - `AM62B-P1 <https://www.ti.com/tool/SK-AM62B-P1>`__

Steps to enable OLDI Panel DT overlay
-------------------------------------

#. Follow the :ref:`How to enable DT overlays in linux <howto_dt_overlays>` guide for steps on building
   and adding the overlay to your SD card. Make sure the correct overlay file has been appended
   in the ``name_overlays`` variable as suggested in the same page.

.. ifconfig:: CONFIG_part_variant in ('AM62X')

      +---------------+---------------------------------------------+
      |  Board        | overlay file name                           |
      +===============+=============================================+
      |  AM62X SK     | k3-am625-sk-microtips-mf101hie-panel.dtbo   |
      +---------------+---------------------------------------------+
      |  AM62X LP SK  | k3-am62-lp-sk-microtips-mf101hie-panel.dtbo |
      +---------------+---------------------------------------------+

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

      +---------------+---------------------------------------------+
      |  Board        | overlay file name                           |
      +===============+=============================================+
      |  AM62PX SK    | k3-am62p5-sk-microtips-mf101hie-panel.dtbo  |
      +---------------+---------------------------------------------+


Steps to enable Touch on the Microtips Panel on AM625 SK EVM
------------------------------------------------------------

AM62X SK E3 revision
^^^^^^^^^^^^^^^^^^^^

#. Power off the LVDS board by disconnecting the 12V barrel jack (do not power off the SK EVM)
#. Run the following commands from the Linux prompt:

   .. code-block:: console

      root@am62xx-evm:~# modprobe -r ili210x
      root@am62xx-evm:~# i2ctransfer -f -y 0 w3@0x3f 0x09 0x1 0x0e
      root@am62xx-evm:~# i2ctransfer -f -y 0 w6@0x3f 0x08 0x04 0x47 0x50 0x73 0x68
      root@am62xx-evm:~# i2ctransfer -f -y 0 w1@0x3f 0x72 r9

#. Power on the LVDS board
#. Run the following command:

   .. code-block:: console

      root@am62xx-evm:~# modprobe ili210x

After re-initializing the module, the touch IC should now be registered as an input and touch should be functional.

AM62B SK & AM62B-P1
^^^^^^^^^^^^^^^^^^^

#. Run the following command

   .. code-block:: console

      root@am62xx-evm:~# modprobe -r ili210x

#. Power off the LVDS panel by disconnecting the 12V barrel jack (do not power off the SK EVM)
#. Power on the LVDS panel
#. Run the following command

   .. code-block:: console

      root@am62xx-evm:~# modprobe ili210x

After re-initializing the module, the touch IC should now be registered as an input and touch should be functional.

.. note::

   ``i2ctransfer`` not required for AM62B SK & AM62B-P1
