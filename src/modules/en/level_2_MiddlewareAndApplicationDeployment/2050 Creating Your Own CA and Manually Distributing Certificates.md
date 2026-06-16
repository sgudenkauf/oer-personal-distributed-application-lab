---
title: "Creating a Custom CA (Certificate Authority) and Manually Distributing Certificates" 
author: ["Gudenkauf, Prof Stefan", "Uwe, Bachmann", "Ronald, Kalk"]
email: "pdal@jade-hs.de"
organization: "PDAL Project, Jade Hochschule" 
date: "2025-11-06" 
version: "1.0.0" 
level: "Level 2, Learning Unit 2.1" 
duration: "2h" 
prerequisites: "Tiny- PC with Proxmox installed and at least one LXC container" 
tags: ["Proxmox", "Linux", "Virtualization", "Middleware", "Certificates", "Certificate Authority"] 
license: "CC BY-SA 4.0"
---

# Creating a Custom CA (Certificate Authority) and Manually Distributing Certificates

## What is this about?

Why do we need certificates in IT?

In IT, certificates are used to uniquely and reliably prove the identity of devices, services, or individuals. They also enable encrypted and secure communication over networks, such as via HTTPS or VPN.
Even in a closed network, you should use your own certificates. Since public Certificate Authorities (CAs) do not have access to internal systems, we need our own CA.

Custom certificates enable encrypted and authenticated communication via protocols like HTTPS, SMTPS, LDAPS, FTPS, as well as for databases like MariaDB, PostgreSQL, and message brokers like MQTT or Kafka. This allows you to retain full control over security, validity, and distribution of certificates within the network.
**Certificates created locally in the application container vs. a custom CA (Certificate Authority)**.
It is possible to create custom certificates in every application container (LXC) – but we have decided against it. We are setting up our own CA to minimize the complexity of distributing individual certificates. A custom CA provides us with unified, centrally managed certificates.

This guide shows you how to use **OpenSSL** on your server `ssl-ca140` (IP: 192.168.137.140) to create your own **Certificate Authority (CA)** and a **single certificate for all services**. The certificates are then manually distributed to the various services and client computers (Windows, Mac, Linux).

-----

## Why a Single Certificate — and Why Multiple?

  * **A single certificate (SAN Certificate)** is practical:
    You only need one file that is valid for all your services.
    This saves effort and is often sufficient for small or test environments.
  * **Multiple certificates (recommended for production):**
    Each service receives its own certificate, which improves security, as only that service is affected if compromised.
    Management (renewal, revocation) also becomes more flexible this way, but is significantly more complex or must be automated.

-----

### Prerequisites

  * An LXC container `ssl-ca140` with OpenSSL installed
  * Familiarity with basic Linux commands
  * SSH access to the server

```bash
sudo apt install openssl
```

---

Create a new user `pdal` with sudo rights.
Switch the user to `pdal` with `su pdal`.

### 1\. Create Folder Structure

```bash
sudo mkdir -p ~/myCA/{certs,crl,newcerts,private}
sudo chmod 700 ~/myCA/private
sudo touch ~/myCA/index.txt
echo 1000 | sudo tee ~/myCA/serial
```

![MkdirMycaCTConsole](./2050attachments/MkdirMycaCTConsole.png)
![Chmod700MycaPrivateCTConsole](./2050attachments/Chmod700MycaPrivateCTConsole.png)
![TouchIndexCTConsole](./2050attachments/TouchIndexCTConsole.png)
![CreateSerial1000](./2050attachments/CreateSerial1000CTConsole.png)

## 2\. Create CA (Certificate Authority)

### 2.1 Create OpenSSL configuration file openssl.cnf

In the folder `~/myCA`, create the file `openssl.cnf` with the following content (simplified example):

```bash
sudo nano ~/myCA/openssl.cnf
```

