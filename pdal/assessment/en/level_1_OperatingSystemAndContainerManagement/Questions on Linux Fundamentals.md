---
title: "Questions on Linux Fundamentals"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "uwe.bachmann@jade-hs.de"
organization: "PDAL-Projekt"
date: "2025-08-19"
version: "1.0.0"
level: "Level 1, Learning Unit 1.2, Assessment"
duration: "0.2 hours"
prerequisites:["Completed - Document: 1200 - Basics of Linux Shell Navigation and System Commands"]
tags: ["PDAL","Assessment"]
license: "CC BY-SA 4.0"
---

### Multiple-Choice Questions on Linux Command Fundamentals

**1. Which command displays the current working directory?**
* A) `ls -l`
    * Hint: This command lists the contents of a directory in long format.
* B) `cd ..`
    * Hint: This command changes to the parent directory.
* **C) `pwd`**
    * Hint: The document describes `pwd` as the command that "shows the path of the current working directory."
* D) `mkdir`
    * Hint: This command is used to create a new directory.
* E) `man`
    * Hint: This command displays the official help page for a command.

**2. What does the `-r` option do in the `rm` and `cp` commands?**
* A) It prompts for confirmation before deleting or overwriting.
    * Hint: The `-i` option is used for this.
* B) It lists directories recursively.
    * Hint: This is a function of the `ls` command with the `-R` option.
* **C) It allows recursive deletion or copying of directories and their contents.**
    * Hint: The document explains the `-r` option for `rm` to delete directories and for `cp` to copy directories recursively.
* D) It's only for deleting files, not for copying.
    * Hint: The `-r` option works for both commands.
* E) It deletes or copies files in read-only mode.
    * Hint: This is not a function of the `-r` option.

**3. Which command is recommended to safely edit the `/etc/sudoers` file?**
* A) `nano /etc/sudoers`
    * Hint: Editing with a normal editor is not recommended, as a typo can render the system unusable.
* **B) `visudo`**
    * Hint: The document dedicates a specific section to the use of `visudo` and emphasizes that it checks the syntax to prevent errors that could make the system unusable.
* C) `vim /etc/sudoers`
    * Hint: Editing with a normal editor like `vim` is not recommended, as a typo can render the system unusable.
* D) `sudoers --edit`
    * Hint: This command does not exist in this form.
* E) `gedit /etc/sudoers`
    * Hint: Editing with a normal editor like `gedit` is not recommended, as a typo can render the system unusable.

**4. According to the documentation, what is the purpose of the command `ping 8.8.8.8`?**
* A) It tests the connection to the local router (gateway).
    * Hint: To do this, you would ping the gateway's IP (e.g., `192.168.137.1`).
* B) It tests name resolution (DNS).
    * Hint: To do this, you would ping a domain like `heise.de`.
* **C) It checks if a connection to the internet exists.**
    * Hint: The section on `ping` explicitly states that pinging an external IP like `8.8.8.8` tests "whether a connection to the internet exists."
* D) It clears the system's DNS cache.
    * Hint: This is not a function of `ping`.
* E) It resets the network interface.
    * Hint: This is not a function of `ping`.

**5. What is the main function of the `Kernel` in the Linux operating system?**
* A) It serves as the interface between the user and the system.
    * Hint: This is the function of the shell.
* B) It manages configuration files.
    * Hint: Configuration files are located in `/etc`.
* **C) It is the core of the system and controls hardware access and processes.**
    * Hint: In the "What is Linux?" section, the Kernel is described as the "core of the system" that controls "hardware access and processes."
* D) It is a collection of fundamental system programs.
    * Hint: These are the GNU tools.
* E) It manages user directories.
    * Hint: User directories are stored in the `/home` directory.

**6. What is the function of the `cd -` command?**
* A) It deletes the previous directory.
    * Hint: This is not the function of the command.
* **B) It returns to the previous directory.**
    * Hint: The document explicitly lists "cd - – Return to the previous directory" under the examples for the `cd` command.
* C) It changes to the root directory (`/`).
    * Hint: The command `cd /` is used for this.
* D) It changes to the directory you were in before the last command.
    * Hint: This is the same as the correct answer.
* E) It changes to the home directory.
    * Hint: The command `cd` with no arguments is used for this.

**7. What is the difference between the `/bin` and `/sbin` directories?**
* A) `/bin` contains temporary files, `/sbin` system logs.
    * Hint: Temporary files are in `/tmp`, logs are in `/var/log`.
* B) `/bin` contains configuration files, `/sbin` user directories.
    * Hint: Configuration files are in `/etc`, user directories are in `/home`.
* **C) `/bin` contains system commands for all users, `/sbin` for administrators.**
    * Hint: The "Directory Structure" table in the document describes this exact difference.
* D) `/bin` is for user programs, `/sbin` for system services.
    * Hint: This better describes the difference between `/usr` and `/sbin`.
* E) `/bin` contains kernel files, `/sbin` bootloader files.
    * Hint: These files are located in `/boot`.

**8. Which command is used to manage the system time and time zone?**
* A) `systemctl status`
    * Hint: This command shows the status of services.
* B) `timesyncd`
    * Hint: This is the service that performs time synchronization in the background.
* C) `date`
    * Hint: This command displays the current date and time but does not manage the time zone or NTP.
* **D) `timedatectl`**
    * Hint: The document dedicates a section to this command and explains its function for managing time and date.
* E) `shutdown`
    * Hint: This command is used to shut down or restart the system.

**9. What does the `CTRL+X` key combination do in the `nano` text editor?**
* A) It saves the file.
    * Hint: `CTRL+O` is used for this.
* B) It searches for text.
    * Hint: `CTRL+W` is used for this.
* **C) It exits the editor.**
    * Hint: The section on `nano` lists "CTRL+X – Exit" as one of the most important key combinations.
* D) It cuts the selected text.
    * Hint: This is a function of other editors.
* E) It pastes text from the clipboard.
    * Hint: This is a function of other editors.

**10. If a scheduled system shutdown needs to be canceled, which command should be used?**
* A) `shutdown -h`
    * Hint: This command performs a shutdown.
* B) `shutdown now`
    * Hint: This command performs an immediate shutdown.
* **C) `shutdown -c`**
    * Hint: The "Important Options" table in the `shutdown` section lists "cancel" as the `-c` option and describes it as "Cancel a scheduled shutdown."
* D) `reboot`
    * Hint: This command restarts the system.
* E) `poweroff`
    * Hint: This command completely turns off the system.

---

### License
This work is licensed under the **Creative Commons Attribution - ShareAlike 4.0 International License**.
 
[To the license text on the Creative Commons website](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en)
