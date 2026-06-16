---
title: "Questions on Network Configuration and Diagnostics in LXC Containers"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "uwe.bachmann@jade-hs.de"
organization: "PDAL-Projekt"
date: "2025-08-25"
version: "1.0.0"
level: "Ebene 1, Lerneinheit 1.3, Assessment"
duration: "0,2 Std"
prerequisites:["Abgeschlossen -  Dokument: 1300 - Network Configuration and Diagnostics in LXC Containers"]
tags: ["PDAL","Assessment"]
license: "CC BY-SA 4.0"
---

### Questions on Network Configuration and Diagnostics in LXC Containers

**1. Which file is typically used in newer Ubuntu versions (>= 18.04) to configure a static IP address in an LXC container?**
* A. `/etc/network/interfaces`
    * *Hint: This file is used for configuration in older Ubuntu or Debian systems.*
* **B. `/etc/netplan/*.yaml`**
    * *Hint: Correct. Netplan is the standard for network configuration in newer Ubuntu versions.*
* C. `/etc/dhcp/dhcpd.conf`
    * *Hint: This file is used for configuring a DHCP server, not for the manual assignment of a static IP address.*
* D. `/etc/resolv.conf`
    * *Hint: This file configures DNS name resolution, not the IP address itself.*
* E. `/etc/sysconfig/network-scripts/ifcfg-eth0`
    * *Hint: This is a configuration path typically used in Red Hat-based systems like CentOS or Fedora.*

**2. What is the main function of the `sudo netplan try` command?**
* A. It saves the new network configuration permanently.
    * *Hint: The `sudo netplan apply` command does this.*
* **B. It tests the configuration before applying it permanently.**
    * *Hint: Correct. The command tests the configuration for 120 seconds to ensure the network remains reachable.*
* C. It shows a preview of the configuration file without making changes.
    * *Hint: A command like `cat` or `nano` would do this.*
* D. It resets the network configuration to DHCP.
    * *Hint: This command has no direct connection to resetting DHCP.*
* E. It deletes the existing Netplan configuration.
    * *Hint: Manual commands like `rm` are necessary for deleting configuration files.*

**3. A `ping 8.8.8.8` works, but a `ping google.com` fails. What is the most likely problem?**
* A. There is a gateway problem.
    * *Hint: If there were a gateway problem, neither IPs nor domains could be reached.*
* **B. There is a DNS problem.**
    * *Hint: Correct. The IP is reachable, but name resolution doesn't work, which indicates a faulty nameserver.*
* C. The web server is unreachable.
    * *Hint: `ping` tests connectivity at the IP level and not the reachability of a web server; `curl` or `wget` are better suited for that.*
* D. The network interface (`eth0`) is not active.
    * *Hint: In this case, no pings would work.*
* E. The static IP address is configured incorrectly.
    * *Hint: If the IP were configured incorrectly, the container would most likely not be able to connect to the external network.*

**4. Which diagnostic tool is used to display a list of all network interfaces, IP addresses, and their status?**
* A. `ping`
    * *Hint: `ping` checks the reachability of a host, not the local interfaces.*
* B. `ip r`
    * *Hint: `ip r` displays the routing table.*
* **C. `ip a`**
    * *Hint: Correct. `ip a` (or `ip address`) is the command for displaying interface information.*
* D. `netstat`
    * *Hint: `netstat` shows network statistics and open connections.*
* E. `curl`
    * *Hint: `curl` is a tool for testing HTTP requests.*

**5. What is the main function of the `ip r` command in the context of network diagnostics?**
* A. It displays open ports.
    * *Hint: `netstat` or `ss` are used for this.*
* B. It tests the reachability of an IP address.
    * *Hint: `ping` is used for this.*
* **C. It displays the routing table and the default gateway.**
    * *Hint: Correct. The command is crucial for checking whether traffic is being routed correctly out of the local network.*
* D. It lists the DNS servers.
    * *Hint: DNS servers are found in the configuration file or under `/etc/resolv.conf`.*
* E. It shows the current IP address.
    * *Hint: `ip a` is used for this.*

**6. What is the difference between using spaces and tabs in a Netplan configuration file?**
* A. There is no difference; both work.
    * *Hint: This is incorrect. YAML is very sensitive.*
* B. Tabs are preferred for indentation.
    * *Hint: On the contrary, tabs are not allowed in YAML and will cause errors.*
* **C. Only spaces are allowed for indentation.**
    * *Hint: Correct. The YAML format used by Netplan accepts only spaces for indentation.*
* D. Tabs are only used for comments.
    * *Hint: Tabs are generally not supported in YAML for any purpose.*
* E. Spaces are only used for the first level of indentation.
    * *Hint: Spaces are used for all levels of indentation.*

**7. What is a typical symptom of a gateway problem?**
* A. `ping 8.8.8.8` works, but `ping google.com` fails.
    * *Hint: This is a symptom of a DNS problem.*
* B. The container does not receive an IP address via DHCP.
    * *Hint: This points to a problem with the DHCP configuration or the server.*
* **C. Neither a `ping` to the gateway nor a `ping` to an external IP works.**
    * *Hint: Correct. The gateway is the first stop that must be reached to get to the internet. If this connection fails, it is the first indicator.*
* D. The container's internal services are not reachable.
    * *Hint: This problem is usually related to the configuration of internal services or a firewall.*
* E. The configuration in `/etc/network/interfaces` is not applied.
    * *Hint: This is a configuration problem that can occur independently of the gateway problem.*

**8. Which command is used to restart the networking service after manually editing the `/etc/network/interfaces` file?**
* A. `sudo netplan apply`
    * *Hint: This command is intended for Netplan configurations.*
* **B. `sudo systemctl restart networking`**
    * *Hint: Correct. This command restarts the relevant service to apply the changes.*
* C. `sudo service networking stop`
    * *Hint: This command stops the service but does not restart it.*
* D. `sudo restart eth0`
    * *Hint: This is not a correct command syntax.*
* E. `sudo networking restart`
    * *Hint: This is an outdated command syntax and is replaced by `systemctl` in modern systems.*

**9. According to the document, when is it essential to assign static IP addresses in a container environment?**
* A. When the host does not offer DHCP.
    * *Hint: The text suggests that DHCP is used by default.*
* B. When the host uses multiple bridges.
    * *Hint: The number of bridges is not a deciding factor for assigning static IPs.*
* **C. When no DNS server is available for name resolution.**
    * *Hint: Correct. If services need to communicate via hostnames but no DNS is present, static IPs are the only reliable method.*
* D. When a connection to the internet is required.
    * *Hint: Internet access can also be established via DHCP and DNS.*
* E. When multiple containers are running on the same host.
    * *Hint: DHCP can also be used with multiple containers as long as DNS resolution is possible.*

**10. According to the document, what is checked with the `netstat -tulnp` command in the LXC container?**
* A. The container's routing table.
    * *Hint: The `ip r` command is intended for this.*
* B. The container's IP address.
    * *Hint: The `ip a` command is used for this.*
* **C. Open, listening ports and their associated processes.**
    * *Hint: Correct. The command lists all listening TCP and UDP ports as well as their associated process IDs.*
* D. Name resolution in the container.
    * *Hint: `ping <hostname>` or `dig` are used for this.*
* E. The internet download speed.
    * *Hint: Tools like `wget` or `speedtest-cli` are better suited for this purpose.*

---

### License
This work is licensed under the **Creative Commons Attribution - ShareAlike 4.0 International License**.
 
[To the license text on the Creative Commons website](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en)
