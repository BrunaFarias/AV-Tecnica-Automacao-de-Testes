import pytest
from utils.data_generator import generate_random_user

class TestUsuariosAPI:
    """
    Conjunto de testes para os endpoints de usuários da API.
    """

    def test_criar_novo_usuario_sucesso(self, users_api_client, new_user_data):
        """
        Testa a criação bem-sucedida de um novo usuário via API.
        Após a criação, tenta obter o usuário para validar.
        """
        # 1. Cria um novo usuário
        response = users_api_client.create_user(
            new_user_data["nome"],
            new_user_data["email"],
            new_user_data["senha"],
            administrador="false" # Pode ser "true" ou "false"
        )
        assert response.status_code == 201
        response_json = response.json()
        assert "message" in response_json
        assert "Cadastro realizado com sucesso" in response_json["message"]
        assert "_id" in response_json
        user_id = response_json["_id"]

        # 2. Verifica se o usuário pode ser obtido pelo ID
        get_response = users_api_client.get_user_by_id(user_id)
        assert get_response.status_code == 200
        get_response_json = get_response.json()
        assert get_response_json["nome"] == new_user_data["nome"]
        assert get_response_json["email"] == new_user_data["email"]


    def test_listar_todos_usuarios(self, users_api_client):
        """
        Testa a listagem de todos os usuários.
        Espera que a resposta contenha uma lista de usuários.
        """
        response = users_api_client.get_all_users()
        assert response.status_code == 200
        response_json = response.json()
        assert "usuarios" in response_json
        assert isinstance(response_json["usuarios"], list)
        assert response_json["quantidade"] >= 0 # Deve haver 0 ou mais usuários

    def test_criar_usuario_email_existente(self, users_api_client, admin_user_credentials):
        """
        Testa a criação de um usuário com um email já existente.
        Espera que a API retorne um erro (ex: 400 Bad Request ou 409 Conflict).
        """
        # Tenta criar um usuário com um email já existente (usando o email do admin para exemplo)
        try:
            response = users_api_client.create_user(
                "Usuario Duplicado",
                admin_user_credentials["email"],
                "senha123",
                administrador="false"
            )
            pytest.fail(f"Criação de usuário com email existente deveria falhar, mas retornou {response.status_code}")
        except Exception as e:
            # A API Serverest retorna 400 Bad Request para email já cadastrado
            assert "400 Client Error: Bad Request for url" in str(e)
