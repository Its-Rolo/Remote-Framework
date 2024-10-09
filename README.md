# Remote-Framework
## Overview
Remote-Framework is a python script that is designed to streamline the process of making a custom local telivision remote.  
  
The script is divided into clearly labeled sections, some of which should not be edited.  
Remote-Framework utilizes http requests to control the device. This works for some platforms, but not all. However, it can be easily edited with some basic python knowledge.  
  
If you are not knowledgable in python, please read the documentation below on how to easily create your first remote.  

# Documentation
## Menu functions

**menu_entry(number, text)** is used for creating a menu option/entry for your main menu or welcome message.  
It takes two parameters (number), which is an integer indicating the order, and (text), which is a string. This string should be whatever you wish to display at the top of your menu.  
  
Example: 
```
menu_entry(1, "Custom Input")
```

---
**menu_starter(title)** is used for creating the top bar of your menu or welcome message.  
It takes one parameter (title), which is a string. This string should be whatever you wish to display at the top of your menu.  
  
Example: 
```
menu_starter("Welcome to my remote, Select an Option:")
```

---
**menu_ender()** is used for creating the bottom bar of your menu or welcome message.  
It takes no parameters.  
  
Example: 
```
menu_ender()
```

## General functions

**request(ip, query)** is used for sending a custom query to the device.  
It takes two parameters (ip), which is the string for the ip address and (query), which is a string for the query you wish to utilize.  
Requests are done in the following format: http://{ip}:8060/query/{query}  
However you may edit that for your platform if needed.  
  
Example: 
```
request(192.168.68.###, apps)
```

---
**send_keypress(ip, key)** is used for sending a custom keypress to the device.    
It takes two parameters (ip), which is the string for the ip address and (query), which is a string for the keypress you wish to send.  
Keypresses may be done differenty for each platform. Research your desired platform and adjust accordingly.  
  
Example: 
```
request(192.168.68.###, apps)
```

## Creating the welcome menu
Remote-Framework comes with a pre-built fully functional welcome menu and does not need editing to work.  
To create your own welcome menu, you can utilize the menu functions to draw your welcome menu:  
```
def print_welcome():
    # Edit this function to customize the welcome message.
    # Example:
    menu_starter("Welcome to my remote, Select an Option:")
    menu_entry(1, "Input IP Manually")
    menu_entry(2, "Auto detect IP")
    menu_ender()
```

## Creating the main menu
Remote-Framework comes with a pre-built fully functional main menu and does not need editing to work.  
To create your own main menu, you can utilize the menu functions to draw your welcome menu:  
```
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
    menu_starter("Welcome to my remote, Select an Option:")
    menu_entry(1, "Custom Input")
    menu_entry(2, "Exit")
    menu_ender()
```

## Editing and adding more options
Remote-Framework comes with two prebuilt functional menu options, and does not need editing to work.  
The default looks like this:  
```
def select_option(ip):
    while True:

        # Display the menu. Do not remove these 2 lines
        draw_menu()
        option = input("")
        #####################
        if option == '1': # Edit numbers and add more options as needed
            # Example function, asks for keystroke ID and sends it
            keystroke = input("Enter the key ID: ")
            send_keypress(ip, keystroke)

        elif option == '2': # Edit as needed. Copy and paste the elif statement to add more options.
            exit()




        # Do not remove the next 2 lines
        else:
            print("Invalid option, please try again.")
```
You may edit the code inside of each if statement to change what each option does.  
To add more options, simply add more elif statements:  
```
def select_option(ip):
    while True:

        # Display the menu. Do not remove these 2 lines
        draw_menu()
        option = input("")

        if option == '1': # Edit numbers and add more options as needed
            # Example function, asks for keystroke ID and sends it
            keystroke = input("Enter the key ID: ")
            send_keypress(ip, keystroke)

        elif option == '2':
            print("This is another menu option!")

        elif option == '3': # Edit as needed. Copy and paste the elif statement to add more options.
            exit()


        # Do not remove the next 2 lines
        else:
            print("Invalid option, please try again.")
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

