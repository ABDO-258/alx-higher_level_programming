#!/usr/bin/python3
"""  script that uses the GitHub API to display the user ID
using Basic Authentication with a personal access token """

import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    r = requests.get(url, auth=(username, password))
    if r.status_code == 200:
        data = r.json()
        user_id = data["id"]
        print(user_id)
    else:
        print(None)
