#!/bin/bash
# Bash script that takes in a URL, sends POST req to passed URL, and displays body of response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
