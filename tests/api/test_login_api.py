import pytest

class TestLoginAPI:
    def test_login_sucesso(self, auth_api_client, admin_user_credentials):
         token = auth_api_client.login(
            admin_user_credentials["email"],
            admin_user_credentials["password"]
        )
         assert token is not None
         assert isinstance(token, str)
         assert len(token) > 0, "O token de autenticação retornado está vazio."

    def test_login_falha(self, auth_api_client):
         try:
            response = auth_api_client.post(
                "/login",
                data={"email": "naoexiste@teste.com", "password": "senhaerrada"}
            )
            pytest.fail(f"Login com credenciais inválidas deveria falhar com 401, mas retornou {response.status_code}")
         except Exception as e:
            # Captura a exceção HTTPError lançada por raise_for_status()
            assert "401 Client Error: Unauthorized for url" in str(e)