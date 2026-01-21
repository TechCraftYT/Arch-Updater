#!/bin/bash

clear

cat assci.txt

echo "             "
echo "Requesting Sudo Permissions"

sudo echo "We have Superuser"

sleep 3

clear

echo "Updating the Repoistory"

sudo pacman -Sy

echo "Upgrading Packages"

sudo pacman -Su --noconfirm

clear

echo "Rebooting in 5 seconds....."
sleep 5 
reboot
