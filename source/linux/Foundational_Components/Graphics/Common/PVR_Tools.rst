.. include:: <isonum.txt>

#############
PowerVR tools
#############

The suite of PowerVR Tools exist to help enable rapid graphics application
development. They target a range of areas including asset exporting and
optimization, PC emulation, prototyping environments, online and offline
performance analysis tools and many more. See PowerVR-SDK_ for additional
details on the tools and detailed documentation.

There are several useful tools available in the Imagination PowerVR SDK that are
compatible with our devices. Two of the most useful tools available are PVRTune
and PVRCarbon, which enable profiling and tracing of Graphics (GFX) activities.

Imagination has moved to packaging the target binaries with their host
installer, so we recommend using those binaries directly for guaranteed
compatibility.

*******
PVRTune
*******

The PVRTune utility is a real-time GPU performance analysis tool. It captures
hardware timing data and counters that ease the identification of performance
bottlenecks. PVRPerfServer collects data that is displayed with the PVRTune
running on the PC. The target binaries reside in the host's PVRTune installation
directory under :file:`PVRPerfServer`.

For more information see Imagination's upstream documentation on PVRTune and
PVRPerfServer.

   - `<https://docs.imgtec.com/tools-manuals/pvrtune-manual/html/pvrtune-manual/topics/introduction.html>`_

*********
PVRCarbon
*********

The PVRCarbon is an OpenGL\ |reg| ES and Vulkan |reg| API recording and analysis
utility. PVRCarbon GUI provides off-line tools to inspect captured data,
identify redundant calls, highlight costly shaders and many more. This tool can
capture traces on target and then play them back on different devices by
introducing shim libraries in place of the standard offering for that API.

This requires a little bit of setup on the target though. See Imagination's
upstream target setup guide for the most recent instructions.

   - `<https://docs.imgtec.com/tools-manuals/pvrcarbon-manual/html/topics/pvrcarbon-recorder/opengl-es.html>`_

.. _PowerVR-SDK: https://www.imgtec.com/developers/powervr-sdk-tools/installers/

