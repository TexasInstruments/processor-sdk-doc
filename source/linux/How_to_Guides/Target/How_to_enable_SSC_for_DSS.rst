.. _how-to-enable-ssc-for-dss:

############################################################
How to enable spread spectrum clocking for display subsystem
############################################################

************
Introduction
************

Spread Spectrum Clocking (SSC) is an electromagnetic interference (EMI) reduction technique that:

- Modulates the clock frequency rather than keeping it constant
- Varies the frequency over time in a controlled way
- Spreads energy across many frequencies instead of focusing it at one frequency
- Reduces peak emissions by spreading the electromagnetic energy

This technique is common in electronic systems, especially in high-speed digital circuits. It helps meet EMI compliance without needing extra shielding or filters.

Digital clock signals have a square wave shape. Most energy focuses at the center frequency and odd harmonics. In the frequency domain, SSC reduces the peak amplitude of the digital clock signal by spreading the energy across a wider frequency range. In the time domain, SSC adds jitter to the clock signal, but the voltage amplitude remains unchanged.

The Display Subsystem (DSS) supports Spread Spectrum Clocking (SSC) for its pixel clock sources. These pixel clocks feed the DSS video ports.

This guide shows how to configure SSC for DSS pixel clocks on supported TI SoCs.

.. important::

   When you enable SSC, the instantaneous peak pixel clock frequency can exceed the nominal frequency. Ensure this peak does not exceed the maximum frequency supported by your display components. This includes external encoders and panels. When using center spread mode, calculate the highest peak frequency:

   - For center spread: Highest frequency = Nominal frequency × (1 + (Modulation depth × 1.2) / 100)
   - For down spread: Highest frequency = Nominal frequency (no overshoot)

   Example: With 100 MHz nominal frequency and 0.5% modulation depth in center spread mode:

   - Highest frequency = 100 MHz × (1 + (0.5 × 1.2) / 100) = 100.6 MHz

   The 1.2 factor accounts for the 20% overshoot on the modulation depth in center spread mode.

*************************************************
Spread spectrum clocking configuration parameters
*************************************************

The ``assigned-clock-sscs`` device tree property configures SSC and takes three parameters:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Parameter
     - Description
   * - Modulation Frequency (Hz)
     - The frequency at which the spread spectrum modulation occurs:

       - Minimum: 32,000 Hz (32 kHz)
       - Maximum: Reference clock frequency / 200
       - Typical values: 32 kHz to 120 kHz
   * - Modulation Depth
     - The amount of frequency spread as a percentage:

       - Minimum: 10 (0.1%)
       - Maximum: 310 (3.1%)
       - Adjustable in increments of 10 (0.1%)
       - Example: 50 = 0.5% spread
       - Units: 1/10,000 (for example, 50 represents 0.5%)
   * - Spread Type
     - Spread mode options:

       - 1: Center spread (frequency varies on both higher and lower frequencies than nominal)
       - 3: Down spread (frequency varies only lower than nominal)

The modulation uses a triangular waveform. The Device Manager automatically configures the hardware based on the parameters specified in the device tree.

********
Examples
********

Example 1: Basic SSC configuration (center spread)
==================================================

This example shows how to enable SSC for the DSS VP2 clock with the following parameters:

- Modulation frequency: 100 kHz
- Modulation depth: 10 (0.1%)
- Spread type: Center spread (1)

Add the following properties to the DSS node in your device tree file (for example, :file:`k3-am62p-j722s-common-main.dtsi`):

.. code-block:: dts

   &dss0 {
       assigned-clocks = <&k3_clks 186 2>;
       assigned-clock-sscs = <100000 10 1>;
   };

.. warning::

   This example uses center spread mode (1). Remember to apply the 1.2 factor for the 20% overshoot when calculating peak frequency. Use down spread mode (Example 2) if you need to avoid exceeding the nominal frequency.

Example 2: SSC with down spread mode
====================================

This example demonstrates down spread mode, which we recommend for display interfaces:

- Modulation frequency: 33 kHz
- Modulation depth: 50 (0.5%)
- Spread type: Down spread (3)

