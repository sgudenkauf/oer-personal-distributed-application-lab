---
title: "Checklist for the Web Application"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe", "Kalk, Ronald"]
email: "uwe.bachmann@jade-hs.de"
organization: "PDAL Project"
date: "2025-09-25"
version: "1.0.0"
level: "Level 2, Learning Unit 2.3, Assessment"
duration: "0.2 hours"
prerequisites:["Completed - 2300 Custom Web Application with Database Connection"]
tags: ["PDAL","Assessment"]
license: "CC BY-SA 4.0"
---

## 📝 Checklist for the Web Application

Each question relates to the correct implementation of the **Contact List Application**. The correct answer is always **True** (Wahr) because it checks compliance with best practices.

### 1. Database Schema

**Question 1:** The `contacts` table has been created in the `contacts_db` database and includes the `id` field as the **`PRIMARY KEY`** and **`AUTO_INCREMENT`**.

| Answer | Hint (Feedback) |
| :--- | :--- |
| **True** | **Correct.** A primary key with auto-increment is essential to uniquely identify and manage every data record (CRUD). |
| False | Check your SQL command. Without a unique primary key (`id INT AUTO_INCREMENT PRIMARY KEY`), the script cannot reliably delete or edit data records later. |

---

### 2. Functionality: Adding Contacts (CREATE)

**Question 2:** After successfully filling out and submitting the form, the **newly created contact** immediately appears in the contact list on the main page.

| Answer | Hint (Feedback) |
| :--- | :--- |
| **True** | **Correct.** This confirms that the `INSERT` statement is working and the database query (`SELECT`) is correctly reading and displaying the new data. |
| False | Check if the `INSERT INTO contacts` command in the PHP script is correctly formulated and if the `$_POST` data is correctly passed to the prepared statements. The subsequent `header('Location: ...')` redirect must also be correct. |

---

### 3. Functionality: Displaying the List (READ)

**Question 3:** If contacts exist in the database, they are displayed in an **ordered HTML table**, with the results sorted by **Name** by default.

| Answer | Hint (Feedback) |
| :--- | :--- |
| **True** | **Correct.** This confirms the correct function of the `SELECT * FROM contacts ORDER BY name` command and the subsequent `foreach` loop in the HTML output. |
| False | Review the `SELECT` command in the **3. QUERY DATA (READ)** section. Ensure that `fetchAll()` correctly loads the data into the `$contacts` array and that the HTML structure iterates through the data correctly. |

---

### 4. Functionality: Deleting Contacts (DELETE)

**Question 4:** Clicking the **"Delete" link** removes the associated contact from the list and the database without any error messages appearing.

| Answer | Hint (Feedback) |
| :--- | :--- |
| **True** | **Correct.** This confirms that the `DELETE` command is correctly triggered via the URL parameters (`?delete_id=...`), the ID is safely passed to the prepared statement, and the record is removed. |
| False | Check the **DELETE code block** (`isset($_GET['delete_id'])`). Ensure that the `href` link in the HTML passes the correct `id` and that the PHP code uses this ID to execute the `DELETE` statement. |

---

## Further Questions

### 5. Database Connection (Index Script)

**Question 5:** The PDO connection code in the `index.php` script uses the option **`PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION`** to output database errors as PHP exceptions.

| Answer | Hint (Feedback) |
| :--- | :--- |
| **True** | **Correct.** This is the modern and cleanest way of error handling in PHP database connections and is essential for troubleshooting. |
| False | Look for the `try/catch` block in the connection code. Without this option, PDO silently ignores errors, making troubleshooting nearly impossible. |

---

### 6. Security and CRUD Logic

**Question 6:** **Prepared Statements** (`$pdo->prepare(...)`) are used for inserting (`INSERT`) and deleting (`DELETE`) data to securely process user input.

| Answer | Hint (Feedback) |
| :--- | :--- |
| **True** | **Correct.** Prepared statements are the **most important** protection mechanism against **SQL Injection**. |
| False | Check the sections for CREATE and DELETE. If you use user input (`$_POST` or `$_GET`) directly in the SQL query, there is a high-security vulnerability (SQL Injection). Use placeholders (`?` or `:name`). |

---

### 7. Output Security

**Question 7:** Contact data read from the database (`$contact['name']`, etc.) is protected using **`htmlspecialchars()`** when outputting the HTML.

| Answer | Hint (Feedback) |
| :--- | :--- |
| **True** | **Correct.** This prevents **Cross-Site Scripting (XSS)** by correctly encoding special HTML characters (like `<` and `>`) before they are displayed in the browser. |
| False | Review the `<tbody>` area in your HTML code. Unprotected output of user input (`<?= $contact['name'] ?>`) poses an XSS security risk. |

---

### 8. Code Organization and Pattern (PRG)

**Question 8:** After adding or deleting a contact, the page is reloaded using the PHP function **`header('Location: ...')`** (Post/Redirect/Get pattern).

| Answer | Hint (Feedback) |
| :--- | :--- |
| **True** | **Correct.** This pattern (PRG) prevents the user from resending the data (e.g., the INSERT command) when reloading the page (F5). |
| False | Check the `if ($_SERVER['REQUEST_METHOD'] === 'POST' ...)` blocks. If the redirect (`header()`) is missing, the browser will ask if the data should be sent again upon pressing F5. |

---

### 9. Code Modularity (Further Development)

**Question 9:** The database configuration (`db_config.php`) is included in `index.php` using the **`require_once`** statement.

| Answer | Hint (Feedback) |
| :--- | :--- |
| **True** | **Correct.** `require_once` is better than `include` because it stops the script if the configuration file is missing (critical error) and prevents double inclusion. |
| False | Check the first line after you have separated the configuration. If you use `include` or `require` without `_once`, you miss the opportunity to apply the best practice for critical code parts. |

---

### 10. Configuration Path Security (Advanced)

**Question 10:** For a production system, the `db_config.php` file would be stored **outside** the directory accessible by the web server (`/var/www/html/`).

| Answer | Hint (Feedback) |
| :--- | :--- |
| **True** | **Correct.** This is a fundamental security practice. Should the web server be incorrectly configured, the sensitive login credentials cannot be accessed directly via the browser. |
| False | Although the file may be in the same folder for the learning project, it must be secured in production. If the PHP interpreter fails, a user could otherwise view the credentials via the URL `.../db_config.php`. |

---

### License
This work is licensed under the **Creative Commons Attribution - ShareAlike 4.0 International License**.
 
[To the license text on the Creative Commons website](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en)
