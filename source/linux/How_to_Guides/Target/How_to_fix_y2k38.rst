##########################
How to prevent Y2K38 issue
##########################

************************
What is the Y2K38 issue?
************************

The Y2K38 issue is a time computing problem that prevents 32-bit systems from representing
dates beyond 03:14:07 UTC on January 19, 2038. On 32-bit platforms, the UNIX time is stored
as a signed 32-bit integer (``time_t``) counting seconds since the UNIX epoch
(00:00:00 UTC on January 1, 1970). This integer overflows at 2,147,483,647 (0x7FFFFFFF),
wrapping to a large negative value and causing the system to interpret the time as a date in 1901.

For more information, see: https://en.wikipedia.org/wiki/Year_2038_problem

The fix requires updates at every layer of the software stack: kernel, C library (glibc),
and all userspace applications. If any component lacks Y2K38 support, the entire
system is vulnerable.

********************
Y2K38 issue resolved
********************

**The current SDK release uses the Scarthgap filesystem, which has the Y2K38 issue resolved.**

TI's 32-bit platforms (AM335x, AM437x) now use OE-core Scarthgap, which includes all
necessary fixes applied at every software layer. The filesystem images provided in this SDK
are Y2K38-compliant by default.

How Yocto/OpenEmbedded ensures Y2K38 compliance
===============================================

Starting with Yocto Nanbield 4.3 (eventually in Scarthgap 5.0), OE-core builds all packages with
the following compile-time defines enabled globally:

.. code-block:: c

   #define _TIME_BITS 64
   #define _FILE_OFFSET_BITS 64

``_TIME_BITS=64`` instructs glibc to use a 64-bit ``time_t`` on 32-bit platforms, making
all time-related types and functions (``struct timespec``, ``struct timeval``, ``time()``,
``clock_gettime()``, etc.) Y2K38-safe. ``_FILE_OFFSET_BITS=64`` enables large file support
(files >2 GB). Yocto enables both flags together to ensure a consistent 64-bit ABI across
the system.

Since all packages in the distribution are rebuilt with these defines, the entire filesystem
is consistently Y2K38-safe.

This approach requires:

- **glibc 2.34 or later**: introduces support for ``_TIME_BITS=64`` on 32-bit architectures
- **Linux kernel 5.6 or later**: completes full 64-bit time syscall support
  (``clock_gettime64``, ``clock_settime64``, etc.) required by glibc on 32-bit systems

The Scarthgap filesystem satisfies both requirements (includes glibc 2.39 and kernel 6.6).

Ensuring your code is Y2K38-friendly
====================================

While the SDK images are Y2K38-friendly, any code introduced from external sources must also be
Y2K38-compliant. Code that is not Y2K38-compliant will break the Y2K38-compatibility of the filesystem.

When building applications or libraries to run on the SDK filesystem, ensure the following compile-time
defines are set:

.. code-block:: c

   #define _TIME_BITS 64
   #define _FILE_OFFSET_BITS 64

Or equivalently, pass these flags to the compiler:

.. code-block:: console

   $ CFLAGS="-D_TIME_BITS=64 -D_FILE_OFFSET_BITS=64" make

With ``_TIME_BITS=64`` set, standard time functions (``time()``, ``clock_gettime()``,
``localtime()``, etc.) automatically use 64-bit time internally (no API changes are
required). However, audit your code for:

- ``time_t`` casts or assignments that assume a 32-bit (4-byte) size
- Hard-coded UNIX timestamps or future dates as raw integer constants
- Use of ``sizeof(time_t)`` in serialization/protocol code

******************************
How to verify Y2K38 compliance
******************************

.. warning::

   Set the date back to the correct value after testing. Running with an incorrect system clock
   can disrupt services such as NTP, certificate validation, and cron jobs.

Check ``sizeof(time_t)``
========================

The quickest way to verify a binary is Y2K38-safe is to check the size of ``time_t`` at
compile time or runtime:

.. code-block:: c

   #include <stdio.h>
   #include <time.h>
   int main(void) {
       printf("sizeof(time_t): %zu\n", sizeof(time_t));
       return 0;
   }

- Compiled **without** ``_TIME_BITS=64``: ``sizeof(time_t)`` = 4 (32-bit, **not Y2K38-safe**)
- Compiled **with** ``_TIME_BITS=64``: ``sizeof(time_t)`` = 8 (64-bit, **Y2K38-safe**)

Test with a post-2038 date
==========================

You can also test whether your system handles dates beyond 2038 correctly by temporarily
setting the system clock past January 19, 2038.

**Test procedure:**

#. Save the current date:

   .. code-block:: console

      $ date
      Tue Jan 19 03:00:00 UTC 2038

#. Set the clock past the Y2K38 boundary:

   .. code-block:: console

      $ date -s "2038-01-20 00:00:00"

#. Verify the system handles the date correctly:

   .. code-block:: console

      $ date
      Wed Jan 20 00:00:00 UTC 2038
      $ date +%s
      2147558400

   On a Y2K38-safe system, ``date +%s`` returns a value greater than ``2147483647``
   (0x7FFFFFFF) without overflow or sign error.

#. Restore the correct date:

   .. code-block:: console

      $ date -s "<correct-date>"

**On a non-Y2K38-safe system**, setting the date past the boundary may cause:

- ``date`` to report a date in 1901 (signed overflow wraps to negative epoch)
- System services to crash or behave unexpectedly
- ``date +%s`` to return a small or negative value
