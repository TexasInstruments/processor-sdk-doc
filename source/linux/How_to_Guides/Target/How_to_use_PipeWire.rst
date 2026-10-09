.. _how-to-use-pipewire:

How to Use PipeWire
###################

Introduction
************

PipeWire is a modern, low-latency multimedia framework that has become the
standard for audio and video handling in Linux applications, providing
graph-based processing with real-time capabilities using unified
architecture. PipeWire’s multi-process architecture allows multiple
applications to seamlessly share multimedia content without conflicts or
resource contention.

Key Highlights
**************

- Unified Multimedia Framework: Single solution for professional audio
  (JACK), consumer audio (PulseAudio), and video processing.
- Low Latency Performance.
- Security Model: Built-in sandboxing support for containerized
  applications.
- Multi-process architecture to let applications share multimedia content.
- Real-time multimedia processing on audio and video.

Basic Concepts
**************

PipeWire Server
===============
The server is the core daemon that manages a graph-based multimedia
processing engine. It handles the creation and execution of the media
graph where audio, video, or MIDI data flows between different processing
components.

PipeWire Clients
================
Clients are applications that connect to the PipeWire server to produce or
consume media streams. They create nodes in the media graph to send or
receive audio or video data.

Session Manager
===============
PipeWire does not handle device routing or policy decisions by itself.
These tasks are managed by a session manager, which monitors devices and
automatically connects streams. In this document, WirePlumber is used as
the session manager.

Nodes, Ports, and Links
=======================
The PipeWire processing graph consists of nodes, ports, and links. A node
represents a processing element, ports act as input or output interfaces,
and links connect ports between nodes to allow media data to flow through
the graph.

PipeWire Main Components
************************

- A PipeWire Daemon that implements the IPC and graph processing.
- An example PipeWire Session Manager that manages objects in the
  PipeWire Daemon.
- A set of Programs to introspect and use the PipeWire Daemon.
- A PipeWire Library to develop PipeWire applications and plugins.
- The SPA (Simple Plugin API) used by both the PipeWire Daemon and in the
  PipeWire Library.

For more info refer `PipeWire Docs <https://docs.pipewire.org/devel/index.html>`__.

Audio System Architecture
*************************

.. figure:: /images/pipewire_stack.png
   :align: center
   :width: 600

- In Linux audio system using, applications such as media players,
  browsers, VoIP clients, or tools like GStreamer send and receive
  audio through APIs like the native PipeWire API or compatibility
  layers for Jack, Pulseaudio or (ALSA).
- These audio streams are handled by the PipeWire media server, which
  builds a processing graph to mix, route, and schedule audio from
  multiple applications.
- A session manager such as WirePlumber applies policies like device
  selection and automatic routing.
- PipeWire accesses actual audio devices using its SPA device plugins
  (for example the ALSA plugin), which communicate with the ALSA sound
  subsystem inside the Linux kernel.
- The kernel drivers then control the physical hardware such as audio
  codecs, sound cards, or interfaces like I2S or HDMI, completing the
  path from application audio streams to the real audio output or
  input devices.

Start and use PipeWire
**********************

After the board is booted, use following commands to get started on
PipeWire:

Check service status
====================

.. code-block:: console

   root@<machine>: systemctl status pipewire wireplumber
   root@<machine>: systemctl status wireplumber

Enable PipeWire and Wireplumber
===============================

Enable service to start automatically at boot

.. code-block:: console

   root@<machine>: systemctl enable pipewire
   root@<machine>: systemctl enable wireplumber

.. ifconfig:: CONFIG_part_variant in ('AM62DX')

   A new service is also added by patches to set default audio devices in
   WirePlumber to avoid manual setup. To enable it:

   .. code-block:: console

      root@<machine>: systemctl enable set-audio-defaults

Start PipeWire and WirePlumber
==============================

Start PipeWire and WirePlumber if not started by default

.. code-block:: console

   root@<machine>: systemctl start pipewire
   root@<machine>: systemctl start wireplumber

.. ifconfig:: CONFIG_part_variant in ('AM62DX')

   .. code-block:: console
   
      root@<machine>: systemctl start set-audio-defaults

General PipeWire commands
*************************

List all objects currently in PipeWire server
=============================================

.. code-block:: console

   root@<machine>: pw-cli list-objects
        id 0, type PipeWire:Interface:Core/4
               object.serial = "0"
               core.name = "pipewire-0"
        id 1, type PipeWire:Interface:Module/3
               object.serial = "1"
               module.name = "libpipewire-module-rt"
        id 2, type PipeWire:Interface:Module/3
               object.serial = "2"
               module.name = "libpipewire-module-protocol-native"
        id 3, type PipeWire:Interface:SecurityContext/3
               object.serial = "3"
        id 4, type PipeWire:Interface:Module/3
               object.serial = "4"
               module.name = "libpipewire-module-profiler"
        id 5, type PipeWire:Interface:Profiler/3
               object.serial = "5"

List only nodes
===============

