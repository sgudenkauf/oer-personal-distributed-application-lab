---
title: "Fragen zum Apache2-Webserver und Benutzerverwaltung"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "uwe.bachmann@jade-hs.de"
organization: "PDAL-Projekt"
date: "2025-09-25"
version: "1.0.0"
level: "Ebene 2, Lerneinheit 2.1, Assessment"
duration: "0,2 Std"
prerequisites: ["Abgeschlossen -  Dokument: 2100 - Apache2-Webserver und Benutzerverwaltung im LXC-Container"]
tags: ["PDAL","Assessment"]
license: "CC BY-SA 4.0"
---

## ❓ 10 Multiple-Choice-Fragen zum Apache2-Webserver und Benutzerverwaltung

1.  **Was ist das primäre Merkmal, das die Architektur von Apache2 in der Standardkonfiguration von Nginx unterscheidet?**
    * A) Apache2 verwendet ausschließlich zentralisierte Konfigurationsdateien, während Nginx dezentrale Dateien nutzt.
        * *Hinweis*: Dies ist falsch. Apache2 nutzt stark modulare Konfigurationen pro Verzeichnis (`.htaccess`), während Nginx zentralisiert konfiguriert wird.
    * B) Apache2 ist eine proprietäre Software, während Nginx Open-Source ist.
        * *Hinweis*: Dies ist falsch. Apache2 gehört zur **Open-Source-Software-Familie**.
    * C) Nginx unterstützt nur statische Inhalte, während Apache2 dynamische Inhalte unterstützt.
        * *Hinweis*: Dies ist falsch. Nginx unterstützt ebenfalls dynamische Inhalte, ist aber typischerweise schneller bei statischen Inhalten.
    * **D) Apache2 verwendet einen prozessbasierten oder Thread-basierten Ansatz, während Nginx ein ereignisgesteuertes, asynchrones Modell nutzt.**
        * *Hinweis*: Dies ist korrekt und beschreibt den grundlegenden Architekturunterschied der beiden Webserver.
    * E) Apache2 wird nur auf Windows-Systemen eingesetzt, Nginx nur auf Linux.
        * *Hinweis*: Dies ist falsch. Apache2 wird auf vielen Betriebssystemen, insbesondere Linux, eingesetzt.

2.  **Welchen Zweck erfüllt der Befehl `sudo apt update` im Installationsprozess?**
    * A) Er installiert den Apache2-Webserver.
        * *Hinweis*: Dies ist falsch. Die Installation erfolgt mit `sudo apt install apache2`.
    * B) Er startet den Apache2-Dienst nach der Installation.
        * *Hinweis*: Dies ist falsch. Der Status wird mit `systemctl status apache2` geprüft, der Dienst startet meist automatisch.
    * **C) Er aktualisiert die Paketlisten und Informationen über verfügbare Software auf dem System.**
        * *Hinweis*: Dies ist korrekt und dient als Vorbereitung für die eigentliche Installation.
    * D) Er entfernt eine bereits vorhandene Apache2-Installation.
        * *Hinweis*: Dies ist falsch. Zum Entfernen wird `apt remove` verwendet.
    * E) Er prüft, ob der Server über eine gültige IP-Adresse verfügt.
        * *Hinweis*: Dies ist falsch. `apt update` ist ein Paketmanagement-Befehl.

3.  **Welches ist das Standard-Webverzeichnis (Document Root), von dem Apache2 standardmäßig Inhalte ausliefert?**
    * A) `/home/www/html`
        * *Hinweis*: Dies ist falsch. Das Webverzeichnis befindet sich nicht im Home-Verzeichnis.
    * B) `/etc/apache2/html`
        * *Hinweis*: Dies ist falsch. `/etc` enthält Konfigurationsdateien, nicht die Inhalte.
    * **C) `/var/www/html`**
        * *Hinweis*: Dies ist korrekt. Dies ist das Standardverzeichnis unter Debian/Ubuntu.
    * D) `/usr/local/apache2`
        * *Hinweis*: Dies ist falsch. Dies ist oft das Installationsverzeichnis, nicht das Webverzeichnis.
    * E) `/var/log/apache2`
        * *Hinweis*: Dies ist falsch. Dieses Verzeichnis enthält die Log-Dateien des Servers.

