#!/bin/bash

# Script Name:                  File Permissions
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      11/29/2023
# Sources:                      https://chat.openai.com/, https://github.com/codefellows/seattle-ops-301d10
# Purpose:                      Create a bash script that launches a menu system with the following options:
# Hello world (prints "Hello world!" to the screen)
# Ping self (pings this computer's loopback address)
# IP info (print the network adapter information for this computer)
# Exit
# Next, the user input should be requested.
# The program should next use a conditional statement to evaluate the user's input, then act according to what the user selected.
# Use a loop to bring up the menu again after the request has been executed

while true; do
    # Display menu options
    echo "Menu:"
    echo "1. Hello World"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"

    # Prompt user for input
    read -p "Enter your choice (1-4): " choice

    # Evaluate user input using a case statement
    case $choice in
        1)
            echo "Hello world!"
            ;;
        2)
            ping -c 4 127.0.0.1
            ;;
        3)  
            ip a
            ;;
        4)
            echo "Exiting menu. Goodbye!"
            exit 0
            ;;
        *)
            echo "Invalid input. Choose 1 of the 4 choices."
            ;;
    esac
done
