"""
conftest.py

This file contains the setup and teardown configurations for pytest fixtures used in the automation suite.
These fixtures can be used across all test modules.
"""

import pytest
from config import BASE_URL, API_KEY
import logging
from utils import send_request

def pytest_addoption(parser):
    parser.addoption("--baseurl", action="store", default=BASE_URL, help="base URL for the API under test")
    parser.addoption("--apikey", action="store", default=API_KEY, help="API key for the API under test")

@pytest.fixture(scope="session")
def base_url(request):
    """Fixture to get the base URL from command line or config."""
    return request.config.getoption("--baseurl")

@pytest.fixture(scope="session")
def api_key(request):
    """Fixture to get the API key from command line or config."""
    return request.config.getoption("--apikey")

@pytest.fixture(scope="session")
def configure_logging():
    """Configure logging for the test session."""
    logging.basicConfig(filename='test_automation.log', level=logging.DEBUG, 
                        format='%(asctime)s %(levelname)s %(message)s', filemode='w')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

@pytest.fixture(autouse=True)
def log_test_info(request, configure_logging):
    """Autouse fixture to log test start and end, can be expanded for more detailed logging."""
    logging.info(f"Starting test: {request.node.name}")
    yield
    logging.info(f"Ending test: {request.node.name}")

@pytest.fixture(scope="function")
def cleanup(request, base_url, api_key):
    """Fixture to clean up data after a test. This is just a placeholder and should be customized."""
    yield
