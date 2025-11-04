---
title: "Test - Fragen zu den Grundlagen der ICS-Konfiguration"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe"]
email: "uwe.bachmann@jade-hs.de"
organization: "PDAL-Projekt"
date: "2025-08-08"
version: "1.0.0"
level: "Ebene 0, Lerneinheit 0.1, Assessment"
duration: "0,2 Std"
prerequisites:["Abgeschlossen -  Dokument: 0150 - Netzwerkkarte Experiment"]
tags: ["PDAL","Assessment"]
license: "CC BY-SA 4.0"
---

### Test - Fragen zu den Grundlagen der ICS-Konfiguration

1.  **Welche IP-Adresse vergibt Windows standardmäßig an den Netzwerkadapter, der die Internetverbindung für das lokale PDAL-Netzwerk freigibt?**
    * A) `10.0.0.1`
        * *Hinweis*: Diese IP-Adresse wird oft als Standard-Gateway in Heimnetzwerken verwendet, aber nicht von Windows ICS.
    * B) `172.16.0.1`
        * *Hinweis*: Dies ist eine private IP-Adresse, die oft in größeren Unternehmensnetzwerken verwendet wird.
    * C) `192.168.1.1`
        * *Hinweis*: Dies ist eine sehr häufige Standard-IP-Adresse für Router in privaten Netzwerken.
    * **D) `192.168.137.1`**
        * *Hinweis*: Genau. Windows verwendet diese spezifische IP-Adresse, um den DHCP-Server und das Gateway für das lokale ICS-Netzwerk bereitzustellen.
    * E) `192.168.0.1`
        * *Hinweis*: Auch diese IP-Adresse wird häufig als Standard-Gateway verwendet, aber nicht von Windows ICS.

2.  **Welche der folgenden Aussagen beschreibt die Funktionsweise von Internet Connection Sharing (ICS) im Kontext des PDAL-Aufbaus am besten?**
    * A) ICS leitet alle Netzwerkpakete direkt an das öffentliche Internet weiter, ohne sie zu filtern.
        * *Hinweis*: Das Gegenteil ist der Fall; ICS beinhaltet eine Firewall, die den Datenverkehr filtert und schützt.
    * **B) ICS fungiert als ein Router und eine Firewall, die das interne Netzwerk schützt und Pakete zwischen den Netzwerken routet.**
        * *Hinweis*: ICS agiert wie ein einfacher Router und ein Paketfilter, um die Netzwerkverbindung zu teilen und das lokale Netzwerk zu sichern.
    * C) ICS synchronisiert die IP-Adressen zwischen dem lokalen Netzwerk und dem Internet automatisch.
        * *Hinweis*: ICS hat keine Funktion zur Synchronisierung von IP-Adressen. Die Clients im lokalen Netzwerk erhalten eine IP-Adresse vom ICS-DHCP-Server.
    * D) ICS erfordert die manuelle Konfiguration von DNS- und Gateway-Adressen auf dem Client-Gerät.
        * *Hinweis*: Durch den integrierten DHCP-Server werden diese Einstellungen automatisch an die Clients vergeben.
    * **E) Durch die ICS/Firewall-API haben auch Antivirenprogramme Zugriff auf die Netzwerkübertragungen und bieten zusätzlichen Schutz.**
        * *Hinweis*: Das stimmt. Die ICS-API ermöglicht es Antivirenprogrammen, Netzwerkübertragungen zu überwachen und zusätzlichen Schutz zu bieten.

---

### Fragen zur Netzwerkkonfiguration und Problemlösung

3.  **Welcher Konfigurationsschritt ist bei der manuellen Netzwerkkonfiguration eines Geräts, das ICS nutzt, typischerweise NICHT erforderlich, da er automatisch vom ICS-System übernommen wird?**
    * A) Die IP-Adresse des Geräts.
        * *Hinweis*: Bei einer manuellen Konfiguration ist die IP-Adresse des Geräts immer erforderlich.
    * B) Die Subnetzmaske.
        * *Hinweis*: Die Subnetzmaske ist ein wesentlicher Bestandteil der manuellen Netzwerkkonfiguration.
    * C) Die MAC-Adresse des Geräts.
        * *Hinweis*: Die MAC-Adresse ist eine Hardware-Adresse und wird nicht konfiguriert.
    * **D) Die DNS- und Gateway-Einstellungen.**
        * *Hinweis*: Wenn Sie DHCP verwenden, werden diese Einstellungen automatisch vom ICS-Server zugewiesen. Bei einer manuellen Konfiguration sind diese Informationen entscheidend.

