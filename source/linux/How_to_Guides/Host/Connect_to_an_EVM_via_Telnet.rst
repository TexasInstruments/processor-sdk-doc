.. http://processors.wiki.ti.com/index.php/GSG:_OMAP35x_DVEVM_Additional_Procedures#Using_Telnet

Connect to an EVM via Telnet
==================================================================

.. rubric:: Using Telnet
   :name: using-telnet

The initialization file (/etc/init.d/rcS) starts a telnet server. If
your development host is in the same sub-net as the EVM, you can telnet
to it using the IP address assigned in the U-boot environment.  The
following is an example from a Linux host.

::

    $ telnet 192.168.1.10

You will be prompted for a user name and password. The user name should
be root and the password should be left blank (just hit Enter).

|

From a Windows XP host, click the Start button, then click Run... Type
telnet and click OK. This will open a telnet window.

Type "o < ip-addr >" and hit enter.  Example:

::

    Microsoft Telnet> o 128.247.107.12

Type root for the password and leave the password blank (just hit Enter)

