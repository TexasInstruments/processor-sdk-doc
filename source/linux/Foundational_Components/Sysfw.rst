***************
System Firmware
***************

System Firmware is a collective term used to describe the TI Foundational
Security (TIFS) and Resource Management (RM)/ Power Management (PM) services.
System Firmware executes on the Security Manager and Device Manager Core (DMSC)
on |__PART_FAMILY_NAME__|.

System Firmware provides foundational security management and centralized
device management.

The responsibilities of TIFS are:

* Responsible for Centralized Foundational Security Management. These include
  functions like authenticated boot, JTAG unlock etc.
* Behaves like a forwarding agent for Resource Management and Power Management
  requests made by Secure hosts (other CPUs) in the SoC.
* Behaves as a forwarding agent for Resource Management and Power Management
  responses from the device manager to the Secure Hosts.
* Firewall Management for resources requested by both secure and non-secure
  hosts.

The responsibilities of Device Manager are:

* Servicing resource management and power management messages from secure and
  non-secure hosts.
* Forwarding non-secure host requests to set the processor boot control or
  firewall configuration for safety applications to the DMSC.
* Forwarding response received from the DMSC to non-secure hosts for the above
  forwarded messages.

Please refer to `TISCI User Guide <https://software-dl.ti.com/tisci/esd/11_01_02/index.html>`__
for details.
