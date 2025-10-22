Docker Linux Container Runtime
==============================

Overview
--------

Docker complements kernel namespacing with a high-level API which
operates at the process level. It runs unix processes with strong
guarantees of isolation and repeatability across servers.

Docker is a great building block for automating distributed systems:
large-scale web deployments, database clusters, continuous deployment
systems, private PaaS, service-oriented architectures, etc.


Exploring Docker In Processor SDK
---------------------------------

Booting the Docker Filesystem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
It is recommended to mount to root filesystem from an SD card as the docker
runtime may not be located on an NFS mount. While it is possible to use Docker
on a NFS root, extra configuration is required to modify the default docker
runtime directory.

.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family', 'AM62X_family')

     Please follow the instructions for the :ref:`Create SD Card Script <processor-sdk-linux-create-sd-card-with-custom-images>`
     and when prompted to select the root filesystem tarball, select the ``tisdk-default-image``


Configuring the Docker daemon
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The default docker configuration is suitable in most settings. In certain cases,
custom configuration may be needed to properly setup docker, for example,
working behind a firewall. In the future, select configuration that may be
required will be provided here. Docker is an open source project with wide
support. Often a search online provide information on configuring for different
environments.

Docker Hello World
^^^^^^^^^^^^^^^^^^
On the EVM, login to the Linux shell. The following command will run the "Hello
World" demo and confirm that docker is properly configured.

.. code-block:: console

    $ docker run hello-world

    Hello from Docker!
    This message shows that your installation appears to be working correctly.

    To generate this message, Docker took the following steps:
     1. The Docker client contacted the Docker daemon.
     2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
        (amd64)
     3. The Docker daemon created a new container from that image which runs the
        executable that produces the output you are currently reading.
     4. The Docker daemon streamed that output to the Docker client, which sent it
        to your terminal.

    To try something more ambitious, you can run an Ubuntu container with:
     $ docker run -it ubuntu bash

    Share images, automate workflows, and more with a free Docker ID:
     https://hub.docker.com/

    For more examples and ideas, visit:
     https://docs.docker.com/get-started/



Docker References
-----------------
* https://docker.com/
* https://hub.docker.com/
