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

def generate_key():
    key = Fernet.generate_key()
    with open("401_mysecret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("401_mysecret.key", "rb").read()

def encrypt_message(message, key):
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()  # Corrected here

generate_key()
key = load_key()

encrypted = encrypt_message("this the line that will be encrypted", key)
print("Encrypted: " + encrypted.decode())

decrypted = decrypt_message(encrypted, key)
print("Decrypted: " + decrypted)
