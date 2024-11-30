..
    The top level heading in this rst file would be level 2 header with `====`

Rogue Debug Info
================

Rogue graphics drivers include the following tools bundled with their user mode
libraries:

.. list-table:: Included rogue debug tools

   * - pvrdebug
     - Control debug verbosity and other device info
   * - pvrlogdump
     - Dump diagnostic information for an application
   * - pvrsrvctl
     - Start, Stop, Restart and configure the GPU using a powervr.ini file
   * - rgx_blit_test
     - Attempt a number of blit opperations and display them to the screen
   * - rgx_compute_test
     - Attempt a number of compute tasks on the core
   * - rgx_kicksync_test
     - Attempt a number of processes on the core to stress the KickSync API
   * - rgx_triangle_test
     - Render a triangle to the attached display
   * - rgx_twiddling_test
     - Attempt to twiddle a number of textures in a number of pixel formats

While future releases of ti-img-rogue-umlibs may include more tools, this is
the core set expected to be available in most ti-img-rogue-umlibs releases and
are the most useful for verifying GPU functionality.

The order of operation to verify fundamental GPU functionality is as follows:

   #. Use rgx_kicksync_test to verify the GPU can communicate with the kernel
      module.

   #. Use rgx_compute_test to verify that the GPU is able to handle a proper
      compute load.

   #. Use rgx_triangle_test to verify that the GPU is able to render to an
      output buffer.


If fundamental functionality has been verified and you are still experiencing
issues try checking the output of the following:

.. code-block:: console

   # pvrdebug -dd

.. note::

   When raising a ticket on e2e forums it is useful to include the output of
   this command if available.

This will dump all device information as reported by the kernel module. Please
insure that the debug info reports:

.. code-block:: text

   Comparison of UM/KM components: MATCHING

User mode and Kernel mode components must move in lockstep. If they do not
match this could lead to the kernel module failing to initialize or undefined
behavior.
