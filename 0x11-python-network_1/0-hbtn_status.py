#!/usr/bin/python3
#Write a Python script that fetches https://alx-intranet.hbtn.io/status
#using urlib

You must use the package urllib
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        data = response.read()
        print("Body response:")
        print("\t- type:", type(data))
        print("\t- content:", data.decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error code:", e.code)
except urllib.error.URLError as e:
    print("URL Error:", e.reason)

