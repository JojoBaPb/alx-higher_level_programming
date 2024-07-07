#!/bin/bash
# Bash script for all HTTP methods for server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
