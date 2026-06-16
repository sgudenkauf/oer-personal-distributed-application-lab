**Autor**: RK 
**Datum:** 12.06.2025  

---

### **a. Fragestellung**

**Aufgabe**:  
Der Tiny-PC soll als Virtualisierungshost mit **Proxmox Virtual Environment (VE)** eingerichtet werden. Ziel ist es, eine funktionierende Installation von Proxmox zu erstellen, die über ein Webinterface administriert werden kann.

**Erwartetes Ergebnis**:  
Ein einsatzbereiter Proxmox VE-Host, der VMs und Container unterstützt und über das Netzwerk erreichbar ist.

---

### **b. Vorbereitung**

**Hardware**:

- **Tiny-PC**:
    
    - Prozessor: Unterstützt Virtualisierung (z. B. Intel VT-x, AMD-V)
    - RAM: Mindestens 4 GB (empfohlen: 8 GB)
    - Festplatte: Mindestens 32 GB (empfohlen: 128 GB oder mehr)
    - Netzwerkkarte: Gigabit-Ethernet
- **Peripherie**:
    
    - Monitor, Tastatur, Maus für die Installation des Tiny PCs (wird später nicht mehr benötigt)
    - Bootfähiger USB-Stick (8 GB oder größer)

**Software**:

- **Proxmox VE ISO-Image**: [Proxmox](https://www.proxmox.com/de/downloads/proxmox-virtual-environment/iso) (Version: z. B. 8.0)
- **Bootloader-Tool**: [Rufus](https://rufus.ie/de/) (Windows) oder [Balena Etcher](https://etcher.balena.io/) (Linux/MacOS)

**Set-Up**:

1. **BIOS/UEFI konfigurieren**:
    
    - Virtualisierung aktivieren (z. B. Intel VT-x oder AMD-V).
    - Secure Boot deaktivieren.
    - Bootreihenfolge so einstellen, dass der USB-Stick zuerst gestartet wird.
2. **Bootfähigen USB-Stick erstellen**:
    
    - ISO-Image mit Rufus oder Balena Etcher auf den USB-Stick schreiben.

---

### **c. Durchführung**

#### **Schritt 1: Proxmox ISO herunterladen und bootfähigen USB-Stick erstellen**

1. Rufe die Proxmox-Downloadseite auf.
2. Lade das aktuellste Proxmox VE ISO-Image herunter (z. B. `proxmox-ve_8.x.iso`).
3. Erstelle mit Rufus (Windows) oder Balena Etcher (Linux/MacOS) einen bootfähigen USB-Stick.
    - Wähle das ISO-Image und den USB-Stick aus.
    - Klicke auf "Start", um den Stick zu erstellen.

#### **Schritt 2: Proxmox Installation starten**

1. Stecke den USB-Stick in den Tiny-PC und starte ihn.
2. Wähle im Boot-Menü (meistens über `F12`, `ESC` oder `DEL`) den USB-Stick aus.
3. Im Boot-Menü von Proxmox wähle `Install Proxmox VE Terminal UI`.
---
<p style="text-align:center; color:red;">
 !!! HINWEIS !!!
</p>
<b>Im Hochschul- Netzwerk dürfen keine Server betrieben werden.
Deshalb nutzen wir im Hochschul- Netzwerk eine Netzwerk Konfiguration die mit ICS realisiert wird.
</b>

---

#### **Schritt 3: Proxmox installieren**

1. **Lizenzbedingungen akzeptieren**:
    - Lese die Lizenzbedingungen und stimme zu.
2. **Festplatte auswählen**:
    - Wähle die Festplatte für die Installation aus (alle Daten auf der Festplatte werden gelöscht).
3. **Zeitzone und Sprache einstellen**:
    - Wähle die gewünschte Zeitzone und das Tastaturlayout.
4. **Passwort und E-Mail**:
    - Lege ein starkes Root-Passwort fest.
    - Gib eine E-Mail-Adresse für Systembenachrichtigungen an.
5. **Netzwerkeinstellungen konfigurieren**:
    - Wähle `Static` .
    - Gib bei statischer IP die IP-Adresse `Netzadresse deines lokalen Netzwerkes und im letzten Oktett eine freie ip z.B. 100`, Subnetzmaske, Gateway `IP deines Routers`und DNS-Server z.B.`8.8.8.8`an.

> [!info] Warum eine statische IP-Adresse? 
> Eine statische IP-Adresse sorgt dafür, dass die VM immer dieselbe Netzwerkadresse (z. B. `192.168.1.100`) verwendet, unabhängig davon, wie oft sie gestartet oder neu verbunden wird. Dadurch ist sie für andere Geräte oder VMs immer unter derselben Adresse zu erreichen. Das ist wichtig, wenn die VM als Server (z. B. Datenbank oder Webserver) dient. 
> 
> Weitere Infos: [[04 Durchführung Statische IP für eine Ubuntu LTS VM]]

#### **Schritt 4: Installation abschließen**

1. Überprüfe die Einstellungen und klicke auf `Install`.
2. Warte, bis die Installation abgeschlossen ist (ca. 10–20 Minuten).
3. Entferne den USB-Stick und starte den Tiny-PC neu.

#### **Schritt 5: Netzwerk Connectivität prüfen**

1. Zunächst versuchen wir ein anderes Gerät im Netzwerk zu pingen
2. Wir stellen fest, das wir keinerlei Geräte im Netzwerk pingen können.

---
<p style="text-align:center; color:red;">
 !!! HINWEIS !!!
</p>
Es ist nicht zu empfehlen einen Proxmox Server über W-LAN zu betreiben.(wenn überhaupt nur in privaten Heimnetzen)<br/>

Wi-Fi-Adapter können nur über Workarounds als Linux-Bridge-Schnittstelle verwendet werden, da die meisten Access Points (APs) Frames ablehnen, deren Quelladresse nicht mit dem AP authentifiziert wurde.@WLANProxmoxVE 


### **d. Quellen**

„balenaEtcher - Flash OS Images to SD Cards & USB Drives“. Zugegriffen 11. Juni 2025. https://www.balena.io/etcher.
„Network Configuration - Proxmox VE“. Zugegriffen 6. Juni 2025. https://pve.proxmox.com/wiki/Network_Configuration#sysadmin_network_vlan.
„Proxmox VE Documentation Index“. Zugegriffen 4. Juni 2025. https://pve.proxmox.com/pve-docs/.
„Rufus - Erstellen Sie bootfähige USB-Laufwerke auf einfache Art und Weise“. Zugegriffen 11. Juni 2025. https://rufus.ie/de/.
„WLAN - Proxmox VE“. Zugegriffen 12. Juni 2025. https://pve.proxmox.com/wiki/WLAN.

- **Tiny-PC BIOS Dokumentation**: Dokumentation des Herstellers für BIOS/UEFI-Optionen.



