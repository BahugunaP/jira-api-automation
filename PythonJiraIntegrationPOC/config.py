import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration settings for different environments"""

    JIRA_CLIENT_ID = os.getenv("JIRA_CLIENT_ID")
    JIRA_CLIENT_SECRET = os.getenv("JIRA_CLIENT_SECRET")
    JIRA_REFRESH_TOKEN = os.getenv("JIRA_REFRESH_TOKEN")
    JIRA_CLOUD_ID = os.getenv("JIRA_CLOUD_ID")
    PROJECT_KEY = os.getenv("PROJECT_KEY")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    ASSIGNEE = os.getenv("ASSIGNEE")
config = Config()
