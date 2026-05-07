import pytest
from jsonschema import validate
from services.pet_service import PetService
from schemas.pet_schema import PET_SCHEMA

class TestPet:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.pet_service = PetService()
        self.pet_id = 12345
        self.pet_payload = {
            "id": self.pet_id,
            "name": "Nina Santos",
            "status": "available"
        }

    def test_ciclo_de_vida_pet(self):
        # POST
        response = self.pet_service.create_pet(self.pet_payload)
        assert response.status_code == 200
        assert response.json()["name"] == self.pet_payload["name"]

        # GET
        response = self.pet_service.get_pet_by_id(self.pet_id)
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 2.0

        # PUT
        self.pet_payload["status"] = "sold"
        response = self.pet_service.update_pet(self.pet_payload)
        assert response.json()["status"] == "sold"

        # DELETE
        response = self.pet_service.delete_pet(self.pet_id)
        assert response.status_code == 200

    def test_validar_contrato_pet(self):
        self.pet_service.create_pet(self.pet_payload)

        response = self.pet_service.get_pet_by_id(12345)
        
        response_data = response.json()

        validate(instance=response_data, schema=PET_SCHEMA)
        
        assert response.status_code == 200