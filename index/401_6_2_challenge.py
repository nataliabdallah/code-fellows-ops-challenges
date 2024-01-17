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

# create a file to encrypt: you can type in terminal: touch mysecret.txt
# make sure there is data in the file to encrypt

# encrypt the file desired to be encrypted

# read key from file
key = ''
with open('401_6_mysecret.key', 'rb') as file:
    key = file.read()
# read data from file
data = ''
with open('401_6_secret.txt', 'rb') as file:
    data = file.read()


# encrypt data
from cryptography.fernet import Fernet

f = Fernet(key)

encryptedData = f.encrypt(data)

# save the encrpted data into a file    
with open('401_6_secret.txt', 'wb') as file:
    file.write(encryptedData)
