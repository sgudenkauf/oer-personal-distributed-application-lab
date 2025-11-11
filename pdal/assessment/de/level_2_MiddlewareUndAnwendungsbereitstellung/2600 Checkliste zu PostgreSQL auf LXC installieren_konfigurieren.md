---
title: "Checkliste zu PostgreSQL auf LXC installieren, konfigurieren"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "uwe.bachmann@jade-hs.de"
organization: "PDAL-Projekt"
date: "2025-09-25"
version: "1.0.0"
level: "Ebene 2, Lerneinheit 2.3, Assessment"
duration: "0,2 Std"
prerequisites: ["Abgeschlossen - 2600 PostgreSQL auf LXC installieren, konfigurieren"]
tags: ["PDAL","Assessment"]
license: "CC BY-SA 4.0"
---

# ❓ Checkliste zu PostgreSQL auf LXC installieren, konfigurieren 

### Installation

**Muss für die Installation von PostgreSQL 16 das Paket `postgresql-contrib` zwingend mitinstalliert werden, um die Basis-Funktionalität des DBMS nutzen zu können?**

* **Ja**
    * **Hinweis:** Das ist nicht korrekt. `postgresql-contrib` enthält optionale Erweiterungen und Funktionen wie z. B. `pg_trgm` oder `dblink`. Die Kerninstallation wird durch das Hauptpaket `postgresql-16` abgedeckt.
* **Nein**
    * **Hinweis:** Das ist richtig. `postgresql-contrib` enthält nur optionale Erweiterungen. Für die Grundfunktionen des Datenbankmanagementsystems ist nur das Hauptpaket `postgresql-16` erforderlich.

### In Datenbank anmelden

**Ist der Befehl `sudo -u postgres psql` der einzige Weg, sich nach der Installation lokal auf der LXC-Konsole an der PostgreSQL-Datenbank anzumelden?**

* **Ja**
    * **Hinweis:** Das ist nicht korrekt. Sie können sich, nachdem Sie die `pg_hba.conf` angepasst und das Passwort gesetzt haben, auch direkt mit dem erstellten Systemadministrator-User `pdal` anmelden, z. B. `psql -U pdal`.
* **Nein**
    * **Hinweis:** Das ist richtig. Der Befehl `sudo -u postgres psql` nutzt die `peer`-Authentifizierung des Linux-Systems. Später kann man sich auch mit anderen erstellten PostgreSQL-Usern und dem Befehl `psql -U <User>` anmelden, sofern die Passwort-Authentifizierung aktiviert ist.

### Benutzer erzeugen

**Kann der Benutzer `dbadmin_pdal` ohne weitere Rechte systemweit neue Datenbanken erstellen (z. B. `CREATE DATABASE testdb;`)?**

* **Ja**
    * **Hinweis:** Das ist nicht korrekt. Der `dbadmin_pdal` hat die Rolle `db_admin` zugewiesen bekommen, welche **kein** `CREATEDB`-Recht besitzt. Nur der Superuser (`db_system_admin` / `pdal`) hat dieses Recht.
* **Nein**
    * **Hinweis:** Das ist richtig. Die Rolle `db_admin` wurde bewusst **ohne** das `CREATEDB`-Recht erstellt, um die Verantwortung für die Datenbankerstellung beim übergeordneten Systemadministrator (`pdal`) zu belassen.

### Rechtemanagement

**Wird die lokale Anmeldung für alle Benutzer nach der Änderung in der `pg_hba.conf` von `peer` auf `md5` automatisch auf Passwort-Authentifizierung umgestellt, auch ohne explizites Passwort-Setzen?**

* **Ja**
    * **Hinweis:** Das ist nicht korrekt. Obwohl die Umstellung auf `md5` die Passwortprüfung **erzwingt**, muss das Passwort für die betroffenen PostgreSQL-User (`pdal`, `dbadmin_pdal`, etc.) **zuvor** in der SQL-Konsole gesetzt worden sein.
* **Nein**
    * **Hinweis:** Das ist richtig. Die `pg_hba.conf`-Änderung zwingt den Server lediglich dazu, ein Passwort zu verlangen. Existiert dieses Passwort im PostgreSQL-System noch nicht, schlägt die Anmeldung fehl.

### Tabelle erzeugen

**Muss der `standard_user` (`appuser_pdal`) für jede neu erstellte Tabelle, die innerhalb der Datenbank `pdal` angelegt wird, explizit die Rechte `SELECT, INSERT, UPDATE, DELETE` erhalten, um Daten bearbeiten zu dürfen?**

* **Ja**
    * **Hinweis:** Das ist nicht korrekt. Dank des Befehls `ALTER DEFAULT PRIVILEGES IN SCHEMA public ...` erhält der `appuser_pdal` diese Rechte automatisch auf alle **zukünftig** in diesem Schema erstellten Tabellen.
* **Nein**
    * **Hinweis:** Das ist richtig. Die **Standard-Rechte** (Default Privileges) wurden für den `appuser_pdal` so gesetzt, dass er nicht bei jeder neuen Tabelle manuell berechtigt werden muss.

---

### Lizenz
Dieses Werk ist lizenziert unter der **Creative Commons - Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz**.
 
[Zum Lizenztext auf der Creative Commons Webseite](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)