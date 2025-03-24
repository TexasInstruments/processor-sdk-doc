
How to Configure the CMA Size
=============================

Contiguous Memory allocation (CMA) is commonly used by memory-to-memory (M2M) devices that do not have
have MMU support. By default in Linux, the CMA size will be 32 MB. For the common TI board, this is far
too small. There are a handful of components that need to use CMA in order for proper operation as well as
achieving optimal performance. These components include, but are not limited to, the multimedia Codecs, CSI,
and TIDSS. TI has already increased the amount of CMA that comes in |__SDK_FULL_NAME__|. The amount that has
been allocated can be checked by running the following command on target:

.. code-block:: console

   target$ cat /proc/meminfo | grep Cma

After executing, an output similar to the one below will be seen.

.. code-block:: console

   CmaTotal:         589824 kB
   CmaFree:          583984 kB

These logs can be used to obtain the amount of CMA that has been allocated and how much of that is still available
for use. Depending on the particular use case, it may be of interest to decrease the size of this allocation pool.
To do so, locate the device tree (.dts) file that contains the main domain for the target board. For example, if
using the AM62PX SoC, open up :file:`arch/arm64/boot/dts/ti/k3-am62p5-sk.dts`. These device tree files contain a
node for reserved memory. A portion of this reserved memory area is for CMA, therefore the area has been named
`linux,cma`. This node contains an attribute called size; changing the value of this attribute cause the CMA region
to grow or shrink. Once attribute is changed to desired value, save and close the dts file so it can be compiled into
proper device tree blob (.dtb). Update the target with new .dtb file and check that new CMA region matches the size
set in the device tree.

CMA allocation can also be changed without re-compilation of device tree. One can stop at u-boot prompt during boot
and update the CMA parameter as shown below:

.. code-block:: console

   target # setenv args_all $args_all cma=1000M
   target # boot

.. note::

   Allocating at u-boot tends to place the CMA in the lower 32 bit region of memory. Many of the common components have been
   ported to operate in the higher 48 bit region of memory. It is recommended to take the approach with changing device tree,
   but this method is fine for quick validation.
