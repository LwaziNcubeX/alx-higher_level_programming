#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""
import requests
import sys


def search_user():
    """
    sends a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter.
    """
    url = "http://0.0.0.0:5000/search_user"

    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    data = {'q': letter}

    response = requests.post(url, data=data)

    try:
        data = response.json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    search_user()
