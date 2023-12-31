#!/usr/bin/python3
"""  script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8) """

from urllib import request, parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    data = {"email": sys.argv[2]}
    data_encode = parse.urlencode(data).encode("utf-8")
    req = request.Request(url, data=data_encode, method='POST')
    with request.urlopen(req) as response:
        decoded_response = response.read().decode("utf-8")
        print(decoded_response)
