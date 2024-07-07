#!/bin/bash
# Bash Script to display Content-Length from a HTTP request
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
