---
title: "Grundlagen der Netzwerk-Kommunikationsanalyse"
author: ["Gudenkauf, Prof Stefan", "Ronald Kalk", "Uwe Bachmann"]
mail: "pdal@jade-hs.de"
organization: "PDAL-Projekt, Jade Hochschule"
date: "2025-11-20"
version: "1.0.0"
level: "Ebene 3, Lerneinheit 3.1"
duration: "Geschätzte Dauer (1 - 2 Stunden)"
prerequisites: "Abschluss Ebene 2"
tags: ["Proxmox", "Linux", "Virtualisierung", "Tshark", "Tcpdump"]
license: "CC BY-SA 4.0"
---

# Grundlagen der Netzwerk-Kommunikationsanalyse

## Einleitung

Die Netzwerk-Kommunikationsanalyse ist ein zentraler Bestandteil der Netzwerktechnik und IT-Sicherheit. Sie ermöglicht nicht nur das Überwachen des Datenverkehrs, sondern vor allem die **Fehleranalyse**, die Leistungsoptimierung und das Aufdecken von Sicherheitsrisiken. In komplexen Netzwerken, wie sie beispielsweise in virtuellen Umgebungen mit mehreren LXC-Containern vorkommen, ist die Analyse des Datenverkehrs unverzichtbar, um Probleme wie Paketverlust, fehlerhafte Verbindungen oder falsch konfigurierte Dienste schnell zu erkennen.

Jedes Gerät in einem Netzwerk sendet und empfängt Datenpakete. Diese Pakete enthalten nicht nur die Nutzdaten (Payload), sondern auch Header-Informationen, die über **Quelle, Ziel, verwendetes Protokoll und Portnummern** Auskunft geben. Das Verstehen dieser Informationen ist entscheidend, um Netzwerkprobleme systematisch zu diagnostizieren.

**Warum ist das wichtig?**

* **Fehleranalyse:** Paketverluste, Verbindungsabbrüche oder fehlerhafte Routen lassen sich durch Analyse der Pakete erkennen.
* **Leistungsoptimierung:** Latenzzeiten, Bandbreitennutzung und Engpässe werden sichtbar.
* **Sicherheit:** Unautorisierte Zugriffe, Malware-Kommunikation oder ungewöhnlicher Traffic können identifiziert werden.

---

## 1. Fachbegriffe

* **Packet (Paket):** Eine kleine Datenmenge, die über das Netzwerk gesendet wird. Jedes Paket besteht aus Header und Payload. Header enthalten Metainformationen wie IP-Adresse, Port, Sequenznummern und Flags. Die Payload enthält die eigentlichen Nutzdaten. Die detaillierte Analyse des Headers ermöglicht es, Kommunikationsfehler oder Sicherheitsvorfälle zu erkennen.

* **IP-Adresse:** Eindeutige Kennung eines Geräts im Netzwerk. Die Analyse der IP-Adressen erlaubt es, Kommunikationswege nachzuvollziehen und zu prüfen, ob Pakete vom richtigen Sender zum richtigen Empfänger gelangen.

* **Port:** Logischer Endpunkt auf einem Gerät, der den Datenverkehr für bestimmte Dienste identifiziert (z. B. Port 80 für HTTP). Das Verständnis von Ports hilft bei der Identifikation von Diensten und der gezielten Fehleranalyse.

* **Protokoll:** Regeln und Formate, nach denen Daten im Netzwerk übertragen werden (z. B. TCP, UDP, HTTP, DNS). Die Kenntnis der Protokolle ist essenziell, um die Kommunikation korrekt zu interpretieren und Probleme wie fehlerhafte Handshakes oder Paketverluste zu erkennen.

* **TCP (Transmission Control Protocol):** Ein verbindungsorientiertes Protokoll. TCP garantiert, dass Pakete korrekt und in der richtigen Reihenfolge beim Empfänger ankommen. Fehler wie verlorene Pakete oder wiederholte Übertragungen können direkt auf Netzwerkprobleme hinweisen.

