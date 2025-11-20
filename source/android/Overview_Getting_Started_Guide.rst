.. _android-prebuilts:

Using Prebuilt binaries
=======================

.. note::

    Linux machine running Ubuntu is needed for building and flashing Android images to the EVM

.. ifconfig:: CONFIG_part_variant in ('AM62X')

    The SDK download page provides pre-built Android binaries (:file:`AM62x_{XX}.{YY}.{ZZ}_emmc.tgz`) which can be readily used to flash the |__PART_FAMILY_NAME__| EVM and boot Android.

    Extract the contents of the pre-built images tarball and follow the procedure mentioned in :ref:`android-flashing` page to flash these binaries to the EVM.

    .. code-block:: console

       $ tar -zxvf AM62x_XX.YY.ZZ_emmc.tgz


.. ifconfig:: CONFIG_part_variant in ('AM62PX')

    The SDK download page provides pre-built Android binaries (:file:`AM62Px_{XX}.{YY}.{ZZ}_emmc.tgz`) which can be readily used to flash the |__PART_FAMILY_NAME__| EVM and boot Android.

    Extract the contents of the pre-built images tarball and follow the procedure mentioned in :ref:`android-flashing` page to flash these binaries to the EVM.

    .. code-block:: console

       $ tar -zxvf AM62Px_XX.YY.ZZ_emmc.tgz


.. ifconfig:: CONFIG_part_variant in ('AM67A')

    The SDK download page provides pre-built Android binaries (:file:`AM67A_{XX}.{YY}.{ZZ}_emmc.tgz`) which can be readily used to flash the |__PART_FAMILY_NAME__| EVM and boot Android.

    Extract the contents of the pre-built images tarball and follow the procedure mentioned in :ref:`android-flashing` page to flash these binaries to the EVM.

    .. code-block:: console

       $ tar -zxvf AM67A_XX.YY.ZZ_emmc.tgz

