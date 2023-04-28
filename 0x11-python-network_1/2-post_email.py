#!/usr/bin/python3
"""This script takes in a url and an email, sends a POST
    request to the passed URL with the email as a parameter, and
    displays the body of the response"""

import urllib.request
import sys
import urllib.parse

if __name__ == "__main__":

    val = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(val).encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
