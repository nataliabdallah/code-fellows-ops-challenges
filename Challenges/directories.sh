#!/bin/bash

# Script Name:                  Directories
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      10/26/2023
# Purpose:                      Create 4 directories and create .txt file in each directory
# Define Variables
dir1=north
dir2=south
dir3=east
dir4=west

# Define array
directories=("$dir1" "$dir2" "$dir3" "$dir4")

# create a .txt file in each directory

for dir in ${directories[*]}; do
    mkdir -p "$dir" #creates the directory if it doesn't exist
    touch "$dir/file.txt"

    done

# End
