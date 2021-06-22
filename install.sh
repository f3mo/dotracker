#!/bin/bash


GOOD="\e[32m"
ENDC="\e[0m"
cp "$PWD/config.json" "$HOME"
source "$HOME/.profile"
chmod +x "$PWD/dotracker.py"
cp "$PWD/dotracker.py" "$HOME/.local/bin/"
printf "${GOOD}Package Successfully installed\n${ENDC}"
