import random

import pytest
import names

from core.providers.test_data_population import get_all_pet_statuses, generate_random_pet_status


@pytest.mark.parametrize("status", get_all_pet_statuses())
def test_find_pet_by_status(pet_api, status):
    response = pet_api.get(path=f"/findByStatus", params=status)

    # response = response.json()
    assert response.status_code == 200, f"Success status code {response.status_code}"
    assert response["status"] == status, f"Returned pet statuses correspond to input {status}"


@pytest.mark.parametrize('id_pet', [random.randint(1, 100) for i in range(10)])
def test_add_new_pet(pet_api, id_pet: int):
    name_pet = names.get_last_name()
    status_pet = generate_random_pet_status()
    request = {
        "id": id_pet,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": name_pet,
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": status_pet
    }

    response = pet_api.post(json=request)
    assert response.status_code == 200, f"Success status code {response.status_code}"

    response_body = response.json()
    assert response_body['name'] == name_pet, f"Pet name corresponds to request {name_pet}"
    assert response_body['id'] == id_pet, f"Pet id corresponds to request {id_pet}"
    assert response_body['status'] == status_pet, f"Pet status corresponds to request {status_pet}"