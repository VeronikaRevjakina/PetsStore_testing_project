"""Custom pet rest client."""
from core.requests.pets.body_generators import get_pet_create_request_body
from core.services.base_client import ApiClient, BASE_URL


class PetsClientApi(ApiClient):
    def __init__(self):
        self.pet_api = ApiClient(f"{BASE_URL}/pet")

    def create_pet(self, id_pet, name_pet, status_pet):
        request = get_pet_create_request_body(id_pet, name_pet, status_pet)
        return self.pet_api.post(json=request)

    def find_by_status(self, status_pet, path=f"/findByStatus"):
        return self.pet_api.get(path=path, params=status_pet)

    def delete_pet(self, id_pet):
        return self.pet_api.delete(f"/{id_pet}")

    def update_pet(self, id_pet, name_pet, status_pet):
        request = get_pet_create_request_body(id_pet, name_pet, status_pet)
        return self.pet_api.put(json=request)

    def find_by_id(self, id_pet):
        return self.pet_api.get(path=f"/{id_pet}")