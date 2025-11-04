---
title: "Functional Check List: pgAdmin4 on LXC"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "uwe.bachmann@jade-hs.de"
organization: "PDAL Project"
date: "2025-10-30"
version: "1.0.0"
level: "Level 2, Learning Unit 2.6.5, Assessment"
duration: "0.2 Hrs"
prerequisites:["Completed - 2600 Installing, Configuring, and Securing PostgreSQL on LXC"]
tags: ["PDAL","Assessment", "pgAdmin4", "Functionality Check"]
license: "CC BY-SA 4.0"
---

# ✅ Functional Check List: pgAdmin4 on LXC

This checklist serves to verify that the installation of pgAdmin4 and the connection to the PostgreSQL server have been successfully established.

---

### 1. Web Accessibility

**Is the pgAdmin4 web interface reachable from the host system via the configured URL (`http://192.168.137.130/pgadmin4`) and does the login page appear?**

* **Yes**
    * **Hint:** The Apache2 web server is running, the `pgadmin4.conf` is correctly configured, and the firewall allows access to port 80.
* **No**
    * **Hint:** Check if the Apache2 service is started, if UFW Port 80 (HTTP) is open, and if the URL correctly includes the path `/pgadmin4`.

### 2. Initial Login

**Were you able to successfully log into the pgAdmin4 interface using the Admin email address and password created in **Step 5**?**

* **Yes**
    * **Hint:** The initial configuration (`setup-web.sh`) was completed successfully, and the local SQLite user database (`pgadmin4.db`) was correctly created.
* **No**
    * **Hint:** Run the script `/usr/pgadmin4/bin/setup-web.sh` again and ensure you have noted the login credentials.

### 3. Network Access (PostgreSQL)

**Can the PostgreSQL server (`192.168.137.160`) be successfully added in pgAdmin4 via the **Connection** tab when the **SSL Mode is temporarily set to `disable`**?**

* **Yes**
    * **Hint:** The `pg_hba.conf` on the PostgreSQL server allows the IP of the pgAdmin container, and the basic network connection is working.
* **No**
    * **Hint:** Check the `pg_hba.conf` on the PostgreSQL server (must allow the IP of the pgAdmin container) and the `postgresql.conf` (`listen_addresses = '*'`).

### 4. Database Display

**After a successful connection (e.g., with the `pdal` user), are the previously created database (`pdal`) and the **example table** (`beispiel`) displayed in the pgAdmin4 tree structure on the left side?**

* **Yes**
    * **Hint:** The connection information (User, Host, DB Name) is correct, and the user has the necessary rights (`CONNECT`) on the database.
* **No**
    * **Hint:** Ensure that the user employed has the correct database rights and that the database and table actually exist (check with `\l` and `\dt` in the `psql` console).

### 5. SSL Functionality

**Can a connection to the PostgreSQL server be successfully established when the **SSL Mode** in pgAdmin4 is set to **`require`** (and not `disable`)?**

* **Yes**
    * **Hint:** SSL encryption (`ssl = on`) is correctly configured on the PostgreSQL server, and the server enforces or accepts encrypted connections.
* **No**
    * **Hint:** Check the PostgreSQL server's log files (`/var/log/postgresql/`) for SSL errors. Ensure that `ssl = on` is active in the `postgresql.conf` and that the required certificates exist.

---

### License
This work is licensed under the **Creative Commons Attribution-ShareAlike 4.0 International License**.

[To the license text on the Creative Commons website](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)
