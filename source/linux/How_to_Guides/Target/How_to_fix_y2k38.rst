######################
How to Fix Y2K38 Issue
######################

************************
What is the Y2K38 Issue?
************************

The Y2K38 issue is a bug which prevents a date from exceeding 03:14:07 UTC on January 19, 2038, on 32-bit systems. This
is because the structures used to store the date experience an integer overflow when the date is set beyond the mentioned
one. This causes the system to crash.

For more information, see: https://en.wikipedia.org/wiki/Year_2038_problem

There are new data structures that are used on 32-bit systems to store date/time in longer fields, thereby avoiding the
overflow and the crash. However, since setting and displaying date/time uses multiple software components (such as the
kernel, glibc etc), **all** code on a filesystem must be Y2K38-compliant (i.e. all code must be using the new data
structures and functions) for the filesystem to be Y2K38-friendly. If any piece of software uses the older structures
and functions, it makes the whole filesystem vulnerable.

To understand how the problem was fixed in Scarthgap filesystem, refer:
https://static.sched.com/hosted_files/osseu2024/8b/EOSS%20Vienna%202024%20-%20Surviving%20Y2038.pdf

*******************************
Building a Y2K38-friendly Image
*******************************

In SDK 9.3, TI's 32-bit platforms are still based on Kirkstone filesystem, which is NOT Y2K38-friendly. The Y2K38 issue
is fixed in OE-core Scarthgap, on which the next release will be based.

Until then, if a Y2K38-friendly filesystem is required, obtain a :file:`tisdk-thinlinux-image` from the latest
`cicd.scarthgap.x`:

.. ifconfig:: CONFIG_part_variant in ('AM335X')

   https://software-dl.ti.com/cicd-report/linux/index.html?section=platform&platform=am335x

.. ifconfig:: CONFIG_part_variant in ('AM437X')

   https://software-dl.ti.com/cicd-report/linux/index.html?section=platform&platform=am437x

The above images are based on the 6.6 Kernel and Scarthgap filesystem, and thus has the Y2K38 issue fixed.

.. note::
   While the above images are Y2K38-friendly, it must be ensured that even the code introduced to it from other sources
   is Y2K38-friendly. Any code that is not Y2K38-friendly will break the Y2K38-compatibility of the filesystem. Thus it
   is important to be intentional about writing Y2K38-friendly code, and to test this code to ensure that the final
   image remains Y2K38-friendly.

To build a Y2K38-friendly image on the 6.6 Kernel and Scarthgap filesystem baseline, follow the "Build Instructions"
section present in the above link.
