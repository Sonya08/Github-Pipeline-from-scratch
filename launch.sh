#!/bin/bash

# Configuration
BRANCH_NAME=$1
REPO_DIR="C:/Users/SONYA/Desktop/Github-Pipeline-from-scratch"
LOG_DIR="${REPO_DIR}/logs"
STDOUT_LOG="${LOG_DIR}/stdout.log"
STDERR_LOG="${LOG_DIR}/stderr.log"
FLASK_APP_PATH="${REPO_DIR}/app.py"

# Create the logs directory if necessary
mkdir -p "${LOG_DIR}"

# Change to the repository directory
cd "${REPO_DIR}"

# Configure Git to avoid divergent branch problems
git config pull.rebase false

# Update the source code
git pull origin $BRANCH_NAME

# Update pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Set the Flask application path
export FLASK_APP="${FLASK_APP_PATH}"

# Kill any process using port 5000


# Start the Flask application in the background
nohup flask run app.py --host=0.0.0.0 --port=5001 > "${STDOUT_LOG}" 2> "${STDERR_LOG}" &
read -p "Press enter to exit"
