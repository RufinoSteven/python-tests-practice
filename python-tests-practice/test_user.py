"""
test_user.py

This module contains tests for the user endpoints of the Swagger Petstore API.
"""

import pytest
from utils import send_request, check_response_status, log_response_details
from config import USER_ENDPOINT

# Test data
user_data = {
    "id": 0,
    "username": "test_user",
    "firstName": "Test",
    "lastName": "User",
    "email": "testuser@example.com",
    "password": "password123",
    "phone": "123-456-7890",
    "userStatus": 0
}

@pytest.fixture(scope="module")
def create_test_user():
    """
    Fixture to create a test user before running tests.
    """
    response = send_request('POST', USER_ENDPOINT, data=user_data)
    check_response_status(response, 200)
    yield
  
    send_request('DELETE', f"{USER_ENDPOINT}/{user_data['username']}")

def test_create_user(create_test_user):
    """
    Test creating a new user.
    """
    response = send_request('GET', f"{USER_ENDPOINT}/{user_data['username']}")
    check_response_status(response, 200)
    log_response_details(response)

def test_user_login():
    """
    Test user login.
    """
    params = {"username": user_data['username'], "password": user_data['password']}
    response = send_request('GET', f"{USER_ENDPOINT}/login", params=params)
    check_response_status(response, 200)
    log_response_details(response)

def test_user_logout():
    """
    Test user logout.
    """
    response = send_request('GET', f"{USER_ENDPOINT}/logout")
    check_response_status(response, 200)
    log_response_details(response)

def test_delete_user(create_test_user):
    """
    Test deleting a user.
    """
    response = send_request('DELETE', f"{USER_ENDPOINT}/{user_data['username']}")
    check_response_status(response, 200)
    log_response_details(response)

