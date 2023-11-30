#!/bin/bash
# sends a request & return size
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'

