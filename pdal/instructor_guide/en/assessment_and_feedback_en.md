---
title: "Competency Assessment in the PDAL: A Hybrid Guide for Instructors"
author: ["Prof. Gudenkauf, Stefan", "Bachmann, Uwe"]
email: "uwe.bachmann@jade-hs.de"
organization: "PDAL Project"
date: "2025-08-11"
version: "1.0.0"
level: "Instructor guide"
duration: "N/a"
prerequisites:["none"]
tags: ["PDAL", "Didactics", "Instructor Guide", "Assessment"]
license: "CC BY-SA 4.0"
---
# Competency Assessment in the PDAL: A Hybrid Guide for Instructors

The Personal Distributed Applications Lab (PDAL) allows learners to gain deep, hands-on experience at their own pace. As an instructor, you face the challenge of assessing these individual learning successes, and most importantly, the **development of competencies** in areas like problem-solving and systems understanding.

This document provides a comprehensive guide for this purpose. It presents a hybrid assessment model resting on three pillars: the verification of theoretical knowledge, the demonstration of practical competencies, and the promotion of critical reflection. With this approach, you can determine not only what learners know but also how they apply that knowledge and learn from their mistakes—essential skills for modern IT practice.

### Assessment and Feedback in the PDAL: A Comprehensive Approach

This document outlines a three-part assessment model specifically developed for the Personal Distributed Applications Lab (PDAL). The goal is to holistically capture learning progress by evaluating theoretical knowledge, practical application skills, and the ability for critical reflection.

---

### Part 1: Knowledge Verification (Multiple-Choice Tests)

This format serves as the foundation to quickly and objectively check learners' understanding of fundamental concepts and facts.

* **Purpose:** To measure knowledge of theoretical fundamentals and terminology from the modules.
* **Implementation:** Create short tests for each competency level (0 to 4). Questions should focus on core terms like "bare-metal hypervisor," "LXC isolation," or "REST API methods."
* **Benefit for Learners:** Instant feedback and the opportunity to specifically identify and close knowledge gaps.
* **Feedback:** For incorrect answers, provide a concise, corrective explanation.


The multiple-choice tests are available as Markdown documents and as H5P modules.
H5P is written with the LUMI editor (https://lumi.education/en/lumi-h5p-offline-desktop-editor/) and can be used directly.

---

### Part 2: Practical Application (PDAL Scenario Challenge)

This is the core of the assessment, which measures learners' true competency: the ability to apply their knowledge in a real, problem-solving environment. Instead of simply providing answers, learners must perform a task in their own PDAL and document the result.

* **Purpose:** To assess practical skills, problem-solving ability, and documentation competence.
* **Implementation:** For each learning level, create concrete "challenges." The tasks should prompt learners to master complex scenarios like configuring secure network communication or debugging a service outage.
* **Example Challenge:**
    * **Task:** "Set up an MQTT broker in Container A and a client in Container B. Configure the broker so that communication is only possible via TLS encryption with self-signed certificates. The client in Container B must successfully send a message to the broker."
    * **Assessment:** Check the functionality of the setup and the quality of the documentation. Criteria include correct configuration, logical sequence of steps, and clarity of the description.
* **Benefit for Learners:** They demonstrate not only what they know but also their ability to apply it in complex situations.

---

### Part 3: Reflection (Lessons Learned)

This format promotes metacognitive skills—the ability to reflect on one's own learning process. Learners reflect on their challenges, solution approaches, and most important insights.

* **Purpose:** To foster critical reflection and deeper understanding.
* **Implementation:** Ask learners to write a short report in Markdown format after completing a challenge or a learning unit. This report should include structured sections such as "Problem Statement," "Obstacles," "Solution Path," and "Key Insight."
* **Benefit for Learners:** They internalize the learned content by actively processing and articulating their experiences.
* **Community Contribution:** These reports can be anonymized and collected to build a valuable knowledge base for future learners.

---

### Recommendation for Instructors

Combine these formats flexibly. Use the multiple-choice tests for a quick knowledge check at the beginning of a module. Use the PDAL scenario challenges to assess practical skills. Use the Lessons Learned reports as a conclusion to each challenge to promote reflection. This hybrid approach provides a robust foundation for fair, comprehensive, and educational assessment.

---

### License
This work is licensed under the **Creative Commons Attribution - ShareAlike 4.0 International License**.
 
[To the license text on the Creative Commons website](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en)
