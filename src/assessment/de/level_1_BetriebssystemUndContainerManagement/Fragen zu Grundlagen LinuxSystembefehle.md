---
title: "Fragen zu Linux-Grundlagen"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "pdal@jade-hs.de"
organization: "PDAL-Projekt"
date: "2025-08-19"
version: "1.0.0"
level: "Ebene 1, Lerneinheit 1.2, Assessment"
duration: "0,2 Std"
prerequisites:["Abgeschlossen -  Dokument: 1200 - Grundlagen der Linux-Shell-Navigation und Systembefehle"]
tags: ["PDAL","Assessment"]
license: "CC BY-SA 4.0"
---

### Multiple-Choice-Fragen zu Linux-Grundlagen

**1. Welcher Befehl zeigt das aktuelle Arbeitsverzeichnis an?**
* A) `ls -l`
    * Hinweis: Dieser Befehl listet den Inhalt eines Verzeichnisses im Langformat auf.
* B) `cd ..`
    * Hinweis: Dieser Befehl wechselt in das übergeordnete Verzeichnis.
* **C) `pwd`**
    * Hinweis: Das Dokument beschreibt `pwd` als Befehl, der "den Pfad des aktuellen Arbeitsverzeichnisses" anzeigt.
* D) `mkdir`
    * Hinweis: Dieser Befehl dient zum Erstellen eines neuen Verzeichnisses.
* E) `man`
    * Hinweis: Dieser Befehl zeigt die offizielle Hilfeseite für einen Befehl an.

**2. Was bewirkt die Option `-r` in den Befehlen `rm` und `cp`?**
* A) Sie zeigt eine Rückfrage vor dem Löschen oder Überschreiben an.
    * Hinweis: Dafür wird die Option `-i` verwendet.
* B) Sie listet Verzeichnisse rekursiv auf.
    * Hinweis: Das ist eine Funktion des Befehls `ls` mit der Option `-R`.
* **C) Sie ermöglicht das rekursive Löschen oder Kopieren von Verzeichnissen und deren Inhalten.**
    * Hinweis: Das Dokument erklärt bei `rm` die Option `-r` für das Löschen von Verzeichnissen und bei `cp` für das rekursive Kopieren von Verzeichnissen.
* D) Sie ist nur für das Löschen von Dateien gedacht, nicht für das Kopieren.
    * Hinweis: Die Option `-r` funktioniert für beide Befehle.
* E) Sie löscht oder kopiert Dateien im schreibgeschützten Modus.
    * Hinweis: Dies ist keine Funktion der Option `-r`.

**3. Welcher Befehl wird empfohlen, um die `/etc/sudoers`-Datei sicher zu bearbeiten?**
* A) `nano /etc/sudoers`
    * Hinweis: Die Bearbeitung mit einem normalen Editor wird nicht empfohlen, da ein Tippfehler das System unbrauchbar machen kann.
* **B) `visudo`**
    * Hinweis: Das Dokument widmet der Verwendung von `visudo` einen eigenen Abschnitt und betont, dass es die Syntax prüft, um Fehler zu verhindern, die das System unbrauchbar machen könnten.
* C) `vim /etc/sudoers`
    * Hinweis: Die Bearbeitung mit einem normalen Editor wie `vim` wird nicht empfohlen, da ein Tippfehler das System unbrauchbar machen kann.
* D) `sudoers --edit`
    * Hinweis: Dieser Befehl existiert in dieser Form nicht.
* E) `gedit /etc/sudoers`
    * Hinweis: Die Bearbeitung mit einem normalen Editor wie `gedit` wird nicht empfohlen, da ein Tippfehler das System unbrauchbar machen kann.

**4. Welchen Zweck hat der Befehl `ping 8.8.8.8` laut Dokumentation?**
* A) Er testet die Verbindung zum lokalen Router (Gateway).
    * Hinweis: Dafür würde man die IP des Gateways (z.B. `192.168.137.1`) pingen.
* B) Er testet die Namensauflösung (DNS).
    * Hinweis: Dafür würde man eine Domain wie `heise.de` pingen.
* **C) Er überprüft, ob eine Verbindung zum Internet besteht.**
    * Hinweis: Im Abschnitt zu `ping` wird ausdrücklich erklärt, dass das Pingen einer externen IP wie `8.8.8.8` testet, "ob eine Verbindung ins Internet besteht".
* D) Er löscht den DNS-Cache des Systems.
    * Hinweis: Das ist keine Funktion von `ping`.
* E) Er setzt die Netzwerkschnittstelle zurück.
    * Hinweis: Das ist keine Funktion von `ping`.

**5. Was ist die Hauptfunktion des `Kernel` im Linux-Betriebssystem?**
* A) Er dient als Schnittstelle zwischen Benutzer und System.
    * Hinweis: Das ist die Funktion der Shell.
* B) Er verwaltet Konfigurationsdateien.
    * Hinweis: Konfigurationsdateien befinden sich in `/etc`.
