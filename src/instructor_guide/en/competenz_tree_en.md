---
title: "Competency Tree Structure: Bottom-Up Learning Path for Distributed Systems in the PDAL"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe"]
email: "pdal@jade-hs.de"
organization: "PDAL Project"
date: "2025-08-11"
version: "1.0.0"
level: "Instructor guide"
duration: "N/a"
prerequisites:["none"]
tags: ["PDAL", "Fundamentals", "Infrastructure", "Didactics", "Instructor Guide"]
license: "CC BY-SA 4.0"
---

# Competency Tree Structure: Bottom-Up Learning Path for Distributed Systems in the PDAL (Granular & Expanded)

---

**Root Competency (The Ultimate Goal):**
* **Gaining experience with distributed applications and middleware systems**
    * *Competency: Design & Implementation of Multi-Service Architectures (Level 4)*

---

## Individual Learning Path: Your Journey to a Personal Distributed Applications Lab (PDAL)

This competency tree serves as a guide for your individual learning path within the PDAL project. The modules are primarily designed as **self-learning modules**, allowing learners to work at their own pace.

To build a solid knowledge base, we recommend completing the **fundamental modules of Level 0 and Level 1**. These modules lay the absolute foundation for all subsequent steps.

Afterward, you can design the learning path **flexibly and according to the learners' interests**. Many modules are deepening and consolidation tasks that serve to substantiate theoretical content through practical experiments. Additionally, **your own, topic-specific modules** can be integrated into the learning path as needed to focus on specific technologies or use cases.

The goal is to provide you with a structured yet adaptable framework to systematically build and deepen your competencies in handling distributed applications and middleware systems.

---

### Level 4: Building & Testing Complex Distributed Applications (Approx. 10-25 hours per learning unit)

* **Competency: Design & Implementation of Multi-Service Architectures**
  * **Description:** The ability to design and implement a multi-layered, distributed application and test its interactions within the PDAL. This includes understanding fault tolerance and documenting one's own project.
  * *Prerequisite: Competency "Analysis & Troubleshooting in Distributed Systems" (Level 3)*
    * **Learning Units (Qualifications):**
      * **Learning Unit 4.1: Designing a Simple Microservices Application (3-5 hours)**
        * **Goal:** Understanding the concepts of microservices and designing a minimal, distributed application (e.g., a frontend, a backend API service, a data service).
        * **Content:** Introduction to microservices, sketching the architecture and communication between services.
      * **Learning Unit 4.2: Implementing the Frontend Microservice (3-7 hours)**
        * **Goal:** Developing and deploying a simple web frontend in an LXC that communicates with the backend.
        * **Content:** Choosing a technology (e.g., Python Flask, Node.js Express, a simple static web server), implementation, deployment in the LXC.
      * **Learning Unit 4.3: Implementing the Backend API Microservice (3-7 hours)**
        * **Goal:** Developing and deploying a **REST API service** in an LXC that processes data and, if necessary, uses a database.
        * **Content:** REST API design (HTTP methods, status codes), data modeling, implementing the logic, deployment in the LXC.
      * **Learning Unit 4.4: Integration and Testing of the Multi-Service Scenario (5-10 hours)**
        * **Goal:** Testing the interaction of all microservices, verifying end-to-end functionality, and basic application-level troubleshooting.
        * **Content:** Network communication between services, configuring environment variables, testing strategies.
      * **Learning Unit 4.5: Fundamentals of Container Orchestration (Optional/Outlook, 5-10 hours)**
        * **Goal:** First steps with Docker and Docker Compose within an LXC for simple orchestration of multiple service containers.
        * **Content:** Installing Docker in an LXC, Dockerfiles, Docker Compose files, starting multi-container applications.
      * **Learning Unit 4.6: Experiments on Fault Tolerance & Resilience (5-10 hours)**
        * **Goal:** Deliberately introducing errors (e.g., disconnecting the network, stopping a service) and analyzing the impact on the distributed application. Initial considerations for resilient designs.
        * **Content:** Chaos Engineering light, error logging, impact on availability.
      * **Learning Unit 4.7: JavaServer Application Project (3-5 hours)**
        * **Goal:** Creating an LXC with a TomCat server and developing a JSP in the PDAL.
        * **Content:** Installing Apache Tomcat, developing a JSP, deploying the JSP on Tomcat, implementing a database in the JSP.
      * **Learning Unit 4.8: Project Documentation (3-5 hours)**
        * **Goal:** Creating clear documentation of the setup, configuration, and functionality of the distributed application developed in the PDAL.
        * **Content:** Architecture diagrams, configuration steps, test cases.

