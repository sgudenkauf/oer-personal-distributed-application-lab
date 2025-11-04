---
title: "Aufbau eines Personal Distributed Applications Lab (PDAL): Experimentieren mit verteilten Systemen in geschützter Umgebung"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe"]
email: "uwe.bachmann@jade-hs.de"
organization: "PDAL-Projekt"
date: "2025-08-11"
version: "1.0.0"
level: "Instructor guide"
duration: "N/a"
prerequisites:["none"]
tags: ["PDAL", "Grundlagen", "Infrastruktur", "Didaktik", "Instructur Guide"]
license: "CC BY-SA 4.0"
---

# Aufbau eines Personal Distributed Applications Lab (PDAL): Experimentieren mit verteilten Systemen in geschützter Umgebung

## Motivation: Die wachsende Bedeutung verteilter Anwendungen verstehen und meistern

Die digitale Landschaft wird zunehmend von verteilten Anwendungen und Systemen dominiert. Von Webdiensten über IoT-Plattformen bis hin zu Microservices-Architekturen – die Fähigkeit, über mehrere vernetzte Komponenten hinweg zu agieren und Daten auszutauschen, ist heute eine Kernkompetenz in der Softwareentwicklung und IT-Infrastruktur. Das Verstehen der Komplexität, die diese Architekturen mit sich bringen – von Netzwerkkommunikation und Latenz über Datenkonsistenz und Fehlertoleranz bis hin zu Sicherheit – ist unerlässlich.

Für Studierende, Entwickler, Admins oder auch einfach Technikbegeisterte stellt sich oft die Frage, wie man sich diesem Feld annähern kann, ohne sofort in teure und komplexe Cloud-Infrastrukturen investieren oder bestehende Produktivsysteme riskieren zu müssen. Das Experimentieren mit Verteilten Systemen erfordert eine isolierte Umgebung, in der man gefahrlos unterschiedlichste Konfigurationen testen, Fehler reproduzieren und neue Technologien ausprobieren kann.

Genau hier setzt die Idee eines **Personal Distributed Applications Lab (PDAL)** an. Ein PDAL ist eine kostengünstige, flexible und sichere Testumgebung, die es Einzelpersonen ermöglicht, praktische Erfahrungen mit verteilten Anwendungen und Middlewaresystemen zu sammeln. Es bietet die ideale Plattform, um die Herausforderungen und Lösungsansätze von verteilten Systemen zu explorieren, ohne die Risiken und den Aufwand einer „echten“ Serverumgebung eingehen zu müssen. Die Motivation ist klar: Durch praktisches Experimentieren ein tiefgreifendes Verständnis für die Funktionsweise und die Fallstricke verteilter Systeme zu entwickeln.

---

## Kurzbeschreibung: Das PDAL im Detail – Aufbau und Funktionsweise

Das vorgeschlagene PDAL basiert auf einem minimalistischen Ansatz, der maximale Flexibilität bei geringstem Kosten- und Administrationsaufwand bietet. Das Herzstück bildet ein handelsüblicher **Tiny-PC**, der als Host für die virtualisierten Komponenten dient. Es soll das Verständnis für verteilte Systeme und verteilte Anwendungen fördern und ist nicht auf hohe Rechenleistung ausgelegt.

### Die Basis: Proxmox als Virtualisierungsplattform

Als Betriebssystem und Virtualisierungsschicht wird **Proxmox Virtual Environment** gewählt. Proxmox ist eine leistungsstarke und quelloffene Server-Virtualisierungsplattform, die auf Debian basiert und die Verwaltung von virtuellen Maschinen (VMs) und Containern (LXC) ermöglicht. Die Vorteile von Proxmox in diesem Kontext sind vielfältig:

* **Benutzerfreundlichkeit:** Proxmox bietet eine intuitive Weboberfläche, die das Erstellen, Konfigurieren und Verwalten von VMs und LXC-Containern erheblich vereinfacht.
* **Leistungsfähigkeit:** Trotz seiner Flexibilität ist Proxmox ressourceneffizient und kann auch auf weniger leistungsstarker Hardware wie einem Tiny-PC stabil laufen.
* **Flexibilität:** Es unterstützt sowohl KVM-basierte VMs als auch LXC-Container, was eine breite Palette an Anwendungsszenarien ermöglicht.

Die Installation von Proxmox auf dem Tiny-PC ist der erste Schritt und bildet das Fundament des PDAL.

### Die Experimentierumgebung: Ubuntu LTS LXC-Container

