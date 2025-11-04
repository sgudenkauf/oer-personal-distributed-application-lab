---
title: "Fragen zur Netzwerkkonfiguration und -diagnose im LXC-Container"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "uwe.bachmann@jade-hs.de"
organization: "PDAL-Projekt"
date: "2025-08-25"
version: "1.0.0"
level: "Ebene 1, Lerneinheit 1.3, Assessment"
duration: "0,2 Std"
prerequisites:["Abgeschlossen -  Dokument: 1300 - Netzwerkkonfiguration und -diagnose im LXC-Container"]
tags: ["PDAL","Assessment"]
license: "CC BY-SA 4.0"
---

### Fragen zur Netzwerkkonfiguration und -diagnose im LXC-Container

**1. Welche Datei wird in neueren Ubuntu-Versionen (>= 18.04) typischerweise zur Konfiguration einer statischen IP-Adresse in einem LXC-Container verwendet?**
* A. `/etc/network/interfaces`
    * *Hinweis: Diese Datei wird für die Konfiguration in älteren Ubuntu- oder Debian-Systemen verwendet.*
* **B. `/etc/netplan/*.yaml`**
    * *Hinweis: Korrekt. Netplan ist der Standard für die Netzwerkkonfiguration in neueren Ubuntu-Versionen.*
* C. `/etc/dhcp/dhcpd.conf`
    * *Hinweis: Diese Datei wird für die Konfiguration eines DHCP-Servers verwendet, nicht für die manuelle Zuweisung einer statischen IP-Adresse.*
* D. `/etc/resolv.conf`
    * *Hinweis: Diese Datei konfiguriert die DNS-Namensauflösung, nicht die IP-Adresse selbst.*
* E. `/etc/sysconfig/network-scripts/ifcfg-eth0`
    * *Hinweis: Dies ist ein Konfigurationspfad, der typischerweise in Red Hat-basierten Systemen wie CentOS oder Fedora verwendet wird.*

**2. Was ist die Hauptfunktionalität des Befehls `sudo netplan try`?**
* A. Er speichert die neue Netzwerkkonfiguration dauerhaft.
    * *Hinweis: Das macht der Befehl `sudo netplan apply`.*
* **B. Er testet die Konfiguration, bevor er sie dauerhaft anwendet.**
    * *Hinweis: Korrekt. Der Befehl testet die Konfiguration für 120 Sekunden, um sicherzustellen, dass das Netzwerk erreichbar bleibt.*
* C. Er zeigt eine Vorschau der Konfigurationsdatei an, ohne Änderungen vorzunehmen.
    * *Hinweis: Das würde ein Befehl wie `cat` oder `nano` tun.*
* D. Er setzt die Netzwerkkonfiguration auf DHCP zurück.
    * *Hinweis: Dieser Befehl hat keinen direkten Bezug zur DHCP-Rücksetzung.*
* E. Er löscht die bestehende Netplan-Konfiguration.
    * *Hinweis: Für das Löschen von Konfigurationsdateien sind manuelle Befehle wie `rm` notwendig.*

**3. Ein `ping 8.8.8.8` funktioniert, aber ein `ping google.com` schlägt fehl. Welches Problem liegt höchstwahrscheinlich vor?**
* A. Es gibt ein Gateway-Problem.
    * *Hinweis: Wenn das Gateway-Problem vorliegen würde, könnten weder IPs noch Domains erreicht werden.*
* B. **Es gibt ein DNS-Problem.**
    * *Hinweis: Korrekt. Die IP ist erreichbar, aber die Namensauflösung funktioniert nicht, was auf einen fehlerhaften Nameserver hinweist.*
* C. Der Webserver ist nicht erreichbar.
    * *Hinweis: `ping` testet die Konnektivität auf IP-Ebene und nicht die Erreichbarkeit eines Webservers, dafür ist `curl` oder `wget` besser geeignet.*
* D. Das Netzwerkinterface (`eth0`) ist nicht aktiv.
    * *Hinweis: In diesem Fall würden keine Pings funktionieren.*
* E. Die statische IP-Adresse ist falsch konfiguriert.
    * *Hinweis: Wenn die IP falsch konfiguriert wäre, würde der Container höchstwahrscheinlich keine Verbindung zum externen Netzwerk herstellen können.*

**4. Welches Diagnostic-Tool wird verwendet, um eine Liste aller Netzwerk-Interfaces, IP-Adressen und deren Status anzuzeigen?**
* A. `ping`
    * *Hinweis: `ping` prüft die Erreichbarkeit eines Hosts, nicht die lokalen Interfaces.*
* B. `ip r`
    * *Hinweis: `ip r` zeigt die Routing-Tabelle an.*
* **C. `ip a`**
    * *Hinweis: Korrekt. `ip a` (oder `ip address`) ist der Befehl zur Anzeige der Interface-Informationen.*
* D. `netstat`
    * *Hinweis: `netstat` zeigt Netzwerkstatistiken und offene Verbindungen an.*
* E. `curl`
    * *Hinweis: `curl` ist ein Tool zum Testen von HTTP-Anfragen.*

**5. Was ist die Hauptfunktion des Befehls `ip r` im Kontext der Netzwerkdiagnose?**
* A. Er zeigt offene Ports an.
    * *Hinweis: Dafür wird `netstat` oder `ss` verwendet.*
* B. Er testet die Erreichbarkeit einer IP-Adresse.
    * *Hinweis: Dafür wird `ping` verwendet.*
* **C. Er zeigt die Routing-Tabelle und das Standard-Gateway an.**
    * *Hinweis: Korrekt. Der Befehl ist entscheidend, um zu prüfen, ob der Datenverkehr korrekt aus dem lokalen Netzwerk geleitet wird.*
