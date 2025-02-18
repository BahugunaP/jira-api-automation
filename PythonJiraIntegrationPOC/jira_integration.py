import requests
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("JIRA_CLIENT_ID")
CLIENT_SECRET = os.getenv("JIRA_CLIENT_SECRET")
REDIRECT_URI = "http://localhost:8000/callback"
AUTHORIZATION_CODE = "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI0N2RlZmMzZi00NGZiLTQ5N2UtOWYxZi0yZTYxODZhNTQxMjAiLCJzdWIiOiI3MTIwMjA6OWZlYTExNjMtYTI2MC00YmZkLTk0MWQtOTI2MmQ1NzBiOGRiIiwibmJmIjoxNzM5NDcwMzI0LCJpc3MiOiJhdXRoLmF0bGFzc2lhbi5jb20iLCJpYXQiOjE3Mzk0NzAzMjQsImV4cCI6MTczOTQ3MDYyNCwiYXVkIjoiVTkySmxuVzU0bUJWMDVMeGtnRU9FM0FBUDBXZ29iNlEiLCJjbGllbnRfYXV0aF90eXBlIjoiUE9TVCIsImh0dHBzOi8vaWQuYXRsYXNzaWFuLmNvbS92ZXJpZmllZCI6dHJ1ZSwiaHR0cHM6Ly9pZC5hdGxhc3NpYW4uY29tL3VqdCI6IjQ3ZGVmYzNmLTQ0ZmItNDk3ZS05ZjFmLTJlNjE4NmE1NDEyMCIsInNjb3BlIjpbInJlYWQ6amlyYS13b3JrIiwid3JpdGU6amlyYS13b3JrIl0sImh0dHBzOi8vaWQuYXRsYXNzaWFuLmNvbS9hdGxfdG9rZW5fdHlwZSI6IkFVVEhfQ09ERSIsImh0dHBzOi8vaWQuYXRsYXNzaWFuLmNvbS9oYXNSZWRpcmVjdFVyaSI6dHJ1ZSwiaHR0cHM6Ly9pZC5hdGxhc3NpYW4uY29tL3Nlc3Npb25faWQiOiIzNWJlMWUxNy02NjVmLTRjZWQtODcxMy0zMWRlOTFhYzVlNmQiLCJodHRwczovL2lkLmF0bGFzc2lhbi5jb20vcHJvY2Vzc1JlZ2lvbiI6InVzLWVhc3QtMSJ9.vKP04TBVM9XvKwGL-BIiAZgW2ZWaAIIXkUigwCkStV4"  # Replace with the actual code from Step 2

def get_access_token():
    url = "https://auth.atlassian.com/oauth/token"
    payload = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": AUTHORIZATION_CODE,
        "redirect_uri": REDIRECT_URI
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json()
        access_token = data["access_token"]
        print(f"Access Token: {access_token}")
        return access_token
    else:
        print(f"Error: {response.json()}")

# Run the function
get_access_token()





# import os
# from jira import JIRA
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# # JIRA Credentials from .env file
# JIRA_URL = os.getenv("JIRA_URL")
# JIRA_EMAIL = os.getenv("JIRA_EMAIL")
# JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")


# # Connect to JIRA
# options = {"server": JIRA_URL}
# jira = JIRA(options, basic_auth=(JIRA_EMAIL, JIRA_API_TOKEN))

# # 1. Create a JIRA Ticket
# def create_jira_ticket(project_key, summary, description,assignee="pankaj.bahuguna@intelliswift.com", issue_type="Task"):
#     try:
#         issue_dict = {
#             "project": {"key": project_key},
#             "summary": summary,
#             "description": description,
#             "issuetype": {"name": issue_type},
#             "assignee": {"name": assignee} 
#         }
#         new_issue = jira.create_issue(fields=issue_dict)
#         print(f"Created Issue: {new_issue.key}")
#         return new_issue.key
#     except Exception as e:
#         print(f"Error creating issue: {e}")
#         return None

# # 2. Get JIRA Ticket Details
# def get_ticket_details(issue_key):
#     issue = jira.issue(issue_key)
#     print(f"Issue: {issue.key}")
#     print(f"Summary: {issue.fields.summary}")
#     print(f"Status: {issue.fields.status}")
#     print(f"Description: {issue.fields.description}")

# # Run the functions for testing
# if __name__ == "__main__":
#     # Create a JIRA ticket
#     ticket_key = create_jira_ticket("UIUX", "Test Issue via Python", "This is a test issue created from Python.")

#     # Get the details of the created ticket
#     get_ticket_details(ticket_key)
