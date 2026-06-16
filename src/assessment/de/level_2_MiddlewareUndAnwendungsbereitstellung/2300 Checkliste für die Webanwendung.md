---
title: "Checkliste für die Webanwendung "
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "pdal@jade-hs.de"
organization: "PDAL-Projekt"
date: "2025-09-25"
version: "1.0.0"
level: "Ebene 2, Lerneinheit 2.3, Assessment"
duration: "0,2 Std"
prerequisites: ["Abgeschlossen - 2300 Eigene Webanwendung mit Datenbankanbindung"]
tags: ["PDAL","Assessment"]
license: "CC BY-SA 4.0"
---

## 📝 Checkliste für die Webanwendung 

Jede Frage bezieht sich auf die korrekte Implementierung der **Kontaktlisten-Anwendung**. Die korrekte Antwort ist immer **Wahr**, da sie die Einhaltung der Best Practice überprüft.

### 1. Datenbankschema

**Frage 1:** Die `contacts`-Tabelle wurde in der `contacts_db` Datenbank angelegt und enthält das Feld `id` als **`PRIMARY KEY`** und **`AUTO_INCREMENT`**.

| Antwort | Hinweis (Feedback) |
| :--- | :--- |
| **Wahr** | **Korrekt.** Ein Primärschlüssel mit Auto-Increment ist essentiell, um jeden Datensatz eindeutig identifizieren und verwalten zu können (CRUD). |
| Falsch | Prüfen Sie Ihren SQL-Befehl. Ohne einen eindeutigen Primärschlüssel (`id INT AUTO_INCREMENT PRIMARY KEY`) kann das Skript Datensätze später nicht zuverlässig löschen oder bearbeiten. |

---

### 2. Funktionalität: Kontakte hinzufügen (CREATE)

**Frage 2:** Nach dem erfolgreichen Ausfüllen und Absenden des Formulars erscheint der **neu erstellte Kontakt** unmittelbar in der Kontaktliste auf der Hauptseite.

| Antwort | Hinweis (Feedback) |
| :--- | :--- |
| **Wahr** | **Korrekt.** Dies bestätigt, dass die `INSERT`-Anweisung funktioniert und die Datenbankabfrage (`SELECT`) die neuen Daten korrekt ausliest und anzeigt. |
| Falsch | Prüfen Sie, ob der `INSERT INTO contacts` Befehl im PHP-Skript korrekt formuliert ist und die `$_POST`-Daten richtig an die Prepared Statements übergeben werden. Auch der anschließende `header('Location: ...')` Redirect muss stimmen. |

---

### 3. Funktionalität: Liste anzeigen (READ)

**Frage 3:** Wenn in der Datenbank Kontakte vorhanden sind, werden diese in einer **geordneten HTML-Tabelle** dargestellt, wobei das Ergebnis standardmäßig nach dem **Namen** sortiert ist.

| Antwort | Hinweis (Feedback) |
| :--- | :--- |
| **Wahr** | **Korrekt.** Dies bestätigt die korrekte Funktion des `SELECT * FROM contacts ORDER BY name` Befehls und der anschließenden `foreach`-Schleife in der HTML-Ausgabe. |
| Falsch | Überprüfen Sie den `SELECT`-Befehl im Abschnitt **3. DATEN ABFRAGEN (READ)**. Stellen Sie sicher, dass `fetchAll()` die Daten korrekt in das `$contacts`-Array lädt und die HTML-Struktur die Daten richtig iteriert. |

---

### 4. Funktionalität: Kontakte löschen (DELETE)

**Frage 4:** Das Klicken auf den **"Löschen"-Link** entfernt den zugehörigen Kontakt aus der Liste und aus der Datenbank, ohne dass eine Fehlermeldung auftritt.

| Antwort | Hinweis (Feedback) |
| :--- | :--- |
| **Wahr** | **Korrekt.** Dies bestätigt, dass der `DELETE`-Befehl korrekt über die URL-Parameter (`?delete_id=...`) ausgelöst wird, die ID sicher an das Prepared Statement übergeben wird und der Datensatz entfernt wird. |
| Falsch | Prüfen Sie den **DELETE-Codeblock** (`isset($_GET['delete_id'])`). Stellen Sie sicher, dass der `href`-Link im HTML die korrekte `id` übergibt und der PHP-Code diese ID zur Ausführung des `DELETE`-Statements verwendet. |

---

## Weiterführende Frage


### 5. Datenbankverbindung (Index-Skript)

**Frage 5:** Der PDO-Verbindungs-Code im `index.php` Skript verwendet die Option **`PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION`**, um Datenbankfehler als PHP-Exceptions auszugeben.

