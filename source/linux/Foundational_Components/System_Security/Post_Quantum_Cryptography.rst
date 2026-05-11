.. _post_quantum_cryptography:

#########################
Post-quantum cryptography
#########################

************
Introduction
************

Post-Quantum Cryptography (PQC) refers to cryptographic algorithms built
to resist attacks by quantum computers. Classical asymmetric algorithms
such as RSA and Elliptic Curve Cryptography (ECC) are vulnerable to
polynomial-time quantum factoring algorithms running on a sufficiently
powerful quantum computer.

The National Institute of Standards and Technology (NIST) has standardized
three PQC algorithms:

- **Federal Information Processing Standards (FIPS) 203**: Module Lattice (ML)
  Key Encapsulation Mechanism (KEM) or ML-KEM, based on CRYSTALS-Kyber
- **FIPS 204**: Module Lattice (ML) Digital Signature Algorithm (DSA) or ML-DSA,
  based on CRYSTALS-Dilithium
- **FIPS 205**: Stateless Hash-Based (SLH) Digital Signature Algorithm (DSA) or SLH-DSA,
  based on SPHINCS+

The SDK includes **OpenSSL 3.5.x**, which provides native support for
all NIST-standardized PQC algorithms through its default provider. You do
not need external libraries or patches.

******************************
Verifying post-quantum support
******************************

To confirm the OpenSSL version and available PQC algorithms on the target board:

.. code-block:: console

   root@<machine>:~# openssl version
   OpenSSL 3.5.5 27 Jan 2026 (Library: OpenSSL 3.5.5 27 Jan 2026)

List supported KEM algorithms:

.. code-block:: console

   root@<machine>:~# openssl list -kem-algorithms | grep -i ml
     { 2.16.840.1.101.3.4.4.1, id-alg-ml-kem-512,  ML-KEM-512,  MLKEM512  } @ default
     { 2.16.840.1.101.3.4.4.2, id-alg-ml-kem-768,  ML-KEM-768,  MLKEM768  } @ default
     { 2.16.840.1.101.3.4.4.3, id-alg-ml-kem-1024, ML-KEM-1024, MLKEM1024 } @ default
     X25519MLKEM768    @ default
     X448MLKEM1024     @ default
     SecP256r1MLKEM768 @ default
     SecP384r1MLKEM1024 @ default

List supported signature algorithms:

.. code-block:: console

   root@<machine>:~# openssl list -signature-algorithms | grep -i -E 'ml-dsa|slh-dsa'
     { 2.16.840.1.101.3.4.3.17, id-ml-dsa-44, ML-DSA-44, MLDSA44 } @ default
     { 2.16.840.1.101.3.4.3.18, id-ml-dsa-65, ML-DSA-65, MLDSA65 } @ default
     { 2.16.840.1.101.3.4.3.19, id-ml-dsa-87, ML-DSA-87, MLDSA87 } @ default
     { 2.16.840.1.101.3.4.3.20, id-slh-dsa-sha2-128s,  SLH-DSA-SHA2-128s  } @ default
     { 2.16.840.1.101.3.4.3.21, id-slh-dsa-sha2-128f,  SLH-DSA-SHA2-128f  } @ default
     { 2.16.840.1.101.3.4.3.22, id-slh-dsa-sha2-192s,  SLH-DSA-SHA2-192s  } @ default
     { 2.16.840.1.101.3.4.3.23, id-slh-dsa-sha2-192f,  SLH-DSA-SHA2-192f  } @ default
     { 2.16.840.1.101.3.4.3.24, id-slh-dsa-sha2-256s,  SLH-DSA-SHA2-256s  } @ default
     { 2.16.840.1.101.3.4.3.25, id-slh-dsa-sha2-256f,  SLH-DSA-SHA2-256f  } @ default
     { 2.16.840.1.101.3.4.3.26, id-slh-dsa-shake-128s, SLH-DSA-SHAKE-128s } @ default
     { 2.16.840.1.101.3.4.3.27, id-slh-dsa-shake-128f, SLH-DSA-SHAKE-128f } @ default
     { 2.16.840.1.101.3.4.3.28, id-slh-dsa-shake-192s, SLH-DSA-SHAKE-192s } @ default
     { 2.16.840.1.101.3.4.3.29, id-slh-dsa-shake-192f, SLH-DSA-SHAKE-192f } @ default
     { 2.16.840.1.101.3.4.3.30, id-slh-dsa-shake-256s, SLH-DSA-SHAKE-256s } @ default
     { 2.16.840.1.101.3.4.3.31, id-slh-dsa-shake-256f, SLH-DSA-SHAKE-256f } @ default