---

### Level 3: System Interaction & Troubleshooting Competence (Approx. 5-15 hours per learning unit)

* **Competency: Analysis & Troubleshooting in Distributed Systems**
  * **Description:** The ability to understand the communication and dependencies between different services and to systematically identify and resolve problems that arise.
  * *Prerequisite: Competency "Deployment & Configuration of Distributed System Components" (Level 2)*
  * **Learning Units (Qualifications):**
    * **Learning Unit 3.1: Fundamentals of Network Communication Analysis (5-8 hours)**
      * **Goal:** Learning to use `tcpdump` or `wireshark` for packet analysis between containers.
      * **Content:** Installing the tools, filtering traffic, identifying source/destination IPs and ports, basic protocol analysis (HTTP, DNS).
    *  **Learning Unit 3.2: Advanced Log Analysis (3-5 hours)**
       *   **Goal:** Effectively finding, filtering, and interpreting system and application logs in Linux containers for troubleshooting.
       *    **Content:** `journalctl` (systemd logs), `grep`, `tail -f`, log rotation, meaning of common log messages, debug mode.
    *  **Learning Unit 3.3: Analysis of Dependencies and Their Effects (3-5 hours)**
       *   **Goal:** Creating a dependency diagram for a simple distributed application and simulating service failures.
        * **Content:** Service maps, understanding call chains, effects of latency and failures.
      * **Learning Unit 3.4: Resource Monitoring and Performance Analysis (4-7 hours)**
        * **Goal:** Monitoring CPU, RAM, network I/O, and disk usage in LXC containers to identify performance bottlenecks.
        * **Content:** `htop`, `nmon`, `iostat`, `dstat`, `ss`, interpreting metrics.

---

### Level 2: Middleware and Application Deployment Competence (Approx. 5-15 hours per learning unit)

