---
title: "Fragen zu Zertifikaten und einer eigenen CA"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "uwe.bachmann@jade-hs.de"
organization: "PDAL-Projekt"
date: "2025-09-24"
version: "1.0.0"
level: "Ebene 2, Lerneinheit 1.05, Assessment"
duration: "0,2 Std"
prerequisites: ["Abgeschlossen -  Dokument: 2050 - Erstellung einer eigenen CA (Certificate Authority) und manuelle Verteilung der Zertifikate"]
tags: ["PDAL","Assessment"]
license: "CC BY-SA 4.0"
---

### 10 Fragen zu Zertifikaten und einer eigenen CA

1.  **Warum werden Zertifikate auch in einem geschlossenen internen Netzwerk benötigt?**
    * A) Sie sind gesetzlich vorgeschrieben, um Daten zu speichern.
        * *Erklärung*: Dies ist falsch. Der Einsatz von Zertifikaten ist keine generelle gesetzliche Vorschrift, sondern dient der Sicherheit und Vertrauenswürdigkeit.
    * B) Öffentliche Zertifizierungsstellen (CAs) können Zertifikate für interne Systeme ausstellen.
        * *Erklärung*: Dies ist falsch. Öffentliche CAs haben keinen Zugriff auf interne Netzwerke und können daher keine Zertifikate für interne Dienste ausstellen.
    * C) Externe Firewalls benötigen sie für die Paketfilterung.
        * *Erklärung*: Dies ist falsch. Zertifikate werden für die Authentifizierung und Verschlüsselung von Datenverkehr verwendet, nicht für die grundlegende Paketfilterung durch Firewalls.
    * **D) Sie ermöglichen die verschlüsselte und authentifizierte Kommunikation zwischen internen Diensten.**
        * *Erklärung*: Dies ist korrekt. Zertifikate stellen sicher, dass die Kommunikation zwischen internen Diensten sicher und vertrauenswürdig abläuft.
    * E) Sie sind ausschließlich für die Identifizierung von Benutzern, nicht von Geräten.
        * *Erklärung*: Dies ist falsch. Zertifikate werden zur Identifizierung von Geräten, Diensten und Personen verwendet.

2.  **Welches Werkzeug wird in der Anleitung zur Erstellung der eigenen Certificate Authority (CA) verwendet?**
    * A) `certbot`
        * *Erklärung*: `Certbot` wird in der Regel verwendet, um Zertifikate von der öffentlichen Zertifizierungsstelle Let's Encrypt zu beziehen und zu verwalten.
    * B) `keytool`
        * *Erklärung*: `keytool` ist ein Werkzeug von Java, das zur Verwaltung von Schlüsselspeichern verwendet wird.
    * C) `gnupg`
        * *Erklärung*: `gnupg` (`Gnu Privacy Guard`) wird hauptsächlich für die Verschlüsselung und Signierung von E-Mails und Dateien verwendet.
    * **D) `OpenSSL`**
        * *Erklärung*: `OpenSSL` ist das Standard-Kommandozeilen-Tool, das in dieser Anleitung für die Erstellung von Zertifikaten und einer CA verwendet wird.
    * E) `ssh-keygen`
        * *Erklärung*: `ssh-keygen` wird verwendet, um SSH-Schlüsselpaare für die sichere Anmeldung an Servern zu erstellen.

3.  **Was ist der Hauptvorteil eines einzigen SAN-Zertifikats im Vergleich zu mehreren einzelnen Zertifikaten für jeden Dienst?**
    * **A) Es vereinfacht die Verwaltung, da nur eine einzige Zertifikatsdatei für alle Dienste benötigt wird.**
        * *Erklärung*: Dies ist korrekt. Ein SAN-Zertifikat sichert mehrere Domains und IPs ab, was den Verwaltungsaufwand in kleinen Umgebungen minimiert.
    * B) Es bietet eine höhere Sicherheit, da bei einer Kompromittierung nicht alle Dienste betroffen sind.
        * *Erklärung*: Dies ist falsch. Das Gegenteil ist der Fall: Bei Kompromittierung eines einzelnen SAN-Zertifikats sind alle gesicherten Dienste gefährdet.
    * C) Es beschleunigt die Netzwerkkommunikation.
        * *Erklärung*: Dies ist falsch. Die Art des Zertifikats hat keinen signifikanten Einfluss auf die Geschwindigkeit der Netzwerkkommunikation.
    * D) Es wird automatisch erneuert, ohne manuelles Zutun.
        * *Erklärung*: Dies ist falsch. Die Erneuerung eines selbst ausgestellten Zertifikats muss manuell oder durch Skripte vorgenommen werden.
    * E) Es ist für öffentliche Webseiten obligatorisch.
        * *Erklärung*: Dies ist falsch. Für öffentliche Webseiten werden Zertifikate von öffentlichen CAs wie Let's Encrypt oder DigiCert benötigt.

