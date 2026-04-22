.. _u-boot-secure-boot-verified-boot:

################################################
Secure boot using U-Boot verified boot framework
################################################

The complete Secure Boot documentation is available at:
:ref:`foundational-secure-boot`. This page specifically covers the
authentication and verification of U-Boot image using `U-Boot Verified Boot`_.

On most other K3 devices, signing and verification of all boot binaries takes
place in the Hardware Security Module (HSM). Thereafter, U-Boot hands off the
secure chain of trust to the Linux kernel :file:`fitImage`.

On AM62Lx, we have transitioned to use the native U-Boot secure boot framework
for a part of this chain of trust. The U-Boot documentation covers more theory
on this at
`U-Boot Verified Boot <https://docs.u-boot.org/en/latest/usage/fit/verified-boot.html>`_
and `U-Boot FIT Signature Verification <https://docs.u-boot.org/en/latest/usage/fit/signature.html#signed-configurations>`__.
The thing to note is, we are applying the same concepts to U-Boot Flattened
Image Tree (FIT) as the kernel FIT examples in the preceding links.

The HSM still handles the verification of :file:`tiboot3.bin` and
:file:`tispl.bin`. However, we hand off the chain of trust to U-Boot just after
this. The :file:`u-boot.img` is a signed FIT image. The U-Boot Secondary
Program Loader (SPL) binary embeds the public key derived from the private key
used to sign the U-Boot FIT. The U-Boot SPL uses this to verify the
authenticity of the loaded U-Boot binary.

**************
The FIT source
**************

The U-Boot FIT configuration node contains a signature sub-node.

.. code-block:: dts

   conf-0 {
      description = "k3-am62lx-evm";
      firmware = "uboot";
      loadables = "uboot";
      fdt = "fdt-0";

      signature {
         algo = "sha512,rsa4096";
         key-name-hint = "custMpk";
         sign-images = "firmware", "loadables", "fdt";
      };
   };

It specifies the key name and algorithm to use for signing, and the images
to sign.

The public key is similarly embedded into U-Boot SPL by using a binman property
called :code:`u-boot-spl-pubkey-dtb`. This handles the heavy lifting of calling
the appropriate :code:`mkimage` commands and packing the public key in the SPL
Device Tree Blob (DTB) correctly.

.. code-block:: dts

   tispl.bin {

      ...

      spl: section {
         u-boot-spl-nodtb {
         };

         u-boot-spl-pubkey-dtb {
            algo = "sha512,rsa4096";
            required = "conf";
            key-name-hint = "custMpk";
         };
      };
   };

The :code:`key-name-hint` property in both these nodes searches for the
:file:`custMpk.key` private key and :file:`custMpk.crt` public key certificate
in the directories defined in the :code:`BINMAN_INDIRS` variable. The default
TI dummy keys reside in :file:`arch/arm/mach-k3/keys/`, and binman copies them
at the start of the build into the build directory:

.. code-block:: dts

   custMpk-crt {
      filename = "custMpk.crt";

      custmpk_crt: blob-ext {
         filename = "arch/arm/mach-k3/keys/custMpk.crt";
      };
   };

   custMpk-key {
      filename = "custMpk.key";

      custmpk_key: blob-ext {
         filename = "arch/arm/mach-k3/keys/custMpk.key";
      };
   };

********************
Runtime verification
********************

At runtime during device boot, U-Boot SPL loads the :file:`u-boot.img` and then
verifies the FIT signature by using the public key it has in its DTB. If the
verification passes, boot continues. Otherwise, it aborts the boot.

***********************
Changing the dummy keys
***********************

The SDKs use the TI dummy key for signing the U-Boot FIT image. But you might
want to use your own key for testing and production. For this, replace the
:file:`arch/arm/mach-k3/keys/custMpk.key` and
:file:`arch/arm/mach-k3/keys/custMpk.crt` with your own key and crt files. The
filenames need to be the same.

It is also possible to use your own keys located at a different location. You
need to change the complete path in the :code:`filename` property above in
:code:`custMpk-crt` and :code:`custMpk-key` in
:file:`arch/arm/dts/k3-am62l3-evm-binman.dtsi` to your .crt and .key files.

After either of the above changes, the U-Boot needs to be built again to get
the signed binaries with the updated keys. Refer to :ref:`top-level-makefile`.

.. note::

   Generating a new set of keys:

   .. code-block:: console

      $ mkdir keys
      $ cd keys
      $ # Generate an RSA private key:
      $ openssl genpkey -algorithm RSA -out custMpk.key \
         -pkeyopt rsa_keygen_bits:4096 -pkeyopt rsa_keygen_pubexp:65537
      $ # Build your cert template (Enter necessary details in the prompts that follow):
      $ openssl req -new -key custMpk.key -out cert.csr
      $ # Self-sign the certificate
      $ openssl x509 -req -days 3650 -in cert.csr -signkey custMpk.key -out custMpk.crt