* **Competency: Deployment & Configuration of Distributed System Components**
  * **Description:** The ability to install and configure various middleware systems and applications (web servers, databases, message brokers, etc.) in individual LXC containers for distributed communication.
  * *Prerequisite: Competency "Effective Management of Linux LXC Containers" (Level 1)*
    * **Learning Units (Qualifications):**
      * **Learning Unit 2.05: Creating Your Own Certificate Authority (CA) (2-3 hours)**
        * **Goal:** Integrating a custom certificate management system into the PDAL and using the certificates on different servers.
        * **Content:** `apt install openSSL`, creating a root certificate, creating server/service certificates, creating a private key and distributing it to different locations (not automated).
      * **Learning Unit 2.1: Web Server Apache2: HTTP and PHP (5-8 hours)**
        * **Goal:** Installation and basic configuration of Apache2 as a web server, serving HTTP content, and integrating PHP.
        * **Content:** `apt install apache2 php libapache2-mod-php`, configuration files, virtual hosts, `phpinfo()`.
      * **Learning Unit 2.2: MariaDB and phpMyAdmin Integration (5-8 hours)**
        * **Goal:** Installation of MariaDB as a database server and phpMyAdmin for administration. Connecting to Apache2/PHP.
        * **Content:** `apt install mariadb-server phpmyadmin`, user and permission management in MariaDB, phpMyAdmin configuration, creating simple databases and tables.
      * **Learning Unit 2.2.1: PostgreSQL Database and Database Management System (DBMS) pgadmin4**
        * **Goal:** Installing PostgreSQL and pgadmin4, creating different user groups/users, creating a database and assigning permissions, securing with SSL.
        * **Content:** `apt install postgres`, user and permission management, SSL certificates, configuring PostgreSQL and pgadmin.
      * **Learning Unit 2.3: Custom Web Application (HTML/PHP) with Database Connection (5-10 hours)**
        * **Goal:** Developing a simple web application in HTML/PHP that stores and retrieves data in MariaDB, accessible via Apache2.
        * **Content:** Basic PHP scripts for database interaction, form processing, simple CRUD operations (Create, Read, Update, Delete).
      * **Learning Unit 2.4: REST Applications: Custom Development and External Use (5-10 hours)**
        * **Goal:** Developing a simple custom **REST API** (e.g., with Python Flask or PHP) and using an external REST API from another application/service.
        * **Content:** HTTP methods (GET, POST, PUT, DELETE), JSON data format, implementing an API endpoint, `curl` or Python `requests` for external API calls.
      * **Learning Unit 2.5: MQTT Broker (Mosquitto): Anonymous & Authenticated (6-10 hours)**
        * **Goal:** Installing and configuring the Mosquitto MQTT broker for anonymous and authenticated connections (username/password).
        * **Content:** `apt install mosquitto`, `mosquitto.conf`, `mosquitto_passwd`, ACLs, testing with `mosquitto_pub`/`mosquitto_sub`.
      * **Learning Unit 2.6: MQTT Client Implementation (Python & Java) (8-12 hours)**
        * **Goal:** Developing custom publisher and subscriber applications in Python and Java that communicate with the configured MQTT broker.
        * **Content:** Using MQTT libraries (e.g., Paho MQTT for Python/Java), topics, QoS levels, sending/receiving messages.
      * **Learning Unit 2.7: MQTT Broker: TLS Encryption (4-6 hours)**
        * **Goal:** Securing MQTT communication with TLS/SSL using custom certificates (from Learning Unit 2.8).
        * **Content:** TLS configuration in `mosquitto.conf`, client certificate validation.
      * **Learning Unit 2.8: Certificate Management and HTTPS for Apache2 (4-6 hours)**
        * **Goal:** Setting up a simple local CA in a container and creating/signing SSL/TLS certificates for Apache2 to enable **HTTPS**.
        * **Content:** OpenSSL commands (CA, keys, CSR, signing), Apache2 SSL module (`a2enmod ssl`), configuration of SSL virtual hosts.
      * **Learning Unit 2.9: JupyterLab: Python, Java, R for Data Analysis & Interaction (6-10 hours)**
        * **Goal:** Installing and configuring JupyterLab and using it for interactive scripts and data analysis in Python, Java, and R.
        * **Content:** `apt install jupyterlab`, installing kernels (Python, IJava, R-kernel), integrating external libraries (e.g., `pandas`, `requests`, `paho`), writing simple code cells to interact with other PDAL services (e.g., REST API calls, MQTT publishing).
      * **Learning Unit 2.10: Grafana: Monitoring and Visualization (8-12 hours)**
        * **Goal:** Installing and configuring Grafana for visualizing data from MariaDB or other sources (e.g., Prometheus Node Exporter in LXCs).
        * **Content:** `apt install grafana`, adding data sources (MariaDB, Prometheus), creating custom dashboards with different visualizations, querying data.

---

### Level 1: Operating System and Container Management Competence (Approx. 3-8 hours per learning unit)

