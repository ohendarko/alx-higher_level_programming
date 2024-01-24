#!/usr/bin/python3
"""a Python script that takes in a URL,
sends a request to the URL and displays
the body of the response"""
import sys
import requests

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    body = r.text
    if r.status_code >= 400:
        print("Error code:", r.status_code)
    else:
        print(body)
