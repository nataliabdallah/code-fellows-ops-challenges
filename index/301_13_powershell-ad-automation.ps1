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

# Dynamically retrieve available OU options
$OUOptions = Get-ADOrganizationalUnit -Filter * | Select-Object -ExpandProperty Name
$OUChoice = $null

# Display options to the user
do {
    Write-Host "Select an Organizational Unit (OU) path:"
    for ($i=0; $i -lt $OUOptions.Count; $i++) {
        Write-Host "$($i + 1). $($OUOptions[$i])"
    }
    
    $OUChoice = Read-Host "Enter the number corresponding to your choice"
} while ($OUChoice -lt 1 -or $OUChoice -gt $OUOptions.Count)

# Map the user's choice to the OU path
$SelectedOU = $OUOptions[$OUChoice - 1]
$OUPath = "OU=$SelectedOU,DC=corp,DC=globexpower,DC=com"

# Prompt the user for input
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

# Create the new user
try {
    New-ADUser -SamAccountName $SamAccountName -UserPrincipalName $UserPrincipalName -GivenName $FirstName -Surname $LastName -Name "$FirstName $LastName" -DisplayName "$LastName, $FirstName" -Office $Office -Department $Department -Title $Title -City $City -State $State -Company $Company -EmailAddress $EmailAddress -AccountPassword $SecurePassword -Enabled $true -Path $OUPath -ErrorAction Stop

    # Display success message
    Write-Host "User $FirstName $LastName created successfully."
    
    # Optional: Retrieve and display the user information
    Get-ADUser -Filter {SamAccountName -eq $SamAccountName} | Format-Table -Property SamAccountName, GivenName, Surname, UserPrincipalName, Office, Department, Title, City, State, Company, EmailAddress
}
catch {
    # Display error message
    Write-Host "Error creating user: $_"
}

