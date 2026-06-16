---
title: "Checkliste zur Funktionsprüfung: pgAdmin4 auf LXC"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "pdal@jade-hs.de"
organization: "PDAL-Projekt"
date: "2025-10-30"
version: "1.0.0"
level: "Ebene 2, Lerneinheit 2.6.5, Assessment"
duration: "0,2 Std"
prerequisites: ["Abgeschlossen - 2600 PostgreSQL auf LXC installieren, konfigurieren und absichern"]
tags: ["PDAL","Assessment", "pgAdmin4", "Funktionsprüfung"]
license: "CC BY-SA 4.0"
---

# ✅ Checkliste zur Funktionsprüfung: pgAdmin4 auf LXC

Diese Checkliste dient der Überprüfung, ob die Installation von pgAdmin4 und die Verbindung zum PostgreSQL-Server erfolgreich eingerichtet wurden.

---

### 1. Web-Erreichbarkeit

**Ist die pgAdmin4-Weboberfläche über die konfigurierte URL (`http://192.168.137.130/pgadmin4`) vom Host-System aus erreichbar und erscheint die Login-Seite?**

* **Ja**
    * **Hinweis:** Der Apache2-Webserver läuft, die `pgadmin4.conf` ist korrekt konfiguriert und die Firewall lässt den Zugriff auf Port 80 zu.
* **Nein**
    * **Hinweis:** Prüfe, ob der Apache2-Dienst gestartet ist, der UFW-Port 80 (HTTP) freigegeben ist und die URL korrekt den Pfad `/pgadmin4` enthält.

### 2. Initial-Login

**Konnten Sie sich mit der in **Schritt 5** erstellten Admin-E-Mail-Adresse und dem Passwort erfolgreich in die pgAdmin4-Oberfläche einloggen?**

* **Ja**
    * **Hinweis:** Die Initialkonfiguration (`setup-web.sh`) wurde erfolgreich abgeschlossen und die lokale SQLite-Benutzerdatenbank (`pgadmin4.db`) wurde korrekt angelegt.
* **Nein**
    * **Hinweis:** Führen Sie das Script `/usr/pgadmin4/bin/setup-web.sh` erneut aus und stellen Sie sicher, dass Sie sich die Zugangsdaten notiert haben.

### 3. Netzwerk-Zugriff (PostgreSQL)

**Lässt sich der PostgreSQL-Server (`192.168.137.160`) in pgAdmin4 über den Reiter **Connection** erfolgreich hinzufügen, wenn der **SSL Mode testweise auf `disable`** gesetzt wird?**

* **Ja**
    * **Hinweis:** Die `pg_hba.conf` auf dem PostgreSQL-Server lässt die IP des pgAdmin-Containers zu, und die grundlegende Netzwerkverbindung funktioniert.
* **Nein**
    * **Hinweis:** Prüfe die `pg_hba.conf` auf dem PostgreSQL-Server (muss die IP des pgAdmin-Containers zulassen) und die `postgresql.conf` (`listen_addresses = '*'`).

### 4. Datenbank-Anzeige

**Wird nach erfolgreicher Verbindung (z. B. mit dem `pdal`-User) die zuvor erstellte Datenbank (`pdal`) und die **Beispielstabelle** (`beispiel`) in der pgAdmin4-Baumstruktur auf der linken Seite angezeigt?**

* **Ja**
    * **Hinweis:** Die Verbindungsinformationen (User, Host, DB-Name) sind korrekt, und der User hat die notwendigen Rechte (`CONNECT`) auf die Datenbank.
* **Nein**
    * **Hinweis:** Stellen Sie sicher, dass der verwendete User die korrekten Datenbankrechte besitzt und dass die Datenbank und Tabelle tatsächlich existieren (`\l` und `\dt` in der `psql`-Konsole prüfen).

### 5. SSL-Funktionalität

**Kann eine Verbindung zum PostgreSQL-Server erfolgreich hergestellt werden, wenn der **SSL Mode** in pgAdmin4 auf **`require`** (und nicht auf `disable`) gesetzt ist?**

* **Ja**
    * **Hinweis:** Die SSL-Verschlüsselung (`ssl = on`) ist auf dem PostgreSQL-Server korrekt konfiguriert, und der Server erzwingt oder akzeptiert verschlüsselte Verbindungen.
* **Nein**
    * **Hinweis:** Prüfen Sie die Logdateien des PostgreSQL-Servers (`/var/log/postgresql/`) auf SSL-Fehler. Stellen Sie sicher, dass `ssl = on` in der `postgresql.conf` aktiv ist und die erforderlichen Zertifikate existieren.

---

### Lizenz
Dieses Werk ist lizenziert unter der **Creative Commons - Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz**.
 
[Zum Lizenztext auf der Creative Commons Webseite](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)
