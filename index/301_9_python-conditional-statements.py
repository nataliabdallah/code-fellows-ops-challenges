#!/usr/bin/env python3

# Script Name:                  Challenge 9 Python Conditionals Statements
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      12/07/2023
# Sources:                      https://chat.openai.com/, https://github.com/codefellows/seattle-ops-301d10
# Purpose:                      Objectives
# Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met.

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions are not met.

# Create an if statement that includes both elif and else to execute when both if and elif are not met.

# Introduction
print("Welcome to the Python Scripting Tutorial!")
print("This script will guide you through creating conditional statements.")

# Explanation of the task
print("\nTask: Compare two objects based on their sizes.")
print("Object 1 is 'big', and Object 2 is 'small'.")

# Sample objects with sizes
big_object = "big"
small_object = "small"

# Explanation of the first if statement
print("\n1. Using the 'Equals' conditional:")
print("   Check if the big object is equal to the small object.")

# If statement using the "Equals" conditional
if big_object == small_object:
    print("   The big object is equal to the small object")
elif big_object != small_object:
    print("   The big object is not equal to the small object")

# Explanation of the next if statements
print("\n2. Using other conditionals:")
print("   Check if the big object is less than, less than or equal to, greater than, and greater than or equal to the small object.")

# If statement using the "Less than" conditional
if big_object < small_object:
    print("   The big object is less than the small object")

# If statement using the "Less than or equal to" conditional
if big_object <= small_object:
    print("   The big object is less than or equal to the small object")

# If statement using the "Greater than" conditional
if big_object > small_object:
    print("   The big object is greater than the small object")

# If statement using the "Greater than or equal to" conditional
if big_object >= small_object:
    print("   The big object is greater than or equal to the small object")

# Explanation of an if statement with both elif and else
print("\n3. Using 'elif' and 'else' keywords:")
print("   Compare the big object with another object named 'medium'.")

# Another object with a size
another_object = "medium"

# If statement with both elif and else
if big_object == another_object:
    print("   The big object is equal to another object")
elif big_object < another_object:
    print("   The big object is less than the other object")
elif big_object > another_object:
    print("   The big object is greater than the other object")
else:
    print("   The big object must be equal to, less than, or greater than the other object")

# Explanation of an if statement with only elif and else
print("\n4. Using only 'elif' and 'else' keywords:")
print("   Compare the big object with another object named 'large'.")

# Another object with a size
large_object = "large"

# If statement with only elif and else
if big_object == large_object:
    print("   The big object is equal to the other large object")
elif big_object < large_object:
    print("   The big object is less than the other large object")
else:
    print("   The big object is greater than or equal to the other large object")

# Conclusion
print("\nCongratulations! You have successfully created conditional statements in Python.")
