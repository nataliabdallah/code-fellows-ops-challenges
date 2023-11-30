#!/bin/bash

# Script Name:                  Challenge 3 File Permissions
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      11/29/2023
# Sources:                      https://chat.openai.com/, https://github.com/codefellows/seattle-ops-301d10
# Purpose:                     Create a new bash script that performs the following:

# Prompts user for input directory path.
# Prompts user for input permissions number (e.g. 777 to perform a chmod 777)
# Navigates to the directory input by the user and changes all files inside it to the input setting.
# Prints to the screen the directory contents and the new permissions settings of everything in the directory.


# Prompts user for input
read -p "Enter your Folder or Folder Path:" first_value

# Prompts user for input: permissions number
read -p "Enter permissions in Format (000): " second_value

# Changes permissions of the directories
chmod -R "$second_value" "$first_value"

# Prints the final product: directory contents, new permissions settings
echo -e "\nDirectory contents after changing permissions:"
ls -al

echo -e "\nPermissions updated succesfully"
