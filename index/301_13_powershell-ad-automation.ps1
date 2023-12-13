#Script Name:               Powershell AD Automation
# Author:                   Nathalie Abdallah
# Date of latest revision:  12/13/2023
# Purpose:                  Overview

# Powershell can be a powerful tool in administering Active Directory (AD) users and computers. Today you'll write a Powershell script to add a new user to AD.

# Resources

# You will need a Windows Server with AD DS installed and the server promoted to Domain Controller
# Microsoft Documentation: New-ADUser{:target="_blank"}
# Objectives

# In your Windows Server, access Powershell ISE.

# Write a Powershell script that adds the below person to AD.
# Franz Ferdinand is the TPS Reporting Lead at GlobeX USA in Springfield, OR office. Franz is part of the TPS Department. Franz's email is ferdi@GlobeXpower.com.
# Test your script. Verify in ADAC that the user was created with the correct attributes. If anything is missing, delete the user in ADAC and re-attempt from Powershell ISE.

$FirstName = Read-Host "Enter first name"
$LastName = Read-Host "Enter last name"
$SamAccountName = Read-Host "Enter SamAccountName"
$UserPrincipalName = Read-Host "Enter UserPrincipalName"
$Office = Read-Host "Enter office"
$Department = Read-Host "Enter department"
$Title = Read-Host "Enter title"
$City = Read-Host "Enter city"
$State = Read-Host "Enter state"
$Company = Read-Host "Enter company"
$EmailAddress = Read-Host "Enter email address"

# Prompt for password input
$SecurePassword = Read-Host "Enter password" -AsSecureString

# Specify the path to the Organizational Unit (OU) where you want to create the user
$OUPath = Read-Host "Enter Organizational Unit (OU) path"

# Create the new user
New-ADUser -SamAccountName $SamAccountName -UserPrincipalName $UserPrincipalName -GivenName $FirstName -Surname $LastName -Name "$FirstName $LastName" -DisplayName "$LastName, $FirstName" -Office $Office -Department $Department -Title $Title -City $City -State $State -Company $Company -EmailAddress $EmailAddress -AccountPassword $SecurePassword -Enabled $true -Path $OUPath

# Display success message
Write-Host "User $FirstName $LastName created successfully."

# Optional: Retrieve and display the user information
Get-ADUser -Filter {SamAccountName -eq $SamAccountName} | Format-Table -Property SamAccountName, GivenName, Surname, UserPrincipalName, Office, Department, Title, City, State, Company, EmailAddress

