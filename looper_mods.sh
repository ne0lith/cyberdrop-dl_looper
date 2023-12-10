#!/bin/sh

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)

. "$SCRIPT_DIR/config.txt"

for i in $(seq 1 $loop_count); do
    echo "Running start.sh - Iteration $i of $loop_count"
    sh start.sh

    if [ "$backup_logs" = true ]; then
        python3 mods/file_management.py "$profile_name"
    fi

    if [ "$send_webhook" = true ]; then
        python3 mods/send_webhook_results.py "$profile_name" "$machine_name"
    fi

    echo "Completed iteration $i of $loop_count"
    echo
done
