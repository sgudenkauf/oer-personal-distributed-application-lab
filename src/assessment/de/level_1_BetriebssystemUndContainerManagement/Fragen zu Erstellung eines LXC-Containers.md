---
title: "Multiple-Choice-Fragen zur Erstellung eines LXC-Containers"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe"]
email: "pdal@jade-hs.de"
organization: "PDAL-Projekt"
date: "2025-08-21"
version: "1.0.0"
level: "Ebene 1, Lerneinheit 1.1, Assessment"
duration: "0,2 Std"
prerequisites:["Abgeschlossen -  Dokument: 1150 - Erstellung eines LXC-Containers"]
tags: ["PDAL","Assessment"]
license: "CC BY-SA 4.0"
---

### Multiple-Choice-Fragen zur Erstellung eines LXC-Containers

1.  **Was ist der Unterschied zwischen einem LXC-Container und einer vollwertigen VM (Virtuellen Maschine)?**
    * A) Ein LXC-Container hat ein eigenen Kernel, während eine VM den Kernel des Hosts nutzt.
        * Hinweis: Dies ist die falsche Aussage. Der Hauptunterschied ist, dass der Container den Kernel des Hosts nutzt.
    * B) Eine VM teilt sich alle Ressourcen mit dem Host, während ein LXC-Container isolierte Ressourcen hat.
        * Hinweis: Dies ist ebenfalls die falsche Aussage. Container teilen sich den Kernel und Bibliotheken.
    * **C) Ein LXC-Container ist eine leichtgewichtige Virtualisierung, die den Kernel des Hostsystems nutzt, während eine VM ein vollständiges Betriebssystem mit eigenem Kernel virtualisiert.**
        * Hinweis: Dies ist die korrekte Aussage. LXC bietet eine Betriebssystem-Virtualisierung, die effizienter ist als die Hardware-Virtualisierung einer VM.
    * D) LXC-Container können nur Linux-Distributionen ausführen, während VMs nur Windows-Systeme ausführen können.
        * Hinweis: LXC kann nur Linux-Systeme ausführen, aber VMs können fast jedes Betriebssystem hosten.
    * E) LXC-Container sind nur für Webserver gedacht, VMs für Datenbanken.
        * Hinweis: Beide Technologien sind für eine Vielzahl von Anwendungsfällen geeignet.

2.  **Welche der folgenden Aufgaben sollte NICHT innerhalb des LXC-Containers ausgeführt werden?**
    * A) Die Installation von Webserver-Software.
        * Hinweis: Die Installation von Anwendungen ist der Hauptzweck eines Containers.
    * B) Die Konfiguration eines neuen Benutzers mit sudo-Rechten.
        * Hinweis: Die Benutzerverwaltung ist ein typischer administrativer Schritt innerhalb des Containers.
    * C) Die Ausführung eines System-Updates (`apt update && apt upgrade`).
        * Hinweis: Regelmäßige Updates sind für die Sicherheit und Funktionalität unerlässlich.
    * **D) Die Änderung der Hardware-Einstellungen wie RAM oder CPU-Kerne.**
        * Hinweis: Diese Einstellungen werden im Proxmox-Host (Hypervisor) konfiguriert, nicht innerhalb des Containers.
    * E) Die Überprüfung der Netzwerkverbindung.
        * Hinweis: Das Überprüfen der Verbindung ist ein Standard-Fehlerbehebungsschritt.

3.  **Warum wird im Dokument für die CTID und den Hostnamen `apache110` gewählt, und die IP-Adresse endet auf `.110`?**
    * A) Weil `110` die Standard-ID für LXC-Container ist.
        * Hinweis: Es gibt keine Standard-ID, Proxmox beginnt die Zählung bei 100.
    * B) Weil dies die einzigen verfügbaren Werte in Proxmox sind.
        * Hinweis: Sie können jede dreistellige CTID wählen.
    * **C) Um eine klare Zuordnung zwischen der Container-ID, dem Hostnamen und dem letzten Oktett der IP-Adresse herzustellen.**
        * Hinweis: Dies ist eine bewährte Vorgehensweise, um die Verwaltung von vielen Containern zu vereinfachen und die Übersichtlichkeit zu verbessern.
    * D) Weil diese Werte automatisch vom Template vorgegeben werden.
        * Hinweis: Die meisten dieser Werte müssen manuell eingegeben werden.
    * E) Um die Sicherheit des Containers zu erhöhen.
        * Hinweis: Die Wahl dieser Werte hat keinen Einfluss auf die Sicherheit.

