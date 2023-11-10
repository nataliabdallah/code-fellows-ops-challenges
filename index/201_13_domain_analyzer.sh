#!/bin/bash


#Script Name:               Domain Analyzer
# Author:                   Nathalie Abdallah
# Date of latest revision:  11/8/2023
# Purpose:                  Create a script that asks a user to type a domain, then displays information about the typed domain. Operations that must be used include:
# whois
# dig
# host
# nslookup

# Add to your bash script a sixth option that calls a function to:

# Take a user input string. Presumably the string is a domain name such as Google.com.
# Run whois against a user input string.
# Run dig against the user input string.
# Run host against the user input string.
# Run nslookup against the user input string.
# Output the results to a single .txt file and open it with your favorite text editor.

# For this challenge you must use at least one variable and one function.

# Variable


# Function to gather domain information and save it to a file


echo "Enter a website name"


read website

# text file output

report="${website}.txt"

# Run whois against a user input string.

echo "Webiste info gathered" 

whois $website | tee -a "$report"

# Run host against the user input string.

dig $website | tee -a "$report"

# Run nslookup against the user input string.

nslookup $website | tee -a "$report"

# Output the results to a single .txt file and open it with your favorite text editor.

host $website | tee -a "$report"

#For this challenge you must use at least one variable and one function.

echo "Your inquiry has been saved to $report"

# open the request

gedit "$report"