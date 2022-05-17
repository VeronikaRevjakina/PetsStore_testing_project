"""Test data population."""
import random

from core.enums.pet import PetStatuses


def get_all_pet_statuses():
    """Get all pet statuses."""
    return [status.value for status in PetStatuses]


def generate_random_pet_status():
    """Generate random pet status value."""
    return random.choice(get_all_pet_statuses()).value
