#!/bin/bash


#Script Name:               Conditionals
# Author:                   Nathalie Abdallah
# Date of latest revision:  10/30/2023
# Purpose:                  Create a script that detects if a file or directory exists, then creates it if it does not exist. 
#                           Your script must use at least one array, one loop, and one conditional.

# Array to check directories
directories=("a" "b" "c")

# for and do portio is the loop
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