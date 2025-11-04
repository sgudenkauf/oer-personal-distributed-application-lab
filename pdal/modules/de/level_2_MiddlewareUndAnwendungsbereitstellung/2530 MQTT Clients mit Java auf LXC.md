---
title: "MQTT Clients mit Java auf zwei LXCs"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "uwe.bachmann@jade-hs.de"
organization: "PDAL-Projekt"
date: "2025-10-17"
version: "1.0.0"
level: "Ebene 2, Lerneinheit 2.5"
duration: "2 Std."
prerequisites: ["Abgeschlossen - 2500 MQTT auf vorhandenem LXC installieren und konfigurieren"]
tags: ["MQTT-Broker", "Mosquitto", "MQTT"]
license: "CC BY-SA 4.0"
---

# 🧪 MQTT Clients mit Java auf zwei LXCs

In diesem Dokument wird das gleiche Beispiel wie im vorherigen Beispiel "MQTT Clients mit Python auf zwei LXCs" in der Sprache Java umgesetzt. Wir müssen dafür zwei externe Bibliotheken für MQTT und JSON verwenden. 

Die Sprache Java erfordert allerdings ein anderes Vorgehen:
- zum einen verwenden wir das Build-Werkzeug "Maven". Dies erfordert ein bestimmtes Vorgehen.
- zum anderen benötigen wir eine gesonderte Klasse für unsere Messages. 

## Warum Java verwenden?

Java ist eine gute Wahl, wenn es um hohe Leistung, die Entwicklung großer, skalierbarer Unternehmensanwendungen und plattformübergreifende Kompatibilität geht. Dies gilt insbesondere für "Echt-Zeit"-Anwendungen. 
Bei nicht komplilierten Sprachen, wie z. B. Python oder PHP,  wird bei jedem Aufruf eines Scriptes das Script kompiliert. Bei Java oder C wird das Script im Vorfeld kompiliert und kann demit sofort verwendet werden. 

Sie können natürlich auch ihren Code in ihrer Java-IDE (z. B. NetBeans) schreiben und testen - ihr Clientrechner kann ja das lokale Netzwerk aufrufen. Grundsätzlich wollen wir aber die Java-Programme auf den LXC-Servern ausführen. Das benötigt ein paar Vorbereitungen.

---

**Maven** ist ein Automatisierungs- und Projektmanagement-Werkzeug für Java-Projekte. Es vereinfacht die Verwaltung von Projektabhängigkeiten (z.B. Bibliotheken wie Paho-MQTT oder Gson-JSON), die Erstellung (Build), das Testen und die Bereitstellung von Anwendungen. Kernstück ist die **pom.xml-Datei**, in der die Projektstruktur und Konfiguration deklariert wird.

**Hauptfunktionen von Maven**

- **Abhängigkeitsverwaltung:** Maven lädt automatisch externe Bibliotheken und Frameworks (wie z.B. Paho-MQTT oder Gson-JSON) aus Maven-Repositories herunter und macht sie im Projekt verfügbar. 
- **Build-Automatisierung:** Es standardisiert den Erstellungsprozess (Kompilieren, Testen, Packen in JAR/WAR-Dateien) eines Projekts. 
- **Projektmanagement:** Maven hilft bei der Erstellung der standardisierten Projektstruktur und der Verwaltung des gesamten Projektlebenszyklus. 
- **Berichterstattung:** Es kann automatisch verschiedene Berichte über den Projektstatus oder die Codequalität generieren. 
Plugins: Die Funktionalität von Maven kann durch Plugins erweitert werden, die für spezifische Aufgaben eingesetzt werden können. 

**Wichtige Konzepte von Maven**

