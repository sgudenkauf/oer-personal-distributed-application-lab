---
title: "JupyterLab Installation Questions"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "uwe.bachmann@jade-hs.de"
organization: "PDAL-Project"
date: "2025-11-07"
version: "1.0.0"
level: "Level 2, Learning Unit 2.8, Assessment"
duration: "0.2 hours"
prerequisites: ["Completed - 2800 Install & Configure JupyterLab in LXC Container"]
tags: ["PDAL","Assessment", "JupyterLab", "Function Check"]
license: "CC BY-SA 4.0"
---

## 📝 True/False Checklist: JupyterLab Installation Verification

### 1. Install Python + Pip + venv

**Question:** Following successful base configuration, Python 3, the Pip package manager, and the module for creating virtual environments (`python3-venv`) are available on the container.
* **true**
    * Note: This is the expected state after Step 2 (`sudo apt install python3 python3-pip python3-venv -y`). All three components must be installed for the subsequent steps.
* **false**
    * Note: In case of failure, check the `apt install` command and ensure all three packages were installed.

---

### 2. Create venv

**Question:** After executing the command `python3 -m venv ~/jupyterlab/venv`, an isolated Python interpreter, separate from the system, exists in the target directory.
* **true**
    * Note: This is the goal of `python3 -m venv`: creating an independent working environment (Step 3.1).
* **false**
    * Note: Check the `~/jupyterlab/venv/bin` directory for the existence of a local `python` interpreter.

---

### 3. Activate venv

**Question:** The virtual environment is successfully activated, which is indicated in the terminal by the prompt showing the identifier `(venv)` and `pip install` commands only being executed within this environment.
* **true**
    * Note: The `(venv)` identifier confirms successful activation (Step 3.2).
* **false**
    * Note: Check if you have executed `source ~/jupyterlab/venv/bin/activate`.

---

### 4. Install JupyterLab

**Question:** Installing JupyterLab using `pip install jupyterlab` within the activated venv has created an isolated, functional JupyterLab instance.
* **true**
    * Note: Using `pip` within the `venv` is the best practice for an isolated installation (Step 3.4).
* **false**
    * Note: Check the Pip output for errors and verify that `jupyter-lab` is now located under `~/jupyterlab/venv/bin/`.

---

### 5. Set Password

**Question:** After setting the password with `jupyter-lab password`, a login mask is displayed in the browser the next time JupyterLab is started, prompting for authentication.
* **true**
    * Note: The login mask signals the successfully activated password protection (Step 5).
* **false**
    * Note: Check if the file `~/.jupyter/jupyter_server_config.json` containing a password hash exists.

---

### 6. Manually Start Jupyter and Access in Browser

**Question:** After manually starting JupyterLab with `--ip=0.0.0.0`, the service is reachable via the container's IP address and Port 8888 in the client browser.
* **true**
    * Note: `--ip=0.0.0.0` allows access from outside the container, and the URL must be `http://<IP>:8888` (Step 6).
* **false**
    * Note: Check firewall settings (if any) and ensure that Port 8888 is open or that the server is running correctly (it can be stopped with `Ctrl` + `c`).

---

### 7. Create System Service

**Question:** After activating and starting the systemd service, JupyterLab automatically starts as a background service upon system boot and remains active without a manual terminal session.
* **true**
    * Note: This is the purpose of the systemd configuration. The status can be checked with `sudo systemctl status jupyterlab` or `journalctl -u jupyterlab -f` (Step 7).
* **false**
    * Note: Check the systemd file for syntax errors, execute `daemon-reload`, and start the service.

---

### 8. Install and Call Java Kernel

**Question:** Following the custom installation of the IJava kernel, the Java kernel is available in the JupyterLab Launcher for creating a new notebook.
* **true**
    * Note: The visibility of the Java kernel in the Launcher or a successful listing via `jupyter kernelspec list` confirms the correct installation (Step 8).
* **false**
    * Note: Verify that the `install.py` script was executed with the correct `python3` from the Venv (`~/jupyterlab/venv/bin/python3 install.py --user`).

---

## License

This work is licensed under the **Creative Commons Attribution - Non-Commercial - Share Alike 4.0 International License**.

[Link to the license text on the Creative Commons website](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)