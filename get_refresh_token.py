from google_auth_oauthlib.flow import InstalledAppFlow

# Define the scopes you need (e.g., full Drive access)
SCOPES = ['https://www.googleapis.com/auth/drive']

def main():
    # Load client secrets configuration
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secret.json', 
        scopes=SCOPES
    )
    
    # Run the local server flow on your desktop
    # This will automatically open your default web browser
    credentials = flow.run_local_server(port=8080)
    
    # Print the refresh token directly to your terminal
    print("\n--- SUCCESS! COPY THE REFRESH TOKEN BELOW ---")
    print(f"Refresh Token: {credentials.refresh_token}")
    print("---------------------------------------------\n")

if __name__ == '__main__':
    main()
