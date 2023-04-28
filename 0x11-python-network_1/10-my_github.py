#!/usr/bin/python3
"""This is a script that takes github credentials and use the 
github API to display an id"""

import sys
import requests

if __name__ == "__main__":

    req = requests.get("https://api.github.com/user",
                        auth=(sys.argv[1], sys.argv[2]))
    if req.status_code >= 400:
        print('None')
    else:
        print(req.json().get('id'))
