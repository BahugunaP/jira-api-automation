import base64
from src.config import Config

def get_auth_headers():
    token = f"{Config.JIRA_USER_EMAIL}:{Config.JIRA_API_TOKEN}"
    encoded_token = base64.b64encode(token.encode()).decode()
    return {
        "Authorization": f"Basic {encoded_token}",
        "Content-Type": "application/json"
    }
