#!/usr/bin/python3

import urllib.request


def fetch_url(url):
    # Fetch the URL and retrieve the response body
    with urllib.request.urlopen(url) as response:
        # Read the response content and decode it as UTF-8
        body = response.read().decode('utf-8')

    # Display the response body with tabulation
    print(f"\t- Body response:")
    print(f"\t\t- type: {type(body)}")
    print(f"\t\t- content: {body}")


if __name__ == "__main__":
    # URL to fetch
    url = 'https://alu-intranet.hbtn.io/status'

    # Call the fetch_url function with the specified URL
    fetch_url(url)
