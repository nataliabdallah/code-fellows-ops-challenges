#!/bin/bash

# Script:                     Loop 
# Author:                     Nathalie Abdallah
# Date of latest revision:    10/27/2024  
# Purpose:                    Ops 201 Challenge 05

# Requirements:
# Write a script that displays running processes, asks the user for a PID, then kills the process with that PID.
# Use a loop in your script.

# Declare variables
option="y"


# Main

# WHILE LOOP
While [ $option == "y" ]
do
    #Instructions for the while loop to execute

    # THis command prints out all running processes on the computer screen
    ps aux
 
    #Ask the user for a process ID
    echo -e"\nPlease give the PID of the process you would like to kill:"

    # Read in that input the user provided
    read pid

    # Kill the process using the pid the user gave us
    kill -9 $pid 

    # Ask the user if they wan to kill another process or exit the script
    echo -e "\nDo you want to kill another process? (y to continue / any other key to stop)"

    # REad in the input the user provided and put it in the variable called option
    read option

done