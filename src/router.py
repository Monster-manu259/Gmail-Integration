from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
import google_auth_oauthlib.flow
from src.utils.processor import SCOPES, create_message, get_gmail_service

router = APIRouter()

@router.get("/")
async def login():

    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        "credentials.json",
        scopes=SCOPES
    )
    flow.redirect_uri = "http://localhost:8000/oauth2callback"

    authorization_url, state = flow.authorization_url(
        access_type="offline",
        include_granted_scopes="true"
    )

    with open("state.txt", "w") as f:
        f.write(state)

    return RedirectResponse(authorization_url)


@router.get("/oauth2callback")
async def oauth_callback(request: Request):
    import google_auth_oauthlib.flow

    with open("state.txt", "r") as f:
        state = f.read()

    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        "credentials.json",
        scopes=SCOPES,
        state=state
    )
    flow.redirect_uri = "http://localhost:8000/oauth2callback"

    flow.fetch_token(authorization_response=str(request.url))

    credentials = flow.credentials

    with open("token.json", "w") as token_file:
        token_file.write(credentials.to_json())

    return {"message": "Authentication successful! You can now send emails using Gmail API."}


@router.post("/send")
async def send_mail():
    service = get_gmail_service()

    email_msg = create_message(
        sender="your_email@gmail.com",
        to="chakra@gmail.com",
        subject="Greetings!",
        message_text="Hello Mr.Chakra Teja, It's great connecting with you!"
    )

    result = service.users().messages().send(
        userId="me",
        body=email_msg
    ).execute()

    return {"message": f"Email sent! Message ID: {result['id']}"}