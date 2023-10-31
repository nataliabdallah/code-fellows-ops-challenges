#!/bin/bash

# Script Name:                  Undo Challenge 4
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      10/26/2023
# Purpose:                      Challenge 4 Creates 4 directories and creates .txt file in each directory
#                               Automation 4 will delete those files and the directories
# Define Variables
dir1=north
dir2=south
dir3=east
dir4=west

# Define array
directories=("$dir1" "$dir2" "$dir3" "$dir4")

# delete a .txt file in each directory

for dir in ${directories[*]}; do
    rm "$dir/file.txt"
    rmdir -p "$dir" #deletes the directory if it finds it exists
    done

# End
