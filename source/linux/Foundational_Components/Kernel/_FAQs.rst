.. http://processors.wiki.ti.com/index.php/Processor_Linux_SDK_kernel_FAQs

**Q: How to let Linux not load kernel modules automatically during system
boot time?**

**A:** Add the module name into the modprobe blacklist in file  */etc/modprobe.d/modprobe.conf*. For example,

::

    # cat /etc/modprobe.d/modprobe.conf
    blacklist musb_am335x

|

**Q: How to disable a peripheral then enable it again?**

**A:** Use its driver's bind/unbind sysfs entries. For example, to disable rtc on AM57x,

::

    root@dra7xx-evm:~# find /sys -name unbind | grep rtc
    /sys/bus/platform/drivers/omap_rtc/unbind
    root@dra7xx-evm:~# cd /sys/bus/platform/drivers/omap_rtc/
    root@dra7xx-evm:/sys/bus/platform/drivers/omap_rtc# ls
    48838000.rtc  bind          module        uevent        unbind
    root@dra7xx-evm:/sys/bus/platform/drivers/omap_rtc# echo 48838000.rtc > unbind
    root@dra7xx-evm:/sys/bus/platform/drivers/omap_rtc#

to enable it again,

::

    root@dra7xx-evm:/sys/bus/platform/drivers/omap_rtc# echo 48838000.rtc > bind
    [ 7792.863975] omap_rtc 48838000.rtc: already running
    [ 7792.869822] omap_rtc 48838000.rtc: rtc core: registered 48838000.rtc as rtc1
    root@dra7xx-evm:/sys/bus/platform/drivers/omap_rtc#

