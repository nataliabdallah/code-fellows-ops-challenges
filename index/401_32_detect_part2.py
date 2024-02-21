#!/usr/bin/env python3

# Script Name:                  Challenge 32 Event Logging part 3/3
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      02/20/2023
# Sources:                      https://chat.openai.com/, https://github.com/codefellows/seattle-ops-301d10
# Purpose:                      Objectives

# Continue developing your Python malware detection tool.

# Alter your search code to recursively scan each file and folder in the user input directory path and print it to the screen.
# For each file scanned within the scope of your search directory:
# Generate the file’s MD5 hash using Hashlib.
# Assign the MD5 hash to a variable.
# Print the variable to the screen along with a timestamp, file name, file size, and complete (not symbolic) file path.
# TIP: You may need to bring in additional Python modules to complete today’s objective.

# The script should be tested to execute successfully in Python3.

import os
import hashlib
from datetime import datetime

def get_md5_hash(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def search_files(directory):
    files_searched = 0

    for root, dirs, files in os.walk(directory):
        for name in files:
            try:
                files_searched += 1
                file_path = os.path.join(root, name)
                md5_hash = get_md5_hash(file_path)
                file_size = os.path.getsize(file_path)
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"Timestamp: {timestamp}, File: {name}, Size: {file_size} bytes, MD5: {md5_hash}, Path: {file_path}")
            except Exception as e:
                print(f"Error processing file {name}: {e}")

    print(f"Files searched: {files_searched}")

if __name__ == "__main__":
    directory = input("Enter the directory to search in: ")
    directory = os.path.normpath(directory)
    search_files(directory)
