import json
import base64
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

SCOPES = [
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.modify",
]


def create_message(sender: str, to: str, subject: str, message_text: str):
    try:
        message = MIMEText(message_text)
        message["to"] = to
        message["from"] = sender
        message["subject"] = subject

        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
        return {"raw": raw}
    except Exception as e:
        raise Exception(f"Error creating email message: {str(e)}")


def get_gmail_service():
    try:
        with open("token.json", "r") as token_file:
            creds_data = json.load(token_file)

        creds = Credentials.from_authorized_user_info(creds_data, SCOPES)

        # Refresh token if expired
        if creds.expired and creds.refresh_token:
            creds.refresh(Request())
            with open("token.json", "w") as f:
                f.write(creds.to_json())

        service = build("gmail", "v1", credentials=creds)
        return service

    except FileNotFoundError:
        raise Exception("token.json missing — authenticate using /auth/login first.")
    except Exception as e:
        raise Exception(f"Failed to initialize Gmail service: {str(e)}")
