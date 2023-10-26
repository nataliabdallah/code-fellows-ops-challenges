#!/bin/bash

# Script Name:                  Variables
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      10/25/2023
# Purpose:                      Explains and gives examples of Variables

# Declaration of variables

# PRICE OF APPLES
# One equal sign means assigining a value
# Two is comparing values
PRICE_PER_APPLE=5
MyFirstLetters=ABC
greeting="Hello world"
FILES=`ls`
WHO=`whoami`

# Declaration of functions
# Basic function that handles printing the greeting to the screen
print_greeting () {
    echo "HELLO WORLD:
    echo "This is our first function"
    echo "The person running this script is $WHO"
}


# Main

# CALL THE FUNCTION - TELL THE COMPUTER TO DO THE THING
print_greeting

print_greeting

#echo $greeting

#echo "The price of an apple today is: $PRICE_PER_APPLE"
#echo "The first ten letters of the alphabet are: ${MyFirstLetters}DEFGHIJ"
#echo "This folder contains the following $FILES"
#echo "The person running this script is $WHO"

# End

#!/bin/bash

# Script Name:                  Review Variables and Functions
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      10/26/2023
# Purpose:                      Review


# Declaration of variables
num1=25
num2=5
num3=10

# Notes: 1 set of paranthases is for the function
# 2 sets is for the mathematics

# Declare function
add_some_numbers() {
    sum=$(($num1+$num3))
    echo $sum
}

# Main
# Call the function
add_some_numbers

# End

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
grocery_list+=" monster"

echo  ${grocery_list[*]}

# End

