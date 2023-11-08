:: Script Name:              System Process Commands
:: Author:                   Nathalie Abdallah
:: Date of latest revision:  11/7/2023
:: Purpose:                 Create a Powershell script that performs the following operations:

:: Create a local file called network_report.txt that holds the contents of an ipconfig /all command.
:: Use Select-String to search network_report.txt and return only the IP version 4 address.
:: Remove the network_report.txt when you are finished searching it.

# Variables so I don't have to write out this entire path and name of file


$create_report = ipconfig /all > C:\Users\natali\Documents\network_report.txt  # This creates the file and inputs the info ipconfig all
$Pluck_IP4 = Select-String -Path C:\Users\natali\Documents\network_report.txt -Pattern 'IPv4' # once the file is created, this string that will print out on powershell will be anything where this keyword is used IPv4
$Erase = rm C:\Users\natali\Documents\network_report.txt; echo "Report erased"

# Functions that will create the file with IPCONFIG all data, then pluck out IPv4 from the file, and display it onto Powershel, then delete the file that was created.
Function Create-NetworkReport {
    $create_report
}

Function Get-IPV4 {
    Write-Output $Pluck_IP4
   
}

Function Erase-Report {
    $Erase
}

# Main

Create-NetworkReport
Get-IPv4
Erase-Report