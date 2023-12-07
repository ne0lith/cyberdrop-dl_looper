#!/bin/sh

NUM_RUNS=20
PROFILE="Default"

for ((i = 1; i <= NUM_RUNS; i++)); do
    echo "Running start.sh - Iteration $i"
    sh start.sh

    python3 mods/file_management.py "$PROFILE"
    python3 mods/send_webhook_results.py "$PROFILE"

    echo "Completed iteration $i"
    echo
done