.. code-block:: dts

   &dss0 {
       assigned-clocks = <&k3_clks 186 2>;
       assigned-clock-sscs = <33000 50 3>;
   };

Example 3: Greater modulation depth
===================================

Here is a configuration with greater modulation depth for better EMI reduction:

- Modulation frequency: 50 kHz
- Modulation depth: 250 (2.5%)
- Spread type: Down spread (3)

.. code-block:: dts

   &dss0 {
       assigned-clocks = <&k3_clks 186 2>;
       assigned-clock-sscs = <50000 250 3>;
   };

Example 4: Multiple pixel clocks
================================

Some SoCs, such as AM62Px, have many DSS instances. This example shows how to configure SSC for multiple pixel clocks together.

For DSS0:

- Modulation frequency: 50 kHz
- Modulation depth: 50 (0.5%)
- Spread type: Down spread (3)

For DSS1:

- Modulation frequency: 33 kHz
- Modulation depth: 50 (0.5%)
- Spread type: Down spread (3)

.. code-block:: dts

   &dss0 {
       assigned-clocks = <&k3_clks 186 2>;
       assigned-clock-sscs = <50000 50 3>;
   };

   &dss1 {
       assigned-clocks = <&k3_clks 232 4>;
       assigned-clock-sscs = <33000 50 3>;
   };

***************
Troubleshooting
***************

Display artifacts
=================

If you observe display artifacts, flickering, or other visual anomalies after enabling SSC:

1. Reduce the modulation depth to a smaller value (for example, try 0.1% or 10 in device tree)
2. Try a different modulation frequency (typical range: 32-100 kHz)
3. Switch from center spread to down spread mode if not already using it
4. Consult your display panel data sheet for spread spectrum tolerance specifications

Clock not found error
=====================

If you experience errors during boot about clock assignment:

1. Verify the clock ID is correct for your SoC (check the technical reference manual)
2. Ensure the Device Manager supports SSC for the specified clock
3. Check that the kernel version includes SSC support for the clock subsystem

****************************
Requirements and limitations
****************************

Hardware support
================

- SSC is currently only supported for display pixel clocks.

Configuration
=============

- Use ``assigned-clocks`` and ``assigned-clock-sscs`` together to specify which clock receives the SSC settings
- SSC causes the instantaneous clock frequency to deviate from the nominal rate
- Some panels have strict jitter requirements

Firmware capability
===================

Check if your firmware supports SSC by using the capability flag:

.. code-block:: console

   # Check firmware capabilities (requires ti-sci driver)
   cat /sys/kernel/debug/ti-sci/fw_caps

Look for ``TISCI_MSG_FLAG_FW_CAP_CLOCK_SSC`` in the capabilities list.

**********************************
Best practices and recommendations
**********************************

- Start with low modulation depth (0.1% to 0.5%) and increase only if needed
- Use down spread mode (3) for display interfaces. This ensures the clock never exceeds the maximum frequency
- Apply the 1.2 factor when using center spread mode
- Validate configuration with your display panel. Ensure timing margins meet requirements

*************************
Customer responsibilities
*************************

.. warning::

   **You assume all responsibility for the configuration and usage of spread spectrum clocking.** You must:

   1. Research the clock limitations associated with your selected display panel
   2. Configure SSC to be compatible with that specific display panel
   3. Verify that the SSC configuration does not cause any system-related issues for any operating condition
   4. Work with the display panel vendor to resolve any issues caused by enabling SSC
   5. Validate displays to have enough functional margin with the jitter introduced by spread spectrum modulation

   Some display panels have clocking limitations not mentioned in their data sheets. Work directly with the display panel manufacturer to resolve any issues from SSC.

**********
References
**********

- :ref:`dss7`
- `Application Note: AM62x, AM62Ax, AM62Px, AM62Lx Spread-Spectrum Clocking <https://www.ti.com/lit/pdf/spradk1>`__
- SoC Technical Reference Manual (TRM)
- System Firmware Documentation - PM Clock API
- Linux kernel device tree bindings: ``Documentation/devicetree/bindings/display/ti/``
- Linux kernel clock framework documentation: ``Documentation/driver-api/clk.rst``
