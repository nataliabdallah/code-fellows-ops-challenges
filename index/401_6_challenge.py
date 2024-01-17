from cryptography.fernet import Fernet
import os

# Generate or load a key for encryption and decryption
def generate_key():
    if os.path.isfile("secret.key"):
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    else:
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    return key

# Function to load the key from a file
def load_key_from_file(file_name="secret.key"):
    with open(file_name, "rb") as key_file:
        return key_file.read()

# Function to encrypt the file
def encrypt_file(file_path, key):
    f = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_path + ".encrypted", "wb") as file:
        file.write(encrypted_data)

# Function to decrypt the file
def decrypt_file(file_path, key):
    f = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_path.replace(".encrypted", ""), "wb") as file:
        file.write(decrypted_data)

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
    key = generate_key()
    
    print("Key is generated/loaded.")

    print("Select a mode:")
    print("1 - Encrypt a file")
    print("2 - Decrypt a file")
    print("3 - Encrypt a message")
    print("4 - Decrypt a message")

    mode = input("Enter mode (1, 2, 3, or 4): ")

    if mode in ["1", "2"]:
        file_path = input("Enter file path: ")
        if mode == "1":
            encrypt_file(file_path, key)
            print(f"File {file_path} has been encrypted.")
        elif mode == "2":
            decrypt_file(file_path, key)
            print("File decrypted successfully.")
    elif mode in ["3", "4"]:
        message = input("Enter the message: ")
        if mode == "3":
            encrypt_message(message, key)
        else:
            decrypt_message(message, key)
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()
