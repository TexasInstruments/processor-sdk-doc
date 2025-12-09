.. _howto_dt_overlays:

**********************************
How to enable DT overlays in linux
**********************************


The |__SDK_FULL_NAME__| supports various features in the form of device-tree overlays appended on top of the board device-tree source files. These features can only be used after enabling their respective overlay blobs (\*.dtbo files). Below are the steps to compile the DT overlay sources, install them on the SD Card, and enable them at the u-boot stage. The SD Card wic image (:file:`tisdk-default-image`) comes with the overlay blobs pre-loaded on the SD Card, and steps 3 through 5 can be skipped, if there are no custom changes required on the DT overlay sources.

.. important::

    These steps are only applicable for GP and HS-FS devices. For HS-SE devices, follow steps 1 through 4, and post that, kindly refer to: :ref:`fitImage-for-HS`, to package the requrired DTBOs in the fitImage.

Steps to enable DT overlays:
============================

#. Flash the SD card with the :file:`tisdk-default-image` available at |__SDK_DOWNLOAD_URL__|.
#. If the SD card got auto-ejected after flashing, re-plug it.
#. On the host machine, build dtbs in the PSDK linux source tree, without any
   changes. Refer to :ref:`Users Guide
   <kernel_users_guide_compiling_the_device_tree_binaries>` for more details.


    .. code-block:: console

        $ make CROSS_COMPILE=aarch64-none-linux-gnu- ARCH=arm64 clean
        $ make CROSS_COMPILE=aarch64-none-linux-gnu- ARCH=arm64 dtbs

#. If the build is successful, the required DT overlay files shall be found as below:

    .. code-block:: console

        $ ls arch/arm64/boot/dts/ti/k3-<required-soc>-*.dtbo

#. Copy this DT overlay file to the :file:`boot/dtb/ti` directory of the root partition of the SD card.

    .. code-block:: console

        $ sudo cp arch/arm64/boot/dts/ti/k3-<overlay>.dtbo <path-to-sd-root>/boot/dtb/ti/

#. Update the :file:`uEnv.txt` file under the boot partition of the SD card, to let u-boot recognize the overlay. Depending on the use-case, multiple DT overlays can also be added, using "space" as the delimiter.

    .. code-block:: console

        name_overlays=ti/k3-<overlay-1>.dtbo ti/k3-<overlay-2>.dtbo ti/k3-<overlay-3>.dtbo

#. Unmount and eject the SD card. Plug it back in the |__PART_FAMILY_NAME__| board and turn the board on.
