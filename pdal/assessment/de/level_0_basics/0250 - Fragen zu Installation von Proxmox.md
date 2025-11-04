---
title: "Fragen zur Installation von Proxmox VE auf einem Tiny PC"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "uwe.bachmann@jade-hs.de"
organization: "PDAL-Projekt"
date: "2025-08-19"
version: "1.0.0"
level: "Ebene 0, Lerneinheit 0.2, Assessment"
duration: "0,2 Std"
prerequisites:["Abgeschlossen -  Dokument: 0250 - Installation von Proxmox VE auf einem Tiny PC"]
tags: ["PDAL","Assessment"]
license: "CC BY-SA 4.0"
---

### Test - Fragen zur Installation von Proxmox VE auf einem Tiny PC

1.  **Welche Aktion ist erforderlich, um die Installation von Proxmox VE von einem USB-Stick zu starten?**
    * A) Das Proxmox-ISO-Image auf die Festplatte des Tiny-PCs kopieren.
        *Hinweis: Ohne Betriebssystem ist das etwas schwierig.*
    * **B) Den USB-Stick als primäres Bootmedium im BIOS/UEFI einstellen oder das Boot-Menü aufrufen.**
        *Hinweis: Im Boot-Menü ist die Reihenfolge der Medien für den Startvorgang eingetragen. Der USB-Stick sollte als Erster in der Reihenfolge gestartet werden.*
    * C) Den USB-Stick mit dem `root`-Passwort formatieren.
        *Hinweis: Das 'root'-Passwort wird im Installationsprozess festgelegt*
    * D) Das ISO-Image mit WinSCP auf den Tiny-PC übertragen.
        *Hinweis: Vor der Installation hat das System noch kein Betriebssystem und daher keine Netzwerkverbindung.*

2.  **Laut dem Dokument soll für die Netzwerkkonfiguration eine statische IP-Adresse vergeben werden. Was ist der Hauptgrund dafür?**
    * A) Um die Leistung der virtuellen Maschinen zu verbessern.
        *Hinweis: Die Leistung virtuellen Maschine hat grundsätzlich nichts mit der Netzwerkverbindung zu tun.*
    * B) Um zu verhindern, dass andere Geräte auf das Proxmox-Webinterface zugreifen können.
        *Hinweis: Das wird nicht durch eine statische IP verhindert.*
    * C) Um die Namensauflösung im Internet zu beschleunigen.
        *Hinweis: Unser lokales Netzwerk ist nicht im allgemeinen Internet aufrufbar.*
    * **D) Um sicherzustellen, dass der Host unter derselben Adresse erreichbar ist, was für Serverdienste wichtig ist.**
        *Hinweis: Würde man DHCP für die Netzwerkkonfiguration verwenden ist nicht sicher gestellt, dass der Host immer die selbe IP-Adresse bekommt. Dies kann in der Anwendungsentwicklung zu größeren Problemen führen.*

3.  **Welche der folgenden IP-Adressen wird laut Dokument zum Pingen des Windows-Rechners mit aktiver ICS-Funktion verwendet, um die Netzwerkkonnektivität zu prüfen?**
    * A) `192.168.1.1`
        *Hinweis: Das ist eine IP-Adresse in einem lokalen Netzwerk - aber nicht unsere.*
    * B) `8.8.8.8`
        *Hinweis: Das ist die IP-Adresse des Google-DNS-Servers.*
    * **C) `192.168.137.1`**
        *Hinweis: Das ist die richtige Addresse für unseren ICS-Adapter.*
    * D) `127.0.0.1`
        *Hinweis: Das ist die "localhost"-Adresse unter der sich jeder PC selbst aufrufen kann.*

4.  **Welche Konfigurationsdatei muss laut Dokument bearbeitet werden, um den Chrony-Zeitserver auf `time.jade-hs.de` umzustellen?**
    * A) `/etc/ntp.conf`
        *Hinweis: Das ist die Konfigurationsdatei für den Network Time Protocol (NTP) Daemon.*
    * **B) `/etc/chrony/chrony.conf`**
        *Hinweis: Das ist die Konfigurationsdatei unter Debian; unserer Proxmox-Installation.*
    * C) `/etc/timesyncd.conf`
        *Hinweis: Das ist die Konfigurationsdatei zur Zeitsynchonisation unter Ubuntu*
    * D) `/etc/network/interfaces`
        *Hinweis: Das ist die Netzwerkkonfiguration unter Debian.*

