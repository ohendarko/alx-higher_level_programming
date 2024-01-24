#!/usr/bin/python3
"""a Python script that fetches
https://alx-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        page = resp.read()
    print("Body of the response:")
    print("\t\t- type:", type(page))
    print("\t\t- content:", page)
    print("\t\t- utf8 content:", page.decode("utf-8"))
