#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""
import sys
from urllib import request
from urllib.error import HTTPError


def display_error_code():
    """
    sends a request to the URL and
    displays the body of the response (decoded in utf-8).
    """
    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)
    except HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    display_error_code()
