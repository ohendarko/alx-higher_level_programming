#!/usr/bin/python3
"""a Python script that fetches
https://alx-intranet.hbtn.io/status"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as resp:
        value = resp.getheader('X-Request-Id')
    print(value)
