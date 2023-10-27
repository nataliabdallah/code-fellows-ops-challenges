#!/bin/bash

# Script Name:                  OPS 201 Challenge 5 LOOPS
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      10/27/2023
# Purpose:                      Write 

# Objective

# Write 

# Task

# Diplays the runing processes
# Asks the user for a PID
# Kills the process with that PID
# Starts over 

# Define an array
names=("Bob" "Jane" "Mike" "Sarah")
COUNT=4
# FOR LOOP
# Basic syntax
for name in ${names[@]}
do
    echo $name
done

# WHILE LOOP
# Basic suntax
while [ $COUNT -gt 0 ]; do
    echo "Value of count is: $COUNT"
    COUNT=$(($COUNT -1)) # this is the line if you remove, it will create an infinite loop (hit cntrl-c to kill the loop)
done
# While (condition) is true, do the actions in the while loop, until that condition is not true. Infinite Loops: error when you don't implement that counter- to break out of the loop

echo "The condition is no longer true, we broke out of the while loop!"


# Main