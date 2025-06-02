import pytest
from utils.data_generator import generate_random_product

class TestProdutosAPI:
    def test_todos_produtos(self, products_api_client):
        response = products_api_client.get_all_products()
        assert response.status_code == 200
        response_json = response.json()
        assert "produtos" in response_json
        assert isinstance(response_json["produtos"], list)
        assert response_json["quantidade"] >= 0 # Deve haver 0 ou mais produtos
