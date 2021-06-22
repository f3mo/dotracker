#!/bin/bash


GOOD="\e[32m"
ENDC="\e[0m"
cp "$PWD/config.json" "$HOME"
cp "$PWD/dotracker.py" "$HOME/.local/bin/"
source "$HOME/.profile"
printf "${GOOD}Package Successfully installed\n${ENDC}"
