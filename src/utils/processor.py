import google.oauth2.credentials
import googleapiclient.discovery
import json
import base64
from email.mime.text import MIMEText
from core.exceptions import HandleException

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def create_message(sender, to, subject, message_text):
    try:
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
        return {"raw": raw}
    except Exception as e:
        raise HandleException(f"Failed to create message: {str(e)}")

def get_gmail_service():
    try:
        with open("token.json", "r") as token_file:
            credentials_data = json.load(token_file)
        creds = google.oauth2.credentials.Credentials.from_authorized_user_info(
            credentials_data,
            scopes=SCOPES
        )
        service = googleapiclient.discovery.build('gmail', 'v1', credentials=creds)
        return service
    except Exception as e:
        raise HandleException(f"Failed to get Gmail service: {str(e)}")