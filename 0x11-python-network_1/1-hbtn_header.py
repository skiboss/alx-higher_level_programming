#!/usr/bin/python3
"""
    This is a python script which takes in a URL, sends a request to the
    URL and displays the value of the X-Request-Id variable found in the
    header of the response
"""


if __name__ == "__main__":
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as res:
        header = res.headers.get('X-Request-Id')
        print(header)
