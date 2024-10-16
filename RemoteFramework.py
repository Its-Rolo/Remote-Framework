#!/usr/bin/env python3


#############################################################################################################
# CODE NECESSARY FOR THE SCRIPT. DO NOT EDIT BELOW THIS LINE. SCROLL FURTHER DOWN FOR WHAT SHOULD BE EDITED #
#############################################################################################################

import requests # For sending HTTP requests to the Roku device
import time # For adding delays
import subprocess
from tqdm import tqdm # For displaying progress bars
import os # For clearing the console
import platform # For checking the operating system

def initialize():
    choice = input("")

    if choice == '1':
        # Manual input
        ip = input("Enter the IP address of the device: ")
        select_option(ip)

    elif choice == '2':
        auto_detection()
        select_option(ip)

def auto_detection():
    # Begin automatic Detection
    base_ip = input("Enter the base IP (format: ###.###.##): ")
    timeout = input("\n Please input the delay between each scan, higher values will result in a slower scan but lower values may skip over the device: ")
    startingValue = input("Input the starting value for the scan (Scans from top down): ")
    # Iterate through the last octet (3 digits) from 255 to 0
    for i in tqdm(range(int(startingValue), -1, -1)):
        # Construct the full IP address
        ip = f"{base_ip}.{i}"
        url = f"http://{ip}:8060/query/device-info"
        
        if i == 0:
            print("No device found.")
            exit()

        try:
            # Send a request to the Roku device info endpoint
            response = requests.get(url, timeout=float(timeout))  # Timeout set to 0.5 seconds to speed up the scan
            if response.status_code == 200:
                clear_console()
                print(f"Possible device found at: {ip}")
                input("Press enter to continue.")
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

# Function to clear the console
def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def request(ip, query):
    response = requests.get(f"http://{ip}:8060/query/{query}")
    return response

def send_keypress(ip, key):
    requests.post(f"http://{ip}:8060/keypress/{key}")

def ascii_art(art):
    print(art)

def top_divider(title):
    print(f"\033[35m╔═════════>\033[0m{title}")

def menu_entry(number, text):
    print(f"\033[35m╠>\033[0m ({number}) {text}")

def menu_ender():
    print("\033[35m╚═════════\033[0m")





#########################################
# ADD CUSTOM FUNCTIONS BELOW THIS LINE. #
#########################################

# Example:
def show_installed_apps(ip):
    request(ip, "apps")

#################################################################################
# BELOW IS THE MAIN PROGRAM CODE. ONLY EDIT CODE INSIDE THE EXISTING FUNCTIONS. #
#################################################################################

def print_welcome():
    # Edit this function to customize the welcome message.
    # Example:
    top_divider("Welcome to my remote, Select an Option:")
    menu_entry(1, "Input IP Manually")
    menu_entry(2, "Auto detect IP")
    menu_ender()

print_welcome()

# Function for drawing the menu. Edit this function to customize the menu.
def draw_menu():
    # Clear the console, do not remove this line
    clear_console()

    # Draw the menu using the functions from the framework. You can customize this as needed.
    ascii_art("""\033[35m
__________                       __          
\______   \ ____   _____   _____/  |_  ____  
|       _// __ \ /     \ /  _ \   __\/ __ \ 
|    |   \  ___/|  Y Y  (  <_> )  | \  ___/ 
|____|_  /\___  >__|_|  /\____/|__|  \___  >
        \/     \/      \/                 \/ """)
    top_divider("Welcome to my remote, Select an Option:")
    menu_entry(1, "Custom Input")
    menu_entry(2, "Exit")
    menu_ender()

# Function for selecting an option. Edit this function to customize the options.
def select_option(ip):
    while True:

        # Display the menu. Do not remove these 2 lines
        draw_menu()
        option = input("")


        if option == '1': # Edit numbers and add more options as needed
            # Example function, asks for keystroke ID and sends it
            keystroke = input("Enter the key ID: ")
            send_keypress(ip, keystroke)

        elif option == '2': # Edit as needed. Copy and paste the elif statement to add more options.
            exit()



        # Do not remove the next 2 lines
        else:
            print("Invalid option, please try again.")



################################
# DO NOT EDIT BELOW THIS LINE. #
################################
initialize()