- **Project Object Model (POM):** Die pom.xml-Datei ist das Herzstück eines Maven-Projekts. Sie enthält Metadaten wie groupId, artifactId und version, die das Projekt eindeutig identifizieren, sowie Informationen über Abhängigkeiten und den Build-Prozess. 
- **Build-Lebenszyklus:** Maven definiert standardisierte Phasen, die durchlaufen werden müssen, z.B. compile, test, package. 
- **Repositories:** Repositories (lokal, zentral oder Remote) sind Speicherorte für projektbezogene Artefakte wie Bibliotheken und sind eine Kernkomponente von Maven. Die Maven-Repositories sind nicht nur für Java verfügbar - siehe [Maven-Repositories](https://mvnrepository.com/).

---

## Java und Maven installieren

Verwenden Sie die LXC-Container des Python-Projektes oder legen sich neue LXC`s an.
Machen sie auf jeden Fall ein `apt update`.

Java installieren sie mit `apt install default-jdk` und bestätigen die Nachfrage mit `y`.
Testen sie die Installation mit den Befehlen `java -version` und `javac -version`. Der erste Befehl testet das Environment (JRE) und der zweite Befehl testet den Compiler. 

Die Ausgabe sollte etwa so aussehen:
```bash
root@mqttPubblisher:~# java -version
openjdk version "21.0.8" 2025-07-15
OpenJDK Runtime Environment (build 21.0.8+9-Ubuntu-0ubuntu124.04.1)
OpenJDK 64-Bit Server VM (build 21.0.8+9-Ubuntu-0ubuntu124.04.1, mixed mode, sharing)

root@mqttPubblisher:~# javac -version
javac 21.0.8
root@mqttPubblisher:~#
```
Notieren Sie sich die Versionsnummer; evtl. müssen sie später die `pom.xml` anpassen.

Maven installieren sie mit dem Befehl `apt install maven`.
Testen sie die Installation mit dem Befehl `mvn -version`.

Die Ausgabe sollte etwa so aussehen:
```bash
root@mqttPubblisher:~# mvn -version
Apache Maven 3.8.7
Maven home: /usr/share/maven
Java version: 21.0.8, vendor: Ubuntu, runtime: /usr/lib/jvm/java-21-openjdk-amd64
Default locale: en_US, platform encoding: UTF-8
OS name: "linux", version: "6.8.12-12-pve", arch: "amd64", family: "unix"
root@mqttPubblisher:~# 
```
Damit sind die Vorbereitungen abgeschlossen.

---

📄 **Erstellung der Maven** `pom.xml`

Um die Paho-/MQTT-Bibliothek (org.eclipse.paho.client.mqttv3, org.eclipse.paho.client.mqttv3) zu verwenden und Ihr Java-Projekt zu kompilieren und auszuführen, benötigen Sie die 'pom.xml'.

**Schritte:**

1. Erstellen Sie ein neues Verzeichnis für Ihr Projekt (z.B. java-mqtt).
2. Erstellen Sie darin die Datei pom.xml.
3. Erstellen Sie die Verzeichnisstruktur für Ihren Quellcode: src/main/java.
4. Legen Sie Ihren Java-Code (MQTTPublisher.java) in dieses Verzeichnis.

Wichtig ist die Verzeichnis-Struktur einzehalten:
```bash
~ihrHomeVerzeichnis
 |
 ├──/java_mqtt
 |  |pom.xml                // Pom-Datei mit Abhängigkeiten
 |  ├──/src
 |  |  ├──/main
 |  |  |  ├──/java
 |  |  |  |  |MQTTPublisher.java  //Ihre Java-Dateien
 |  |  |  |  |MyJsonMessage.java
```

Gehen  in das Verzeichnis `java-mqtt`. Die POM-Datei speichern sie mit `nano pom.xml`:

```bash
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.pdal.projekt</groupId>
    <artifactId>MqttPublisher</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.source>21</maven.compiler.source>
        <maven.compiler.target>21</maven.compiler.target>
        <paho.mqtt.version>1.2.5</paho.mqtt.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.eclipse.paho</groupId>
            <artifactId>org.eclipse.paho.client.mqttv3</artifactId>
            <version>1.2.5</version>
        </dependency>
        <dependency>
            <groupId>com.google.code.gson</groupId>
            <artifactId>gson</artifactId>
            <version>2.13.1</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.8.1</version>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-assembly-plugin</artifactId>
                <version>3.3.0</version>
                <configuration>
                    <descriptorRefs>
                        <descriptorRef>jar-with-dependencies</descriptorRef>
                    </descriptorRefs>
                    <archive>
                        <manifest>
                            <mainClass>MQTTPublisher</mainClass>
                        </manifest>
                    </archive>
                </configuration>
                <executions>
                    <execution>
                        <id>make-assembly</id>
                        <phase>package</phase>
                        <goals>
                            <goal>single</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>

```

Maven kann damit die benötigten Bibliotheken aus dem Maven-Respository herunterladen, das Projekt erstellen und ausführbar machen. Daher kann der erste Aufruf etwas länger dauern. 

---

## Java-Programme Publisher erstellen

Für unser MQTT-Beispiel verwenden wir zwei Programme:
- **Klasse MyJsonMessage** - ist eine Beispiel-Klasse als Kommunikations-Objekt. Dient vor allem dazu die Google-Gson-Bibliothek nutzen zu können und damit JSON-Objekte zu erstellen. 
- **Klasse MQTTPublisher** - implementiert das Erstellen von JSON-Objekten und den MQTT-Publisher. 

Erstellen sie die Java-Klasse `MyJsonMessager.java` mit `nano MyJsonMessager.java` unter `~/java_mqtt/src/main/java/`.

```bash
package serv.mqttpublisher;

import java.time.LocalDateTime;

/**
 *
 * @author uw1009
 */
public class MyJsonMessage {
    
    String ldt;
    Integer number;
    String message;
    String senderID;

    public String getLdt() {
        return ldt;
    }

    public void setLdt(String ldt) {
        this.ldt = ldt;
    }

    public Integer getNumber() {
        return number;
    }

    public void setNumber(Integer number) {
        this.number = number;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public String getSenderID() {
        return senderID;
    }

    public void setSenderID(String senderID) {
        this.senderID = senderID;
    }

    public MyJsonMessage(LocalDateTime ldto, Integer number, String message, String senderID) {
        this.ldt = ldto.toString();
        this.number = number;
        this.message = message;
        this.senderID = senderID;
    }

    @Override
    public String toString() {
        return "MyJsonMessage{" + "ld=" + ldt + ", number=" + number + ", message=" + message + ", senderID=" + senderID + '}';
    }
    
}
```

Als nächstes erstellen wir die `MqttPublisher.java`-Datei in dem gleichen Verzeichnis.

```bash
package serv.mqttpublisher;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import java.time.LocalDateTime;
import java.util.logging.Level;
import java.util.logging.Logger;

import org.eclipse.paho.client.mqttv3.*;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;


/**
 *
 * @author pdal
 */
public class MqttPublisher {

    public static void main(String[] args) {
        String broker = "tcp://192.168.137.160:1883";
        String topic = "test/topic";
        String content;
        int qos = 0;
        
        LocalDateTime now = LocalDateTime.now();
        int counter = 0;
        // neues Message-Objekt erzeugen
        MyJsonMessage mjm = new MyJsonMessage(now, counter, 
                "Loop: ", "Publischer1");
        
        //Gson-Objekt erzeugen
        // Gson gson = new Gson();
        
        // Gson-Pretty-Printer ist nur weil es besser aussieht.
        // Technisch macht es keinen Unterschied Gson oder 
        // Gson-Pretty-Printer verwendet wird.
        Gson gson = new GsonBuilder().setPrettyPrinting().create();

        LocalDateTime newLdt = LocalDateTime.parse(mjm.getLdt());
        System.out.println(newLdt.toLocalDate() + " :: " + newLdt.toLocalTime());
        
        try {
            // MQTT-Client initialisieren
            MqttClient client = new MqttClient(broker, MqttClient.generateClientId(), new MemoryPersistence());

            // Verbindung herstellen
            client.connect();
            
            while(true){
                // Nachricht anpassen
                mjm.setNumber(counter);
                mjm.setLdt(LocalDateTime.now().toString());
                
                content = gson.toJson(mjm);
                // Nachricht veröffentlichen
                MqttMessage message = new MqttMessage(content.getBytes());
                message.setQos(qos);
                client.publish(topic, message);         

                Thread.sleep(10000);
                
                // Schleife verlassen nach ...
                if(counter == 100)
                    break;
                                
                counter++;
            }
            
            // Verbindung beenden
            client.disconnect();
        } catch (MqttException e) {
            e.printStackTrace();
        } catch (InterruptedException ex) {
            Logger.getLogger(MqttPublisher.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}

```
Damit sind beide Beispielsklassen für den Publisher erstellt.

---

## Java-Klassen kompilieren und ausführen


