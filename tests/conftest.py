import pytest

from core.services.pets.client_methods import PetsClientApi

pet_store_client = PetsClientApi()


@pytest.fixture
def pet_api():
    return PetsClientApi()


@pytest.fixture
def create_pet_fixture(pet_api, id_pet, name_pet, status_pet):
    return pet_api.create_pet(id_pet, name_pet, status_pet)

