#!/bin/bash

BRANCH_NAME=$1

# Update the path to the repository
cd "C:/Users/SONYA/Desktop/Github-Pipeline-from-scratch"

git pull origin $BRANCH_NAME

pip install -r requirements.txt

pytest

# Pause to keep the console window open
read -p "Press enter to exit"
