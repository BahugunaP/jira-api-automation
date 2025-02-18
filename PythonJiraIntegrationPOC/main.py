# main.py
import sys
import logging 
import os
from src.config import Config 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# Ensure 'logs' directory exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configure logging
logging.basicConfig(
    filename="logs/app.log",
    level=logging.DEBUG,  # Set to DEBUG to capture all logs
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"  # Append logs
)
logging.info("Starting Jira API Integration...")

from src.issue_service import IssueService

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    issue_service = IssueService()

    # Example: Create a new issue
    summary = "Test issue"
    description = "This is a test issue created via Python and Jira API."
    try:
        issue_key = issue_service.create_new_issue(summary, description, Config.get("JIRA_PROJECT_KEY"), Config.get("TASK_TYPE"))

        if issue_key:
            print(f"Successfully created issue with key: {issue_key}")
            logging.info(f"Created issue: {issue_key}")
        else:
            print("Issue creation failed.")
            logging.info("Failed to create issue")

        # Example: Fetch issue details
        issue_details = issue_service.fetch_issue_details(issue_key)
        if issue_details:
            print(f"Issue details: {issue_details}")
            logging.info(f"Issue Details: {issue_details}")
        else:
            print("Failed to fetch Issue details.")
            logging.info(f"Failed to fetch issue details for {issue_key}")
    except Exception as e:
            logging.error(f"An error occurred: {e}")

