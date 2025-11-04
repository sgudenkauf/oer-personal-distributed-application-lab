---
title: "MQTT auf vorhandenem LXC installieren und konfigurieren"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "uwe.bachmann@jade-hs.de"
organization: "PDAL-Projekt"
date: "2025-10-07"
version: "1.0.0"
level: "Ebene 2, Lerneinheit 2.5.1 (Optional)"
duration: "2 Std."
prerequisites: ["Abgeschlossen - 2500 - MQTT auf vorhandenem LXC installieren und konfigurieren"]
tags: ["MQTT-Broker", "Mosquitto", "MQTT"]
license: "CC BY-SA 4.0"
---

# 🔐 MQTT mit TLS-Verschlüsselung & Zertifikats-Authentifizierung

Bisher senden wir die Daten an unseren MQTT-Broker unverschlüsselt. Auch versenden wir diese unverschlüsselt an die Subscriber.

Um die Daten verschlüsselt senden zu können, benötigen sowohl Server als auch Clients **Zertifikate**.

MQTT mit TLS-Verschlüsselung arbeitet auf dem Standard-Port **`8883`**.

Hier wird die Erstellung und Konfiguration von **Beispiel-Zertifikaten** auf dem Broker beschrieben.

## 1. Zertifikate erstellen und sichern (Broker)

**Wichtig:** Der private Schlüssel der Root-CA (`ca.key`) darf den Broker nach der Erstellung und Signierung der Server- und Client-Zertifikate **nicht auf dem System verbleiben**\!

```bash
# Wechsel in das Mosquitto-Zertifikatsverzeichnis
cd /etc/mosquitto/certs

# CA (Root-Zertifikat erstellen)
openssl genrsa -out ca.key 4096
openssl req -x509 -new -key ca.key -sha256 -days 1825 -out ca.crt -subj "/CN=MQTT-CA"

# Server-Zertifikat (Schlüssel und Request erstellen)
openssl genrsa -out server.key 4096
openssl req -new -key server.key -out server.csr -subj "/CN=192.168.137.150"
# Server-Zertifikat mit der CA signieren
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 825 -sha256
```

**Client-Zertifikat für Kai**

```bash
openssl genrsa -out Kai.key 4096
openssl req -new -key Kai.key -out Kai.csr -subj "/CN=Kai"
openssl x509 -req -in Kai.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out Kai.crt -days 825 -sha256
```

### 🔒 1.1. Dateiberechtigungen anpassen und CA-Schlüssel sichern

Dies sind kritische Schritte zur Gewährleistung der Sicherheit.

```bash
# 1. Sicherung des privaten CA-Schlüssels und Entfernung vom Broker-System
# ACHTUNG: Der private Schlüssel der CA darf nicht auf dem Broker verbleiben!
# Beispiel: Kopieren Sie die ca.key an einen sicheren Ort außerhalb des LXC.
# Wir löschen den Schlüssel hier, nachdem er zur Signierung genutzt wurde.
sudo rm ca.key
sudo rm server.csr Kai.csr # .csr Dateien werden nicht mehr benötigt

# 2. Server-Schlüssel (server.key) nur für den Dienst-Benutzer Mosquitto lesbar machen
sudo chmod 600 /etc/mosquitto/certs/server.key
sudo chown mosquitto:mosquitto /etc/mosquitto/certs/server.key

# 3. Server- und CA-Zertifikate für den Dienst-Benutzer lesbar machen
# Wir stellen sicher, dass alle .crt-Dateien dem Mosquitto-Benutzer gehören und lesbar sind.
sudo chmod 644 /etc/mosquitto/certs/*.crt
sudo chown mosquitto:mosquitto /etc/mosquitto/certs/*.crt
```

## 2. TLS-Listener in `mosquitto.conf` konfigurieren

Wir fügen einen dedizierten TLS-Listener auf Port `8883` hinzu, der **Client-Zertifikate zur Authentifizierung verlangt**.

```bash
sudo nano /etc/mosquitto/mosquitto.conf

# Ergänzen:

listener 8883
cafile /etc/mosquitto/certs/ca.crt
certfile /etc/mosquitto/certs/server.crt
keyfile /etc/mosquitto/certs/server.key

require_certificate true
use_identity_as_username true
```

**Erklärung der TLS-Einstellungen:**

  * **`listener 8883`**: Definiert den Port für verschlüsselte Verbindungen.
  * **`require_certificate true`**: Erzwingt die **Client-Zertifikats-Authentifizierung** (Mutual TLS, mTLS). Nur Clients mit einem von der CA signierten Zertifikat dürfen sich verbinden.
  * **`use_identity_as_username true`**: Verwendet den **Common Name (CN)** des Client-Zertifikats (hier: `Kai`) als MQTT-Benutzernamen. Dies ermöglicht die Kombination mit **ACLs** aus der vorherigen Lerneinheit.

## 3. Dienst neu starten und Verbindung testen

### 🔁 Dienst neu starten

