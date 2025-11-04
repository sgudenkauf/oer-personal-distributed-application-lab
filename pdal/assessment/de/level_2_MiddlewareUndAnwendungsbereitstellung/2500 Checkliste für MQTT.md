---
title: "Checkliste zur Überprüfung des REST-Service"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "uwe.bachmann@jade-hs.de"
organization: "PDAL-Projekt"
date: "2025-09-25"
version: "1.0.0"
level: "Ebene 2, Lerneinheit 2.3, Assessment"
duration: "0,2 Std"
prerequisites:["Abgeschlossen - 2500 MQTT auf vorhandenem LXC installieren und konfigurieren"]
tags: ["PDAL","Assessment"]
license: "CC BY-SA 4.0"
---

# ✅ Checkliste zur Überprüfung der MQTT-Funktionalität (Implementierungsprüfung)

Diese Fragen dienen als Ja-/Nein-Prüfung, ob die Installations- und Konfigurationsschritte gemäß der Dokumentation erfolgreich waren.

### Basiskonfiguration und Installation

**Installation und Aktivierung erfolgreich**

Wurden die Pakete **`mosquitto`** und **`mosquitto-clients`** erfolgreich installiert und konnte der Dienst `mosquitto` aktiviert (`enable`) und gestartet (`start`) werden?

* **Ja (Hinweis zur erfolgreichen Bearbeitung):** Die Befehle `sudo apt install -y mosquitto mosquitto-clients` und `sudo systemctl start mosquitto` wurden erfolgreich und fehlerfrei ausgeführt.
* **Nein (Hinweis zur Korrektur):** Prüfen Sie die Internetverbindung des LXC-Containers und führen Sie **`sudo apt update`** vor der Installation durch. Starten Sie den Dienst (`sudo systemctl start mosquitto`) erneut.

**Dienststatus korrekt**

Zeigt der Befehl **`sudo systemctl status mosquitto`**, dass der Dienst **läuft** (`active (running)`) und für den automatischen Start konfiguriert ist (`enabled`)?

* **Ja (Hinweis zur erfolgreichen Bearbeitung):** Die Ausgabe des Status zeigt **`active (running)`** in grüner Schrift und **`enabled`** in der Zeile "Loaded".
* **Nein (Hinweis zur Korrektur):** Verwenden Sie **`sudo systemctl enable mosquitto`** zur Aktivierung und **`sudo systemctl restart mosquitto`** zum erneuten Starten des Dienstes.

***

### Anonyme Kommunikation (Phase 1)

**Anonyme Konfiguration abgeschlossen**

Wurde die Konfigurationsdatei **`/etc/mosquitto/mosquitto.conf`** so angepasst, dass **`listener 1883`** und **`allow_anonymous true`** gesetzt sind, und wurde der Dienst danach neu gestartet?

* **Ja (Hinweis zur erfolgreichen Bearbeitung):** Die beiden Zeilen sind in der Konfigurationsdatei vorhanden und der Befehl **`sudo systemctl restart mosquitto`** wurde ausgeführt.
* **Nein (Hinweis zur Korrektur):** Bearbeiten Sie die Datei mit `sudo nano /etc/mosquitto/mosquitto.conf`, fügen die Zeilen hinzu und stellen Sie sicher, dass der Dienst neu gestartet wird, damit die Konfiguration übernommen wird.

**Host-Client-Test erfolgreich**

Konnte eine Nachricht vom Host des Brokers aus **gesendet (`mosquitto_pub`)** und erfolgreich **empfangen (`mosquitto_sub`)** werden (z.B. über Port 1883)?

* **Ja (Hinweis zur erfolgreichen Bearbeitung):** Der `mosquitto_sub`-Befehl zeigte die Nachricht ("Hallo MQTT") an, nachdem sie vom `mosquitto_pub`-Befehl gesendet wurde.
* **Nein (Hinweis zur Korrektur):** Überprüfen Sie, ob die IP-Adresse des Brokers im Befehl korrekt ist und ob der Broker läuft (siehe Frage "Dienststatus korrekt"). Testen Sie ggf. zuerst mit **`localhost`** anstelle der IP.

