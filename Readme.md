
# Gmail Integration

A FastAPI-based Python project to send and receive emails programmatically using Gmail API and OAuth2 authentication.

## Features

- Send emails via Gmail API
- Read and list inbox emails
- Secure OAuth2 authentication
- RESTful API endpoints for integration

## Installation

1. Clone the repository:
    ```bash
    https://github.com/Monster-manu259/Gmail-Integration.git
    cd Gmail-Intergration
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Environment & Configuration

1. Enable Gmail API in your Google Cloud project.
2. Download `credentials.json` from Google Cloud Console and place it in the project root directory.
3. Create a `.env` file in the root directory with the following variables:
    ```env
    CLIENT_ID= "your_client_id"
    CLIENT_SECRET= "your_client_secret"
    PROJECT_ID= "your_project_id"
    AUTH_URI= "your_auth_url"
    TOKEN_URI= "your_token_url"
    AUTH_PROVIDER_X509_CERT_URL= "auth_provider_url"
    REDIRECT_URI= "redirect_url"
    ```

## Usage

Start the FastAPI server:
```bash
uvicorn main:app --reload
```

## Technologies & Libraries Used

- Python 3.x
- FastAPI
- Uvicorn
- python-dotenv
- google-auth
- google-auth-oauthlib
- google-api-python-client
- pydantic


## License

MIT

- Gmail API
- OAuth2

