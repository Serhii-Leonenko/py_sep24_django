import os
from pprint import pprint

import requests
from dotenv import load_dotenv
"""
This script guides the user through the OAuth2 flow to obtain an access token and refresh token
"""

load_dotenv()

APP_KEY = os.environ["DROPBOX_APP_KEY"]
APP_SECRET = os.environ["DROPBOX_APP_SECRET"]

authorize_url = f"https://www.dropbox.com/oauth2/authorize?client_id={APP_KEY}&token_access_type=offline&response_type=code"
print("1. Go to: " + authorize_url)
print("2. Click \"Allow\" (you might have to log in first).")
print("3. Copy the authorization code.")
auth_code = input("Enter the authorization code here: ").strip()

auth = (APP_KEY, APP_SECRET)
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}
url = "https://api.dropboxapi.com/oauth2/token"

payload = {
    "code": auth_code,
    "grant_type": "authorization_code",
}

response = requests.post(url, data=payload, headers=headers, auth=auth)

# Check the response
if response.status_code == 200:
    print("Access token obtained successfully:")
    pprint(response.json())
else:
    print("Failed to obtain access token:")
    print(response.status_code, response.text)
