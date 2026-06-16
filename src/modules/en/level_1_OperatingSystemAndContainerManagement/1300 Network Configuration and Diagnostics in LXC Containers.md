---
title: "Network Configuration and Diagnostics in LXC Containers" 
author: ["Gudenkauf, Prof Stefan", "Uwe, Bachmann", "Ronald, Kalk"]
email: "pdal@jade-hs.de"
organization: "PDAL-Projekt, Jade University of Applied Sciences" 
date: "2025-08-22" 
version: "1.0.0" level: "Level 1, Learning Unit 1.3" 
duration: "Estimated Duration (e.g., 2-4 hours)" 
prerequisites: "Tiny PC with Proxmox installed and at least one LXC container" 
tags: ["Proxmox", "Linux", "Virtualization", "Basics"] 
license: "CC BY-SA 4.0"

---

# Network Configuration and Diagnostics in LXC Containers

## 1\. Introduction

This documentation covers **network configuration in LXC containers**, specifically setting a **static IP address**. It also introduces important **network diagnostic tools** that can be used to identify and fix network problems within an LXC container.

The estimated time for this topic is about **2–4 hours** and is suitable for both learners in the field of Linux networking and for practical use in server or container operations.

> Tip: Create your own LXC container to test the configurations. If something goes wrong, delete the LXC container, create a new one, and repeat the test.

-----

## 2\. Fundamentals of Network Configuration in LXC Containers

By default, an LXC container gets its IP address via **DHCP** from the host or a bridge (e.g., `vmbr0`). In distributed container environments where, for example, databases or web servers need to communicate with each other, either DNS name resolution or the assignment of **static IP addresses** is required to ensure reliable accessibility.

However, since we are not using a DNS server, it is essential to assign static IP addresses here.

### 2.1 Network Files

Depending on the server/LXC version used, there are two variants:

1.  **Newer Ubuntu versions (\>= 18.04):**
      - Configuration via **Netplan** in `/etc/netplan/*.yaml`.
2.  **Older Ubuntu versions (\< 18.04) or Debian containers:**
      - Configuration via **/etc/network/interfaces**.

-----

## 3\. Configuring a Static IP Address

### 3.1 Configuration with Netplan

1.  Open the Netplan configuration file (e.g., `01-netcfg.yaml`):

    ```bash
    sudo nano /etc/netplan/01-netcfg.yaml
    ```

2.  Example configuration for a static IP:

    ```yaml
    network:
      version: 2
      ethernets:
        eth0:
          dhcp4: no
          addresses:
            - 192.168.137.110/24
          gateway4: 192.168.137.1
          nameservers:
            addresses:
              - 192.168.137.1
              - 8.8.8.8
    ```

    **Explanation:**

      - `eth0` → Network interface of the LXC container
      - `dhcp4: no` → Disable DHCP
      - `addresses` → Static IP address with subnet
      - `gateway4` → Default gateway
      - `nameservers` → DNS servers

    > Note: ⚠️ **Caution with Netplan/YAML:**
    > The Netplan configuration file uses the **YAML format**, which is very sensitive to **spelling and indentation**.
    > YAML works exclusively with **spaces** for indentation – **tabs are not allowed**.
    > Incorrect indentation or syntax errors will prevent Netplan from **applying the configuration**.
    > In this case, either the old network configuration remains, or an error occurs, rendering the network unavailable.

3.  Test configuration (safe option):

    ```bash
    sudo netplan try
    ```

      - This command applies the new network configuration on a trial basis.
      - You have **120 seconds** to confirm the changes with `ENTER`.
      - If you made a mistake and the network is unreachable, it will automatically revert to the old working configuration after the time expires.

4.  Apply changes permanently:

    ```bash
    sudo netplan apply
    ```

      - The new configuration is **permanently applied**.
      - From this point on, the configuration remains active until it is changed again.

5.  Verify network settings:

    ```bash
    ip a
    ```

![IpALxcConsole](./1300attachments/IpALxcConsole.png)

-----

### 3.2 Configuration with /etc/network/interfaces

1.  Open the file:

    ```bash
    sudo nano /etc/network/interfaces
    ```

2.  Example configuration:

    ```bash
    auto eth0
    iface eth0 inet static
        address 192.168.137.110
        netmask 255.255.255.0
        gateway 192.168.137.1
        dns-nameservers 192.168.137.1 8.8.8.8
    ```

3.  Restart the networking service:

    ```bash
    sudo systemctl restart networking
    ```

4.  Verification:

    ```bash
    ip a
    ```

-----

