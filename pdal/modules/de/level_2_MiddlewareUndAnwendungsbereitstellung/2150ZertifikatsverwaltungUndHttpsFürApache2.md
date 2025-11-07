---
title: "Zertifikatsverwaltung und HTTPS für Apache2"
author: ["Gudenkauf, Prof Stefan", "Uwe, Bachmann", "Ronald, Kalk"]
mail: "uwe.bachmann@jade-hs.de"
organization: "z.B. PDAL-Projekt, Jade Hochschule"
date: "2025-10-10"
version: "1.0.0"
level: "Ebene 2, Lerneinheit 2.1.5"
duration: "Geschätzte Dauer (z.B. 4-6 Stunden)"
prerequisites: ["Abgeschlossen - 2100 - Apache2-Webserver & Benutzerverwaltung im LXC-Container", "Abgeschlossen - 2050 - Erstellung einer eigenen CA (Certificate Authority) und manuelle Verteilung der Zertifikate"]
tags: ["Proxmox", "Linux", "Virtualisierung", "Apache2 Webserver", "Zertifikataverwaltung"]
license: "CC BY-NC-SA 4.0"
---

# Zertifikatsverwaltung und HTTPS für Apache2

## 1. Einleitung

Diese Dokumentation behandelt die Grundlagen und praktische Umsetzung der **Zertifikatsverwaltung und HTTPS-Konfiguration** für den Apache2-Webserver unter Linux. Sie richtet sich an **Studierende und Lehrende**, die sich mit Websicherheit, Verschlüsselung und Zertifikatsinfrastruktur vertraut machen möchten.

Ziel ist es, eine eigene **Certificate Authority (CA)** zu erstellen, Zertifikate für Server zu signieren und diese Zertifikate zur Absicherung der Kommunikation zwischen Client und Server (HTTPS) einzusetzen.

---

## 2. Grundlagen

**Einleitung:**

Bevor wir mit der praktischen Umsetzung beginnen, ist es wichtig zu verstehen, **warum Zertifikate** und **HTTPS** notwendig sind. In diesem Kapitel werden die theoretischen Grundlagen erklärt, die für das Verständnis der weiteren Schritte notwendig sind.

### 2.1 Was ist HTTPS?

**HTTPS (Hypertext Transfer Protocol Secure)** ist die verschlüsselte Variante von HTTP. Es verwendet **TLS (Transport Layer Security)**, um Daten zwischen Client (z. B. Browser) und Server vertraulich und integritätsgesichert zu übertragen.

### 2.2 Was sind Zertifikate?

Ein **Zertifikat** ist eine digitale Bescheinigung, die bestätigt, dass ein öffentlicher Schlüssel zu einer bestimmten Identität gehört. Zertifikate enthalten:

* Den öffentlichen Schlüssel
* Informationen über den Besitzer (z. B. Domainname)
* Die ausstellende Stelle (CA)
* Gültigkeitszeitraum
* Signatur der CA

### 2.3 Die Rolle der Certificate Authority (CA)

Eine **CA** ist eine vertrauenswürdige Instanz, die Zertifikate ausstellt und signiert. Es gibt:

