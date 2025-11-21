---
title: "Questions on Apache2 Web Server and User Management"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "pdal@jade-hs.de"
organization: "PDAL Project"
date: "2025-09-25"
version: "1.0.0"
level: "Level 2, Learning Unit 2.1, Assessment"
duration: "0.2 hours"
prerequisites: 
["Completed - Document: 2100 - Apache2 Web Server & User Management in an LXC Container"]
tags: ["PDAL","Assessment"]
license: "CC BY-SA 4.0"
---

## ❓ 10 Multiple-Choice Questions on Apache2 Web Server and User Management

1. **What is the primary characteristic that differentiates the architecture of Apache2 in its default configuration from Nginx?**
    * A) Apache2 exclusively uses centralized configuration files, while Nginx uses decentralized files.
        * *Hint*: This is incorrect. Apache2 heavily utilizes modular per-directory configurations (`.htaccess`), while Nginx is configured centrally.
    * B) Apache2 is proprietary software, while Nginx is open-source.
        * *Hint*: This is incorrect. Apache2 belongs to the **open-source software family**.
    * C) Nginx only supports static content, while Apache2 supports dynamic content.
        * *Hint*: This is incorrect. Nginx also supports dynamic content but is typically faster with static content.
    * **D) Apache2 uses a process-based or thread-based approach, while Nginx uses an event-driven, asynchronous model.**
        * *Hint*: This is correct and describes the fundamental architectural difference between the two web servers.
    * E) Apache2 is only used on Windows systems, Nginx only on Linux.
        * *Hint*: This is incorrect. Apache2 is used on many operating systems, especially Linux.

2. **What is the purpose of the command `sudo apt update` during the installation process?**
    * A) It installs the Apache2 web server.
        * *Hint*: This is incorrect. Installation is done with `sudo apt install apache2`.
    * B) It starts the Apache2 service after installation.
        * *Hint*: This is incorrect. The status is checked with `systemctl status apache2`, and the service usually starts automatically.
    * **C) It updates the package lists and information about available software on the system.**
        * *Hint*: This is correct and serves as preparation for the actual installation.
    * D) It removes an already existing Apache2 installation.
        * *Hint*: This is incorrect. `apt remove` is used for removal.
    * E) It checks whether the server has a valid IP address.
        * *Hint*: This is incorrect. `apt update` is a package management command.

3. **What is the standard web directory (Document Root) from which Apache2 delivers content by default?**
    * A) `/home/www/html`
        * *Hint*: This is incorrect. The web directory is not located in the home directory.
    * B) `/etc/apache2/html`
        * *Hint*: This is incorrect. `/etc` contains configuration files, not the content.
    * **C) `/var/www/html`**
        * *Hint*: This is correct. This is the standard directory under Debian/Ubuntu.
    * D) `/usr/local/apache2`
        * *Hint*: This is incorrect. This is often the installation directory, not the web directory.
    * E) `/var/log/apache2`
        * *Hint*: This is incorrect. This directory contains the server's log files.

4. **What is the main reason for using PHP over static HTML pages on a web server?**
    * A) PHP files are delivered faster than static HTML pages.
        * *Hint*: This is incorrect. Static HTML pages are often faster because no server-side processing is necessary.
    * B) PHP is a database and stores user data.
        * *Hint*: This is incorrect. PHP is a scripting language, not a database, but it enables interaction with databases.
    * **C) PHP enables the creation of dynamic web pages that generate content based on databases or user input.**
        * *Hint*: This is correct. PHP is a server-side scripting language that allows for dynamic content.
    * D) PHP code is executed directly in the user's browser.
        * *Hint*: This is incorrect. PHP is a **server-side** scripting language.
    * E) The use of PHP is required by law.
        * *Hint*: This is incorrect. There is no such requirement.

5. **What is the purpose of the Apache2 PHP module (`libapache2-mod-php`) installed in the guide?**
    * A) It is an FTP client required for uploading PHP files.
        * *Hint*: This is incorrect. FTP/SFTP is used for external uploads.
    * B) It is a database server used by PHP.
        * *Hint*: This is incorrect. Databases like MySQL are installed separately.
    * C) It allows editing PHP files on the server.
        * *Hint*: This is incorrect. This is enabled by editors like `nano` or SFTP clients.
    * **D) It integrates the PHP interpreter into the Apache2 web server to process and deliver PHP files.**
        * *Hint*: This is correct. The module (`libapache2-mod-php`) is the necessary interface.
    * E) It is only needed to check the PHP status via the command line.
        * *Hint*: This is incorrect. `php-cli` is installed for that purpose.