4.  **Was ist der Hauptgrund für die Verwendung von PHP gegenüber statischen HTML-Seiten auf einem Webserver?**
    * A) PHP-Dateien werden schneller ausgeliefert als statische HTML-Seiten.
        * *Hinweis*: Dies ist falsch. Statische HTML-Seiten sind oft schneller, da keine serverseitige Verarbeitung nötig ist.
    * B) PHP ist eine Datenbank und speichert Benutzerdaten.
        * *Hinweis*: Dies ist falsch. PHP ist eine Skriptsprache, keine Datenbank, ermöglicht aber Interaktion mit Datenbanken.
    * **C) PHP ermöglicht die Erstellung dynamischer Webseiten, die Inhalte basierend auf Datenbanken oder Benutzereingaben generieren.**
        * *Hinweis*: Dies ist korrekt. PHP ist eine serverseitige Skriptsprache, die dynamische Inhalte ermöglicht.
    * D) PHP-Code wird direkt im Browser des Benutzers ausgeführt.
        * *Hinweis*: Dies ist falsch. PHP ist eine **serverseitige** Skriptsprache.
    * E) Die Verwendung von PHP ist gesetzlich vorgeschrieben.
        * *Hinweis*: Dies ist falsch. Es gibt keine solche Vorschrift.

5.  **Welchen Zweck erfüllt das Apache2-PHP-Modul (`libapache2-mod-php`), das in der Anleitung installiert wird?**
    * A) Es ist ein FTP-Client, der für den Upload von PHP-Dateien benötigt wird.
        * *Hinweis*: Dies ist falsch. FTP/SFTP wird für den Upload von außen genutzt.
    * B) Es ist ein Datenbankserver, der von PHP verwendet wird.
        * *Hinweis*: Dies ist falsch. Datenbanken wie MySQL werden separat installiert.
    * C) Es ermöglicht das Editieren von PHP-Dateien auf dem Server.
        * *Hinweis*: Dies ist falsch. Das wird durch Editoren wie `nano` oder SFTP-Clients ermöglicht.
    * **D) Es integriert den PHP-Interpreter in den Apache2-Webserver, um PHP-Dateien verarbeiten und ausliefern zu können.**
        * *Hinweis*: Dies ist korrekt. Das Modul (`libapache2-mod-php`) ist die notwendige Schnittstelle.
    * E) Es wird nur für die Überprüfung des PHP-Status über die Kommandozeile benötigt.
        * *Hinweis*: Dies ist falsch. Dafür wird `php-cli` installiert.

6.  **Welcher Befehl wird verwendet, um die Änderungen an der Apache2-Konfiguration zu übernehmen, ohne den Dienst komplett neu zu starten?**
    * A) `sudo systemctl stop apache2`
        * *Hinweis*: Dies ist falsch. Dieser Befehl stoppt den Dienst.
    * B) `sudo apt update`
        * *Hinweis*: Dies ist falsch. Dieser Befehl aktualisiert die Paketlisten.
    * **C) `sudo systemctl reload apache2`**
        * *Hinweis*: Dies ist korrekt. `reload` lädt die Konfiguration neu, ohne laufende Verbindungen zu unterbrechen, was effizienter ist als `restart`.
    * D) `sudo systemctl status apache2`
        * *Hinweis*: Dies ist falsch. Dieser Befehl prüft den Status.
    * E) `sudo systemctl start apache2`
        * *Hinweis*: Dies ist falsch. Dieser Befehl startet den Dienst.

7.  **Was ist die grundlegende Rolle von Benutzergruppen auf einem Linux-Server, insbesondere im Kontext der Apache2-Verwaltung (Abschnitt 3)?**
    * A) Sie sind erforderlich, um statische HTML-Seiten zu hosten.
        * *Hinweis*: Dies ist falsch. HTML-Seiten erfordern keine spezielle Gruppenverwaltung.
    * **B) Sie ermöglichen die zentrale Verwaltung von Zugriffsrechten für mehrere Benutzer auf Dateien, Verzeichnisse oder Systemdienste.**
        * *Hinweis*: Dies ist korrekt. Gruppen erleichtern die Verwaltung von Berechtigungen, da Rechte nicht einzeln für jeden Benutzer vergeben werden müssen.
    * C) Gruppen werden nur verwendet, um Benutzern Root-Rechte zu geben.
        * *Hinweis*: Dies ist falsch. Gruppen können auch für nicht-privilegierte Zugriffe genutzt werden (z. B. Leserechte).
    * D) Sie dienen dazu, die Server-IP-Adresse zu verschlüsseln.
        * *Hinweis*: Dies ist falsch. Gruppen haben nichts mit IP-Verschlüsselung zu tun.
    * E) Gruppen sind ein veraltetes Konzept und werden heute nicht mehr verwendet.
        * *Hinweis*: Dies ist falsch. Gruppen sind ein essenzieller Bestandteil der Linux-Berechtigungsverwaltung.

