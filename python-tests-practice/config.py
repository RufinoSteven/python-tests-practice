"""
config.py

Configuration settings for the automation suite testing the Swagger Petstore API.
"""

# Base URL of the Swagger Petstore API
BASE_URL = "https://petstore.swagger.io/v2"

# Endpoint paths
PET_ENDPOINT = "/pet"
STORE_ENDPOINT = "/store"
USER_ENDPOINT = "/user"

# Timeout settings for API requests
REQUEST_TIMEOUT = 10  # seconds

import logging
LOGGING_LEVEL = logging.DEBUG
LOG_FILE = "test_automation.log"

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

API_KEY = "your_api_key_here"
