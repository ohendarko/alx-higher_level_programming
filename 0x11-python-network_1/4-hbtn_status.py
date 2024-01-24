#!/usr/bin/python3
"""a Python script that fetches
https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    page = r.text
    print("Body response:")
    print("\t- type:", type(page))
    print("\t- content:", page)
