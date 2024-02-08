"""
utils.py

Utility functions for the automation suite testing the Swagger Petstore API.
"""

import requests
from config import BASE_URL, HEADERS, REQUEST_TIMEOUT

def send_request(method, endpoint, data=None, params=None):
    """
    Send an HTTP request to the specified endpoint.

    :param method: HTTP method (e.g., 'GET', 'POST', 'PUT', 'DELETE')
    :param endpoint: API endpoint path
    :param data: Data to be sent in the body of the request (optional)
    :param params: Dictionary of URL parameters (optional)
    :return: Response object
    """
    url = f"{BASE_URL}{endpoint}"
    if method.upper() == 'GET':
        response = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT, params=params)
    elif method.upper() == 'POST':
        response = requests.post(url, headers=HEADERS, json=data, timeout=REQUEST_TIMEOUT, params=params)
    elif method.upper() == 'PUT':
        response = requests.put(url, headers=HEADERS, json=data, timeout=REQUEST_TIMEOUT, params=params)
    elif method.upper() == 'DELETE':
        response = requests.delete(url, headers=HEADERS, timeout=REQUEST_TIMEOUT, params=params)
    else:
        raise ValueError(f"Unsupported HTTP method: {method}")
    return response

def check_response_status(response, expected_status):
    """
    Check if the response status code matches the expected status code.

    :param response: Response object
    :param expected_status: Expected HTTP status code
    :return: None, raises an exception if the status codes do not match
    """
    if response.status_code != expected_status:
        raise AssertionError(f"Expected status {expected_status}, got {response.status_code}")

def log_response_details(response):
    """
    Log the details of an HTTP response. This function can be expanded to include
    more detailed logging based on the project requirements.

    :param response: Response object
    :return: None
    """
    print(f"URL: {response.url}")
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")

