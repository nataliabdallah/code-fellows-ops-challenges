#!/bin/bash


#Script Name:               Conditionals
# Author:                   Nathalie Abdallah
# Date of latest revision:  10/30/2023
# Purpose:                  Create a script that detects if a file or directory exists, then creates it if it does not exist. 
#                           Your script must use at least one array, one loop, and one conditional.

# Array to check directories
directories=("a" "b" "c")

# for and do portion is the loop
for path in "${directories[@]}" # About the array and its connection to what I want regarding my array
do
# inside the loop [  -e "$path" ] is the condition. This condition checks the existence of a path or directory however you want to call it 
    if [ -e "$path" ] # check if the directory exists
    then 
        echo "$path already exists."
    else
        mkdir -p "$path" # if it doesn't exist create it (mkdir is the command in terminal or bash that creates the directory| the '-p' option ensures that intermediate
        echo "$path has been created."                              # directories are also created)
    fi
done

# Declare an array - contains a list of files
files=(file1.txt file2.txt file3.txt file4.txt)

# For Loop - that does a check for each file in my array - (do some action for each file in the list)           # Requirements
for file in "${files[@]}"
do
    # CONDITIONAL -CHECK IF FILE EXISTS (the action is the conditional)       
                                      # Commenting/Planning
    # If files exists then print out a statemnt telling the user that the file exists.
    if [ -f "$file" ]
    then    
        echo "$file exists"
    # Else statement - catch all other situations 
    else                                                              # If there is monster (buy)
        # Tell the user the file doesn't exist 
        echo "$file does not exist"                                   # else (buy sugar free)    
        # Ask the user if they want to create it or simply go ahead and create it
        touch $file
        echo "The $file has been created"
    fi

# Close out our for loop
done

