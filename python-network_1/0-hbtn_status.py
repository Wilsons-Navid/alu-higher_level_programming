#!/usr/bin/python3

# Import the urllib module to handle the HTTP request
import urllib.request

# Function to fetch URL and display response body
def fetch_url(url):
    # Fetch the URL and retrieve the response body
    with urllib.request.urlopen(url) as response:
        # Read the response content as bytes
        body_bytes = response.read()

    # Convert response body bytes to UTF-8 encoded string
    body_utf8 = body_bytes.decode('utf-8')

    # Display the response body with tabulation
    print("\t- Body response:")
    print(f"\t\t- type: {type(body_bytes)}")
    print(f"\t\t- content: {body_bytes}")
    print(f"\t\t- utf8 content: {body_utf8}")


if __name__ == "__main__":
    # URL to fetch
    url = 'https://alu-intranet.hbtn.io/status'

    # Call the fetch_url function with the specified URL
    fetch_url(url)
