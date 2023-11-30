#!/bin/bash
# sends a POST request to the URL, and displays response.
curl -sX POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
