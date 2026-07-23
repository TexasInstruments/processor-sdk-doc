Real-Time Linux on TI SoCs
==========================

The Real-Time Linux kernel is a great way to control the maximum context
switch latency of a system to achieve predictable response times in your
embedded application without resorting to bare metal code or RTOS
kernels.

Though Linux will never be a formally proven RTOS, the hardware support,
frameworks, and libraries built for Linux can all run on a real-time
Linux kernel which increases development speed for any application that
has some type of deadline to meet.

In this section we will walk through the process of measuring the
performance, and some tips on how to tune the kernel for your specific
workload to get the best performance out of your system.

What Is The Real-Time Linux Kernel?
-----------------------------------

The Real-Time Linux kernel is a set of patches, sometimes called the
PREEMPT_RT or RT patch, which are in the final stages of being accepted
into the mainline Linux kernel.

These patches introduce or modify existing core systems in the kernel to
maximize the time our CPUs can be interrupted by the scheduler and
introduce a level determinism to the Linux kernel to control the maximum
latency the system will experience when switching contexts.

It's important to note these patches do not focus on the minimum
interrupt latency and can sometimes even increase it in certain
situations.

As of this writing updates to the ``printk()`` system is the last
remaining major effort to be merged. You can see the latest news about
this effort here: https://wiki.linuxfoundation.org/realtime/

Validating We Are Using A Real-Time Capable Kernel
--------------------------------------------------

Because of the length of time the real-time patchset has been working
its way into the mainline Linux kernel some of its features are already
in use with vanilla kernel builds. This can make it difficult to
determine if the kernel is fully real-time capable.

One easy way to determine if the kernel currently running is real-time
capable is by looking if the realtime file exists in our :file:`/sys`
directory

.. code:: console

   cat /sys/kernel/realtime

If the file is not found then the current kernel does not have all the
required features needed by the kernel to be fully preemptible and is
not suited for running a real-time application.

Testing Kernel Performance
--------------------------

There are many ways to test or evaluate the performance of your
application with the Real-Time Kernel and some of them will be more
relevant than others depending on the nature of your application.
However as we'll explain later it is typically best to test using your
application and using stressing tools to examine its behavior under
different circumstances.

Timer Based Applications
^^^^^^^^^^^^^^^^^^^^^^^^
Say for example you need to take a measurement from a sensor every 100us
for quality assurance. So our application will wake a task up every
100us to take this measurement before sending it out to the main
controller. This being a timer based task, we will need to ensure the
kernel has a periodic interrupt generated fast enough to ensure the
kernel can switch to our task to take a sample at our 100us deadline.

To simulate this type of workload we can generate various background
loads that our application may experience using a tool like stress-ng.

.. code:: console

   stress-ng –cpu-method=all -c20 &

Then we can monitor our application's performance or use another tool
like cyclictest_ to measure the context switch latency the CPUs are
experiencing.

.. _cyclictest: https://wiki.linuxfoundation.org/realtime/documentation/howto/tools/cyclictest/start

Cyclictest_ is a simple program maintained by the real-time kernel
developers to detect any anomolies or latency spikes when developing the
next version of the Linux kernel. There are quite a few options we can
set however for this example we will run cyclictest on all CPU cores
with a priority of 80 for 5 hours.

.. code:: console 

   cyclictest -m -Sp80 -D5h -h400 -i200 -M
   ...
   # Total: 108000000 107999945 107999881 107999811
   # Min Latencies: 00003 00004 00003 00003
   # Avg Latencies: 00005 00005 00005 00005
   # Max Latencies: 00029 00033 00034 00037

Here we can see each CPU took on average 5us however they took a maximum
of 29us, 33us, 34us and 37us to switch from the background stress-ng
tasks to the cyclictest task which was measuring the context switch.
Though this may be of little relevance if your application is doing more
than only consuming CPU cycles.

Depending on the usecase it may be more suitable to run different or
more stressing algorithms than just a CPU stressing function for example
a function to stress the memory-management system. More information and
a complete list about these functions in stress-ng can be found in the
source code of this project located here:
https://github.com/ColinIanKing/stress-ng

Driver (Ethernet) Based Interrupts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As we will see a little later, a lot of work has gone into servicing IO
or hard interrupts by our CPUs in the real-time kernel. And while a
large portion of these interrupt handlers have been offloaded to
threaded interrupts which can be put to sleep, these smaller hard
interrupts are not completely transparent and continue to degrade
performance.

One good way to demonstrate this is by using the iperf3 tool to generate
large amounts of ethernet traffic.

On a host machine connected to our embedded device we can run the
following command to create a server to listen for incoming network
traffic

.. code:: console 

   iperf3 -s

Next, on our embedded device, we can issue the command to send ethernet
traffic back and forth to the server to generate large amounts of hard
interrupts for our CPUs to service the incoming packets

.. code:: console 

   iperf3 -c 10.10.10.1 -p 7575 -bidir

With this going on in the background, we can begin monitoring our
application or using cyclictest again to show that the maximum latencies
have increased and depending on your use case may even exceed our
requirements for our application.

So how can we tune the kernel to achieve the maximum performance from
our embedded system to ensure we stay below our requirements?

Tips For Tuning The Real-Time Kernel
------------------------------------

Be warned, tuning the Real-Time Linux kernel is an extremely iterative
task. There are thousands of knobs and settings we can tweak (too many
for us to list here) and any one of them can have large impacts on the
overall performance of the system. Be prepared to spend many days or
weeks at this.

Technique to Tuning (Slow is Fast)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is very tempting to make large changes to our system before we start
another round of tests, however once improvements are found, it is
extremely difficult to narrow down which change actually made the
improvements. Keep your changes small and run many tests to slowly
approach your tuning goals.

Technique to Testing
^^^^^^^^^^^^^^^^^^^^

We also suggest running long tests that stretch into hours or days. Many
of these settings could introduce unusual edge-cases of high latency or
strain a resource in the SoC beyond what is acceptable for your
application that will only be visible after many hours of testing.


It's usually a good idea to embed and use monitoring mechanisms inside
your application to gauge the effects of our tuning efforts. Not only
will this give us concrete evidence our tuning efforts are working,
simulating our application with stress-ng or any other application could
be missing key parts that test the system and lead us down a false path.

Disable Unnecessary Applications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Many distributions like Debian, or Yocto will come with many
applications enabled and running by default as a convenience. This can
put strain on our system that the kernel will not be able to overcome.
For example we do not need Wayland running on a system without a screen.
Disabling our GUI will free main memory bandwidth allowing our
application to make fetches into DDR faster and improve the time it
takes our CPUs to context switch.

Disable Unnecessary Drivers
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The real-time kernel developers have done a lot to limit the effects
interrupts have on CPUs running real-time tasks by creating a worker
thread to process the interrupt and allowing the CPU to exit from its
interrupt context as quickly as possible to return to executing our
real-time application. Even with this work the CPU will still require a
non-zero amount of time to return from the interrupt context.

The drivers for unused and unneeded peripherals like remote cores, I2C
controllers, MMC, VPUs, Ethernet controllers, DSPs, and USB devices like
mice and keyboards can all generate interrupts that take time away from
the CPU running our application needlessly. Disabling the devices in
our DTB prevents the kernel from loading the corresponding drivers at
all and limits the number of interrupts our CPUs must service.

Wrapping Up
-----------

While these tips only scratch the surface of what the real time kernel
is and how we can achieve the best performance out of it, there is quite
a lot of documentation available to help you get started with the
real-time patchset. For now all I can say is good luck.


