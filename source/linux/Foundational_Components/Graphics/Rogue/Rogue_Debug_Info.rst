..
    The top level heading in this rst file would be level 2 header with `====`

Rogue debug info
================

Rogue graphics drivers include the following tools bundled with their user mode
libraries:

.. list-table:: Included rogue debug tools

   * - ``pvrdebug``
     - Control debug verbosity and other device info
   * - ``pvrlogdump``
     - Dump diagnostic information for an application
   * - ``pvrsrvctl``
     - Start, Stop, Restart and configure the GPU using a powervr.ini file
   * - ``rgx_blit_test``
     - Try several blit operations and display them to the screen
   * - ``rgx_compute_test``
     - Try several different compute tasks on the core
   * - ``rgx_triangle_test``
     - Render a triangle to the attached display
   * - ``rgx_twiddling_test``
     - Twiddle several textures in several different pixel formats

Future releases of ti-img-rogue-umlibs can include more tools. This is the core
set expected to be available in most ti-img-rogue-umlibs releases and are the
most useful for verifying GPU functionality.

The order of operation to verify fundamental GPU functionality is as follows:

   #. Use ``rgx_compute_test`` to verify that the GPU is able to handle a proper
      compute load.

   #. Use ``rgx_triangle_test`` to verify that the GPU is able to render to an
      output buffer.


If you are still experiencing issues after verifying fundamental functionality,
try checking the output of the following:

.. code-block:: console

   # pvrdebug -dd

.. note::

   When raising a ticket on e2e forums it is useful to include the output of
   this command if available.

This will dump all device information as reported by the kernel module. Please
ensure that the debug info reports:

.. code-block:: text

   Comparison of UM/KM components: MATCHING

User mode and kernel mode components must move in lockstep. If they do not match
this could lead to the kernel module failing to initialize or undefined
behavior.
