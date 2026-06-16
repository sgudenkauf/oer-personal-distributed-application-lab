---
title: "Checklist for REST Service Verification"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "pdal@jade-hs.de"
organization: "PDAL-Projekt"
date: "2025-09-25"
version: "1.0.0"
level: "Level 2, Learning Unit 2.3, Assessment"
duration: "0.2 Hrs"
prerequisites: ["Completed - 2500 Install and Configure MQTT on an existing LXC"]
tags: ["PDAL","Assessment"]
license: "CC BY-SA 4.0"
---

# ✅ Checklist for MQTT Functionality Verification (Implementation Check)

These questions serve as a Yes/No check to verify whether the installation and configuration steps were successfully completed according to the documentation.

***

### Basic Configuration and Installation

**Installation and Activation Successful**

Were the packages **`mosquitto`** and **`mosquitto-clients`** successfully installed, and could the `mosquitto` service be activated (`enable`) and started (`start`)?

* **Yes (Note for successful completion):** The commands `sudo apt install -y mosquitto mosquitto-clients` and `sudo systemctl start mosquitto` were executed successfully and without errors.
* **No (Note for correction):** Check the internet connection of the LXC container and run **`sudo apt update`** before the installation. Start the service (`sudo systemctl start mosquitto`) again.

**Service Status Correct**

Does the command **`sudo systemctl status mosquitto`** show that the service is **running** (`active (running)`) and configured for automatic startup (`enabled`)?

* **Yes (Note for successful completion):** The status output shows **`active (running)`** in green text and **`enabled`** in the "Loaded" line.
* **No (Note for correction):** Use **`sudo systemctl enable mosquitto`** for activation and **`sudo systemctl restart mosquitto`** to restart the service.

***

### Anonymous Communication (Phase 1)

**Anonymous Configuration Compldete**

Was the configuration file **`/etc/mosquitto/mosquitto.conf`** adjusted so that **`listener 1883`** and **`allow_anonymous true`** are set, and was the service restarted afterward?

* **Yes (Note for successful completion):** Both lines are present in the configuration file, and the command **`sudo systemctl restart mosquitto`** was executed.
* **No (Note for correction):** Edit the file with `sudo nano /etc/mosquitto/mosquitto.conf`, add the lines, and ensure the service is restarted so the configuration is applied.

**Host Client Test Successful**

Could a message be **sent (`mosquitto_pub`)** and successfully **received (`mosquitto_sub`)** from the broker's host (e.g., via port 1883)?

* **Yes (Note for successful completion):** The `mosquitto_sub` command displayed the message ("Hallo MQTT") after it was sent by the `mosquitto_pub` command.
* **No (Note for correction):** Verify that the broker's IP address is correct in the command and that the broker is running (see "Service Status Correct" question). If necessary, test with **`localhost`** instead of the IP first.

**MQTT Explorer Test Successful**

Could the **MQTT Explorer** successfully connect to the broker **without** providing a username/password and see the test messages?

* **Yes (Note for successful completion):** The MQTT Explorer showed the connection status as **"Connected"** and listed the `test/topic`.
* **No (Note for correction):** Check the IP address and **Port (1883)** in the MQTT Explorer's connection settings. Ensure that no firewall is blocking the connection.

***

### Password-Protected Communication (Phase 2)

**User Creation Successful**

Was at least one user (**`pdal` or `Kai`**) created using **`sudo mosquitto_passwd`** and stored in the file `/etc/mosquitto/passwords/mqtt_users`?

* **Yes (Note for successful completion):** The file **`mqtt_users`** exists and contains the encrypted username and password.
* **No (Note for correction):** Execute the command `sudo mosquitto_passwd -c /etc/mosquitto/passwords/mqtt_users pdal` (or `Kai`) again and assign the password.

**Authenticated Client Test Successful**

Could a message be successfully published using the **`mosquitto_pub`** command **only** by providing the **user (`-u`)** and **password (`-P`)**?

* **Yes (Note for successful completion):** The command worked **with** the user/password and failed **without** these parameters (after `allow_anonymous false` was set).
* **No (Note for correction):** Check the correct spelling of the username and password. Ensure that **`allow_anonymous false`** is set in `mosquitto.conf` and that the service has been restarted.

***

### Access Control (Phase 3: ACLs)

**ACL File Created and Configured**

Was the ACL file **`/etc/mosquitto/acl`** created with at least one **`user`** and the associated **`topic`** permissions (`read`, `write`, or `readwrite`) and referenced in **`mosquitto.conf`**?

* **Yes (Note for successful completion):** The file `/etc/mosquitto/acl` exists with content, and the line **`acl_file /etc/mosquitto/acl`** was added to `mosquitto.conf`.
* **No (Note for correction):** Create the file with `nano /etc/mosquitto/acl` and insert the example from the documentation. Then, edit `mosquitto.conf`.

**Read Permission Tested**

Does the attempt to subscribe to a topic for which the user **lacks `read` permission** result in the subscriber **receiving no messages**?

* **Yes (Note for successful completion):** A test client without read permission for a specific topic receives no messages, while a client with read permission does (e.g., User "Kai" trying to read the topic `pdal/#`, which fails).
* **No (Note for correction):** Check the syntax of the **`topic read`** line in the ACL file. A wildcard rule (e.g., `#` or `+`) might be unintentionally allowing access.

---

### License
This work is licensed under the **Creative Commons Attribution - ShareAlike 4.0 International License**.

[To the license text on the Creative Commons website](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en)