## 4\. Network Diagnostic Tools in the LXC Container

Various commands are available for diagnosing network problems. Below is an overview of the most important tools with examples of their use.

-----

### 4.1 `ping` – Check Reachability

```bash
ping 192.168.137.1
```

checks the reachability of the internal network. If the test is successful...

```bash
ping 8.8.8.8
```

checks the reachability of Google's DNS, and therefore the connection to the internet. If the test is successful...

```bash
ping google.com
```

checks name resolution on the internet.

  - Identifies fundamental problems such as a missing internet connection or DNS resolution issues.

-----

### 4.2 `ip a` – Display Network Interfaces

```bash
ip a
```

  - Lists all interfaces, IP addresses, and their status.
  - Important for checking if the static IP was set correctly.

-----

### 4.3 `ip r` – Display Routing Table

```bash
ip r
```

  - Shows the default gateway and routing rules.
  - Source of error: If the gateway is missing, no connection to the internet is possible.

-----

### 4.4 `netstat -tulnp` – Display Open Ports

```bash
sudo netstat -tulnp
```

  - `-t` → TCP connections
  - `-u` → UDP connections
  - `-l` → listening ports only
  - `-n` → numerical output (IP instead of name)
  - `-p` → process information

Example output:

| Proto | Recv-Q | Send-Q | Local Address | Foreign Address | State | PID/Program name |
|-------|--------|--------|---------------|-----------------|--------|------------------|
| tcp | 0 | 0 | 0.0.0.0:22 | 0.0.0.0:\* | LISTEN | 450/sshd |

-----

### 4.5 `curl` – Test HTTP Requests

```bash
curl http://google.com
curl -I http://google.com
```

  - `-I` shows only the headers.
  - Useful for testing if a web server is reachable.

-----

### 4.6 `wget` – Download Files from the Web

```bash
wget https://dlcdn.apache.org/tomcat/tomcat-10/v10.1.43/bin/apache-tomcat-10.1.43.tar.gz
```

  - Useful for checking connectivity and download capability.
  - Can also be used for automated installations.

-----

## 5\. Network Flow: Host ↔ LXC Container ↔ Internet

To better understand network configuration, the following diagram shows the typical data flow:

```text
            +-------------------------+
            |      Internet           |
            +-------------------------+
                     |
                (Gateway/Router)
                     or
            (Windows Host with ICS)
                     |
            +-------------------------+
            |   Proxmox Host          |
            |   Bridge: vmbr0         |
            +-------------------------+
                     |
            +-------------------------+
            |   LXC Container         |
            |   eth0: 192.168.137.110 |
            +-------------------------+
```

  - **Internet ↔ Gateway/Router or Windows Host with ICS:** Connection to the external network
  - **Proxmox Host (Bridge vmbr0):** mediates between the physical network and the LXC container
  - **LXC Container (eth0):** receives a static IP (e.g., `192.168.137.110`)

-----

## 6\. Typical Sources of Error – Graphical Overview

The following scenarios help with diagnosis:

### 6.1 Gateway Problem

```text
[LXC Container] ---X---> [Gateway/Router] ---> [Internet]
    eth0: 192.168.137.110
    ping 192.168.137.1  --> ERROR
    ping 8.8.8.8        --> ERROR
```

  - **Symptoms:** No connection to the internet, gateway is unreachable.
  - **Solution:** Check the gateway entry in `netplan` or `interfaces`.

If connectivity from the LXC container to the gateway or the internet is not working, you can also check and change the network parameters directly in the **Proxmox web interface**:

1.  **Log in to the Proxmox web interface:**

    ```bash
    https://<Proxmox-IP>:8006
    ```

2.  **Select the LXC container:**

      - On the left, select the corresponding LXC container.

3.  **Check the network:**

      - Open the **"Network"** tab.
      - Here you can see the configuration of `eth0` or other interfaces:
          - **IP Address**
          - **Netmask**
          - **Gateway**

4.  **Adjust settings (if necessary):**

      - Set the IP address to the correct subnet.
      - Enter the correct gateway (e.g., 192.168.137.1).
      - Save the changes.

5.  **Restart the LXC container**
    or apply the network configuration:

    ```bash
    sudo ip a    # check
    sudo ping 192.168.137.1
    ```

    Note: Changes made via the web interface are automatically applied to the LXC container configuration file `/etc/pve/lxc/<CTID>`.conf.

### 6.2 DNS Problem

