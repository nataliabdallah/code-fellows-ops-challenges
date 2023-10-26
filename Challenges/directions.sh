#!/bin/bash

# Script Name:                  Arrays 101
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      10/26/2023
# Purpose:                      Learn about arrays

# Define Variables
dir1=North
dir2=South
dir3=East
dir4=West

# Define array
compass=($dir1 $dir2 $dir3 $dir4)

# Print out the entire grocery list
echo  ${compass[*]}

# End

