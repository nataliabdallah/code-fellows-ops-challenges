#!/usr/bin/env python3

# Script Name:                  Challenge 401 Class 6
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      01/16/2024
# Sources:                      https://chat.openai.com/, https://www.youtube.com/watch?v=vk4WWIreH8Q, https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python, https://pypi.org/project/cryptography/
# Purpose:                      In Python, create a script that utilizes the cryptography library to:

# Prompt the user to select a mode:
# Encrypt a file (mode 1) Delete the existing target file and replace it entirely with the encrypted version.
# Decrypt a file (mode 2) Delete the encrypted target file and replace it entirely with the decrypted version.
# Encrypt a message (mode 3) Print the ciphertext to the screen.
# Decrypt a message (mode 4) Print the cleartext to the screen.

# pip install cryptography (on termnal enter this command to install this)

from cryptography.fernet import Fernet
import os

# Generate or load a key for encryption and decryption
def generate_or_load_key():
    if os.path.isfile("secret.key"):
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    else:
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    return key

# Function to manually input a key or read from a file
def input_key():
    key_input = input("Enter the key or key file name: ")
    if os.path.isfile(key_input):
        with open(key_input, "rb") as key_file:
            return key_file.read()
    else:
        return key_input.encode()

# Function to encrypt the file
def encrypt_file(file_path, key):
    f = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_path + ".encrypted", "wb") as file:
        file.write(encrypted_data)
    print(f"File {file_path} has been encrypted.")

# Function to decrypt the file
def decrypt_file(file_path, key):
    f = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_path.replace(".encrypted", ""), "wb") as file:
        file.write(decrypted_data)
    print("File decrypted successfully.")

# Function to encrypt a message
def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    print("Encrypted Message: " + encrypted_message.decode())

# Function to decrypt a message
def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message.encode())
    print("Decrypted Message: " + decrypted_message.decode())

# Main function to handle user interaction
def main():
    print("Select a mode:")
    print("1 - Encrypt a file")
    print("2 - Decrypt a file")
    print("3 - Encrypt a message")
    print("4 - Decrypt a message")
    mode = input("Enter mode (1, 2, 3, or 4): ")

    if mode in ["1", "2"]:
        file_path = input("Enter file path: ")
        if mode == "1":
            key = generate_or_load_key()
            encrypt_file(file_path, key)
        elif mode == "2":
            key = input_key()
            decrypt_file(file_path, key)
    elif mode in ["3", "4"]:
        key = generate_or_load_key() if mode == "3" else input_key()
        message = input("Enter the message: ")
        if mode == "3":
            encrypt_message(message, key)
        else:
            decrypt_message(message, key)
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()