```bash
[ ca ]
default_ca = CA_default

[ CA_default ]
dir               = /home/pdal/myCA
certs             = $dir/certs
crl_dir           = $dir/crl
new_certs_dir     = $dir/newcerts
database          = $dir/index.txt
serial            = $dir/serial
RANDFILE          = $dir/private/.rand

private_key       = $dir/private/ca.key.pem
certificate       = $dir/certs/ca.cert.pem

default_days      = 3650
default_crl_days  = 30
default_md        = sha256

policy            = policy_loose

[ policy_loose ]
countryName             = optional
stateOrProvinceName     = optional
localityName            = optional
organizationName        = optional
organizationalUnitName  = optional
commonName              = supplied
emailAddress            = optional

[ req ]
default_bits       = 4096
distinguished_name = req_distinguished_name
string_mask        = utf8only

[ req_distinguished_name ]
countryName                     = Country Name (2 letter code)
stateOrProvinceName             = State or Province Name
localityName                    = Locality Name
organizationName                = Organization Name
organizationalUnitName          = Organizational Unit Name
commonName                      = Common Name
emailAddress                    = Email Address

[ v3_ca ]
subjectKeyIdentifier=hash
authorityKeyIdentifier=keyid:always,issuer
basicConstraints = critical, CA:true
keyUsage = critical, digitalSignature, cRLSign, keyCertSign

[ v3_server ]
basicConstraints = CA:FALSE
keyUsage = digitalSignature, keyEncipherment
extendedKeyUsage = serverAuth
subjectAltName = @alt_names

[ alt_names ]
DNS.1 = apache.local
IP.1 = 192.168.137.101
DNS.2 = mariadb.local
IP.2 = 192.168.137.120
DNS.3 = pgadmin4.local
IP.3 = 192.168.137.130
DNS.4 = CA-ssl.local
IP.4 = 192.168.137.140
DNS.5 = kafka.local
IP.5 = 192.168.137.150
DNS.6 = postgresql.local
IP.6 = 192.168.137.160
DNS.7 = mqtt.local
IP.7 =192.168.137.170
```

![OpensslCNF01](./2050attachments/OpensslCNF01.png)
![OpensslCNF02](./2050attachments/OpensslCNF02.png)
![OpensslCNF03](./2050attachments/OpensslCNF03.png)

> Hint: Adjust paths and names as needed. Replace `/home/username` with your actual path.

**Explanation of the Configuration File:**

#### [ ca ]

```bash
default_ca = CA_default
```

Defines which CA configuration is used.

**CA\_default** refers to the following section [ CA\_default ].

#### [ CA\_default ]

```bash
dir               = /home/pdal/myCA
```

'$dir' is the root directory of your CA files (Adjust 'username' to your username).

All subsequent paths are built upon this.

```bash
certs             = $dir/certs
crl_dir           = $dir/crl
new_certs_dir     = $dir/newcerts
database          = $dir/index.txt
serial            = $dir/serial
RANDFILE          = $dir/private/.rand
```

**certs**: Stores issued certificates

**crl\_dir**: For revoked certificates (Certificate Revocation Lists)

**new\_certs\_dir**: Internal folder for new certificates

**database**: File where OpenSSL documents the issued certificates

**serial**: File with the current serial number

**RANDFILE**: Helper file for random data (e.g., during key generation)

```bash
private_key       = $dir/private/ca.key.pem
certificate       = $dir/certs/ca.cert.pem
```

Storage locations of the CA key and CA certificate

```bash
default_days      = 3650
default_crl_days  = 30
default_md        = sha256
```

**default\_days**: Validity period of a new certificate (here: 10 years)

**default\_crl\_days**: How long a revocation list is valid

**default\_md**: Hash algorithm (here: sha256, more secure than e.g., md5)

```bash
policy            = policy_loose
```

Defines how strictly OpenSSL checks the entered fields (e.g., whether country or organization is mandatory)

#### [ policy_loose ]

```bash
countryName             = optional
stateOrProvinceName     = optional
localityName            = optional
organizationName        = optional
organizationalUnitName  = optional
commonName              = supplied
emailAddress            = optional
```

This is a loose policy: most fields are optional, only 'commonName' (the server name like 'apache.local') must be provided.

#### [ req ]

```bash
default_bits       = 4096
distinguished_name = req_distinguished_name
string_mask        = utf8only
```

Configuration for new Certificate Signing Requests (CSRs).

**default\_bits**: Key length in bits (the more, the more secure – 4096 is strong).

