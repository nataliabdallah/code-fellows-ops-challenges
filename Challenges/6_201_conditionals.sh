#!/bin/bash


#Script Name:               Conditionals
# Author:                   Nathalie Abdallah
# Date of latest revision:  10/30/2023
# Purpose:                  Create a script that detects if a file or directory exists, then creates it if it does not exist. 
#                           Your script must use at least one array, one loop, and one conditional.

# Array to store directories
dirs=("north" "south" "east" "west")

# Loop that shows if directory exists
dir_in_array() {
    local dir_check="$1"
    for dir in "${dir[@]}"
    do
        if [ "$dir" = "$dir_check" ]
        then
            return 0 # boolean true; dir is in array
        fi
    done
    return 1 # boolean false; dir is not in array
}

get_name() {
    read -p "List the options in dirs (yes/no): " view # view directory
    if [ "$view" == "y" ] || [  "$view" == "yes"  ]
    then
        echo "Arrays: "
        echo "${dirs[@]}"
    fi

    # loop to ask for user input
    while true
    do
        read -p "Enter a directory name (type 'done' to finish): " dir_name

}