6. **Which command is used to apply changes to the Apache2 configuration without completely restarting the service?**
    * A) `sudo systemctl stop apache2`
        * *Hint*: This is incorrect. This command stops the service.
    * B) `sudo apt update`
        * *Hint*: This is incorrect. This command updates package lists.
    * **C) `sudo systemctl reload apache2`**
        * *Hint*: This is correct. `reload` reloads the configuration without interrupting active connections, which is more efficient than `restart`.
    * D) `sudo systemctl status apache2`
        * *Hint*: This is incorrect. This command checks the status.
    * E) `sudo systemctl start apache2`
        * *Hint*: This is incorrect. This command starts the service.

7. **What is the fundamental role of user groups on a Linux server, especially in the context of Apache2 administration (Section 3)?**
    * A) They are required to host static HTML pages.
        * *Hint*: This is incorrect. HTML pages do not require specific group management.
    * **B) They enable the central management of access rights for multiple users to files, directories, or system services.**
        * *Hint*: This is correct. Groups simplify permission management as rights do not have to be assigned individually to each user.
    * C) Groups are only used to grant root privileges to users.
        * *Hint*: This is incorrect. Groups can also be used for non-privileged access (e.g., read rights).
    * D) They are used to encrypt the server's IP address.
        * *Hint*: This is incorrect. Groups have nothing to do with IP encryption.
    * E) Groups are an outdated concept and are no longer used today.
        * *Hint*: This is incorrect. Groups are an essential part of Linux permission management.

8. **Why is the `visudo` tool used instead of a direct editor (like `nano /etc/sudoers`) to set up sudo rights for the `apacherestart` group?**
    * A) `visudo` is only available via the Proxmox web interface.
        * *Hint*: This is incorrect. `visudo` is a command-line tool.
    * B) It is the only tool that encrypts passwords.
        * *Hint*: This is incorrect. `visudo` has primarily other security functions.
    * **C) `visudo` performs a syntax check on the `/etc/sudoers` file to prevent errors from locking up the system's entire `sudo` functionality.**
        * *Hint*: This is correct and the main benefit of `visudo`. A faulty `sudoers` file can make root access impossible.
    * D) It can only be executed by the `apacherestart` group.
        * *Hint*: This is incorrect. `visudo` is executed with root privileges (or `sudo`).
    * E) It automatically creates the required `apacherestart` group.
        * *Hint*: This is incorrect. The group must be created manually with `groupadd`.

9. **What is the purpose of the configuration line `Alias /user1 /home/user1/www` in the Apache configuration file `stud-aliases.conf`?**
    * A) It creates the user `user1`.
        * *Hint*: This is incorrect. The user is created with `useradd`.
    * B) It determines that the user `user1` is allowed to read the Apache directory.
        * *Hint*: This is incorrect. This is a permission question.
    * C) It grants the Apache server the rights to access the home directory.
        * *Hint*: This is incorrect. Rights are set with `chown` and `chmod`.
    * D) It configures the Apache server as a reverse proxy.
        * *Hint*: This is incorrect. A reverse proxy forwards requests, which is not the case here.
    * **E) It maps the URL path `/user1` on the web server to the physical directory `/home/user1/www` on the file system, making the content accessible via HTTP.**
        * *Hint*: This is correct. An Alias creates a virtual directory structure in the web server that points to a different physical directory.

10. **Which of the following files or paths is assigned the permissions `sudo chown -R www-data:www-data` and `sudo chmod -R 755` during the SFTP transfer of web files?**
    * A) The `sudoers` file for permission management.
        * *Hint*: This is incorrect. The `sudoers` file should only be edited by root/admin tools.
    * B) The `ca.cert.pem` certificate for TLS encryption.
        * *Hint*: This is incorrect. Certificates have different permissions and are not part of this process.
    * C) The user's home directory (`/home/user1`).
        * *Hint*: This is incorrect. The home directory is assigned `chmod 755` in the guide, but not `chown www-data:www-data`.
    * **D) The project folders in the standard web directory (`/var/www/html/mein_projekt`) for larger projects.**
        * *Hint**: This is correct. These permissions ensure that the Apache process (`www-data`) can read the files and that the rights are set correctly.
    * E) The main configuration file of the Apache server (`apache2.conf`).
        * *Hint*: This is incorrect. This file is managed by root/system accounts.

---

### License
This work is licensed under the **Creative Commons Attribution - ShareAlike 4.0 International License**.
 
[To the license text on the Creative Commons website](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en)
