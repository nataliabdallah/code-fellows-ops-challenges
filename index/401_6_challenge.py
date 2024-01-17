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

from cryptography.fernet import Fernet #imports the 'Fernet' class from 'cryptograpy.fernet' module
import os # imports os module, provides functions for interacting with the operating system

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

# Function to encrypt the file
def encrypt_file(file_path, key):                         # defines the function 'encrypt_file' which encrypts a file at the given path with the provided key
    f = Fernet(key)                                       # creates a new 'Fernet' object with the given key for encryption
    with open(file_path, "rb") as file:  # Opens the specified fine in binary read mode, reads its contents, and
        file_data = file.read()          # stores them in 'file_data'
    encrypted_data = f.encrypt(file_data)                 # encrypts the read data using the 'Fernet' object
    with open(file_path + ".encrypted", "wb") as file: # opens or creates a new file with '.encrypted' appended to the original
        file.write(encrypted_data)                     # original filename in binary write mode, and writes the encrypted data to this file.
    print(f"File {file_path} has been encrypted.") # prints a message indicating this file has been encrypted

# Function to decrypt the file
def decrypt_file(file_path, key): # defines the function 'decrypt_file' which decrypts a file at the given path with providied key
    f = Fernet(key)               # creates a new 'Fernet' object with the given key fro decryption
    with open(file_path, "rb") as file:  # opens the specified file in binary read mode and
        encrypted_data = file.read()     # reads the encrypted data
    decrypted_data = f.decrypt(encrypted_data)  # decrypts the encrypted data using the 'Fernet' object
    with open(file_path.replace(".encrypted", ""), "wb") as file:  # open/creates a new file with .'encrypted' removed from the 
        file.write(decrypted_data)                                 # filename in binary write mode, and writes the decrypted data to this file
    print("File decrypted successfully.")  # prints a message indicating the file has ben decrypted succesfully

# Function to encrypt a message
def encrypt_message(message, key):  # defines the function 'encrypt_message', encrypts a string using provided key
    f = Fernet(key)               # creates a 'Fernet' object with the given key for encryption
    encrypted_message = f.encrypt(message.encode()) # encrypyts the message after encoding it to bytes
    print("Encrypted Message: " + encrypted_message.decode()) # prints the encrypted message after 
                                                              # decoding it back to a string
# Function to decrypt a message
def decrypt_message(encrypted_message, key):  # defines the function 'decrypt_message', decrypts the string inputted using provided key
    f = Fernet(key)                         # creates a 'Fernet' object with the given key for decryption
    decrypted_message = f.decrypt(encrypted_message.encode()) # decrypts the encrypted message after encoding it to bytes
    print("Decrypted Message: " + decrypted_message.decode()) # prints the decrypted message after decoding it back to a string

# Main function to handle user interaction
def main():                                # defines the 'main' function, serves as the entry point for user interactions with the script
    print("Select a mode:")  # prints the message asking user to select mode
    print("1 - Encrypt a file")                   # these print
    print("2 - Decrypt a file")                   # the options
    print("3 - Encrypt a message")                # available to the user
    print("4 - Decrypt a message")
    mode = input("Enter mode (1, 2, 3, or 4): ") # asks the user to enter their choice of mode and
#                                                # stores the input in the variable 'mode'
    if mode in ["1", "2"]:  # checks if the user's input for 'mode' is either 1 or 2
        file_path = input("Enter file path: ") # if the mode is for file operations, it prompts user to enter file path and stores the input in the variable 'file_path'
        if mode == "1":                  # within file operations, checks if the mode is 1
            key = generate_or_load_key() # calls 'generate_or_load_key()' to get the ecryption key, either generting or loading an existing
            encrypt_file(file_path, key) # calls 'ecrypt_file()' function witht the file path and the key to encrypt the file
        elif mode == "2": # check if the mode is 2
            key = input_key() # call 'input_key()' to let the user input the decryption key or specify a file to read the key from
            decrypt_file(file_path, key) # call 'decrypt_file()' function with the file path and the key to decrypt the file
    elif mode in ["3", "4"]:  # checks if the user's input for 'mode' is either 3 or 4
        key = generate_or_load_key() if mode == "3" else input_key() # for mode 3: calls 'generate_or_load_key(); for mode 4: calls 'input_key()'
        message = input("Enter the message: ") # asks the user to enter a message to be encrypted
        if mode == "3": # checks if the mode is 3
            encrypt_message(message, key) # calls 'encrypt_message()' with the message and the key to encrypt the key
        else:                            # the alternative for message operations (mode 4)
            decrypt_message(message, key) # calls 'decrypt_message()' with the encrypted messae and the key to decrypt it
    else:                              # if entered mode is not 1-4
        print("Invalid mode selected.")# it prints an error message

if __name__ == "__main__": # standard python phrase for running 'main' function when the script is 
    main()                 # executed as the main program (not imported as a module in another script)
