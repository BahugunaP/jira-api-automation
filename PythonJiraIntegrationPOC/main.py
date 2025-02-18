# main.py
import sys
import os
from src.config import Config 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.issue_service import IssueService

if __name__ == "__main__":
    issue_service = IssueService()

    # Example: Create a new issue
    summary = "Test issue"
    description = "This is a test issue created via Python and Jira API."
    issue_key = issue_service.create_new_issue(summary, description, Config.get("JIRA_PROJECT_KEY"), Config.get("TASK_TYPE"))

    if issue_key:
        print(f"Successfully created issue with key: {issue_key}")
    else:
        print("Issue creation failed.")

    # Example: Fetch issue details
    issue_details = issue_service.fetch_issue_details(issue_key)
    if issue_details:
        print(f"Issue details: {issue_details}")
    else:
        print("Failed to fetch issue details.")
