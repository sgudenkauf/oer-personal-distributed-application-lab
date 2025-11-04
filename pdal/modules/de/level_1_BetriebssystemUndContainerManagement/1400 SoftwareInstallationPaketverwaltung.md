---
title: "Software Installation und Paketverwaltung"
author: ["Gudenkauf, Prof Stefan", "Uwe, Bachmann", "Ronald, Kalk"]
mail: "uwe.bachmann@jade-hs.de"
organization: "z.B. PDAL-Projekt, Jade Hochschule"
date: "2025-08-26"
version: "1.0.0"
level: "Ebene 1, Lerneinheit 1.4"
duration: "Geschätzte Dauer (z.B. 2-3 Stunden)"
prerequisites: "Tiny- PC mit installiertem Proxmox und mindestens einem LXC-Containers"
tags: ["Proxmox", "Linux", "Virtualisierung", "Basics"]
license: "CC BY-SA 4.0"
---

# 📦 Software-Installation und Paketverwaltung unter Linux (Debian/Ubuntu)

Die Verwaltung von Softwarepaketen ist ein zentraler Bestandteil jedes Linux-Systems.  
Unter Linux-basierten Distributionen (z. B. **Ubuntu, Debian, Linux Mint, Proxmox VE**) wird dafür das Tool **APT (Advanced Package Tool)** verwendet.  
Zusätzlich gibt es Hilfsprogramme wie `wget`, um Dateien aus dem Internet herunterzuladen.

Anders als bei Windows gibt es bei Linux **keinen automatischen Update-Dienst**, der das System ohne Benutzerinteraktion aktualisiert.  
Updates müssen daher **manuell angestoßen** werden, z. B. mit:

```bash
sudo apt update       # Paketlisten aktualisieren
sudo apt upgrade      # installierbare Updates anwenden
```
---

## 🔹 Grundlagen von APT

APT arbeitet mit einem **Paket-Repository**, das eine Sammlung von Softwarepaketen enthält.  
Jedes Paket besteht aus Programmen, Bibliotheken und Metadaten.

Die **Repositories** werden von den jeweiligen Linux-Distributionen gepflegt und stellen sicher, dass die Pakete aktuell und geprüft sind.  
Damit das System weiß, welche Pakete verfügbar sind, greift `apt` auf eine **Paketliste** zurück, die regelmäßig aktualisiert werden sollte.  

Beim Installieren oder Aktualisieren von Paketen werden die entsprechenden Dateien über die **im Repository hinterlegten URLs** abgefragt und heruntergeladen.


---

## 🛠️ Häufig verwendete APT-Befehle

### 1. Paketlisten aktualisieren

```bash
sudo apt update
```

* Ruft die neuesten Paketinformationen von den konfigurierten Repositories ab.
* Führt **noch kein Upgrade** durch, sondern aktualisiert nur die Datenbank.
* Sollte immer **vor Installationen** ausgeführt werden.

### 2. Systempakete aktualisieren

```bash
sudo apt upgrade
```

* Installiert die neuesten Versionen aller bereits installierten Pakete.
* Lässt bestehende Konfigurationen normalerweise unberührt.

>👉 Tipp: Um auch Abhängigkeiten und verwaiste Pakete automatisch zu aktualisieren, kann verwendet werden:

```bash
sudo apt full-upgrade
```

### 3. Software installieren

```bash
sudo apt install <paketname>
```

Beispiele:

```bash
sudo apt install apache2
sudo apt install htop
```

* Lädt das Paket und alle Abhängigkeiten herunter und installiert sie.
* Bei grafischen Programmen werden automatisch zusätzliche Bibliotheken installiert.

---

### 4. Software entfernen

```bash
sudo apt remove <paketname>
```

Beispiel:

```bash
sudo apt remove apache2
```

* Entfernt das Paket, **lässt aber Konfigurationsdateien zurück**.
* Nützlich, wenn man die Software später wieder installieren möchte.

👉 Um auch die Konfiguration zu löschen:

```bash
sudo apt purge <paketname>
```

---

### 5. Verwaiste Pakete entfernen

```bash
sudo apt autoremove
```

* Entfernt automatisch nicht mehr benötigte Abhängigkeiten.
* Praktisch nach Deinstallation von Software.

---

### 6. Paket suchen

```bash
apt search <suchbegriff>
```

Beispiel:

```bash
apt search nginx
```

* Zeigt verfügbare Pakete, die zum Suchbegriff passen.

---

### 7. Informationen zu einem Paket anzeigen

```bash
apt show <paketname>
```

Beispiel:

```bash
apt show curl
```

* Liefert Details wie Version, Beschreibung, Abhängigkeiten.

---

## 🔄 Upgrade auf eine neue Ubuntu-Version

