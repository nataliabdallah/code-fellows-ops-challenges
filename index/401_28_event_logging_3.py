#!/usr/bin/env python3

# Script Name:                  Challenge 27 Event Logging part 3/3
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      02/14/2023
# Sources:                      https://chat.openai.com/, https://github.com/codefellows/seattle-ops-301d10
# Purpose:                      Objectives
# Use StreamHandler and FileHandler in your Python script.
# FileHandler should write to a local file.
# StreamHandler should output to the terminal.

# Include all features in 3/3 script

import logging
from logging.handlers import RotatingFileHandler
from cryptography.fernet import Fernet

# Configure logger
logger = logging.getLogger('encryption_tool')
logger.setLevel(logging.DEBUG)  # Set to DEBUG to capture all levels of logs

# Formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# FileHandler with log rotation
file_handler = RotatingFileHandler('encryption_tool.log', maxBytes=5*1024*1024, backupCount=2)
file_handler.setLevel(logging.INFO)  # Set to INFO for the file handler
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# StreamHandler for console output
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)  # Set to DEBUG for console to see all log levels
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

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
        raise e

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
    encrypted_message = encrypt_message("This is a secret message", key)
    logger.debug(f"Encrypted: {encrypted_message}")
    decrypted_message = decrypt_message(encrypted_message, key)
    logger.debug(f"Decrypted: {decrypted_message}")
except Exception as e:
    logger.critical("An unrecoverable error occurred.", exc_info=True)
