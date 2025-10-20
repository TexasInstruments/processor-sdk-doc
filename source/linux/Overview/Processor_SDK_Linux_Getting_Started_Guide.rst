Getting Started Here
====================

Welcome to the Linux Getting Started Guide
------------------------------------------

Thanks for your interest in learning more about the Linux Software
Development Kit (SDK). The SDK as we affectionately call it is our
attempt to provide a great starting point to develop an embedded
system on a TI Processor running Linux. Given this goal, we wanted to
provide something that is more than just a typical Board Support
Package (BSP) containing a bootloader, Linux kernel, and filesystem.
While these are certainly necessary elements, we feel they are just a
starting point, especially for those that aren’t experts in developing
with Linux. So, the SDK also contains tools for developing on TI
Processors (a validated cross-compiling toolchain, for example),
pre-built libraries that you can use without having to rebuild them
yourself, and some documentation to help explain how all of these
pieces work together. We package all of this together with a working
Linux Embedded System that has been built with all of the things
mentioned above.

What it really serves as is a “known good” starting point. One of the
big challenges with starting development on a new platform (not to
mention, a new Operating System (OS) for many), is getting an
environment set up where you can build and debug code on hardware. The
SDK attacks this problem with providing everything you need to do
development, and it is validated on standard TI hardware platforms
(EVMs) (see :ref:`here <release-specific-supported-platforms-and-versions>` for more details).
It wraps all of this up into one simple installer that helps get
everything you need in the right place to do development. For example,
you can start off with simply re-building the Linux Embedded System
that we provide to validate that everything is working on your system.
This simple step gives you confidence that you can move forward from a
good baseline.

As you go along your development journey and have questions, there is
documentation and support available to you. Make sure to save a pointer
to the :ref:`Processor SDK Linux Software Developer's Guide <linux-index>`. If you don't find what you
need, take a look at the active `E2E Processor Support
<https://e2e.ti.com/support/processors>`__ Forum
and see if the topic has been covered before. If not, post
a new thread and we’ll do our best to provide some guidance.

|

What would you like to do with the SDK?
---------------------------------------

As described above, the SDK has a lot to it. Let’s break it down to two
pieces to simplify things a bit:

-  The example :ref:`Embedded Linux System <linux-software-stack>`.
   Essentially, a working bootloader (U-Boot), Linux
   kernel, and filesystem that can be put on an SD card and ran on a TI
   EVMs.

   .. ifconfig:: CONFIG_sdk in ('SITARA')

       It can also be used on one of the very popular Beaglebones (either the original
       “white” or the newer “black”). For K2H/K2K, K2E, and K2L platforms
       which are not using SD cards, U-Boot is loaded to NOR, Linux kernel
       is fetched from TFTP server, and filesystem is on NFS.

-  Everything needed to create the above embedded system from “scratch”:

   -  U-Boot sources and configuration files
   -  Kernel sources and configuration files

   .. ifconfig:: CONFIG_sdk in ('JACINTO','j7_foundational')

       -  Hypervisor sources and configuration files

   -  An ARM cross-compiling toolchain as well as other host binaries
      and components

   .. ifconfig:: CONFIG_sdk in ('SITARA')

       -  RTOS application sources and configuration files
       -  A Yocto/OE compliant filesystem

   .. ifconfig:: CONFIG_sdk in ('JACINTO','j7_foundational')

       -  A Yocto/OE compliant filesystem and sources for example
          applications

   -  A variety of scripts and Makefiles to automate certain tasks
   -  Other components needed to build an embedded Linux system that
      don’t fit neatly into one of the above buckets

With these two pieces more clearly defined, we can now get back to that
all important question, "What would you like to do with the SDK?". If
the answer is clearly "I want to build something and I'm ready to start
developing now!", then go ahead and skip down to the "I want to
Develop!" (or, `Developing with the Linux SDK <Processor_SDK_Linux_Getting_Started_Guide.html#start-your-linux-development>`__
section below for instructions on installing the SDK on a Linux Host
System. This is a somewhat involved process focusing on the second of
the two parts of the SDK listed above and may be more than some people
want to start with. However, it provides access to the full spectrum of
development from rebuilding the SDK from sources to fully adapting it
with new device drivers and applications.