* **UDP (User Datagram Protocol):** Verbindungsloses Protokoll. Schneller als TCP, aber ohne Zustellgarantie. Ideal für Echtzeitdaten wie Audio/Video. Fehler in UDP-Kommunikation zeigen sich z. B. durch Paketverluste oder Jitter.

* **Wireshark:** Ein grafisches Tool zur Paketerfassung und -analyse. Ermöglicht die Visualisierung von Paketen, Filtern nach IP/Port/Protokoll und die Rekonstruktion von Sessions. Unverzichtbar für detaillierte Fehleranalyse und Sicherheitsüberprüfungen.

* **TShark:** Die Kommandozeilen-Version von Wireshark, die für Server und LXC-Container ohne GUI eingesetzt wird. Wireshark und TShark sind zwei Versionen desselben Projektes, wobei TShark die gleichen Analysefunktionen bietet, jedoch über die Shell bedient wird.

* **tcpdump:** Kommandozeilen-basiertes Tool, das Pakete mitschneidet. Flexibel für Serverumgebungen ohne GUI. Eignet sich besonders für schnelle Analysen oder Logging von Traffic, der später in Wireshark ausgewertet wird.

---

## 2. Ziele der Lerneinheit

1. **Installation und Grundkonfiguration von `tcpdump` und `Wireshark`/`TShark`:**

   * Ermöglicht den Einstieg in die Paketerfassung.
   * Legt die Grundlage für systematische Fehlerdiagnose.

2. **Filtern von Netzwerktraffic nach IP, Port und Protokoll:**

   * Wichtig, um gezielt Kommunikationsprobleme zwischen einzelnen Containern oder Geräten zu identifizieren.
   * Filter verhindern, dass die Analyse durch irrelevanten Traffic überlastet wird.

3. **Identifikation von Quell- und Ziel-IP-Adressen sowie Ports:**

   * Essentiell für das Erkennen von fehlerhaften Verbindungen oder unautorisierten Zugriffen.
   * Hilft, die Ursache von Paketverlusten, Timeouts oder fehlerhaften Verbindungen zu bestimmen.

4. **Grundlegende Analyse von HTTP- und DNS-Protokollen zwischen Containern:**

   * Fehler wie fehlgeschlagene DNS-Auflösungen, HTTP-Fehlercodes oder fehlerhafte TLS-Handshakes werden sichtbar.
   * Diese Analyse ist entscheidend, um Dienste innerhalb der Container-Umgebung zuverlässig zu betreiben.

5. **Sicherheitsaspekt:**

   * Analyse von Netzwerkpaketen hilft, ungewöhnliche oder unautorisierte Zugriffe zu erkennen.
   * Erkennen von Malware-Kommunikation, Port-Scans oder Man-in-the-Middle-Versuchen.
   * Fehleranalyse und Sicherheitsanalyse sind oft eng miteinander verbunden, da viele Fehlerursachen auch Sicherheitsrisiken aufdecken.

---

## 3. Netzwerk-Analyse mit TShark

Dieser Abschnitt befaßt sich mit der Einrichtung eines zentralen `LXC-Containers` für die Netzwerk-Analyse aller LXC-Container in der Proxmox-Umgebung des PDAL-Projekts. Ziel ist es, den gesamten Netzwerkverkehr zu beobachten und Fehler zu analysieren, ohne `TShark` auf jedem Container installieren zu müssen.

---

## 4. Installation von TShark auf einem separaten LXC

### 4.1 LXC-Container anlegen

* IP: `192.168.137.230`
* Benutzer: `pdal`
* Passwort: `JadeHS20`

Benutzer `pdal` mit `sudo-Rechten` versehen.

