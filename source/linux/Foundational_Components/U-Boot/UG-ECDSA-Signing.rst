.. _u-boot-ecdsa-signing:

#############################################
ECDSA signing for K3 devices
#############################################

The SDK signs boot images with an RSA key by default. This page only lists what changes to use an ECDSA key instead on K3 devices (AM62, AM64, AM65, J721E, J722S, J784S4, etc.). For the full signing procedure, follow the original guides linked in each section.

Any ECDSA curve supported by OpenSSL can be used (for example secp256r1, secp384r1, secp521r1). P-384 (secp384r1) is recommended. The FIT signature algorithm is ``sha512,ecdsa`` regardless of the curve.

.. _ecdsa-key-gen:

**************************
Generate ECDSA keys
**************************

Generate the key and certificate with the same names the RSA setup already uses, so nothing else needs renaming:

.. code-block:: console

   openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:secp384r1 -out custMpk.key
   openssl req -new -x509 -key custMpk.key -out custMpk.crt -days 3650 -subj "/CN=Custom ECDSA Key"

Use ``openssl ecparam -list_curves`` to see the other curves available.

.. _ecdsa-boot-images:

***************************
Sign boot images
***************************

For tiboot3.bin, tispl.bin and u-boot.img, binman picks the key from ``arch/arm/mach-k3/keys/``. Replace the existing RSA files with your ECDSA ones:

.. code-block:: console

   cp custMpk.key arch/arm/mach-k3/keys/custMpk.pem
   cp custMpk.crt arch/arm/mach-k3/keys/custMpk.crt

No devicetree or config changes are needed. Build as described in :ref:`top-level-makefile`.

.. _ecdsa-kernel-fitimage:

***************************
Sign kernel fitImage
***************************

Follow the `U-Boot K3 FIT signature signing guide <https://docs.u-boot.org/en/v2026.04/board/ti/k3.html#fit-signature-signing>`__, with these differences:

#. Change the algorithm in the ``signature-1`` node of your ``fitImage.its``. Keep ``key-name-hint = "custMpk"``:

   .. code-block:: dts

      signature-1 {
         algo = "sha512,ecdsa";
         key-name-hint = "custMpk";
         sign-images = "kernel", "fdt";
      };

#. Put your ECDSA ``custMpk.key`` and ``custMpk.crt`` in the keys directory you pass to ``mkimage -k``.

#. Rebuild U-Boot after generating the fitImage, so the updated ``dt.dtb`` with the public key is packed into u-boot.img.

Check the result with ``mkimage -l fitImage``; the signature section should show ``sha512,ecdsa``.

.. ifconfig:: CONFIG_part_family in ('AM62LX_family')

   .. _ecdsa-uboot-fit:

   .. rubric:: Sign U-Boot FIT

   On AM62Lx, u-boot.img is a signed FIT image. Change the algorithm on the FIT configuration node in the board ``*-binman.dtsi``. Keep ``key-name-hint = "custMpk"``:

   .. code-block:: dts

      signature {
         algo = "sha512,ecdsa";
         key-name-hint = "custMpk";
         sign-images = "firmware", "loadables", "fdt";
      };

   Replace ``custMpk.key``, ``custMpk.pem`` and ``custMpk.crt`` in ``arch/arm/mach-k3/keys/`` with your ECDSA key and certificate, then rebuild U-Boot. Check the result with ``mkimage -l u-boot.img``.

.. _ecdsa-see-also:

********
See also
********

- :ref:`foundational-secure-boot` - complete secure boot documentation
- :ref:`top-level-makefile` - top-level build instructions
- `FIT signature signing - U-Boot K3 documentation <https://docs.u-boot.org/en/v2026.04/board/ti/k3.html#fit-signature-signing>`__
