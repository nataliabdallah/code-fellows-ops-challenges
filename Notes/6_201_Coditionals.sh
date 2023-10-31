#!/bin/bash


#Script Name:               Conditionals
# Author:                   Nathalie Abdallah
# Date of latest revision:  10/30/2023
# Purpose:                  A grocery list checker


# Array to store the grocery list
grocery_list=("apples" "milk" "bread" "monster")

# Function that is going to check if an item is in grocery list
grocery_list_checker() {
    # Item I am looking for in my list
    search_item="$1"
   # echo $search_item

    # For loop (instead of a while loop) Any time youre doing something with an Array, that should be a For loop, to go over each item on the list
    for item in "${grocery_list[@]}"
    do
        # echo $item
        #check if the item I'm looking for is in my list of not
        if [ "$item" == "$search_item" ]
        then 
            return 0 # If a computer returns 0 = success
            echo "The item is in your grocery list!"
         fi
    done
    return 1 # false (this means something is broken in the script if it returns 1)

}

# side note: in bash you can't declare an object like in C#


# Main

# WHILE Loop
# This while loop is going to repeatedly ask the user for items to check (leave out a counter in order to make infinite loop- on purpose leave out [ ] and just put in while ture:)
while true; 
do 
    # Ask the user for imput of an item to look for in a list
    read -p "Enter an item to check if it's on your grocery list: Type done to exit.)" item_to_check

    # Check if the user's input is done
    if [ "$item_to_check" == "done" ]
    then
        break # Exit the loop
    fi

    # Check if the item is in the grocery list - call the function we built
    if grocery_list_checker "$item_to_check"
    then
        echo "Item '$item_to_check' is already on your grocery list."
    else    
        # if the item is not on the list, ask the user if they want to add it
        read -p "'$item_to_check' is not on your list, do you want to add it? (yes/no)" add_to_list
        if [  "$add_to_list" == "yes" ]
        then 
            grocery_list+=("$item_to_check")
            echo "'$item to check' was added to your list."
        else
            echo "'$item_to_check' was not added to your list."
        fi
     fi

done

# Ask the user if they are ready to see their completed grocery list
read -p "are you ready to see your completed grocery list? (yes/no)"
if [  "$show_list" == "yes"]
then
    echo "Your completed grocery list:"
    echo "{Sgrocery_list[*]}"
else 
    echo "OK, you can check your list later."
fi
