#!/usr/bin/python3
"""a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    load = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(load).encode('utf-8')
    req = urllib.request.Request(url=sys.argv[1], data=data, method='POST')
    with urllib.request.urlopen(req) as resp:
        body = resp.read().decode('utf-8')
    print(body)
