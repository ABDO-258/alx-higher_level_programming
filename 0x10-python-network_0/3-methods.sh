#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept.
curl -sI "$URL" | grep -i Allow | awk '{print $2}'
