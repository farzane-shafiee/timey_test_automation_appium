from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def get_google_credential():
    """Get google token for credential."""

    creds = None

    if os.path.exists('src/device_data/token.json'):
        creds = Credentials.from_authorized_user_file('src/device_data/token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'src/device_data/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('src/device_data/token.json', 'w') as token:
            token.write(creds.to_json())

    return creds


def create_service(creds):
    return build('gmail', 'v1', credentials=creds)


def get_mails(service, maxResults=10):
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=maxResults).execute()
    messages = results.get('messages', [])

    if not messages:
        print('No messages found in the inbox.')
        return
    return messages


def get_otp(service, messages):
    try:
        latest_otp = ''
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            message_text = get_message_text(msg)

            if message_text["subject"] == 'رمز یکبار مصرف':
                latest_otp = message_text["body"][-5:]
                break

        return latest_otp

    except HttpError as error:
        print(f'An error occurred: {error}')


def get_message_text(message):
    headers = message['payload']['headers']
    subject = next((header['value'] for header in headers if header['name'] == 'Subject'), '')
    from_address = next((header['value'] for header in headers if header['name'] == 'From'), '')
    date = next((header['value'] for header in headers if header['name'] == 'Date'), '')
    body = message['snippet']
    return {'subject': subject, 'from': from_address, 'date': date, 'body': body}


def get_otp_api():
    creds = get_google_credential()  # Authenticate gmail
    service = create_service(creds=creds)  # service read gmail

    mails_list = get_mails(service=service)
    otp = get_otp(service=service, messages=mails_list)
    return otp


if __name__ == '__main__':
    otp = get_otp_api()