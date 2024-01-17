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

# Read the key from file
key = ''
with open('401_6_mysecret.key', 'rb') as file:
    key = file.read()
    
# read the encrypted data from file
encryptedData = ''
with open('401_6_secret.txt', 'rb') as file:
    encryptedData = file.read()
    
# decrypt the data
from cryptography.fernet import Fernet

f = Fernet(key)

decryptedData = f.decrypt(encryptedData)


print('Encrypted data:', encryptedData.decode())

print()

print('Decrypted data:', decryptedData.decode())
