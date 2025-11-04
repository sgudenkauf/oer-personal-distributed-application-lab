---
title: "Questions on Certificates and a Custom CA"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "uwe.bachmann@jade-hs.de"
organization: "PDAL Project"
date: "2025-09-24"
version: "1.0.0"
level: "Level 2, Learning Unit 1.05, Assessment"
duration: "0.2 Hrs"
prerequisites:["Completed - Document: 2050 - Creating a Custom CA (Certificate Authority) and Manually Distributing Certificates"]
tags: ["PDAL","Assessment"]
license: "CC BY-SA 4.0"
---

### 10 Questions on Certificates and a Custom CA

1. **Why are certificates needed even in a closed internal network?**
    * A) They are legally required for data storage.
        * *Explanation*: This is incorrect. The use of certificates is not a general legal requirement but serves to ensure security and trustworthiness.
    * B) Public Certificate Authorities (CAs) can issue certificates for internal systems.
        * *Explanation*: This is incorrect. Public CAs don't have access to internal networks and therefore can't issue certificates for internal services.
    * C) External firewalls need them for packet filtering.
        * *Explanation*: This is incorrect. Certificates are used for the authentication and encryption of data traffic, not for basic packet filtering by firewalls.
    * **D) They enable encrypted and authenticated communication between internal services.**
        * *Explanation*: This is correct. Certificates ensure that communication between internal services is secure and trustworthy.
    * E) They are exclusively for identifying users, not devices.
        * *Explanation*: This is incorrect. Certificates are used to identify devices, services, and individuals.

2. **Which tool is used in the guide to create the custom Certificate Authority (CA)?**
    * A) `certbot`
        * *Explanation*: `Certbot` is typically used to obtain and manage certificates from the public Certificate Authority Let's Encrypt.
    * B) `keytool`
        * *Explanation*: `keytool` is a Java utility used to manage key stores.
    * C) `gnupg`
        * *Explanation*: `gnupg` (`Gnu Privacy Guard`) is primarily used for the encryption and signing of emails and files.
    * **D) `OpenSSL`**
        * *Explanation*: `OpenSSL` is the standard command-line tool used in this guide for creating certificates and a CA.
    * E) `ssh-keygen`
        * *Explanation*: `ssh-keygen` is used to create SSH key pairs for secure logins to servers.

3. **What is the main advantage of a single SAN certificate compared to multiple individual certificates for each service?**
    * **A) It simplifies management, as only a single certificate file is needed for all services.**
        * *Explanation*: This is correct. A SAN certificate secures multiple domains and IPs, which minimizes management effort in small environments.
    * B) It offers higher security, as not all services are affected in the event of a compromise.
        * *Explanation*: This is incorrect. The opposite is true: if a single SAN certificate is compromised, all secured services are at risk.
    * C) It speeds up network communication.
        * *Explanation*: This is incorrect. The type of certificate doesn't have a significant impact on network communication speed.
    * D) It renews automatically without manual intervention.
        * *Explanation*: This is incorrect. The renewal of a self-issued certificate must be done manually or via scripts.
    * E) It is mandatory for public websites.
        * *Explanation*: This is incorrect. Public websites require certificates from public CAs like Let's Encrypt or DigiCert.

4. **What is the purpose of the `index.txt` file in the CA structure?**
    * A) It stores the passwords of all issued certificates.
        * *Explanation*: This is incorrect. Passwords should never be stored unencrypted in a file.
    * B) It contains the root certificates of all trusted CAs.
        * *Explanation*: This is incorrect. The file is created by your own CA and does not contain external root certificates.
    * **C) It serves as a database where OpenSSL documents the issued certificates.**
        * *Explanation*: This is correct. OpenSSL uses this file to manage issued certificates and their status.
    * D) It stores temporary data for key generation.
        * *Explanation*: This is incorrect. Temporary data is stored in the `RANDFILE`.
    * E) It is a simple log file that is manually filled by the administrator.
        * *Explanation*: This is incorrect. The file is automatically updated by OpenSSL and serves as a database.

5. **What does `default_days = 3650` in the `openssl.cnf` configuration file mean?**
    * A) The CA must be renewed every 3650 days.
        * *Explanation*: This is incorrect. This is the default validity period for new certificates, not for the CA itself.
    * B) The Certificate Revocation List (CRL) is updated every 3650 days.
        * *Explanation*: This is incorrect. The validity of the CRL is determined by `default_crl_days`.
    * C) The maximum key length is 3650 bits.
        * *Explanation*: This is incorrect. The key length is defined by `default_bits`.
    * **D) The validity period of a newly issued certificate is 10 years.**
        * *Explanation*: This is correct. 3650 days corresponds to 10 years, which is the default validity period for new certificates.
    * E) The certificate is automatically revoked after 3650 days.
        * *Explanation*: This is incorrect. A revocation is done manually.

