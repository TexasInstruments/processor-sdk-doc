.. _pub_edgeai_docker_env:

==================
Docker Environment
==================

Docker is a set of "platform as a service" products that uses the OS-level
virtualization to deliver software in packages called containers.
Docker container provides a quick start environment to the developer to
run the out of box demos and build applications.

The Docker image is based on Ubuntu 22.04.LTS and contains different
open source components like OpenCV, GStreamer, Python and pip packages
which are required to run the demos. The user can choose to install any
additional 3rd party applications and packages as required.

.. _pub_edgeai_docker_build_ontarget:

Building Docker image
======================

The `docker/Dockerfile` in the edgeai-gst-apps repo describes the recipe for
creating the Docker container image. Feel free to review and update it to
include additional packages before building the image.

.. note::

   Building Docker image on target using the provided Dockerfile will take
   about 15-20 minutes to complete with good internet connection.
   Building Docker containers on target can be slow and resource constrained.
   The Dockerfile provided will build on target without any issues but if
   you add more packages or build components from source, running out of memory
   can be a common problem. As an alternative we highly recommend trying
   QEMU builds for cross-compiling the images for arm64 architecture on a PC
   and then load the compiled image on target.

Initiate the Docker image build as shown,

.. code-block:: bash

   /opt/edgeai-gst-apps/docker# ./docker_build.sh

Running the Docker container
============================

Enter the Docker session as shown,

.. code-block:: bash

   /opt/edgeai-gst-apps/docker# ./docker_run.sh

This will start a Ubuntu 22.04.LTS image based Docker container and the prompt
will change as below,

.. code-block:: bash

   [docker] /opt/edgeai-gst-apps#


The Docker container has been created in privilege mode, so that it has root
capabilities to all devices on the target system like Network etc.
The container file system also mounts the target file system of /dev, /opt to
access camera, display and other hardware accelerators the SoC has to offer.

.. note::

   It is highly recommended to use the docker_run.sh script to launch the
   docker container because this script will take care of saving any changes
   made to the filesystem. This will make sure that any modifications to
   the Docker filesystem including new package installation, updates to
   some files and also command history is saved automatically and is
   available the next time you launch the container. The container will
   be committed only if you exit from the container explicitly. If you restart
   the board without exiting container, any changes done from last saved state
   will be lost.

.. note::

   After building and running the docker container, one needs to run
   :file:`setup_script.sh` before running any of the demo applications.
   This is required to rebuild all components against the shared libraries
   of docker, same should be done when switching back to Yocto

.. _pub_edgeai_docker_additional_commands:

Additional Docker commands
==========================

.. note::

   This section is provided only for additional reference and not required to
   run out-of-box demos

**Commit Docker container**

Generally, containers have a short life cycle. If the container has any local
changes it is good to save the changes on top of the existing Docker image.
When re-running the Docker image, the local changes can be restored.

Following commands show how to save the changes made to the last container.
Note that this is already done automatically by :file:`docker_run.sh` when you exit
the container.

.. code-block:: bash

   cont_id=`docker ps -q -l`
   docker commit $cont_id edge_ai_kit
   docker container rm $cont_id


For more information refer:
`Commit Docker image <https://docs.docker.com/engine/reference/commandline/commit/>`_

**Save Docker Image**

Docker image can be saved as tar file by using the command below:

.. code-block:: console

   docker save --output <pre_built_docker_image.tar>

For more information refer here.
`Save Docker image <https://docs.docker.com/engine/reference/commandline/save/>`_

**Load Docker image**

Load a previously saved Docker image using the command below:

.. code-block:: console

   docker load --input <pre_built_docker_image.tar>

For more information refer here.
`Load Docker image <https://docs.docker.com/engine/reference/commandline/load/>`_

**Remove Docker image**

Docker image can be removed by using the command below:

.. code-block:: console

   Remove selected image:
   docker rmi <image_name/ID>

   Remove all image:
   docker image prune -a

For more information refer
`rmi reference <https://docs.docker.com/engine/reference/commandline/rmi/>`_ and
`Image prune reference <https://docs.docker.com/engine/reference/commandline/image_prune/>`_

**Remove Docker container**

Docker container can be removed by using the command below:

.. code-block:: console

   Remove selected container:
   docker rm <container_ID>

   Remove all container:
   docker container prune

For more information refer here.
`rm reference <https://docs.docker.com/engine/reference/commandline/rm/>`_ and
`Container Prune reference <https://docs.docker.com/engine/reference/commandline/container_prune/>`_

Relocating Docker Root Location
===============================
The default location for Docker files is **/var/lib/docker**. Any Docker images
created will be stored here. This will be a problem anytime the SD card is
updated with a new targetfs. If a secondary storage (SSD or USB based storage)
is available, then it is recommended to relocate the default Docker root
location so as to preserve any existing Docker images. Once the relocation
has been done, the Docker content will not be affected by any future targetfs
updates or accidental corruptions of the SD card.

The following steps outline the process for Docker root directory relocation
assuming that the current Docker root is not at the desired location. If the
current location is the desired location then exit this procedure.

1. Run 'Docker info' command and inspect the output. Locate the line with
   content **Docker Root Dir**. It will list the current location.

2. To preserve any existing images, export them to .tar files for importing
   later into the new location.

3. Inspect the content under /etc/docker to see if there is a file by name
   **daemon.json**. If the file is not present then create **/etc/docker/docker.json**
   and add the following content. Update the 'key:value' pair for the key "graph"
   to reflect the desired root location. If the file already exists, then make
   sure that the line with "graph" exists in the file and points to the desired
   target location.

   .. code-block:: json

      {
         "graph": "/run/media/nvme0n1/docker_root",
         "storage-driver": "overlay",
         "live-restore": true
      }

   In the configuration above, the key/value pair
   **'"graph": "/run/media/nvme0n1/docker_root"'** defines the root location
   **'/run/media/nvme0n1/docker_root'.**

4. Once the daemon.json file has been copied and updated, run the following
   commands

   .. code-block:: bash

      $ systemctl restart docker
      $ docker info

   Make sure that the new Docker root appears under **Docker Root Dir** value.

5. If you exported the existing images in step (2) then import them and they
   will appear under the new Docker root.

6. Anytime the SD card is updated with a new targetfs, steps (1), (3), and
   (4) need to be followed.

**Additional references**

| https://docs.docker.com/engine/reference/commandline/images/
| https://docs.docker.com/engine/reference/commandline/ps/