4.  **Warum trat im Experiment eine Fehlermeldung bei der Systemaktualisierung auf, die auf eine Zeit-Synchronisierung zurückzuführen war?**
    * A) Die DNS-Namensauflösung war fehlerhaft konfiguriert.
        * *Hinweis*: Wenn die DNS-Auflösung fehlerhaft wäre, könnten die Paket-Repositorys nicht gefunden werden. Dies war aber nicht die Ursache des Fehlers.
    * B) Der verwendete USB-Netzwerkadapter unterstützte keine Zeitprotokolle.
        * *Hinweis*: Der Adapter hat die Netzwerkverbindung bereitgestellt. Das Protokoll wird durch die Software implementiert.
    * **C) Der NTP-Port (UDP 123) war im Hochschulnetzwerk gesperrt, was die Zeitsynchronisierung verhinderte.**
        * *Hinweis*: Die Firewall der Hochschule blockierte den für die Zeitsynchronisierung notwendigen Port, wodurch eine korrekte Zeiteinstellung verhindert wurde.
    * D) Die IP-Adresse des ICS-Adapters wurde manuell geändert.
        * *Hinweis*: Eine Änderung der IP-Adresse des ICS-Adapters könnte zu Verbindungsproblemen führen, hat aber keine direkte Auswirkung auf die Zeitsynchronisierung.

5.  **Welche Aktion war laut dem Dokument notwendig, um das Problem mit der Zeit-Synchronisierung zu beheben?**
    * A) Den Netzwerkadapter auf dem Windows-Gerät neu starten.
        * *Hinweis*: Ein Neustart des Adapters könnte vorübergehende Probleme beheben, behebt aber nicht die grundsätzliche Blockade des Ports.
    * **B) In der `timesyncd.conf` einen anderen Zeitserver konfigurieren, der erreichbar ist.**
        * *Hinweis*: Die Konfiguration eines alternativen Zeitservers, der nicht von der Firewall blockiert wird, ist der richtige Weg, um das Problem zu beheben.
    * C) Die Firewall-Regeln auf dem Windows-Gerät deaktivieren.
        * *Hinweis*: Die Firewall-Regeln waren nicht auf dem Windows-Gerät, sondern im Hochschulnetzwerk.
    * D) Die IP-Adresse manuell in der Raspberry Pi Konfiguration ändern.
        * *Hinweis*: Die IP-Adresse zu ändern, würde das Problem mit dem Zeitserver nicht beheben.

---

### Fragen zu den praktischen Aspekten

6.  **Angenommen, Sie haben Ihr PDAL über ICS mit einem Windows 11 Notebook verbunden. Sie möchten die Proxmox-Weboberfläche auf Ihrem Notebook erreichen. Welche IP-Adresse müssen Sie in Ihrem Browser eingeben?**
    * A) `192.168.1.1`
        * *Hinweis*: Diese Adresse ist das Standard-Gateway in vielen privaten Netzwerken, nicht aber die des Proxmox-Hosts.
    * B) `192.168.137.1`
        * *Hinweis*: Dies ist die Adresse Ihres ICS-Gateways (das Windows-Notebook), nicht die des Proxmox-Servers.
    * **C) Die IP-Adresse, die Sie dem Proxmox-Host zugewiesen haben (z.B. `192.168.137.x`)**
        * *Hinweis*: Richtig. Um eine Verbindung zum Proxmox-Webinterface herzustellen, müssen Sie sich mit der IP-Adresse des Proxmox-Hosts selbst verbinden.
    * D) Die externe IP-Adresse des Windows-Notebooks.
        * *Hinweis*: Die externe IP-Adresse wird für die Kommunikation mit dem Internet verwendet, nicht für die interne Kommunikation innerhalb des ICS-Netzwerks.

7.  **Das Dokument stellt fest, dass man sich auf dem Zielsystem (z.B. Raspberry Pi) keine Sorgen um DNS- und Gateway-Einstellungen machen muss, wenn man DHCP verwendet. Warum ist dies der Fall?**
    * A) DHCP ist eine veraltete Methode, die diese Einstellungen nicht benötigt.
        * *Hinweis*: DHCP ist immer noch der Standard für die automatische Netzwerkkonfiguration.
    * **B) Der DHCP-Server, der von Windows ICS bereitgestellt wird, vergibt diese Informationen automatisch an das Client-Gerät.**
        * *Hinweis*: Das ist der Kern der DHCP-Funktion: Der Server teilt die Netzwerk-Konfigurationsdetails, um eine Verbindung zu ermöglichen.
    * C) Das Zielsystem greift direkt auf die DNS-Server des öffentlichen Internets zu.
        * *Hinweis*: Ohne ein Gateway und die DNS-Informationen, die vom DHCP-Server zugewiesen werden, kann das Zielsystem keine Verbindung zum Internet herstellen.
    * D) Diese Einstellungen sind nur für ausgehenden, nicht aber für eingehenden Traffic relevant.
        * *Hinweis*: Diese Einstellungen sind für jeglichen Traffic von Bedeutung, der außerhalb des lokalen Netzwerks geroutet werden muss.

---

### Lizenz
Dieses Werk ist lizenziert unter der **Creative Commons - Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz**.
 
[Zum Lizenztext auf der Creative Commons Webseite](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)