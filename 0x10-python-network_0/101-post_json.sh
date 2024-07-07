#!/bin/bash
# Bash Script to do JSON POST request with the provided JSON file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