.. code-block:: console

   root@<machine>: pw-cli list-objects Node
        id 29, type PipeWire:Interface:Node/3
                object.serial = "29"
                factory.id = "11"
                priority.driver = "200000"
                node.name = "Dummy-Driver"
        id 30, type PipeWire:Interface:Node/3
                object.serial = "30"
                factory.id = "11"
                priority.driver = "190000"
                node.name = "Freewheel-Driver"
        id 31, type PipeWire:Interface:Node/3
                object.serial = "31"
                factory.id = "19"
                node.description = "Audio Output"
                node.name = "alsa_audio_sink"
                media.class = "Audio/Sink"
        id 32, type PipeWire:Interface:Node/3
                object.serial = "32"
                factory.id = "19"
                node.description = "Audio Input"
                node.name = "alsa_audio_source"
                media.class = "Audio/Source"

Inspect specific object
=======================

Inspect specific object using command ``pw-cli info <object-id>``.

.. code-block:: console

   root@<machine>: pw-cli info 31
        id: 31
        permissions: rwxm-
        type: PipeWire:Interface:Node/3
        input ports: 0/0
        output ports: 8/129
        state: "suspended"
        properties:
            factory.name = "api.alsa.pcm.source"
            node.name = "alsa_audio_source"
            node.description = "Audio Input"
            media.class = "Audio/Source"
            api.alsa.period-size = "1024"
            node.driver = "true"
            api.alsa.disable-mmap = "false"
            api.alsa.disable-batch = "false"
            api.alsa.path = "hw:0,0"
            audio.rate = "48000"
            audio.channels = "8"

Play and Record Stereo Audio
============================

Play audio via ``pw-play`` or ``aplay`` directly.

.. code-block:: console

   root@<machine>: pw-play --target=alsa_audio_sink <wav file path>
   root@<machine>: aplay <wav file path>

Record audio via PipeWire user tools or ``aplay`` directly.

.. code-block:: console

   root@<machine>: pw-record --target=alsa_audio_source <path of new wav file>
   root@<machine>: arecord <path of new wav file>

Configuration Details
=====================

A typical PipeWire setup consists of

- PipeWire daemon
- Session manager (usually WirePlumber)
- Compatibility servers (PulseAudio, JACK)
- Client configuration

Each of these has its own configuration file which uses SPA JSON format,
which is a relaxed JSON syntax.

.. list-table:: Configuration files
   :widths: 30 70
   :header-rows: 1

   * - Files
     - Purpose
   * - pipewire.conf
     - Configures the PipeWire daemon
   * - client.conf
     - Configures PipeWire clients
   * - pipewire-pulse.conf
     - PulseAudio compatibility server
   * - filter-chain.conf
     - Audio processing filters

Instead of modifying the main file, PipeWire recommends using drop-in files
to override only specific settings. Example in directory

.. code-block:: console

   $ /etc/pipewire/pipewire.conf.d/

.. ifconfig:: CONFIG_part_variant in ('AM62DX')

   Let’s discuss reference configuration files added specifically for
   AM62D2-EVM in patches in the upcoming sections.

   There are two reference configurations files, sink and source added for
   AM62D2-EVM.

   **90-pipewire-sink.conf**

   .. code-block:: text

      # PipeWire sink configuration for AM62D.

      context.objects = [
          {
              factory = adapter
              args = {
                  factory.name           = api.alsa.pcm.sink
                  node.name              = "alsa_audio_sink"
                  node.description       = "Audio Output"
                  media.class            = "Audio/Sink"
                  api.alsa.period-size   = 1024
                  api.alsa.headroom      = 0
                  api.alsa.disable-mmap  = false
                  api.alsa.disable-batch = false
                  api.alsa.path          = "hw:0,0"
                  audio.rate             = 48000
                  audio.channels         = 8
                  audio.position         = [ FL FR FC LFE RL RR SL SR ]
               }
           }
      ]

   **91-pipewire-source.conf**

   .. code-block:: text

      # PipeWire source configuration for AM62D.

      context.objects = [
          {
              factory = adapter
              args = {
                  factory.name           = api.alsa.pcm.source
                  node.name              = "alsa_audio_source"
                  node.description       = "Audio Input"
                  media.class            = "Audio/Source"
                  api.alsa.period-size   = 1024
                  api.alsa.headroom      = 0
                  api.alsa.disable-mmap  = false
                  api.alsa.disable-batch = false
                  api.alsa.path          = "hw:0,0"
                  audio.rate             = 48000
                  audio.channels         = 8
                  audio.position         = [ FL FR FC LFE RL RR SL SR ]
               }
           }
       ]

