# Web_app_vuln_scanner_CodTech

**COMPANY**: CODTECH IT SOLUTIONS

**NAME**: ABHINANDAN BAIS

**DOMAIN**: CS & EH

**INTERN ID**: CT08GXK

**BATCH DETAILS**: December 30th, 2024 to January 30th, 2025

**MENTOR NAME**: NEELA SANTOSHI

# DESCRIPTION OF THE TOOL

This is a Web Vulnerability Scanner script written in Python. It performs basic vulnerability checks for SQL Injection and Cross-Site Scripting (XSS) while also identifying form inputs that could be potential targets for testing.

Description:

SQL Injection Detection:


Uses predefined payloads to append to the URL.

Checks if the response contains SQL error messages to flag potential vulnerabilities.

XSS Detection:

Appends XSS payloads to the URL.

Verifies if the payload appears in the response, indicating potential vulnerability.

Form Input Discovery:


Analyzes the HTML content of the page.

Lists form inputs (<input> tags), which could be exploited for injection attacks.

User Interface:


Prompts the user for a target URL.

Displays scan progress and findings in a readable format.

![Screenshot 2025-01-13 091931](https://github.com/user-attachments/assets/da4df683-b3df-4f08-8d08-1f6c6b904405)