.. ifconfig:: CONFIG_sdk in ('SITARA')

    .. note::
       For K2H/K2K, K2E, and K2L platforms which are not using SD cards, please
       also go ahead and skip down to the “I want to Develop!” (or, `Developing
       with the Linux SDK <Processor_SDK_Linux_Getting_Started_Guide.html#start-your-linux-development>`__ section.

So, if you’re not quite there yet, let’s discuss some other options.
Maybe you’d like to evaluate the SDK a bit to see if it is how you’d
like to get started.

If this is not good enough and you really want to get your hands on something,
check out the next section which shares how to play with the embedded Linux
system, the first piece of the SDK mentioned earlier. All you’ll need is access
to a Linux computer, a SD card, a SD card reader, some free, open-source
software, and a supported :ref:`Hardware Platform
<release-specific-supported-platforms-and-versions>`.

 .. rubric:: Evaluating the SDK Embedded Linux System
    :name: evaluating-the-sdk-embedded-linux-system

If you’re a hands on person, reading documentation and looking at
presentations gets old fast. So, if you want to see an example of what
you can build with the SDK and actually hold it in your hands and play
with it (or show it to someone else that needs help understanding what
you want to do with it), with minimal effort, you can simply run the
SDK Embedded Linux System on a supported :ref:`Hardware platform
<release-specific-supported-platforms-and-versions>`.
This will allow you to poke and prod and interact. It’s a powerful way
to get the imagination active and engaged.

.. ifconfig:: CONFIG_sdk in ('SITARA')

    If you’ve recently purchased a TI EVM or Starterkit, it should have came
    with a SD card with the SDK on it. If that is the case, simply plug the
    card in, boot it up, and let your imagination run wild. However, if
    you’re like us and the boards you are given never have all of the stuff
    they came with, or if you purchased a
    `Beaglebone <http://beagleboard.org/Products/BeagleBone>`__ or
    `Beaglebone
    Black <http://beagleboard.org/Products/BeagleBone%20Black>`__, you might
    not have a SD card with the SDK on it. Or, maybe, the SDK on your SD
    card is simply a few revisions old and you want the latest and greatest.
    If that is the case, check out the :ref:`Create SD Card <processor-sdk-linux-create-sd-card>`
    page. Just remember, you won’t be able to build or change anything,
    simply evaluate the SDK Embedded Linux System as delivered.
    But, even this is enough to get the imagination going and all some folks
    want to do.

    .. note::
       The above is not applicable to K2H/K2K, K2E, and K2L platforms, which
       are not using SD card.

.. rubric:: Start your Linux Development
   :name: start-your-linux-development

OK, you’re all in. Either you’ve known this is what you wanted to do, or
you’ve gone through the above steps and you want to do more. It’s time
to develop! Here’s a high level overview:

-  Get a Linux host up and running if you don’t already have one
-  Install the SDK and run some scripts to get everything set up
-  Put the SDK Embedded Linux System on a SD card or TFTP/NFS to play
   with
-  Build something to validate set up – the SDK for example
-  Add something to the SDK, like a simple Hello World app

After completing these steps, you’ll have a known good baseline from
which you can start development.

#. **Configure a Linux Host**

   If you already have a Linux host machine, go to Step 2.

   To do Linux development with the SDK, you’ll need a host PC running
   Linux. The Linux host is generally much faster and has a lot more
   memory (both RAM and hard disk space) than the typical embedded
   system. While it is certainly possible to do all development
   natively, we feel the advantages of using a host provide a better way
   to go and what is supported out of the box with the SDK.

   There are many, many ways to get access to a Linux host. We simply
   can’t validate all possibilities and iterations, therefore we focus
   on validating using `Ubuntu <http://www.ubuntu.com/>`__ as the host
   Linux distribution, running natively. We validate the Long-term
   Support (LTS) versions of Ubuntu at the time of a SDK release.

   .. ifconfig:: CONFIG_sdk in ('SITARA')

       For example, at the time of this writing, Ubuntu |__LINUX_UBUNTU_VERSION_SHORT__|
       is the currently supported LTS version).

   Can you use other versions of Ubuntu or even other distributions?
   Theoretically, yes, as long as you can get it to work and there may
   be more “assembly” required. If you can use the Ubuntu version
   validated against the SDK, it will be the smoothest path and we will
   be able to help you more if you do run into trouble.

   Likewise, we would strongly recommend getting a **native 64-bit**
   Ubuntu LTS machine set up for development. For the cost of a little
   bit of hard drive space, Ubuntu can have direct access to the host’s
   hardware. Virtual Machines (VMs) have come a long way over the years,
   and many people use them daily without problems. However, when you
   are working with a target embedded system (that may be a prototype
   board), whether it be a TI board or eventually your own, removing the
   complexity of a VM from the get go can avoid a lot of frustration
   (i.e. wasted time). When using a VM while connecting and
   disconnecting hardware components, you have to be very diligent about
   making sure what is connected to what. You might prefer using an hour
   to get more work done than debugging a perceived problem caused by
   the fact the virtual host grabbed a USB port when you weren’t
   watching.

   When you’re ready to proceed,
   `Ubuntu <http://www.ubuntu.com/download/desktop/install-desktop-long-term-support>`__
   provides a great overview for how to install natively.


