#!/bin/bash

# Script:                     Loop 
# Author:                     Nathalie Abdallah
# Date of latest revision:    10/27/2024  
# Purpose:                    Ops 201 Challenge 05

# Tasks
# Write a script that:
# Displays running processes
# Asks the user for a PID
# Kills the process with that PID
# Starts over at step 1 and continues until the user exits with Ctrl + C
# Use a loop so that the script will continuously start over, displaying the running processes, asking the user for input, etc.
# For this assignment, initialize a process that won't harm the OS's functionality upon termination. Don't kill essential processes required for the OS to work, such as kernel drivers.
# Hint: you can open a second terminal in your development environment and start it pinging one of your other machines. This will be a safe process to target.

# Array
kernel='(1 2 3 11 12 13 262 289 531 532 533 653 657 659 667 687 688 801 846 865 1028 1053 1352 1357 1401 1427 1612 1711 7050 7086 7216 7257)'

# WHILE LOOP
while true; do
  echo "Running processes:"  # display running processes
  ps auxf 
  read -p "Enter PID to kill (Ctrl + C to exit): " pid # ask user for PID

  if [ "$pid" != "$kernel"]; then
     # check if input is a valid PID
     if [ -z "$pid" ]; then
       echo "entered invalid PID, enter valid PID."
     else
       # check if PID is valid
       if ps -p "$pid" > /dev/null; then
         #  kill process
         kill "$pid"
         echo "Killed process with PID: $pid"
       else
         echo "No mathing process to $pid."
       fi
   fi

   else 
    echo "Process with PID $pid is excluded from termination"

  fi
done