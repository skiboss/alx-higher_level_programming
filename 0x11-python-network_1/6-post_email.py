#!/usr/bin/python3
"""This script takes a url and an email address, sends a post
    request to the passed url with the email as a parameter,
    and finally displays the body of the response"""

import sys
import requests

if __name__ == "__main__":

    value = {"email": sys.argv[2]}
    req = requests.post(sys.argv[1], data=value)
    print(req.text)
