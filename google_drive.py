from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os

# Load these variables securely from your remote server's environment
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REFRESH_TOKEN = os.environ.get("REFRESH_TOKEN")

# Recreate the credentials object
creds = Credentials(
    token=None,  # The library will automatically fetch a fresh access token using the refresh token
    refresh_token=REFRESH_TOKEN,
    token_uri="https://oauth2.googleapis.com/token",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
)

# Build the Drive service
service = build("drive", "v3", credentials=creds)

# Test the connection by listing files
results = service.files().list(pageSize=10).execute()
print(results.get("files", []))
