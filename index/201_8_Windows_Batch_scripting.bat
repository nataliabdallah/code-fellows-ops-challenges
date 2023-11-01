@echo off 
setlocal enabledelayedexpansion

:: the @echo off turns off echo in the file, so that you cannot see the commands being displayed, and only the parts of the script that is commended to be displayed

:: The setlocal means it will not be visible to other batch files that are running, this starts a localized environment and you must end it with endlocal

set /p sourcePath=Enter the source folder path:

:: "set" is the command to give a variable a value

:: the / p  tells the "set" to prompt user for input

:: "sourcePath=Enter the source folder path:"" The text that will be displayed to user will be :Enter the source folder path. sourcePath is the variable

set /p destinationPath=Enter the destination folder path:

:: this follows the same structure with a second variable that prompts the user to enter the destination folder path intead of the source folder path.

if not exist "!sourcePath!\" (
    echo Error: Source folder does not exist.
    goto :eof
)

:: this is conditional to search for said folder or file and if not there, come back with said response

if not exist "!destinationPath!\" (
    echo Error: Destination folder does not exist.
    goto :eof
)

:: This is the same conditional with just chaning what the search is for

robocopy "!sourcePath!" "!destinationPath!" /E

:: robocopy copies everything the is sourcePath and destinationPath whci is folders, and the /E at the end copies even empty folders and subfolders. 

if errorlevel 8 (
    echo Error: ROBOCOPY encountered errors during the copy operation.
) else (
    echo Copy operation completed successfully.

:: this conditional will check for errors specific to errorlevel 8, and if no errors will copy and echo the success as stated above
::  errorlevel 8 errors include:

:: Permissions issues, File corruption, Network connectivity issues, Drive full, Destination folder does not exist, File in use, File too large, and Invalid Path
:: errorlevel 8 is a shortcut instead of writing a script for this one thing

:: And End is like the done in a sh script. but endlocal is what is used to end the delayed response otherwise this script will delay other .bat scripts


:end
endlocal