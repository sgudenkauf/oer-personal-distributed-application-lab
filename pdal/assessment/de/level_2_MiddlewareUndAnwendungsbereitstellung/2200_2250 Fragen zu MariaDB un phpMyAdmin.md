---
title: "Fragen zu MariaDB und phpMyAdmin"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "uwe.bachmann@jade-hs.de"
organization: "PDAL-Projekt"
date: "2025-09-25"
version: "1.0.0"
level: "Ebene 2, Lerneinheit 2.2x, Assessment"
duration: "0,2 Std"
prerequisites:["Abgeschlossen - 2100 Apache2-Webserver und Benutzerverwaltung im LXC-Container", "Abgeschossen - Installation und Konfiguration von phpMyAdmin im Apache2 LXC", "Abgeschlossen - Installation und Konfiguration von MariaDB im LXC-Container"]
tags: ["PDAL","Assessment"]
license: "CC BY-SA 4.0"
---

## Multiple-Choice-Fragen zu MariaDB und phpMyAdmin (Lerneinheit 2.2)

### 1. Installation und Betrieb

**Frage 1: Welcher Befehl wird in der Shell eines Ubuntu LXC-Containers ausgeführt, um MariaDB als Datenbankserver zu installieren?**

A. `sudo apt install mysql-server`
> **Hinweis:** Dies würde den originalen MySQL-Server von Oracle installieren. MariaDB ist ein Fork.

B. `sudo mariadb --install`
> **Hinweis:** Dies ist kein gültiger `apt`- oder Shell-Befehl zur Installation.

C. `sudo systemctl start mariadb`
> **Hinweis:** Dies ist der Befehl zum Starten des Dienstes, nicht zur Installation des Pakets.

D. `sudo apt get install mariadb-db`
> **Hinweis:** Der korrekte `apt`-Befehl verwendet `apt install`.

**E. `sudo apt install mariadb-server`**
> **Hinweis:** **Korrekt.** Dies ist der Standardpaketname für den MariaDB-Server unter Debian/Ubuntu.

---

### 2. Sicherheit und Konfiguration

**Frage 2: Welchen Zweck hat die Änderung der Einstellung `bind-address = 127.0.0.1` in der MariaDB-Konfigurationsdatei (`50-server.cnf`) zu einer spezifischen Container-IP (z.B. `192.168.137.120`)?**

A. Die Datenbank wird nur noch über das Unix Socket zugänglich sein.
> **Hinweis:** Die Änderung auf eine IP entfernt nicht den Socket-Zugriff, blockiert aber externe TCP-Verbindungen.

B. Die MariaDB-Performance wird durch eine dedizierte IP optimiert.
> **Hinweis:** Die Performance wird dadurch nicht direkt beeinflusst, nur die Netzwerkerreichbarkeit.

C. Es wird der Standardport 3306 auf Port 80 umgeleitet.
> **Hinweis:** Die `bind-address` definiert das Interface, nicht den Port.

D. Die Datenbank ist nur noch für lokale Programme (localhost) erreichbar.
> **Hinweis:** Das Gegenteil ist der Fall: `127.0.0.1` macht sie nur lokal erreichbar.

**E. Die Datenbank wird zusätzlich zur Localhost-Schnittstelle über diese spezifische IP für externe Clients im Netzwerk erreichbar.**
> **Hinweis:** **Korrekt.** Die Datenbank "lauscht" nun auf dieser IP und erlaubt Remote-Verbindungen, sofern der Firewall-Port 3306 offen ist.

---

### 3. Benutzerverwaltung und Berechtigungen

**Frage 3: Welcher SQL-Befehl ist notwendig, um nach dem Anlegen eines neuen Datenbankbenutzers und dem Setzen von Berechtigungen die Änderungen sofort zu aktivieren, ohne den MariaDB-Dienst neu zu starten?**

A. `COMMIT;`
> **Hinweis:** `COMMIT` wird verwendet, um Transaktionen zu beenden, nicht um die Berechtigungstabellen zu aktualisieren.

B. `UPDATE PRIVILEGES;`
> **Hinweis:** Dies ist keine gültige SQL-Anweisung zur Aktualisierung der Berechtigungen.

C. `RESTART SERVICE;`
> **Hinweis:** Dies wäre ein Betriebssystembefehl (`systemctl`), nicht SQL, und ist unnötig.

D. `ENABLE USER 'pdal';`
> **Hinweis:** Der Benutzer ist sofort nach `CREATE USER` aktiv.

**E. `FLUSH PRIVILEGES;`**
> **Hinweis:** **Korrekt.** Dieser Befehl weist MariaDB an, die im Arbeitsspeicher gehaltenen Berechtigungen neu aus den Grant-Tabellen zu laden.

---

### 4. Zeichenkodierung

