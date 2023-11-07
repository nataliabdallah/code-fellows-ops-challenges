:: Script Name:              System Process Commands
:: Author:                   Nathalie Abdallah
:: Date of latest revision:  11/7/2023
:: Purpose:                 Create a Powershell script that performs the following operations:

:: Create a local file called network_report.txt that holds the contents of an ipconfig /all command.
:: Use Select-String to search network_report.txt and return only the IP version 4 address.
:: Remove the network_report.txt when you are finished searching it.

:: Variables so I don't have to write out this entire path and name of file

$target = "network_report.txt"
$path = "C:\Users\natali\Documents\"

:: Function that puts all the info of ipconfig all onto the .txt
ipconfig /all > $path$target

echo "created report"

:: once the file is created, this string that will print out on powershell will be anything where this keyword is used IPv4
Select-String -Path $path$target -Pattern 'IPv4'

:: Removes the file after it's been opened
if (Test-Path -Path $path$target -PathType) {
    :: this gets the process that has the file opened
    $process = Get-Process -Id (Get-ItemProperty -Path $filePath).ProcessId

    :: Waits for the process to Close
    Wait-Process -Id $process.Id

    :: Deletes the file
    Remove-Item -Path $filepath -Force
}

