

### Markdown Style Guide für PDAL

Dieser Style Guide soll sicherstellen, dass alle Dokumente des PDAL einheitlich formatiert sind und die notwendigen Informationen enthalten.

#### 1\. Metadaten (Dokumenteninformation)

Jedes Dokument muss am Anfang einen **YAML-Frontmatter-Block** enthalten. Dieser Block wird von vielen Markdown-Renderern (wie Hugo, Jekyll oder Pandoc) automatisch erkannt und verarbeitet.

```markdown
---
title: "Titel der Lerneinheit"
author: ["Name des Autors", "Name des Co-Authors"]
mail: "uwe.bachmann@jade-hs.de"
organization: "z.B. PDAL-Projekt, Jade Hochschule"
date: "YYYY-MM-DD"
version: "1.0.0"
level: "Ebene 0, Lerneinheit 0.1"
duration: "Geschätzte Dauer (z.B. 1-2 Stunden)"
prerequisites: "Voraussetzungen (z.B. Abgeschlossene Lerneinheit 0.1)"
tags: ["Proxmox", "Linux", "Virtualisierung", "Basics"]
license: "CC BY-SA 4.0"
---
```

  * **title:** Der spezifische Titel der Lerneinheit.
  * **author:** Der Name des Hauptautors oder der Autorengruppe.
  * **mail:** Kontaktaddresse für Feedback.
  * **organization:** Die Organisation, die das Modul entwickelt hat.
  * **date:** Das Erstellungs- oder letzte Änderungsdatum.
  * **version:** Die Versionsnummer des Dokuments.
  * **level:** Die Ebene und Lerneinheit im Kompetenzbaum.
  * **duration:** Die geschätzte Zeit, die benötigt wird, um die Einheit durchzuführen.
  * **prerequisites:** Eine Liste der Qualifikationen, die notwendig sind, um diese Einheit zu beginnen.
  * **tags:** Schlüsselwörter zur leichteren Auffindbarkeit.
  * **license:** Legt die Lizenz der Dokumente fest.

#### 2\. Dokumentstruktur

Jede Lerneinheit folgt einer festen Struktur, um einen konsistenten Lernablauf zu gewährleisten. Diese Struktur sollte als Hauptüberschriften (`##`) im Dokument verwendet werden.

  * **`## 1. Einleitung / These`**: Beginnt das Dokument mit einer kurzen Einführung und stellt die zentrale These oder das Lernziel der Einheit vor. Was ist das übergeordnete Thema? Warum ist es relevant?
  * **`## 2. Voraussetzung`**: Listet alle notwendigen vorhergehenden Schritte, Qualifikationen oder benötigte Materialien auf. Dies hilft dem Lernenden zu prüfen, ob er bereit ist für die Einheit.
  * **`## 3. Inhalt / Umsetzung`**: Dies ist der Hauptteil der Lerneinheit. Hier werden die praktischen Schritte, Anleitungen und Erklärungen im Detail präsentiert. Dieser Abschnitt kann mit Unterüberschriften (`###`, `####`) weiter gegliedert werden.
  * **`## 4. Zusammenfassung / Lesson Learned`**: Fasst die wichtigsten Erkenntnisse der Einheit zusammen und reflektiert, was erreicht wurde. Hier können auch weiterführende Fragestellungen zur Selbstreflexion stehen.
  * **`## 5. Literatur / Quellen`**: Listet alle verwendeten Quellen, Bücher oder hilfreichen Links auf. Dies dient nicht nur der Urheberrechtskonformität, sondern auch der Vertiefung des Wissens.

#### 3\. Überschriften

Die Überschriftenstruktur muss hierarchisch und logisch sein, um die Lesbarkeit und Navigation zu erleichtern.

  * Verwenden Sie immer nur **eine einzige H1-Überschrift (`#`)** pro Dokument für den Titel, der im Frontmatter steht.
  * Nutzen Sie `##` für die Hauptabschnitte der Lerneinheit (z.B. "Einführung", "Aufgabe", "Fazit").
  * Verwenden Sie `###` für Unterabschnitte und `####` für noch tiefere Gliederungen.
  * **Konvention:** Lassen Sie zwischen der Raute und dem Titel immer ein Leerzeichen.

