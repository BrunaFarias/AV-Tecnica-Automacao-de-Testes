from .base_api_cliente import BaseApiCliente

class AutenticacaoApiCliente(BaseApiCliente):
    def __init__(self, base_url):
        super().__init__(base_url)
        self.endpoint = "/login"

    def login(self, email, password):
        """Realiza o login e retorna o token de autenticação."""
        login_data = {
            "email": email,
            "password": password
        }
        response = self.post(self.endpoint, data=login_data)
        return response.json().get("authorization")
