#!/usr/bin/python3
"""  script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""

from urllib import request
from urllib.error import HTTPError
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            decoded_response = response.read().decode("utf-8")
            print(decoded_response)
    except HTTPError as error:
        print(f"Error code: {error.code}")
