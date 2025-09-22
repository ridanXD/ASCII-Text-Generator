#!/bin/bash

loading() {
    duration=$1
    interval=0.1
    spin="/-\|"
    end=$((SECONDS + duration))
    i=0
    while [ $SECONDS -lt $end ]; do
        printf "\r%s ${spin:i%4:1}" "$2"
        sleep $interval
        ((i++))
    done
    printf "\r%s Done!          \n" "$2"
}

loading 3 "Preparing project..."

ENV_NAME="env"

if [ ! -d "$ENV_NAME" ]; then
    echo "Creating virtual environment..."
    python -m venv $ENV_NAME
else
    echo "Virtual environment already exists."
fi

echo "Activating virtual environment..."
source env/bin/activate

if [ -f "requirements.txt" ]; then
    echo "Installing requirements..."
    pip install -r requirements.txt
fi

echo "Well Done! Virtual environment is ready."

