from pydantic import BaseModel
from typing import Optional

class AuthSuccessResponse(BaseModel):
    message: str

class AuthErrorResponse(BaseModel):
    error: str

class EmailSendSuccessResponse(BaseModel):
    message: str
    message_id: Optional[str] = None

class EmailSendErrorResponse(BaseModel):
    error: str
	