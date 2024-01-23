#!/usr/bin/env python3

# Script Name:                  Challenge 401 Class 7
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      01/17/2024
# Sources:                      https://chat.openai.com/, https://www.youtube.com/watch?v=vk4WWIreH8Q, https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python, https://pypi.org/project/cryptography/
# Purpose:                      In Python, create a TCP Port Range Scanner that tests whether a TCP port is open or closed. The script must:

# Utilize the scapy library
# Define host IP
# Define port range or specific set of ports to scan
# Test each port in the specified range using a for loop
# If flag 0x12 received, send a RST packet to graciously close the open connection. Notify the user the port is open.
# If flag 0x14 received, notify user the port is closed.
# If no flag is received, notify the user the port is filtered and silently dropped.

import scapy
from scapy.all import IP, TCP, sr1, send

# Define target and range of ports to scan
scan_target = "scanme.nmap.org"
target_ports = range(22, 444)  
local_port = 1027



# Scanning each port
for port in target_ports:
    # Send SYN and wait for response
    scan_response = sr1(IP(dst=scan_target)/TCP(sport=local_port, dport=port, flags="S"), timeout=1, verbose=0)

    # Analyze response
    if scan_response is not None and scan_response.haslayer(TCP):
        if scan_response.getlayer(TCP).flags == 0x12:  # Open port (SYN-ACK)
            print(f"Port {port} is open!")
            send(IP(dst=scan_target)/TCP(sport=local_port, dport=port, flags="R"), verbose=0)
        elif scan_response.getlayer(TCP).flags == 0x14:  # Closed port (RST-ACK)
            print(f"Port {port} is closed.")
    else:  # No response or filtered port
        print(f"Port {port} is filtered or unresponsive.")
