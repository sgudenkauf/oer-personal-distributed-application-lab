---
title: "Fragen zur Software-Installation und Paketverwaltung unter Linux"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "uwe.bachmann@jade-hs.de"
organization: "PDAL-Projekt"
date: "2025-08-26"
version: "1.0.0"
level: "Ebene 1, Lerneinheit 1.4, Assessment"
duration: "0,2 Std"
prerequisites:["Abgeschlossen -  Dokument: 1400 - Software-Installation und Paketverwaltung unter Linux (Debian/Ubuntu)"]
tags: ["PDAL","Assessment"]
license: "CC BY-SA 4.0"
---

### Fragen zur Software-Installation und Paketverwaltung unter Linux

**1. Was ist die Hauptfunktion des Befehls `sudo apt update`?**
* A. Er installiert alle ausstehenden System-Updates.
   * *Hinweis: Dieser Befehl aktualisiert nur die Paketlisten, nicht die installierten Pakete selbst.*
* B. Er entfernt nicht mehr benötigte Abhängigkeiten.
   * *Hinweis: Dafür ist der Befehl `sudo apt autoremove` vorgesehen.*
* **C. Er aktualisiert die Paketlisten von den Repositories.**
   * *Hinweis: Korrekt. Dieser Befehl ruft die neuesten Paketinformationen ab, damit das System weiß, welche Software verfügbar ist.*
* D. Er installiert eine neue Software.
   * *Hinweis: Dafür ist der Befehl `sudo apt install` zuständig.*
* E. Er führt ein vollständiges System-Upgrade durch, einschließlich neuer Versionen.
   * *Hinweis: Ein vollständiges Upgrade wird mit `sudo apt full-upgrade` durchgeführt.*

**2. Welcher APT-Befehl sollte immer vor der Installation neuer Software ausgeführt werden?**
* A. `sudo apt autoremove`
   * *Hinweis: Dieser Befehl wird nach der Deinstallation von Software verwendet, um Abhängigkeiten zu entfernen.*
* B. `sudo apt upgrade`
   * *Hinweis: Dieser Befehl installiert Updates, sollte aber nach `apt update` ausgeführt werden.*
* C. `sudo apt full-upgrade`
   * *Hinweis: Dies ist eine umfassendere Version von `apt upgrade` und wird nicht zwingend vor jeder Installation benötigt.*
* **D. `sudo apt update`**
   * *Hinweis: Korrekt. Um sicherzustellen, dass Sie die aktuellsten Paketinformationen haben, sollten die Paketlisten immer zuerst aktualisiert werden.*
* E. `apt search <paketname>`
   * *Hinweis: Dieser Befehl dient nur zum Suchen von Paketen, nicht zur Vorbereitung der Installation.*

**3. Was ist der Unterschied zwischen den Befehlen `sudo apt remove <paketname>` und `sudo apt purge <paketname>`?**
* A. `remove` löscht auch Konfigurationsdateien, während `purge` sie behält.
   * *Hinweis: Dies ist genau das Gegenteil der im Dokument beschriebenen Funktion.*
* B. `remove` entfernt nur die Abhängigkeiten, während `purge` das Hauptpaket entfernt.
   * *Hinweis: Beide entfernen das Hauptpaket, aber `purge` ist umfassender.*
* C. `remove` ist für grafische Pakete, `purge` für Kommandozeilen-Tools.
   * *Hinweis: Die Befehle gelten für alle Pakettypen.*
* **D. `remove` lässt Konfigurationsdateien zurück, `purge` entfernt sie.**
   * *Hinweis: Korrekt. `purge` ist der umfassendere Befehl zur vollständigen Deinstallation.*
* E. `remove` erfordert eine Internetverbindung, `purge` nicht.
   * *Hinweis: Beide Befehle benötigen eine Internetverbindung, um die Paketinformationen abzugleichen.*

