#!/bin/bash
# print the byte counts of requested URL
curl -s "$1" | wc -c
