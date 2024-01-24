#!/usr/bin/env python3

# Script Name:                  Challenge 401 Class 13
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      01/24/2024
# Sources:                      https://chat.openai.com/, https://www.youtube.com/watch?v=vk4WWIreH8Q, https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python, https://pypi.org/project/cryptography/
# Purpose:                      The final iteration of your network scanning tool will perform the following:

# Ping an IP address determined by the user.
# If the host exists, scan its ports and determine if any are open.


import ipaddress
from scapy.all import IP, ICMP, TCP, sr1, send

# ICMP Ping Sweep function
def icmp_ping_sweep(network):
    all_hosts = list(network.hosts())
    responsive_hosts = []

    for host in all_hosts:
        print(f"Pinging {host}...")
        response = sr1(IP(dst=str(host))/ICMP(), timeout=1, verbose=0)

        if response is not None:
            print(f"{host} responded.")
            responsive_hosts.append(str(host))
        else:
            print(f"{host} did not respond.")

    return responsive_hosts

# TCP Port Range Scanner function
def tcp_port_range_scanner(host, port_range):
    src_port = 1025
    for dst_port in port_range:
        tcp_response = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags="S"), timeout=1, verbose=0)
        
        if tcp_response is not None and tcp_response.haslayer(TCP):
            if tcp_response.getlayer(TCP).flags == 0x12:
                print(f"Port {dst_port} on {host} is open!")
                send(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags="R"), verbose=0)
            elif tcp_response.getlayer(TCP).flags == 0x14:
                print(f"Port {dst_port} on {host} is closed.")
        else:
            print(f"Port {dst_port} on {host} is filtered or unresponsive.")

# Script Execution
print("This script will first perform an ICMP Ping Sweep and then scan specific ports at your command.")

# Getting network input
network_input = input("Enter the network address (e.g. 10.10.0.0/24): ")
try:
    network = ipaddress.ip_network(network_input, strict=False)
except ValueError as e:
    print(f"Invalid network address: {e}")
    exit()

# Running ICMP Ping Sweep
responsive_hosts = icmp_ping_sweep(network)

# TCP Port Range Scan for each responsive host
for host in responsive_hosts:
    print(f"\nHost {host} responded. Ready to perform TCP port scan.")
    port_range_input = input(f"Enter port range for TCP scan on {host} (e.g. 1-1024): ").split("-")
    try:
        port_range = range(int(port_range_input[0]), int(port_range_input[1]) + 1)
        tcp_port_range_scanner(host, port_range)
    except ValueError as e:
        print(f"Invalid port range: {e}")