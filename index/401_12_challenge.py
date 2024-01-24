#!/usr/bin/env python3

# Script Name:                  Challenge 401 Class 12
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      01/23/2024
# Sources:                      https://chat.openai.com/, https://www.youtube.com/watch?v=vk4WWIreH8Q, https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python, https://pypi.org/project/cryptography/
# Purpose:                      Add the following features to your Network Security Tool:

# User menu prompting choice between TCP Port Range Scanner mode and ICMP Ping Sweep mode, with the former leading to yesterday’s feature set
# ICMP Ping Sweep tool
# Prompt user for network address including CIDR block, for example “10.10.0.0/24”
# Careful not to populate the host bits!

# Create a list of all addresses in the given network
# Ping all addresses on the given network except for network address and broadcast address
# If no response, inform the user that the host is down or unresponsive.
# If ICMP type is 3 and ICMP code is either 1, 2, 3, 9, 10, or 13 then inform the user that the host is actively blocking ICMP traffic.
# Otherwise, inform the user that the host is responding.
# Count how many hosts are online and inform the user.

import ipaddress
from scapy.all import IP, ICMP, TCP, sr1, send

# ICMP Ping Sweep tool function
def icmp_ping_sweep(network):
    # Create a list of all host IP addresses in the network
    all_hosts = list(network.hosts())
    # Counter
    online_hosts = 0

    # Ping each host and print the result
    for host in all_hosts:
        response = sr1(IP(dst=str(host))/ICMP(), timeout=1, verbose=0)

        if response is None:
            print(f"{host} is down or unresponsive.")
        elif response.haslayer(ICMP) and response.getlayer(ICMP).type == 3 and response.getlayer(ICMP).code in [1, 2, 3, 9, 10, 13]:
            print(f"{host} is actively blocking ICMP traffic.")
            online_hosts += 1
        else:
            print(f"{host} is online and responding.")
            online_hosts += 1

    print(f"Number of online hosts: {online_hosts}")

# TCP Port Range Scanner function
def tcp_port_range_scanner(host, port_range):
    # Test each port in the specified range using a for loop
    for dst_port in port_range:
        src_port = 1025
        response = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port,flags="S"), timeout=1, verbose=0)
        
        if response is not None and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
            print(f"Port {dst_port} is open!")
            rst_pkt = IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="R")
            send(rst_pkt, verbose=0)
        elif response is not None and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
            print(f"Port {dst_port} is closed.")
        else:
            print(f"Port {dst_port} is filtered and silently dropped.")

# User menu
while True:
    print("Select an option:")
    print("1. TCP Port Range Scanner")
    print("2. ICMP Ping Sweep")
    print("3. Quit")
    choice = input("Enter your choice (1, 2 or 3): ")
    
    if choice == "1":
        host = input("Enter host IP to scan: ")
        port_range = input("Enter port range (e.g. 1-1024) or specific set of ports to scan (e.g. 22,80,443): ").split(",")
        if "-" in port_range[0]:
            port_range = range(int(port_range[0].split("-")[0]), int(port_range[0].split("-")[1])+1)
        else:
            port_range = [int(p) for p in port_range]
        tcp_port_range_scanner(host, port_range)
    elif choice == "2":
        network_input = input("Enter the network address (e.g. 10.10.0.0/24): ")
        try:
            network = ipaddress.ip_network(network_input, strict=False)
            icmp_ping_sweep(network)
        except ValueError as e:
            print(f"Invalid network address: {e}")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")