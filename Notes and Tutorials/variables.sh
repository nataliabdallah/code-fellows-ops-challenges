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