**distinguished\_name**: Which fields are queried during the CSR.

**string\_mask = utf8only**: Only UTF-8 characters allowed.

#### [ req\_distinguished\_name ]

```bash
countryName            = Country Name (2 letter code)
stateOrProvinceName    = State or Province Name
...
```

This defines which fields are queried when creating a certificate (e.g., Country, Organization, Common Name).

#### [ v3_ca ]

```bash
subjectKeyIdentifier=hash
authorityKeyIdentifier=keyid:always,issuer
basicConstraints = critical, CA:true
keyUsage = critical, digitalSignature, cRLSign, keyCertSign
```

Extensions for CA Certificates

**basicConstraints = CA:true**: Clarifies that this certificate is allowed to issue certificates.

**keyUsage**: Which actions are allowed with the key.

#### [ v3_server ]

```bash
basicConstraints = CA:FALSE
keyUsage = digitalSignature, keyEncipherment
extendedKeyUsage = serverAuth
subjectAltName = @alt_names
```

Extensions for Server Certificates:

  * **CA:FALSE**: This certificate is not a CA certificate,
  * **keyUsage**: For digital signature and encryption,
  * **extendedKeyUsage**: May be used as a TLS server certificate.
  * **subjectAltName**: Refers to the list of alternative names below.

#### [ alt_names ]

```bash
DNS.1 = apache.local
IP.1 = 192.168.137.101
DNS.2 = mariadb.local
IP.2 = 192.168.137.120
DNS.3 = pgadmin4.local
IP.3 = 192.168.137.130
DNS.4 = CA-ssl.local
IP.4 = 192.168.137.140
DNS.5 = kafka.local
IP.5 = 192.168.137.150
DNS.6 = postgresql.local
IP.6 = 192.168.137.160
DNS.7 = mqtt.local
IP.7 =192.168.137.170
```

This is the SAN list (Subject Alternative Name).

It allows the certificate to secure multiple names and IP addresses,
e.g., `apache.local` for Apache, `mariadb.local` for MariaDB, etc.

This means only a single certificate is needed for all services – this is the so-called pdal certificate.

### Conclusion

This configuration defines a custom CA with:

> loose input requirements,
>
> strong key (4096 bit),
>
> SAN support for many services,
>
> 1 certificate for all servers (pdal certificate).

### 2.2 Create CA Key and CA Certificate

Go to the `~/myCA` folder with the command `cd ~/myCA/`.

```bash
sudo openssl genrsa -aes256 -out private/ca.key.pem 4096
```

![OpensslGenRsaCTConsole01](./2050attachments/OpensslGenRsaCTConsole01.png)

You enter a password for confirmation. We choose `JadeHS20` in our example, after which you have to confirm the password again.

![OpensslGenRsaCTConsole02](./2050attachments/OpensslGenRsaCTConsole02.png)

```bash
sudo chmod 400 private/ca.key.pem
```

![Chmod400cakeypem](./2050attachments/Chmod400cakeypem.png)

```bash
sudo openssl req -config openssl.cnf \
      -key private/ca.key.pem \
      -new -x509 -days 3650 -sha256 -extensions v3_ca \
      -out certs/ca.cert.pem
```

You will be asked for details like country, organization, etc. You **must** fill these in appropriately.

![CreateCaCertPemCTConsole](./2050attachments/CreateCaCertPemCTConsole.png)

## 3. Create Server Certificate with SAN (for all services)

### 3.1 Create Private Key for Server

```bash
sudo openssl genrsa -out private/server.key.pem 2048
sudo chmod 400 private/server.key.pem
```

![CreateServerKeyPemCTConsole](./2050attachments/CreateServerKeyPemCTConsole.png)

### 3.2 Create Certificate Signing Request (CSR) with SAN


**Create the CSR (Certificate Signing Request):**

What is a CSR?

A CSR is a file that:

  - contains a public key,
  - was created along with identity information (e.g., Common Name, Organization, Location, SANs),
  - is intended to be signed by a Certificate Authority (CA) to generate a valid certificate.

<!-- end list -->

