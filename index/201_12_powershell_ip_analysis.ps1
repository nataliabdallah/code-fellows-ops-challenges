# Script Name:              System Process Commands
# Author:                   Nathalie Abdallah
# Date of latest revision:  11/7/2023
# Purpose:                 Create a Powershell script that performs the following operations:

# Create a local file called network_report.txt that holds the contents of an ipconfig /all command.
# Use Select-String to search network_report.txt and return only the IP version 4 address.
# Remove the network_report.txt when you are finished searching it.

# Variables so I don't have to write out this entire path and name of file

$report = "C:\Users\network_report.txt"

# Function to create the Network Report file, highlight IPv4, erase the file, then display message the report was erased
Function Manage-NetworkReport {
    ipconfig /all > $report #this takes ipconfig info and creates and prints to file

    Select-String -Path $report -Pattern 'IPv4' # this highlights the ipv4 and displays its instances on powershell

    Remove-Item -Path $report # this removes the item

    Write-Output "Report erased"

}

# Main
Manage-NetworkReport