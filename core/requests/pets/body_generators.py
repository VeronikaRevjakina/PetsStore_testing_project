"""Test data population."""
from core.providers.files_provider import get_json_data

TEST_DATA_DIR = "tests/test_data"


def get_pet_create_request_body(id_pet, name_pet, status_pet):
    """Generate create pet request body."""
    request_body = get_json_data(f"{TEST_DATA_DIR}/create_pet")
    request_body['id'] = id_pet
    request_body['name'] = name_pet
    request_body['status'] = status_pet
    return request_body
