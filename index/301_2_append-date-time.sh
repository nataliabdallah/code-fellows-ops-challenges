#!/bin/bash

# Script Name:                  Challenge 2 Append Date Time
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      11/27/2023
# Sources:                      https://chat.openai.com/, https://github.com/codefellows/seattle-ops-301d10
# Purpose:                      Create a bash script that:

#Copies /var/log/syslog to the current working directory
#Appends the current date and time to the filename

# variables
copy="/var/log/syslog"
timestamp=$(date +"%Y-%m-%d-%H:%M:%S")
file="/home/$USER/Desktop/syslog_$timestamp"  # corrected file path and added missing double quote

# copy syslog file to the current working directory with timestamp
cp "$copy" "$file"  # added double quotes to handle paths with spaces

echo "command executed successfully!"

