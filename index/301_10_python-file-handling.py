#!/usr/bin/env python3

# Script Name:                  Challenge 10 Python Conditionals Statements
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      12/08/2023
# Sources:                      https://chat.openai.com/, https://github.com/codefellows/seattle-ops-301d10
# Purpose:                      Objectives
# Using file handling commands, create a Python script that creates a new .txt file, appends three lines, prints to the screen the first line, then deletes the .txt file

# Explanation of the script
explanation = """
This script demonstrates basic file handling operations in Python:

1. It creates a new text file named 'example.txt'.
2. Appends three lines of text to the file.
3. Reads and prints the first line from the file.
4. Deletes the 'example.txt' file.

Now, let's walk through each step:

Step 1: Create a new .txt file
    with open('example.txt', 'w') as file:
        file.write('This is the first line.\\n')
        file.write('This is the second line.\\n')
        file.write('This is the third line.\\n')

Press Enter to continue...
"""

# Print the explanation and execute Step 1
print(explanation)
input()

# Execute Step 1
exec("""
# Create a new .txt file
with open('example.txt', 'w') as file:
    file.write('This is the first line.\\n')
    file.write('This is the second line.\\n')
    file.write('This is the third line.\\n')
""")
print("Step 1 executed successfully.")

# Step 2: Read and print the first line
explanation_step_2 = """
Step 2: Read and print the first line
    with open('example.txt', 'r') as file:
        first_line = file.readline()
        print("First line:", first_line)

Press Enter to continue...
"""
print(explanation_step_2)
input()

# Execute Step 2
exec("""
# Read and print the first line
with open('example.txt', 'r') as file:
    first_line = file.readline()
    print("First line:", first_line)
""")

# Step 3: Delete the .txt file
explanation_step_3 = """
Step 3: Delete the .txt file
    import os
    os.remove('example.txt')

Press Enter to continue...
"""
print(explanation_step_3)
input()

# Execute Step 3
exec("""
# Delete the .txt file
import os
os.remove('example.txt')

print("File deleted successfully.")
""")

# Final message
print("Script execution complete.")
