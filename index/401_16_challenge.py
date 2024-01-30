#!/usr/bin/env python3

# Script Name:                  Challenge 401 Class 13
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      01/30/2024
# Sources:                      https://chat.openai.com/, https://www.youtube.com/watch?v=vk4WWIreH8Q, https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python, https://pypi.org/project/cryptography/
# Purpose:                      In Python, create a script that prompts the user to select one of the following modes:

# Mode 1: Offensive; Dictionary Iterator

# Accepts a user input word list file path and iterates through the word list, assigning the word being read to a variable.
# Add a delay between words.
# Print to the screen the value of the variable.
# Mode 2: Defensive; Password Recognized

# Accepts a user input string.
# Accepts a user input word list file path.
# Search the word list for the user input string.
# Print to the screen whether the string appeared in the word list.

import time
choose = "choose"
c = "_"
ch16 = input(" {:^38}\n Option 1: Offensive; Dictionary Iterator\n\n Option 2:Defensive; Password Recognized\n                   ".format(choose))

if ch16 == "1":
    path = input("Enter file path: ")
    with open(path, "r") as file:
        for line in file:
            word = line.strip()
            print(word)
            time.sleep(1)

elif ch16 == "2":
    usrinput = input("Enter string: ")
    path = input("Enter file path: ")
    with open(path, "r") as file:
        words = file.read().splitlines()
        if usrinput in words:
            print("found it!.")
        else:
            print("no luck.")
else:
    print("fix me i'm broken.")