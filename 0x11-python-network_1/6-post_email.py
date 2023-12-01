#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
import sys
import requests


def post_email():
    """
    sends a POST request to the passed URL with the email as a parameter
    displays the body of the response (decoded in utf-8)
    """
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}

    response = requests.post(url, data=data)
    response.encoding = 'utf-8'
    print(response.text)


if __name__ == "__main__":
    post_email()