6. **Which property in `openssl.cnf` indicates that a certificate is allowed to function as a Certificate Authority?**
    * A) `keyUsage = keyCertSign`
        * *Explanation*: This is incorrect. `keyCertSign` alone is not sufficient; it must be used in the `v3_ca` section together with `basicConstraints`.
    * B) `extendedKeyUsage = serverAuth`
        * *Explanation*: This is incorrect. `serverAuth` specifies that a certificate may be used for a server, not as a CA.
    * C) `subjectKeyIdentifier=hash`
        * *Explanation*: This is incorrect. This option identifies the public key of the certificate.
    * **D) `basicConstraints = critical, CA:true`**
        * *Explanation*: This is correct. This option in the `v3_ca` section is essential to mark a certificate as a CA.
    * E) `policy = policy_loose`
        * *Explanation*: This is incorrect. The policy determines which fields are mandatory when entering data.

7. **Why are the permissions of the private CA key (`ca.key.pem`) set to `400`?**
    * A) To allow everyone to read and execute the certificate.
        * *Explanation*: This is incorrect. The `400` permission only allows the owner to read the file.
    * B) To copy the file from the CA to the web server container.
        * *Explanation*: This is incorrect. The permissions are for security, not for the copying process.
    * C) To grant read permissions to the Apache2 web server.
        * *Explanation*: This is incorrect. The Apache web server doesn't need read permissions for the private CA key.
    * **D) To ensure that only the owner can read the file.**
        * *Explanation*: This is correct. The CA's private key is the most important and sensitive asset. The `400` permission ensures that only the owner can access it.
    * E) To reduce the file size.
        * *Explanation*: This is incorrect. Permissions have no effect on file size.

8. **What is a `Certificate Signing Request` (CSR)?**
    * A) A file that contains the private key of the CA and is used for signing.
        * *Explanation*: This is incorrect. A CSR contains a public key and identity information. The private key remains on the device.
    * **B) A file with a public key and identity information that must be signed by a CA.**
        * *Explanation*: This is correct. The CSR is the request you send to a CA to obtain a valid certificate.
    * C) The final certificate signed by the CA.
        * *Explanation*: This is incorrect. The CSR is just the request; the final certificate is the response from the CA.
    * D) A temporary password used during certificate creation.
        * *Explanation*: This is incorrect. A CSR is a file with key and identity information.
    * E) A command to check the validity of a certificate.
        * *Explanation*: This is incorrect. A command for checking validity is, for example, `openssl x509 -in file.pem -text`.

9. **Which files must be transferred from the CA to a client (e.g., the Apache2 container) to enable a secure TLS connection?**
    * A) `ca.cert.pem` and `server.key.pem`
        * *Explanation*: This is incorrect. The `server.cert.pem` certificate is missing.
    * B) Only `server.cert.pem` and `server.key.pem`
        * *Explanation*: This is incorrect. Without the `ca.cert.pem` certificate, the client cannot trust the server certificate.
    * C) Only the CA root certificate (`ca.cert.pem`)
        * *Explanation*: This is incorrect. The client needs the server certificate and the server's private key to establish a connection.
    * D) Only the private key (`server.key.pem`)
        * *Explanation*: This is incorrect. The private key alone is useless without the corresponding certificate.
    * **E) `ca.cert.pem`, `server.cert.pem`, and `server.key.pem`**
        * *Explanation*: This is correct. The client needs the CA certificate to trust the server, and the server needs its own certificate and private key.

10. **Why must the CA certificate (`ca.cert.pem`) be imported onto a client machine?**
    * A) To verify the validity of public certificates (e.g., from Google).
        * *Explanation*: This is incorrect. The client relies on pre-installed root certificates for this.
    * B) To allow the client to create its own certificates.
        * *Explanation*: This is incorrect. The CA certificate doesn't enable certificate creation; it only establishes trust.
    * **C) So the client trusts the server certificate issued by the custom CA.**
        * *Explanation*: This is correct. By importing the CA certificate, the operating system trusts all certificates signed by that CA.
    * D) To speed up the network connection.
        * *Explanation*: This is incorrect. The import has no effect on speed.
    * E) To transfer the server's private key to the client.
        * *Explanation*: This is incorrect. Private keys should never be transferred from a server or imported onto clients.


---

### License
This work is licensed under the **Creative Commons Attribution - ShareAlike 4.0 International License**.
 
[To the license text on the Creative Commons website](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en)
