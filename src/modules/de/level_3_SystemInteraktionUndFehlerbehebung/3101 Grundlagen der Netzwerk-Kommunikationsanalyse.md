---
title: "Grundlagen der Netzwerk-Kommunikationsanalyse"
author: ["Gudenkauf, Prof Stefan", "Ronald Kalk", "Uwe Bachmann"]
mail: "pdal@jade-hs.de"
organization: "PDAL-Projekt, Jade Hochschule"
date: "2026-01-12"
version: "1.0.0"
level: "Ebene 3, Lerneinheit 3.1"
duration: "Geschätzte Dauer (1 - 2 Stunden)"
prerequisites: "Abschluss Ebene 2"
tags: ["Proxmox", "Linux", "Virtualisierung", "Tshark", "Tcpdump"]
license: "CC BY-SA 4.0"
---

# 📘 Grundlagen der Netzwerk-Kommunikationsanalyse

## Einleitung

Die Netzwerk-Kommunikationsanalyse ist ein zentraler Bestandteil der Netzwerktechnik und IT-Sicherheit. Sie ermöglicht nicht nur das Überwachen des Datenverkehrs, sondern vor allem die **Fehleranalyse**, die Leistungsoptimierung und das Aufdecken von Sicherheitsrisiken.

In virtuellen Umgebungen wie Proxmox ist die Analyse unverzichtbar, um Probleme wie Paketverlust oder falsch konfigurierte Dienste zwischen LXC-Containern systematisch zu diagnostizieren.

---

## 1. Fachbegriffe

* **Packet (Paket):** Eine kleine Datenmenge, bestehend aus **Header** (Metadaten wie IP/Port) und **Payload** (Nutzdaten).
* **TCP (Transmission Control Protocol):** Verbindungsorientiert. Garantiert die Zustellung und Reihenfolge. Ideal für Webverkehr und Datenbanken.
* **UDP (User Datagram Protocol):** Verbindungslos. Schnell, aber ohne Empfangsbestätigung. Ideal für Streaming oder DNS.
* **Wireshark / TShark:** Wireshark ist das grafische Tool, **TShark** die mächtige Kommandozeilen-Version für Server/LXC ohne grafische Oberfläche.
* **tcpdump:** Ein schlankes, hochflexibles Tool zum schnellen Mitschneiden von Traffic, oft als Vorstufe zur Analyse in Wireshark genutzt.

---

## 2. Ziele der Lerneinheit

1. **Installation:** Grundkonfiguration von `tcpdump` und `TShark`.
2. **Filterung:** Gezieltes Eingrenzen von Traffic nach IP, Port und Protokoll.
3. **Diagnose:** Identifikation von Fehlern wie Timeouts oder abgebrochenen Handshakes.
4. **Sicherheit:** Erkennen von unautorisierten Zugriffen oder Man-in-the-Middle-Szenarien.

---

## 3. Zentrale Analyse-Umgebung (Setup)

Anstatt TShark auf jedem LXC zu installieren, richten wir einen **zentralen Sniffer-Container** ein. Dieser beobachtet den gesamten Verkehr der Proxmox-Bridge `vmbr0`.

### 3.1 Installation

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install tshark -y

```

> 💡 **Wichtig:** Während der Installation die Frage, ob Nicht-Root-Benutzer sniffen dürfen, mit **"Yes"** beantworten.

### 3.2 Der Promiscuous Mode

Damit der Sniffer-Container Pakete sieht, die nicht an ihn selbst gerichtet sind, muss das Interface in den "Promiscuous Mode" versetzt werden.

> ⚠️ **ACHTUNG:** Das Mitschneiden von fremdem Datenverkehr darf nur zu Diagnosezwecken im eigenen lokalen Netzwerk und/oder in Absprache mit dem Administrator erfolgen (Datenschutz/Recht).

**Aktivierung auf dem Sniffer-LXC:**

```bash
sudo ip link set dev eth0 promisc on
# Prüfung:
ip link show eth0 | grep PROMISC

```

---

## 4. Arbeiten mit TShark

### 4.1 Grundlegende Befehle & Filter

* **Live-Capture (einfach):** `tshark -i eth0`
* **Filter nach Host:** `tshark -i eth0 host 192.168.137.120`
* **Filter nach Subnetz:** `tshark -i eth0 net 192.168.137.0/24`

### 4.2 Protokollbasierte Analyse

| Dienst | Port | TShark Filter |
| --- | --- | --- |
| **HTTP** | 80 | `port 80` |
| **MariaDB** | 3306 | `port 3306` |
| **DNS** | 53 | `port 53` |
| **MQTT** | 1883 | `port 1883` |

**Spezial-Filter für TCP-Fehler:**

```bash
# Zeigt nur Verbindungsanfragen (SYN) - gut zum Finden von Portscans oder Timeouts
tshark -i eth0 tcp.flags.syn==1

```

---

## 5. Analyse verschlüsselter Kommunikation (TLS/SSH)

Bei verschlüsselten Protokollen (HTTPS, SSH) kann TShark den Inhalt der Payload **nicht** lesen. Dennoch ist eine Fehleranalyse möglich über:

* **Metadata:** Wer spricht mit wem? Wie oft?
* **Handshake:** Schlägt der TLS-Aufbau fehl?
* **Timing:** Gibt es ungewöhnliche Verzögerungen im Verbindungsaufbau?

---

## 6. Arbeiten mit tcpdump (Alternative)

`tcpdump` ist oft bereits vorinstalliert oder schneller einsatzbereit für "Quick & Dirty" Analysen.

### 6.1 tcpdump ohne Root (CAP_NET_RAW)

Ein Highlight für die Sicherheit: Wir geben dem Programm nur die exakt benötigte Berechtigung, anstatt es mit vollen Root-Rechten laufen zu lassen.

```bash
# Capability zuweisen
sudo setcap cap_net_raw,cap_net_admin=eip /usr/sbin/tcpdump

# Ausführung als normaler Benutzer 'pdal'
tcpdump -i eth0

```

### 6.2 Wichtige Praxis-Parameter

* **In Datei speichern:** `tcpdump -i eth0 -w dump.pcap`
* **Inhalt anzeigen (ASCII):** `tcpdump -i eth0 -A`
* **Sehr ausführlich:** `tcpdump -i eth0 -vvv`

---

## 7. Zusammenfassung & Best Practices

* **Zentralisierung:** Ein Sniffer-LXC schont Ressourcen und hält andere Container "sauber".
* **Filterung:** "Capture less, analyze more" – nutzen Sie Filter, um nicht in der Datenmenge zu ertrinken.
* **Verschlüsselung:** Erwarten Sie keine Passwörter bei HTTPS, konzentrieren Sie sich auf die Verbindungsstabilität.
* **Dateiformat:** Nutzen Sie `.pcap`, um Captures von tcpdump später komfortabel in Wireshark (GUI) zu öffnen.

---

## Quellen

* „tshark(1)“. Zugegriffen: 14. November 2025. [Online]. Verfügbar unter: [Tshark Manual](https://www.wireshark.org/docs/man-pages/tshark.html)
* „Home | TCPDUMP & LIBPCAP“. Zugegriffen: 14. November 2025. [Online]. Verfügbar unter: [tcpdump Doc](https://www.tcpdump.org/index.html#documentation)
---

### Lizenz

Dieses Werk ist lizenziert unter der **Creative Commons Namensnennung - Nicht-kommerziell - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz**.
