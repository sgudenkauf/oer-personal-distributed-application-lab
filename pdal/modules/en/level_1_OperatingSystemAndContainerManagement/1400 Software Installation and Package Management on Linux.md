---
title: "Software Installation and Package Management" 
author: ["Gudenkauf, Prof Stefan", "Uwe, Bachmann", "Ronald, Kalk"]
mail: "uwe.bachmann@jade-hs.de"
organization: "e.g., PDAL-Projekt, Jade University of Applied Sciences" 
date: "2025-08-26" 
version: "1.0.0" level: "Level 1, Learning Unit 1.4" 
duration: "Estimated Duration (e.g., 2-3 hours)" 
prerequisites: "Tiny PC with Proxmox installed and at least one LXC container" 
tags: ["Proxmox", "Linux", "Virtualization", "Basics"] 
license: "CC BY-SA 4.0"
---

# 📦 Software Installation and Package Management on Linux (Debian/Ubuntu)

Managing software packages is a core part of any Linux system. On Linux-based distributions (e.g., **Ubuntu, Debian, Linux Mint, Proxmox VE**), the **APT (Advanced Package Tool)** is used for this. In addition, there are utility programs like `wget` to download files from the internet.

Unlike with Windows, Linux has **no automatic update service** that updates the system without user interaction. Updates must therefore be **triggered manually**, for example with:

```bash
sudo apt update      # Update package lists
sudo apt upgrade     # Apply installable updates
```

-----

## 🔹 APT Fundamentals

APT works with a **package repository**, which contains a collection of software packages. Each package consists of programs, libraries, and metadata.

The **repositories** are maintained by the respective Linux distributions and ensure that the packages are up-to-date and verified. For the system to know which packages are available, `apt` relies on a **package list** that should be updated regularly.

When installing or updating packages, the corresponding files are queried and downloaded via the **URLs stored in the repository**.

-----

## 🛠️ Frequently Used APT Commands

### 1\. Update Package Lists

```bash
sudo apt update
```

  * Retrieves the latest package information from the configured repositories.
  * **Does not yet perform an upgrade**, but only updates the database.
  * Should always be run **before installations**.

### 2\. Update System Packages

```bash
sudo apt upgrade
```

  * Installs the latest versions of all already installed packages.
  * Normally leaves existing configurations untouched.

> 👉 Tip: To also automatically update dependencies and orphaned packages, you can use:

```bash
sudo apt full-upgrade
```

### 3\. Install Software

```bash
sudo apt install <package name>
```

Examples:

```bash
sudo apt install apache2
sudo apt install htop
```

  * Downloads and installs the package and all its dependencies.
  * For graphical programs, additional libraries are automatically installed.

-----

### 4\. Remove Software

```bash
sudo apt remove <package name>
```

Example:

```bash
sudo apt remove apache2
```

  * Removes the package but **leaves configuration files behind**.
  * Useful if you want to install the software again later.

👉 To also delete the configuration:

```bash
sudo apt purge <package name>
```

-----

### 5\. Remove Orphaned Packages

```bash
sudo apt autoremove
```

  * Automatically removes no longer needed dependencies.
  * Practical after uninstalling software.

-----

### 6\. Search for a Package

```bash
apt search <search term>
```

Example:

```bash
apt search nginx
```

  * Displays available packages that match the search term.

-----

### 7\. Show Package Information

```bash
apt show <package name>
```

Example:

```bash
apt show curl
```

  * Provides details such as version, description, and dependencies.

-----

## 🔄 Upgrade to a New Ubuntu Version

When a **new Ubuntu version** is released (e.g., from Ubuntu 22.04 LTS → 24.04 LTS), `apt update && apt upgrade` is not enough. For this, the **do-release-upgrade** tool is used.

### Preparation

1.  Apply all current updates:

    ```bash
    sudo apt update && sudo apt upgrade && sudo apt full-upgrade
    ```

2.  Reboot the system (if a kernel update was installed):

    ```bash
    sudo reboot
    ```

### Start Upgrade

```bash
sudo do-release-upgrade
```

  * Starts the Ubuntu upgrade assistant.
  * Guides you through the complete upgrade process.
  * May ask how to handle existing configuration files.

👉 If `do-release-upgrade` is not available, it can be installed:

```bash
sudo apt install update-manager-core
```

### Manual Upgrade (Alternative Method)

If you change the release directly via `/etc/apt/sources.list`:

1.  Change all entries from, for example, `jammy` → `noble` (depending on the version).

2.  Afterwards:

    ```bash
    sudo apt update && sudo apt full-upgrade
    ```

    > ⚠️ Warning: This manual method is **more prone to errors** and is only recommended for experienced admins.

-----

## 🌍 Downloading Files with `wget`

`wget` is a command-line tool to download files from the internet.

> **Note:** Software should **only be installed** via `wget` if the desired application is **not available through the package repository**. By default, it is always safer and easier to install packages via **APT**.

```bash
sudo apt install wget
```

### Download a File

```bash
wget <URL>
```

Example:

```bash
wget https://dlcdn.apache.org/tomcat/tomcat-10/v10.1.43/bin/apache-tomcat-10.1.43.tar.gz
```

  * Downloads the file to the current directory.

> Note:
> You must either be in the desired download directory before running the command, or explicitly specify the destination path during the download (see example below):

```bash
wget -P /path/to/destination/directory https://dlcdn.apache.org/tomcat/tomcat-10/v10.1.43/bin/apache-tomcat-10.1.43.tar.gz
```

### Download Multiple Files

```bash
wget -i urls.txt
```

  * Useful if `urls.txt` contains a list of URLs.

### Download in the Background

```bash
wget -b <URL>
```

-----

## ✅ Summary

| Command | Function |
| ------------------------- | -------------------------------------------- |
| `sudo apt update` | Updates package lists |
| `sudo apt upgrade` | Installs new package versions |
| `sudo apt full-upgrade` | Also updates dependencies |
| `sudo apt install` | Installs a package |
| `sudo apt remove` | Removes package, keeps config files |
| `sudo apt purge` | Removes package including configuration |
| `sudo apt autoremove` | Removes orphaned dependencies |
| `apt search` | Searches for packages |
| `apt show` | Shows package details |
| `sudo do-release-upgrade` | Upgrades to a new Ubuntu version |
| `wget <URL>` | Downloads a file from the internet |

-----

## Sources

  * "apt › apt › Wiki › ubuntuusers.de". Accessed: August 21, 2025. [Online]. Available at: [apt reference](https://wiki.ubuntuusers.de/apt/apt/)
  * "Upgrade › Wiki › ubuntuusers.de". Accessed: August 21, 2025. [Online]. Available at: [Upgrade reference](https://wiki.ubuntuusers.de/Upgrade/)
  * "wget › Wiki › ubuntuusers.de". Accessed: August 21, 2025. [Online]. Available at: [wget reference](https://wiki.ubuntuusers.de/wget/)

-----

### License
This work is licensed under the **Creative Commons Attribution - ShareAlike 4.0 International License**.
 
[To the license text on the Creative Commons website](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en)
