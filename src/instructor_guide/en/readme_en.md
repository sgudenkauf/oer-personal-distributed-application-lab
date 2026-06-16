---
title: "Building a Personal Distributed Applications Lab (PDAL): Experimenting with Distributed Systems in a Protected Environment"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe"]
email: "pdal@jade-hs.de"
organization: "PDAL-Projekt"
date: "2025-08-11"
version: "1.0.0"
level: "Instructor guide"
duration: "N/a"
prerequisites:["none"]
tags: ["PDAL", "Basics", "Infrastructur", "Didaktic", "Instructure Guide"]
license: "CC BY-SA 4.0"
---

# Building a Personal Distributed Applications Lab (PDAL): Experimenting with Distributed Systems in a Protected Environment

## Motivation: Understanding and Mastering the Growing Importance of Distributed Applications

The digital landscape is increasingly dominated by distributed applications and systems. From web services to IoT platforms and microservice architectures, the ability to operate across multiple connected components and exchange data is now a core competency in software development and IT infrastructure. Understanding the complexity that these architectures bring—from network communication and latency to data consistency, fault tolerance, and security—is essential.

For students, developers, admins, or simply tech enthusiasts, the question often arises of how to approach this field without immediately investing in expensive and complex cloud infrastructures or risking existing production systems. Experimenting with distributed systems requires an isolated environment where you can safely test a wide range of configurations, reproduce errors, and try out new technologies.

This is precisely where the idea of a **Personal Distributed Applications Lab (PDAL)** comes in. A PDAL is a cost-effective, flexible, and secure test environment that allows individuals to gain practical experience with distributed applications and middleware systems. It provides the ideal platform to explore the challenges and solutions of distributed systems without having to take on the risks and effort of a "real" server environment. The motivation is clear: to develop a deep understanding of how distributed systems work and their pitfalls through practical experimentation.

---

## Brief Description: The PDAL in Detail – Structure and Functionality

The proposed PDAL is based on a minimalist approach that offers maximum flexibility with minimal cost and administrative effort. At its heart is a standard **Tiny PC**, which serves as the host for the virtualized components. The goal is to promote an understanding of distributed systems and distributed applications, not to provide high computing power.

### The Foundation: Proxmox as the Virtualization Platform

**Proxmox Virtual Environment** is chosen as the operating system and virtualization layer. Proxmox is a powerful, open-source server virtualization platform based on Debian that enables the management of virtual machines (VMs) and containers (LXC). The advantages of Proxmox in this context are manifold:

* **User-Friendliness:** Proxmox offers an intuitive web interface that significantly simplifies the creation, configuration, and management of VMs and LXC containers.
* **Performance:** Despite its flexibility, Proxmox is resource-efficient and can run stably even on less powerful hardware like a Tiny PC.
* **Flexibility:** It supports both KVM-based VMs and LXC containers, which allows for a wide range of application scenarios.

Installing Proxmox on the Tiny PC is the first step and forms the foundation of the PDAL.

### The Experimentation Environment: Ubuntu LTS LXC Containers

Within Proxmox, **Ubuntu LTS (Long Term Support) LXC containers** (Linux Containers) are used as the primary "virtual" machines for distributed applications. In contrast to full virtual machines, LXC containers are significantly more lightweight and offer significant advantages for such an experimentation lab:

* **Resource Efficiency:** LXC containers share the host system's kernel and therefore require significantly fewer resources (CPU, RAM, storage space) than traditional VMs. This is particularly advantageous for a Tiny PC with limited resources.
* **Rapid Deployment:** Creating and deleting LXC containers is extremely fast. This enables quick iteration through different configurations and the rapid setup of new test environments.
* **Isolation:** Although they share the kernel, LXC containers provide excellent process and file system isolation, so experiments in one container do not affect the others.

Within these Ubuntu LTS LXC containers, a wide variety of services and applications relevant to distributed systems can be installed and tested:

