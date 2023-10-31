#Script Name:               Retrieval via PowerShell
# Author:                   Nathalie Abdallah
# Date of latest revision:  10/31/2023
# Purpose:                  Create a script that...

# Create a Powershell script that performs these operations on separate lines. The overall script is not designed to operate holistically, but rather act as a reference for how to execute various interesting operations with the process family of Powershell commandlets. Clearly indicate with comments each component below.

# Remember to follow this class's commenting requirements on all scripts.

# Output all events from the System event log that occurred in the last 24 hours to a file on your desktop named last_24.txt.
# Output all "error" type events from the System event log to a file on your desktop named errors.txt.
# Print to the screen all events with ID of 16 from the System event log.
# Print to the screen the most recent 20 entries from the System event log.'
# Print to the screen all sources of the 500 most recent entries in the System event log. Ensure that the full lines are displayed (get rid of the ... and show the entire text).




# Output all events from the System event log that occured in the last 24 hourse to a file on your desktop named last_24.txt.
Get_WinEvent -LogName System -FilterHashtable @{LogName='System'; StartTime=(Get-Data).AddDays(-1)} | Out-File "$env:USERPROFILE\Desktop\last_24.txt"

# Output all "error" type events from the System event log to a file on your desktop named errors.txt.
Get-WinEvent -LogName System -ErrorLevel "Error" | Out-File "$env:USERPROFILE\Desktop\errors.txt"

# Print to the screen all events with ID of 16 from the System event log.
Get-WinEvent -LogName System | Where-Object { $_.Id -eq 16 } | Format-Table -AutoSize

# Print to the screen the most recent 20 entries from the System event log.
Get-WinEvent -LogName System -MaxEvents 20 | Format-Table -AutoSize

# Print to the screen all sources of the 500 most recent entries in the System event log. Ensure that the full lines are displayed.
Get-WinEvent -LogName System -MaxEvents 500 | Select-Object -ExpandProperty ProviderName