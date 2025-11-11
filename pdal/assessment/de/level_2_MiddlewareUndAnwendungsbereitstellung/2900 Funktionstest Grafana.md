---
title: "Fragen zur Grafana-Installation"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "uwe.bachmann@jade-hs.de"
organization: "PDAL-Projekt"
date: "2025-11-07"
version: "1.0.0"
level: "Ebene 2, Lerneinheit 2.8, Assessment"
duration: "0,2 Std"
prerequisites: ["Abgeschlossen - 2900 Grafana in einem LXC-Container installieren"]
tags: ["PDAL","Assessment", "Grafana", "Funktionsprüfung"]
license: "CC BY-SA 4.0"
---

## 🛠️ Funktionstest: Fragen zur Grafana-Installation

**Grafana-Repository einbinden**
Das Grafana-Repository ist erfolgreich eingebunden (Abschnitt 5). Nach `sudo apt update` wurde in der Konsole eine Zeile angezeigt, die auf das Grafana-Repository hinweist (z.B. "Hit:X https://apt.grafana.com stable InRelease").
 - **True:** 
    --  **Hinweis:** Dies bestätigt, dass die moderne GPG-Key-Verwaltung erfolgreich war und das Repository erkannt wird. 
- **False:**
    -- **Hinweis:** Überprüfen Sie die Befehle in Sektion 5. Wahrscheinlich wurde die Datei `/etc/apt/sources.list.d/grafana.list` nicht korrekt erstellt.

**Dienst einrichten**
Der Grafana-Dienst ist erfolgreich gestartet (Abschnitt 7). Die Abfrage `sudo systemctl status grafana-server` zeigte den Dienst als **`active (running)`** und **`enabled`** an.
- **True:**
    -- **Hinweis:** Der Dienst läuft und wird beim nächsten Neustart des Containers automatisch gestartet. 
- **False:** 
    -- **Hinweis:** Führen Sie `sudo systemctl enable grafana-server` und danach `sudo systemctl start grafana-server` erneut aus. 

**Web Connection testen**
Der initiale Zugriff über HTTP funktioniert (Abschnitt 8).** Der Browser konnte die Grafana-Login-Seite über `http://<IP-Adresse>:3000` erreichen und forderte zur Eingabe von Benutzername und Passwort auf.
- **True:** Die Anmeldeseite wurde korrekt geladen.
    -- **Hinweis:** Dies bestätigt, dass Grafana läuft und das Netzwerk im Container korrekt konfiguriert ist.
- **False:** 
    -- **Hinweis:**  Überprüfen Sie den Dienst-Status und stellen Sie sicher, dass Sie die korrekte IP-Adresse und den Port **3000** verwenden.

**Erster Login**
Admin-Passwort wurde gesichert (Nach Abschnitt 8). Nach dem initialen Login mit `admin`/`admin` wurde das Passwort erfolgreich geändert und ein erneuter Login mit dem neuen Passwort war erfolgreich.
- **True:** 
    -- **Hinweis:** Dies bestätigt, dass die Datenbank-Initialisierung und die grundlegende Benutzerverwaltung funktionieren. 
- **False:** 
    -- **Hinweis:** Löschen Sie Browser-Cookies/Cache und wiederholen Sie den initialen Login-Prozess mit dem Standardpasswort, um sicherzustellen, dass die Änderung korrekt gespeichert wird.

**TLS einrichten**
Der sichere Zugriff funktioniert (Abschnitt 9.5). Die Grafana-Weboberfläche ist über `https://<IP-Adresse>` erreichbar und der Browser zeigt **keine Zertifikatswarnung** an (vorausgesetzt die interne CA ist auf dem Client eingebunden).
- **True:** 
    -- **Hinweis:** Dies ist das Endziel der Absicherung: Der Dienst ist über TLS erreichbar, und das Zertifikat wird vom Client als vertrauenswürdig eingestuft. 
- **False:**  Es wurde eine Zertifikatswarnung angezeigt, oder die Seite war nicht über HTTPS erreichbar. 
    -- **Hinweis:** Stellen Sie sicher, dass Sie `sudo systemctl restart grafana-server` ausgeführt haben und die interne CA auf dem Client-PC korrekt installiert ist (Abschnitt 9.6).

---

## Lizenz

Dieses Werk ist lizenziert unter der **Creative Commons Namensnennung - Nicht-kommerziell - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz**.

[Zum Lizenztext auf der Creative Commons Webseite](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.de)