| Antwort | Hinweis (Feedback) |
| :--- | :--- |
| **Wahr** | **Korrekt.** Dies ist die moderne und sauberste Art der Fehlerbehandlung in PHP-Datenbankverbindungen und essenziell für die Fehlersuche. |
| Falsch | Suchen Sie nach dem `try/catch`-Block im Verbindungs-Code. Ohne diese Option ignoriert PDO Fehler stumm, was die Fehlersuche fast unmöglich macht. |

---

### 6. Sicherheit und CRUD-Logik

**Frage 6:** Zum Einfügen (`INSERT`) und Löschen (`DELETE`) von Daten werden **Prepared Statements** (`$pdo->prepare(...)`) verwendet, um Benutzereingaben sicher zu verarbeiten.

| Antwort | Hinweis (Feedback) |
| :--- | :--- |
| **Wahr** | **Korrekt.** Prepared Statements sind der **wichtigste** Schutzmechanismus gegen **SQL Injection**. |
| Falsch | Prüfen Sie die Abschnitte für CREATE und DELETE. Wenn Sie Benutzereingaben (`$_POST` oder `$_GET`) direkt im SQL-Query verwenden, besteht eine hohe Sicherheitslücke (SQL Injection). Nutzen Sie Platzhalter (`?` oder `:name`). |

---

### 7. Ausgabe-Sicherheit

**Frage 7:** Die aus der Datenbank gelesenen Kontaktdaten (`$contact['name']`, etc.) werden bei der HTML-Ausgabe mit **`htmlspecialchars()`** geschützt.

| Antwort | Hinweis (Feedback) |
| :--- | :--- |
| **Wahr** | **Korrekt.** Dies verhindert **Cross-Site Scripting (XSS)**, indem spezielle HTML-Zeichen (wie `<` und `>`) korrekt encodiert werden, bevor sie im Browser dargestellt werden. |
| Falsch | Überprüfen Sie den `<tbody>`-Bereich in Ihrem HTML-Code. Ungeschützte Ausgaben von Benutzereingaben (`<?= $contact['name'] ?>`) stellen ein XSS-Sicherheitsrisiko dar. |

---

### 8. Code-Organisation und Muster (PRG)

**Frage 8:** Nach dem Hinzufügen oder Löschen eines Kontakts wird die Seite mithilfe der PHP-Funktion **`header('Location: ...')`** neu geladen (Post/Redirect/Get-Muster).

| Antwort | Hinweis (Feedback) |
| :--- | :--- |
| **Wahr** | **Korrekt.** Dieses Muster (PRG) verhindert, dass der Benutzer bei einem Neuladen der Seite (F5) die Daten (z.B. den INSERT-Befehl) erneut sendet. |
| Falsch | Prüfen Sie die `if ($_SERVER['REQUEST_METHOD'] === 'POST' ...)`-Blöcke. Wenn der Redirect (`header()`) fehlt, fragt der Browser bei F5, ob die Daten erneut gesendet werden sollen. |

---

### 9. Code-Modularität (Weiterentwicklung)

**Frage 9:** Die Datenbank-Konfiguration (`db_config.php`) wird im `index.php` mit der Anweisung **`require_once`** eingebunden.

| Antwort | Hinweis (Feedback) |
| :--- | :--- |
| **Wahr** | **Korrekt.** `require_once` ist besser als `include`, weil es das Skript bei fehlender Konfigurationsdatei stoppt (kritischer Fehler) und eine doppelte Einbindung verhindert. |
| Falsch | Prüfen Sie die erste Zeile, nachdem Sie die Konfiguration ausgelagert haben. Wenn Sie `include` oder `require` ohne `_once` verwenden, verpassen Sie die Gelegenheit, die beste Praxis für kritische Code-Teile anzuwenden. |

---

### 10. Sicherheit des Konfigurationspfades (Erweitert)

**Frage 10:** Für ein Produktivsystem würde die Datei `db_config.php` **außerhalb** des vom Webserver zugänglichen Verzeichnisses (`/var/www/html/`) gespeichert werden.

| Antwort | Hinweis (Feedback) |
| :--- | :--- |
| **Wahr** | **Korrekt.** Dies ist eine fundamentale Sicherheitspraxis. Sollte der Webserver fehlerhaft konfiguriert sein, können die sensiblen Anmeldedaten nicht direkt über den Browser abgerufen werden. |
| Falsch | Obwohl die Datei im Lernprojekt im selben Ordner liegen mag: In Produktion muss sie gesichert werden. Wenn der PHP-Interpreter ausfällt, kann ein Benutzer sonst die Anmeldedaten über die URL `.../db_config.php` einsehen. |

---

### Lizenz
Dieses Werk ist lizenziert unter der **Creative Commons - Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz**.
 
[Zum Lizenztext auf der Creative Commons Webseite](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)