8.  **Warum wird das Werkzeug `visudo` anstelle eines direkten Editors (wie z.B. `nano /etc/sudoers`) verwendet, um die sudo-Rechte für die Gruppe `apacherestart` einzurichten?**
    * A) `visudo` ist nur über das Proxmox-Webinterface verfügbar.
        * *Hinweis*: Dies ist falsch. `visudo` ist ein Kommandozeilen-Tool.
    * B) Es ist das einzige Werkzeug, das Passwörter verschlüsselt.
        * *Hinweis*: Dies ist falsch. `visudo` hat primär andere Sicherheitsfunktionen.
    * **C) `visudo` führt eine Syntaxprüfung der `/etc/sudoers`-Datei durch, um zu verhindern, dass Fehler die gesamte `sudo`-Funktionalität des Systems sperren.**
        * *Hinweis*: Dies ist korrekt und der Hauptvorteil von `visudo`. Ein fehlerhaftes `sudoers`-File kann Root-Zugriff unmöglich machen.
    * D) Es kann nur von der Gruppe `apacherestart` ausgeführt werden.
        * *Hinweis*: Dies ist falsch. `visudo` wird mit Root-Rechten (oder `sudo`) ausgeführt.
    * E) Es erstellt automatisch die benötigte Gruppe `apacherestart`.
        * *Hinweis*: Dies ist falsch. Die Gruppe muss manuell mit `groupadd` erstellt werden.

9.  **Welchen Zweck erfüllt die Konfigurationszeile `Alias /user1 /home/user1/www` in der Apache-Konfigurationsdatei `stud-aliases.conf`?**
    * A) Sie erstellt den Benutzer `user1`.
        * *Hinweis*: Dies ist falsch. Der Benutzer wird mit `useradd` erstellt.
    * B) Sie legt fest, dass der Benutzer `user1` das Apache-Verzeichnis lesen darf.
        * *Hinweis*: Dies ist falsch. Dies ist eine Berechtigungsfrage.
    * C) Sie gewährt dem Apache-Server die Rechte, auf das Home-Verzeichnis zuzugreifen.
        * *Hinweis*: Dies ist falsch. Die Rechte werden mit `chown` und `chmod` eingestellt.
    * D) Sie konfiguriert den Apache-Server als Reverse Proxy.
        * *Hinweis*: Dies ist falsch. Ein Reverse Proxy leitet Anfragen weiter, was hier nicht der Fall ist.
    * **E) Sie weist den URL-Pfad `/user1` auf dem Webserver dem physischen Verzeichnis `/home/user1/www` auf dem Dateisystem zu, sodass der Inhalt über HTTP abrufbar ist.**
        * *Hinweis*: Dies ist korrekt. Ein Alias erstellt eine virtuelle Verzeichnisstruktur im Webserver, die auf ein anderes physisches Verzeichnis zeigt.

10. **Welche der folgenden Dateien oder Pfade wird bei der SFTP-Übertragung von Webdateien mit den Berechtigungen `sudo chown -R www-data:www-data` und `sudo chmod -R 755` versehen?**
    * A) Das `sudoers`-File für die Berechtigungsverwaltung.
        * *Hinweis*: Dies ist falsch. Die `sudoers`-Datei sollte nur von Root/Admin-Tools bearbeitet werden.
    * B) Das `ca.cert.pem` Zertifikat für die TLS-Verschlüsselung.
        * *Hinweis*: Dies ist falsch. Zertifikate haben andere Berechtigungen und sind nicht Teil dieses Prozesses.
    * C) Das Home-Verzeichnis des Benutzers (`/home/user1`).
        * *Hinweis*: Dies ist falsch. Das Home-Verzeichnis erhält in der Anleitung `chmod 755`, aber nicht `chown www-data:www-data`.
    * **D) Die Projektordner im Standard-Webverzeichnis (`/var/www/html/mein_projekt`) für größere Projekte.**
        * *Hinweis**: Dies ist korrekt. Diese Berechtigungen stellen sicher, dass der Apache-Prozess (`www-data`) die Dateien lesen kann und die Rechte korrekt gesetzt sind.
    * E) Die Hauptkonfigurationsdatei des Apache-Servers (`apache2.conf`).
        * *Hinweis*: Dies ist falsch. Diese Datei wird von Root/System-Accounts verwaltet.


---

### Lizenz
Dieses Werk ist lizenziert unter der **Creative Commons - Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz**.
 
[Zum Lizenztext auf der Creative Commons Webseite](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)
