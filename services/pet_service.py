import requests

class PetService:
    def __init__(self):
        self.base_url = "https://petstore.swagger.io/v2/pet"

    def create_pet(self, payload):
        return requests.post(self.base_url, json=payload)

    def get_pet_by_id(self, pet_id):
        return requests.get(f"{self.base_url}/{pet_id}")

    def update_pet(self, payload):
        return requests.put(self.base_url, json=payload)

    def delete_pet(self, pet_id):
        return requests.delete(f"{self.base_url}/{pet_id}")