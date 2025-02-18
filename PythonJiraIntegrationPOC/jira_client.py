import requests
import os
import logging
from config import config

# Logging setup
logging.basicConfig(
    filename="logs/app.log",
    level=config.LOG_LEVEL,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

class JiraClient:
    """Handles JIRA API interactions"""

    def __init__(self):
        self.access_token = self.get_access_token()

    def get_access_token(self):
        """Retrieve or refresh access token"""
        if os.path.exists("access_token.txt"):
            with open("access_token.txt", "r") as file:
                return file.read().strip()
        return self.refresh_access_token(config.JIRA_REFRESH_TOKEN)

    def refresh_access_token(self, refresh_token):
        """Refresh OAuth 2.0 access token"""
        url = "https://auth.atlassian.com/oauth/token"
        payload = {
            "grant_type": "refresh_token",
            "client_id": config.JIRA_CLIENT_ID,
            "client_secret": config.JIRA_CLIENT_SECRET,
            "refresh_token": refresh_token
        }

        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            new_access_token = data["access_token"]
            new_refresh_token = data["refresh_token"]

            # Save new tokens
            with open("access_token.txt", "w") as file:
                file.write(new_access_token)

            # Update refresh token in .env
            os.environ["JIRA_REFRESH_TOKEN"] = new_refresh_token

            logging.info("Token refreshed successfully!")
            return new_access_token
        else:
            logging.error(f"Error refreshing token: {response.json()}")
            raise Exception("Failed to refresh access token")

    def create_issue(self, summary, description, issue_type="Task"):
        """Create a JIRA issue"""
        url = f"https://api.atlassian.com/ex/jira/{config.JIRA_CLOUD_ID}/rest/api/2/issue"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = {
            "fields": {
                "project": {"key": config.PROJECT_KEY},
                "summary": summary,
                "description": description,
                "issuetype": {"name": issue_type},
                "assignee": {"name": config.ASSIGNEE} 
            }
        }

        response = requests.post(url, headers=headers, json=payload)

        # Handle expired token case
        if response.status_code == 401:
            logging.warning("Token expired. Refreshing...")
            self.access_token = self.refresh_access_token(config.JIRA_REFRESH_TOKEN)
            headers["Authorization"] = f"Bearer {self.access_token}"
            response = requests.post(url, headers=headers, json=payload)

        return response.json()

    def get_issue_details(self, issue_key):
        """Fetch JIRA issue details"""
        url = f"https://api.atlassian.com/ex/jira/{config.JIRA_CLOUD_ID}/rest/api/2/issue/{issue_key}"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Accept": "application/json"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 401:
            logging.warning("Token expired. Refreshing...")
            self.access_token = self.refresh_access_token(config.JIRA_REFRESH_TOKEN)
            headers["Authorization"] = f"Bearer {self.access_token}"
            response = requests.get(url, headers=headers)

        return response.json()