Innerhalb von Proxmox werden **Ubuntu LTS (Long Term Support) LXC-Container** (Linux Containers) als die primären "virtuellen" Maschinen für die verteilten Anwendungen eingesetzt. LXC-Container sind im Gegensatz zu vollständigen virtuellen Maschinen deutlich schlanker und bieten signifikante Vorteile für ein solches Experimentierlabor:

* **Ressourceneffizienz:** LXC-Container teilen sich den Kernel des Host-Systems und benötigen daher deutlich weniger Ressourcen (CPU, RAM, Speicherplatz) als herkömmliche VMs. Dies ist besonders vorteilhaft für einen Tiny-PC mit begrenzten Ressourcen.
* **Schnelle Bereitstellung:** Die Erstellung und das Löschen von LXC-Containern erfolgt extrem schnell. Dies ermöglicht ein zügiges Iterieren über verschiedene Konfigurationen und das schnelle Aufsetzen neuer Testumgebungen.
* **Isolation:** Obwohl sie den Kernel teilen, bieten LXC-Container eine hervorragende Prozess- und Dateisystem-Isolation, sodass die Experimente in einem Container die anderen nicht beeinflussen.

Innerhalb dieser Ubuntu LTS LXC-Container können dann unterschiedlichste Dienste und Anwendungen installiert und getestet werden, die für verteilte Systeme relevant sind:

* **Webserver (z.B. Nginx, Apache):** Zum Hosten von APIs oder statischen Inhalten.
* **Datenbanken (z.B. PostgreSQL, MongoDB, Redis):** Zum Speichern und Verwalten von Daten, auch in verteilten Setups (Replikation, Sharding).
* **Message Broker (z.B. MQTT, Kafka, RabbitMQ):** Für asynchrone Kommunikation und Event-Streaming in verteilten Architekturen.
* **Zertifizierungsstelle (CA):** Zum Erzeugen und Verwalten von SSL/TLS-Zertifikaten für sichere Kommunikation zwischen den Containern.
* **Jupyter Notebooks:** Für interaktive Datenanalyse und Prototyping von verteilten Algorithmen.
* **Java-/Python-Codeinstanzen:** Zum Implementieren und Testen von kundenspezifischer Netzwerkkommunikation, Microservices oder verteilten Algorithmen.

Durch die Kombination mehrerer LXC-Container können komplexe Szenarien wie Microservices-Architekturen, verteilte Datenbankcluster oder IoT-Backends simuliert werden. Jeder Container repräsentiert dabei einen Knoten im verteilten System.

---

### Netzwerkverbindung: Die isolierte Bridge zum Erfolg

Ein entscheidender Aspekt des PDAL ist seine vollständige Isolation vom Produktivnetzwerk. Die Netzwerkverbindung des Tiny-PCs wird über eine **USB-Netzwerkkarte** hergestellt, die an einen Entry-PC (Windows) angeschlossen ist. Auf diesem Entry-PC wird **Internet Connection Sharing (ICS)** aktiviert, um eine isolierte und kontrollierte Netzwerkverbindung für das PDAL bereitzustellen. Diese Konfiguration bietet mehrere Vorteile:

* **Abgrenzung vom Produktivnetzwerk:** Das PDAL agiert als **vollständig geschlossenes System**. Experimente, die Netzwerkfehler verursachen, oder fehlerhafte Konfigurationen können das Heimnetzwerk oder andere produktive Systeme nicht beeinträchtigen. Dies ist besonders relevant in Umgebungen, in denen das Betreiben unautorisierter Server strikt untersagt ist. Mit dem PDAL können Sie eine **vollständige Serverlandschaft** simulieren und betreiben, ohne gegen Sicherheitsrichtlinien oder Netzwerkregeln zu verstoßen, da Ihr Labor nur mit dem Entry-PC und nicht direkt mit dem Produktivnetzwerk verbunden ist.
* **Einfache Konfiguration:** Die Windows-Bridge leitet den Traffic vom Tiny-PC ins Internet (falls benötigt, z.B. für Software-Updates der LXC-Container) und ermöglicht gleichzeitig die Kommunikation zwischen dem Tiny-PC und dem Host-PC für Managementzwecke (z.B. Zugriff auf die Proxmox-Weboberfläche).
* **Sicherheit:** Da das PDAL isoliert ist, sind die Sicherheitsbedenken deutlich geringer als bei einem System, das direkt mit dem Internet verbunden ist. Potenziell unsichere Testanwendungen oder Fehlkonfigurationen stellen keine Gefahr für das Heimnetzwerk dar. Sie können neue Software oder Konfigurationen **risikofrei testen**, ohne Angst vor Datenlecks oder Kompromittierungen im Produktivnetzwerk haben zu müssen.

