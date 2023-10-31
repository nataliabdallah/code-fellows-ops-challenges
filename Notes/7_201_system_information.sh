#!/bin/bash


#Script Name:               System Information
# Author:                   Nathalie Abdallah
# Date of latest revision:  10/30/2023
# Purpose:                  Create a script that...

# Uses lshw to display system information to the screen about the following components:

# Name of the computer|CPU|Produc|Vendor|Physical ID|Bus Info|Width|RAM|Description|Physical ID|Size|Display adapter|Description|Product|Vendor|Physical ID|Size|Display adapter
# Description|Product|Vendor|Physical ID|Bus Info|Width|Clock|Capabilities|Configuration|Resources|Network adapter|Descritpion|Product|Vendor|Physical ID|Bus Info|Logical name
# Version|Serial|Size|Capacity|Width|Clock|Capabilities|Configuration|Resources

# Uses grep to remove irrelevant information from the lshw output
# Add text to the output clearly indicating which component (such as CPU, RAM, etc.) the script is returning information about
# Runs as Root; you may execute the shell script with sudo or as Root

#!/bin/bash


# Main

# Search the output of lshw command and return every line with the word bridge in it
lshw | grep "bridge" #the pipe grabs the output on the left and feeds it to the command on the right hand side (Super Mario pipes) 

# in the hardware info, grep will look for everything that contains the name bridge
