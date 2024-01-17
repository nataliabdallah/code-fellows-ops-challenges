#!/usr/bin/env python3

# Script Name:                  Challenge 401 Class 6
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      01/12/2024
# Sources:                      https://chat.openai.com/, https://www.youtube.com/watch?v=vk4WWIreH8Q, https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python, https://pypi.org/project/cryptography/
# Purpose:                      In Python, create a script that utilizes the cryptography library to:

# Prompt the user to select a mode:
# Encrypt a file (mode 1) Delete the existing target file and replace it entirely with the encrypted version.
# Decrypt a file (mode 2) Delete the encrypted target file and replace it entirely with the decrypted version.
# Encrypt a message (mode 3) Print the ciphertext to the screen.
# Decrypt a message (mode 4) Print the cleartext to the screen.

# pip install cryptography (on termnal enter this command to install this)

from cryptography.fernet import Fernet

# Load the key
with open('401_6_mysecret.key', 'rb') as file:
    key = file.read()

# Initialize Fernet
f = Fernet(key)

# Read the encrypted content
with open('401_6_secret.txt', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

# Decrypt the content
decrypted = f.decrypt(encrypted)

# Save the decrypted content
with open('401_6_secret.txt', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)