* **Öffentliche CAs** (z. B. Let's Encrypt, DigiCert)
* **Private / eigene CAs**, die für interne Netzwerke verwendet werden

In dieser Anleitung wird eine **eigene CA** verwendet, um die Zertifikatserstellung und -prüfung vollständig zu verstehen.

---

## 3. Einrichtung einer eigenen Certificate Authority (CA)

**Einleitung:**

Damit wir unsere eigenen Zertifikate ausstellen können, benötigen wir eine **eigene Zertifizierungsstelle (CA)**. Diese CA ist der zentrale Punkt der Vertrauenskette – sie signiert Serverzertifikate und stellt damit sicher, dass die Identität eines Servers überprüfbar ist.

Dies wird genauer im Dokument [[2050 CA-sslmitSANZertifikat]] beschrieben.

---

## 4. Serverzertifikat erstellen

**Einleitung:**

In diesem Kapitel erstellen wir ein Zertifikat für unseren Apache2-Webserver auf unserem bereits erstellten CA LXC. Dieses Zertifikat wird von unserer CA signiert und ermöglicht eine sichere HTTPS-Verbindung in unserem lokalen Netzwerk.

Die einzelnen Schritte die hierzu notwendig sind werden im Dokument [[2050 CA-sslmitSANZertifikat]] genauer beschrieben.

---

Wechseln Sie nun zu CA-LXC:

### 4.1 Schlüssel für den Apache2-Server generieren

```bash
sudo openssl genrsa -out /etc/ssl/private/apache.key.pem 2048
sudo chmod 400 /etc/ssl/private/apache.key.pem
```

Dies ist der **private Schlüssel** des Webservers – er muss geheim bleiben und wird später in der Apache2-Konfiguration verwendet.

### 4.2 Certificate Signing Request (CSR) erstellen

```bash
sudo openssl req -new -key /etc/ssl/private/apache.key.pem \
  -out /etc/ssl/apache.csr.pem \
  -subj "/C=DE/ST=Niedersachsen/L=Wilhelmshaven/O=Hochschule/OU=IT/CN=webserver.local"
```

Ein **CSR**(Certificate Signing Request) ist eine Anfrage an die CA, ein Zertifikat zu signieren. Er enthält die Identitätsinformationen und den öffentlichen Schlüssel.

### 4.3 Zertifikat mit der eigenen CA signieren

```bash
sudo openssl x509 -req -in /etc/ssl/apache.csr.pem \
  -CA ~/myCA/certs/ca.cert.pem -CAkey ~/myCA/private/ca.key.pem \
  -CAcreateserial -out ~/myCA/certs/apache.cert.pem -days 825 -sha256
```

Hier signiert unsere CA den CSR und erstellt ein **gültiges Serverzertifikat**.

### 4.4 Prüfung des Serverzertifikats

```bash
openssl x509 -in /etc/ssl/certs/apache.cert.pem -text -noout
```

Damit lässt sich das Zertifikat auf Richtigkeit prüfen.

### 4.5 Kopieren der Zertifikate und des Server Schlüssels

### 4.5 Kopieren der Zertifikate und des Server-Schlüssels

Die für Apache benötigten Zertifikate und der zugehörige private Schlüssel müssen in die entsprechenden Verzeichnisse kopiert werden:

```bash
sudo cp /root/ca/private/apache.key.pem /etc/ssl/private/
sudo cp /root/ca/certs/apache.cert.pem /etc/ssl/certs/
sudo cp /root/ca/certs/ca.cert.pem /etc/ssl/myCA/certs/
```

Achte darauf, dass die Dateirechte korrekt gesetzt sind, damit nur der Benutzer `root` Zugriff auf den privaten Schlüssel hat:

```bash
sudo chmod 600 /etc/ssl/private/apache.key.pem
```

Weitere Details zur Erstellung und Struktur der Zertifikate findest du im Dokument
👉 **[[2050 CA-sslmitSANZertifikat]]**.

---

## 5. Apache2 für HTTPS konfigurieren

**Einleitung:**

Nachdem das Zertifikat erstellt wurde, müssen wir den Apache2-Webserver so konfigurieren, dass er HTTPS-Verbindungen akzeptiert und die erstellten Zertifikate verwendet.
Wir nutzen die **globalen Apache-Konfigurationen** für die Standardports **80** und **443**.

---

### 5.1 SSL-Modul aktivieren

Das SSL-Modul ist notwendig, damit Apache2 HTTPS-Verbindungen unterstützen kann.

```bash
sudo a2enmod ssl
sudo systemctl restart apache2
```

---

### 5.2 Globale HTTP-Konfiguration (Port 80)

Bearbeite die Datei `/etc/apache2/ports.conf` und stelle sicher, dass folgender Eintrag vorhanden ist:

```bash
Listen 80
```

Bearbeite dann die Standardkonfiguration `/etc/apache2/sites-available/000-default.conf` und stelle sicher, dass die HTTP-Einstellungen korrekt gesetzt sind:

* Die Email des Serveradmins eintragen.
* ggfs das DocumentRoot anpassen.
* ggfs die `.` vor dem `<VirtualHost>` und `</VirtualHost>` entfernen.

```bash
<VirtualHost *:80>
    ServerAdmin admin@webserver.local
    DocumentRoot /var/www/html

    <Directory /var/www/html>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

Diese Konfiguration stellt sicher, dass Apache auf Port 80 lauscht und den Standard-Webinhalt ausliefert.

---

### 5.3 Globale HTTPS-Konfiguration (Port 443)

Bearbeite die Datei `/etc/apache2/ports.conf` und stelle sicher, dass folgender Eintrag vorhanden ist:

```bash
Listen 443
```

Anschließend wird die Standard-SSL-Konfiguration angepasst. Bearbeite dazu `/etc/apache2/sites-available/default-ssl.conf`:

* die Punkte vor dem `.<VirtualHost>` und dem `.</VirtualHost>` müssen entfernt werden.
* Die Zertifikatspfade hinzufügen bzw anpassen.
* Die Email des Serveradmins eintragen.
* ggfs das DocumentRoot anpassen.

```bash
<VirtualHost *:443>
    ServerAdmin admin@webserver.local
    DocumentRoot /var/www/html

    SSLEngine on
    SSLCertificateFile /etc/ssl/certs/apache.cert.pem
    SSLCertificateKeyFile /etc/ssl/private/apache.key.pem
    SSLCACertificateFile /etc/ssl/myCA/certs/ca.cert.pem

    <Directory /var/www/html>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

Diese Konfiguration aktiviert HTTPS auf Port 443 und bindet die erstellten Zertifikate ein.

---

### 5.4 Konfiguration aktivieren und Apache neu laden

Damit die vorgenommenen Änderungen wirksam werden, müssen wir die Konfiguration aktivieren und den Apache Server neu laden.

```bash
sudo a2ensite default-ssl.conf
sudo systemctl reload apache2
```

Damit ist der HTTPS-Betrieb aktiv.

---

### 5.5 Test der HTTPS-Verbindung

Rufe im Browser die Adresse deines Servers auf:

```bash
https://<IP-des-Webservers>
```

Falls der Browser eine Sicherheitswarnung anzeigt, importiere das CA-Zertifikat deiner eigenen Zertifizierungsstelle in den Browser oder das Betriebssystem.

---

### Wichtiger Hinweis zu produktiven Umgebungen

In produktiven Systemen sollte **immer mit VirtualHosts gearbeitet werden**. Dadurch lassen sich mehrere Webseiten oder Dienste auf demselben Server unabhängig voneinander betreiben, mit jeweils eigenen Konfigurationen, Domains und Zertifikaten. Ein weiterer wichtiger Grund für die Nutzung von VirtualHosts ist die **Verknappung von IPv4-Adressen**. Da nicht jede Website eine eigene IP-Adresse erhalten kann, wurde das Konzept der **Name-Based VirtualHosts** entwickelt. Hierbei teilt sich eine Vielzahl von Domains dieselbe IP-Adresse, während der Hostname vom Client im HTTP-Header übermittelt wird. Apache kann so anhand des Hostnamens die passende Konfiguration und Website ausliefern.

Dank moderner Technologien wie **SNI (Server Name Indication)** ist es heute zudem möglich, auch **mehrere HTTPS-Websites auf einer IP-Adresse** zu betreiben, da der gewünschte Hostname bereits während des TLS-Handshakes übermittelt wird. Ohne diese Funktion wäre der gleichzeitige Betrieb mehrerer SSL-Zertifikate auf einer IP-Adresse nicht praktikabel.

Ohne VirtualHosts ist es nur möglich, **eine globale Standardkonfiguration** für alle Anfragen auf Port 80 und 443 zu verwenden. Das bedeutet, dass nur **ein einziges Zertifikat** für alle Domains genutzt werden kann, was für produktive Umgebungen in der Regel **nicht praktikabel** ist.

Mit VirtualHosts hingegen kann jede Website ihr **eigenes SSL-Zertifikat** verwenden, was sowohl aus Sicherheits- als auch aus organisatorischen Gründen die empfohlene Vorgehensweise ist.

Darüber hinaus bieten VirtualHosts eine Reihe weiterer Vorteile:

* **Bessere Trennung und Organisation:** Jede Domain oder Subdomain kann ihre eigene Konfigurationsdatei, Fehlerseiten, Logs und Zugriffsbeschränkungen besitzen.
* **Flexibilität bei Technologien:** Unterschiedliche VirtualHosts können verschiedene PHP-Versionen, Proxy-Ziele oder Backends nutzen (z. B. für getrennte Entwicklungs- und Produktionsumgebungen).
* **Sicherheitsvorteile:** Durch getrennte Kontexte lassen sich Berechtigungen, Verzeichnisse und Module gezielt einschränken.
* **Skalierbarkeit:** Neue Domains oder Dienste lassen sich einfach hinzufügen, ohne bestehende Konfigurationen zu verändern.
* **Bessere Wartbarkeit:** Änderungen an einer Website wirken sich nicht auf andere VirtualHosts aus, was Fehlkonfigurationen reduziert.

Kurz gesagt: VirtualHosts sind heute ein **Best Practice** für alle Webserver, da sie Ordnung, Sicherheit, Flexibilität und eine effiziente Nutzung der knappen IPv4-Ressourcen ermöglichen und gleichzeitig durch SNI die sichere Nutzung von HTTPS auf einer gemeinsamen IP-Adresse unterstützen.

---

## 6. CA-Zertifikat verteilen

**Einleitung:**

Damit Clients dem Serverzertifikat vertrauen, müssen sie auch der ausstellenden CA vertrauen. In diesem Kapitel zeigen wir, wie man das CA-Zertifikat auf verschiedenen Systemen importiert.

Wer das [[2050 CA-sslmitSANZertifikat]] Dokument bereits bearbeitet hat, hat diesen Schritt bereits erledigt.

### 6.1 Unter Linux

```bash
sudo cp /etc/ssl/myCA/certs/ca.cert.pem /usr/local/share/ca-certificates/myCA.crt
sudo update-ca-certificates
```

### 6.2 Unter Windows

* Öffne `certmgr.msc`
* Importiere `ca.cert.pem` unter **Vertrauenswürdige Stammzertifizierungsstellen**

### 6.3 Unter macOS

* Öffne „Schlüsselbundverwaltung“
* Importiere `ca.cert.pem` und markiere es als **immer vertrauen**

---

## 7. Optional: Serverzertifikate mit Subject Alternative Names (SAN)

Wenn ein Server unter mehreren Namen (z. B. `webserver.local`, `apache.local`) erreichbar ist, muss das Zertifikat diese Namen über **Subject Alternative Names (SAN)** abdecken.

>**Hinweis!**
Wie man eine SAN-Liste erstellt wird im Dokument [[2050 CA-sslmitSANZertifikat]] bereits behandelt.

---

## 8. Fehlersuche und Tipps

**Einleitung:**

In diesem Abschnitt werden häufige Fehler und deren Lösungen beschrieben, um typische Probleme bei der Zertifikatsverwaltung und Apache2-Konfiguration zu beheben.

| Problem                                  | Mögliche Ursache                | Lösung                                                     |
| ---------------------------------------- | ------------------------------- | ---------------------------------------------------------- |
| Browser meldet "Verbindung nicht sicher" | CA-Zertifikat nicht importiert  | Importiere die CA in den Browser                           |
| Apache startet nicht                     | Fehler in der SSL-Konfiguration | `sudo apachectl configtest` ausführen                      |
| Falsches Zertifikat geladen              | Pfad oder Name falsch           | Überprüfe `SSLCertificateFile` und `SSLCertificateKeyFile` |

---

## 9. Zusammenfassung

**Einleitung:**

In der Zusammenfassung werden die wichtigsten Punkte der gesamten Dokumentation noch einmal wiederholt.

Diese Anleitung zeigte:

* Erstellung und Signierung von Serverzertifikaten
* Integration in Apache2 für HTTPS
* Verteilung und Vertrauen von Zertifikaten auf Clients

Damit ist eine vollständig abgesicherte HTTPS-Kommunikation in einer kontrollierten Umgebung (z. B. Schulnetz, Labor oder Unternehmen) möglich.

---

## 10. Weiterführende Themen

**Einleitung:**

Für fortgeschrittene Nutzer gibt es viele Möglichkeiten, die hier erlernten Konzepte zu erweitern oder zu automatisieren.

* Automatisierte Zertifikatserneuerung (z. B. mit Skripten)
* Integration von Client-Zertifikaten zur Authentifizierung
* Verwendung von Intermediate CAs
* TLS-Härtung in Apache2 (Cipher Suites, Protokolle, HSTS)

---

## 11. Alternative Wege der Zertifikatsverwaltung

**Einleitung:**

Neben einer eigenen CA gibt es auch andere Methoden, Zertifikate zu erstellen und zu verwalten. Diese unterscheiden sich in Aufwand, Vertrauen, Kosten und Automatisierung.

### 11.1 Öffentliche Zertifizierungsstellen

Öffentliche CAs (z. B. DigiCert, Sectigo) stellen Zertifikate aus, die automatisch von allen gängigen Browsern und Betriebssystemen vertraut werden. Sie sind ideal für produktive Websites, aber kostenpflichtig.

### 11.2 Let's Encrypt

**Let's Encrypt** ist eine kostenlose, automatisierte und öffentliche CA. Sie ermöglicht über Tools wie **Certbot** eine einfache Einrichtung und automatische Erneuerung von Zertifikaten. Allerdings ist sie nur für öffentliche Domains geeignet (nicht für interne Netzwerke ohne DNS-Auflösung).

### 11.3 Self-Signed Zertifikate ohne CA

Ein **selbstsigniertes Zertifikat** wird direkt vom Server erzeugt, ohne eine CA. Es bietet Verschlüsselung, aber kein Vertrauen – Browser zeigen daher eine Warnung an. Diese Methode eignet sich nur für Tests oder Entwicklungsumgebungen.

---

### Fazit

Eine eigene CA bietet maximale Kontrolle und eignet sich hervorragend für **interne Netzwerke** oder **Lehrumgebungen**. Für **öffentliche Websites** sind jedoch **Let's Encrypt** oder kommerzielle CAs die bevorzugte Lösung, da sie automatisch vertraut werden und den Wartungsaufwand minimieren.

## Quellen

* „Documentation“. Zugegriffen: 10. Oktober 2025. [Online]. Verfügbar unter: [Let's Encrypt Doc](https://letsencrypt.org/docs/)
* „Getting Started“. Zugegriffen: 10. Oktober 2025. [Online]. Verfügbar unter: [Let's Encrypt Getting Started](https://letsencrypt.org/getting-started/)
* „How to setup your own CA with OpenSSL“, Gist. Zugegriffen: 10. Oktober 2025. [Online]. Verfügbar unter: [How to setup your own CA with OpenSSL](https://gist.github.com/soarez/9688998)
* „Install an SSL Certificate on Apache Mod_SSL“, SSL.com. Zugegriffen: 10. Oktober 2025. [Online]. Verfügbar unter: [Install SSL Certificate](https://www.ssl.com/how-to/install-ssl-apache-mod-ssl/)
* „mod_ssl - Apache HTTP Server Version 2.4“. Zugegriffen: 10. Oktober 2025. [Online]. Verfügbar unter: [SSL Modul Apache](https://httpd.apache.org/docs/2.4/mod/mod_ssl.html?utm_source=chatgpt.com)
* „openssl-ca - OpenSSL Documentation“. Zugegriffen: 10. Oktober 2025. [Online]. Verfügbar unter: [OpenSSL Doc](https://docs.openssl.org/3.0/man1/openssl-ca/?utm_source=chatgpt.com)
* L. Rendek, „Setting Up a Secure Apache Server on Ubuntu 24.04“, LinuxConfig. Zugegriffen: 10. Oktober 2025. [Online]. Verfügbar unter: [Secure Apache on Ubuntu](https://linuxconfig.org/setting-up-a-secure-apache-server-on-ubuntu-24-04)
* „SSL/TLS Strong Encryption: How-To - Apache HTTP Server Version 2.4“. Zugegriffen: 10. Oktober 2025. [Online]. Verfügbar unter: [SSL/TLS strong Encryption](https://httpd.apache.org/docs/2.4/ssl/ssl_howto.html?utm_source=chatgpt.com)

---

## Lizenz

Dieses Werk ist lizenziert unter der **Creative Commons Namensnennung - Nicht-kommerziell - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz**.

[Zum Lizenztext auf der Creative Commons Webseite](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.de)

