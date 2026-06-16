---
title: "Multiple-Choice Questions for Creating an LXC Container"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe"]
email: "uwe.bachmann@jade-hs.de"
organization: "PDAL Project"
date: "2025-08-21"
version: "1.0.0"
level: "Level 1, Learning Unit 1.1, Assessment"
duration: "0.2 hours"
prerequisites: ["Completed - Document: 1150 - Creating an LXC Container"]
tags: ["PDAL", "Assessment"]
license: "CC BY-SA 4.0"
---

### Multiple-Choice Questions for Creating an LXC Container

1.  **What is the difference between an LXC container and a full-fledged VM (Virtual Machine)?**
    * A) An LXC container has its own kernel, while a VM uses the host's kernel.
        * Hint: This is the incorrect statement. The main difference is that the container uses the host's kernel.
    * B) A VM shares all resources with the host, while an LXC container has isolated resources.
        * Hint: This is also an incorrect statement. Containers share the kernel and libraries.
    * **C) An LXC container is a lightweight virtualization that uses the host system's kernel, while a VM virtualizes a complete operating system with its own kernel.**
        * Hint: This is the correct statement. LXC offers operating system virtualization, which is more efficient than the hardware virtualization of a VM.
    * D) LXC containers can only run Linux distributions, while VMs can only run Windows systems.
        * Hint: LXC can only run Linux systems, but VMs can host almost any operating system.
    * E) LXC containers are only intended for web servers, and VMs for databases.
        * Hint: Both technologies are suitable for a wide variety of use cases.

2.  **Which of the following tasks should NOT be performed inside the LXC container?**
    * A) Installing web server software.
        * Hint: Installing applications is the main purpose of a container.
    * B) Configuring a new user with sudo privileges.
        * Hint: User management is a typical administrative step within the container.
    * C) Running a system update (`apt update && apt upgrade`).
        * Hint: Regular updates are essential for security and functionality.
    * **D) Changing hardware settings like RAM or CPU cores.**
        * Hint: These settings are configured on the Proxmox host (hypervisor), not inside the container.
    * E) Checking network connectivity.
        * Hint: Checking the connection is a standard troubleshooting step.

3.  **Why are the CTID and hostname `apache110` chosen in the document, and why does the IP address end in `.110`?**
    * A) Because `110` is the default ID for LXC containers.
        * Hint: There is no default ID; Proxmox starts counting at 100.
    * B) Because these are the only values available in Proxmox.
        * Hint: You can choose any three-digit CTID.
    * **C) To establish a clear association between the container ID, the hostname, and the last octet of the IP address.**
        * Hint: This is a best practice to simplify the management of many containers and improve clarity.
    * D) Because these values are automatically set by the template.
        * Hint: Most of these values must be entered manually.
    * E) To increase the container's security.
        * Hint: The choice of these values has no impact on security.

4.  **What is the advantage of using an "unprivileged" container, as recommended in the document?**
    * A) It is more powerful because it can use more hardware resources.
        * Hint: Unprivileged containers can even be slightly slower because they have additional restrictions.
    * **B) It increases security because processes inside the container cannot run as `root` on the host system.**
        * Hint: This is the main advantage. An unprivileged container cannot gain host system privileges, even if compromised.
    * C) It requires less RAM and CPU cores.
        * Hint: Resource allocation is independent of the privilege status.
    * D) It allows the installation of Windows applications.
        * Hint: This is not possible with LXC containers.
    * E) It is easier to configure than a privileged container.
        * Hint: Both are configured similarly; the main difference is in the security model.

5.  **Why is it a recommended step to check the network connectivity of a new container in three steps (`ping` gateway, Google DNS, and a domain name)?**
    * A) To measure the speed of the internet connection.
        * Hint: This is a side effect, but not the main purpose.
    * B) To test the host's firewall rules.
        * Hint: A ping tests reachability, but not specific firewall rules.
    * **C) To verify reachability at different levels: local network, external network, and name resolution.**
        * Hint: This method helps to isolate the problem step-by-step if the connection fails.
    * D) To change the container's IP address.
        * Hint: Pings do not change network configurations.
    * E) To establish a connection to the Proxmox web interface.
        * Hint: The web interface is provided by the host, not the container.