4.  **Welchen Zweck erfüllt die Datei `index.txt` in der CA-Struktur?**
    * A) Sie speichert die Passwörter aller ausgestellten Zertifikate.
        * *Erklärung*: Dies ist falsch. Passwörter sollten niemals unverschlüsselt in einer Datei gespeichert werden.
    * B) Sie enthält die Root-Zertifikate aller vertrauenswürdigen CAs.
        * *Erklärung*: Dies ist falsch. Die Datei wird von der eigenen CA erstellt und enthält keine externen Root-Zertifikate.
    * **C) Sie dient als Datenbank, in der OpenSSL die ausgestellten Zertifikate dokumentiert.**
        * *Erklärung*: Dies ist korrekt. OpenSSL verwendet diese Datei, um ausgestellte Zertifikate und deren Status zu verwalten.
    * D) Sie speichert temporäre Daten für die Schlüsselerzeugung.
        * *Erklärung*: Dies ist falsch. Die temporären Daten werden in der `RANDFILE` gespeichert.
    * E) Sie ist eine reine Log-Datei, die vom Administrator manuell gefüllt wird.
        * *Erklärung*: Dies ist falsch. Die Datei wird von OpenSSL automatisch aktualisiert und dient als Datenbank.

5.  **Was bedeutet `default_days = 3650` in der `openssl.cnf` Konfigurationsdatei?**
    * A) Die CA muss alle 3650 Tage erneuert werden.
        * *Erklärung*: Dies ist falsch. Dies ist die Standard-Gültigkeitsdauer für neue Zertifikate, nicht für die CA selbst.
    * B) Die Sperrliste (CRL) wird alle 3650 Tage aktualisiert.
        * *Erklärung*: Dies ist falsch. Die Gültigkeitsdauer der Sperrliste wird durch `default_crl_days` festgelegt.
    * C) Die maximale Schlüssellänge beträgt 3650 Bit.
        * *Erklärung*: Dies ist falsch. Die Schlüssellänge wird durch `default_bits` definiert.
    * **D) Die Gültigkeitsdauer eines neu ausgestellten Zertifikats beträgt 10 Jahre.**
        * *Erklärung*: Dies ist korrekt. 3650 Tage entsprechen 10 Jahren, was die Standard-Gültigkeitsdauer für neue Zertifikate ist.
    * E) Das Zertifikat wird nach 3650 Tagen automatisch widerrufen.
        * *Erklärung*: Dies ist falsch. Ein Widerruf erfolgt manuell.

6.  **Welche Eigenschaft in der `openssl.cnf` gibt an, dass ein Zertifikat als Zertifizierungsstelle fungieren darf?**
    * A) `keyUsage = keyCertSign`
        * *Erklärung*: Dies ist falsch. `keyCertSign` allein ist nicht ausreichend; es muss in der Sektion `v3_ca` zusammen mit `basicConstraints` verwendet werden.
    * B) `extendedKeyUsage = serverAuth`
        * *Erklärung*: Dies ist falsch. `serverAuth` legt fest, dass ein Zertifikat für einen Server verwendet werden darf, nicht als CA.
    * C) `subjectKeyIdentifier=hash`
        * *Erklärung*: Dies ist falsch. Diese Option identifiziert den öffentlichen Schlüssel des Zertifikats.
    * **D) `basicConstraints = critical, CA:true`**
        * *Erklärung*: Dies ist korrekt. Diese Option in der `v3_ca` Sektion ist entscheidend, um ein Zertifikat als CA zu kennzeichnen.
    * E) `policy = policy_loose`
        * *Erklärung*: Dies ist falsch. Die Richtlinie legt fest, welche Felder beim Ausfüllen obligatorisch sind.

7.  **Warum werden die Rechte des privaten CA-Schlüssels (`ca.key.pem`) auf `400` gesetzt?**
    * A) Um zu erlauben, dass jeder das Zertifikat lesen und ausführen kann.
        * *Erklärung*: Dies ist falsch. Die Berechtigung `400` erlaubt nur dem Besitzer Leserechte.
    * B) Um die Datei von der CA in den Webserver-Container zu kopieren.
        * *Erklärung*: Dies ist falsch. Die Berechtigungen sind für die Sicherheit da, nicht für den Kopiervorgang.
    * C) Um dem Apache2-Webserver Leserechte zu gewähren.
        * *Erklärung*: Dies ist falsch. Der Apache-Webserver benötigt keine Leserechte für den privaten CA-Schlüssel.
    * **D) Um sicherzustellen, dass nur der Besitzer die Datei lesen kann.**
        * *Erklärung*: Dies ist korrekt. Der private Schlüssel der CA ist das wichtigste und schützenswerteste Asset. Die Berechtigung `400` sorgt dafür, dass nur der Besitzer darauf zugreifen kann.
    * E) Um die Dateigröße zu reduzieren.
        * *Erklärung*: Dies ist falsch. Die Berechtigungen haben keinen Einfluss auf die Dateigröße.

