#!/bin/bash

# Script Name:                  Arrays 101
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      10/26/2023
# Purpose:                      Learn about arrays

# Define Variables
PRICE_PER_APPLE=5,10,15 # this won't work
PRICE_PER_APPLE=5

# Define array
grocery_list=(apple bananas orange onion)

# Print out the entire grocery list
echo ${grocery_list} # the curly brackets and square brackets with the star is necessary: the stary means grab everything

# Append a new item to the list
new_snack=monster
grocery_list+= monster

echo  ${grocery_list[*]}