* **Web servers (e.g., Nginx, Apache):** For hosting APIs or static content.
* **Databases (e.g., PostgreSQL, MongoDB, Redis):** For storing and managing data, also in distributed setups (replication, sharding).
* **Message brokers (e.g., MQTT, Kafka, RabbitMQ):** For asynchronous communication and event streaming in distributed architectures.
* **Certificate Authority (CA):** For generating and managing SSL/TLS certificates for secure communication between containers.
* **Jupyter Notebooks:** For interactive data analysis and prototyping of distributed algorithms.
* **Java/Python code instances:** For implementing and testing custom network communication, microservices, or distributed algorithms.

By combining multiple LXC containers, complex scenarios such as microservice architectures, distributed database clusters, or IoT backends can be simulated. Each container represents a node in the distributed system.

---

### Network Connection: The Isolated Bridge to Success

A crucial aspect of the PDAL is its complete isolation from the production network. The Tiny PC's network connection is established via a **USB network card** connected to an Entry PC (Windows). **Internet Connection Sharing (ICS)** is enabled on this Entry PC to provide an isolated and controlled network connection for the PDAL. This configuration offers several advantages:

* **Separation from the Production Network:** The PDAL acts as a **completely closed system**. Experiments that cause network errors or faulty configurations cannot affect the home network or other production systems. This is particularly relevant in environments where operating unauthorized servers is strictly prohibited. With the PDAL, you can simulate and operate a **complete server landscape** without violating security policies or network rules, as your lab is only connected to the Entry PC and not directly to the production network.
* **Simple Configuration:** The Windows bridge forwards traffic from the Tiny PC to the internet (if needed, e.g., for software updates of the LXC containers) and at the same time enables communication between the Tiny PC and the host PC for management purposes (e.g., accessing the Proxmox web interface).
* **Security:** Since the PDAL is isolated, security concerns are significantly lower than with a system directly connected to the internet. Potentially insecure test applications or misconfigurations do not pose a risk to the home network. You can **test new software or configurations risk-free** without having to worry about data leaks or compromises in the production network.

---

## Benefits at a Glance: Why a PDAL is the Ideal Learning Platform

The architecture described here offers a number of compelling advantages that make it the ideal learning and experimentation environment for distributed applications:

1.  **Rapid Iteration:** LXC containers can be created, started, stopped, and deleted in seconds. This greatly accelerates the experimentation cycle.
2.  **Diverse Applications:** From basic web servers to complex message brokers or distributed databases, LXC containers can take on almost any role in a distributed system.
3.  **Isolation and Security:** The PDAL operates as a closed system. Faulty experiments or configurations never affect the production network. Security concerns are minimal compared to real server systems.
4.  **Low Learning Curve:** The basic installation of Proxmox and the management of LXC containers can be learned quickly, especially with the intuitive web interface.
5.  **Cost-Effectiveness:** In contrast to purchasing dedicated server hardware or using paid cloud services, the investment costs for a Tiny PC and a USB network card are minimal.
6.  **Open-Source Principle:** All main components used (Proxmox, Ubuntu, LXC) are open source or can be used free of charge, which avoids additional costs and offers broad community support.
7.  **Risk-Free Learning:** The main goal of the PDAL is to create an environment where you can safely experiment, make mistakes, and learn from them without endangering real systems or data.

---

## Conclusion and Outlook

Building a Personal Distributed Applications Lab based on a Tiny PC, Proxmox, and Ubuntu LTS LXC containers offers an excellent opportunity to explore the world of distributed applications. It is an investment in your own knowledge and practical skills, which are increasingly in demand in the modern IT world.

This PDAL is not just a playground for tech enthusiasts but also a serious tool for personal and professional development. It enables the simulated experience of challenges such as network partitions, data consistency problems, or latency effects that often remain abstract in theory. Through practical engagement with these topics, a deep understanding is developed that goes far beyond pure theoretical knowledge.

The next step could be the concrete implementation of example applications: How do you build a simple microservice cluster? How do you configure a replicated database? How can messages be exchanged via a message broker? The PDAL is the perfect stage to answer all these questions yourself and thus acquire the complex concepts of distributed systems. It is your personal innovation lab, where mistakes become the best teachers and discovering new solutions becomes a daily success.

