#!/bin/bash
 
BRANCH_NAME=$1
 
cd /Users/SONYA/Desktop/Github-Pipeline-from-scratch
 
git pull origin $BRANCH_NAME
 
pip install -r requirements.txt
 
pytest