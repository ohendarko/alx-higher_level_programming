#!/usr/bin/python3
"""a Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter."""
import sys
import requests

if __name__ == "__main__":
    r = requests.get("https://api.github.com/user",
                     auth=(sys.argv[1], sys.argv[2]))
    try:
        json_data = r.json()
        print(json_data.get('id'))
    except ValueError:
        print(None)