**4. Welches Tool wird laut Dokument für ein Upgrade auf eine neue Ubuntu-Version (z. B. 22.04 auf 24.04) empfohlen?**
* A. `sudo apt full-upgrade`
   * *Hinweis: Dieser Befehl reicht nicht für einen vollständigen Release-Wechsel aus, er aktualisiert nur die Pakete innerhalb der aktuellen Version.*
* **B. `sudo do-release-upgrade`**
   * *Hinweis: Korrekt. Dieses spezielle Tool ist der offizielle und empfohlene Weg, um auf eine neue Ubuntu-Version zu migrieren.*
* C. `sudo apt upgrade --new-release`
   * *Hinweis: Solch eine Befehlssyntax existiert für diesen Zweck nicht.*
* D. Die Einträge in der `/etc/apt/sources.list` manuell ändern.
   * *Hinweis: Das Dokument bezeichnet diese Methode als fehleranfällig und empfiehlt sie nur für erfahrene Admins.*
* E. Ein Skript verwenden, das die APT-Repositories ändert.
   * *Hinweis: Das ist eine manuelle, fehleranfällige Methode, die dem `do-release-upgrade`-Assistenten nicht überlegen ist.*

**5. Was ist die Hauptfunktion des Befehls `sudo apt autoremove`?**
* A. Er löscht alle heruntergeladenen Paketdateien aus dem Cache.
   * *Hinweis: Dies würde ein Befehl wie `sudo apt clean` tun.*
* **B. Er entfernt automatisch nicht mehr benötigte Abhängigkeiten.**
   * *Hinweis: Korrekt. Der Befehl räumt das System auf, indem er Pakete entfernt, die von keiner anderen installierten Software mehr benötigt werden.*
* C. Er entfernt alle Konfigurationsdateien nach der Deinstallation.
   * *Hinweis: Dafür wird `apt purge` verwendet.*
* D. Er sucht nach installierten Paketen, die neuere Versionen benötigen.
   * *Hinweis: Das ist die Funktion von `apt update`.*
* E. Er löscht ein Paket und seine Konfigurationsdateien in einem Schritt.
   * *Hinweis: Das ist die Funktion von `apt purge`.*

**6. Was ist der entscheidende Unterschied bei der Software-Installation zwischen Linux und Windows, der im Dokument hervorgehoben wird?**
* A. Linux verwendet eine Kommandozeile, Windows eine grafische Oberfläche.
   * *Hinweis: Dies ist ein Unterschied in der Bedienung, aber nicht der entscheidende Punkt laut Text.*
* B. Linux nutzt APT, während Windows den Microsoft Store verwendet.
   * *Hinweis: APT ist zwar ein Unterschied, aber nicht der wichtigste, der im Dokument erwähnt wird.*
* **C. Linux hat keinen automatischen Update-Dienst, der das System ohne Benutzerinteraktion aktualisiert.**
   * *Hinweis: Korrekt. Das Dokument betont, dass Updates in Linux manuell angestoßen werden müssen, im Gegensatz zur Automatisierung in Windows.*
* D. Linux-Installationen sind immer sicherer als Windows-Installationen.
   * *Hinweis: Das Dokument erwähnt, dass APT-Installationen sicherer sind, aber macht keine allgemeine Aussage über die Sicherheit der beiden Betriebssysteme.*
* E. Linux-Software kann nicht deinstalliert werden, wenn man die Konfigurationsdateien behalten möchte.
   * *Hinweis: Das Dokument zeigt, dass `apt remove` genau diese Funktion bietet.*

**7. Welchen Nachteil hat die manuelle Installation von Software mit `wget` im Vergleich zur Installation über APT?**
* **A. Es ist nicht möglich, Abhängigkeiten automatisch mit zu installieren.**
   * *Hinweis: Korrekt. APT löst Abhängigkeiten automatisch auf, während dies bei der manuellen Installation nicht der Fall ist.*
* B. `wget` kann keine Dateien aus dem Internet herunterladen.
   * *Hinweis: Dies ist die Hauptfunktion von `wget`.*
