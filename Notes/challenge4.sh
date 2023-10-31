#!/bin/bash

#Write a script that:

# Creates four directories: dir1

# Put the name of the four directoreis in an array

# Define array

paths=(./demo ./demo/dir1 ./demo/dir2 ./dem/dir3)


# References the array variable to create a new .txt file in each directory

# Create the directories using the paths we put into the array
mkdir ${paths[*]}