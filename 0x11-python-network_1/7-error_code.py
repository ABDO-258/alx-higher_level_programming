#!/usr/bin/python3
""" s script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
 and finally displays the body of the response """

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
