---
title: "Erstellung eines LXC-Containers"
author: ["Gudenkauf, Prof Stefan", "Ronald Kalk", "Uwe Bachmann"]
mail: "uwe.bachmann@jade-hs.de"
organization: "z.B. PDAL-Projekt, Jade Hochschule"
date: "2025-08-21"
version: "1.0.0"
level: "Ebene 1, Lerneinheit 1.1"
duration: "1.0 h"
prerequisites: "Voraussetzungen funktionsfähiges Proxmox"
tags: ["Proxmox", "Linux", "Virtualisierung", "Basic-LXC"]
license: "CC BY-SA 4.0"
---

# Erstellung eines LXC-Containers

In diesem Dokument wird das Erstellen und Konfigurieren eines LXC-Standard-Containers beschrieben. 

In den folgenden Dokumenten wird immer nur die Installation bzw. Konfiguration von Anwendungen in einen funktionierenden LXC-Container beschrieben. 

## 🎯 Ziel

Erstellung eines LXC-Containers mit folgenden Angaben:

- **CTID:** 110  
- **Hostname:** apache110  
- **IP:** 192.168.137.110/24  
- **Gateway:** 192.168.137.1  
- **DNS:** vom Host übernommen  
- **RAM:** 512 MB  
- **Festplatte:** 8 GB  
- **Template:** `/var/lib/vz/template/cache/ubuntu-24.04-standard_24.04-2_amd64.tar.zst`

### Zusätzliche Schritte

1. Benutzer `pdal` (sudoer), Passwort: `meinPasswort` anlegen,
2. System-Update (`apt update/upgrade`) durchführen,
3. timedatectl Zeitzone `Europe/Berlin` einstellen
4. Netzwerkprüfung (Gateway & DNS-Auflösung).

>Hinweis: Im PDAL-Projekt können Sie ausnahmsweise immer den gleichen User und das gleiche Passwort nutzen. 
Das sollte in Produktiv-System natürlich niemals gemacht werden.
---

## 🧭 1. Template prüfen & hochladen

- Prüfe unter `Datacenter → <local> → Templates`, ob dein Template vorhanden ist.

![CTTemplateWebinterface](./1150attachments/CTTemplateWebinterface.png)
- Falls nicht: **Upload** oder Download via Web‑UI.
  
![CTTemplatedlWebinterface01](./1150attachments/CTTemplatedlWebinterface01.png)
- Navigiere zu "Templates":
  
![CTTemplatedlWebinterface02](./1150attachments/CTTemplatedlWebinterface02.png)
- Entsprechndes Template auswählen und auf "Download" klicken.

![CTTemplatedlWebinterface03](./1150attachments/CTTemplatedlWebinterface03.png)

Nach dem Download sollte das Template jetzt angezeigt werden.

---

## 🛠️ 2. Container erstellen

1. Rechtsklick auf den Knoten → **Create CT**
2. **General**:
   - CT ID: `110`
   - Hostname: `apache110`
   - Password: (root PW setzen)
   - Unprivileged: ✅
   ![General-Tab](./1150attachments/GeneralTab.png)

>Hinweis: Proxmox nutzt dreistellige Zahlen für die CT ID. Wir nutzen als Kennung das letzte Oktet der IP-Adresse. Dazu wählen Sie einen aussagekräftigen Namen; z. B. "apache110".

3. **Template**:
   - Storage: z. B. `local`
   - Template wählen
  
   ![Template-Tab](./1150attachments/TemplateTab.png)

4. **Root Disk**:
   - Storage: `local-lvm`
   - Size: `8 GiB`

   ![Disks-Tab](./1150attachments/DisksTab.png)

5. **CPU & Memory**:
   - Cores: `1`
   - Memory: `512 MiB`, Swap optional `512 MiB`
   ![CPU-Tab](./1150attachments/CPUTab.png)
   ![Memory-Tab](./1150attachments/MemoryTab.png)

6. **Network**:
   - Bridge: `vmbr0`
   - IPv4: Static `192.168.137.110/24`
   - Gateway: `192.168.137.1`

   ![Network-Tab](./1150attachments/NetworkTab.png)

7. **DNS**:
   - "Use DNS from host" (Standard)
   ![DNS-Tab](./1150attachments/DNSTab.png)