Wenn eine **neue Ubuntu-Version** veröffentlicht wird (z. B. von Ubuntu 22.04 LTS → 24.04 LTS), reicht `apt update && apt upgrade` nicht aus.
Dafür gibt es das Tool **do-release-upgrade**.

### Vorbereitung

1. Alle aktuellen Updates einspielen:

   ```bash
   sudo apt update && sudo apt upgrade && sudo apt full-upgrade
   ```

2. Neustart des Systems (falls ein Kernel-Update installiert wurde):

   ```bash
   sudo reboot
   ```

### Upgrade starten

```bash
sudo do-release-upgrade
```

* Startet den Ubuntu-Upgrade-Assistenten.
* Führt durch den kompletten Upgrade-Prozess.
* Fragt ggf. nach, wie mit bestehenden Konfigurationsdateien umgegangen werden soll.

👉 Falls `do-release-upgrade` nicht verfügbar ist, kann es installiert werden:

```bash
sudo apt install update-manager-core
```


### Manuelles Upgrade (alternative Methode)

Falls man das Release direkt per `/etc/apt/sources.list` umstellt:

1. Alle Einträge von z. B. `jammy` → `noble` (je nach Version) ändern.
2. Danach:

   ```bash
   sudo apt update && sudo apt full-upgrade
   ```

   >⚠️ Achtung: Diese manuelle Methode ist **fehleranfälliger** und wird nur für erfahrene Admins empfohlen.

---

## 🌍 Dateien mit `wget` herunterladen

`wget` ist ein Kommandozeilen-Tool, um Dateien aus dem Internet herunterzuladen.  

> **Hinweis:** Die Installation von Software über `wget` sollte **nur dann** erfolgen, wenn die gewünschte Anwendung **nicht über das Paket-Repository** verfügbar ist.  
> Standardmäßig ist es immer sicherer und einfacher, Pakete über **APT** zu installieren.

```bash
sudo apt install wget
```

### Datei herunterladen

```bash
wget <URL>
```

Beispiel:

```bash
wget https://dlcdn.apache.org/tomcat/tomcat-10/v10.1.43/bin/apache-tomcat-10.1.43.tar.gz
```

* Lädt die Datei in das aktuelle Verzeichnis herunter.

>Hinweis:
Man muss sich entweder im gewünschten Download-Verzeichnis befinden, bevor man den Befehl ausführt,
oder beim Download den Zielpfad explizit angeben (siehe Beispiel unten):

```bash
wget -P /pfad/zum/zielverzeichnis https://dlcdn.apache.org/tomcat/tomcat-10/v10.1.43/bin/apache-tomcat-10.1.43.tar.gz
```

### Mehrere Dateien herunterladen

```bash
wget -i urls.txt
```

* Nützlich, wenn `urls.txt` eine Liste von URLs enthält.

### Download im Hintergrund

```bash
wget -b <URL>
```

---

## ✅ Zusammenfassung

| Befehl                    | Funktion                                     |
| ------------------------- | -------------------------------------------- |
| `sudo apt update`         | Aktualisiert Paketlisten                     |
| `sudo apt upgrade`        | Installiert neue Paketversionen              |
| `sudo apt full-upgrade`   | Aktualisiert auch Abhängigkeiten             |
| `sudo apt install`        | Installiert ein Paket                        |
| `sudo apt remove`         | Entfernt Paket, behält Konfigurationsdateien |
| `sudo apt purge`          | Entfernt Paket inkl. Konfiguration           |
| `sudo apt autoremove`     | Entfernt verwaiste Abhängigkeiten            |
| `apt search`              | Sucht nach Paketen                           |
| `apt show`                | Zeigt Paketdetails                           |
| `sudo do-release-upgrade` | Upgrade auf neue Ubuntu-Version              |
| `wget <URL>`              | Lädt Datei aus dem Internet                  |

---

## Quellen

* „apt › apt › Wiki › ubuntuusers.de“. Zugegriffen: 21. August 2025. [Online]. Verfügbar unter: [apt Referenz](https://wiki.ubuntuusers.de/apt/apt/)
* „Upgrade › Wiki › ubuntuusers.de“. Zugegriffen: 21. August 2025. [Online]. Verfügbar unter: [Upgrade Referenz](https://wiki.ubuntuusers.de/Upgrade/)
* „wget › Wiki › ubuntuusers.de“. Zugegriffen: 21. August 2025. [Online]. Verfügbar unter: [wget Referenz](https://wiki.ubuntuusers.de/wget/)

---

### Lizenz
Dieses Werk ist lizenziert unter der **Creative Commons - Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz**.
 
[Zum Lizenztext auf der Creative Commons Webseite](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)

