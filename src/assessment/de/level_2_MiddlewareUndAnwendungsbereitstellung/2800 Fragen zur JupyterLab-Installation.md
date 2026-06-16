---
title: "Fragen zur JupyterLab-Installation"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "pdal@jade-hs.de"
organization: "PDAL-Projekt"
date: "2025-11-07"
version: "1.0.0"
level: "Ebene 2, Lerneinheit 2.8, Assessment"
duration: "0,2 Std"
prerequisites: ["Abgeschlossen - 2800 Jupyterlab im LXC-Container installieren & konfigurieren"]
tags: ["PDAL","Assessment", "JupyterLab", "Funktionsprüfung"]
license: "CC BY-SA 4.0"
---

## 📝 True-/False-Checkliste: JupyterLab Installationsprüfung

### 1. Python + Pip + venv installieren

**Frage:** Nach erfolgreicher Basiskonfiguration sind Python 3, der Paketmanager Pip und das Modul zur Erstellung virtueller Umgebungen (`python3-venv`) auf dem Container verfügbar.
* **true**
    * Hinweis: Dies ist der erwartete Zustand nach Schritt 2 (`sudo apt install python3 python3-pip python3-venv -y`). Alle drei Komponenten müssen für die weiteren Schritte installiert sein.
* **false**
    * Hinweis: Bei Misserfolg prüfen Sie den `apt install`-Befehl und stellen Sie sicher, dass alle drei Pakete installiert wurden.

---

### 2. Erstellen venv

**Frage:** Nachdem der Befehl `python3 -m venv ~/jupyterlab/venv` ausgeführt wurde, existiert im Zielverzeichnis ein isolierter Python-Interpreter, der vom System getrennt ist.
* **true**
    * Hinweis: Dies ist das Ziel von `python3 -m venv`: die Erstellung einer unabhängigen Arbeitsumgebung (Schritt 3.1).
* **false**
    * Hinweis: Überprüfen Sie das Verzeichnis `~/jupyterlab/venv/bin` auf die Existenz eines lokalen `python`-Interpreters.

---

### 3. Aktivieren venv

**Frage:** Die virtuelle Umgebung ist erfolgreich aktiviert, was sich im Terminal daran erkennen lässt, dass der Shell-Prompt die Kennzeichnung `(venv)` anzeigt und `pip install` nur innerhalb dieser Umgebung ausgeführt wird.
* **true**
    * Hinweis: Die Kennzeichnung `(venv)` bestätigt die erfolgreiche Aktivierung (Schritt 3.2).
* **false**
    * Hinweis: Prüfen Sie, ob Sie `source ~/jupyterlab/venv/bin/activate` ausgeführt haben.

---

### 4. Installation JupyterLab

**Frage:** Die Installation von JupyterLab mittels `pip install jupyterlab` innerhalb der aktivierten venv hat eine isolierte, funktionsfähige JupyterLab-Instanz erzeugt.
* **true**
    * Hinweis: Die Verwendung von `pip` in der `venv` ist die Best Practice für eine isolierte Installation (Schritt 3.4).
* **false**
    * Hinweis: Prüfen Sie die Pip-Ausgabe auf Fehler und vergewissern Sie sich, dass `jupyter-lab` nun unter `~/jupyterlab/venv/bin/` liegt.

---

### 5. Passwort setzen

**Frage:** Nach dem Setzen des Passworts mit `jupyter-lab password` wird beim nächsten Start von JupyterLab im Browser eine Anmeldemaske zur Authentifizierung angezeigt.
* **true**
    * Hinweis: Die Anmeldemaske signalisiert den erfolgreich aktivierten Passwortschutz (Schritt 5).
* **false**
    * Hinweis: Überprüfen Sie, ob die Datei `~/.jupyter/jupyter_server_config.json` mit einem Passwort-Hash existiert.

---

### 6. Jupyter manuell starten und im Browser aufrufen

**Frage:** Nach dem manuellen Start von JupyterLab mit `--ip=0.0.0.0` ist der Dienst über die IP-Adresse des Containers und Port 8888 im Client-Browser erreichbar.
* **true**
    * Hinweis: `--ip=0.0.0.0` erlaubt den Zugriff von außerhalb des Containers, und die URL muss `http://<IP>:8888` sein (Schritt 6).
* **false**
    * Hinweis: Prüfen Sie die Firewall-Einstellungen (falls vorhanden) und stellen Sie sicher, dass der Port 8888 geöffnet ist oder der Server korrekt läuft (mit `strg` + `c` kann er beendet werden).

---

### 7. Erstellen System-Dienst

**Frage:** Nach dem Aktivieren und Starten des systemd-Dienstes wird JupyterLab automatisch beim Systemstart als Hintergrunddienst gestartet und bleibt ohne manuelle Terminal-Sitzung aktiv.
* **true**
    * Hinweis: Dies ist der Zweck der systemd-Konfiguration. Der Status kann mit `sudo systemctl status jupyterlab` oder `journalctl -u jupyterlab -f` geprüft werden (Schritt 7).
* **false**
    * Hinweis: Prüfen Sie die systemd-Datei auf Syntaxfehler, führen Sie `daemon-reload` aus und starten Sie den Dienst.

---

### 8. Java-Kernel installieren und aufrufen

**Frage:** Nach der benutzerdefinierten Installation des IJava-Kernels steht der Java-Kernel im JupyterLab-Launcher zur Erstellung eines neuen Notebooks zur Verfügung.
* **true**
    * Hinweis: Die Sichtbarkeit des Java-Kernels im Launcher oder eine erfolgreiche Listung via `jupyter kernelspec list` bestätigt die korrekte Installation (Schritt 8).
* **false**
    * Hinweis: Überprüfen Sie, ob das `install.py`-Skript mit dem korrekten `python3` aus der Venv ausgeführt wurde (`~/jupyterlab/venv/bin/python3 install.py --user`).

---

## Lizenz

Dieses Werk ist lizenziert unter der **Creative Commons Namensnennung - Nicht-kommerziell - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz**.

[Zum Lizenztext auf der Creative Commons Webseite](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.de)