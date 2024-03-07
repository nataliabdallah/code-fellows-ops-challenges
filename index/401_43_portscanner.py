#!/usr/bin/env python3

# Script Name:                  Challenge 401 Class 43 (look at challenge 11)
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      03/06/2024
# Sources:                      https://chat.openai.com/, https://www.youtube.com/watch?v=vk4WWIreH8Q, https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python, https://pypi.org/project/cryptography/
# Purpose:                      In Python, Create a Port Scanner
# Overview
# The socket python module grants us access to low level networking interface operations directly from the Python 3 script.

import socket

def port_scanner(host, port_range):
    # Convert hostname to IPv4 address
    try:
        target_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")
        return

    print(f"Scanning target {target_ip}")

    for port in port_range:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port} is open")
            else:
                print(f"Port {port} is closed or filtered")
            s.close()

if __name__ == "__main__":
    # Define your target and port range here
    scan_target = "scanme.nmap.org"  # Change this to the host you want to scan
    target_ports = range(22, 444)  # Define the range of ports to scan

    port_scanner(scan_target, target_ports)
