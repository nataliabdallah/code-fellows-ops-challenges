@echo off
setlocal enabledelayedexpansion


:: Prompt the user to input the source folder path
set /p "sourceFolder=Enter the source folder path: "


:: Check if the source folder exists
if not exist "!sourceFolder!\" (
    echo folder does not exist
    pause
    exit /b 1
)

:: Prompt the user to input the destination folder path
set /p "destFolder=Endter the destination folder path: "


:: Check if the destination folder exists, create it if it doesn't
if not exist "!destFolder!\" (
    echo creating folder
    mkdir "!destFolder!"
    if errorlevel 1 (
        echo Failed to create folder
        pause
        exit /b 1
    )
)


:: Use ROBOCOPY to copy files and subdirectories
robocopy "!sourceFolder!" "!destFolder!" /E
if errorlevel 16 (
    echo copy operation error
)   else (
    echo Copy operation completed successfully!
)

endlocal

:: In a real-world scenario storing backup files need to be in an area that is:
:: secure
:: fast to get to
:: has the storage capable to store all the data
:: make sure the eggs aren't all in one basket (different locations)(compartmentalization)
:: and can be easily organized with protocols