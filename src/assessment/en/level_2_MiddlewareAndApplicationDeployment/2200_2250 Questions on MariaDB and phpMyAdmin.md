---
title: "Questions on MariaDB and phpMyAdmin"
author: ["Gudenkauf, Prof Stefan", "Uwe, Bachmann", "Ronald, Kalk"]
email: "pdal@jade-hs.de"
organization: "PDAL-Projekt"
date: "2025-09-29"
version: "1.0.0"
level: "Level 2, Learning Unit 2.2x, Assessment"
duration: "0.2 Hrs"
prerequisites: ["Completed - 2100 Apache2 Webserver and User Management in LXC Container", "Completed - Installation and Configuration of phpMyAdmin in Apache2 LXC", "Completed - Installation and Configuration of MariaDB in LXC Container"]
tags: ["PDAL","Assessment"]
license: "CC BY-SA 4.0"
---

## Multiple-Choice Questions on MariaDB and phpMyAdmin (Learning Unit 2.2)

### 1. Installation and Operation

**Question 1: Which command is executed in the shell of an Ubuntu LXC container to install MariaDB as the database server?**

A. `sudo apt install mysql-server`
> **Hint:** This would install the original MySQL server from Oracle. MariaDB is a fork.

B. `sudo mariadb --install`
> **Hint:** This is not a valid `apt` or shell command for installation.

C. `sudo systemctl start mariadb`
> **Hint:** This is the command to start the service, not to install the package.

D. `sudo apt get install mariadb-db`
> **Hint:** The correct `apt` command uses `apt install`.

**E. `sudo apt install mariadb-server`**
> **Hint:** **Correct.** This is the standard package name for the MariaDB server on Debian/Ubuntu.

---

### 2. Security and Configuration

**Question 2: What is the purpose of changing the `bind-address = 127.0.0.1` setting in the MariaDB configuration file (`50-server.cnf`) to a specific container IP (e.g., `192.168.137.120`)?**

A. The database will only be accessible via the Unix Socket.
> **Hint:** Changing to an IP does not remove socket access, but it blocks external TCP connections if only `127.0.0.1` is set.

B. MariaDB performance is optimized by a dedicated IP.
> **Hint:** Performance is not directly affected, only network reachability.

C. The default port 3306 is redirected to port 80.
> **Hint:** The `bind-address` defines the interface, not the port.

D. The database is only accessible to local programs (localhost).
> **Hint:** The opposite is true: `127.0.0.1` makes it only locally accessible.

**E. The database becomes accessible to external clients in the network via this specific IP, in addition to the Localhost interface.**
> **Hint:** **Correct.** The database now "listens" on this IP and allows remote connections, provided the firewall port 3306 is open.

---

### 3. User Management and Permissions

**Question 3: Which SQL command is necessary to immediately activate changes after creating a new database user and setting permissions, without restarting the MariaDB service?**

A. `COMMIT;`
> **Hint:** `COMMIT` is used to end transactions, not to update the privilege tables.

B. `UPDATE PRIVILEGES;`
> **Hint:** This is not a valid SQL statement for updating permissions.

C. `RESTART SERVICE;`
> **Hint:** This would be an operating system command (`systemctl`), not SQL, and is unnecessary.

D. `ENABLE USER 'pdal';`
> **Hint:** The user is active immediately after `CREATE USER`.

**E. `FLUSH PRIVILEGES;`**
> **Hint:** **Correct.** This command instructs MariaDB to reload the permissions held in memory from the grant tables.

---

### 4. Character Encoding

**Question 4: What effect does the setting `collation-server = utf8mb4_general_ci` in the MariaDB configuration have on text comparisons and sorting?**

A. It speeds up queries on text fields.
> **Hint:** Collations affect the logic, not directly the speed (compared to other collations).

B. It enforces the use of the old `utf8` character set.
> **Hint:** `utf8mb4` is the modern, extended version of UTF-8.

**C. Text comparisons are "Case-Insensitive" (uppercase and lowercase are not distinguished).**
> **Hint:** **Correct.** The suffix `_ci` (Case Insensitive) causes "Test" and "test," for example, to be treated as equivalent.

D. Text comparisons are "Case-Sensitive" (uppercase and lowercase are distinguished).
> **Hint:** This would require the suffix `_cs` (Case Sensitive).

E. Only the ASCII character set is supported.
> **Hint:** `utf8mb4` supports the full Unicode character set, including emojis and special characters.

---

### 5. phpMyAdmin Installation

**Question 5: Why is the answer "No" given to the question about configuration with `dbconfig-common` during the installation of phpMyAdmin (`apt install phpmyadmin php-mysql`) when MariaDB is running in a separate LXC container?**

A. `dbconfig-common` cannot manage MariaDB databases.
> **Hint:** The tool can manage both MySQL and MariaDB, but only if they are local or directly reachable.

B. `dbconfig-common` is outdated and should no longer be used.
> **Hint:** The tool is still part of the Debian/Ubuntu repositories.

C. The installation would fail because PHP is not running on the MariaDB container.
> **Hint:** The failure is due to the missing local database.