---

## Vorteile auf einen Blick: Warum ein PDAL die ideale Lernplattform ist

Die hier beschriebene Architektur bietet eine Reihe von überzeugenden Vorteilen, die sie zur idealen Lern- und Experimentierumgebung für verteilte Anwendungen machen:

1.  **Schnelle Iteration:** LXC-Container können in Sekundenschnelle erstellt, gestartet, gestoppt und gelöscht werden. Dies beschleunigt den Experimentierzyklus enorm.
2.  **Vielfältige Einsatzmöglichkeiten:** Von grundlegenden Webservern bis hin zu komplexen Message Brokern oder verteilten Datenbanken – LXC-Container können nahezu jede Rolle in einem verteilten System einnehmen.
3.  **Isolation und Sicherheit:** Das PDAL arbeitet als geschlossenes System. Fehlerhafte Experimente oder Konfigurationen beeinträchtigen niemals das Produktivnetzwerk. Sicherheitsbedenken sind im Vergleich zu realen Serversystemen minimal.
4.  **Geringer Einarbeitungsaufwand:** Die grundlegende Installation von Proxmox und das Management von LXC-Containern sind schnell zu erlernen, insbesondere mit der intuitiven Weboberfläche.
5.  **Kosteneffizienz:** Im Gegensatz zur Anschaffung dedizierter Serverhardware oder der Nutzung kostenpflichtiger Cloud-Dienste sind die Investitionskosten für einen Tiny-PC und eine USB-Netzwerkkarte minimal.
6.  **Open-Source-Prinzip:** Alle verwendeten Hauptkomponenten (Proxmox, Ubuntu, LXC) sind Open Source oder lizenzfrei nutzbar, was zusätzliche Kosten vermeidet und eine breite Community-Unterstützung bietet.
7.  **Gefahrloses Lernen:** Das Hauptziel des PDAL ist es, eine Umgebung zu schaffen, in der man gefahrlos experimentieren, Fehler machen und daraus lernen kann, ohne reale Systeme oder Daten zu gefährden.

---

## Fazit und Ausblick

Der Aufbau eines Personal Distributed Applications Lab auf Basis eines Tiny-PCs, Proxmox und Ubuntu LTS LXC-Containern bietet eine herausragende Möglichkeit, die Welt der verteilten Anwendungen zu erkunden. Es ist eine Investition in das eigene Wissen und die praktischen Fähigkeiten, die in der modernen IT-Welt immer gefragter sind.

Dieses PDAL ist nicht nur eine Spielwiese für Technologiebegeisterte, sondern auch ein ernstzunehmendes Werkzeug für die persönliche und berufliche Weiterentwicklung. Es ermöglicht das simulierte Erleben von Herausforderungen wie Netzwerkpartitionen, Datenkonsistenzproblemen oder Latenzeffekten, die in der Theorie oft abstrakt bleiben. Durch die praktische Auseinandersetzung mit diesen Themen wird ein tiefgreifendes Verständnis entwickelt, das weit über reines Theoriewissen hinausgeht.

Der nächste Schritt könnte die konkrete Implementierung von Beispielanwendungen sein: Wie baut man einen einfachen Microservice-Verbund? Wie konfiguriert man eine replizierte Datenbank? Wie lassen sich Nachrichten über einen Message Broker austauschen? Das PDAL ist die perfekte Bühne, um all diese Fragen selbst zu beantworten und sich so die komplexen Konzepte verteilter Systeme anzueignen. Es ist Ihr persönliches Innovationslabor, in dem Fehler zu den besten Lehrern werden und das Entdecken neuer Lösungsansätze zum täglichen Erfolgserlebnis.

Für die praktische Umsetzung gibt es Reihe von Dokumenten die dem Lernenden schrittweise durch die notwendigen Schritte führen. Dabei werden die notwendigen Kompetenzen schrittweise erworben:
- Ebene 0: Basis-Infrastruktur-Kompetenz (Das absolute Fundament)
- Ebene 1: Betriebssystem- und Container-Management-Kompetenz
- Ebene 2: Middleware- und Anwendungsbereitstellungs-Kompetenz
- Ebene 3: System-Interaktion & Fehlerbehebungs-Kompetenz
- Ebene 4: Aufbau & Test von komplexen verteilten Anwendungen

**Das Ziel ist Kompetenzen in "Erfahrungen mit verteilten Anwendungen und Middlewaresystemen" zu sammeln.** 

