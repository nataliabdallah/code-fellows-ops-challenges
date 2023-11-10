#!/bin/bash

# Script Name:                  Variables
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      10/25/2023
# Purpose:                      Explains and gives examples of Variables

# Declaration of variables

# PRICE OF APPLES
# One equal sign means assigining a value
# Two is comparing values
PRICE_PER_APPLE=5
MyFirstLetters=ABC
greeting="Hello world"
FILES=`ls`
WHO=`whoami`

# Declaration of functions
# Basic function that handles printing the greeting to the screen
print_greeting () {
    echo "HELLO WORLD:
    echo "This is our first function"
    echo "The person running this script is $WHO"
}


# Main

# CALL THE FUNCTION - TELL THE COMPUTER TO DO THE THING
print_greeting

print_greeting

#echo $greeting

#echo "The price of an apple today is: $PRICE_PER_APPLE"
#echo "The first ten letters of the alphabet are: ${MyFirstLetters}DEFGHIJ"
#echo "This folder contains the following $FILES"
#echo "The person running this script is $WHO"

# End

#!/bin/bash

# Script Name:                  Review Variables and Functions
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      10/26/2023
# Purpose:                      Review


# Declaration of variables
num1=25
num2=5
num3=10

# Notes: 1 set of paranthases is for the function
# 2 sets is for the mathematics

# Declare function
add_some_numbers() {
    sum=$(($num1+$num3))
    echo $sum
}

# Main
# Call the function
add_some_numbers

# End

#!/bin/bash

# Script Name:                  Arrays 101
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      10/26/2023
# Purpose:                      Learn about arrays

# Define Variables
PRICE_PER_APPLE=5,10,15 # this won't work
PRICE_PER_APPLE=5

# Define array
grocery_list=(apple bananas orange onion)

# Print out the entire grocery list
echo ${grocery_list} # the curly brackets and square brackets with the star is necessary: the stary means grab everything

# Append a new item to the list
new_snack=monster
grocery_list+=" monster"

echo  ${grocery_list[*]}

# End

#!/bin/bash

# Script Name:                  Directions
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      10/26/2023
# Purpose:                      Array showing 4 directions

# Define Variables
dir1=North
dir2=South
dir3=East
dir4=West

# Define array
compass=($dir1 $dir2 $dir3 $dir4)

# Print out t list
echo  ${compass[*]}

# End

#!/bin/bash

# Script Name:                  Directories
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      10/26/2023
# Purpose:                      Create 4 directories and create .txt file in each directory
# Define Variables
dir1=north
dir2=south
dir3=east
dir4=west

# Define array
directories=($dir1 $dir2 $dir3 $dir4)

# create a .txt file in each directory
for dir in "$(directories[*])"; do
mkdir -p "$dir" # Create the directory if it doesn't exist"
touch "$dir/file.txt"
done

# End

#!/bin/bash

# Script:                     Login History  
# Author:                     Nathalie Abdallah
# Date of latest revision:    10/27/2024  
# Purpose:                    Ops 201 Challenge 05

# Write a script: 
# That displays the running processes (I will focus on PING processes)
# Asks the user for a PID
# Kills the process with that PID
# Starts over at step 1 and continues until the user exits with `Ctrl + C`

while true; do
  # display running processes
  echo "Running PING processes:"
  ps aux | grep [p]ing # the [] in ping prevent grep from matching itself

  # ask user for PID
  read -p "Enter PID to kill (Ctrl + C to exit): " pid

  # check if input is empty
  if [ -z "$pid" ]; then
    echo "No PID entered. Enter valid PID."
  else
    # check if PID is valid
    if ps -p "$pid" > /dev/null; then
      #  kill process
      kill "$pid"
      echo "Killed process with PID: $pid"
    else
      echo "No mathing process to $pid."
    fi
  fi
done

#!/bin/bash

# Script:                     Loop 
# Author:                     Nathalie Abdallah
# Date of latest revision:    10/27/2024  
# Purpose:                    Ops 201 Challenge 05

# Tasks
# Write a script that:
# Displays running processes
# Asks the user for a PID
# Kills the process with that PID
# Starts over at step 1 and continues until the user exits with Ctrl + C
# Use a loop so that the script will continuously start over, displaying the running processes, asking the user for input, etc.
# For this assignment, initialize a process that won't harm the OS's functionality upon termination. Don't kill essential processes required for the OS to work, such as kernel drivers.
# Hint: you can open a second terminal in your development environment and start it pinging one of your other machines. This will be a safe process to target.


