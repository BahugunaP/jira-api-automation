from jira_client import JiraClient

if __name__ == "__main__":
    jira = JiraClient()

    # Create a JIRA issue
    response = jira.create_issue("New Task Request", "Detailed Task description", "Task")
    print("Created Issue:", response)

    # Fetch issue details
    issue_key = response.get("key", "UNKNOWN")
    details = jira.get_issue_details(issue_key)
    print("Issue Details:", details)
