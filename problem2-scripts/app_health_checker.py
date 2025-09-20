import requests
import logging
from datetime import datetime

# --- CONFIGURATION ---
# List of URLs to check. You can add or change these.
URLS_TO_CHECK = [
    "https://www.google.com",
    "https://www.github.com",
    "http://httpbin.org/status/503", # This is a test site that will return a 503 error
    "https://thissitedoesnotexist12345.com" # This site will fail to connect
]
LOG_FILE = "app_health.log"
REQUEST_TIMEOUT_SECONDS = 5

# --- LOGGING SETUP ---
# Configure logging to output to both a file and the console.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

def check_application_status(url):
    """
    Checks the status of a single application URL.
    Logs 'UP' for successful status codes (2xx) and 'DOWN' for all other cases.
    """
    try:
        # Send an HTTP GET request to the URL with a specified timeout.
        response = requests.get(url, timeout=REQUEST_TIMEOUT_SECONDS)

        # Check if the HTTP status code is in the success range (e.g., 200 OK).
        if 200 <= response.status_code < 300:
            logging.info(f"UP: '{url}' is functioning correctly (Status Code: {response.status_code})")
        else:
            # Any other status code (4xx, 5xx) is considered a problem.
            logging.error(f"DOWN: '{url}' is not functioning correctly (Status Code: {response.status_code})")

    except requests.exceptions.Timeout:
        # Handle cases where the request times out.
        logging.error(f"DOWN: '{url}' is not responding (Request timed out)")

    except requests.exceptions.ConnectionError:
        # Handle cases where the connection fails (e.g., DNS failure, connection refused).
        logging.error(f"DOWN: '{url}' is not reachable (Connection error)")

    except requests.exceptions.RequestException as e:
        # Handle any other request-related exceptions.
        logging.error(f"DOWN: An unexpected error occurred for '{url}': {e}")


def main():
    """Main function to iterate through URLs and check their status."""
    logging.info("--- Starting Application Health Checks ---")
    for url in URLS_TO_CHECK:
        check_application_status(url)
    logging.info("--- Application Health Checks Finished ---")

if __name__ == "__main__":
    main()
