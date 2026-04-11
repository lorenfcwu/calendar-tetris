import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def get_calendar_service(user_id="default", force_login=False):
    creds = None
    # Use a unique filename for each user
    token_file = f'token_{user_id}.json'

    # 1. Try to load existing credentials UNLESS we are forcing a login
    if os.path.exists(token_file) and not force_login:
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    
    # 2. If no valid creds, or we forced a login, run the flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token and not force_login:
            creds.refresh(Request())
        else:
            # This triggers the browser window
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
            
        # 3. Save the specific token for THIS user
        with open(token_file, 'w') as token:
            token.write(creds.to_json())

    return build('calendar', 'v3', credentials=creds)

# def get_calendar_service():
#     creds = None
#     # The file token.json stores the user's access and refresh tokens.
#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open('token.json', 'w') as token:
#             token.write(creds.to_json())

#     return build('calendar', 'v3', credentials=creds)

if __name__ == '__main__':
    service = get_calendar_service()
    print("Authentication Successful!")