#!/bin/bash


# Main

# Search the output of lshw command and return every line with the word bridge in it
lshw | grep "bridge" #the pipe grabs the output on the left and feeds it to the command on the right hand side (Super Mario pipes)