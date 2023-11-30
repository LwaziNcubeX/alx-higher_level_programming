#!/bin/bash
# Use curl to send a request to the specified URL & display the size of the response body in bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'

