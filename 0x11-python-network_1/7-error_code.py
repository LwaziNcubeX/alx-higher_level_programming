#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""
import sys
import requests


def display_error_code():
    """
    sends a request to the URL and
    displays the body of the response (decoded in utf-8).
    """
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)


if __name__ == "__main__":
    display_error_code()