### 4.2 Grundinstallation

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install tshark -y
```

> Hinweis: Während der Installation fragt TShark, ob Nicht-Root-Benutzer Pakete sniffen dürfen. Mit `Yes` bestätigen.

### 4.3 Netzwerk-Konfiguration

* Alle LXC müssen über dieselbe Bridge (`vmbr0`) laufen.
* Promiscuous Mode aktivieren:

**Was ist der Promiscuous Mode?**

Der `Promiscuous Mode` ist ein spezieller Betriebsmodus eines `Netzwerk-Interfaces`, bei dem das Interface alle Netzwerkpakete empfängt, die über das `Netzwerksegment` oder die `Bridge` laufen, unabhängig davon, ob die Pakete für die eigene `IP-Adresse` bestimmt sind oder nicht.

**Wozu es dient:**

Ermöglicht die zentralisierte Analyse des gesamten Netzwerkverkehrs.

Unverzichtbar für Tools wie `TShark` oder `Wireshark`, um Fehler, Paketverluste oder Sicherheitsvorfälle im Netzwerk zu erkennen.

**Wichtig:**

Nur auf dem `Interface` aktivieren, das den gesamten Traffic überwachen soll (z. B. der TShark-Container).

Andere Hosts oder Container müssen nicht im Promiscuous Mode laufen.

```bash
sudo ip link set dev eth0 promisc on
```

* Prüfen:

```bash
ip link show eth0
# Sollte 'PROMISC' in den Flags enthalten
```

### 4.4 Test der Sniffer-Umgebung

```bash
tshark -i eth0 -c 10
```

> Es sollten erste Pakete angezeigt werden, z.B. DHCP, ARP.

---

## 5. Konfiguration von TShark für zentrale Analyse

### 5.1 Alle Interfaces beobachten

```bash
tshark -i eth0
```

* Beobachtet den gesamten Verkehr über das Interface des Sniffer-LXC.
* Alternativ mehrere Interfaces:

```bash
tshark -i eth0 -i eth1
```

### 5.2 Filter nach Subnetz oder Hosts

```bash
tshark -i eth0 net 192.168.137.0/24
```

```bash
tshark -i eth0 host 192.168.137.230 and host 192.168.137.120
```

### 5.3 Protokollbasierte Filter

| Protokoll  | Standard-Port | Filter      | Hinweis                                  |
| ---------- | ------------- | ----------- | ---------------------------------------- |
| HTTP       | 80            | `port 80`   | Standard-Port, anpassen falls abweichend |
| HTTPS      | 443           | `port 443`  | Standard-Port, anpassen falls abweichend |
| MariaDB    | 3306          | `port 3306` | Standard-Port, anpassen falls abweichend |
| PostgreSQL | 5432          | `port 5432` | Standard-Port, anpassen falls abweichend |
| MQTT       | 1883          | `port 1883` | Standard-Port, anpassen falls abweichend |
| MQTT TLS   | 8883          | `port 8883` | Standard-Port, anpassen falls abweichend |
| Kafka      | 9092          | `port 9092` | Standard-Port, anpassen falls abweichend |

Beispiel für TCP-Handshake-Fehler:

```bash
tshark -i eth0 tcp.flags.syn==1
```

### 5.4 Logging in Datei

```bash
tshark -i eth0 -f "net 192.168.137.0/24" -w /var/log/tshark_capture.pcap
```

* Mit Wireshark oder Tshark später analysierbar

---

## 6. Analyse verschlüsselter Kommunikation

* Inhalt von `TLS/HTTPS/SSH` ist verschlüsselt.
* Meta-Daten sichtbar: `IP`, `Port`, `Timing`, `Flags`.
* Fehleranalyse möglich: `TLS-Handshakes`, `Zertifikate`, `Timeouts`.

---

## 6. Beispiele für praktische Analyse

### 6.1 Kommunikation zwischen zwei Containern prüfen

```bash
tshark -i eth0 host 192.168.137.230 and host 192.168.137.120
```

### 6.2 Nur Datenbankverkehr überwachen

```bash
tshark -i eth0 port 3306 or port 5432
```

### 6.3 HTTP/HTTPS Analyse für Webdienste

```bash
tshark -i eth0 port 80 or port 443
```

### 6.4 DNS-Fehleranalyse

```bash
tshark -i eth0 port 53
```

---

## 7. Installation von tcpdump auf LXC-Container

Dieser Abschnitt befaßt sich mit der Installation, Konfiguration und Nutzung von **tcpdump** auf einem bestehenden LXC-Container (derselbe, der bereits für T-Shark genutzt wird). Die Dokumentation richtet sich an Studierende und Lernende und erklärt Schritt für Schritt die wichtigsten Funktionen von tcpdump, inklusive Praxisbeispiele, Filter und optionaler Erweiterungen.

---

## 8. Installation

### 8.1 Paketinstallation

```bash
sudo apt update
sudo apt install tcpdump -y
```

### 8.2 Überprüfung der Installation

```bash
tcpdump --version
```

Erwartete Ausgabe: tcpdump Version 4.x.x oder ähnlich.

---

> Hinweis: Tcpdump benötigt Root-Rechte oder die Linux-Fähigkeit **CAP_NET_RAW**, um Netzwerkpakete abfangen zu können.

---

## 9. tcpdump ohne Root mit CAP_NET_RAW

Tcpdump kann auch ohne Root-Rechte ausgeführt werden, wenn dem Programm die Fähigkeit **CAP_NET_RAW** zugewiesen wird.

### 9.1 Was ist CAP_NET_RAW?

* **CAP_NET_RAW** ist eine Linux-Kapazität (Capability), also eine feingranulare Berechtigung für Prozesse.
* Sie erlaubt einem Prozess, **rohe Netzwerkpakete zu senden und zu empfangen**, ohne Root-Rechte zu benötigen.
* Normalerweise ist das Erfassen von Paketen auf niedrigem Level nur Root möglich. Mit CAP_NET_RAW kann ein Nicht-Root-Prozess tcpdump oder eigene Netzwerktools nutzen.

### 9.2 tcpdump mit CAP_NET_RAW nutzen

1. Dem tcpdump-Programm die Fähigkeit zuweisen:

   ```bash
   sudo setcap cap_net_raw,cap_net_admin=eip /usr/sbin/tcpdump
   ```

   * `cap_net_raw,cap_net_admin=eip` setzt die erforderlichen Berechtigungen für Netzwerkoperationen.

2. Tcpdump als normaler Benutzer ausführen:

   ```bash
   tcpdump -i eth0
   ```

   * Vorteil: Sicherer als Root-Rechte, da nur Zugriff auf rohe Netzwerkpakete erlaubt wird.
   * CAP_NET_RAW ermöglicht das Erfassen und Senden von Paketen ohne vollen Root-Zugriff.

---

## 10. Grundlegende Nutzung

### 10.1 Pakete auf einem Interface erfassen

```bash
sudo tcpdump -i eth0
```

* `-i eth0`: Interface auswählen (bei LXC kann auch `eth0` oder `ensX` sein)
* Standardmäßig werden nur die Header angezeigt.

### 10.2 Pakete in eine Datei speichern

```bash
sudo tcpdump -i eth0 -w capture.pcap
```

* `-w capture.pcap`: Pakete werden in der Datei `capture.pcap` gespeichert
* Diese Datei kann später z. B. mit Wireshark oder T-Shark analysiert werden.

### 10.3 Nur bestimmte Pakete filtern

* Nur TCP-Pakete:

   ```bash
   sudo tcpdump -i eth0 tcp
   ```

* Pakete von/zur IP-Adresse 192.168.137.110:

   ```bash
   sudo tcpdump -i eth0 host 192.168.137.110
   ```

* Pakete auf Port 80:

   ```bash
   sudo tcpdump -i eth0 port 80
   ```

---

## 11. Erweiterte Nutzung

### 11.1 Live-Analyse mit Anzeige von Inhalt

```bash
sudo tcpdump -i eth0 -A
```

* `-A`: ASCII-Ausgabe des Paketinhalts

### 11.2 Filter kombinieren

```bash
sudo tcpdump -i eth0 tcp port 443 and host 192.168.137.110
```

* Filter können mit `and`, `or`, `not` kombiniert werden

### 11.3 Limitieren der Paketanzahl

```bash
sudo tcpdump -i eth0 -c 100
```

* `-c 100`: Erfasst nur 100 Pakete

### 11.4 Zeitstempel und ausführliche Ausgabe

```bash
sudo tcpdump -i eth0 -tttt -v
```

* `-tttt`: detaillierte Zeitstempel
* `-v` / `-vv` / `-vvv`: steigende Detailgenauigkeit

---

## 12. Sicherheitshinweise

* Tcpdump erfasst alle Pakete, sensible Daten können angezeigt werden → Zugriff auf Container begrenzen
* Root-Rechte oder CAP_NET_RAW erforderlich → nur vertrauenswürdige Benutzer verwenden
* Speicherplatz beachten, wenn Pakete in Dateien geschrieben werden

---

## 13. Optional: Analyse mit Wireshark/T-Shark

* Captures aus tcpdump (`.pcap`) können direkt mit T-Shark analysiert werden:

   ```bash
   tshark -r capture.pcap
   ```

* Ermöglicht Kombination von tcpdump + T-Shark für tiefergehende Analysen

---

## 14. Fazit

## 15. Best Practices

1. **Nicht zu viele Webkonsolen gleichzeitig öffnen**, sonst hängt die Anzeige.
2. **Promiscuous Mode aktivieren**, um gesamten Bridge-Traffic zu sehen.
3. **TShark/tcpdump auf dem Host oder einem zentralen LXC installieren**, nicht auf jedem Container.
4. **Filter verwenden**, um die Analyse übersichtlich zu halten.
5. **Für verschlüsselte Protokolle** nur Meta-Daten analysieren; Inhalte bleiben verschlüsselt.

---

## 16. Zusammenfassung

* Ein zentraler TShark/tcpdump-LXC reicht aus, um den gesamten LXC-Traffic zu analysieren.
* Promiscuous Mode auf dem Interface ist zwingend notwendig.
* Filter nach IP, Subnetz, Ports oder Protokollen erleichtert die Analyse.
* Verschlüsselte Kommunikation kann nicht im Inhalt mitgelesen werden, aber Fehler und Metadaten sind sichtbar.
* Logging in Dateien ermöglicht spätere Detailanalyse mit Wireshark.

## Fazit

Die Netzwerk-Kommunikationsanalyse ist ein unverzichtbares Werkzeug für die **Fehlerdiagnose**, **Leistungsoptimierung** und **Sicherheitsüberwachung** in modernen IT-Umgebungen. Durch das Verständnis von Paketen, IPs, Ports und Protokollen können Probleme gezielt lokalisiert und behoben werden. Insbesondere in Container-Umgebungen wie LXC ist die systematische Analyse essenziell, um komplexe Kommunikationsprobleme schnell zu identifizieren und gleichzeitig Sicherheitsrisiken zu minimieren.
**TShark** ist ein effektives Werkzeug zur gezielten Fehleranalyse im Netzwerk. Durch das Erfassen von Netzwerkpaketen und die Anwendung von Filtern auf IP-Adressen, Ports oder Protokolle lassen sich Verbindungsprobleme, Timeouts, fehlerhafte Handshakes oder andere Kommunikationsstörungen zuverlässig identifizieren. Auch wenn verschlüsselte Verbindungen nur eingeschränkt einsehbar sind, liefern Meta-Daten wie Quell- und Ziel-IP, Portinformationen und Zeitstempel wertvolle Hinweise für die Diagnose. Die Möglichkeit, Daten zu protokollieren und später detailliert auszuwerten, erleichtert die systematische Analyse von Netzwerkproblemen. Überwachung des Netzwerks kann dabei unterstützend genutzt werden, steht jedoch nicht im Mittelpunkt – der Fokus liegt auf der Fehlersuche und der Behebung von Problemen.
**Tcpdump** bietet eine schnelle, flexible Möglichkeit, Netzverkehr zu erfassen und zu filtern. Zusammen mit T-Shark oder Wireshark können auch komplexe Analysen durchgeführt werden.

---

## Quellen

* „tshark(1)“. Zugegriffen: 14. November 2025. [Online]. Verfügbar unter: [Tshark Manual](https://www.wireshark.org/docs/man-pages/tshark.html)
* „Home | TCPDUMP & LIBPCAP“. Zugegriffen: 14. November 2025. [Online]. Verfügbar unter: [tcpdump Doc](https://www.tcpdump.org/index.html#documentation)

---

## Lizenz

Dieses Werk ist lizenziert unter der **Creative Commons Namensnennung - Nicht-kommerziell - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz**.

[Zum Lizenztext auf der Creative Commons Webseite](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.de)


