#!/usr/bin/env python3

# Script Name:                  Challenge 401 Class 2
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      01/12/2024
# Sources:                      https://chat.openai.com/, https://downloads.cisecurity.org/#/, 
# Purpose:                      PowerShell Script to automate CIS 9019 Windows Server Rule: 1.1.5(L)

# 1.1.5 (L1) Ensure 'Minimum password length' is set to '14 or more 
# (Automated)




function Set-MinimumPasswordLength {
    param (
        [int]$Length = 14  # Set default length to 14
    )
    $tempPath = "$env:temp\secpol.cfg"
    $dbPath = "$env:windir\security\local.sdb"
    $logPath = "$env:windir\security\logs\scesrv.log"

    # Export current security settings
    secedit /export /cfg $tempPath > $null

    # Modify the Minimum Password Length setting
    $content = Get-Content $tempPath
    $content = $content -replace "MinimumPasswordLength\s*=\s*\d", "MinimumPasswordLength = $Length"
    Set-Content $tempPath -Value $content

    # Import the modified settings
    secedit /import /cfg $tempPath /db $dbPath /log $logPath /quiet > $null

    # Enforce the updated policies
    secedit /configure /db $dbPath /cfg $tempPath /log $logPath /quiet > $null
}

# Setting the minimum password length to 14
Set-MinimumPasswordLength