# WHILE LOOP
while true; do
  echo "Running processes:"  # display running processes
  ps auxf 
  read -p "Enter PID to kill (Ctrl + C to exit): " pid # ask user for PID

  # check if input is a valid PID
  if [ $pid =~ ^[0-9]+$ ]] ]; then
    echo "entered invalid PID, try again."
  else
    # check if PID is valid
    if ps -p "$pid" > /dev/null; then
      #  kill process
      kill "$pid"
      echo "Killed process with PID: $pid"
    else
      echo "No mathing process to $pid."
    fi
fi
done

#!/bin/bash

# Script:                     Loop 
# Author:                     Nathalie Abdallah
# Date of latest revision:    10/27/2024  
# Purpose:                    Ops 201 Challenge 05

# Tasks
# Write a script that:
# Displays running processes
# Asks the user for a PID
# Kills the process with that PID
# Starts over at step 1 and continues until the user exits with Ctrl + C
# Use a loop so that the script will continuously start over, displaying the running processes, asking the user for input, etc.
# For this assignment, initialize a process that won't harm the OS's functionality upon termination. Don't kill essential processes required for the OS to work, such as kernel drivers.
# Hint: you can open a second terminal in your development environment and start it pinging one of your other machines. This will be a safe process to target.

#Array
  kernel='(1 2 3 11 12 13 262 289 531 532 533 653 657 659 667 687 688 801 846 865 1028 1053 1352 1357 1401 1427 1612 1711 7050 7086 7216 7257)'

# WHILE LOOP
while true; do
   echo "Running processes"
   ps auxf # displays running processes
  read -p "Enter PID to kill (Ctrl + C to exit): " pid # ask user for PID


  if [ "$pid" != "$kernel"] then #check if PID is not in list of excluded PIDs
    
    if [ -z "$pid" ]; then # check if input is a valid PID
      
      if ps -p "$pid" > /dev/null; then # check if PID is valid
        kill "$pid" #  kill process
        echo "Killed process with PID: $pid"

      else
        echo "No mathing process to $pid."
      fi
      
    else 
        echo "entered invalid PID, input valid PID"  
    fi

  else
    echo "process with PID $pid is excluded from termination."
  fi

done

#!/bin/bash

# Script:                     Login History  
# Author:                     Nathalie Abdallah  
# Date of latest revision:    10/30/2023  
# Purpose:                    Ops 201 Challenge 06

# define array and dir names
dirs=("dir1" "dir2" "dir3" "dir4")

# does the directory exist?
dir_in_array() {
  local dir_check="$1"
  for dir in "${dirs[@]}"; do
    if [ "$dir" = "$dir_check" ]; then
      return 0 # boolean true; dir is in array
    fi
  done
  return 1 # boolean false; dir is not in array
}

get_name() {
  # view directory
  read -p "Want to view array? (y/n): " view
  if [ "$view" == "y" ] || [ "$view" == "yes" ]; then
    echo "Array: "
    echo "${dirs[@]}"
  fi

  # loop to ask for user input
  while true; do
    read -p "Enter a directory name (type 'done' to finish): " dir_name

    # does user want to exit
    if [ "$dir_name" == "done" ]; then
      break
    fi

    # does the directory exist?
    if dir_in_array "$dir_name"; then 
      echo "'$dir-name' already exists."
    else
      # does user want to create the directory?
      read -p "'$dir_name' not in list.  Do you want to add it? (y/n): " add_dir

      if [ "$add_dir" == "y" ] || [ "$add_dir" == "yes" ]; then
        # add to array
        dirs+=("$dir_name")
        echo "Added '$dir_name' to array."

        # create dir
        mkdir "$dir_name"
        echo "'$dir_name' created."
      else
        echo "'$dir_name' not added."
      fi
    fi
  done
}

get_name

# do you want to delete a dir?
while true; do
  read -p "Do you want to remove a directory? (y/n): " rm_dir

  if [ "$rm_dir" == "y" ] || [ "$rm_dir" == "yes" ]; then
    read -p "Dir to be be removed: " dir_rm
    if dir_in_array "$dir_rm"; then
      # remove from array
      dirs=("${dirs[@]/$dir_rm}")
      rm -r "$dir_rm"
      echo "'$dir_rm' removed."
    else
      echo "'$dir_rm' not in array."
    fi
  else
    break
  fi
done

# print array
read -p "Want to view your completed array? (y/n): " show_array
if [ "$show_array" == "y" ] || [ "$show_array" == "yes" ]; then
  echo "Here is your completed array: "
  echo "${dirs[@]}"
  read -p "Press Enter to exit."
else 
  echo "Ok, goodbye."
fi

