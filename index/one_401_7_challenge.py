# Script Name:                  Challenge 401 Class 7
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      01/17/2024
# Sources:                      https://chat.openai.com/, https://www.youtube.com/watch?v=vk4WWIreH8Q, https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python, https://pypi.org/project/cryptography/
# Purpose:                      In Python, create a script that utilizes the cryptography library to:

# encrypt and decrypt the entire contents of what is in a folder

# this script is part of 401_6_challenge.py
# It is meant to be called on from the main script: 401_6_challenge.py

from cryptography.fernet import Fernet
import os

# Function to recursively encrypt a folder
def encrypt_folder(folder_path, key):
    f = Fernet(key)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as file:
                file_data = file.read()
            encrypted_data = f.encrypt(file_data)
            with open(file_path + ".encrypted", "wb") as file:
                file.write(encrypted_data)
            os.remove(file_path)
    print(f"Folder {folder_path} and its contents have been encrypted.")

# Function to recursively decrypt a folder
def decrypt_folder(folder_path, key):
    f = Fernet(key)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".encrypted"):
                file_path = os.path.join(root, file)
                with open(file_path, "rb") as file:
                    encrypted_data = file.read()
                decrypted_data = f.decrypt(encrypted_data)
                with open(file_path.replace(".encrypted", ""), "wb") as file:
                    file.write(decrypted_data)
                os.remove(file_path)
    print(f"Folder {folder_path} and its contents have been decrypted.")
    
    
