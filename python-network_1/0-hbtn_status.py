#!/usr/bin/python3

"""
Script to fetch a URL and display the response body.
URL: https://intranet.hbtn.io/status
"""

import urllib.request

if __name__ == "__main__":
    # URL to fetch
    url = 'https://intranet.hbtn.io/status'

    # Headers for the request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Create a request object with the URL and headers
    req = urllib.request.Request(url, headers=headers)

    # Fetch the URL and retrieve the response
    with urllib.request.urlopen(req) as response:
        # Read the response content as bytes
        r = response.read()

        # Display the response body
        print("Body response:")
        print("\t- type: {}".format(type(r)))
        print("\t- content: {}".format(r))
        print("\t- utf8 content: {}".format(r.decode("UTF-8")))
