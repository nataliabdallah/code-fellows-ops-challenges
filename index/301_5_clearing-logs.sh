#!/bin/bash

# Script Name:                  Challenge 4 conditional in menu systems
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      12/01/2023
# Sources:                      https://chat.openai.com/, https://github.com/codefellows/seattle-ops-301d10
# Purpose:                     Write a bash script that performs the following tasks:

# Print to the screen the file size of the log files before compression
# Compress the contents of the log files listed below to a backup directory
# /var/log/syslog
#  /var/log/wtmp
# The file name should contain a time stamp with the following format -YYYYMMDDHHMMSS
# Example: /var/log/backups/syslog-20220928081457.zip
# Hint: gzip is a preinstalled Linux application for performing zip formatted compression.

# Clear the contents of the log file
# Print to screen the file size of the compressed file
# Compare the size of the compressed files to the size of the original log files

# variables
challenge5="$HOME/challenge5"

timestamp=$(date +"-%Y%m%d%H%M%S")


# prints size of syslogs and wtmp
size_syslog=$(du -h /var/log/syslog | awk '{print $1}')
echo "Size of /var/log/syslog: $size_syslog"

size_wtmp=$(du -h /var/log/wtmp | awk '{print $1}')
echo "Size of /var/log/wtmp: $size_wtmp"

# Compress the log files into a single zip file with timestamp suffix
filezip="syslogs${timestamp}.zip"
zip -r "$challenge5/$filezip" /var/log/syslog /var/log/wtmp
echo "Compression completed"

# Clear the contents of the original log files
sudo truncate -s 0 /var/log/syslog
sudo truncate -s 0 /var/log/wtmp

echo "Contents of syslog and wtmp cleared"

# Prints the size of the compressed file
size_comp=$(du -h "$challenge5/$filezip" | awk '{print $1}')
echo "Size of compressed file ($filezip): $size_comp"

# Prints the size of the original log files for comparison
echo "Size of syslog before compression: $size_syslog"
echo "Size of wtmp before compression: $size_wtmp"
