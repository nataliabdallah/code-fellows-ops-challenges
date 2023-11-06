:: Script Name:              System Process Commands
:: Author:                   Nathalie Abdallah
:: Date of latest revision:  11/6/2023
:: Purpose:                  Write a Powershell script that automates the configuration of a new Windows 10 endpoint. Your script should perform the following:

:: Enable File and Printer Sharing
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False
:: Allow ICMP traffic
netsh advfirewall firewal add rule name= "Allow incoming ping requests IPv4"  dir+in action=allow protocol=icmpv4
:: Enable Remote management
reg add "HKLM\SYSTEM\CurrentcontrolSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
:: Remove bloatware
iex ((New-Object System.Net.WebClient).DownloadString('https://git.io/debloat'))
:: Enable Hyper-V
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
:: Disable SMBv1, an insecure protocol
Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force