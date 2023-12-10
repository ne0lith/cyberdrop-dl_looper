#!/bin/sh

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
. "$SCRIPT_DIR/config.txt"

for i in $(seq 1 $loop_count); do
    echo "Running start.sh - Iteration $i of $loop_count"
    sh start.sh
    echo "Completed iteration $i of $loop_count"
    echo
done
