# src/issue_service.py

from src.jira_client import JiraClient
import logging

logging.basicConfig(filename="logs/app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class IssueService:
    def __init__(self):
        self.jira_client = JiraClient()  # Instantiate the JiraClient class

    def create_new_issue(self, summary, description, projectKey, taskType):
        """Creates a new issue with default project and issue type."""
      
        # Use the method through the instance of JiraClient
        issue_key = self.jira_client.create_issue(summary, description, projectKey, taskType)

        if issue_key:
            return issue_key
        else:
            return None

    def fetch_issue_details(self, issue_key):
        """Fetches issue details."""
        issue_details = self.jira_client.get_issue_details(issue_key)
        if issue_details:
            return issue_details
        else:
            return None
