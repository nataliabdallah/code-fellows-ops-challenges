#!/usr/bin/env python3

# Script Name:                  Challenge 7 Directory Creation (user friendly)
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      12/05/2023
# Sources:                      https://chat.openai.com/, https://github.com/codefellows/seattle-ops-301d10
# Purpose:                      Create a Python script that generates all directories, sub-directories and files for a user-provided directory path.
# a:                            Intended for the script to execute for user friendly experience
#                               this assists in learning what is taking place, and breaking down the process in file: b


# Script must ask the user for a file path and read a user input string into a variable.
# Script must use the os.walk() function from the os library.
# Script must enclose the os.walk() function within a python function that hands it the user input file path.




# Import libraries
import os

# Declaration of functions
def generate_directory_structure(user_input_path):
    try:
        # Flag to check if anything is processed
        processed = False

        for (root, dirs, files) in os.walk(user_input_path):
            # Print the current root directory
            print(f"Processing root directory: {root}")

            # Print the subdirectories in the current directory
            print(f"Subdirectories in {root}: {dirs}")

            # Print the files in the current directory
            print(f"Files in {root}: {files}")

            # Add a separator line for better readability
            print("=" * 40)

            # Set the flag to True since something is processed
            processed = True

        # Check if nothing is processed
        if not processed:
            print("No directories or files found in the specified path.")

    except KeyboardInterrupt:
        print("\nScript execution canceled. Hit Ctrl+C again to exit.")

    except Exception as e:
        print(f"Error: {e}")

# Get the current working directory
current_directory = os.getcwd()

# List directories in the current working directory
available_directories = next(os.walk(current_directory))[1]

# Main
if not available_directories:
    # If there are no directories, create directories, subdirectories, and files
    print("Creating directories, subdirectories, and files...")

    try:
        for i in range(1, 3):
            directory_name = f"dir{i}"
            os.makedirs(os.path.join(current_directory, directory_name))

            for j in range(1, 3):
                subdirectory_name = f"subdir{j}"
                os.makedirs(os.path.join(current_directory, directory_name, subdirectory_name))

                for k in range(1, 3):
                    file_name = f"file{k}.txt"
                    with open(os.path.join(current_directory, directory_name, subdirectory_name, file_name), 'w') as file:
                        file.write("This is a sample file.")

        print("\nDirectory structure and files created.")
        print("Press Ctrl+C to cancel the script and re-execute.")
        
        # Hide other options by setting available_directories to an empty list
        available_directories = []

    except KeyboardInterrupt:
        print("\nScript execution canceled. Hit Ctrl+C again to exit.")

# Continue with the menu
while True:
    print("Options:")
    
    if available_directories:
        print("1. Generate directory structure")
        print("2. Exit")
    else:
        print("Press Ctrl+C to cancel the script and re-execute.")

    # Display available directories for the user to choose from
    print("Available Directories:")
    for i, directory in enumerate(available_directories, start=1):
        print(f"{i}. {directory}")

    if available_directories:
        choice = input("Enter your choice (1, 2, or select a directory number): ")

        if choice == "1":
            # Allow the user to select a directory from the list
            if available_directories:
                print("Select a directory:")
                for i, directory in enumerate(available_directories, start=1):
                    print(f"{i}. {directory}")

                dir_choice = int(input("Enter the number corresponding to the directory: "))

                if 1 <= dir_choice <= len(available_directories):
                    user_input_path = os.path.join(current_directory, available_directories[dir_choice - 1])
                    generate_directory_structure(user_input_path)
                else:
                    print("Invalid directory selection.")
            else:
                print("No directories available in the current working directory.")
        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or select a directory number.")
    else:
        # Pause and wait for Ctrl+C to cancel the script
        try:
            input("Press Enter to continue...")
        except KeyboardInterrupt:
            print("\nScript execution canceled. Hit Ctrl+C again to exit.")
            break


