#!/usr/bin/python3
"""a Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8)"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as resp:
            body = resp.read().decode('utf-8')
        print(body)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
