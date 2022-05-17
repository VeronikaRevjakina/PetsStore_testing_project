"""Enum for pet statuses"""
from enum import Enum


class PetStatuses(str, Enum):
    """Pet statuses."""

    available = "available"
    pending = "pending"
    sold = "sold"
