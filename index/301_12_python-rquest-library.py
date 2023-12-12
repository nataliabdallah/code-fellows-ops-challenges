#!/usr/bin/env python3

# Script Name:                  Challenge 12 Python Requests Library
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      12/12/2023
# Sources:                      https://chat.openai.com/, https://github.com/codefellows/seattle-ops-301d10
# Purpose:                      Ops Challenge: Python Requests Library (this script will schow the coded portion to the user for learnning purposes)

# Overview

# Ever wondered how web browsers like Google Chrome communicate with web servers to create the interactive web sites and apps we use every day? One technical answer is HTTP requests. Today, you will be performing HTTP GET requests using the requests Python library. This library is very useful for a security professional to evaluate how a web server responds to outside requests.

# Resources

# Python Requests Library Guide{:target="_blank"}
# Objectives

# Create a Python script that performs the following:

# Prompt the user to type a string input as the variable for your destination URL.

# Prompt the user to select a HTTP Method of the following options:

# GET
# POST
# PUT
# DELETE
# HEAD
# PATCH
# OPTIONS
# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.

# Using the requests library, perform a request against the destination URL with the HTTP Method selected by the user.

# For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.

# For the given URL, print response header information to the screen.

import requests

def translate_status_code(status_code):
    status_codes = {
        100: 'Continue',
        101: 'Switching Protocols',
        200: 'OK',
        201: 'Created',
        202: 'Accepted',
        203: 'Non-Authoritative Information',
        204: 'No Content',
        205: 'Reset Content',
        206: 'Partial Content',
        300: 'Multiple Choices',
        301: 'Moved Permanently',
        302: 'Found',
        303: 'See Other',
        304: 'Not Modified',
        305: 'Use Proxy',
        307: 'Temporary Redirect',
        400: 'Bad Request',
        401: 'Unauthorized',
        402: 'Payment Required',
        403: 'Forbidden',
        404: 'Not Found',
        405: 'Method Not Allowed',
        406: 'Not Acceptable',
        407: 'Proxy Authentication Required',
        408: 'Request Timeout',
        409: 'Conflict',
        410: 'Gone',
        411: 'Length Required',
        412: 'Precondition Failed',
        413: 'Payload Too Large',
        414: 'URI Too Long',
        415: 'Unsupported Media Type',
        416: 'Range Not Satisfiable',
        417: 'Expectation Failed',
        418: "I'm a teapot",
        426: 'Upgrade Required',
        500: 'Internal Server Error',
        501: 'Not Implemented',
        502: 'Bad Gateway',
        503: 'Service Unavailable',
        504: 'Gateway Timeout',
        505: 'HTTP Version Not Supported',
    }
    
    return status_codes.get(status_code, 'Unknown Status Code')

def main():
    # Prompt user for URL and HTTP Method
    url = input("Enter the destination URL: ")
    
    # Check if the URL starts with http:// or https://, if not, prepend http://
    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    http_method = input("Enter the HTTP Method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ").upper()

    # Print the request information and ask for confirmation
    input("\nPress Enter to see the code for the request.")
    
    # Print code for the request
    print(f"\nCode for the request:\n"
          f"url = '{url}'\n"
          f"http_method = '{http_method}'\n"
          f"response = requests.request(http_method, url)\n")

    input("\nPress Enter to see the code for handling the response.")

    # Perform request
    response = requests.request(http_method, url)

    # Translate status code and print response header information
    print(f"\nResponse Information:\nStatus Code: {response.status_code} - {translate_status_code(response.status_code)}")
    
    # Print response headers
    print("\nResponse Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")

if __name__ == "__main__":
    main()
