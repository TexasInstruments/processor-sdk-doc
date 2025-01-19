How do I integrate a different version of open source software than what is packaged in |__SDK_FULL_NAME__|?
============================================================================================================

If users have a need to move to a different component version (older or newer)
because of an existing bug, feature limitations or other reasons, TI will not
support the version migration. As a reference, TI provides the list of a few
recipes that were updated while integrating the components to the
|__SDK_FULL_NAME__|.

::


        ├── QT5:
        │    ├──Baseline:
        │    │     └──meta-qt5:recipes-qt/qt5/: recipes and patches from community
        │    │
        │    └──Arago (TI) updates:
        │         ├──meta-arago:
        │         │ ├──meta-arago-distro/recipes-qt/qt5: recipes update and additional patches
        │         │ ├──meta-arago-extra/recipes-qt/examples:local qt5 examples
        │         │ ├──meta-arago-distro/recipes-qt/examples:local qt5 examples recipe update and patches
        │         │ ├──meta-arago-distro/recipes-core/packagegroups: no changes are expected
        │         │ │   ├──packagegroup-arago-qte.bb
        │         │ │   ├──packagegroup-arago-tisdk-qte.bb
        │         │ │   └──packagegroup-arago-tisdk-qte-sdk-host.bb
        │         │ ├──meta-arago-extras\recipes-core\packagegroups: no changes are expected
        │         │ │   └──packagegroup-arago-qte-toolchain-target.bb
        │         │ │
        │         │ ├──meta-arago-distro/conf/layer.conf: No changes needed for QT configurations
        │         │ └──meta-arago-distro/conf/distro/arago.conf
        │         └──meta-processor-sdk:
        │               └──recipes-qt/qt5: additional recipe updates and patches
        ├──Wayland/Weston:
        │    ├──Baseline:
        │    │     └──oe-core/meta/recipes-graphics/wayland: recipes and patches from community
        │    │
        │    └──Arago (TI) updates:
        │         ├──meta-arago:
        │         │ ├──meta-arago-distro/recipes-graphics/wayland: recipes update and additional patches
        │         │ ├──meta-arago-extras/recipes-graphics/wayland/wayland-protocols
        │         │ ├──meta-arago-distro/recipes-graphics/wayland/wayland-ivi-extension: wayland-ivi recipes
        │         │ ├──meta-arago-distro/recipes-graphics/wayland/weston-conf: weston configuration
        │         │ └──meta-arago-distro/conf/distro/arago.conf: DISTRO_FEATURES

        Note: There are many modules that depend on wayland. For example: chromium-wayland, qt5/qtwayland, gstreamer1.0-plugins-bad(waylandsink), glmark2 and gtk+3
        ├──SGX (Not recommended to modify):
        │    ├──Baseline:
        │    │
        │    ├──meta-ti:
        │    │  ├──recipes-graphics/libgles/ti-sgx-ddk-um_<version>
        │    │  └──recipes-bsp/powervr-drivers/ti-sgx-ddk-km_<version>
        │    │
        │    ├──meta-arago:
        │    │  ├──meta-arago-extras/recipes-graphics/img-pvr-sdk
        │    │  ├──meta-arago-distro/recipes-tisdk/ti-tisdk-makefile/ti-tisdk-makefile/Makefile_ti-sgx-ddk-km
        │    │  └──meta-arago-distro/conf/distro/include/arago-prefs.inc: define virtual/egl, virtual/libgles1 and virtual/libgles2
        │    │
        │    │ Note: There are many modules that depend on sgx, but that does not affect sgx update.
        │    │
        │    └──Arago (TI) updates:
        │       └──meta-processor-sdk:
        │           └──recipes-graphics/libgles/ti-sgx-ddk-um_version: for non-sgx build only
        ├──Gstreamer:
        │    ├──Baseline:
        │    │
        │    ├──meta-openembedded:
        │    │  └──meta-multimedia/recipes-multimedia/gstreamer-0.10: recipes and patches from community
        │    │
        │    │
        │    ├──oe-core:
        │    │  └──meta/recipes-multimedia/gstreamer: recipes and patches from community
        │    │      ├──gstreamer1.0-plugins-base
        │    │      ├──gstreamer1.0-plugins-bad
        │    │      ├──gstreamer1.0-plugins-good
        │    │      ├──gstreamer1.0-plugins-ugly
        │    │      └──gstreamer1.0-libav
        │    │
        │    └──Arago (TI) updates:
        │       └──meta-arago:
        │       ├──meta-arago-extras/recipes-multimedia/gst-plugins-ti: TI-specific recipes for TI plugins
        │       ├──meta-arago-extras/recipes-multimedia/gstreamer/gstreamer1.0-plugins-bad: recipes update and additional patches
        │       ├──meta-arago-distro/conf/distro/arago.conf: configuration
        │       └──meta-arago-distro/recipes-core/packagegroups/packagegroup-arago-tisdk-multimedia-sdk-target.bb: package


If users wish to learn more about Yocto project or Arago build, please refer to the below video link and the documentation on `Building Processor SDK Linux through Yocto <../../Overview_Building_the_SDK.html>`__.

- https://training.ti.com/customizing-yocto-for-production-introduction