```bash
sudo systemctl restart mosquitto
```

### 🧪 Verbindung testen (Clientseitig)

Zum Testen müssen die Client-Zertifikate (`ca.crt`, `Kai.crt`, `Kai.key`) auf den Rechner kopiert werden, von dem aus der Befehl abgesetzt wird. Hier testen wir der Einfachheit halber **direkt auf dem Broker-LXC**, da die Dateien dort noch vorhanden sind.

```bash
mosquitto_pub -h 192.168.137.150 -p 8883 \
--cafile /etc/mosquitto/certs/ca.crt \
--cert /etc/mosquitto/certs/Kai.crt \
--key /etc/mosquitto/certs/Kai.key \
-t Kai/logs -m "TLS & Authentifiziert"
```

Wenn dieser Befehl erfolgreich ist, wurde die TLS-Verschlüsselung mit Client-Authentifizierung korrekt eingerichtet.

-----

## 📌 Zusammenfassung: Verzeichnisstruktur

```
/etc/mosquitto/
├── certs/
│   ├── ca.crt        # Root-CA Zertifikat
│   ├── server.crt    # Server-Zertifikat
│   ├── server.key    # Server-Schlüssel (chmod 600, chown mosquitto)
│   ├── Kai.crt       # Client-Zertifikat (wird für Clients benötigt)
│   └── Kai.key       # Client-Schlüssel (wird für Clients benötigt)
├── passwords/ (optional)
│   └── mqtt_users
├── acl               # optional (für CN-basierte Zugriffskontrolle)
└── mosquitto.conf
```
>Hinweis: Wenn Kai von einem separaten Rechner (Client-PC, anderer LXC, Raspberry Pi usw.) arbeitet, müssen die Befehle zur Veröffentlichung von Nachrichten wie folgt angepasst werden:

Dateien kopieren: Sie müssen die drei Dateien (ca.crt, Kai.crt, Kai.key) von Ihrem Broker-LXC auf das Client-System kopieren und dort in ein Verzeichnis legen (z.B. /home/kai/mqtt-certs/).

Pfad anpassen: Die Pfadangaben im mosquitto_pub-Befehl müssen auf die lokalen Pfade des Client-Systems zeigen:

```bash
# Auf dem Client-System ausführen:
mosquitto_pub -h 192.168.137.150 -p 8883 \
--cafile /home/kai/mqtt-certs/ca.crt \
--cert /home/kai/mqtt-certs/Kai.crt \
--key /home/kai/mqtt-certs/Kai.key \
-t Kai/logs -m "Hallo von extern"
```
Ohne diese Dateien (insbesondere den privaten Schlüssel) kann der Client die verschlüsselte Verbindung nicht aufbauen oder sich nicht gegenüber dem Broker authentifizieren.

---

Neben der Erstellung der Zertifikate und dem Testen der Verbindung auf der Konsole müssen Sie sich für automatisierte Scripte noch mit den entsprechenden **Client-Bibliotheken** beschäftigen – z. B. Paho-MQTT. Die Integration von Zertifikaten in diese Bibliotheken ist **nicht trivial**.

-----

## Quellen

  - „client module — Eclipse paho-mqtt documentation“. Zugegriffen 9. Juli 2025. [https://eclipse.dev/paho/files/paho.mqtt.python/html/client.html](https://eclipse.dev/paho/files/paho.mqtt.python/html/client.html).
  - Destuynder (:kang), Guillaume. „Getcap, Setcap and File Capabilities“. kang’s things & stuff, 17. Dezember 2013. [https://www.insecure.ws/2013/12/17/getcap-setcap.html](https://www.insecure.ws/2013/12/17/getcap-setcap.html).
  - Docile, Egidio. „Introduction to Linux Capabilities“. LinuxConfig (blog), 1. November 2023. [https://linuxconfig.org/introduction-to-linux-capabilities](https://linuxconfig.org/introduction-to-linux-capabilities).
  - Inc, EMQ Technologies. „MQTT Guide 2025: Beginner to Advanced“. [www.emqx.com](https://www.emqx.com). Zugegriffen 9. Juli 2025. [https://www.emqx.com/en/mqtt-guide](https://www.emqx.com/en/mqtt-guide).
  - Kerrisk, Michael. The Linux Programming Interface: A Linux Und UNIX System Programming Handbook. Ninth printing. San Francisco, CA: No Starch Press, 2018.
  - „Linux Capabilities: Setting and Modifying Permissions | Baeldung on Linux“, 26. Oktober 2023. [https://www.baeldung.com/linux/set-modify-capability-permissions](https://www.baeldung.com/linux/set-modify-capability-permissions).
  - Nordquist, Thomas. „MQTT Explorer“. MQTT Explorer. Zugegriffen 8. Juli 2025. [http://mqtt-explorer.com/](http://mqtt-explorer.com/).

-----

### Lizenz
Dieses Werk ist lizenziert unter der **Creative Commons - Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz**.
 
[Zum Lizenztext auf der Creative Commons Webseite](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)
