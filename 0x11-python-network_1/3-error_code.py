#!/usr/bin/python3
"""This script takes a url and sends a request to the url then
    displays the body of the response"""

import sys
import urllib.request
from urllib.error import HTTPError

if __name__ == "__main__":

    try:
        with urllib.request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode("utf-8"))
    except HTTPError as err:
        print("Error code: {}".format(err.code))