* C. Es kann nur eine Datei gleichzeitig heruntergeladen werden.
   * *Hinweis: Mit der Option `-i` kann `wget` auch mehrere Dateien herunterladen.*
* D. `wget` ist in den meisten Distributionen nicht standardmäßig installiert.
   * *Hinweis: Obwohl `wget` nicht immer vorinstalliert ist, ist dies nicht der Hauptnachteil im Vergleich zu APT.*
* E. Man muss sich immer im richtigen Verzeichnis befinden, um die Datei herunterzuladen.
   * *Hinweis: Es ist möglich, den Zielpfad mit der Option `-P` anzugeben.*

**8. Welchen Zweck erfüllt der Befehl `apt show <paketname>`?**
* A. Er startet eine grafische Benutzeroberfläche zur Paketverwaltung.
   * *Hinweis: Dieser Befehl ist für die Kommandozeile.*
* B. Er zeigt an, ob das Paket bereits installiert ist.
   * *Hinweis: Obwohl dies eine Information sein kann, ist es nicht der Hauptzweck.*
* C. Er entfernt das Paket vom System.
   * *Hinweis: Dafür wird `apt remove` oder `apt purge` verwendet.*
* **D. Er liefert detaillierte Informationen über ein Paket, wie Version und Abhängigkeiten.**
   * *Hinweis: Korrekt. Der Befehl ist ideal, um vor einer Installation oder einem Upgrade mehr über ein Paket zu erfahren.*
* E. Er sucht nach ähnlichen Paketen im Repository.
   * *Hinweis: Dafür ist der Befehl `apt search` zuständig.*

**9. Was muss laut Dokument nach einem Kernel-Update getan werden, um sicherzustellen, dass alle Änderungen wirksam werden?**
* A. Die Paketlisten mit `sudo apt update` aktualisieren.
   * *Hinweis: Dies ist nur der erste Schritt bei der Aktualisierung von Paketen.*
* B. `sudo apt autoremove` ausführen.
   * *Hinweis: Dies entfernt verwaiste Abhängigkeiten, hat aber keinen direkten Einfluss auf die Aktivierung des neuen Kernels.*
* C. Den Computer ausschalten und wieder einschalten.
   * *Hinweis: Dies ist zwar eine Möglichkeit, aber der spezifische Befehl ist ein Neustart.*
* **D. Das System mit `sudo reboot` neu starten.**
   * *Hinweis: Korrekt. Ein Neustart ist erforderlich, damit das System den neuen Kernel lädt und verwendet.*
* E. Nichts, das System lädt den neuen Kernel automatisch beim nächsten Start.
   * *Hinweis: Der Neustart muss explizit angestoßen werden.*

**10. Was geschieht, wenn Sie ein Paket mit `sudo apt remove` entfernen?**
* A. Das Paket wird vollständig gelöscht, einschließlich seiner Konfigurationsdateien.
   * *Hinweis: Dies ist die Funktion von `sudo apt purge`.*
* B. Es wird nur die Programmdatei entfernt, alle Bibliotheken bleiben erhalten.
   * *Hinweis: Die zugehörigen Bibliotheken werden als Abhängigkeiten behandelt.*
* C. Nur die Konfigurationsdateien werden gelöscht.
   * *Hinweis: `remove` behält die Konfigurationsdateien.*
* D. Die Deinstallation schlägt fehl, wenn noch Abhängigkeiten vorhanden sind.
   * *Hinweis: Der Paketmanager kann das Paket entfernen, aber die Abhängigkeiten bleiben zurück und können später mit `autoremove` entfernt werden.*
* **E. Das Paket wird entfernt, aber seine Konfigurationsdateien bleiben auf dem System.**
   * *Hinweis: Korrekt. Dies ist praktisch, wenn das Paket später neu installiert werden soll und die alten Einstellungen beibehalten werden sollen.*

---

### Lizenz
Dieses Werk ist lizenziert unter der **Creative Commons - Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz**.
 
[Zum Lizenztext auf der Creative Commons Webseite](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)