* **Competency: Effective Management of Linux LXC Containers**
  * **Description:** The ability to provision, configure, and perform basic Linux tasks within Ubuntu LTS LXC containers.
  * *Prerequisite: Competency "Mastering PDAL Hardware & Basic Virtualization" (Level 0)*
    * **Learning Units (Qualifications):**
      * **Learning Unit 1.1: First Ubuntu LTS LXC Container (2-3 hours)**
        * **Goal:** Successfully creating an Ubuntu LTS LXC container from a Proxmox template and the first login.
        * **Content:** Selecting the template, resource allocation, configuring the network (DHCP), starting the container, logging in via console/SSH.
      * **Learning Unit 1.2: Basic Linux Shell Navigation and Commands (3-5 hours)**
        * **Goal:** Confidently using basic Linux commands for filesystem, user, and process management.
        * **Content:** `cd`, `ls`, `mkdir`, `rm`, `cp`, `mv`, `cat`, `more`, `less`, `sudo`, `useradd`, `passwd`, `ps`, `top`, `kill`, `df`, `du`.
      * **Learning Unit 1.3: Network Configuration and Diagnosis in the Container (2-4 hours)**
        * **Goal:** Configuring static IPs in the container and effectively using network diagnostic tools.
        * **Content:** Editing `/etc/netplan` or `/etc/network/interfaces`, `ping`, `ip a`, `ip r`, `netstat -tulnp`, `curl`, `wget`.
      * **Learning Unit 1.4: Software Installation and Package Management (2-3 hours)**
        * **Goal:** Confidently using `apt` for installing, updating, and removing software packages.
        * **Content:** `apt update`, `apt upgrade`, `apt install`, `apt remove`, `apt search`, adding PPAs/repositories.
      * **Learning Unit 1.5: Creating Your Own Certificate Authority (CA) (2-3 hours)**
        * **Goal:** Integrating a custom certificate management system into the PDAL and using the certificates on different servers.
        * **Content:** `apt install openSSL`, creating a root certificate, creating server/service certificates, creating a private key and distributing it to different locations (not automated).
---

### Level 0: Basic Infrastructure Competence (The Absolute Foundation) (Approx. 1-5 hours per learning unit)

* **Competency: Mastering PDAL Hardware & Basic Virtualization**
  * **Description:** The fundamental ability to prepare the tiny PC hardware, install Proxmox, and establish the essential, isolated network connection for the PDAL.
  * *Prerequisite: No other competencies. This is the starting point.*
    * **Learning Units (Qualifications):**
      * **Learning Unit 0.1: Selecting and Preparing the Tiny PC (1-2 hours)**
        * **Goal:** Understanding hardware requirements and preparing the tiny PC for Proxmox installation.
        * **Content:** Minimum requirements (RAM, CPU, storage), BIOS/UEFI settings (enabling virtualization), boot order.
      * **Learning Unit 0.2: Installing Proxmox VE (2-4 hours)**
        * **Goal:** Successfully installing Proxmox VE on the tiny PC as a bare-metal hypervisor.
        * **Content:** Downloading the Proxmox ISO, creating a bootable USB stick, performing the installation, initial configuration (IP address, root password).
      * **Learning Unit 0.3: Basic Network Configuration of the Host PC (Windows) for ICS (2-3 hours)**
        * **Goal:** Correctly setting up Internet Connection Sharing (ICS) on Windows to provide the tiny PC with isolated internet access.
        * **Content:** Installing the USB network adapter, enabling ICS for the LAN connection (USB adapter), understanding the resulting IP address ranges (192.168.137.x).
      * **Learning Unit 0.4: First Access to the Proxmox Web Interface (1-2 hours)**
        * **Goal:** Successfully accessing the Proxmox management interface from the host PC and getting a first orientation in the dashboard.
        * **Content:** Entering the Proxmox IP in the browser, logging in with root credentials, overview of the main menu items.
      * **Learning Unit 0.5: Introduction to Proxmox Storage Management (1-2 hours)**
        * **Goal:** Understanding the different storage types in Proxmox and creating the first storage pool for container templates.
        * **Content:** Concepts of LVM, ZFS, directory as storage types, adding a directory, downloading the first LXC template.

---

### License
This work is licensed under the **Creative Commons Attribution - ShareAlike 4.0 International License**.
 
[To the license text on the Creative Commons website](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en)