D. The database structure will later be created manually via the phpMyAdmin WebGUI.
> **Hint:** The structure (`create_tables.sql`) is created manually, but via the host and client, not the WebGUI.

**E. The database is running externally, and `dbconfig-common` attempts to create and link the necessary configuration database locally, which would fail or be undesirable.**
> **Hint:** **Correct.** Since the database is on a different host, the configuration must be performed manually.

---

### 6. phpMyAdmin Connection

**Question 6: Which configuration line in `/etc/phpmyadmin/config.inc.php` in the Apache container must be adjusted to establish the connection to the external MariaDB IP (`192.168.137.120`)?**

A. `$cfg['Servers'][$i]['ip'] = '192.168.137.120';`
> **Hint:** The correct key for the host address is not `ip`.

B. `$cfg['Servers'][$i]['bind-address'] = '192.168.137.120';`
> **Hint:** `bind-address` is a MariaDB server parameter, not a phpMyAdmin client parameter.

C. `$cfg['Servers'][$i]['database'] = '192.168.137.120';`
> **Hint:** The `database` key would set the name of the default database.

D. `if (empty($dbserver)) $dbserver = '192.168.137.120';`
> **Hint:** While this line is supplemented, it is not the main configuration line for the host.

**E. `$cfg['Servers'][$i]['host'] = '192.168.137.120';`**
> **Hint:** **Correct.** The `host` key defines the IP address of the database server to which phpMyAdmin should connect.

---

### 7. Advanced phpMyAdmin Features

**Question 7: What is the main purpose of the `phpmyadmin` database (with the `pma__*` tables) after its creation and linking in the configuration file (`config.inc.php`)?**

A. It stores the actual user data of the web application.
> **Hint:** The database is intended only for phpMyAdmin's own administrative tasks.

B. It serves as temporary storage for large SQL queries.
> **Hint:** The database contains persistent configuration data, not temporary queries.

C. It stores the logins and passwords of the database users.
> **Hint:** MariaDB stores passwords internally; phpMyAdmin does not store them.

D. It stores the Apache2 access logs for later analysis.
> **Hint:** This is a task for the web server or a log server.

**E. It enables advanced phpMyAdmin features such as the Designer, Bookmarks, and Relations display.**
> **Hint:** **Correct.** The configuration storage (Advanced Features) is needed to activate these additional functions, as they must store metadata.

---

### 8. Host as a Bridge

**Question 8: Which Proxmox command is used to copy the `create_tables.sql` file back from the MariaDB container (CT 120) to the Proxmox host after it has been executed there?**

A. `pct exec 120 -- cp /tmp/create_tables.sql /root/`
> **Hint:** This command only copies the file *within* the container.

B. `pct move 120 /tmp/create_tables.sql /root/`
> **Hint:** `pct move` is intended for moving the *entire container*.

C. `scp /tmp/create_tables.sql root@120:/root/`
> **Hint:** This would be network-based `scp` and requires SSH access and configuration.

**D. `pct pull 120 /tmp/create_tables.sql /root/`**
> **Hint:** **Correct.** The `pct pull` command copies files *from* the container *to* the host.

E. `pct push 120 /tmp/create_tables.sql /root/`
> **Hint:** `pct push` copies files *from* the host *into* the container.

---

### 9. Systemd and MariaDB

**Question 9: What is the main reason for executing the command `sudo systemctl enable mariadb` after installing the MariaDB server?**

A. It configures the database for remote access.
> **Hint:** The `bind-address` in the configuration is responsible for this.

B. It executes the security script `mysql_secure_installation`.
> **Hint:** The script must be called separately.

C. It ensures the database is started immediately.
> **Hint:** The command `systemctl start` is responsible for this.

D. It installs all necessary MariaDB dependencies.
> **Hint:** This is the job of `apt install`.

**E. It ensures that the MariaDB service automatically restarts after a container reboot.**
> **Hint:** **Correct.** `enable` creates the necessary symlink so that the service is activated at system startup (persistence).

---

### 10. Troubleshooting in phpMyAdmin

**Question 10: If a `Access denied` error occurs in phpMyAdmin, what is the most likely cause in the MariaDB container if the user `pdal` exists on the database side?**

A. The `bind-address` in MariaDB is set to `0.0.0.0`.
> **Hint:** `0.0.0.0` would *enable* access, not block it (provided the firewall allows it).

B. The MariaDB service was not started with `systemctl start`.
> **Hint:** Then it would be a connection error, not `Access denied`.

C. The Apache firewall blocks port 80.
> **Hint:** This would prevent access to the phpMyAdmin website, not the database access.

D. The configuration database (`phpmyadmin`) was not created.
> **Hint:** This would only trigger the "Advanced Features" warning, not block the login.

**E. The user `pdal` does not have permission in the MariaDB database for the host address of the Apache container (e.g., `192.168.137.101`).**
> **Hint:** **Correct.** `Access denied` means the database server does not accept the combination of username, password, and **host address** (where the connection originates).

---

### License
This work is licensed under the **Creative Commons Attribution - ShareAlike 4.0 International License**.
 
[To the license text on the Creative Commons website](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en)
