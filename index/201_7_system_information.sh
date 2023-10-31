#!/bin/bash


#Script Name:               System Information
# Author:                   Nathalie Abdallah
# Date of latest revision:  10/31/2023
# Purpose:                  Create a script that...

# Uses lshw to display system information to the screen about the following components:
# Name of the computer
# CPU
# Product
# Vendor
# Physical ID
# Bus info
# Width
# RAM
# Description
# Physical ID
# Size
# Display adapter
# Description
# Product
# Vendor
# Physical ID
# Bus info
# Width
# Clock
# Capabilities
# Configuration
# Resources
# Network adapter
# Description
# Product
# Vendor
# Physical ID
# Bus info
# Logical name
# Version
# Serial
# Size
# Capacity
# Width
# Clock
# Capabilities
# Configuration
# Resources
# Uses grep to remove irrelevant information from the lshw output
# Add text to the output clearly indicating which component (such as CPU, RAM, etc.) the script is returning information about
# Runs as Root; you may execute the shell script with sudo or as Root

# conditional
if [[  $EUID -ne 0  ]]
then
    echo "typo detected to Run type: sudo ./201_7_system_information.sh"
    exit 1
fi

# Function displays information for the specific component
display_component_info() {
    component="$1"
    echo "____*__*_***_-_* $component *_-_***_*__*_____"
    lshw -c $component | grep -E "description|product|vendor|physical id|bus info|width|clock|capabilities|configuration|resources|logical name|version|serial|size|capacity"
    echo
}

# Display info for each component
display_component_info "system"
display_component_info "cpu"
display_component_info "memory"
display_component_info "display"
display_component_info "network"

exit 0