#!/bin/bash


#Script Name:               Conditionals
# Author:                   Nathalie Abdallah
# Date of latest revision:  10/30/2023
# Purpose:                  Create a script that detects if a file or directory exists, then creates it if it does not exist. 
#                           Your script must use at least one array, one loop, and one conditional.

# Array to check directories
directories=("a" "b" "c")


for path in "${directories[@]}" # About the array and its connection to what I want regarding my array
do
    if [ -e "$path" ] # check if the directory exists
    then 
        echo "$path already exists."
    else
        mkdir -p "$path" # if it doesn't exist create it
        echo "$path has been created."
    fi
done