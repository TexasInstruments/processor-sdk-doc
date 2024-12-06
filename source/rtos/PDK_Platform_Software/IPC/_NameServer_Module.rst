.. http://processors.wiki.ti.com/index.php/IPC_Users_Guide/NameServer_Module 

.. |nsmCfg_Img1| Image:: /images/Book_cfg.png
                 :target: http://software-dl.ti.com/dsps/dsps_public_sw/sdo_sb/targetcontent/ipc/latest/docs/cdoc/index.html#ti/sdo/utils/NameServer.html

.. |nsmCfg_Img2| Image:: /images/Book_cfg.png
                 :target: http://software-dl.ti.com/dsps/dsps_public_sw/sdo_sb/targetcontent/ipc/latest/docs/cdoc/indexChrome.html

                 
.. |nsmRun_Img1| Image:: /images/Book_run.png
                 :target: http://downloads.ti.com/dsps/dsps_public_sw/sdo_sb/targetcontent/ipc/latest/docs/doxygen/html/_name_server_8h.html

.. |nsmRun_Img2| Image:: /images/Book_run.png
                 :target: http://downloads.ti.com/dsps/dsps_public_sw/sdo_sb/targetcontent/ipc/latest/docs/doxygen/html/_name_server_8h.html
                 
| 

   +---------------+---------------+
   |     API Reference Links       |
   +===============+===============+
   | |nsmCfg_Img1| | |nsmRun_Img1| |
   +---------------+---------------+


The NameServer module manages local name/value pairs. This enables an application and other modules to store and retrieve values based on a name.
The NameServer module maintains thread-safety for its APIs. However, NameServer APIs cannot be called from an interrupt (that is, Hwi context). They can be called from Swis (BIOS-only) and Tasks.

This module supports different lengths of values. The NameServer_add() and NameServer_get() functions support variable-length values. The NameServer_addUInt32() function is optimized for UInt32 variables and constants.

The NameServer module currently does not perform any endian or word size conversion. Also there is no asynchronous support at this time.

You can create NameServer instances dynamically. On BIOS, you can also create NameServer instances statically.

Creating NameServer Instances Statically (BIOS-only)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To create a NameServer instance statically, you can add statements similar to the following to your XDCtools configuration script:

::
  
  var NameServer = xdc.useModule('ti.sdo.utils.NameServer');
   
  var nameServerParams = new NameServer.Params;
  nameServerParams.maxRuntimeEntries = 10;
  nameServerParams.maxNameLen = 32;
  var nameServer0 = NameServer.create("nameServer0", nameServerParams);

If you want to specify the heap to be used by the NameServer module and a NameServer instance, use configuration statements similar to the following:


::
  
  var NameServer = xdc.useModule('ti.sdo.utils.NameServer');
  var HeapMem = xdc.useModule('ti.sysbios.heaps.HeapMem');
   
  var heapParams = new HeapMem.Params;
  heapParams.size = 1024;
  var heapMem = HeapMem.create(heapParams);
   
  var nameServerParams = new NameServer.Params;
  nameServerParams.tableHeap = heapMem;
  var nameServer = NameServer.create("staticNameServer", nameServerParams);

To create a NameServer instance dynamically, initialize a NameServer_Params structure with 
NameServer_Params_init() and customize the values as needed. 
The parameters include the following:

- **checkExisting.** If true, NameServer check to see if a name already exists in the name/value table before adding it.
- **maxNameLen.** Specify the maximum length, in characters, of the name field in the table.
- **maxRuntimeEntries.** Specify the maximum number of name/value pairs this table can hold. If you set this parameter to NameServer_ALLOWGROWTH, then NameServer allows dynamic growth of the table.
- **maxValueLen.** Specify the maximum length, in MAUs, of the value field in the table.
- **tableHeap.** The heap to allocate the name/value table from when allocating dynamically. If this parameter is NULL, the heap used for object allocation is also used here.

After setting parameters, use NameServer_create() to create an instance. 
Each NameServer instance manages its own name/value table.

|nsmCfg_Img2| The latest version of the NameServer module 
configuration documentation is available `online <http://software-dl.ti.com/dsps/dsps_public_sw/sdo_sb/targetcontent/ipc/latest/docs/cdoc/indexChrome.html>`_.

Creating and Removing NameServer Instances Dynamically
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The following C example creates a NameServer instance dynamically. 
The instance allows a maximum of 10 runtime entries (instead of using ALLOWGROWTH). 
This example also specifies where to allocate the memory needed for the tables (instead of using the default).

::
  
  NameServer_Handle NSHandle;
  NameServer_Params params;
   
  NameServer_Params_init(&params);
  params.tableHeap = HeapStd_Handle_upCast(myHeap);
  params.maxRuntimeEntries = 10;
  NSHandle = NameServer_create("myTable", &params);
  if (NSHandle == NULL) {
      // manage error
  }

This example C code adds and removes entries at run-time:

::
  
  Ptr key;
   
  key = NameServer_addUInt32(NSHandle, "volume", 5);
  if (key == NULL) {
      // manage error
  }
   
  NameServer_removeEntry(NSHandle, key);
  // or
  NameServer_remove(NSHandle, "volume");


|nsmRun_Img2| The latest version of the NameServer module run-time API 
documentation is available `online <http://downloads.ti.com/dsps/dsps_public_sw/sdo_sb/targetcontent/ipc/latest/docs/doxygen/html/_name_server_8h.html>`_.


Searching NameServer Instances
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The following example searches the NameServer instance pointed to by "handle" on 
the specified processor for a name-value pair with the name stored in nameToFind. 
It returns the value of the pair to valueBuf.

::
  
  /* Search NameServer */
  status = NameServer_get(NSHandle, nameToFind, valueBuf, sizeof(UInt32), procId);

Using different parameters for different table instances allows you to meet 
requirements like the following:

- **Size differences.** The maxValueLen parameter specifies the maximum length, in MAUs, of the value field in the table. One table could allow long values (for example, > 32 bits), while another table could be used to store integers. This customization enables better memory usage.
- **Performance.** Multiple NameServer tables can improve the search time when retrieving a name/value pair.
- **Relax name uniqueness.** Names in a specific table must be unique, but the same name can be used in different tables.

When you call NameServer_delete(), the memory for the name/values pairs is freed. 
You do not need to call NameServer_remove() on the entries before deleting a NameServer instance.

Other NameServer APIs
^^^^^^^^^^^^^^^^^^^^^^
In addition to the functions mentioned above, the NameServer module provides the following APIs:

- **NameServer_get()** Retrieves the value portion of a local name/value pair from the specified processor.
- **NameServer_getLocal()** Retrieves the value portion of a local name/value pair.
- **NameServer_remove()** Removes a name/value pair from the table given a name.
- **NameServer_removeEntry()** Removes an entry from the table given a pointer to an entry.

NameServer maintains the name/values table in local memory, not in shared memory. 
However the NameServer module can be used in a multiprocessor system. 
The module communicates with other processors via NameServer Remote drivers, 
which are implementations of the INameServerRemote interface. 
The communication to the other processors is dependent on the Remote drivers implementation. 
When a remote driver is created, it registers with NameServer via the NameServer_registerRemoteDriver() API.

The NameServer module uses the MultiProc module to identify different processors. 
Which remote processors to query and the order in which they are queried is 
determined by the procId array passed to the NameServer_get() function.



