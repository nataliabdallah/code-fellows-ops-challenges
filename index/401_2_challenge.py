#!/usr/bin/env python3

# Script Name:                  Challenge 401 Class 2
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      01/09/2024
# Sources:                      https://chat.openai.com/,
# Purpose:                      Requirements:

# In Python, create an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down.

# The script must:

# Transmit a single ICMP (ping) packet to a specific IP every two seconds.
# Evaluate the response as either success or failure.
# Assign success or failure to a status variable.
# For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.
# Example output: 2020-10-05 17:57:57.510261 Network Active to 8.8.8.8
# 

#TODO: Transmit a single ICMP (ping) packet to a specific IP every two seconds.

import os
import time

specific_ip = "8.8.8.8"

#send_ping = os.system("ping -c 1 " + specific_ip)
#time.sleep(2)
    

#TODO: Evaluate the response as either success or failure.
import subprocess

def ping_host(host):
    try:
        subprocess.run(["ping", "-c", "1", host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True 
    except subprocess.CalledProcessError:
        return False

#TODO: Assign success or failure to a status variable.

while True:
    if ping_host(specific_ip):
        print(f"Ping to {specific_ip} successful")
    else:
        print(f"Ping to {specific_ip} failed")
        
    time.sleep(2)

#TODO: For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.

#TODO: Example output: 2020-10-05 17:57:57.510261 Network Active to 8.8.8.8

