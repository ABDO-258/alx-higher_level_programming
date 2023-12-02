#!/usr/bin/python3
""" s script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
 and finally displays the body of the response """

import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    datas = {"q": letter}

    r = requests.post(url, data=datas)
    try:
        r_json = r.json()
        if r_json:
            print(f'[{r_json["id"]}] {r_json["name"]}')
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