```bash
sudo openssl req \
  -new \
  -key private/server.key.pem \
  -out server.csr.pem \
  -config ~/myCA/openssl.cnf \
  -subj "/C=DE/ST=Niedersachsen/L=Wilhelmshaven/O=Jade-Hochschule/OU=FB-MIT/CN=all-services.local"
```

![CertificateSigningRequestCaCTConsole](./2050attachments/CertificateSigningRequestCaCTConsole.png)

Afterward, you can check if the key was actually created with the following command:

```bash
ls -l server.csr.pem
openssl req -in server.csr.pem -noout -text
```

![CheckCsrRightCACTConsole](./2050attachments/CheckCsrRightCACTConsole.png)
![CheckCsrRightCACTConsole02](./2050attachments/CheckCsrRightCACTConsole02.png)

### 3.3 Sign Certificate with SAN

```bash
sudo openssl ca -config openssl.cnf -extensions v3_server -days 825 -notext -md sha256 -in server.csr.pem -out certs/server.cert.pem
```

You will be asked if you want to sign the certificate – confirm with y.
Then you must confirm once more with y for the certificate to be created and written to the database.

![ZertifikatsSignierungCACTConsole](./2050attachments/ZertifikatsSignierungCACTConsole.png)

Afterward, you must set the permissions on the certificate.

```bash
sudo chmod 444 certs/server.cert.pem
```

![Chmod444Server.Cert.PemCACTConsole](./2050attachments/Chmod444Server.Cert.PemCACTConsole.png)

## 4. Distribute and Configure Certificates to Services

The certificate `server.cert.pem`, the key `server.key.pem`, and the CA certificate `ca.cert.pem` are needed on all servers/services.

### 🔐 Goal

We want to:

  * Copy the files `ca.cert.pem`, `server.cert.pem`, and `server.key.pem` in the CA container to `/home/pdal/download`.
  * Download these files to your local computer in `C:\tmp` using WinSCP via SFTP.
  * Upload the files later to the Apache2 container to `/home/pdal/download` using WinSCP via SFTP. (This will be explained in a separate document.)
  * Move the files from there into the corresponding directories, e.g., in the Apache2 container.

### 📁 Prerequisites

  * LXC container for CA (ca-container) is active.
  * User `pdal` exists.
  * SFTP access via IP or hostname is possible.
  * SFTP client such as WinSCP is installed on your Windows computer (but also works without a separate client via the command line).

🔹 1. Prepare files in the CA container

### Create Download Directory

We first create a directory named `download` in the home directory of the user `pdal` in the CA container.

```bash
sudo mkdir -p /home/pdal/download
```

![MkdirHomePdalDownloadCAConsole.png](./2050attachments/MkdirHomePdalDownloadCAConsole.png)

### Adjust Paths, if necessary

Now we copy the individual certificates and the server key into the download directory.
Since the `/home/pdal/myca/private` directory belongs to root and only root is allowed to access this directory, we must later log in to the container as `root`.
We do this as follows. We are currently logged in as `pdal` and must enter `sudo -i` to switch to the user `root` to gain access to the private directory.

```bash
sudo cp /home/pdal/myCA/certs/ca.cert.pem /home/pdal/download/
sudo cp /home/pdal/myCA/certs/server.cert.pem /home/pdal/download/
sudo -i
cp /home/pdal/myCA/private/server.key.pem /home/pdal/download/
```

This follows the syntax `sudo cp theFileToCopyWithPath theTargetDirectory`.

![CpCertsDownloadCaConsole](./2050attachments/CPCertsDownloadCaConsole.png)

### Adjust Permissions (optional, so that user pdal has access)

We are still in the container as root. If not, please switch to the root level with `sudo -i`.

The files just copied all belong to the user Root and have very strict permissions. To be able to download these files via an SFTP client, we must change the permissions and also the owner of the files. We do this with the `chown` command and the `chmod` command.

![CertsDownloadPermissionCaConsole](./2050attachments/CertsDownloadPermissionsCaConsole.png)

```bash
chown pdal:pdal /home/pdal/download/*.pem
chmod 600 /home/pdal/download/*.pem
```

![CertsDownloadPermissionChangedCaConsole](./2050attachments/CertsDownloadPermissionsChangedCaConsole.png)

