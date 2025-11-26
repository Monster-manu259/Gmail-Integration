from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    def __init__(self):
        self.CLIENT_ID = os.getenv("CLIENT_ID")
        self.CLIENT_SECRET = os.getenv("CLIENT_SECRET")
        self.PROJECT_ID = os.getenv("PROJECT_ID")
        self.AUTH_URI = os.getenv("AUTH_URI")
        self.TOKEN_URI = os.getenv("TOKEN_URI")
        self.CERT_URL = os.getenv("AUTH_PROVIDER_X509_CERT_URL")
        self.REDIRECT_URI = os.getenv("REDIRECT_URI")
    def get_client_config(self):
        return {
            "web": {
                "client_id": self.CLIENT_ID,
                "project_id": self.PROJECT_ID,
                "auth_uri": self.AUTH_URI,
                "token_uri": self.TOKEN_URI,
                "auth_provider_x509_cert_url": self.CERT_URL,
                "client_secret": self.CLIENT_SECRET,
                "redirect_uris": [self.REDIRECT_URI],
                "javascript_origins": ["http://localhost:8000"]
            }
        }

settings = Settings()
