#!/usr/bin/env python3

# Script Name:                  Challenge 27 Event Logging part 2/3
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      02/13/2023
# Sources:                      https://chat.openai.com/, https://github.com/codefellows/seattle-ops-301d10
# Purpose:                      Objectives

import logging
from logging.handlers import RotatingFileHandler
from cryptography.fernet import Fernet

# Configure logging with rotation
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
logFile = 'encryption_tool.log'

# Set up a rotating log handler
logHandler = RotatingFileHandler(logFile, mode='a', maxBytes=5*1024*1024,  # 5 MB
                                 backupCount=2, encoding=None, delay=0)
logHandler.setFormatter(log_formatter)
logHandler.setLevel(logging.INFO)

logger = logging.getLogger('root')
logger.setLevel(logging.INFO)
logger.addHandler(logHandler)

def generate_key():
    try:
        key = Fernet.generate_key()
        with open("401_mysecret.key", "wb") as key_file:
            key_file.write(key)
        logger.info("Key generated successfully.")
    except Exception as e:
        logger.error(f"Error generating key: {e}")

def load_key():
    try:
        return open("401_mysecret.key", "rb").read()
    except Exception as e:
        logger.error(f"Error loading key: {e}")
        raise e  # Re-raise exception after logging

def encrypt_message(message, key):
    try:
        encoded_message = message.encode()
        f = Fernet(key)
        encrypted_message = f.encrypt(encoded_message)
        logger.info("Message encrypted successfully.")
        return encrypted_message
    except Exception as e:
        logger.error(f"Error encrypting message: {e}")
        raise e

def decrypt_message(encrypted_message, key):
    try:
        f = Fernet(key)
        decrypted_message = f.decrypt(encrypted_message)
        logger.info("Message decrypted successfully.")
        return decrypted_message.decode()
    except Exception as e:
        logger.error(f"Error decrypting message: {e}")
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
    logger.critical("An unrecoverable error occurred.", exc_info=True)