8. **Confirm**:
   - "Start after created": ✅
   - Auf **Finish** klicken
   ![Confirm-Tab](./1150attachments/ConfirmTab.png)

---

## ▶️ 3. Container starten & erste Schritte

- Container wird automatisch gestartet oder manuell über Web‑UI starten.
- Console öffnen → mit `root` + gesetztem Passwort einloggen.
![CT-Console](./1150attachments/CTConsole.png)
![Login-Console](./1150attachments/LoginConsole.png)

---

## 👤 4. Benutzer `pdal` anlegen & als sudo setzen

```bash
adduser pdal
# Passwort: meinPasswort
usermod -aG sudo pdal
```

![adduser-Console](./1150attachments/AdduserConsole.png)

![adduser-Console01](./1150attachments/AdduserConsole01.png)
Passwort für User `pdal` setzen und bestättigen.

![adduser-Console02](./1150attachments/AdduserConsole02.png)
![adduser-Console03](./1150attachments/AdduserConsole03.png)
![Usermod-Console01](./1150attachments/UsermodConsole01.png)

## 🌐 5. Netzwerkprüfung

In diesem Schritt stellen wir sicher, dass der neue Container eine Netzwerkverbindung hat. 

```bash
ping -c3 192.168.137.1
```
>Hinweis: Die Option `-c3` führt nur drei Pings aus.

![PingGwConsole](./1150attachments/PingGwConsole.png)

Dieser Schritt stellt sicher, dass eine Netzwerkverbindung besteht. Falls hier Probleme auftreten bitte die Netzwerkeinstellungen des Containers prüfen - `ContainerID → Network → Netzwerkeinstellungen`.

```bash
ping -c3 8.8.8.8
```

![PingGooglednsConsole](./1150attachments/PingGooglednsConsole.png)

Dieser Schritt stellt sicher, dass externe IP-Adressen angesprochen werden können. 

```bash
ping -c3 heise.de
```

![PingNamensauflösungHeiseConsole](./1150attachments/PingNamensauflösungHeiseConsole.png)

Dieser Schritt stellt sicher, dass die DNS-Auflösung korrekt funktioniert. 

## 🔄 6. System aktualisieren

Mit korrekt funktionierendem Netzwerk können Sie das System jetzt aktualisieren:

```bash
apt update && apt upgrade -y
```

![AptUpdateundAptUpgradeConsole01](./1150attachments/AptUpdateundAptUpgradeConsole01.png)
![AptUpdateundAptUpgradeConsole02](./1150attachments/AptUpdateundAptUpgradeConsole02.png)
![AptUpdateundAptUpgradeConsoleß3](./1150attachments/AptUpdateundAptUpgradeConsole03.png)

## 🕒 7. Zeitzone nur für die Darstellung konfigurieren und Status abfragen

```bash
timedatectl set-timezone Europe/Berlin
```

![TimezoneConsole](./1150attachments/TimezoneConsole.png)

```bash
timedatectl status
```

![TimedateStatusConsole](./1150attachments/TimedateStatusConsole.png)

>Hinweis: Der Container bezieht die Systemzeit von dem Host-System (Proxmox). Stimmt hier die Systemzeit nicht prüfen Sie die Einstellungen in Proxmox. 

✅ 🚀 Ergebnis

Der Container apache110 ist jetzt:

- mit Benutzer pdal (sudo) konfiguriert

- Netzwerk geprüft (Gateway, DNS)

- vollständig aktualisiert (apt update/upgrade)

- Zeitzone Europe/Berlin gesetzt

Sie können den Container nun für Ihre Zwecke verwenden und entsprechende Anwendungen installieren bzw. konfigurieren. 

---

## Quellen

- „Proxmox VE Documentation Index“. Zugegriffen: 4. Juni 2025. [Online]. Verfügbar unter: [Proxmox PVE-Docs](https://pve.proxmox.com/pve-docs/)
- canonical, „Ubuntu Server how-to guides“. [Online]. Verfügbar unter: [Ubuntu Server How-To](https://documentation.ubuntu.com/_/downloads/server/en/latest/pdf/)

---

### Lizenz
Dieses Werk ist lizenziert unter der **Creative Commons - Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz**.
 
[Zum Lizenztext auf der Creative Commons Webseite](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)