5.  **Warum wird laut dem Dokument beim ersten Aufruf des Proxmox-Webinterfaces eine Zertifikatswarnung angezeigt?**
    * A) Weil der Browser kein HSTS (HTTP Strict Transport Security) für die IP-Adresse unterstützt.
        *Hinweis: HSTS ist ein Sicherheitsmechanismus für HTTPS-Verbindungen.*
    * **B) Weil Proxmox ein selbstsigniertes Root-CA-Zertifikat verwendet, dem der Browser nicht vertraut.**
        *Hinweis: Unser System kennt die Zertifikate von Proxmox noch nicht; daher sind die erst einmal nicht vertrauenswürdig.*
    * C) Weil der NTP-Dienst noch nicht korrekt synchronisiert ist.
        *Hinweis: Der NTP-Dienst hat hiermit nicht direkt zu tun.*
    * D) Weil das Passwort für den `root`-Benutzer zu schwach ist.
        *Hinweis: Das Passwort hat nichts mit den Zertifikaten zu tun.*

6. **Was ist die Hauptfunktion von Proxmox VE, wie im Dokument beschrieben?**
    * A) Es ist ein Betriebssystem für Desktop-PCs.
        *Hinweis: Proxmox ist für Server gedacht, nicht für Desktops.*
    * B) Es ist eine Software zum Erstellen von Dokumenten.
        *Hinweis: Das ist eine Anwendungssoftware.*
    * **C) Es ist ein Virtualisierungshost, der VMs und Container hostet.**
        *Hinweis: Die Hauptaufgabe eines Hypervisors wie Proxmox ist die Verwaltung virtueller Umgebungen.*
    * D) Es ist ein Tool zur Netzwerküberwachung.
        *Hinweis: Das ist eine spezialisierte Netzwerk-Software.*
    * E) Es ist eine Firewall-Lösung.
        *Hinweis: Proxmox hat zwar Firewall-Funktionen, aber das ist nicht seine Hauptfunktion.*

7. **Warum wird im Dokument empfohlen, das Proxmox CA-Zertifikat in den Client-Browser zu importieren?**
    * A) Um die Geschwindigkeit der Netzwerkverbindung zu erhöhen.
        *Hinweis: Die Zertifikatsinstallation hat keinen Einfluss auf die Geschwindigkeit.*
    * B) Um das Proxmox-System zu aktualisieren.
        *Hinweis: Updates werden über die Paketverwaltung vorgenommen.*
    * C) Um die Benutzeroberfläche von Proxmox anzupassen.
        *Hinweis: Das ist eine Einstellung im Webinterface.*
    * **D) Um die Sicherheitswarnung des Browsers zu unterdrücken und eine vertrauenswürdige HTTPS-Verbindung herzustellen.**
        *Hinweis: Das Zertifikat macht die Verbindung vom Browser zum Server als sicher und vertrauenswürdig  erkennbar.*
    * E) Um eine statische IP-Adresse zu konfigurieren.
        *Hinweis: Das ist eine Netzwerkeinstellung auf dem Proxmox-Host.*

8. **Die Installation wird mit der statischen IP-Adresse 192.168.137.xxx/24 konfiguriert. Was repräsentiert die /24 Notation in dieser Adresse?**
    * A) Die Version des IP-Protokolls.
        *Hinweis: Das hat nichts mit der IP-Version zu tun.*
    * B) Die Anzahl der Hosts, die im Netzwerk verfügbar sind.
        *Hinweis: Das ist die Anzahl der Subnetz-Masken-Bits.*
    * C) Den Port, auf dem der Webserver läuft.
        *Hinweis: Ports werden separat konfiguriert.*
    * D) Die maximale Bandbreite der Netzwerkverbindung.
        *Hinweis: Die Bandbreite ist eine Hardware-Eigenschaft.*
    * **E) Die Subnetzmaske, die 24 Bits für das Netzwerk und 8 Bits für Hosts bereitstellt.**
        *Hinweis: Die /24 Notation ist eine CIDR-Notation und bedeutet, dass die ersten 24 Bits die Netzwerk-ID sind.*

9. **Was ist der Hauptgrund für die Verwendung von Rufus oder Balena Etcher, um das ISO-Image auf einen USB-Stick zu schreiben?**
    * A) Um die Dateigröße des ISO-Images zu reduzieren.
        *Hinweis: Die Größe bleibt gleich.*
    * B) Um das USB-Laufwerk zu formatieren.
        *Hinweis: Das ist ein Nebeneffekt, aber nicht der Hauptzweck.*
    * C) Um eine Sicherungskopie des ISO-Images zu erstellen.
        *Hinweis: Dafür gibt es spezielle Backup-Software.*
    * **D) Um den USB-Stick bootfähig zu machen, damit das Installationsprogramm direkt vom Stick gestartet werden kann.**
        *Hinweis: Ein einfaches Kopieren funktioniert nicht, es muss eine bootfähige Struktur erstellt werden.*
    * E) Um ein Passwort für den Installationsvorgang festzulegen.
        *Hinweis: Dafür gibt es keine Funktionalität.*

---

### Lizenz
Dieses Werk ist lizenziert unter der **Creative Commons - Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz**.
 
[Zum Lizenztext auf der Creative Commons Webseite](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)

