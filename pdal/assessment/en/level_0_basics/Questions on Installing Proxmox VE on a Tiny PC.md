---
title: "Test - Questions on the Fundamentals of ICS Configuration"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe"]
email: "pdal@jade-hs.de"
organization: "PDAL Project"
date: "2025-08-20"
version: "1.0.0"
level: "Level 0, Learning Unit 0.1, Assessment"
duration: "0.5 Hrs"
prerequisites:["Completed - Document: 0250 Installing Proxmox VE on a Tiny PC"]
tags: ["PDAL", "Assessment"]
license: "CC BY-SA 4.0"
---

### Test - Questions on Installing Proxmox VE on a Tiny PC

1.  **What action is required to start the installation of Proxmox VE from a USB stick?**
    * A) Copy the Proxmox ISO image to the Tiny PC's hard drive.
      *Note: This is a bit difficult without an operating system.*
    * **B) Set the USB stick as the primary boot medium in the BIOS/UEFI or open the boot menu.**
      *Note: The boot menu lists the order of media for the startup process. The USB stick should be started first in the order.*
    * C) Format the USB stick with the `root` password.
      *Note: The 'root' password is set during the installation process.*
    * D) Transfer the ISO image to the Tiny PC using WinSCP.
      *Note: The system has no operating system before installation and therefore no network connection.*

2.  **According to the document, a static IP address should be assigned for the network configuration. What is the main reason for this?**
    * A) To improve the performance of the virtual machines.
      *Note: The performance of a virtual machine is generally unrelated to the network connection.*
    * B) To prevent other devices from accessing the Proxmox web interface.
      *Note: This is not prevented by a static IP address.*
    * C) To speed up name resolution on the internet.
      *Note: Our local network is not accessible on the general internet.*
    * **D) To ensure that the host is reachable at the same address, which is important for server services.**
      *Note: If you were to use DHCP for network configuration, it is not guaranteed that the host will always get the same IP address. This can lead to major problems in application development.*

3.  **According to the document, which of the following IP addresses is used to ping the Windows computer with active ICS function to check network connectivity?**
    * A) `192.168.1.1`
      *Note: This is an IP address in a local network - but not ours.*
    * B) `8.8.8.8`
      *Note: This is the IP address of the Google DNS server.*
    * **C) `192.168.137.1`**
      *Note: This is the correct address for our ICS adapter.*
    * D) `127.0.0.1`
      *Note: This is the "localhost" address that every PC can use to call itself.*

4.  **According to the document, which configuration file needs to be edited to switch the Chrony time server to `time.jade-hs.de`?**
    * A) `/etc/ntp.conf`
      *Note: This is the configuration file for the Network Time Protocol (NTP) daemon.*
    * **B) `/etc/chrony/chrony.conf`**
      *Note: This is the configuration file under Debian; our Proxmox installation.*
    * C) `/etc/timesyncd.conf`
      *Note: This is the configuration file for time synchronization under Ubuntu.*
    * D) `/etc/network/interfaces`
      *Note: This is the network configuration under Debian.*

5.  **According to the document, why is a certificate warning displayed when you first access the Proxmox web interface?**
    * A) Because the browser does not support HSTS (HTTP Strict Transport Security) for the IP address.
      *Note: HSTS is a security mechanism for HTTPS connections.*
    * **B) Because Proxmox uses a self-signed Root CA certificate that the browser does not trust.**
      *Note: Our system does not yet know the certificates from Proxmox; therefore, they are not trustworthy at first.*
    * C) Because the NTP service has not yet synchronized correctly.
      *Note: The NTP service has nothing directly to do with this.*
    * D) Because the password for the `root` user is too weak.
      *Note: The password has nothing to do with the certificates.*

6.  **What is the main function of Proxmox VE, as described in the document?**
    * A) It is an operating system for desktop PCs.
      *Note: Proxmox is intended for servers, not desktops.*
    * B) It is software for creating documents.
      *Note: This is application software.*
    * **C) It is a virtualization host that hosts VMs and containers.**
      *Note: The main task of a hypervisor like Proxmox is to manage virtual environments.*
    * D) It is a network monitoring tool.
      *Note: This is specialized network software.*
    * E) It is a firewall solution.
      *Note: Proxmox does have firewall functions, but this is not its main function.*

7.  **Why does the document recommend importing the Proxmox CA certificate into the client browser?**
    * A) To increase the speed of the network connection.
      *Note: Certificate installation has no effect on speed.*
    * B) To update the Proxmox system.
      *Note: Updates are made via the package manager.*
    * C) To customize the Proxmox user interface.
      *Note: This is a setting in the web interface.*
    * **D) To suppress the browser's security warning and establish a trusted HTTPS connection.**
      *Note: The certificate makes the connection from the browser to the server recognizable as secure and trustworthy.*
    * E) To configure a static IP address.
      *Note: This is a network setting on the Proxmox host.*

8.  **The installation is configured with the static IP address 192.168.137.xxx/24. What does the /24 notation in this address represent?**
    * A) The version of the IP protocol.
      *Note: This has nothing to do with the IP version.*
    * B) The number of hosts available on the network.
      *Note: This is the number of subnet mask bits.*
    * C) The port on which the web server is running.
      *Note: Ports are configured separately.*
    * D) The maximum bandwidth of the network connection.
      *Note: Bandwidth is a hardware property.*
    * **E) The subnet mask, which provides 24 bits for the network and 8 bits for hosts.**
      *Note: The /24 notation is a CIDR notation and means that the first 24 bits are the network ID.*

9.  **What is the main reason for using Rufus or Balena Etcher to write the ISO image to a USB stick?**
    * A) To reduce the file size of the ISO image.
      *Note: The size remains the same.*
    * B) To format the USB drive.
      *Note: This is a side effect, but not the main purpose.*
    * C) To create a backup copy of the ISO image.
      *Note: Special backup software is used for this.*
    * **D) To make the USB stick bootable so that the installation program can be started directly from the stick.**
      *Note: A simple copy does not work; a bootable structure must be created.*
    * E) To set a password for the installation process.
      *Note: There is no functionality for this.*


---

### License
This work is licensed under the **Creative Commons Attribution - ShareAlike 4.0 International License**.
 
[To the license text on the Creative Commons website](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en)
