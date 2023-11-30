#!/bin/bash
# sends a POST request to the URL, and displays response.
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1" | grep -E "POST params:|email|subject"
