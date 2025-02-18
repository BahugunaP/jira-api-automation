# src/config.py
import os
class Config:
    JIRA_BASE_URL = os.getenv("JIRA_BASE_URL")
    JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
    JIRA_USER_EMAIL = os.getenv("JIRA_USER_EMAIL")
    JIRA_PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY")
    TASK_TYPE = os.getenv("TASK_TYPE")
    @classmethod
    def get(cls, key):
        """Retrieve configuration values."""
        return getattr(cls, key, None)
