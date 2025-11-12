# oer-personal-distributed-application-lab
A safe, personal learning environment for creating distributed systems and developing distributed applications

---
title: "Lernen mit dem PDAL: Grundlagen für verteilte Anwendungen und Systeme"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe"]
email: "uwe.bachmann@jade-hs.de"
organization: "PDAL-Projekt"
date: "2025-08-07"
version: "1.0.0"
level: "Ebene 0"
duration: ""
prerequisites: ""
tags: ["PDAL", "Motivation", "Einführung"]
license: "CC BY-SA 4.0"
---

# Lernen mit dem PDAL: Grundlagen für verteilte Anwendungen und Systeme

### Die Bedeutung verteilter Systeme

**Verteilte Systeme** sind der Motor unserer modernen Welt. Sie bezeichnen die Infrastruktur aus miteinander verbundenen Computern, die zusammenarbeiten, um ein gemeinsames Ziel zu erreichen. Jede Nutzung einer App wie TikTok, ein Video-Stream auf Netflix oder ein Online-Einkauf bei Amazon basiert auf solchen Systemen, die aus Tausenden von Servern bestehen. Innerhalb dieser Systeme laufen **verteilte Anwendungen**, wie z. B. eine Microservices-Architektur. Das Verständnis dieser Infrastrukturen und der darauf laufenden Anwendungen ist eine der gefragtesten Kompetenzen auf dem heutigen Arbeitsmarkt.

### Die Herausforderung des praktischen Lernens

Um verteilte Systeme zu verstehen, ist es unerlässlich, sie selbst aufzubauen und darauf Anwendungen zu entwickeln. In traditionellen Kursen ist dies oft schwierig, da das Arbeiten auf echten, produktiven Servern zu riskant ist. Gleichzeitig bleiben theoretische Konzepte ohne praktische Anwendung abstrakt. Das PDAL (Personal Distributed Applications Lab) schließt genau diese Lücke.

### Das PDAL: Das eigene Rechenzentrum

Das PDAL ist eine sichere, persönliche Lernumgebung für den Aufbau **verteilter Systeme** und die Entwicklung **verteilter Anwendungen**. Es ermöglicht den Aufbau eines eigenen kleinen Rechenzentrums, das vom Hauptrechner isoliert ist. Hier kann man ohne Risiko experimentieren, Fehler machen und daraus lernen. Der Lernende wird angeleitet, virtuelle Umgebungen (LXC-Container) zu erstellen, zu vernetzen und darauf Middleware-Dienste wie Webserver und Datenbanken zu installieren. Darauf aufbauend werden dann die eigenen **verteilten Anwendungen** implementiert.

### Was das PDAL bietet und was nicht

Das PDAL ist **keine vollständige Ausbildung zum Systemadministrator** und setzt keine spezifischen Vorkenntnisse voraus. Es dient als erster, angeleiteter Einstieg in die Welt der **verteilten Systeme** und **Anwendungen**. Der Fokus liegt auf der Vermittlung von Grundlagen, die schnelle Erfolge ermöglichen und die Motivation aufrechterhalten. Der Lernpfad lehrt nicht nur die Durchführung einzelner Schritte, sondern auch die Fähigkeit zur eigenständigen Problemlösung. Am Ende dieses Pfades ist eine solide Basis für die selbstständige Weiterbildung in diesem Themenfeld geschaffen.

### Benötigte Voraussetzungen

Für den Start sind folgende Materialien notwendig:

* **Eigener Rechner:** Ein Windows-PC, der als Host dient.
* **USB-Stick (mind. 8 GB):** Wird für die Installation des Hypervisors Proxmox VE benötigt.
* **USB-Netzwerkkarte:** Ermöglicht die Isolation des PDAL vom Heimnetzwerk.
* **Übungsrechner:** Ein dedizierter Rechner (z.B. ein älterer Laptop oder ein Mini-PC), der ausschließlich für das PDAL genutzt wird.

![Ausstattung](./attachment/Ausstattung.jpg)

### Lernziele des PDAL

Am Ende des Lernpfades werden folgende Kompetenzen erworben:

* **Infrastruktur-Grundlagen:** Ein Host-Rechner kann mit einem Bare-Metal-Hyperviser (Proxmox VE) eingerichtet und virtuelle Umgebungen (LXC-Container) können verwaltet werden.
* **Betriebssystem- und Container-Management** Dieser Block ist der Fähigkeit gewidmet, Ubuntu LTS LXC-Container zu erstellen, zu konfigurieren und grundlegende Linux-Aufgaben innerhalb der Container auszuführen.
* **Praktische Anwendung:** Verschiedene Middleware-Systeme wie Apache, MariaDB, JupyterLab, Grafana und MQTT-Broker können installiert und konfiguriert werden.
* **Verteilte Anwendungen:** Eine einfache verteilte Anwendung (Microservices) kann entworfen und implementiert werden, wobei das Zusammenspiel der einzelnen Komponenten verstanden wird.

---

### Lizenz
Dieses Werk ist lizenziert unter der **Creative Commons - Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz**.
 
[Zum Lizenztext auf der Creative Commons Webseite](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)
 



