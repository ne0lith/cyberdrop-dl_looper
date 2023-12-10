#!/bin/sh

source config.txt

for ((i = 1; i <= loop_count; i++)); do
    echo "Running start.sh - Iteration $i"
    sh start.sh
    echo "Completed iteration $i"
    echo
done
