.. _oob-demo-applications:

##################
Demo Applications
##################

The SDK supports the following Out-Of-Box demo-applications

.. toctree::
   :maxdepth: 1

   Edge_AI_Gallery_User_Guide
   TI_Apps_Launcher_User_Guide
   Seva_Store
   Chromium_Browser
   Benchmark_Demo_User_Guide
   Webserver_Demo_User_Guide
   Display_Cluster_User_Guide
   TI_LVGL_Demo_User_Guide
   AM62D_Dsp_Offload_User_Guide.rst
   AM62D_2DFFT_User_Guide.rst
   EV_charging_Demo_User_Guide.rst

.. ifconfig:: CONFIG_sdk in ('j7_foundational')

   Use the tisdk-default-image-|__SDK_BUILD_MACHINE__| to be able to run the above demo applications.

   - Refer to :ref:`hardware-evm-setup` for preliminary hardware setup.
   - Refer to :ref:`processor-sdk-linux-create-sd-card` to prepare a SD card with the tisdk-default-image provided in the SDK.
   - To run a demo refer to the respective user guide from above
