#!/bin/bash
# displays only the status code of the response
curl -sIo /dev/null -w "%{http_code}" "$1"
