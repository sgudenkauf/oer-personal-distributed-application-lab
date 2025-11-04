---
title: "Kompetenzbewertung im PDAL: Ein hybrider Leitfaden für Lehrende"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe"]
email: "uwe.bachmann@jade-hs.de"
organization: "PDAL-Projekt"
date: "2025-08-11"
version: "1.0.0"
level: "Instructor guide"
duration: "N/a"
prerequisites:["none"]
tags: ["PDAL", "Didaktik", "Instructur Guide", "Assessment"]
license: "CC BY-SA 4.0"
---
# Kompetenzbewertung im PDAL: Ein hybrider Leitfaden für Lehrende

Das Personal Distributed Applications Lab (PDAL) ermöglicht den Lernenden, im eigenen Tempo tiefgreifende praktische Erfahrungen zu sammeln. Als Lehrende stehen Sie vor der Herausforderung, diese individuellen Lernerfolge und vor allem die **Entwicklung von Kompetenzen** in Bereichen wie Problemlösung und Systemverständnis nachvollziehbar zu beurteilen.

Dieses Dokument bietet Ihnen hierfür einen umfassenden Leitfaden. Es stellt ein hybrides Bewertungsmodell vor, das auf drei Säulen ruht: der Überprüfung des Fachwissens, der Demonstration praktischer Kompetenzen und der Förderung der kritischen Reflexion. Mit diesem Ansatz können Sie nicht nur feststellen, was die Lernenden wissen, sondern auch wie sie dieses Wissen anwenden und aus ihren Fehlern lernen – essenzielle Fähigkeiten für die moderne IT-Praxis.

### Bewertung und Feedback im PDAL: Ein umfassender Ansatz

Dieses Dokument erläutert ein dreiteiliges Bewertungsmodell, das speziell für das Personal Distributed Applications Lab (PDAL) entwickelt wurde. Ziel ist es, den Lernfortschritt ganzheitlich zu erfassen, indem wir theoretisches Wissen, praktische Anwendungsfähigkeiten und die Fähigkeit zur kritischen Reflexion bewerten.

---

### Teil 1: Wissensüberprüfung (Multiple-Choice-Tests)

Dieses Format dient als Fundament, um schnell und objektiv das Verständnis der Lernenden für grundlegende Konzepte und Fakten zu überprüfen.

* **Zweck:** Messung der Kenntnis theoretischer Grundlagen und Terminologie aus den Modulen.
* **Umsetzung:**Zu jeder Kompetenzebene (0 bis 4) werden kurze Tests erstellt. Die Fragen sollten sich auf Kernbegriffe wie "Bare-Metal-Hypervisor", "LXC-Isolation" oder "REST-API-Methoden" konzentrieren.
* **Vorteil für Lernende:** Sofortiges Feedback und die Möglichkeit, Wissenslücken gezielt zu erkennen und zu schließen.
* **Feedback:** Geben Sie bei falschen Antworten eine prägnante, korrigierende Erklärung.


Die Multiple-Choice-Tests liegen als Markdown-Dokument und als H5P-Modul vor. 
H5P ist mit dem LUMI-Editor (https://lumi.education/en/lumi-h5p-offline-desktop-editor/) geschrieben und können direkt verwendet werden. 

---

### Teil 2: Praktische Anwendung (PDAL-Szenario-Challenge)

Dies ist das Herzstück der Bewertung, das die wahre Kompetenz der Lernenden misst: die Fähigkeit, ihr Wissen in einer realen, problemlösenden Umgebung anzuwenden. Anstatt nur Antworten zu liefern, müssen die Lernenden eine Aufgabe in ihrem eigenen PDAL durchführen und das Ergebnis dokumentieren.

* **Zweck:** Bewertung der praktischen Fähigkeiten, der Problemlösungskompetenz und der Fähigkeit zur Dokumentation.
* **Umsetzung:** Für jede Lernebene gibt es konkrete "Challenges". Die Aufgaben sollen die Lernenden dazu bringen, komplexe Szenarien wie die Konfiguration einer gesicherten Netzwerkkommunikation oder das Debuggen eines Dienstausfalls zu meistern. 
* **Beispiel-Challenge:**
    * **Aufgabe:** "Richten Sie einen MQTT-Broker in Container A und einen Client in Container B ein. Konfigurieren Sie den Broker so, dass die Kommunikation nur über TLS-Verschlüsselung mit selbstsignierten Zertifikaten möglich ist. Der Client in Container B muss eine Nachricht erfolgreich an den Broker senden."
    * **Bewertung:** Überprüfen Sie die Funktionalität des Setups und die Qualität der Dokumentation. Kriterien sind hierbei die korrekte Konfiguration, die logische Abfolge der Schritte und die Klarheit der Beschreibung.
* **Vorteil für Lernende:** Sie demonstrieren nicht nur ihr Wissen, sondern auch die Fähigkeit, es in komplexen Situationen anzuwenden.

---

### Teil 3: Reflexion (Lessons Learned)

Dieses Format fördert die metakognitiven Fähigkeiten – die Fähigkeit, über den eigenen Lernprozess nachzudenken. Die Lernenden reflektieren ihre Herausforderungen, Lösungsansätze und wichtigsten Erkenntnisse.

* **Zweck:** Förderung der kritischen Reflexion und des tieferen Verständnisses.
* **Umsetzung:** Bitten Sie die Lernenden, nach Abschluss einer Challenge oder einer Lerneinheit einen kurzen Bericht in Markdown-Format zu verfassen. Dieser Bericht sollte strukturierte Abschnitte wie "Problemstellung", "Hindernisse", "Lösungsweg" und "Wichtigste Erkenntnis" enthalten. 
* **Vorteil für Lernende:** Sie verinnerlichen die gelernten Inhalte, indem sie ihre Erfahrungen aktiv verarbeiten und formulieren.
* **Community-Beitrag:** Diese Berichte können anonymisiert und gesammelt werden, um eine wertvolle Wissensdatenbank für zukünftige Lernende aufzubauen.

---

### Empfehlung für Lehrende

Kombinieren Sie diese Formate flexibel. Nutzen Sie die Multiple-Choice-Tests für eine schnelle Wissensüberprüfung am Beginn eines Moduls. Setzen Sie die PDAL-Szenario-Challenges ein, um die praktischen Fähigkeiten zu bewerten. Verwenden Sie die Lessons-Learned-Berichte als Abschluss jeder Challenge, um die Reflexion zu fördern. Dieser hybride Ansatz bietet eine robuste Grundlage für eine faire, umfassende und lehrreiche Bewertung.

---

### Lizenz
Dieses Werk ist lizenziert unter der **Creative Commons - Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz**.
 
[Zum Lizenztext auf der Creative Commons Webseite](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)
