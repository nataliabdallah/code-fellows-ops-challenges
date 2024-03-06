#!/usr/bin/env python3

# Script Name:                  Challenge 42 Part 2 of 3 NMAP - ATTACK TOOLS
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      03/5/2023
# Sources:                      https://chat.openai.com/, https://github.com/codefellows/seattle-ops-401d10
# Purpose:                      Objectives: 
# Nmap is a highly popular security tool used for enumeration tasks. By importing Nmap into Python we can begin to develop our own enumeration/port scanner tool.

# Today you will use Python to develop a custom Nmap scanner that can later be combined with other Python scripts to create a pentester toolkit.

# Resources
# Staging
# This script requires Python3 and python-nmap 0.6.1.

# From a Linux VM run sudo pip3 install python-nmap to install the Nmap library for Python.
# Import libraries
import nmap
import re

# Function to validate the IP address
def is_valid_ip(ip):
    pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    return pattern.match(ip) is not None

# Function to validate the port range
def is_valid_port_range(range):
    pattern = re.compile(r'^\d+-\d+$')
    return pattern.match(range) is not None

# Main function
def main():
    scanner = nmap.PortScanner()

    print("Nmap Automation Tool")
    print("--------------------")

    ip_addr = input("IP address to scan: ")
    if not is_valid_ip(ip_addr):
        print("Invalid IP address format.")
        return

    print("The IP you entered is: ", ip_addr)

    resp = input("""\nSelect scan to execute:
                    1) SYN ACK Scan
                    2) UDP Scan
                    3) Full Scan\n""")
    if resp not in ['1', '2', '3']:
        print("Please enter a valid option (1, 2, or 3).")
        return

    print("You have selected option: ", resp)

    port_range = input("Enter the port range (e.g., 1-100): ")
    if not is_valid_port_range(port_range):
        print("Invalid port range format.")
        return

    try:
        if resp == '1':
            scanner.scan(ip_addr, port_range, '-v -sS')
        elif resp == '2':
            scanner.scan(ip_addr, port_range, '-v -sU')
        elif resp == '3':
            scanner.scan(ip_addr, port_range, '-v -sS -sV -sC -A -O')

        print(f"Nmap Version: {scanner.nmap_version()}")
        print(scanner.scaninfo())
        print(f"IP Status: {scanner[ip_addr].state()}")
        open_ports = []
        for protocol in scanner[ip_addr].all_protocols():
            open_ports.extend(list(scanner[ip_addr][protocol].keys()))
        print("Open Ports: ", open_ports)
    except nmap.PortScannerError as e:
        print(f"Scan error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == '__main__':
    main()