4.  **Welchen Vorteil bietet die Verwendung eines "unprivileged" Containers, wie im Dokument empfohlen?**
    * A) Er ist leistungsstärker, da er mehr Hardware-Ressourcen nutzen kann.
        * Hinweis: Unprivileged Container können sogar leicht langsamer sein, da sie zusätzliche Einschränkungen haben.
    * **B) Er erhöht die Sicherheit, da Prozesse innerhalb des Containers nicht als `root` auf dem Hostsystem ausgeführt werden können.**
        * Hinweis: Dies ist der Hauptvorteil. Ein unprivilegierter Container kann keine Host-System-Privilegien erlangen, selbst wenn er kompromittiert wird.
    * C) Er benötigt weniger RAM und CPU-Kerne.
        * Hinweis: Die Ressourcenzuweisung ist unabhängig vom Privilegienstatus.
    * D) Er ermöglicht die Installation von Windows-Anwendungen.
        * Hinweis: Das ist bei LXC-Containern nicht möglich.
    * E) Er ist einfacher zu konfigurieren als ein privilegierter Container.
        * Hinweis: Beide sind ähnlich zu konfigurieren, der Hauptunterschied liegt im Sicherheitsmodell.

5.  **Warum ist es ein empfohlener Schritt, die Netzwerkkonnektivität eines neuen Containers in drei Schritten (`ping` Gateway, Google DNS, und Domain-Namen) zu überprüfen?**
    * A) Um die Geschwindigkeit der Internetverbindung zu messen.
        * Hinweis: Dies ist ein Nebeneffekt, aber nicht der Hauptzweck.
    * B) Um die Firewall-Regeln des Hosts zu testen.
        * Hinweis: Ein Ping testet die Erreichbarkeit, aber nicht die spezifischen Firewall-Regeln.
    * **C) Um die Erreichbarkeit auf verschiedenen Ebenen zu verifizieren: lokales Netzwerk, externes Netzwerk und Namensauflösung.**
        * Hinweis: Diese Methode hilft, das Problem schrittweise zu isolieren, falls die Verbindung fehlschlägt.
    * D) Um die IP-Adresse des Containers zu ändern.
        * Hinweis: Pings ändern keine Netzwerkkonfiguration.
    * E) Um eine Verbindung zum Proxmox-Webinterface herzustellen.
        * Hinweis: Das Webinterface wird vom Host bereitgestellt, nicht vom Container.

6.  **Welche Funktion erfüllt der Befehl `usermod -aG sudo pdal`?**
    * A) Er löscht den Benutzer `pdal` aus dem System.
        * Hinweis: Der Befehl zum Löschen lautet `deluser`.
    * B) Er erstellt den Benutzer `pdal` und setzt ein Passwort.
        * Hinweis: Dafür wird der Befehl `adduser` verwendet.
    * **C) Er fügt den bestehenden Benutzer `pdal` zur `sudo`-Gruppe hinzu, um ihm Administratorrechte zu geben.**
        * Hinweis: Die Option `-aG` steht für "append to group" und ist der korrekte Weg, um einem Benutzer `sudo`-Rechte zu verleihen.
    * D) Er ändert den Hostnamen des Containers.
        * Hinweis: Dafür würde man den Befehl `hostnamectl` verwenden.
    * E) Er aktualisiert alle Pakete auf dem System.
        * Hinweis: Dafür wird `apt upgrade` verwendet.

