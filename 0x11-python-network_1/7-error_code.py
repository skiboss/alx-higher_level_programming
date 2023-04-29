#!/usr/bin/python3
"""This script takes a url, sends a request to the url and
    displays the body of the response"""

import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get(argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