Bei bedarf können die Lernenden das erworbene Wissen und die gewonnen Erfahrungen mit entsprechenden Tests nachweisen; auch hierfür gibt es entsprechende Vorlagen. 

Idealerweise werden mit den Übungen und Experimenten das theoretisch erworbene Wissen ergänzt. Themen wie Funktionsweise von unterschiedlichen Protokollen und Standards, Einbindung von Datenbanken in eigene Anwendungen, Konzeption von verteilten Anwendungen, usw. könnnen damit praktisch unterstützt werden. 

## Quellen für den Artikel "Aufbau eines Personal Distributed Applications Lab (PDAL)"

### Allgemeine Motivation / Bedeutung verteilter Systeme
* **Theorie der verteilten Systeme:**
    * Coulouris, G., Dollimore, J., Kindberg, T., & Blair, G. (2019). *Distributed Systems: Concepts and Design* (5th ed.). Addison-Wesley.
    * Tanenbaum, A. S., & van Steen, M. (2017). *Distributed Systems: Principles and Paradigms* (3rd ed.). Pearson.
* **Trends in der Softwareentwicklung (Microservices, Cloud, IoT):**
    * **Artikel auf renommierten Tech-Blogs oder Entwickler-Plattformen:** 
      * Medium, Martin Fowler's Blog (insbesondere zum Thema Microservices)
      https://www.martinfowler.com/tags/microservices.html, 
      * The New Stack, InfoQ. ( Microservices, Cloud Native oder IoT-Architekturen hervorheben.)
      https://www.infoq.com/articles/microservices-intro/,
      https://www.infoq.com/cloud-native/, https://www.infoq.com/iot/


### Proxmox Virtual Environment
* **Offizielle Proxmox VE Dokumentation:** [https://pve.proxmox.com/wiki/Main_Page](https://pve.proxmox.com/wiki/Main_Page)
    * Hier finden Sie detaillierte Informationen zur Installation, Verwaltung, Features (KVM, LXC) und den Vorteilen.
* **Proxmox VE Offizielle Webseite:** [https://www.proxmox.com/en/proxmox-ve](https://www.proxmox.com/en/proxmox-ve)
    * Enthält Informationen zu den Kernfunktionen und der Philosophie hinter dem Projekt.
* **Open Source Lizenz:** Sie können auf der Proxmox-Webseite oder in der Dokumentation die Informationen zur Lizenzierung (AGPLv3) finden, um den Open-Source-Aspekt zu belegen.

### Ubuntu LTS LXC-Container
* **LXC Offizielle Webseite:** [https://linuxcontainers.org/](https://linuxcontainers.org/)
    * Grundlegende Informationen zu LXC, wie es funktioniert und seine Vorteile gegenüber VMs.
* **Ubuntu Offizielle Webseite:** [https://ubuntu.com/](https://ubuntu.com/)
    * Informationen zu Ubuntu LTS (Long Term Support) und seinen Vorteilen für Serverumgebungen (Stabilität, lange Support-Periode).
* **Container-Technologien im Allgemeinen:**
    * **Docker-Dokumentation (zum Vergleich und besseren Verständnis von Containern):** [https://docs.docker.com/](https://docs.docker.com/) (Obwohl Sie LXC verwenden, ist Docker die bekannteste Container-Technologie und kann zur Erklärung des Konzepts der "Containerisierung" herangezogen werden).
    * **Artikel über den Unterschied zwischen VMs und Containern (LXC, Docker):** Suchen Sie auf Plattformen wie Red Hat Blog, IBM Developer, DigitalOcean Tutorials nach "VM vs. Container" oder "LXC vs. Docker" um die Ressourceneffizienz und schnelle Bereitstellung zu belegen.

### Netzwerkverbindung (USB-Netzwerkkarte, Windows Bridge)
* **Microsoft Support Dokumentation zur Netzwerkbrücke in Windows:** [Einrichten einer ICS (Internet Connection Sharing) unter Windows](https://learn.microsoft.com/de-de/troubleshoot/windows-server/networking/set-up-internet-connection-sharing)


**Alle Systeme OpenSource oder lizenzfrei:**
* **Proxmox:** Offizielle Webseite (Lizenzierung).
* **Ubuntu:** Offizielle Webseite (Lizenzierung).
* **LXC:** Offizielle Webseite (Lizenzierung).
* Die genannten Softwarepakete (Nginx, PostgreSQL, Kafka, MQTT etc.) sind ebenfalls quelloffen oder haben freie Editionen.

---

### Lizenz
Dieses Werk ist lizenziert unter der **Creative Commons - Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz**.
 
[Zum Lizenztext auf der Creative Commons Webseite](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)