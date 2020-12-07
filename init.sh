#!/bin/bash

echo "Installing packages..."
sudo apt-get update && sudo apt-get install git neofetch ffmpeg flac net-tools nano &> /dev/null
sudo apt-get install python3.8 python3-pip &> /dev/null
sudo apt-get install python3-setuptools &> /dev/null
echo "Installing python requirements..."
python3.8 -m pip install wheel &> /dev/null
python3.8 -m pip install -r requirements.txt
echo "Running the userbot.."
