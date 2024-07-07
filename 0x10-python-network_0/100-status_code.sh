#!/bin/bash
# Script to GET request and SHOW response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
