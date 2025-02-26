.. include:: <isonum.txt>

######
OpenCL
######

The OpenCL\ |trade| libraries are packaged with the |__SDK_FULL_NAME__| and are
used by compute centric libraries for offloading tasks to the GPU without the
overhead of managing displays or creating a offscreen context. The drivers run
on an ARM core and programs the firmware running inside a GPU core with commands
submitted by the user applications.

OpenCL\ |trade| differs from OpenGL\ |reg| in that it makes use of a predefined
Installable Client Driver (ICD) Loader to allow applications to query and pick
the device it deems necessary instead of relying on a predefined mapping between
a chosen display and backing vendor acceleration implementation. This means that
typically an application that wants to use OpenCL\ |trade| should link against
an ICD loader library instead of directly using a specific library.

.. note::

   Tools may choose to dynamically load their respective OpenCL\ |trade| library
   at runtime using dlopen, which may fail in Yocto based environments. This is
   usually the result of a clash in philosophies between Yocto and Application
   developers over the usage of devlinks (also know in Yocto as "dev-so"s). It's
   Yocto's belief that, for the most part, applications should not attempt to
   use dev links directly and should instead open the specific version of the
   library they need. You may choose to patch the application to do this or
   create the devlink from :file:`/usr/lib/libOpenCL.so` to
   :file:`/usr/lib/libOpenCL.so.1` manually. Tools provided by Yocto will be
   patched accordingly already.

A useful tool for debugging OpenCL\ |trade| ICD Loaders and devices is
:command:`clinfo`. This command, when run without any arguments will present a
list of all supported devices, associated parameters, and supported extensions.

For more information about OpenCL\ |trade| extensions see:

   - `<https://docs.imgtec.com/performance-guides/compute-recommendations/html/topics/introduction/introduction.html>`__
   - `<https://registry.khronos.org/OpenCL/>`__
