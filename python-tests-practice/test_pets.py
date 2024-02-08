"""
test_pets.py

This module contains tests for the Pet endpoints of the Swagger Petstore API.
"""

import pytest
from utils import send_request, check_response_status, log_response_details
from config import PET_ENDPOINT

# Test data
valid_pet_id = 1  
invalid_pet_id = 999999  

@pytest.mark.parametrize("pet_id, expected_status", [
    (valid_pet_id, 200),
    (invalid_pet_id, 404)
])
def test_get_pet_by_id(pet_id, expected_status):
    """
    Test retrieving a pet by ID.
    """
    response = send_request('GET', f"{PET_ENDPOINT}/{pet_id}")
    check_response_status(response, expected_status)
    log_response_details(response)
    if expected_status == 200:
        assert response.json()['id'] == pet_id, "The returned pet ID does not match the requested ID."

def test_add_new_pet():
    """
    Test adding a new pet to the store.
    """
    new_pet_data = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    response = send_request('POST', PET_ENDPOINT, data=new_pet_data)
    check_response_status(response, 200)
    log_response_details(response)
    assert response.json()['name'] == new_pet_data['name'], "The name of the added pet does not match."

def test_update_pet():
    """
    Test updating an existing pet in the store.
    """
    updated_pet_data = {
        "id": valid_pet_id,
        "category": {
            "id": 1,
            "name": "updated_category"
        },
        "name": "updated_doggie",
        "photoUrls": [
            "updated_string"
        ],
        "tags": [
            {
                "id": 1,
                "name": "updated_tag"
            }
        ],
        "status": "sold"
    }
    response = send_request('PUT', PET_ENDPOINT, data=updated_pet_data)
    check_response_status(response, 200)
    log_response_details(response)
    assert response.json()['name'] == updated_pet_data['name'], "The name of the updated pet does not match."

def test_delete_pet():
    """
    Test deleting a pet by ID.
    """
 
    pet_data_for_deletion = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "pet_to_delete",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    add_response = send_request('POST', PET_ENDPOINT, data=pet_data_for_deletion)
    pet_id_to_delete = add_response.json()['id']


    delete_response = send_request('DELETE', f"{PET_ENDPOINT}/{pet_id_to_delete}")
    check_response_status(delete_response, 200)
    log_response_details(delete_response)

    verify_response = send_request('GET', f"{PET_ENDPOINT}/{pet_id_to_delete}")
    check_response_status(verify_response, 404)
