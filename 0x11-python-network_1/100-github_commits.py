#!/usr/bin/python3
"""lists 10 commits (from the most recent to oldest)
of the repository“rails” by the user “rails”
Uses the GitHub API
Print all commits by: `<sha>: <author name>` (one by line)"""
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
