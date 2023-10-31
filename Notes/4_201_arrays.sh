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
#echo ${grocery_list} # the curly brackets and square brackets with the star is necessary: the stary means grab everything

# Prints out the total number of items on the list
# ADDING THE POUND sign in fron of the array name gives me the count of items in my list
#echo ${#gocery_list[2]}

# Append a new item to the list
new_snack=monster
#grocery_list+=($new_snack) #the paranthases direct it to put it at the end of the list, not in as part of place holder 0

# Add monster as the second item on the list
grocery_list[1]+=$new_snack

echo  ${grocery_list[*]}

# Print out the last item on the list
echo ${grocery_list[${#gocery_list[*]}-1]}