********************
Supported algorithms
********************

Key encapsulation
=================

ML-KEM is a KEM used to securely establish a shared secret between two
parties. It replaces classical Elliptic Curve Diffie-Hellman (ECDH) or
RSA key exchange in protocols such as Transport Layer Security (TLS).

Security levels reference Advanced Encryption Standard (AES) bit
equivalence as a baseline:

+------------------+----------------------+----------------------------+
| Algorithm        | NIST Security Level  | Use Case                   |
+==================+======================+============================+
| ML-KEM-512       | Level 1 (~AES-128)   | Constrained environments   |
+------------------+----------------------+----------------------------+
| ML-KEM-768       | Level 3 (~AES-192)   | General purpose            |
+------------------+----------------------+----------------------------+
| ML-KEM-1024      | Level 5 (~AES-256)   | High-security applications |
+------------------+----------------------+----------------------------+

Hybrid KEM variants combine classical and PQC algorithms, providing
protection even if an attacker breaks one:

- ``X25519MLKEM768``: X25519 + ML-KEM-768 (recommended for TLS)
- ``X448MLKEM1024``: X448 + ML-KEM-1024
- ``SecP256r1MLKEM768``: ECDH P-256 + ML-KEM-768
- ``SecP384r1MLKEM1024``: ECDH P-384 + ML-KEM-1024

Digital signatures
==================

ML-DSA is a lattice-based DSA replacing classical RSA or Elliptic Curve
Digital Signature Algorithm (ECDSA) signatures.

+------------+----------------------+---------------------+
| Algorithm  | NIST Security Level  | Key Size (approx.)  |
+============+======================+=====================+
| ML-DSA-44  | Level 2              | ~1.3 KB             |
+------------+----------------------+---------------------+
| ML-DSA-65  | Level 3              | ~2.0 KB             |
+------------+----------------------+---------------------+
| ML-DSA-87  | Level 5              | ~2.6 KB             |
+------------+----------------------+---------------------+

Hash-based signatures
=====================

SLH-DSA is a stateless hash-based signature scheme with minimal security
assumptions (only hash function security). It is available in SHA-2 and
Secure Hash Algorithm-3 (SHA-3) extendable-output (SHAKE) variants, each
with small (``s``) and fast (``f``) tradeoffs:

- ``s`` variants: smaller signatures, slower signing
- ``f`` variants: larger signatures, faster signing

**************
Usage examples
**************

Generating keys and signing
===========================

Generate an ML-DSA key pair:

.. code-block:: console

   root@<machine>:~# openssl genpkey -algorithm ML-DSA-65 -out ml-dsa.key
   root@<machine>:~# openssl pkey -in ml-dsa.key -pubout -out ml-dsa.pub

Sign a file:

.. code-block:: console

   root@<machine>:~# echo "hello pqc" > file.txt
   root@<machine>:~# openssl pkeyutl -sign -inkey ml-dsa.key -in file.txt -out file.sig

Verify the signature:

.. code-block:: console

   root@<machine>:~# openssl pkeyutl -verify -pubin -inkey ml-dsa.pub -in file.txt -sigfile file.sig
   Signature Verified Successfully

Hash-based key signing
======================

.. code-block:: console

   root@<machine>:~# openssl genpkey -algorithm SLH-DSA-SHA2-128s -out slh-dsa.key
   root@<machine>:~# openssl pkeyutl -sign -inkey slh-dsa.key -in file.txt -out file.sig

Self-signed certificate
=======================

Generate a self-signed certificate with ML-DSA for testing:

.. code-block:: console

   root@<machine>:~# openssl req -x509 -newkey ml-dsa-65 \
       -keyout server.key -out server.crt \
       -days 365 -nodes -subj '/CN=my-device'

************************
Testing the key exchange
************************

ML-KEM is a KEM primitive. It does not have a standalone encrypt or decrypt
command. ML-KEM serves only as the key exchange mechanism inside a
TLS 1.3 handshake (replacing ECDH). Both client and server must advertise
the same group to negotiate it.

Generating a certificate
========================

The TLS server requires a certificate. Use ML-DSA for a fully PQC
setup:

