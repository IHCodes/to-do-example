#!/bin/bash
echo "Updating packages"
sudo apt-get update
echo "installing Python"
sudo apt install python3
echo "installing pip"
sudo apt install python3-pip
echo "creating virtual environment"
sudo python3.8-distutils
sudo apt install python3.8-venv
sudo python3 -m venv .venv
source .venv/bin/activate
echo "installing project requirements"
pip install -r requirements.txt
