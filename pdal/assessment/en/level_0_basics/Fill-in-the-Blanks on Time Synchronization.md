---
title: "Fill-in-the-Blanks on Time Synchronization"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "pdal@jade-hs.de"
organization: "PDAL Project"
date: "2025-08-20"
version: "1.0.0"
level: "Level 0, Learning Unit 0.2, Assessment"
duration: "0.2 hours"
prerequisites:["Completed - Document: 0260 - Explanation of why time synchronization is important"]
tags: ["PDAL","Assessment"]
license: "CC BY-SA 4.0"
---

### Fill-in-the-Blanks on Time Synchronization (Drag and Drop)

A precise and consistent system time is crucial in IT systems and *virtualization environments* like Proxmox VE.

Many *security mechanisms* (e.g., TLS/SSL certificates, tokens, logins) are *time-dependent*. Inaccurate time can cause *certificates* to appear invalid or authentications to fail.

Consistent time stamps in system logs are essential for *error analysis* and monitoring. Time differences make it difficult to trace event chains in *distributed* systems.

In a Proxmox cluster, an identical time base between hosts is *mandatory*. Without *synchronization*, problems can occur with quorum formation, migration, or *replication*.

Time-controlled processes such as Cronjobs, backups, and updates depend on correct *time stamps*. Incorrect times lead to missed or repeatedly executed tasks.

---

### License
This work is licensed under the **Creative Commons Attribution - ShareAlike 4.0 International License**.
 
[To the license text on the Creative Commons website](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en)