**Frage 4: Was bewirkt die Einstellung `collation-server = utf8mb4_general_ci` in der MariaDB-Konfiguration in Bezug auf Textvergleiche und Sortierung?**

A. Sie beschleunigt die Abfragen von Textfeldern.
> **Hinweis:** Kollationen beeinflussen die Logik, nicht direkt die Geschwindigkeit (im Vergleich zu anderen Kollationen).

B. Sie erzwingt die Verwendung des alten `utf8`-Zeichensatzes.
> **Hinweis:** `utf8mb4` ist die moderne, erweiterte Version von UTF-8.

**C. Textvergleiche erfolgen "Case-Insensitive" (Groß- und Kleinschreibung werden nicht unterschieden).**
> **Hinweis:** **Korrekt.** Das Suffix `_ci` (Case Insensitive) bewirkt, dass z.B. "Test" und "test" als gleichwertig behandelt werden.

D. Textvergleiche erfolgen "Case-Sensitive" (Groß- und Kleinschreibung wird unterschieden).
> **Hinweis:** Dies würde das Suffix `_cs` (Case Sensitive) erfordern.

E. Es wird nur der ASCII-Zeichensatz unterstützt.
> **Hinweis:** `utf8mb4` unterstützt den vollen Unicode-Zeichensatz, einschließlich Emojis und Sonderzeichen.

---

### 5. phpMyAdmin-Installation

**Frage 5: Warum wird bei der Installation von phpMyAdmin (`apt install phpmyadmin php-mysql`) auf die Frage nach der Konfiguration mit `dbconfig-common` mit "Nein" geantwortet, wenn MariaDB in einem separaten LXC-Container läuft?**

A. `dbconfig-common` kann keine MariaDB-Datenbanken verwalten.
> **Hinweis:** Das Tool kann sowohl MySQL als auch MariaDB verwalten, aber nur, wenn sie lokal oder direkt erreichbar sind.

B. `dbconfig-common` ist veraltet und sollte nicht mehr verwendet werden.
> **Hinweis:** Das Tool ist weiterhin Bestandteil der Debian/Ubuntu-Repositories.

C. Die Installation würde scheitern, da PHP nicht auf dem MariaDB-Container läuft.
> **Hinweis:** Das Scheitern liegt an der fehlenden lokalen Datenbank.

D. Die Datenbankstruktur wird später manuell über die WebGUI von phpMyAdmin erstellt.
> **Hinweis:** Die Struktur (`create_tables.sql`) wird manuell, aber über den Host und den Client erstellt, nicht über die WebGUI.

**E. Die Datenbank läuft extern, und `dbconfig-common` versucht, die benötigte Konfigurationsdatenbank lokal zu erstellen und zu verknüpfen, was fehlschlagen würde oder unerwünscht ist.**
> **Hinweis:** **Korrekt.** Da die Datenbank auf einem anderen Host liegt, muss die Konfiguration manuell vorgenommen werden.

---

### 6. phpMyAdmin-Verbindung

**Frage 6: Welche Konfigurationszeile muss in `/etc/phpmyadmin/config.inc.php` im Apache-Container angepasst werden, um die Verbindung zur externen MariaDB-IP (`192.168.137.120`) herzustellen?**

A. `$cfg['Servers'][$i]['ip'] = '192.168.137.120';`
> **Hinweis:** Der korrekte Schlüssel für die Host-Adresse ist nicht `ip`.

B. `$cfg['Servers'][$i]['bind-address'] = '192.168.137.120';`
> **Hinweis:** `bind-address` ist ein MariaDB-Server-Parameter, kein phpMyAdmin-Client-Parameter.

C. `$cfg['Servers'][$i]['database'] = '192.168.137.120';`
> **Hinweis:** Der `database`-Schlüssel würde den Namen der Standarddatenbank festlegen.

D. `if (empty($dbserver)) $dbserver = '192.168.137.120';`
> **Hinweis:** Diese Zeile wird zwar ergänzt, ist aber nicht die Hauptkonfigurationszeile für den Host.

**E. `$cfg['Servers'][$i]['host'] = '192.168.137.120';`**
> **Hinweis:** **Korrekt.** Der Schlüssel `host` definiert die IP-Adresse des Datenbankservers, zu dem phpMyAdmin eine Verbindung aufbauen soll.

---

### 7. Erweiterte phpMyAdmin-Funktionen

**Frage 7: Welchen Hauptzweck erfüllt die Datenbank `phpmyadmin` (mit den Tabellen `pma__*`) nach ihrer Erstellung und Verknüpfung in der Konfigurationsdatei (`config.inc.php`)?**

A. Sie speichert die tatsächlichen Benutzerdaten der Webanwendung.
> **Hinweis:** Die Datenbank ist nur für Verwaltungsaufgaben von phpMyAdmin selbst gedacht.

