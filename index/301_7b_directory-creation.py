#!/usr/bin/env python3

# Script Name:                  Challenge 7 Directory Creation (simplified)
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      12/05/2023
# Sources:                      https://chat.openai.com/, https://github.com/codefellows/seattle-ops-301d10
# Purpose:                      Create a Python script that generates all directories, sub-directories and files for a user-provided directory path.
# b:                            simplified version to understand scripting 

# Script must ask the user for a file path and read a user input string into a variable.
# Script must use the os.walk() function from the os library.
# Script must enclose the os.walk() function within a python function that hands it the user input file path.



# Import libraries
import os

# Declaration of functions
def generate_directory_structure(directory):
    for (root, dirs, files) in os.walk(directory):
        # Add a print command here to print ==root==
        print("==folder==")
        print(root)
        # Add a print command here to print ==dirs==
        print("==sub-folders==")
        print(dirs)
        # Add a print command here to print ==files==
        print("==files==")
        print(files)

# Main
# Read user input into a variable
directory = input("Enter the name of a directory in your current directory(folder) or directory path: ")

# Pass the variable into the function
generate_directory_structure(directory)
