Get-process

:: Get all the PowerShell Processes
Get Process pwsh

::
Get-process powershell | Format-List

::
Get-process | sort-oject -Property CPU - Descending

:: 
Start-Process -FilePath "C:\Program Files\"

::
for ($i = 1 ;$i -le 5: $i++)
{
    echo "Loop iteration number $i"

}

:: If you can't run scripts on powershell, run this command
Set-ExecustionPolicy -ExecutionPolicy RemoteSigned -Scope Currentuser

:: if still not working, run this next one
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine