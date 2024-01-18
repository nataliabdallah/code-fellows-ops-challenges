# Script Name:                  Challenge 401 Class 7
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      01/17/2024
# Sources:                      https://chat.openai.com/, https://www.youtube.com/watch?v=vk4WWIreH8Q, https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python, https://pypi.org/project/cryptography/
# Purpose:                      In Python, create a script that utilizes the cryptography library to:

# encrypt and decrypt the entire contents of what is in a folder

# this script calls on 401_7_challenge.py, attempt to test options 5 and 6 to script: 401_6_challenge.py

from cryptography.fernet import Fernet
import os
# Import the folder operations from the other script
from one_401_7_challenge import encrypt_folder, decrypt_folder

# Generate or load a key for encryption and decryption
def generate_or_load_key(): # defines the function 'generate_or_load_key' 
    if os.path.isfile("secret.key"): # checks if there is a file named 'secret.key' in the current directory
        with open("secret.key", "rb") as key_file: 
            key = key_file.read() # 'with open' - if secret.key exists, it opens the file in binary read mode 'rb' and reads the key from it
    else:
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:   # from 'else-return' if 'secret.key' doesn't exist, it generates a new key using 
            key_file.write(key)                      # 'Fernet.generate_key()' creates 'secre.key', write the key into it in binary write mode 'wb'
    return key

# Function to manually input a key or read from a file
def input_key():                                          # defines the funtion 'input_key'- handles the user's input for the encryption key
    key_input = input("Enter the key or key file name: ") # prompts the user to enter either a key directly, or a filename containing the key
    if os.path.isfile(key_input):                         # checks if the input string is a valid filename in the current directory
        with open(key_input, "rb") as key_file:           # if the input is a valid filename, it opens the file in 'rb' and returns the key read form the file
            return key_file.read()
    else:                                                 # if the input is not a filename, it treats input as the key itself and encodes it to bytes before returning
        return key_input.encode()




def main():
    print("Select a mode:")
    print("5 - Encrypt a folder")
    print("6 - Decrypt a folder")
    mode = input("Enter mode (1, 2, 3, 4, 5, or 6): ")

    # 
    if mode == "5":
        path = input("Enter folder path to encrypt: ")
        key = generate_or_load_key()
        encrypt_folder(path, key)
    elif mode == "6":
        path = input("Enter folder path to decrypt: ")
        key = input_key()
        decrypt_folder(path, key)

    # 
if __name__ == "__main__":
    main()