For practical implementation, there is a series of documents that guide the learner step-by-step through the necessary steps. The necessary skills are acquired progressively:
- Level 0: Basic Infrastructure Competence (The absolute foundation)
- Level 1: Operating System and Container Management Competence
- Level 2: Middleware and Application Deployment Competence
- Level 3: System Interaction & Troubleshooting Competence
- Level 4: Building & Testing Complex Distributed Applications

**The goal is to gain competence in "experience with distributed applications and middleware systems."**

If required, learners can prove the knowledge they have acquired and the experience they have gained with corresponding tests; there are also corresponding templates for this.

Ideally, the exercises and experiments supplement the theoretical knowledge acquired. Topics such as how different protocols and standards work, integrating databases into your own applications, designing distributed applications, etc., can thus be practically supported.

---

## Sources for the article "Building a Personal Distributed Applications Lab (PDAL)"

### General Motivation / Importance of Distributed Systems
* **Theory of Distributed Systems:**
    * Coulouris, G., Dollimore, J., Kindberg, T., & Blair, G. (2019). *Distributed Systems: Concepts and Design* (5th ed.). Addison-Wesley.
    * Tanenbaum, A. S., & van Steen, M. (2017). *Distributed Systems: Principles and Paradigms* (3rd ed.). Pearson.
* **Trends in Software Development (Microservices, Cloud, IoT):**
    * **Articles on renowned tech blogs or developer platforms:**
        * Medium, Martin Fowler's Blog (especially on the topic of microservices)
            [https://www.martinfowler.com/tags/microservices.html](https://www.martinfowler.com/tags/microservices.html),
        * The New Stack, InfoQ. (Highlighting microservices, cloud-native, or IoT architectures.)
            [https://www.infoq.com/articles/microservices-intro/](https://www.infoq.com/articles/microservices-intro/),
            [https://www.infoq.com/cloud-native/](https://www.infoq.com/cloud-native/), [https://www.infoq.com/iot/](https://www.infoq.com/iot/)

### Proxmox Virtual Environment
* **Official Proxmox VE Documentation:** [https://pve.proxmox.com/wiki/Main_Page](https://pve.proxmox.com/wiki/Main_Page)
    * Here you will find detailed information on installation, administration, features (KVM, LXC), and the benefits.
* **Proxmox VE Official Website:** [https://www.proxmox.com/en/proxmox-ve](https://www.proxmox.com/en/proxmox-ve)
    * Contains information about the core functions and the philosophy behind the project.
* **Open Source License:** You can find information on licensing (AGPLv3) on the Proxmox website or in the documentation to prove the open-source aspect.

### Ubuntu LTS LXC Containers
* **LXC Official Website:** [https://linuxcontainers.org/](https://linuxcontainers.org/)
    * Basic information on LXC, how it works, and its advantages over VMs.
* **Ubuntu Official Website:** [https://ubuntu.com/](https://ubuntu.com/)
    * Information on Ubuntu LTS (Long Term Support) and its advantages for server environments (stability, long support period).
* **Container Technologies in General:**
    * **Docker Documentation (for comparison and a better understanding of containers):** [https://docs.docker.com/](https://docs.docker.com/) (Although you are using LXC, Docker is the best-known container technology and can be used to explain the concept of "containerization").
    * **Articles on the difference between VMs and containers (LXC, Docker):** Search for "VM vs. Container" or "LXC vs. Docker" on platforms like Red Hat Blog, IBM Developer, DigitalOcean Tutorials to prove resource efficiency and rapid deployment.

### Network Connection (USB Network Card, Windows Bridge)
* **Microsoft Support Documentation on Network Bridge in Windows:** [Set up ICS (Internet Connection Sharing) in Windows](https://learn.microsoft.com/de-de/troubleshoot/windows-server/networking/set-up-internet-connection-sharing)

**All systems are open source or free to use:**
* **Proxmox:** Official website (licensing).
* **Ubuntu:** Official website (licensing).
* **LXC:** Official website (licensing).
* The mentioned software packages (Nginx, PostgreSQL, Kafka, MQTT etc.) are also open source or have free editions.

---

### License
This work is licensed under the **Creative Commons Attribution - ShareAlike 4.0 International License**.
 
[To the license text on the Creative Commons website](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en)