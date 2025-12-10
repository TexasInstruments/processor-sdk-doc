.. _sysfw-trace-parser:

Enabling and Parsing SYSFW Trace
================================

SYSFW Trace Parser
------------------
This chapter gives details on how a helper script packaged in the SDK can be
used to parse the TISCI trace data. For more details on the TIFS trace refer
to `Trace chapter <https://software-dl.ti.com/tisci/esd/latest/4_trace/trace.html>`__
of TISCI documentation.


SDK packages a SYSFW trace parser utility (``bin/sysfw_trace_parser.py``) which
helps in parsing the hex strings that are output in UART when trace is enabled.

Usage of this tool is described below. Current version of trace (Option -Tv) is ``0x03006``.

::

    usage: ./sysfw_trace_parser.py [-h] (-l LOG_FILE | -d SERIAL_PORT)
                                   (-o OUTPUT_FILE | -O) [-Tv TRACE_DATA_VERSION]
                                   [-t] [-r RULES_FILE] [-Pm]


    Required arguments - Choose one of the inputs:
      -l LOG_FILE, --log_file LOG_FILE
                            Log File provided as input (default: None)
      -d SERIAL_PORT, --serial_port SERIAL_PORT
                            Provide Device as input: Requires pyserial package
                            installed: See https://pyserial.readthedocs.io/
                            (default: None)

    Required arguments - Choose one of the outputs:
      -o OUTPUT_FILE, --output_file OUTPUT_FILE
                            Parse out the output to a file (default: None)
      -O, --output_console  Log File to parse and report results to console
                            (default: False)

    optional arguments:
      -h, --help            show this help message and exit
      -Tv TRACE_DATA_VERSION, --trace_data_version TRACE_DATA_VERSION
                            Trace data version input in form "0xYYZZZ" where YY is
                            the major and ZZZ is the minor version. A trace data
                            version found in the log will override this input
                            (default: None)
      -t, --time_stamp_relative
                            Add TimeStamp to output in relative milliseconds(this
                            is approximation ONLY) (default: False)
      -r RULES_FILE, --rules_file RULES_FILE
                            Alternate Rules file (default: /home/vishallocal/SYSFW
                            /system-firmware-tools/system-firmware-
                            test/scripts/sysfw_trace_rules.json)
      -Pm, --print_match_only
                            Print just decoded data, (default: False)

    This script can also be called as a python module with the same arguments as
    the CLI. from sysfw_trace_parser import * sysfw_cli_job(args_arr=["-l",
    "sysfw_v2019.03_fail.log","-o","/tmp/out.log","-Tv","0x00000"]);


Enabling SYSFW Traces via Board Configuration
---------------------------------------------

Enabling and disabling of SYSFW traces is controlled by the debug configuration
settings in the SYSFW Board Configuration. Refer to `TISCI documentation <https://software-dl.ti.com/tisci/esd/latest/3_boardcfg/BOARDCFG.html#design-details-for-system-firmware-debug-console>`__
for more info on the Board Configuration.

For Linux boot flow, the default SYSFW Board Configuration is present in
u-boot code under the file path ``board/ti/<board-name>/board-cfg.yaml``.
The trace configuration is controlled by ``trace_dst_enables`` and
``trace_src_enables`` values and by default they are disabled.

::

    trace_dst_enables : 0x00
    trace_src_enables : 0x00


To enable traces update the ``trace_dst_enables`` and ``trace_src_enables`` values
of board-cfg.yaml file according to `boardcfg_dbg_dst_ports <https://software-dl.ti.com/tisci/esd/latest/3_boardcfg/BOARDCFG.html#boardcfg-dbg-dst-ports>`__
and `boardcfg_dbg_src <https://software-dl.ti.com/tisci/esd/latest/3_boardcfg/BOARDCFG.html#boardcfg-dbg-src>`__
settings accordingly.

The example below shows values that enable SYSFW traces destination on UART
and traces from all sources. After making the changes re-build the u-boot binaries
for the changes to take effect.

::

    trace_dst_enables : 0x01
    trace_src_enables : 0x1F
