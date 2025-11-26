from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from pathlib import Path
import google_auth_oauthlib.flow
from src.utils.processor import SCOPES
from src.config.settings import settings
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


router = APIRouter()

REDIRECT_URI = settings.REDIRECT_URI


@router.get("/login")
async def login():
    flow = google_auth_oauthlib.flow.Flow.from_client_config(
        settings.get_client_config(),
        scopes=SCOPES
    )
    flow.redirect_uri = REDIRECT_URI

    auth_url, state = flow.authorization_url(
        access_type="offline",
        include_granted_scopes="true",
        prompt="consent"
    )

    Path("state.txt").write_text(state)
    return RedirectResponse(auth_url)


@router.get("/callback")
async def callback(request: Request):
    try:
        state = Path("state.txt").read_text()
        flow = google_auth_oauthlib.flow.Flow.from_client_config(
            settings.get_client_config(),
            scopes=SCOPES,
            state=state
        )
        flow.redirect_uri = REDIRECT_URI
        flow.fetch_token(authorization_response=str(request.url))
        creds = flow.credentials
        Path("token.json").write_text(creds.to_json())
        return {"message": "Authentication successful Now you can send emails."}
    except Exception as e:
        return {"error": str(e)}
