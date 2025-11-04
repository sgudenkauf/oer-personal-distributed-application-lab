---
title: "Checklist for REST Service Verification"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "uwe.bachmann@jade-hs.de"
organization: "PDAL-Projekt"
date: "2025-09-25"
version: "1.0.0"
level: "Level 2, Learning Unit 2.3, Assessment"
duration: "0.2 Hrs"
prerequisites:["Completed - 2400 REST Applications - Proprietary Development and External Use"]
tags: ["PDAL","Assessment"]
license: "CC BY-SA 4.0"
---

## ✅ Checklist for REST Service Verification

The successful implementation of the temperature conversion web service can be verified using the following points. These serve as True/False questions for checking the correct functionality of the created PHP application.

### 1. File Structure and Basic Functionality

**Question 1: File Creation Successful**

The PHP file `tempUmrechner.php` was correctly created in the `/rest/` directory of the web server and populated with all the code from the document.

* **Answer True:** The source file exists in the correct location, and permissions allow the web server to access it.
* **Answer False (Correction Note):** Check if the file is located in the correct path (e.g., `/var/www/html/rest/`) and whether the web server (Apache2) is running and correctly processing PHP. A syntax error in the code can also prevent the call.

**Question 2: Basic Browser Call**

Calling the example link in the browser (`http://<ip-webcontainer>/rest/tempUmrechner.php?wert=20&einheit=celsius`) worked and returned the JSON object **{"einheit":"fahrenheit","wert":68}** as the response.

* **Answer True:** The web service is reachable, PHP processes the inputs successfully, and the basic conversion works.
* **Answer False (Correction Note):** Make sure that Apache2 and PHP are active. An HTTP status code **500** indicates an internal server error, which is usually caused by a syntax error in the PHP code.

***

### 2. Correct Conversion Logic

**Question 3: Conversion from Celsius to Fahrenheit**

The query for the value **$28.4^\circ$ Celsius** (`wert=28.4&einheit=celsius`) returns the correct value **$83.12$ Fahrenheit**.

* **Answer True:** The formula stored in the code $(\text{C} \times 1.8) + 32$ was correctly implemented and leads to the correct result.
* **Answer False (Correction Note):** Check the calculation in the PHP script: `$wert * 1.8 + 32`. Ensure that the variable `$wert` is used correctly.

**Question 4: Conversion from Fahrenheit to Celsius**

The query for the value **$100.4^\circ$ Fahrenheit** (`wert=100.4&einheit=fahrenheit`) returns the correct value **$38.0$ Celsius**.

* **Answer True:** The formula stored in the code $(\text{F} - 32) / 1.8$ was correctly implemented and leads to the correct result.
* **Answer False (Correction Note):** Check the correct parentheses and subtraction in the PHP script: `($wert - 32) / 1.8`. Errors in this formula are often due to missing parentheses.

***

### 3. Robust Error Handling (Validation)

**Question 5: Handling Missing Parameters**

If the URL is called without the parameter `wert` (or `einheit`), the service returns the HTTP status code **400** and an explanatory error message in JSON format.

* **Answer True:** The first error handling block (`!isset($_GET['wert']) || !isset($_GET['einheit'])`) was successfully implemented and prevents the script from crashing.
* **Answer False (Correction Note):** Check the code block under **1. Prüfen auf benötigte Parameter**. The function `sendError(400, "Fehlende Parameter...")` must be called when inputs are missing.

**Question 6: Handling Invalid Values**

If the parameter `wert` contains a non-numeric value (e.g., `wert=abc`), the service returns the HTTP status code **400** and aborts the conversion.

* **Answer True:** Error handling with `!is_numeric($wert)` prevents calculation with invalid data.
* **Answer False (Correction Note):** Check the code block under **2. Prüfen auf gültigen Wert**. For non-numeric input, the function `sendError(400, "Der Parameter 'wert' muss numerisch sein.")` must be called.

**Question 7: Handling Invalid Units**

The service **robustly** accepts the unit even in capital letters (e.g., `FAHRENHEIT`) and returns the HTTP status code **400** for an unknown unit (e.g., `kelvin`).

* **Answer True:** The use of `strtolower($_GET['einheit'])` ensures input robustness, and the final `if` check catches unknown units.
* **Answer False (Correction Note):** Check the code block under **3. Prüfen auf gültige Einheit**. Ensure the unit is converted to lowercase before checking, and that unknown units correctly lead to `sendError(400, "Ungültiger Wert...")`.

---

### License
This work is licensed under the **Creative Commons Attribution - ShareAlike 4.0 International License**.
 
[To the license text on the Creative Commons website](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en)