```text
[LXC Container] ---> [Gateway/Router] ---> [Internet]
    eth0: 192.168.137.110
    ping 8.8.8.8   --> OK
    ping google.com --> ERROR
```

  - **Symptoms:** IPs are reachable, but domains are not.
  - **Solution:** Check the nameserver entry in `netplan` or `interfaces`.

Alternative: Check DNS settings via the Proxmox web interface

1.  Log in to the Proxmox web interface:

    ```bash
    https://<Proxmox-IP>:8006
    ```

2.  Select the LXC container:

      - On the left, select the corresponding LXC container.

3.  Check the network:

      - Open the "Network" tab.

      - Here you can see the configuration of `eth0` or other interfaces:

          - IP Address

          - Netmask

          - Gateway

          - DNS Server

4.  Adjust DNS servers:

      - Add e.g., 8.8.8.8 or another working nameserver.

      - Save the changes.

5.  Restart the LXC container or apply the network configuration:

    ```bash
    sudo netplan apply # if netplan is used
    sudo ping google.com # check
    ```

-----

### 6.3 ICS Adapter Fails After Windows Update

It sometimes happens that (after Windows updates) the **ICS adapter (Internet Connection Sharing)** no longer works.
This leads to **no connection from the internal network to the internet and vice versa**.

**Procedure for resolution:**

1.  Open **Network Settings** in Windows.

2.  Select **Advanced network settings** → **More adapter options**.

3.  In the new window, select the network connection used, right-click, and open **Properties**.

4.  Go to the **Sharing** tab and **deactivate** Internet Connection Sharing (uncheck the box).

      - Confirm with **OK**.

5.  Re-open the adapter options and go back to **Sharing**.

6.  **Reactivate** the checkbox for Internet Connection Sharing, select the **ICS adapter** in the field below, and confirm with **OK**.

➡️ The ICS connection should then work as usual.

## 7\. Example Workflows

This section shows **practical workflows for network configuration and diagnostics in LXC containers**.
The goal is to demonstrate with concrete examples how to:

  - Correctly set up a **static IP address** and test the network connection.
  - Check **connectivity to the local network, internet, and DNS**.
  - Recognize and systematically diagnose common **causes of a missing internet connection**.
  - Check network services and open ports to identify potential problems with server applications.

The workflows are intended to serve as practical, step-by-step instructions that can be applied directly in real container environments.

### 7.1 Set up and test static IP

1.  Adjust Netplan → `sudo netplan apply`.
2.  `ping 192.168.137.1` → Check connectivity to the gateway, in this case, the ICS network interface.
3.  `ping 8.8.8.8` → Check connectivity to Google DNS.
4.  `ping google.com` → Check if name resolution works.
5.  `curl http://google.com` → Test HTTP connection.

-----

### 7.2 Troubleshooting a Missing Internet Connection

1.  **Check IP:**

    ```bash
    ip a
    ```

2.  **Check Gateway:**

    ```bash
    ip r
    ```

3.  **Check DNS:**

    ```bash
    ping 8.8.8.8
    ping google.com
    ```

      - If `8.8.8.8` works, but `google.com` does not → DNS problem.

4.  **Check Ports (e.g., web server in the LXC container):**

    ```bash
    netstat -tulnp
    ```

-----

## 8\. Summary

  - **Static IPs** are configured via `/etc/netplan/*.yaml` (newer systems) or `/etc/network/interfaces` (older systems).
  - Diagnostic tools like `ping`, `ip a`, `ip r`, `netstat`, `curl`, and `wget` help to quickly identify network problems.
  - **Graphical overviews** facilitate understanding network flow and troubleshooting.

-----

## 9\. Further Exercises

  - Setting up multiple static IPs (e.g., for different services in the container).
  - Using `ss` as a modern replacement for `netstat`.
  - Combining `curl` with REST APIs to test the functionality of web services.
  - The general error analysis and troubleshooting will follow in a later module.

-----

## Sources

  - "Command Overview › Shell › Wiki › ubuntuusers.de". Accessed: August 20, 2025. [Online]. Available at: [Ubuntuuser Command Overview](https://wiki.ubuntuusers.de/Shell/Befehls%C3%BCbersicht/)
  - H. Lasch, "Linux-Kommandos Kurzreferenz | Linux | Nutzungshinweise | FRIZ | Fakultät für Informatik | TU Chemnitz". Accessed: August 20, 2025. [Online]. Available at: [Linux Reference](https://www.tu-chemnitz.de/informatik/friz/linux/referenz.php)

---

### License
This work is licensed under the **Creative Commons Attribution - ShareAlike 4.0 International License**.
 
[To the license text on the Creative Commons website](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en)
