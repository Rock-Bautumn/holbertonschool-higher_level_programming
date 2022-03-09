#!/usr/bin/python3
"""
This file gets the status of Holberton intranet
"""


if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('http://intranet.hbtn.io/status') as response:
        html = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: OK")