7.  **Warum wird das `timedatectl` im LXC-Container nur zur Konfiguration der Zeitzone, nicht aber zur Zeitsynchronisierung verwendet?**
    * A) Weil LXC-Container keine eigene Systemzeit haben.
        * Hinweis: Container haben eine eigene, isolierte Zeitansicht, die jedoch vom Host abhängt.
    * B) Weil `timedatectl` nur auf virtuellen Maschinen funktioniert, nicht in Containern.
        * Hinweis: Der Befehl funktioniert auch in Containern.
    * **C) Weil die Systemzeit des Containers vom Hostsystem übernommen wird und eine separate Zeitsynchronisierung nicht notwendig ist.**
        * Hinweis: Dies ist ein grundlegendes Konzept von Containern. Sie teilen den Kernel und damit auch die Systemzeit mit dem Host.
    * D) Weil Zeitsynchronisierungsdienste wie `chrony` in LXC-Containern nicht installiert werden können.
        * Hinweis: `chrony` kann installiert werden, aber es wäre redundant.
    * E) Weil `timedatectl` die Zeit aus dem Internet holt, was in einem ICS-Netzwerk nicht möglich ist.
        * Hinweis: Dies ist die falsche Annahme.

8.  **Was bedeutet das `-y` Flag in dem Befehl `apt upgrade -y`?**
    * A) Es zeigt eine Liste der zu installierenden Pakete an.
        * Hinweis: Dafür wird das `-s` oder `--simulate` Flag verwendet.
    * B) Es stoppt den Aktualisierungsprozess, wenn ein Fehler auftritt.
        * Hinweis: Dies ist nicht die Funktion des `-y` Flags.
    * **C) Es beantwortet alle Bestätigungsanfragen (Ja/Nein) automatisch mit "Ja" und führt die Aktion non-interaktiv aus.**
        * Hinweis: Das `-y` Flag ist nützlich für die Automatisierung von Skripten, um manuelle Eingaben zu vermeiden.
    * D) Es führt ein Rollback zu einer früheren Paketversion durch.
        * Hinweis: Dafür gibt es andere Befehle.
    * E) Es lädt die Paketlisten von einem anderen Repository herunter.
        * Hinweis: Dafür würde man die `/etc/apt/sources.list` bearbeiten.

9.  **Welche Rolle spielt ein Template wie `ubuntu-24.04-standard_...amd64.tar.zst` bei der Erstellung eines LXC-Containers?**
    * A) Es dient als Backup für den Container.
        * Hinweis: Templates sind keine Backups, sondern Grundinstallationen.
    * B) Es ist eine vollwertige, lauffähige VM.
        * Hinweis: Ein Template ist kein fertiges System.
    * C) Es enthält die Konfigurationsdateien für den Container.
        * Hinweis: Die Konfigurationsdateien werden bei der Erstellung des Containers generiert.
    * **D) Es ist ein minimiertes Dateisystem-Image, das die Basis für einen neuen Container bildet und die Installation beschleunigt.**
        * Hinweis: Templates enthalten nur die minimalen Dateien, die für eine funktionierende Umgebung erforderlich sind.
    * E) Es wird nur für die Installation von Anwendungen benötigt.
        * Hinweis: Es ist die Grundlage für das gesamte Betriebssystem im Container.

10. **Was ist die Funktion einer "Bridge" (`vmbr0`) im Kontext der Netzwerkkonfiguration in Proxmox?**
    * A) Sie verbindet zwei physikalische Netzwerkkarten miteinander.
        * Hinweis: Das kann eine Bridge tun, ist aber nicht ihre Hauptfunktion im Proxmox-Kontext.
    * **B) Sie agiert als virtueller Switch, der es dem Host und allen VMs/Containern ermöglicht, miteinander und mit dem physischen Netzwerk zu kommunizieren.**
        * Hinweis: Eine Bridge verbindet virtuelle und physische Netzwerkschnittstellen.
    * C) Sie ist ein virtueller Router, der den Datenverkehr zwischen Containern und dem Internet leitet.
        * Hinweis: Ein Router leitet den Verkehr zwischen verschiedenen Netzwerken, eine Bridge verbindet sie auf der gleichen Ebene.
    * D) Sie dient als Firewall, um den Container vor Angriffen zu schützen.
        * Hinweis: Die Firewall-Funktion ist separat konfigurierbar.
    * E) Sie ist eine reine Software-Funktion ohne Verbindung zur physischen Hardware.
        * Hinweis: Sie verbindet das virtuelle Netzwerk mit der physischen Netzwerkschnittstelle des Hosts.

--- 

### Lizenz
Dieses Werk ist lizenziert unter der **Creative Commons - Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz**.
 
[Zum Lizenztext auf der Creative Commons Webseite](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)
