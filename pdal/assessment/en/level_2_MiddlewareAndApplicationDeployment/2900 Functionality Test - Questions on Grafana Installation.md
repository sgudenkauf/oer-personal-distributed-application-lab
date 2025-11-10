---
title: "Questions on Grafana Installation"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "uwe.bachmann@jade-hs.de"
organization: "PDAL Project"
date: "2025-11-07"
version: "1.0.0"
level: "Level 2, Learning Unit 2.8, Assessment"
duration: "0.2 Hrs"
prerequisites:["Completed - 2900 Install Grafana in an LXC Container"]
tags: ["PDAL","Assessment", "Grafana", "Functionality Check"]
license: "CC BY-SA 4.0"
---

## 🛠️ Functionality Test: Questions on Grafana Installation

**Integrate Grafana Repository**
The Grafana repository is successfully integrated (Section 5). After `sudo apt update`, a line was displayed in the console indicating the Grafana repository (e.g., "Hit:X [https://apt.grafana.com](https://apt.grafana.com) stable InRelease").
 - **True:**
    -- **Hint:** This confirms that the modern GPG key management was successful and the repository is recognized.
- **False:**
    -- **Hint:** Check the commands in Section 5. The file `/etc/apt/sources.list.d/grafana.list` was likely not created correctly.

**Set up Service**
The Grafana service is successfully started (Section 7). The query `sudo systemctl status grafana-server` showed the service as **`active (running)`** and **`enabled`**.
- **True:**
    -- **Hint:** The service is running and will start automatically the next time the container is rebooted.
- **False:**
    -- **Hint:** Run `sudo systemctl enable grafana-server` and then `sudo systemctl start grafana-server` again.

**Test Web Connection**
Initial access via HTTP is functional (Section 8). The browser could reach the Grafana login page via `http://<IP-Address>:3000` and prompted for username and password.
- **True:** The login page loaded correctly.
    -- **Hint:** This confirms that Grafana is running and the network is configured correctly in the container.
- **False:**
    -- **Hint:** Check the service status and ensure you are using the correct IP address and **Port 3000**.

**First Login**
Admin password was secured (After Section 8). After the initial login with `admin`/`admin`, the password was successfully changed, and a subsequent login with the new password was successful.
- **True:**
    -- **Hint:** This confirms that the database initialization and basic user management are working.
- **False:**
    -- **Hint:** Clear browser cookies/cache and repeat the initial login process with the standard password to ensure the change is saved correctly.

**Set up TLS**
Secure access is functional (Section 9.5). The Grafana web interface is reachable via `https://<IP-Address>` and the browser shows **no certificate warning** (assuming the internal CA is integrated on the client).
- **True:**
    -- **Hint:** This is the final goal of the security setup: the service is reachable via TLS, and the certificate is trusted by the client.
- **False:** 
    -- **Hint:** Ensure you have executed `sudo systemctl restart grafana-server` and that the internal CA is correctly installed on the client PC (Section 9.6).

---

## License

This work is licensed under the **Creative Commons Attribution - NonCommercial - ShareAlike 4.0 International License**.

[Link to the license text on the Creative Commons website](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)