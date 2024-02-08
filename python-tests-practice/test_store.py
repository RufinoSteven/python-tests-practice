"""
test_store.py

This module contains tests for the store endpoints of the Swagger Petstore API.
"""

import pytest
from utils import send_request, check_response_status, log_response_details
from config import STORE_ENDPOINT

ORDER_DATA = None

@pytest.mark.order
def test_place_order_for_pet():
    """
    Test placing an order for a pet.
    """
    global ORDER_DATA
    ORDER_DATA = {
        "id": 0,
        "petId": 0,
        "quantity": 0,
        "shipDate": "2023-01-01T00:00:00.000Z",
        "status": "placed",
        "complete": True
    }
    
    response = send_request('POST', f"{STORE_ENDPOINT}/order", data=ORDER_DATA)
    ORDER_DATA = response.json()
    check_response_status(response, 200)
    log_response_details(response)


@pytest.mark.order
def test_get_order_by_id():
    
    """
    Test retrieving an order by ID.
    """
    global ORDER_DATA

    response = send_request('GET', f"{STORE_ENDPOINT}/order/{ORDER_DATA.get('id')}")
    check_response_status(response, 200)
    log_response_details(response)


@pytest.mark.order
def test_delete_order():
    """
    Test deleting an order by ID.
    """
    global ORDER_DATA

    response = send_request('DELETE', f"{STORE_ENDPOINT}/order/{ORDER_DATA.get('id')}")
    check_response_status(response, 200)
    log_response_details(response)


@pytest.mark.inventory
def test_get_inventory():
    """
    Test getting inventory data.
    """
    response = send_request('GET', f"{STORE_ENDPOINT}/inventory")
    check_response_status(response, 200)
    log_response_details(response)


