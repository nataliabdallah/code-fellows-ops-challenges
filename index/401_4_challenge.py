

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