#. **Install the SDK**

   Within your Linux host machine, `Install the Linux SDK <Download_and_Install_the_SDK.html>`__.

   .. note::
      Processor SDK Installer is 64-bit, and installs only on 64-bit host
      machine. Support for 32-bit host is dropped as the cross-compile toolchain is
      available only for 64-bit machines.

   .. note::
      At least 20 GB of free space is required on the host machine for
      installing the |__SDK_FULL_NAME__| package.

#. **Create a SD Card**

   .. ifconfig:: CONFIG_sdk in ('SITARA')

       Use the :doc:`Create SD Card <Processor_SDK_Linux_create_SD_card>`,
       or **One-time Program EVM for K2H/K2K, K2E, and K2L** - following directions for :doc:`Program EVM User Guide <Program_EVM>`

   .. ifconfig:: CONFIG_sdk in ('JACINTO','j7_foundational')

       Use the mksdboot.sh script from the installer.

       .. ifconfig:: CONFIG_part_variant in ('AM65X')

         .. note::
            By default, the mksdboot.sh copies the PG2.0 sysfw to the SD card. To
            use the PG1.0 sysfw, copy the board-support/prebuilt-images/sysfw-am65x-evm.itb
            file to /media/$USER/boot/sysfw.itb.

   .. note::
      You will need a >8GB SD Card and the capability to connect that card
      to your Linux Host machine (using a USB SD Card reader, for example).

   .. note::
      If using a virtual machine as your Linux host, you may need to import
      the SD Card reader into your virtual machine (disconnect it from the
      host and connect it to the VM so that the Linux VM can see it).

   .. ifconfig:: CONFIG_sdk in ('SITARA')

       .. note::
          For K2H/K2K, K2E, and K2L platforms which are not using SD card,
          one-time EVM programming is needed if u-boot has not been loaded
          before or the previous u-boot is somehow corrupted. Please see
          details at `Program EVM User Guide <Program_EVM.html>`__.

#. **Configure your development environment**

   There are many ways to connect the host development platform and the
   target board. These connections will vary depending on how you like
   to develop and what you are trying to do. Here is an example of a
   common set up with a serial connection for console and ethernet for
   networking (TFTP, NFS, etc.):

   .. note::
      The recommended setup is to use TFTP for booting the kernel and NFS
      for hosting the target root filesystem. Since the SDK provides full
      cross-compile development environment for the x86 host, this
      configuration will simplify the transfer of files to and from the
      target platform.

   .. ifconfig:: CONFIG_sdk in ('SITARA')

       .. Image:: /images/AM335x_Development_Environment.png

#. **Use the SD Card to boot the target board** properly connected for
   your development environment.

   .. ifconfig:: CONFIG_sdk in ('SITARA')

       .. note::
          This is not applicable to K2H/K2K, K2E, and K2L platforms. For those
          platforms, power up the EVM and stop at the U-boot prompt as
          described in `Program EVM User Guide <Program_EVM.html>`__

#. **Run the Setup Script**

   Once the SDK has been installed, `Run the setup.sh Script <Run_Setup_Scripts.html>`__
   on your host to guide you through the remaining development
   environment configuration.

   .. note::
       If using a virtual machine as your Linux host, you will likely need
       to import the target board into the virtual machine as a mass storage
       device.


#. **Rebuild sources**

   Use the `top-level Makefile <Top_Level_Makefile.html>`__
   in the SDK root directory. For example:

   -  ``make all`` rebuilds all components in the SDK
   -  ``make linux`` configures and builds the kernel
   -  ``make u-boot`` builds u-boot

   The file system can be rebuilt following the instructions at :ref:`Building the SDK <overview-building-the-sdk>`.


   .. code-block:: bash

      cd /tmp
      wget http://ftp.gnu.org/gnu/make/make-4.1.tar.gz
      tar xvf make-4.1.tar.gz
      cd make-4.1/
      ./configure
      make
      sudo make install
      cd ..
      rm -rf make-4.1.tar.gz make-4.1

|

What Would You Like to do Next?
-------------------------------

Now that you have a solid baseline set up, you can choose what you'd
like to do next based on what you need to do. Here are some of the many
possibilities:

