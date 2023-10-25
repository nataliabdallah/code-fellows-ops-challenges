#!/bin/bash

# Script Name:                  Hello World
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      10/25/2023
# Purpose:                      Print asomething to the screen

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

# Main

echo $greeting
x="Hello World"
echo $x
echo "The price of an apple today is: $PRICE_PER_APPLE"
echo "The first ten letters of the alphabet are: ${MyFirstLetters}DEFGHIJ"
echo "This folder contains the following $FILES"
echo "The person running this script is $WHO"

# End