#!/usr/bin/python3
"""Sends a request to the URL and displays the value of the X-Request-Id"""
import sys
import requests


def which_header():
    """
    Sends a request to the URL and displays the value of the X-Request-Id
    """
    url = sys.argv[1]
    response = requests.get(url)
    content_type = response.headers['X-Request-Id']
    print(content_type)


if __name__ == "__main__":
    which_header()
