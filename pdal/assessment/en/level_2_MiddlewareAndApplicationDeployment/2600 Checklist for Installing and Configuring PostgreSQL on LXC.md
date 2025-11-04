---
title: "Checklist for Installing and Configuring PostgreSQL on LXC"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "uwe.bachmann@jade-hs.de"
organization: "PDAL Project"
date: "2025-09-25"
version: "1.0.0"
level: "Level 2, Learning Unit 2.3, Assessment"
duration: "0.2 Hrs"
prerequisites:["Completed - 2600 Installing and Configuring PostgreSQL on LXC"]
tags: ["PDAL","Assessment"]
license: "CC BY-SA 4.0"
---

# ❓ Checklist for Installing and Configuring PostgreSQL on LXC

### Installation

**Does the package `postgresql-contrib` absolutely have to be installed along with PostgreSQL 16 to utilize the basic functionality of the DBMS?**

* **Yes**
    * **Hint:** This is incorrect. `postgresql-contrib` contains optional extensions and functions, such as `pg_trgm` or `dblink`. The core installation is covered by the main package `postgresql-16`.
* **No**
    * **Hint:** This is correct. `postgresql-contrib` only contains optional extensions. Only the main package `postgresql-16` is required for the basic functionality of the database management system.

### Logging into the Database

**Is the command `sudo -u postgres psql` the only way to log into the PostgreSQL database locally on the LXC console after installation?**

* **Yes**
    * **Hint:** This is incorrect. After adjusting the `pg_hba.conf` and setting the password, you can also log in directly with the created system administrator user `pdal`, for example, `psql -U pdal`.
* **No**
    * **Hint:** This is correct. The command `sudo -u postgres psql` uses the Linux system's `peer` authentication. Later, you can also log in with other created PostgreSQL users and the command `psql -U <User>`, provided password authentication is enabled.

### Creating Users

**Can the user `dbadmin_pdal` create new databases system-wide (e.g., `CREATE DATABASE testdb;`) without further rights?**

* **Yes**
    * **Hint:** This is incorrect. The `dbadmin_pdal` has been assigned the role `db_admin`, which **does not** possess the `CREATEDB` right. Only the superuser (`db_system_admin` / `pdal`) has this right.
* **No**
    * **Hint:** This is correct. The role `db_admin` was intentionally created **without** the `CREATEDB` right to keep the responsibility for database creation with the superordinate system administrator (`pdal`).

### Rights Management

**Will local login for all users automatically switch to password authentication after changing `peer` to `md5` in the `pg_hba.conf`, even without explicitly setting a password?**

* **Yes**
    * **Hint:** This is incorrect. Although changing to `md5` **enforces** password checking, the password for the affected PostgreSQL users (`pdal`, `dbadmin_pdal`, etc.) must have been **set beforehand** in the SQL console.
* **No**
    * **Hint:** This is correct. The `pg_hba.conf` change merely forces the server to request a password. If this password does not yet exist in the PostgreSQL system, the login will fail.

### Creating Tables

**Does the `standard_user` (`appuser_pdal`) have to explicitly receive the rights `SELECT, INSERT, UPDATE, DELETE` for every newly created table within the database `pdal` in order to edit data?**

* **Yes**
    * **Hint:** This is incorrect. Thanks to the command `ALTER DEFAULT PRIVILEGES IN SCHEMA public ...`, the `appuser_pdal` automatically receives these rights on all **future** tables created in this schema.
* **No**
    * **Hint:** This is correct. The **Default Privileges** were set for the `appuser_pdal` so that they do not have to be manually granted permissions for every new table.

---

### License
This work is licensed under the **Creative Commons Attribution-ShareAlike 4.0 International License**.

[To the license text on the Creative Commons website](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)