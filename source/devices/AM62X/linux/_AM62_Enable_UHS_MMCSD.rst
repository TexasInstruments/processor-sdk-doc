
AM62 SD UHS Speed modes Enable
==============================

In 08.03 release, SD card enumeration failures were observed on a few U1
class of SD cards. These include but not limited to,

#. Microcenter U1 class cards
#. Kingston U1 class cards
#. HP U1 class cards

A conservative approach was taken to disable UHS modes
by default, and support wide range of SD cards. However if required they
can be enabled by using the following steps,

    - Yocto build Flow

        #. Revert the following commits, from meta-processor-sdk layer

            #. https://git.ti.com/cgit/processor-sdk/meta-processor-sdk/commit/?h=dunfell&id=75a86ac2cd049b606a121736a7b73ed26aded5a8
            #. https://git.ti.com/cgit/processor-sdk/meta-processor-sdk/commit/?h=dunfell&id=0d1b740906f182f6570f9d01b52ad92dab1aae88

        #. Cleaning up U-Boot and Kernel repos

            ::

               $MACHINE=am62x-evm bitbake -f linux-ti-staging-c do_cleansstate
               $MACHINE=am62x-evm bitbake -f u-boot-ti-staging -c do_cleansstate

        #. Rebuild the wic image

            ::

               $MACHINE=am62x-evm bitbake -f tisdk-default-image

    - Building from source tree

        Run the following commands in respective src tree directories to revert UHS disable patches.

            #. <SDK_INSTALL_PATH>/board-support/linux-5.10.109+gitAUTOINC+9e58028f94-g9e58028f94

                ::

                    patch -p1 -R < patches/0001-arm64-dts-ti-k3-am62-main-Disable-UHS-speed-modes-on.patch

            #. <SDK_INSTALL_PATH>/board-support/u-boot-2021.01+gitAUTOINC+74fc69c889-g74fc69c889

                ::

                    patch -p1 -R < patches/0001-Revert-arm-dts-k3-am625-sk-u-boot-Add-u-boot-tag-to-.patch
                    patch -p1 -R < patches/0002-Revert-configs-am62x_evm_a53_defconfig-Enable-config.patch

            #. Recompile dtb

                ::

                    make linux-dtbs

            #. Recompile the kernel Image

                ::

                    make linux

            #. Recompile the bootloaders

                ::

                    make u-boot
