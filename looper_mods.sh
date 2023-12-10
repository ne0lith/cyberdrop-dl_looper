#!/bin/sh

NUM_RUNS=20
PROFILE="Default"
MACHINE_NAME="Default"
BACKUP_LOGS=false  # Set to true to enable file_management.py
SEND_WEBHOOK=false  # Set to true to enable send_webhook_results.py

for ((i = 1; i <= NUM_RUNS; i++)); do
    echo "Running start.sh - Iteration $i"
    sh start.sh

    if [ "$BACKUP_LOGS" = true ]; then
        python3 mods/file_management.py "$PROFILE"
    fi

    if [ "$SEND_WEBHOOK" = true ]; then
        python3 mods/send_webhook_results.py "$PROFILE" "$MACHINE_NAME"
    fi

    echo "Completed iteration $i"
    echo
done
