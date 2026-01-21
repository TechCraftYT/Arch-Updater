#!/usr/bin/python

###########################################################
# A Simple Script in Python to update Arch based distros. #
###########################################################

import os


#Variables
############################################
sudo = "sudo echo Root Granted" 
command1 = "sudo pacman -Sy"
command2 = "sudo pacman -Su --noconfirm"
cat = "cat assci.txt"
reboot = "echo Packages Upgraded. Rebooting in 5 seconds..."
############################################
os.system ("clear")

os.system (cat)

os.system ("echo")

os.system (sudo)

os.system (command1)

os.system (command2)

os.system (reboot)

os.system ("sleep 5 && reboot ")