#!/usr/bin/env python3

# Script Name:                  Challenge 8 Python Collections
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      12/07/2023
# Sources:                      https://chat.openai.com/, https://github.com/codefellows/seattle-ops-301d10
# Purpose:                      Objectives
# Create a Python script that includes the following:

# Assign to a variable a list of ten string elements.
# Print the fourth element of the list.
# Print the sixth through tenth element of the list.
# Change the value of the seventh element to “onion”.

#Step 1: Assign a list of ten string elements to a variable

my_list = ["element1", "element 2", "element3", "element4", "element5", "element6", "element7", "element8", "element9", "element10"]

# Step 2: Print the fourth element of the list
print("step2: print the fourth element of the list")
print("Fourth element:", my_list[3])
print()

# step 3: Print the sixth through tenth element of the list
print("step 3: print the 6-10 elements of the list")
print("6-10 elements:", my_list[5])
print()

#step4: Change the value of the seventh element to "onion"
print("step4: Change the value of the seventh element to 'onion'")
my_list[6] = "onion"

# step 5: print the updated list
print("step 5: print the updated list")
print("Updated list:", my_list)