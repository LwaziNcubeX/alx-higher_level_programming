#!/bin/bash
# cURL a JSON file and displays the body of the response.
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
