# IU-Blimp-Kit
This repository contains all the information for assembling the Indiana University Highschool Blimp Kit! The repository includes the models used for the vehicle and the software to control the blimp with an xbox controller.

## Step 1: Setup
Start the vehicle by plugging in the battery to the blimp's power bus. The motor controllers will beep "low" and then "high", and each motor will pulse to confirm the microcontroller is wired correctly. The laptop should be powered on and open the xbox python control script.

## Step 2: Connect
Once all hardware is set up and in place, connect the computer to the WiFi network initialized by the blimp's microcontroller. Once connected, run the [xbox controller script](https://github.iu.edu/caedtayl/IU-Blimp-Kit/blob/main/Software/Controller%20Files/xbox_control.py) and wait for the console to begin printing the control commands from the controller.

## Step 3: Control
The vehicle is now actively being controlled by the xbox controller. The left joysick controls the up and down movement of the vehicle. The right joystick allows the vehicle to turn left and right, and to move forward and backward. Pressing "B" causes the vehicle to cut power to all motors, and disconnect the controller. Restarting the laptop python script will reconnect the vehicle. In the event the blimp does not disconnect cleanly, it will sit and "hang", you will have to unplug the battery and reconnect to hard reset the device.
