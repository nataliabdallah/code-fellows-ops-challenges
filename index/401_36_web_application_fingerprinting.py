#!/usr/bin/python3
# Script Name:                  Challenge 36 Web Application Fingerprinting
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      02/26/2023
# Sources:                      https://chat.openai.com/, https://github.com/codefellows/seattle-ops-301d10
# Purpose:                      Objectives

# For this lab you’ll need to develop and test your Python script from a Linux VM with the tools Nmap, Netcat, and Telnet installed. Generally speaking, Kali Linux is the recommendation for this challenge.

# In Python create a script that executes from a Linux box to perform the following:

# Prompts the user to type a URL or IP address.
# Prompts the user to type a port number.
# Performs banner grabbing using netcat against the target address at the target port; prints the results to the screen then moves on to the step below.
# Performs banner grabbing using telnet against the target address at the target port; prints the results to the screen then moves on to the step below.
# Performs banner grabbing using Nmap against the target address of all well-known ports; prints the results to the screen.
# NOTE: Be sure to only target approved URLs like scanme.nmap.org or web servers you own.

import subprocess
import telnetlib

def run_netcat(addr, port):
    """
    Uses subprocess to execute the netcat command and grab the banner.
    """
    try:
        # Builds the netcat command as a string
        command = f"nc -vn {addr} {port} -w 3"
        # Executes the command using subprocess, with a timeout to avoid hanging
        output = subprocess.check_output(command, shell=True, timeout=10, stderr=subprocess.STDOUT)
        print("Netcat Banner Grabbing Result:")
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print("Netcat failed:", e.output.decode())
    except subprocess.TimeoutExpired:
        print("Netcat command timed out.")

def run_telnet(addr, port):
    """
    Uses telnetlib to connect to the target and grab the banner.
    """
    try:
        # Connects to the target with a timeout
        with telnetlib.Telnet(addr, port, timeout=10) as tn:
            # Reads until a newline or timeout
            output = tn.read_until(b"\n", timeout=5)
            print("Telnet Banner Grabbing Result:")
            print(output.decode())
    except Exception as e:
        print("Telnet failed:", str(e))

def run_nmap(addr):
    """
    Uses subprocess to execute the nmap command for banner grabbing on well-known ports.
    """
    try:
        # Nmap command to scan well-known ports and attempt version detection
        command = f"nmap -p 1-1023 -sV {addr}"
        output = subprocess.check_output(command, shell=True, timeout=60, stderr=subprocess.STDOUT)
        print("Nmap Banner Grabbing Result:")
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print("Nmap failed:", e.output.decode())
    except subprocess.TimeoutExpired:
        print("Nmap command timed out.")

def main():
    # Prompts the user for target address and port
    addr = input("Enter the URL or IP address: ")
    port = int(input("Enter the port number: "))

    # Executes banner grabbing using the defined functions
    run_netcat(addr, port)
    run_telnet(addr, port)
    run_nmap(addr)  # Note: Nmap scans well-known ports, ignoring the user-provided port

if __name__ == "__main__":
    main()