.. ifconfig:: CONFIG_sdk in ('SITARA')

    +--------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
    |  **Link**                                                                                                          | **Summary**                                                                                                        |
    +--------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
    |`AM335X <http://www.ti.com/tool/PROCESSOR-SDK-AM335X>`__, `AM437X <http://www.ti.com/tool/PROCESSOR-SDK-AM437X>`__, |Download the SDK                                                                                                    |
    |`AM57X <http://www.ti.com/tool/PROCESSOR-SDK-AM57X>`__, `66AK2Ex <http://www.ti.com/tool/PROCESSOR-SDK-K2E>`__,     |                                                                                                                    |
    |`66AK2Gx <http://www.ti.com/tool/PROCESSOR-SDK-K2G>`__, `66AK2Hx <http://www.ti.com/tool/PROCESSOR-SDK-K2H>`__,     |                                                                                                                    |
    |`66AK2Lx <http://www.ti.com/tool/PROCESSOR-SDK-K2L>`__                                                              |                                                                                                                    |
    +--------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
    |:ref:`Processor SDK Linux Software Developer's Guide <linux-index>`                                                 |The SDK's Homepage, a must have link for SDK users.                                                                 |
    +--------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
    |`Processor SDK Training Series <http://training.ti.com/processor-sdk-training-series>`__                            |This series provides an introduction to the Processor SDK and how to use this software to start building            |
    |                                                                                                                    |applications on TI embedded processors.                                                                             |
    +--------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
    |`Processor SDK Linux Training: Hands on with the Linux SDK                                                          |The next step in learning about the Processor SDK Linux. This lab walks through how to use the SDK and              |
    |<http://processors.wiki.ti.com/index.php/Processor_SDK_Linux_Training:_Hands_on_with_the_Linux_SDK>`__              |Code Composer Studio with examples applications.                                                                    |
    +--------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
    |`Debugging Embedded Linux Systems Training Series                                                                   |This series teaches the techniques of debugging kernel issues that may be encountered in embedded Linux systems.    |
    |<https://training.ti.com/debugging-embedded-linux-systems-training-series>`__                                       |It explains the Linux kernel logging system and logging API, illustrates how to locate a particular device driver,  |
    |                                                                                                                    |and demonstrates how to read kernel oops logs.                                                                      |
    +--------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
    |`Processor SDK Linux How-To Guides <../How_to_Guides.html>`__                                                       |The SDK How-To pages. The Hands On with the SDK has some great information for developing your first                |
    |                                                                                                                    |Linux application.                                                                                                  |
    +--------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
    |`Processor SDK Linux Kernel <../Foundational_Components_Kernel.html>`__                                             |More information on the Linux Kernel provided with the SDK (how to build it, for example).                          |
    +--------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
    |`Processor SDK Linux U-Boot <../Foundational_Components_U-Boot.html>`__                                             |Everything you want to know about U-Boot, the bootloader provided with the SDK.                                     |
    +--------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
    |`Processor SDK Linux Filesystem <../Foundational_Components_Filesystem.html>`__                                     |Details about the various Filesystems delivered with the SDK, and their contents.                                   |
    +--------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
    |`Processor SDK Linux Tools <../Foundational_Components_Tools.html>`__                                               |Documentation for all of the various tools included with the SDK.                                                   |
    +--------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+

.. ifconfig:: CONFIG_sdk in ('JACINTO','j7_foundational')

    .. Note::
        Some of the training content below has been written for DRA80x devices.
        Work towards making these trainings tailored for Jacinto devices is in progress.
        Not all the trainings will be applicable for Jacinto devices.

    +--------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
    |  **Link**                                                                                                          | **Summary**                                                                                                        |
    +--------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
    |:ref:`Processor SDK Linux Software Developer's Guide <linux-index>`                                                 |The SDK's Homepage, a must have link for SDK users.                                                                 |
    +--------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
    |`Processor SDK Training Series <http://training.ti.com/processor-sdk-training-series>`__                            |This series provides an introduction to the Processor SDK and how to use this software to start building            |
    |                                                                                                                    |applications on TI embedded processors.                                                                             |
    +--------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
    |`Processor SDK Linux Training: Hands on with the Linux SDK                                                          |The next step in learning about the Processor SDK Linux. This lab walks through how to use the SDK and              |
    |<http://processors.wiki.ti.com/index.php/Processor_SDK_Linux_Training:_Hands_on_with_the_Linux_SDK>`__              |Code Composer Studio with examples applications.                                                                    |
    +--------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
    |`Debugging Embedded Linux Systems Training Series                                                                   |This series teaches the techniques of debugging kernel issues that may be encountered in embedded Linux systems.    |
    |<https://training.ti.com/debugging-embedded-linux-systems-training-series>`__                                       |It explains the Linux kernel logging system and logging API, illustrates how to locate a particular device driver,  |
    |                                                                                                                    |and demonstrates how to read kernel oops logs.                                                                      |
    +--------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
    |`Processor SDK Linux How-To Guides <../How_to_Guides.html>`__                                                       |The SDK How-To pages. The Hands On with the SDK has some great information for developing your first                |
    |                                                                                                                    |Linux application.                                                                                                  |
    +--------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
