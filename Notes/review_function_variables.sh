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

