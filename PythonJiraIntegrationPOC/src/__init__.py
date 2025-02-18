import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

from src.auth import get_auth_headers
from .jira_client import JiraClient


__all__ = ["get_auth_headers", "create_issue", "get_issue_details", "logger"]