6.  **What is the function of the command `usermod -aG sudo pdal`?**
    * A) It deletes the user `pdal` from the system.
        * Hint: The command for deletion is `deluser`.
    * B) It creates the user `pdal` and sets a password.
        * Hint: The `adduser` command is used for this.
    * **C) It adds the existing user `pdal` to the `sudo` group to give them administrative rights.**
        * Hint: The `-aG` option stands for "append to group" and is the correct way to grant `sudo` rights to a user.
    * D) It changes the container's hostname.
        * Hint: The `hostnamectl` command would be used for this.
    * E) It updates all packages on the system.
        * Hint: `apt upgrade` is used for this.

7.  **Why is `timedatectl` used in the LXC container only to configure the timezone and not for time synchronization?**
    * A) Because LXC containers do not have their own system time.
        * Hint: Containers have their own, isolated time view, but it depends on the host.
    * B) Because `timedatectl` only works on virtual machines, not in containers.
        * Hint: The command also works in containers.
    * **C) Because the container's system time is inherited from the host system, and a separate time synchronization is not necessary.**
        * Hint: This is a fundamental concept of containers. They share the kernel and thus the system time with the host.
    * D) Because time synchronization services like `chrony` cannot be installed in LXC containers.
        * Hint: `chrony` can be installed, but it would be redundant.
    * E) Because `timedatectl` gets the time from the internet, which is not possible in an ICS network.
        * Hint: This is the wrong assumption.

8.  **What does the `-y` flag in the command `apt upgrade -y` mean?**
    * A) It displays a list of packages to be installed.
        * Hint: The `-s` or `--simulate` flag is used for this.
    * B) It stops the update process if an error occurs.
        * Hint: This is not the function of the `-y` flag.
    * **C) It automatically answers all confirmation requests (yes/no) with "yes" and executes the action non-interactively.**
        * Hint: The `-y` flag is useful for automating scripts to avoid manual input.
    * D) It performs a rollback to an earlier package version.
        * Hint: There are other commands for this.
    * E) It downloads the package lists from a different repository.
        * Hint: You would edit `/etc/apt/sources.list` for this.

9.  **What role does a template like `ubuntu-24.04-standard_...amd64.tar.zst` play in creating an LXC container?**
    * A) It serves as a backup for the container.
        * Hint: Templates are not backups, but base installations.
    * B) It is a full-fledged, runnable VM.
        * Hint: A template is not a finished system.
    * C) It contains the configuration files for the container.
        * Hint: The configuration files are generated when the container is created.
    * **D) It is a minimized filesystem image that forms the basis for a new container and speeds up the installation.**
        * Hint: Templates contain only the minimal files required for a functional environment.
    * E) It is only needed for the installation of applications.
        * Hint: It is the foundation for the entire operating system in the container.

10. **What is the function of a "bridge" (`vmbr0`) in the context of network configuration in Proxmox?**
    * A) It connects two physical network cards with each other.
        * Hint: A bridge can do that, but it is not its main function in the Proxmox context.
    * **B) It acts as a virtual switch that allows the host and all VMs/containers to communicate with each other and with the physical network.**
        * Hint: A bridge connects virtual and physical network interfaces.
    * C) It is a virtual router that routes traffic between containers and the internet.
        * Hint: A router routes traffic between different networks; a bridge connects them on the same level.
    * D) It serves as a firewall to protect the container from attacks.
        * Hint: The firewall function is configured separately.
    * E) It is a purely software function without a connection to the physical hardware.
        * Hint: It connects the virtual network to the host's physical network interface.

---

### License
This work is licensed under the **Creative Commons Attribution - ShareAlike 4.0 International License**.
 
[To the license text on the Creative Commons website](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en)
