from fastapi import APIRouter
from pydantic import BaseModel
from src.utils.processor import get_gmail_service, create_message

router = APIRouter()

class EmailBody(BaseModel):
    to: str
    subject: str
    message_text: str


@router.post("/send")
async def send_email(body: EmailBody):
    service = get_gmail_service()

    message = create_message(
        sender="me",
        to=body.to,
        subject=body.subject,
        message_text=body.message_text
    )

    result = service.users().messages().send(
        userId="me",
        body=message
    ).execute()

    return {"status": "sent", "message_id": result.get("id")}