* **C) Er ist das Herzstück des Systems und steuert Hardwarezugriffe und Prozesse.**
    * Hinweis: Im Abschnitt "Was ist Linux?" wird der Kernel als "Herzstück des Systems" beschrieben, das "Hardwarezugriffe und Prozesse" steuert.
* D) Er ist eine Sammlung grundlegender Systemprogramme.
    * Hinweis: Dies sind die GNU-Werkzeuge.
* E) Er verwaltet die Benutzerverzeichnisse.
    * Hinweis: Benutzerverzeichnisse werden im Verzeichnis `/home` gespeichert.

**6. Was ist die Funktion des Befehls `cd -`?**
* A) Er löscht das vorherige Verzeichnis.
    * Hinweis: Das ist nicht die Funktion des Befehls.
* **B) Er kehrt zum vorherigen Verzeichnis zurück.**
    * Hinweis: Das Dokument listet unter den Beispielen für den `cd`-Befehl ausdrücklich "cd - – Zum vorherigen Verzeichnis zurückkehren" auf.
* C) Er wechselt ins Wurzelverzeichnis (`/`).
    * Hinweis: Dafür wird der Befehl `cd /` verwendet.
* D) Er wechselt in das Verzeichnis, in dem man sich vor dem letzten Befehl befand.
    * Hinweis: Dies ist dasselbe wie die korrekte Antwort.
* E) Er wechselt ins Home-Verzeichnis.
    * Hinweis: Dafür wird der Befehl `cd` ohne Argumente verwendet.

**7. Was ist der Unterschied zwischen den Verzeichnissen `/bin` und `/sbin`?**
* A) `/bin` enthält temporäre Dateien, `/sbin` Systemprotokolle.
    * Hinweis: Temporäre Dateien sind in `/tmp`, Protokolle in `/var/log`.
* B) `/bin` enthält Konfigurationsdateien, `/sbin` Benutzerverzeichnisse.
    * Hinweis: Konfigurationsdateien sind in `/etc`, Benutzerverzeichnisse in `/home`.
* **C) `/bin` enthält Systembefehle für alle Benutzer, `/sbin` für Administratoren.**
    * Hinweis: Die Tabelle "Verzeichnisstruktur" im Dokument beschreibt genau diesen Unterschied.
* D) `/bin` ist für Benutzerprogramme, `/sbin` für Systemdienste.
    * Hinweis: Dies beschreibt eher den Unterschied zwischen `/usr` und `/sbin`.
* E) `/bin` enthält Kernel-Dateien, `/sbin` Bootloader-Dateien.
    * Hinweis: Diese Dateien befinden sich in `/boot`.

**8. Welcher Befehl wird verwendet, um die Systemzeit und Zeitzone zu verwalten?**
* A) `systemctl status`
    * Hinweis: Dieser Befehl zeigt den Status von Diensten an.
* B) `timesyncd`
    * Hinweis: Dies ist der Dienst, der die Zeitsynchronisation im Hintergrund durchführt.
* C) `date`
    * Hinweis: Dieser Befehl zeigt das aktuelle Datum und die Zeit an, verwaltet aber nicht die Zeitzone oder NTP.
* **D) `timedatectl`**
    * Hinweis: Das Dokument widmet diesem Befehl einen eigenen Abschnitt und erklärt seine Funktion zur Verwaltung von Zeit und Datum.
* E) `shutdown`
    * Hinweis: Dieser Befehl dient zum Herunterfahren oder Neustarten des Systems.

**9. Was bewirkt die Tastenkombination `STRG+X` im Texteditor `nano`?**
* A) Sie speichert die Datei.
    * Hinweis: Dafür wird `STRG+O` verwendet.
* B) Sie sucht nach Text.
    * Hinweis: Dafür wird `STRG+W` verwendet.
* **C) Sie beendet den Editor.**
    * Hinweis: Der Abschnitt über `nano` listet "STRG+X – Beenden" als eine der wichtigsten Tastenkombinationen auf.
* D) Sie schneidet den ausgewählten Text aus.
    * Hinweis: Das ist eine Funktion anderer Editoren.
* E) Sie fügt den Text aus der Zwischenablage ein.
    * Hinweis: Das ist eine Funktion anderer Editoren.

**10. Wenn ein geplanter System-Shutdown abgebrochen werden soll, welcher Befehl muss verwendet werden?**
* A) `shutdown -h`
    * Hinweis: Dieser Befehl führt ein Herunterfahren durch.
* B) `shutdown now`
    * Hinweis: Dieser Befehl führt ein sofortiges Herunterfahren durch.
* **C) `shutdown -c`**
    * Hinweis: Die Tabelle "Wichtige Optionen" im Abschnitt zu `shutdown` führt "cancel" als Option `-c` auf und beschreibt sie als "Geplantes Herunterfahren abbrechen".
* D) `reboot`
    * Hinweis: Dieser Befehl startet das System neu.
* E) `poweroff`
    * Hinweis: Dieser Befehl schaltet das System vollständig aus.

---

### Lizenz
Dieses Werk ist lizenziert unter der **Creative Commons - Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz**.
 
[Zum Lizenztext auf der Creative Commons Webseite](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)

