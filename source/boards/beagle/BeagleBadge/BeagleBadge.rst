###########
BeagleBadge
###########

The BeagleBadge is a compact development platform from `BeagleBoard <https://www.beagleboard.org/>`__ powered
by the `TI AM62L SoC <https://www.ti.com/product/AM62L/>`__. Designed for portable and low-power applications,
it features a built-in CC33xx chip supporting WI-FI and Bluetooth applications, multiple low power modes, and
an integrated fuel gauge for battery power monitoring. The board provides a rich interface including an e-paper
connector, DSI connector, Grove expansion, seven-segment displays, and an RGB LED. Fully supported in TI sources,
the BeagleBadge offers flexible boot options (OSPI, UART, SD, USB-DFU). It supports Zephyr or Linux (with Armbian
or Arago distributions), making it an ideal open source solution for modern IoT and HMI projects.

.. list-table:: Supported Distributions
   :header-rows: 1
   :widths: 15, 15

   * - Component
     - Branch
   * - Armbian
     - `2025.12-beaglebadge <https://github.com/TexasInstruments/armbian-build/tree/2025.12-beaglebadge>`__
   * - Arago
     - `Scarthgap <https://github.com/TexasInstruments/meta-tisdk/tree/scarthgap>`__

.. toctree::

   linux/Getting_Started

For more information see
`<https://docs.beagle.cc/boards/beaglebadge/index.html>`__.