* D. Er listet die DNS-Server auf.
    * *Hinweis: Die DNS-Server sind in der Konfigurationsdatei oder unter `/etc/resolv.conf` zu finden.
* E. Er zeigt die aktuelle IP-Adresse an.*
    * *Hinweis: Dafür wird `ip a` verwendet.*

**6. Was ist der Unterschied zwischen der Verwendung von Leerzeichen und Tabs in einer Netplan-Konfigurationsdatei?**
* A. Es gibt keinen Unterschied; beides funktioniert.
    * *Hinweis: Dies ist falsch. YAML ist sehr empfindlich.*
* B. Tabs werden für Einrückungen bevorzugt.
    * *Hinweis: Im Gegenteil, Tabs sind in YAML nicht erlaubt und führen zu Fehlern.*
* **C. Nur Leerzeichen sind für Einrückungen erlaubt.**
    * *Hinweis: Korrekt. Das YAML-Format, das von Netplan verwendet wird, akzeptiert ausschließlich Leerzeichen zur Einrückung.*
* D. Tabs werden nur für Kommentare verwendet.
    * *Hinweis: Tabs werden in YAML generell nicht unterstützt, egal wofür.*
* E. Leerzeichen werden nur für die erste Ebene der Einrückung verwendet.
    * *Hinweis: Leerzeichen werden für alle Ebenen der Einrückung verwendet.*

**7. Was ist ein typisches Symptom für ein Gateway-Problem?**
* A. `ping 8.8.8.8` funktioniert, aber `ping google.com` schlägt fehl.
    * *Hinweis: Das ist ein Symptom eines DNS-Problems.*
* B. Der Container erhält keine IP-Adresse über DHCP.
    * *Hinweis: Das deutet auf ein Problem mit der DHCP-Konfiguration oder dem Server hin.*
* **C. Weder ein `ping` zum Gateway noch ein `ping` zu einer externen IP funktioniert.**
    * *Hinweis: Korrekt. Das Gateway ist die erste Station, die erreicht werden muss, um ins Internet zu gelangen. Wenn diese Verbindung fehlschlägt, ist das der erste Indikator.*
* D. Die internen Dienste des Containers sind nicht erreichbar.
    * *Hinweis: Dieses Problem liegt meistens an der Konfiguration der internen Dienste oder einer Firewall.*
* E. Die Konfiguration in `/etc/network/interfaces` wird nicht angewendet.
    * *Hinweis: Dies ist ein Konfigurationsproblem, das unabhängig vom Gateway-Problem auftreten kann.*

**8. Welchen Befehl verwendet man, um den Netzwerkdienst nach der manuellen Bearbeitung der `/etc/network/interfaces` Datei neu zu starten?**
* A. `sudo netplan apply`
    * *Hinweis: Dieser Befehl ist für Netplan-Konfigurationen gedacht.*
* **B. `sudo systemctl restart networking`**
    * *Hinweis: Korrekt. Dieser Befehl startet den zuständigen Dienst neu, um die Änderungen zu übernehmen.*
* C. `sudo service networking stop`
    * *Hinweis: Dieser Befehl stoppt den Dienst, startet ihn aber nicht neu.*
* D. `sudo restart eth0`
    * *Hinweis: Dies ist keine korrekte Befehlssyntax.*
* E. `sudo networking restart`
    * *Hinweis: Dies ist eine veraltete Befehlssyntax und wird in modernen Systemen durch `systemctl` ersetzt.*

**9. Wann ist es laut dem Dokument unabdingbar, statische IP-Adressen in einer Container-Umgebung zu vergeben?**
* A. Wenn der Host kein DHCP anbietet.
    * *Hinweis: Der Text legt nahe, dass DHCP standardmäßig verwendet wird.*
* B. Wenn der Host mehrere Bridges nutzt.
    * *Hinweis: Die Anzahl der Bridges ist kein entscheidender Faktor für die Vergabe statischer IPs.*
* **C. Wenn kein DNS-Server für die Namensauflösung zur Verfügung steht.**
    * *Hinweis: Korrekt. Wenn Dienste über Hostnamen kommunizieren müssen, aber kein DNS vorhanden ist, sind statische IPs die einzige verlässliche Methode.*
* D. Wenn eine Verbindung ins Internet benötigt wird.
    * *Hinweis: Internetzugang kann auch über DHCP und DNS hergestellt werden.*
* E. Wenn mehrere Container auf dem gleichen Host laufen.
    * *Hinweis: Auch bei mehreren Containern kann DHCP verwendet werden, solange eine DNS-Auflösung möglich ist.*

**10. Was wird laut dem Dokument mit dem `netstat -tulnp`-Befehl im LXC-Container geprüft?**
* A. Die Routing-Tabelle des Containers.
    * *Hinweis: Dafür ist der Befehl `ip r` vorgesehen.*
* B. Die IP-Adresse des Containers.
    * *Hinweis: Dafür wird der Befehl `ip a` verwendet.*
* **C. Offene, lauschende Ports und die zugehörigen Prozesse.**
    * *Hinweis: Korrekt. Der Befehl listet alle lauschenden TCP- und UDP-Ports sowie die dazugehörigen Prozess-IDs auf.*
* D. Die Namensauflösung im Container.
    * *Hinweis: Dafür wird `ping <hostname>` oder `dig` verwendet.*
* E. Die Download-Geschwindigkeit aus dem Internet.
    * *Hinweis: Tools wie `wget` oder `speedtest-cli` sind für diesen Zweck besser geeignet.*

---

### Lizenz
Dieses Werk ist lizenziert unter der **Creative Commons - Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz**.
 
[Zum Lizenztext auf der Creative Commons Webseite](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)

