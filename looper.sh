#!/bin/sh

NUM_RUNS=20

for ((i = 1; i <= NUM_RUNS; i++)); do
    echo "Running start.sh - Iteration $i"
    sh start.sh
    echo "Completed iteration $i"
    echo
done
