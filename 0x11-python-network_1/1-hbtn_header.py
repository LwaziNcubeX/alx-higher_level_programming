#!/usr/bin/python3
"""Sends a request to the URL and displays the value of the X-Request-Id"""
from urllib import request
import sys


def fetch_header():
    """
    Sends a request to the URL and displays the value of the X-Request-Id
    """
    url = sys.argv[1]
    with request.urlopen(url) as response:
        content_type = response.headers['X-Request-Id']
        print(content_type)


if __name__ == "__main__":
    fetch_header()