.. ifconfig:: CONFIG_part_variant not in ('AM62DX')

   For other platforms, you can use similar configuration files for sink and source.
   Below are example configurations for both.

   **90-pipewire-sink.conf**

   .. code-block:: text

      # PipeWire sink configuration
      context.objects = [
          {
              factory = adapter
              args = {
                  factory.name           = api.alsa.pcm.sink
                  node.name              = "alsa_audio_sink"
                  node.description       = "Audio Output"
                  media.class            = "Audio/Sink"
                  api.alsa.period-size   = 1024
                  api.alsa.path          = "hw:0,0"
                  audio.rate             = 48000
                  audio.channels         = 2
                  audio.position         = [ FL FR ]
               }
           }
      ]

   **91-pipewire-source.conf**

   .. code-block:: text

      # PipeWire source configuration
      context.objects = [
          {
              factory = adapter
              args = {
                  factory.name           = api.alsa.pcm.source
                  node.name              = "alsa_audio_source"
                  node.description       = "Audio Input"
                  media.class            = "Audio/Source"
                  api.alsa.period-size   = 1024
                  api.alsa.path          = "hw:0,0"
                  audio.rate             = 48000
                  audio.channels         = 2
                  audio.position         = [ FL FR ]
               }
           }
      ]

Both files use identical structural patterns with only key functional
differences:

- **context.objects**
  Main configuration array defining objects created in PipeWire context.
  Each object in this array becomes a node in the PipeWire graph.
- **factory = adapter**
  Specifies that this object should be created using the "adapter"
  factory. Adapters in PipeWire are used to bridge between different
  APIs (in this case, ALSA to PipeWire). Both configuration files use
  adapter factory to bridge ALSA hardware to PipeWire nodes.
- **factory.name**
  Determines direction: output vs input
- **node.name**
  Internal PipeWire node identifier. Creates alsa_audio_sink for playback
  and alsa_audio_source for capture.
- **node.description**
  Human-readable name in audio apps.
- **media.class**
  PipeWire media classification "Audio/Sink" for playback and
  "Audio/Source" for recording.
- **api.alsa.path**
  For direct hardware access. Only PipeWire can access the audio hardware
  and ALSA applications must go through PipeWire.
- **audio.channels**
  Configures both input and output for 8 channel audio in case of
  AM62D2-EVM and stereo audio in case of other devices.

These configurations create two fundamental nodes in PipeWire's audio
graph:
- Sink Node: Terminal endpoint for audio playback chains
- Source Node: Starting point for audio capture chains
- Matched Pair: Enables full-duplex audio applications

For more information, please refer `Alsa Configuration <https://pipewire.pages.freedesktop.org/wireplumber/daemon/configuration/alsa.html>`__.

WirePlumber Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

.. ifconfig:: CONFIG_part_variant in ('AM62DX')

   Use the command below to list all the available audio sinks and sources.

   .. code-block:: console

      root@<machine>: wpctl status
      PipeWire 'pipewire-0' [1.6.0, root@am62dxx-evm, cookie:3333499771]
      └─ Clients:
          34. WirePlumber [1.6.0, root@am62dxx-evm, pid:9716]
          58. WirePlumber [export] [1.6.0, root@am62dxx-evm, pid:9716]
          94. wpctl [1.6.0, root@am62dxx-evm, pid:9753]

       Audio
       ├ Devices:
       │ 59. Built-in Audio [alsa]
       │
       ├ Sinks:
       │ * 31. Audio Output [vol: 1.00]
       │ 68. Built-in Audio Stereo [vol: 0.40]
       │
       ├ Sources:
       │ * 32. Audio Input [vol: 1.00]
       │ 69. Built-in Audio Stereo [vol: 1.00]
       │
       ├ Filters:
       │
       └─ Streams:

       Video
       ├ Devices:
       │
       ├ Sinks:
       │
       ├ Sources:
       │
       ├ Filters:
       │
       └─ Streams:

       Settings
       └─ Default Configured Devices:
         0. Audio/Sink alsa_audio_sink
         1. Audio/Source alsa_audio_source

.. ifconfig:: CONFIG_part_variant not in ('AM62DX')

   Use the command below to list all the available audio sinks and sources.

   .. code-block:: console

      root@<machine>: wpctl status
      PipeWire 'pipewire-0' [1.6.0, root@<machine>, cookie:3333499771]
      └─ Clients:
          34. WirePlumber [1.6.0, root@<machine>, pid:9716]
          58. WirePlumber [export] [1.6.0, root@am62dxx-evm, pid:9716]
          94. wpctl [1.6.0, root@<machine>, pid:9753]

       Audio
       ├ Devices:
       │ 59. Built-in Audio [alsa]
       │
       ├ Sinks:
       │ * 68. Built-in Audio Stereo [vol: 0.40]
       │
       ├ Sources:
       │ * 69. Built-in Audio Stereo [vol: 1.00]
       │
       ├ Filters:
       │
       └─ Streams:

       Video
       ├ Devices:
       │
       ├ Sinks:
       │
       ├ Sources:
       │
       ├ Filters:
       │
       └─ Streams:

Use ``wpctl`` inspect to display information about the specified object.

.. code-block:: console

   root@<machine>: wpctl inspect <object number>

Defaults source could also be set manually by using the ID number of sinks
and sources:

.. code-block:: console

   root@<machine>: wpctl set-default <object number>
   root@<machine>: wpctl set-default <object number>