🔹 2. Download files from the CA container via SFTP using WinSCP.
Steps:

  * Start WinSCP.
  * Open a new SFTP session:
      * Host: IP of your CA container
      * User: `pdal`
      * Password: Password
  * Navigate in the right window (Remote Browser) to:

<!-- end list -->

```bash
/home/pdal/download/
```

  * Select the files `ca.cert.pem`, `server.cert.pem`, `server.key.pem`.
  * Drag them to the local directory on your PC:

`C:\tmp`
![WinSCPCertsDownloadCtempCA](./2050attachments/WinSCPCertsDownloadCtempCA.png)

It also works completely without extra apps like WinSCP. Starting with Windows 10/11, I have the option to download the files via the command prompt using the `scp` command. Here are the individual steps on how this works.
We open the command prompt on our Windows client as Administrator.

```bash
scp pdal@192.168.137.140:/home/pdal/download/*.pem C:\tmp\
```

![SCPCertsDownladCAConsole](./2050attachments/SCPCertsDownloadCAConsole.png)

Here we are asked if we want to continue the connection because the host is not recognized.
We must confirm with `yes`. 
The 3 files are now in the `tmp` directory under `C:`.

🔹 3. Upload files to the Apache2 container via SFTP.

In WinSCP, open a new SFTP session to the Apache2 container:

  * Host: `192.168.137.101`
  * User: `pdal`
  * Password: `JadeHS20`

Navigate in the Remote Browser to the destination:

```bash
/home/pdal/download/
```

Drag the three `.pem` files from the local window (`C:\tmp`) into it.

![WinSCPCertsUploadHomePdalDownloadApache202](./2050attachments/WinSCPCertsUploadHomePdalDownloadApache202.png)

## 5\. Install Certificate on Windows, Mac, Linux

Import the CA certificate (`ca.cert.pem`) as a trusted root certificate authority in the respective operating systems. We do this so that browsers or other tools can establish a secure connection without certificate errors.

This way, your clients will recognize all certificates originating from your CA as trustworthy.

![ICSBenutzerZertifikatsVerwaltung01](./2050attachments/ICSBenutzerZertifikatsVerwaltung01.png)
![CertMngrTrustedCerts](./2050attachments/CertMngrTrustedCerts.png)
![CertMngrTrustedCerts02](./2050attachments/CertMngrTrustedCerts02.png)
![CertMngrTrustedCertsImport01](./2050attachments/CertMngrTrustedCertsImport01.png)
![CertMngrTrustedCertsImport02](./2050attachments/CertMngrTrustedCertsImport02.png)
![CertMngrTrustedCertsImport03](./2050attachments/CertMngrTrustedCertsImport03.png)
![CertMngrTrustedCertsImport04](./2050attachments/CertMngrTrustedCertsImport04.png)
![CertMngrTrustedCertsImport05](./2050attachments/CertMngrTrustedCertsImport05.png)
![CertMngrTrustedCertsImport06](./2050attachments/CertMngrTrustedCertsImport06.png)
![CertMngrTrustedCertsImport07](./2050attachments/CertMngrTrustedCertsImport07.png)
![CertMngrTrustedCertsImport08](./2050attachments/CertMngrTrustedCertsImport08.png)

## 6. Summary and Recommendations

A SAN certificate for all services is quick and easy for small environments.

For production and greater security: Create a separate certificate for each service (with its own CSR and signing).

Always keep private keys secure\!

Distribute the CA certificate to all clients so that TLS connections are recognized as secure.

## Sources

  * "Own certificates with openssl — Linux and Open Source". Accessed: August 26, 2025. \[Online]. Available at: [OpenSSL Basic Knowledge](https://www.grund-wissen.de/linux/server/openssl.html)
  * "CA › Wiki › ubuntuusers.de". Accessed: August 26, 2025. \[Online]. Available at: [CA Wiki Ubuntuusers](https://wiki.ubuntuusers.de/CA/)

-----

### License

This work is licensed under the **Creative Commons Attribution-ShareAlike 4.0 International License**.

[To the license text on the Creative Commons website](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)
