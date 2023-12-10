#!/bin/sh

source config.txt

for ((i = 1; i <= loop_count; i++)); do
    echo "Running start.sh - Iteration $i"
    sh start.sh

    if [ "$backup_logs" = true ]; then
        python3 mods/file_management.py "$profile_name"
    fi

    if [ "$send_webhook" = true ]; then
        python3 mods/send_webhook_results.py "$profile_name" "$machine_name"
    fi

    echo "Completed iteration $i"
    echo
done