8.  **Was ist ein `Certificate Signing Request` (CSR)?**
    * A) Eine Datei, die den privaten Schlüssel der CA enthält und zur Signierung verwendet wird.
        * *Erklärung*: Dies ist falsch. Ein CSR enthält einen öffentlichen Schlüssel und Informationen zur Identität. Der private Schlüssel verbleibt auf dem Gerät.
    * **B) Eine Datei mit einem öffentlichen Schlüssel und Identitätsinformationen, die von einer CA signiert werden muss.**
        * *Erklärung*: Dies ist korrekt. Der CSR ist der Antrag, den man an eine CA sendet, um ein Zertifikat zu erhalten.
    * C) Das fertige, von der CA signierte Zertifikat.
        * *Erklärung*: Dies ist falsch. Der CSR ist nur der Antrag; das fertige Zertifikat ist die Antwort der CA.
    * D) Ein temporäres Passwort, das bei der Erstellung des Zertifikats verwendet wird.
        * *Erklärung*: Dies ist falsch. Ein CSR ist eine Datei mit Schlüssel- und Identitätsinformationen.
    * E) Ein Befehl, um die Gültigkeit eines Zertifikats zu überprüfen.
        * *Erklärung*: Dies ist falsch. Ein Befehl zur Überprüfung ist z. B. `openssl x509 -in file.pem -text`.

9.  **Welche Dateien müssen von der CA an einen Client (z. B. den Apache2-Container) übertragen werden, um eine sichere TLS-Verbindung zu ermöglichen?**
    * A) `ca.cert.pem` und `server.key.pem`
        * *Erklärung*: Dies ist falsch. Es fehlt das `server.cert.pem`-Zertifikat.
    * B) Nur `server.cert.pem` und `server.key.pem`
        * *Erklärung*: Dies ist falsch. Ohne das `ca.cert.pem`-Zertifikat kann der Client dem Server-Zertifikat nicht vertrauen.
    * C) Nur das Root-Zertifikat der CA (`ca.cert.pem`)
        * *Erklärung*: Dies ist falsch. Der Client benötigt das Server-Zertifikat und den privaten Schlüssel des Servers, um eine Verbindung herzustellen.
    * D) Nur der private Schlüssel (`server.key.pem`)
        * *Erklärung*: Dies ist falsch. Der private Schlüssel allein ist nutzlos ohne das dazugehörige Zertifikat.
    * **E) `ca.cert.pem`, `server.cert.pem` und `server.key.pem`**
        * *Erklärung*: Dies ist korrekt. Der Client benötigt das CA-Zertifikat, um dem Server zu vertrauen, und der Server benötigt sein eigenes Zertifikat und den privaten Schlüssel.

10. **Warum muss das CA-Zertifikat (`ca.cert.pem`) auf einem Client-Rechner importiert werden?**
    * A) Um die Gültigkeit von öffentlichen Zertifikaten (z. B. von Google) zu überprüfen.
        * *Erklärung*: Dies ist falsch. Der Client verlässt sich hierfür auf die bereits vorinstallierten Root-Zertifikate.
    * B) Um dem Client die Erstellung eigener Zertifikate zu ermöglichen.
        * *Erklärung*: Dies ist falsch. Das CA-Zertifikat ermöglicht keine Zertifikatserstellung, sondern dient nur der Vertrauensstellung.
    * **C) Damit der Client dem von der eigenen CA ausgestellten Server-Zertifikat vertraut.**
        * *Erklärung*: Dies ist korrekt. Durch den Import des CA-Zertifikats vertraut das Betriebssystem allen von dieser CA signierten Zertifikaten.
    * D) Um die Netzwerkverbindung zu beschleunigen.
        * *Erklärung*: Dies ist falsch. Der Import hat keinen Einfluss auf die Geschwindigkeit.
    * E) Um den privaten Schlüssel des Servers auf den Client zu übertragen.
        * *Erklärung*: Dies ist falsch. Private Schlüssel sollten niemals von einem Server übertragen oder auf Clients importiert werden.

---

### Lizenz
Dieses Werk ist lizenziert unter der **Creative Commons - Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz**.
 
[Zum Lizenztext auf der Creative Commons Webseite](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)
