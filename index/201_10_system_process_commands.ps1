# Script Name:              System Process Commands
# Author:                   Nathalie Abdallah
# Date of latest revision:  11/3/2023
# Purpose:                  Create a Powershell script that performs these operations on separate lines.

# The overall script is not designed to operate holistically, but rather act as a reference for how to execute various interesting operations with the process family of Powershell commandlets. Clearly indicate with comments each component below.
# Remember to follow this class's commenting requirements on all scripts.

# Print to the terminal screen all active processes ordered by highest CPU time consumption at the top.
Get-Process | Sort-Oject CPU -Descending | Format-Table
# Print to the terminal screen all active processes ordered by highest Process Identification Number at the top.
Get-Process | Sort-Object ID -Descending | Format-Table
# Print to the terminal screen the top five active processes ordered by highest Working Set (WS(K)) at the top.
Get-Process | Sort-Object WS -Descending | Select-Object -First 5 | Format-Table
# Start a browser process (such as Google Chrome or MS Edge) and have it open https://owasp.org/www-project-top-ten/.
Start-Process "chrome" "https://owasp.org/www-project-top-ten/"
# Start the process Notepad ten times using a for loop.
for ($i = 1; $i -le 10; $i++) {
    Start-Process "notepad"
}
# Close all instances of the Notepad.
Get-Process "notepad" | ForEach-Object { Stop-Process $_.Id }
# Kill a process by its Process Identification Number. Choose a process whose termination won't destabilize the system, such as Google Chrome or MS Edge.
$targetPID = 8776                           # this number will change according to what you want to kill
Stop-Process -Id $targetPID