#### 4\. Hervorhebungen und Formatierungen

  * **Fett:** Verwenden Sie immer **zwei Sternchen (`**Wort**`)** für fettgedruckten Text, um wichtige Begriffe oder Befehle im Fließtext hervorzuheben.
  * **Kursiv:** Verwenden Sie immer **ein Sternchen (`*Wort*`)** für kursiv gedruckten Text.
  * **Monospace/Code:** Verwenden Sie immer **Backticks (\`\`Befehl`oder`Dateiname\`)** für die Namen von Dateien, Verzeichnissen, Befehlen oder technischen Begriffen, die im Fließtext vorkommen.
  * **Code im Text:** `` ` `` für Dateinamen und Befehle.
  * **Code-Blöcke:** `` ` `` mit Sprachangabe für Shell, Python, YAML etc.
  * **Hinweise:** Nutzung von Zitatblöcken `>` für Warnungen und Tipps.

#### 5\. Code-Blöcke

Code-Blöcke müssen immer mit der **Sprachbezeichnung** versehen werden (sogenanntes "Syntax Highlighting"), damit sie leichter lesbar sind.

  * **Allgemeine Syntax:** Drei Backticks, gefolgt von der Sprache.
  * **Beispiele:**
      * Für Shell-Befehle: \`\`\`\`bash\`
      * Für Code-Beispiele: `` python`,  ``java\`
      * Für Konfigurationsdateien: `` yaml`,  ``ini\`
      * Für reine Textausgaben: \`\`\`\`text\`

#### 6\. Listen

  * **Ungeordnete Listen:** Verwenden Sie immer ein **Sternchen (`*`)** oder einen **Bindestrich (`-`)** gefolgt von einem Leerzeichen. Seien Sie in einem Dokument konsistent.
  * **Geordnete Listen:** Verwenden Sie immer **Zahlen gefolgt von einem Punkt (`1.`, `2.`, `3.`)**.

#### 7\. Hinweise und Anmerkungen

Da wir keine CSS-Boxen verwenden möchten, nutzen wir die Standard-Markdown-Syntax für Zitatblöcke, um wichtige Hinweise optisch hervorzuheben. Dies wird von den meisten Renderern mit einem grauen Balken am Rand dargestellt.

  * **Für allgemeine Hinweise:** `> **Hinweis:** Dies ist ein allgemeiner Hinweis.`
  * **Für Warnungen:** `> **Wichtig:** Eine wichtige Warnung, die beachtet werden muss!`


#### 8\. Bild- und Urheberrechtskonventionen

Um die Urheberrechtskonformität zu gewährleisten, wird festgelegt:

  * **Urheberrecht:** Es dürfen ausschließlich **selbst erstellte Bilder** verwendet werden. Screenshots, Fotos von Hardware oder selbst gezeichnete Diagramme sind zulässig.
  * **Bildbeschreibungen:** Jedes Bild muss mit der Standard-Markdown-Syntax `![Bildbeschreibung](pfad/zum/bild.jpg)` eingefügt werden. Die Bildbeschreibung muss kurz und prägnant den Inhalt des Bildes wiedergeben.


#### 9\. Literatur- / Quellenverzeichnis
  * **Quellenangaben:** Quellenangaben für verwendete Literatur, offizielle Dokumentationen oder hilfreiche Websites werden im Abschnitt `## Literatur / Quellen` gesammelt.
      * **Formatierung:** Verwenden Sie hier eine ungeordnete Liste (`-`). Jede Quelle sollte möglichst vollständig angegeben werden (z.B. Titel, Autor/Organisation, Link, Zugriffsdatum).

#### 10\. Lizenzangaben

Alle Dokumente werden mit Lizenzangaben "CC BY SA" versehen. In den Meta-Daten um maschinenlesbare Lizenzen zu übermitteln und am Ende jedes Dokumentes in folgender Art:

### Lizenz deutsch
Dieses Werk ist lizenziert unter der **Creative Commons - Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz**.


[Zum Lizenztext auf der Creative Commons Webseite](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)
```text
[Zum Lizenztext auf der Creative Commons Webseite](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)
```

### Lizenz englisch

### License
This work is licensed under the **Creative Commons Attribution - ShareAlike 4.0 International License**.
 
[To the license text on the Creative Commons website](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en)
 
´´´text 
[To the license text on the Creative Commons website](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en)
´´´ 


------------

### Das PDAL-Projekt: Struktur und Philosophie
Das PDAL ist als ein Open Educational Resource (OER)-Projekt konzipiert, das Lernende, Lehrende und das Thema Leistungskontrolle in drei klaren, voneinander getrennten Bereichen organisiert. Diese Struktur stellt sicher, dass jede Zielgruppe die für sie relevanten Informationen schnell und einfach findet, ohne von irrelevanten Inhalten abgelenkt zu werden.

Die Dokumentation ist in purem Markdown gehalten, um eine maximale Flexibilität, Langlebigkeit und die einfache Anpassung an verschiedene Plattformen und die Weiterentwicklung durch die Community zu gewährleisten.

```
/pdal-project
├── README_de.md           # Erklärung und Motivation für alle Zielgruppen
├── README_en.md           # Explanation and motivation for all target groups
│
├── /modules             # Kernmaterialien für Lernende
│   ├── /de
│   │   ├── /level_0_basics
│   │   │   ├── 0.1_hardware_setup.md
│   │   │   ├── 0.2_proxmox_install.md
│   │   │   └── ...
│   │   ├── /level_1_linux_lxc
│   │   │   ├── 1.1_first_container.md
│   │   │   └── ...
│   │   └── ...
│   └── /en
│       ├── /level_0_basics
│       │   ├── 0.1_hardware_setup.md
│       │   ├── 0.2_proxmox_install.md
│       │   └── ...
│       ├── /level_1_linux_lxc
│       │   ├── 1.1_first_container.md
│       │   └── ...
│       └── ...
│
├── /instructor_guide    # Handbuch und Ressourcen für Lehrende
│   ├── /de
│   │   ├── README.md           # Einführung und pädagogische Philosophie für Lehrende
│   │   ├── competence_tree.md    # Der vollständige Kompetenzbaum
│   │   ├── technical_setup.md    # Anleitung zur Einrichtung der Lehrumgebung
│   │   ├── assessment_and_feedback.md  # Vorschläge für Bewertung und Feedback
│   │   └── solutions             # Musterlösungen für Aufgaben
│   │       ├── level_0_basics
│   │       │   └── ...
│   │       └── ...
│   └── /en
│       ├── README.md           # Introduction and pedagogical philosophy for instructors
│       ├── competence_tree.md    # The complete competence tree
│       ├── technical_setup.md    # Guide to setting up the teaching environment
│       ├── assessment_and_feedback.md  # Suggestions for assessment and feedback
│       └── solutions             # Sample solutions for tasks
│           ├── level_0_basics
│           │   └── ...
│           └── ...
│
└── /assessment          # Freiwillige Aufgaben zur Selbstkontrolle
    ├── /de
    │   ├── /level_0_basics
    │   │   ├── 0.1_quiz.h5p
│   │   └── ...
│   │   ├── /level_1_linux_lxc
│   │   │   ├── 1.1_quiz.h5p
│   │   │   └── ...
│   │   └── ...
    └── /en
        ├── /level_0_basics
        │   ├── 0.1_quiz.h5p
        │   └── ...
        ├── /level_1_linux_lxc
        │   ├── 1.1_quiz.h5p
        │   └── ...
        └── ...
```
---

### Lizenz
Dieses Werk ist lizenziert unter der **Creative Commons - Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz**.
 
[Zum Lizenztext auf der Creative Commons Webseite](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)
 


