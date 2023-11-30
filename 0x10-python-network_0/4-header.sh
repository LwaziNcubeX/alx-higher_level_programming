#!/bin/bash
# sends a GET request to the URL, and displays response.
curl -sX GET "$1" -H "X-School-User-Id: 98"
