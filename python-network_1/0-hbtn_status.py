#!/usr/bin/python3
"""
Fetches the status from https://intranet.hbtn.io/status, handling
potential authentication or access restriction issues.

Requires the `requests` library (install using `pip install requests`)
"""

import requests

def fetch_status(url="https://intranet.hbtn.io/status", username=None, password=None):
  """
  Fetches the status from the provided URL, optionally using authentication.

  Args:
      url (str, optional): The URL to fetch the status from. Defaults to "https://intranet.hbtn.io/status".
      username (str, optional): The username for authentication. Defaults to None.
      password (str, optional): The password for authentication. Defaults to None.

  Returns:
      str or None: The response body content (decoded as UTF-8) if successful, or None on error.
  """

  try:
    if username and password:
      # Authentication is provided, use requests with credentials
      response = requests.get(url, auth=(username, password))
    else:
      # No authentication provided, use basic urllib.request
      response = urllib.request.urlopen(url)

    response.raise_for_status()  # Raise an exception for non-2xx status codes

    # Successful response
    content = response.text  # Access the response body as text (decoded UTF-8)
    return content

  except requests.exceptions.RequestException as e:
    # Handle any request-related exceptions
    print(f"Error: {e}")
    return None
  except urllib.error.HTTPError as e:
    # Handle HTTP errors specifically
    print(f"HTTP Error: {e.code} - {e.reason}")
    return None

if __name__ == "__main__":
  # Example usage without authentication
  status = fetch_status()
  if status:
    print("Received response:")
    print(status)  # Process the retrieved status as needed

  # Example usage with authentication (replace with actual credentials)
  # status = fetch_status(url="https://your_custom_url", username="your_username", password="your_password")
  # ... process status as needed ...

