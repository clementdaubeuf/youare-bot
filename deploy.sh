#!/bin/bash

PROCESS_NAME="youare_bot.py"

if pgrep -f "$PROCESS_NAME" > /dev/null; then
    echo "Stopping current process..."
    pkill -f "$PROCESS_NAME"
    sleep 5
fi

git pull

pip install -r requirements.txt

python3 youare_bot.py &
