#!/bin/bash

# Script Name:                  Functions
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      10/25/2023
# Purpose:                      Print simple Functions

# Declaration of variables

# One equal sign means assigining a value
# Two is comparing values

WHO=`whoami`

# Declaration of functions
# Basic function that handles printing the greeting to the screen
print_greeting () {
    echo "HELLO WORLD"
    echo "This is our first function"
    echo "The person running this script is $WHO"
}

# Main

# CALL THE FUNCTION - TELL THE COMPUTER TO DO THE THING
print_greeting

# End