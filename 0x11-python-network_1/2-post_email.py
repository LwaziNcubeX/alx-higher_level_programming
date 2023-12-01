#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
from urllib import request, parse
import sys


def post_email():
    """
    sends a POST request to the passed URL with the email as a parameter
    displays the body of the response (decoded in utf-8)
    """
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}

    new_data = parse.urlencode(data).encode('utf-8')

    with request.urlopen(url, data=new_data) as response:
        content = response.read().decode('utf-8')
        print(content)


if __name__ == "__main__":
    post_email()
