#!/usr/bin/python3
"""
This file gets the status of Holberton intranet
"""
from sys import argv

if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen(argv[1]) as response:
        # headinfo = response.read()
        # print(headinfo.headers)
        # print(dir(response))
        print(response.headers["X-Request-Id"])
        # print(f"response info:\n {response.info()}")
