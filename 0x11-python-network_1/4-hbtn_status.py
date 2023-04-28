#!/usr/bin/python3
""" This script fetches https://alx-intranet.hbtn.io/status """

import requests

if __name__ == "__main__":
    res = requests.get("https://alx-intranet.hbtn.io/status")
    data = res.text
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