**MQTT-Explorer-Test erfolgreich**

Konnte der **MQTT-Explorer** erfolgreich und **ohne** Angabe von Benutzername/Passwort eine Verbindung zum Broker aufbauen und die Testnachrichten sehen?

* **Ja (Hinweis zur erfolgreichen Bearbeitung):** Der MQTT-Explorer zeigte den Verbindungsstatus als **"Connected"** und listete das `test/topic` auf.
* **Nein (Hinweis zur Korrektur):** Prüfen Sie die IP-Adresse und den **Port (1883)** in den Verbindungseinstellungen des MQTT-Explorers. Stellen Sie sicher, dass keine Firewall die Verbindung blockiert.

***

### Passwortgeschützte Kommunikation (Phase 2)

**Benutzeranlage erfolgreich**

Wurde mindestens ein Benutzer (**`pdal` oder `Kai`**) mithilfe von **`sudo mosquitto_passwd`** erstellt und in der Datei `/etc/mosquitto/passwords/mqtt_users` gespeichert?

* **Ja (Hinweis zur erfolgreichen Bearbeitung):** Die Datei **`mqtt_users`** existiert und enthält den verschlüsselten Benutzernamen und das Passwort.
* **Nein (Hinweis zur Korrektur):** Führen Sie den Befehl `sudo mosquitto_passwd -c /etc/mosquitto/passwords/mqtt_users pdal` (oder `Kai`) erneut aus und vergeben Sie das Passwort.

**Authentifizierter Client-Test erfolgreich**

Konnte eine Nachricht mit dem **`mosquitto_pub`**-Befehl nur durch Angabe von **Benutzer (`-u`)** und **Passwort (`-P`)** erfolgreich veröffentlicht werden?

* **Ja (Hinweis zur erfolgreichen Bearbeitung):** Der Befehl funktionierte mit **Benutzer/Passwort** und schlug **ohne** diese Parameter fehl (nachdem `allow_anonymous false` gesetzt wurde).
* **Nein (Hinweis zur Korrektur):** Prüfen Sie die korrekte Schreibweise von Benutzername und Passwort. Vergewissern Sie sich, dass **`allow_anonymous false`** in der `mosquitto.conf` gesetzt und der Dienst neu gestartet wurde.

***

### Zugriffskontrolle (Phase 3: ACLs)

**ACL-Datei erstellt und konfiguriert**

Wurde die ACL-Datei **`/etc/mosquitto/acl`** mit mindestens einer **`user`** und den zugehörigen **`topic`** Berechtigungen (`read`, `write` oder `readwrite`) erstellt und in der **`mosquitto.conf`** referenziert?

* **Ja (Hinweis zur erfolgreichen Bearbeitung):** Die Datei `/etc/mosquitto/acl` existiert mit Inhalt und die Zeile **`acl_file /etc/mosquitto/acl`** wurde in die `mosquitto.conf` aufgenommen.
* **Nein (Hinweis zur Korrektur):** Erstellen Sie die Datei mit `nano /etc/mosquitto/acl` und fügen Sie das Beispiel aus der Dokumentation ein. Bearbeiten Sie anschließend die `mosquitto.conf`.

**Leseberechtigung getestet**

Führt der Versuch, ein Topic zu abonnieren, für das der Benutzer **keine `read`-Berechtigung** hat, dazu, dass der Subscriber **keine Nachrichten** empfängt?

* **Ja (Hinweis zur erfolgreichen Bearbeitung):** Ein Test-Client, der kein Leserecht für ein bestimmtes Topic hat, empfängt keine Nachrichten, während ein Client mit Leserecht dies tut (z.B. User "Kai" versucht, das Topic `pdal/#` zu lesen, was fehlschlägt).
* **Nein (Hinweis zur Korrektur):** Überprüfen Sie die Syntax der **`topic read`** Zeile in der ACL-Datei. Möglicherweise erlaubt eine Wildcard-Regel (z.B. `#` oder `+`) den Zugriff ungewollt.

---

### Lizenz
Dieses Werk ist lizenziert unter der **Creative Commons - Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz**.
 
[Zum Lizenztext auf der Creative Commons Webseite](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)