.. code-block:: console

   root@<machine>:~# openssl req -x509 -newkey ml-dsa-65 \
       -keyout /tmp/server.key -out /tmp/server.crt \
       -days 1 -nodes -subj '/CN=test'

Starting the server
===================

.. code-block:: console

   root@<machine>:~# openssl s_server \
       -cert /tmp/server.crt \
       -key /tmp/server.key \
       -groups X25519MLKEM768 \
       -port 4433 -www &

Connecting the client
=====================

.. code-block:: console

   root@<machine>:~# openssl s_client \
       -connect localhost:4433 \
       -groups X25519MLKEM768 \
       </dev/null 2>&1 | grep -E 'group|Cipher|Protocol'

Expected output confirming ML-KEM negotiation:

.. code-block:: console

   Negotiated TLS1.3 group: X25519MLKEM768
   New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
   Protocol  : TLSv1.3

Handshake walkthrough
=====================

The verbose handshake (``-msg`` flag) reveals the full PQC key exchange flow:

.. code-block:: console

   root@<machine>:~# openssl s_client \
       -connect localhost:4433 \
       -groups X25519MLKEM768 \
       -msg </dev/null 2>&1

Annotated handshake sequence:

.. code-block:: text

   >>> ClientHello
       Client advertises X25519MLKEM768 in supported_groups + key_share.
       Sends its ML-KEM public key (encapsulation key) to the server.

   <<< ServerHello  [length ~0x4ba]
       Server selects X25519MLKEM768.
       Encapsulates using client's ML-KEM public key.
       Sends the ML-KEM ciphertext (~1200 bytes) back. This is the
       key encapsulation happening over the wire.

   <<< Certificate
       Server's certificate using ML-DSA-65 signature (15616-bit key).

   <<< CertificateVerify
       Proves server holds the private key, signed with ML-DSA-65.

   <<< Finished  /  >>> Finished
       Both sides confirm the handshake using the derived shared secret.

   Negotiated TLS1.3 group: X25519MLKEM768
   Protocol  : TLSv1.3
   Cipher    : TLS_AES_256_GCM_SHA384

The full session uses PQC at every asymmetric operation. Bulk encryption
uses AES-256 in Galois Counter Mode (GCM):

+---------------------+-------------------+-------------------------------+
| TLS Role            | Algorithm         | Standard                      |
+=====================+===================+===============================+
| Key exchange        | X25519MLKEM768    | Hybrid (classical + FIPS 203) |
+---------------------+-------------------+-------------------------------+
| Server certificate  | ML-DSA-65         | FIPS 204                      |
+---------------------+-------------------+-------------------------------+
| Bulk encryption     | AES-256-GCM       | Symmetric (not PQC-relevant)  |
+---------------------+-------------------+-------------------------------+

.. note::

   The ``X25519MLKEM768`` hybrid is the recommended choice for TLS. It
   provides classical security from X25519 in addition to PQC security
   from ML-KEM-768. If either algorithm is ever broken, the other still
   protects the session.

*****
Notes
*****

- ML-KEM requires TLS 1.3. You cannot use it with TLS 1.2 or earlier.
- SLH-DSA signatures are large (8-50 KB depending on variant). Use ML-DSA
  for TLS certificates where size matters.
- All algorithms above are available in the OpenSSL ``default`` provider.
  You do not need additional provider configuration.

********
See also
********

- `OpenSSL 3.5 release notes <https://www.openssl.org/news/openssl-3.5-notes.html>`_
- `openssl-genpkey(1): ML-DSA and ML-KEM key generation options <https://docs.openssl.org/3.5/man1/openssl-genpkey/>`_
- `openssl-pkeyutl(1): ML-DSA, ML-KEM, and SLH-DSA algorithm sections <https://docs.openssl.org/3.5/man1/openssl-pkeyutl/>`_
- `openssl-s_client(1) <https://docs.openssl.org/3.5/man1/openssl-s_client/>`_
- `openssl-s_server(1) <https://docs.openssl.org/3.5/man1/openssl-s_server/>`_
- `EVP_PKEY-ML-KEM(7) <https://docs.openssl.org/3.5/man7/EVP_PKEY-ML-KEM/>`_
- `EVP_PKEY-ML-DSA(7) <https://docs.openssl.org/3.5/man7/EVP_PKEY-ML-DSA/>`_
- `EVP_PKEY-SLH-DSA(7) <https://docs.openssl.org/3.5/man7/EVP_PKEY-SLH-DSA/>`_
