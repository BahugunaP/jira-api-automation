# src/jira_client.py

import requests
from jira import JIRA
from src.config import Config  # Import the Config class

class JiraClient:
    def __init__(self):
        self.base_url = Config.get("JIRA_BASE_URL")
        self.user_email = Config.get("JIRA_USER_EMAIL")
        self.api_token = Config.get("JIRA_API_TOKEN")
        options = {"server": self.base_url}
        self.jira = JIRA(options, basic_auth=( self.user_email, self.api_token))
        if not self.base_url or not self.api_token or not self.user_email:
            raise ValueError("JIRA configuration values are missing!")

    def create_issue(self, summary, description, projectKey, taskType="Task", assignee="pankaj.bahuguna@intelliswift.com", ):
          try:
                issue_dict = {
                    "project": {"key": projectKey},
                    "summary": summary,
                    "description": description,
                    "issuetype": {"name": taskType},
                    "assignee": {"name": assignee} 
                }
                new_issue = self.jira.create_issue(fields=issue_dict)
                print(f"Created Issue: {new_issue.key}")
                return new_issue.key
          except Exception as e:
            print(f"Error creating issue: {e}")
            return None


    def get_issue_details(self, issue_key):
        issue = self.jira.issue(issue_key)
        print(f"Issue: {issue.key}")
        print(f"Summary: {issue.fields.summary}")
        print(f"Status: {issue.fields.status}")
        print(f"Description: {issue.fields.description}")
        return issue
    
