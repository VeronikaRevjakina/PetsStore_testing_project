"""Test data population."""
import random

import names

from core.enums.pet import PetStatuses


def get_all_pet_statuses():
    """Get all pet statuses."""
    return [status.value for status in PetStatuses]


def generate_random_pet_create_parameters(amount_of_runs=10):
    """Generate random pet create parameters."""
    for i in range(amount_of_runs):
        id_pet = get_random_pet_id()
        name_pet = get_random_pet_name()
        status_pet = generate_random_pet_status()
        yield id_pet, name_pet, status_pet


def generate_triples_with_unique_statuses():
    """Generate tuple with status for pets."""
    for status in get_all_pet_statuses():
        id_pet = get_random_pet_id()
        name_pet = get_random_pet_name()
        yield id_pet, name_pet, status


def generate_random_pet_status():
    """Generate random pet status value."""
    return random.choice(get_all_pet_statuses())


def get_random_pet_id():
    """Generate random pet id."""
    return random.randint(1, 100)


def get_random_pet_name():
    """Generate random pet name."""
    return names.get_last_name()
