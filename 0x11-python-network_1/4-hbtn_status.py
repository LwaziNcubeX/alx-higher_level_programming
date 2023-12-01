#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests


def fetch_me_again():
    """
    A Function that fetches https://alx-intranet.hbtn.io/status
    """
    url = "https://alx-intranet.hbtn.io/status"

    data = requests.get(url)
    data.encoding = 'utf-8'
    print('Body response:')
    print('\t- type: {}'.format(type(data.text)))
    print('\t- content: {}'.format(data.text))


if __name__ == "__main__":
    fetch_me_again()
