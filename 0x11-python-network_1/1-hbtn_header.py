#!/usr/bin/python3
#Write a Python script that takes in a URL, sends a request to the URL and
#displays the value of the X-Request-Id variable found in the header of the response.
#using the packages urllib and sys

import urllib.request
import sys

def get_x_request_id(url):
    request = urllib.request.Request(url)
    
    with urllib.request.urlopen(request) as response:
        x_request_id = response.headers.get('X-Request-Id')
        return x_request_id

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    x_request_id = get_x_request_id(url)

    print("X-Request-Id:", x_request_id)

