# rokuRA
## Overview
rokuRA is a python script that allows for remote control of a Roku TV (so long as on the same wifi as the television)

## Usage
STEPS BELOW ARE NOT POSSIBLE WHILE REPO IS PRIVATE
Linux users can use curl to install the script as an executable:  

Step 1:
```
sudo curl -L https://raw.githubusercontent.com/Its-Rolo/rokuRA/main/rokuRA.py -o /usr/local/bin/rokuRA
```
Step 2:
```
sudo chmod a+rx /usr/local/bin/rokuRA
```
The script can now be run via the 'rokuRA command in the terminal
```
rokuRA
```

Options:
1. Install Web Cast -- Installs web cast, which can be used for pwning TVs with your own custom video content or MP3s. First, the script turns the volume down to 0 to ensure that the victim device will not disturb the owner with the sound of attempts or pin entry. Then, it runs through all of the combinations until it successfully brutes the pin to install the application. It then re-adjusts the volume to a reasonable level.
2. Install Another App -- Same as option 1, except you can enter the app ID of the app you want to install. Please see "Custom Apps" for details.
3. Launch Web Cast -- Starts the Web Cast application, which will give you the ability to stream your media via the application.
4. Launch Web Cast (PWN Mode: Be warned!) -- Turns the volume up to max, and then launches Web Cast.
5. Launch Another App -- Starts your custom application by ID.
6. Loop Shutdown -- Sends a poweroff command every second to the TV until you kill the script.
7. Custom keystroke -- Sends a custom keystroke to the TV given a key ID
8. Exit

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
