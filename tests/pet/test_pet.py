import pytest

from core.providers.test_data_population import generate_random_pet_create_parameters, \
    generate_triples_with_unique_statuses, generate_random_pet_status, get_random_pet_name


@pytest.mark.create
@pytest.mark.parametrize('id_pet,name_pet,status_pet', [*generate_random_pet_create_parameters()])
def test_add_new_pet(create_pet_fixture, id_pet, name_pet, status_pet):
    response = create_pet_fixture
    assert response.status_code == 200, f"Success status code {response.status_code}"

    response_body = response.json()
    assert response_body['name'] == name_pet, f"Pet name corresponds to request {name_pet}"
    assert response_body['id'] == id_pet, f"Pet id corresponds to request {id_pet}"
    assert response_body['status'] == status_pet, f"Pet status corresponds to request {status_pet}"


@pytest.mark.getters
@pytest.mark.parametrize("id_pet,name_pet,status_pet", [*generate_triples_with_unique_statuses()])
def test_find_pet_by_status(create_pet_fixture, pet_api, id_pet, name_pet, status_pet):
    response = pet_api.find_by_status(status_pet)
    assert response.status_code == 200, f"Success status code {response.status_code}"

    response_body = response.json()
    assert all(entry['status'] == status_pet for entry in response_body), f"All found pets statuses correspond to " \
                                                                          f"requested {status_pet} "


@pytest.mark.parametrize('id_pet,name_pet,status_pet', [*generate_random_pet_create_parameters(amount_of_runs=3)])
def test_pet_delete(create_pet_fixture, pet_api, id_pet, name_pet, status_pet):
    response = pet_api.delete_pet(id_pet)
    assert response.status_code == 200, f"Success status code {response.status_code}"

    response = pet_api.find_by_id(id_pet)
    assert response.status_code == 404, f"Deleted pet {id_pet} is not found {response.status_code}"


@pytest.mark.parametrize('id_pet,name_pet,status_pet', [*generate_random_pet_create_parameters(amount_of_runs=3)])
def test_pet_update(create_pet_fixture, pet_api, id_pet, name_pet, status_pet):
    updated_status_pet = generate_random_pet_status()
    updated_name_pet = get_random_pet_name()
    response = pet_api.update_pet(id_pet, updated_name_pet, updated_status_pet)
    assert response.status_code == 200, f"Success status code {response.status_code}"

    response_body = response.json()
    assert response_body['id'] == id_pet, f"Pet id is not updated {id_pet}"
    assert response_body['name'] == updated_name_pet, f"Pet name is updated according to {updated_name_pet}"
    assert response_body['status'] == updated_status_pet, f"Pet status corresponds to request {updated_status_pet}"


@pytest.mark.getters
@pytest.mark.parametrize("id_pet,name_pet,status_pet", [*generate_random_pet_create_parameters(amount_of_runs=1)])
def test_find_pet_by_id(create_pet_fixture, pet_api, id_pet, name_pet, status_pet):
    response = pet_api.find_by_id(id_pet)
    assert response.status_code == 200, f"Success status code {response.status_code}"

    response_body = response.json()
    assert response_body['id'] == id_pet, f"Correct pet is found by {id_pet}"
