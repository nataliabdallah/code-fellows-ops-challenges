#!/usr/bin/env python3

# Script Name:                  Challenge 4 conditional in menu systems
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      12/04/2023
# Sources:                      https://chat.openai.com/, https://github.com/codefellows/seattle-ops-301d10
# Purpose:                      Before proceeding, ensure that course prework assignment “Setup Python” is complete.

# Microsoft Visual Studio Code is the recommended IDE for Python assignments throughout the Ops sequence.

# In Ubuntu, create a Python script that executes a few bash commands successfully. Indicate in comments how you achieved this.

# Requirements:

# The Python module “os” must be utilized.
# At least three variables must be declared and referenced in Python.
# The Python function print() must be used at least three times.
# Include execution of the following bash commands inside your Python script:

# whoami
# ip a
# lshw -short


# import OS (python library that allows you to interact with BASH)

import os


# variables- the .read() brings out the actual contents of the commands instead of the numbers associated with the os module that I can't understand
whoami = os.popen("whoami").read()
ipa = os.popen("ip a").read()
lshw = os.popen("lshw").read()

# Function print

print (whoami)
print (ipa)
print (lshw)




