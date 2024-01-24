#!/usr/bin/python3
"""a Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter."""
import sys
import requests

if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    r = requests.get(url)
    try:
        commits = r.json()
        for commit in commits[:10]:
            crow = commit.get('sha')
            authName = commit.get('commit',
                                {}).get('author',{}).get(
                'name', 'Unknown Author')
            print(f"{crow}: {authName}")
    except ValueError:
        print("Not a valid JSON")
