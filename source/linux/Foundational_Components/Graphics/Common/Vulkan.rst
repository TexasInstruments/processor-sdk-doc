.. include:: <isonum.txt>

######
Vulkan
######

The Vulkan\ |reg| libraries are packaged with the |__SDK_FULL_NAME__| and can be
used by graphics stacks such as Qt and GTK. The drivers run on an ARM core and
programs the firmware running inside a GPU core with rendering commands
submitted by the user applications.

Vulkan\ |reg| is a relatively new API that focuses on increased verbosity and
control over the device as opposed to OpenGL\ |reg| ES, which was initially
intended to abstract common processing functions for developers. As a result, it
can be written by hand but it is usually advised to use an existing abstraction
framework, such as the previously mentioned GTK or Qt widget based framework.

Like OpenCL\ |trade|, Vulkan\ |reg| has an Installable Client Driver (ICD)
Loader to allow applications to query and pick the device it deems necessary
instead of relying on a predefined mapping between a chosen display and backing
vendor acceleration implementation. This means that typically an application
that wants to use Vulkan\ |reg| should link against an ICD loader library
instead of directly using a vendor specific library.

A useful tool for debugging Vulkan\ |reg| ICD Loaders and devices is
:command:`vulkaninfo`. This command, when run without any arguments will present
a list of all supported devices, associated parameters, and supported
extensions.

For more information about Vulkan\ |reg| extensions see:

   - `<https://docs.imgtec.com/starter-guides/vulkan-hello-api-guide/html/topics/introduction.html>`_
   - `<https://registry.khronos.org/vulkan/>`_

