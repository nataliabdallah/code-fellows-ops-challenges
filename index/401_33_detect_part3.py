#!/usr/bin/env python3

# Script Name:                  Challenge 33 Event Logging part 3/3
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      02/21/2023
# Sources:                     "Marco"; https://chat.openai.com/, https://github.com/codefellows/seattle-ops-301d10
# Purpose:                      Objectives


import os
import time
import datetime
import hashlib
import math
import subprocess
from sys import platform

# Variables
my_os = platform

# Functions
def windows_search():
    filepath = input("Please enter the directory you want to search in: ")
    filename = input("Please enter the name of the file: ")
    print("Please wait while we search…")
    time.sleep(1)

    # Count files searched and found
    search_command = f'dir /a:-d /s /b "{filepath}" | find /c ":\\\"'
    find_command = f'dir /b/s "{filepath}" | findstr /M /C:"{filename}"'
    searchcount = os.popen(search_command).read().strip()
    found_files = os.popen(find_command).read().strip().split('\n')
    foundcount = len(found_files)

    print(f"Files searched: {searchcount}")
    print(f"Files found: {foundcount}")
    for file in found_files:
        print(file)

def os_check():
    print("Let's check your system's OS")
    time.sleep(1)
    print(f"Your system is running {my_os}")
    time.sleep(1)
    print("Now that we know which OS you're running, let's scan your system")
    time.sleep(1)

def linux_search():
    filepath = input("Please enter the directory you want to search in: ")
    filename = input("Please enter the name of the file: ")
    print("Please wait while we search…")
    time.sleep(1)

    # Count and print the number of files searched and discovered
    search_command = f'find "{filepath}" -type f | wc -l'
    find_command = f'find "{filepath}" -type f -name "{filename}"'
    searchcount = os.popen(search_command).read().strip()
    found_files = os.popen(find_command).read().strip().split('\n')
    foundcount = len(found_files)

    print(f"{searchcount} files searched.")
    print(f"Found {foundcount} files that matched:")
    for file in found_files:
        print(file)

def current_time():
    rn = datetime.datetime.now()
    return rn.strftime('%m-%d-%Y %H-%M-%S')

def hash_file(filename):
    h = hashlib.md5()
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()

def hash_catcher():
    print("Taking a look at the hashes of all the given directory")
    time.sleep(1)

    dir_count = 0
    file_count = 0
    start_path = input("Enter path of directory you want to catch hash from: ")
    for path, dirs, files in os.walk(start_path):
        print(f'DIRECTORY: {path}\n')
        dir_count += 1
        for file in files:
            fstat = os.stat(os.path.join(path, file))
            fsize = fstat.st_size
            unit = "B"
            if fsize > 1024 * 1024:
                fsize /= (1024 * 1024)
                unit = "MB"
            elif fsize > 1024:
                fsize /= 1024
                unit = "KB"

            file_count += 1
            filename = os.path.join(path, file)
            md5 = hash_file(filename)
            timestamp = current_time()
            print(f"{timestamp}\nFILENAME: {file}\tSIZE: {fsize:.2f}{unit}\tPATH: {filename}\nHASH: {md5}\n")
            malware_check(md5)
    print(f'Summary: Hashed {file_count} files in {dir_count} directories.')

# Malware checker
def malware_check(the_hash):
    apikey = os.getenv('API_KEY_VIRUSTOTAL')
    if not apikey:
        print("VirusTotal API key is not set.")
        return

    command = ['python3', 'virustotal-search.py', '-k', apikey, '-m', the_hash]
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error running VirusTotal scan: {e.stderr.decode()}")

# User Interface
print("Malware Analysis and Removal Tool")
time.sleep(1)
print("What do you want the tool to do?")
if __name__ == "__main__":
    while True:
        mode = input("""
        1 - Check OS, Search for file
        2 - Get File Hashes for all files in a folder
        3 - Exit
        Please enter a number:

        """)
        if mode == "1":
            os_check()
            if my_os == "linux" or my_os == "linux2":
                linux_search()
            elif my_os == "win32" or my_os == "win64":
                windows_search()
        elif mode == "2":
            hash_catcher()
        elif mode == "3":
            break
        else:
            print("Invalid Selection...")
