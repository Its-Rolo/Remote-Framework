# rokuRA
## Overview
Lost your remote? Just want to control your TV in a more interesting way?  
rokuRA (Roku Remote Access) is a python script that allows for you to control your Roku television from your computer.  
To do this, you must have access to both the wifi network that the Roku is connected to and the local IP address of the television.  
Do not attempt to use rokuRA on any devices that you do not own.  
![alt text](https://github.com/Its-Rolo/rokuRA/blob/main/rokuRA.png?raw=true)

## Usage 
Linux users can use curl to install the script and make it executable:  

Step 1:
```
sudo curl -L https://raw.githubusercontent.com/Its-Rolo/rokuRA/main/rokuRA.py -o /usr/local/bin/rokuRA
sudo chmod a+rx /usr/local/bin/rokuRA
```
The script can now be run via the 'rokuRA' command in the terminal
```
rokuRA
```

## Before executing the script, you must first identify the IP address of the Roku TV. This can be done in multiple ways:
Method 1: Directly from the Roku TV  

In settings, you can find the local IP address in the network -> about section.  

Method 2: Automatic detection through the script  

When prompted by the script to input an IP, instead press enter without inputting anything.  
It will first prompt you for a base IP, as it will only scan for the last 3 digits.
It will then prompt you for a timeout/delay value. 0.5 - 1 is recommended.  
Now wait while the script automatically checks each final value on the base_ip
    
## Uninstallation

Step 1, cd into the directory:
```
cd /usr/local/bin
```
Step 2, remove the file:
```
sudo rm rokuRA
```

## List of possible Key IDs

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
Find Remote: "FindRemote"
Sleep Mode: "Sleep"
Wake Up: "WakeUp"
```

## Custom Apps
Maybe you'd rather install a custom app. If you have a Roku TV, install the app, and then navigate to http://ip:8060/query/apps to get the App ID, then you can pass the application ID via the options to install that app instead of webcast.

Here is an example of what it looks like, where 2595 is the app id:
`<app id="2595" type="appl" version="4.8.1110">Crunchyroll</app>`
