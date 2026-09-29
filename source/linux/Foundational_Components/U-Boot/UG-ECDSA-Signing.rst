.. _u-boot-ecdsa-signing:

#############################################
ECDSA signing of K3 boot images
#############################################

K3 secure boot images (:file:`tiboot3.bin`, :file:`tispl.bin`, and
:file:`u-boot.img`) are signed with a customer master private key,
:file:`custMpk.pem`, before being authenticated by ROM/TIFS during boot.
By default this key is RSA. This guide shows how to switch to ECDSA signing
instead, using your own ECDSA key, with a standalone ``ti-u-boot`` build.

This is a separate mechanism from the HSM-based signing covered in
:ref:`foundational-secure-boot` and from the U-Boot native verified boot
RSA/FIT flow described in :ref:`u-boot-secure-boot-verified-boot`.

*************
Prerequisites
*************

- A working ``ti-u-boot`` source tree, checked out and able to build your
  board's defconfig normally.
- Your own ECDSA private key, in PEM format, named :file:`custMpk.pem`.

*******************
How the key is used
*******************

:file:`tiboot3.bin` comes from the Cortex-R5 (R5 SPL) build, while
:file:`tispl.bin` and :file:`u-boot.img` come from the separate Cortex-A72
build. These are two distinct ``make`` invocations, using different
defconfigs and different cross-compilers, each with its own ``binman``
pass (the ``.binman_stamp`` target in the top-level :file:`Makefile`).
Within each of those two builds, all of that build's outputs are produced
by binman in a single pass, so for the A72 build, :file:`tispl.bin` and
:file:`u-boot.img` are signed together, with no separate key selection
between them. The signing key path itself is controlled, for both builds,
by one Kconfig string, ``CONFIG_K3_KEYFILE_NAME``, defined in
:file:`arch/arm/mach-k3/Kconfig`:

.. code-block:: text

   config K3_KEYFILE_NAME
   	string "Key file used by binman to sign K3 boot images"
   	default "rsa/custMpk.pem"

The value is consumed directly in the devicetree source. In
:file:`arch/arm/dts/k3-binman.dtsi`, the ``custMpk`` binman entry resolves
and stages the actual key file:

.. code-block:: dts

   &binman {
   	custMpk {
   		filename = "custMpk.pem";
   		custmpk_pem: blob-ext {
   			filename = CONFIG_K3_KEYFILE_NAME;
   		};
   	};
   };

Every ``ti-secure``/``ti-secure-rom`` signing node, meaning the ones that
produce :file:`tispl.bin` and :file:`u-boot.img` in :file:`k3-binman.dtsi`,
and the board-specific node that produces :file:`tiboot3.bin` in each
board's ``*-binman.dtsi``, references the key by its staged name:

.. code-block:: dts

   keyfile = "custMpk.pem";

Because ``CONFIG_K3_KEYFILE_NAME`` is the same Kconfig option in both the
Cortex-R5 and Cortex-A72 defconfigs, merging the same
:file:`k3_ecdsa.config` fragment onto both builds switches the key used for
:file:`tiboot3.bin`, :file:`tispl.bin`, and :file:`u-boot.img` together.
There is nothing to configure per image, only per build.

*****
Steps
*****

1. Place your ECDSA key under :file:`arch/arm/mach-k3/keys/ecdsa/` in the
   ``ti-u-boot`` source tree:

   .. code-block:: console

      cp /path/to/your/ecdsa_custMpk.pem arch/arm/mach-k3/keys/ecdsa/custMpk.pem

   This directory is searched by binman by default, alongside the repo
   root, so no additional path configuration is required for a standalone
   build. If your key lives elsewhere, point binman at its parent
   directory instead, using ``BINMAN_INDIRS`` (see below).

2. Configure and build the Cortex-R5 defconfig, merging the
   :file:`configs/k3_ecdsa.config` fragment on top of it, to produce
   :file:`tiboot3.bin`:

   .. code-block:: console

      make ${UBOOT_CFG_CORTEXR} k3_ecdsa.config
      make CROSS_COMPILE=${CC32} \
           BINMAN_INDIRS="${LNX_FW_PATH} /path/to/keys"

   Here ``/path/to/keys`` is the directory that contains your ``ecdsa``
   (or ``rsa``) subfolder, not the subfolder itself, since
   ``CONFIG_K3_KEYFILE_NAME`` already carries the ``ecdsa/custMpk.pem``
   part of the path. If your key is at the default location from step 1
   (:file:`arch/arm/mach-k3/keys/ecdsa/custMpk.pem`), this entry can be
   dropped from ``BINMAN_INDIRS``, since that directory is already
   searched by default.

3. Configure and build the Cortex-A72 defconfig the same way, to produce
   :file:`tispl.bin` and :file:`u-boot.img` together:

   .. code-block:: console

      make ${UBOOT_CFG_CORTEXA} k3_ecdsa.config
      make CROSS_COMPILE=${CC64} \
           BINMAN_INDIRS="${LNX_FW_PATH} /path/to/keys" \
           BL31=${TFA_PATH}/build/k3/${TFA_BOARD}/release/bl31.bin \
           TEE=${OPTEE_PATH}/out/arm-plat-k3/core/tee-raw.bin

   ``BL31``/``TEE`` are unrelated to key selection: they point binman at
   the TF-A and OP-TEE binaries this build needs to assemble
   :file:`tispl.bin`. They are passed on the same ``make`` line as
   ``BINMAN_INDIRS`` because both outputs of this build
   (:file:`tispl.bin` and :file:`u-boot.img`) come from the same single
   binman pass.

   In both builds, binman signs its outputs using ``openssl``, which
   auto-detects the key algorithm (RSA or EC) from the key file itself.
   No separate algorithm selection is needed beyond the key path change
   from the ``k3_ecdsa.config`` fragment.

4. Confirm the resulting images were signed with the ECDSA key by
   extracting and inspecting the certificate, for example from
   :file:`tiboot3.bin`:

   .. code-block:: console

      openssl x509 -inform DER -in <extracted-cert> -noout -text | grep "Public Key Algorithm"

   This should report ``id-ecPublicKey`` rather than ``rsaEncryption``.
   Repeat against the certificates embedded in :file:`tispl.bin` and
   :file:`u-boot.img` to confirm the same key was used for both builds.

**********************
Switching back to RSA
**********************

Reconfigure without the fragment, or explicitly clear the option back to
its default:

.. code-block:: console

   make <board>_defconfig

********
See Also
********

- :ref:`foundational-secure-boot`
- :ref:`u-boot-secure-boot-verified-boot`
