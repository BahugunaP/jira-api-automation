# src/jira_client.py

import os
import logging
from jira import JIRA
from src.config import Config  # Import the Config class


if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/app.log",  # Log file name
    level=logging.INFO,               # Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode ="a" #appand log instead of overwriting
)

class JiraClient:
    def __init__(self):
        self.base_url = Config.get("JIRA_BASE_URL")
        self.user_email = Config.get("JIRA_USER_EMAIL")
        self.api_token = Config.get("JIRA_API_TOKEN")
        options = {"server": self.base_url}
        self.jira = JIRA(options, basic_auth=( self.user_email, self.api_token))
        if not self.base_url or not self.api_token or not self.user_email:
            raise ValueError("JIRA configuration values are missing!")
        else:
             logging.info("JiraClient initialized successfully.")
    def create_issue(self, summary, description, projectKey, taskType="Task", assignee="pankaj.bahuguna@intelliswift.com", ):
          try:
                issue_dict = {
                    "project": {"key": projectKey},
                    "summary": summary,
                    "description": description,
                    "issuetype": {"name": taskType},
                    "assignee": {"name": assignee} 
                }
                logging.info(f"Creating issue: {summary}")
                new_issue = self.jira.create_issue(fields=issue_dict)
                print(f"Created Issue: {new_issue.key}")
                logging.info(f"Issue created successfully: {new_issue.key}")
                return new_issue.key
          except Exception as e:
            logging.error(f"Failed to create issue: {e}")
            print(f"Error creating issue: {e}")
            raise SystemExit(f"Failed to create issue: {e}")


    def get_issue_details(self, issue_key):
         try: 
            issue = self.jira.issue(issue_key)
            return issue
         except Exception as e:
             logging.error(f"Failed to create issue: {e}") 
             raise SystemExit(f"Failed to create issue: {e}")
    
