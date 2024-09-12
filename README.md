# rokuRA
## Overview
rokuRA is a python script that allows for remote control of a Roku TV (so long as on the same wifi as the television)

## Usage
STEPS BELOW ARE NOT POSSIBLE WHILE REPO IS PRIVATE  
Linux users can use curl to install the script as an executable:  

Step 1:
```
sudo curl -L https://raw.githubusercontent.com/Its-Rolo/rokuRA/main/rokuRA.py -o /usr/local/bin/rokuRA
sudo chmod a+rx /usr/local/bin/rokuRA
```
The script can now be run via the 'rokuRA command in the terminal
```
rokuRA
```

# Before executing the script, you must first identify the IP address of the Roku TV. This can be done in multiple ways:
Method 1: Directly from the Roku TV  

In settings, you can find the local IP address in the network -> about section.  
  
Method 2: nmap scan (Steps below are for linux)

If you do not have access to the Roku TV / Remote, you can use nmap to scan the network and identify connected devices.  
  
Step 1: Identify the networks IP address  
open the terminal and input the following command:
```
ip addr
```
A large amount of text will show up. Look for the IP that comes after "inet" and copy it entirely including the number after the '/'

Step 2: Scan the IP with nmap
In the terminal, run the command:
```
sudo nmap -sn IP_ADDRESS/HERE
```
(Obviously replace the last part with the ip address, for example '192.###.#.###/##'
This will display all devices connected to the network. Locate the Roku TV and note down the IP to be inputted when running the script.
    


## Uninstallation

Step 1, cd into the directory:
```
cd /usr/local/bin
```
Step 2, remove the file:
```
sudo rm rokuRA
```

## List of known Key IDs

Arrow Keys:
```
Up: "Up"
Down: "Down"
Left: "Left"
Right: "Right"
```
Navigation Controls:
```
OK button: "Select"
Back: "Back"
Home: "Home"
Info or asterisk button (*): "Info"
```
Playback Controls:
```
Play: "Play"
Pause: "Pause"
Toggle Play/Pause: "PlayPause"
Rewind: "Rewind"
Fast Forward: "FastForward"
Reverse one frame: "ReverseFrame"
Forward one frame: "ForwardFrame"
Instant Replay: "InstantReplay"
Open Search: "Search"
```
Media Control Keys:
```
Mute/Unmute: "VolumeMute"
Channel Up: "ChannelUp"
Channel Down: "ChannelDown"
```
Input Controls:
```
TV Input: "InputTuner"
HDMI 1: "InputHDMI1"
HDMI 2: "InputHDMI2"
HDMI 3: "InputHDMI3"
HDMI 4: "InputHDMI4"
AV Input: "InputAV"
Component Input: "InputComponent"
```
Special Commands:
```
Find Remote: "FindRemote" <- PLAYS NOISE THROUGH COMPATIBLE REMOTES!!!!!!
Sleep Mode: "Sleep"
Wake Up: "WakeUp"
```

## Custom Apps
Maybe you'd rather install a custom app. If you have a Roku TV, install the app, and then navigate to http://ip:8060/query/apps to get the App ID, then you can pass the application ID via the options to install that app instead of webcast.

Here is an example of what it looks like, where 2595 is the app id:
`<app id="2595" type="appl" version="4.8.1110">Crunchyroll</app>`
