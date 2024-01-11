#!/usr/bin/env python3

# Script Name:                  Challenge 401 Class 2
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      01/09/2024
# Sources:                      https://chat.openai.com/, https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-03/challenges/ops_challenge_3_demo.py
# Purpose:                      Requirements:

# In Python, add the below features to your uptime sensor tool.

# The script must:

# Ask the user for an email address and password to use for sending notifications.
# Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).
# Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event.


# TODO: import libraries

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# TODO: Create foundation for email

def send_email(sender_email, sender_password, receiver_email, subject, body):
    # Set up the MIME
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

# TODO: 

if __name__ == "__main__":
    try:
        # Get user email and password for notifications
        sender_email = input("Enter your email address: ")
        if not sender_email:
            sender_email = 'youremail.com'
        sender_password = input("Enter your email password (App Password for Gmail): ")
        if not sender_password:
            sender_password = "yourpassword from the app in gmail (not login passowrd))"
        receiver_email = input("Enter the administrator's email address: ")

        # Compose the email
        subject = "Test Notification"
        body = "This is a test email notification from your Python script."

        # Send the email notification
        send_email(sender_email, sender_password, receiver_email, subject, body)

        print("Email sent successfully.")
    except KeyboardInterrupt:
        exit("\nExiting the script")