B. Sie dient als temporärer Speicher für große SQL-Abfragen.
> **Hinweis:** Die Datenbank enthält persistente Konfigurationsdaten, nicht temporäre Abfragen.

C. Sie speichert die Logins und Passwörter der Datenbank-User.
> **Hinweis:** MariaDB speichert Passwörter intern; phpMyAdmin speichert sie nicht.

D. Sie speichert die Apache2-Zugriffslogs zur späteren Analyse.
> **Hinweis:** Dies ist eine Aufgabe des Webservers oder eines Log-Servers.

**E. Sie ermöglicht erweiterte phpMyAdmin-Features wie den Designer, Bookmarks und Relationen-Darstellung.**
> **Hinweis:** **Korrekt.** Der Konfigurationsspeicher (Advanced Features) wird benötigt, um diese Zusatzfunktionen zu aktivieren, da sie Metadaten speichern müssen.

---

### 8. Host als Brücke

**Frage 8: Welches Proxmox-Kommando wird verwendet, um die `create_tables.sql` Datei aus dem MariaDB-Container (CT 120) zurück auf den Proxmox-Host zu kopieren, nachdem sie dort ausgeführt wurde?**

A. `pct exec 120 -- cp /tmp/create_tables.sql /root/`
> **Hinweis:** Dieser Befehl kopiert die Datei nur *innerhalb* des Containers.

B. `pct move 120 /tmp/create_tables.sql /root/`
> **Hinweis:** `pct move` ist für das Verschieben des *gesamten Containers* gedacht.

C. `scp /tmp/create_tables.sql root@120:/root/`
> **Hinweis:** Dies wäre ein netzwerkbasiertes `scp` und erfordert SSH-Zugriff und Konfiguration.

**D. `pct pull 120 /tmp/create_tables.sql /root/`**
> **Hinweis:** **Korrekt.** Der `pct pull`-Befehl kopiert Dateien *vom* Container *auf* den Host.

E. `pct push 120 /tmp/create_tables.sql /root/`
> **Hinweis:** `pct push` kopiert Dateien *vom* Host *in* den Container.

---

### 9. Systemd und MariaDB

**Frage 9: Was ist der Hauptgrund, warum der Befehl `sudo systemctl enable mariadb` nach der Installation des MariaDB-Servers ausgeführt wird?**

A. Er konfiguriert die Datenbank für den Remote-Zugriff.
> **Hinweis:** Dafür ist die `bind-address` in der Konfiguration zuständig.

B. Er führt das Sicherheitsskript `mysql_secure_installation` aus.
> **Hinweis:** Das Skript muss separat aufgerufen werden.

C. Er sorgt dafür, dass die Datenbank sofort gestartet wird.
> **Hinweis:** Dafür ist der Befehl `systemctl start` zuständig.

D. Er installiert alle notwendigen MariaDB-Dependencies.
> **Hinweis:** Dies ist die Aufgabe von `apt install`.

**E. Er sorgt dafür, dass der MariaDB-Dienst nach einem Neustart des Containers automatisch wieder gestartet wird.**
> **Hinweis:** **Korrekt.** `enable` erstellt den notwendigen Symlink, damit der Dienst beim Systemstart aktiviert wird (Persistence).

---

### 10. Fehlerbehebung in phpMyAdmin

**Frage 10: Bei einem `Access denied` Fehler von phpMyAdmin ist die wahrscheinlichste Ursache im MariaDB-Container, wenn der Benutzer `pdal` auf der Datenbankseite existiert?**

A. Die `bind-address` in MariaDB ist auf `0.0.0.0` gesetzt.
> **Hinweis:** `0.0.0.0` würde den Zugriff *ermöglichen*, nicht blockieren (vorausgesetzt die Firewall erlaubt es).

B. Der MariaDB-Dienst wurde nicht mit `systemctl start` gestartet.
> **Hinweis:** Dann wäre es ein Verbindungsfehler, kein `Access denied`.

C. Die Apache-Firewall blockiert Port 80.
> **Hinweis:** Dies würde den Zugriff auf die phpMyAdmin-Webseite verhindern, nicht den Datenbank-Zugriff.

D. Die Konfigurationsdatenbank (`phpmyadmin`) wurde nicht erstellt.
> **Hinweis:** Dies würde nur die "Advanced Features"-Warnung auslösen, nicht den Login blockieren.

**E. Der Benutzer `pdal` hat in der MariaDB-Datenbank keine Berechtigung für die Host-Adresse des Apache-Containers (z.B. `192.168.137.101`).**
> **Hinweis:** **Korrekt.** `Access denied` bedeutet, dass der Datenbankserver die Kombination aus Benutzername, Passwort und **Host-Adresse** (von wo die Verbindung kommt) nicht akzeptiert.

---

### Lizenz
Dieses Werk ist lizenziert unter der **Creative Commons - Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz**.
 
[Zum Lizenztext auf der Creative Commons Webseite](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)
