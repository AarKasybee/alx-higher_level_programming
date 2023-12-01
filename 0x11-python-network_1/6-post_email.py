#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import requests
import sys

def send_post_request(url, email):
    payload = {'email': email}
    response = requests.post(url, data=payload)
    return response.text

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    response_body = send_post_request(url, email)
    
    print("Response Body:")
    print(response_body)

