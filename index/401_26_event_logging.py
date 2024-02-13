
#!/usr/bin/env python3

# Script Name:                  Challenge 26 Event Logging part 1/3
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      02/13/2023
# Sources:                      https://chat.openai.com/, https://github.com/codefellows/seattle-ops-301d10
# Purpose:                      Objectives

import logging
from cryptography.fernet import Fernet

# Configure logging
logging.basicConfig(filename='encryption_tool.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_key():
    try:
        key = Fernet.generate_key()
        with open("401_mysecret.key", "wb") as key_file:
            key_file.write(key)
        logging.info("Key generated successfully.")
    except Exception as e:
        logging.error(f"Error generating key: {e}")

def load_key():
    try:
        return open("401_mysecret.key", "rb").read()
    except Exception as e:
        logging.error(f"Error loading key: {e}")
        raise e  # Re-raise exception after logging

def encrypt_message(message, key):
    try:
        encoded_message = message.encode()
        f = Fernet(key)
        encrypted_message = f.encrypt(encoded_message)
        logging.info("Message encrypted successfully.")
        return encrypted_message
    except Exception as e:
        logging.error(f"Error encrypting message: {e}")
        raise e

def decrypt_message(encrypted_message, key):
    try:
        f = Fernet(key)
        decrypted_message = f.decrypt(encrypted_message)
        logging.info("Message decrypted successfully.")
        return decrypted_message.decode()
    except Exception as e:
        logging.error(f"Error decrypting message: {e}")
        raise e

try:
    generate_key()
    key = load_key()
    # Example usage
    encrypted_message = encrypt_message("This is a secret message", key)
    print("Encrypted:", encrypted_message)
    decrypted_message = decrypt_message(encrypted_message, key)
    print("Decrypted:", decrypted_message)
except Exception as e:
    logging.critical("An unrecoverable error occurred.", exc_info=True)
