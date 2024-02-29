#!/usr/bin/env python3

# Script Name:                  Challenge 38 XSS Vulnerability Detection with Python
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      02/28/2023
# Sources:                      https://chat.openai.com/, https://github.com/codefellows/seattle-ops-401d10
# Purpose:                      Objectives: This script was already made, descriptions were added.

# Note: Ensure the 'requests' and 'beautifulsoup4' (bs4) libraries are installed in your Python environment before executing this script.

# Import libraries
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Function to retrieve all forms from a given webpage
def get_all_forms(url):
    # Fetches the content of the URL, parses it as HTML, and finds all <form> elements.
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

# Function to extract details from a form
def get_form_details(form):
    # Gathers essential details from a form, such as its action (URL to send the form data), method (GET or POST), and its input fields.
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    # Iterates over all input tags and collects their types and names.
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

# Function to submit a form with given inputs
def submit_form(form_details, url, value):
    # Constructs the full URL to submit the form data to and prepares the data payload based on input fields.
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        # Assigns the provided 'value' to all text and search input fields.
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    # Submits the form data either using a POST or GET request based on the form's method.
    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

# Function to test for XSS vulnerabilities
def scan_xss(url):
    # Retrieves all forms from the URL and attempts to submit them with a JavaScript payload.
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = "<script>alert('XSS')</script>"  # The JavaScript code used to test for XSS vulnerabilities.
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        # Checks if the submitted JavaScript is reflected in the response content, indicating a potential XSS vulnerability.
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main execution block
if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:")  # Prompts the user to enter a URL to test.
    print(scan_xss(url))  # Calls the scan_xss function with the provided URL and prints the result.

# After annotating and possibly modifying this script, it should be tested against web applications with known XSS vulnerabilities (XSS-positive) and those without such vulnerabilities (XSS-negative) to ensure its effectiveness and accuracy.
# Please add your test outputs here, clearly indicating which outputs correspond to XSS-positive and XSS-negative detections.
