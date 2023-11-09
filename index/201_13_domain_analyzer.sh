#!/bin/bash


#Script Name:               Conditionals
# Author:                   Nathalie Abdallah
# Date of latest revision:  10/30/2023
# Purpose:                 Create a script that asks a user to type a domain, then displays information about the typed domain. Operations that must be used include:
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

# OUTPUT RESULTS INTO A .txt file 
gather_info() {
    domain="$1"
    echo "WHOIS Infromation:" > domain.txt
    whois "$domain" >> domain.txt

    echo -e "\nDIG Information:" >> domain.txt
    dig "$domain" >> domain.txt

    echo -e "\nHOST Information:" >> domain.txt
    host "$domain" >> domain.txt

    echo -e "\nNSLOOKUP Inforamtion:" >> domain.txt
    nslookup "$domain" >> domain.txt
    
    echo "Results save to domain.txt"

}

# Ask the User to Input a domain
read -p "Enter a domain name: " user_input

# Run the Function with user input
gather_info "$user_input"

#Open the file on Gedit
$editor domain.txt
                                   
done

