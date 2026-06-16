---
title: "Checkliste zur Überprüfung des REST-Service"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "pdal@jade-hs.de"
organization: "PDAL-Projekt"
date: "2025-09-25"
version: "1.0.0"
level: "Ebene 2, Lerneinheit 2.3, Assessment"
duration: "0,2 Std"
prerequisites: ["Abgeschlossen - 2400 REST-Anwendungen - Eigenentwicklung und externe Nutzung"]
tags: ["PDAL","Assessment"]
license: "CC BY-SA 4.0"
---
***

## ✅ Checkliste zur Überprüfung des REST-Service

Die erfolgreiche Implementierung des Temperaturumrechnungs-Web-Services kann anhand der folgenden Punkte überprüft werden. Diese dienen als Wahr-/Falsch-Fragen zur Überprüfung der korrekten Funktionalität der erstellten PHP-Anwendung.

### 1. Dateistruktur und Basis-Funktionalität

**Frage 1: Dateierstellung erfolgreich**

Die PHP-Datei `tempUmrechner.php` wurde korrekt im Verzeichnis `/rest/` des Web-Servers erstellt und mit dem gesamten Code aus dem Dokument befüllt.

* **Antwort Wahr:** Die Quelldatei existiert am korrekten Ort, und die Berechtigungen ermöglichen dem Webserver den Zugriff darauf.
* **Antwort Falsch (Korrekturhinweis):** Prüfen Sie, ob die Datei unter dem richtigen Pfad (z.B. `/var/www/html/rest/`) liegt und ob der Webserver (Apache2) läuft und PHP korrekt verarbeitet. Ein Syntaxfehler im Code kann ebenfalls den Aufruf verhindern.

**Frage 2: Basis-Aufruf im Browser**

Der Aufruf im Browser mit dem Beispiel-Link (`http://<ip-webcontainer>/rest/tempUmrechner.php?wert=20&einheit=celsius`) funktionierte und lieferte als Antwort das JSON-Objekt **{"einheit":"fahrenheit","wert":68}** zurück.

* **Antwort Wahr:** Der Web-Service ist erreichbar, PHP verarbeitet die Eingaben erfolgreich, und die Basis-Umrechnung funktioniert.
* **Antwort Falsch (Korrekturhinweis):** Stellen Sie sicher, dass Apache2 und PHP aktiv sind. Ein HTTP-Statuscode **500** deutet auf einen internen Serverfehler hin, der meist durch einen Syntaxfehler im PHP-Code verursacht wird.

***

### 2. Korrekte Umrechnungslogik

**Frage 3: Konvertierung von Celsius nach Fahrenheit**

Die Abfrage für die Werte **$28.4^\circ$ Celsius** (`wert=28.4&einheit=celsius`) liefert den korrekten Wert **$83.12$ Fahrenheit** zurück.

* **Antwort Wahr:** Die im Code hinterlegte Formel $(\text{C} \times 1.8) + 32$ wurde korrekt implementiert und führt zum korrekten Ergebnis.
* **Antwort Falsch (Korrekturhinweis):** Überprüfen Sie im PHP-Skript die Berechnung: `$wert * 1.8 + 32`. Stellen Sie sicher, dass die Variable `$wert` korrekt verwendet wird.

**Frage 4: Konvertierung von Fahrenheit nach Celsius**

Die Abfrage für die Werte **$100.4^\circ$ Fahrenheit** (`wert=100.4&einheit=fahrenheit`) liefert den korrekten Wert **$38.0$ Celsius** zurück.

* **Antwort Wahr:** Die im Code hinterlegte Formel $(\text{F} - 32) / 1.8$ wurde korrekt implementiert und führt zum korrekten Ergebnis.
* **Antwort Falsch (Korrekturhinweis):** Überprüfen Sie im PHP-Skript die korrekte Klammerung und Subtraktion: `($wert - 32) / 1.8`. Fehler in dieser Formel sind häufig auf fehlende Klammern zurückzuführen.

***

### 3. Stabile Fehlerbehandlung (Validierung)

**Frage 5: Umgang mit fehlenden Parametern**

Wenn die URL ohne den Parameter `wert` (oder `einheit`) aufgerufen wird, gibt der Service den HTTP-Statuscode **400** und eine erklärende Fehlermeldung im JSON-Format zurück.

* **Antwort Wahr:** Die erste Fehlerbehandlung (`!isset($_GET['wert']) || !isset($_GET['einheit'])`) wurde erfolgreich implementiert und verhindert, dass das Skript abstürzt.
* **Antwort Falsch (Korrekturhinweis):** Prüfen Sie den Codeblock unter **1. Prüfen auf benötigte Parameter**. Die Funktion `sendError(400, "Fehlende Parameter...")` muss bei fehlenden Eingaben aufgerufen werden.

**Frage 6: Umgang mit ungültigen Werten**

Wenn der Parameter `wert` einen nicht-numerischen Wert (z.B. `wert=abc`) enthält, gibt der Service den HTTP-Statuscode **400** zurück und bricht die Umrechnung ab.

* **Antwort Wahr:** Die Fehlerbehandlung mit `!is_numeric($wert)` verhindert die Berechnung mit ungültigen Daten.
* **Antwort Falsch (Korrekturhinweis):** Prüfen Sie den Codeblock unter **2. Prüfen auf gültigen Wert**. Bei nicht-numerischer Eingabe muss die Funktion `sendError(400, "Der Parameter 'wert' muss numerisch sein.")` aufgerufen werden.

**Frage 7: Umgang mit ungültigen Einheiten**

Der Service akzeptiert die Einheit **robust** auch in Großbuchstaben (z.B. `FAHRENHEIT`) und gibt bei einer unbekannten Einheit (z.B. `kelvin`) den HTTP-Statuscode **400** zurück.

* **Antwort Wahr:** Die Verwendung von `strtolower($_GET['einheit'])` gewährleistet Robustheit bei der Eingabe, und die abschließende `if`-Prüfung fängt unbekannte Einheiten ab.
* **Antwort Falsch (Korrekturhinweis):** Prüfen Sie den Codeblock unter **3. Prüfen auf gültige Einheit**. Stellen Sie sicher, dass die Einheit vor der Prüfung in Kleinbuchstaben konvertiert wird, und dass unbekannte Einheiten korrekt zu `sendError(400, "Ungültiger Wert...")` führen.

---

### Lizenz
Dieses Werk ist lizenziert unter der **Creative Commons - Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz**.
 
[Zum Lizenztext auf der Creative Commons Webseite](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)
