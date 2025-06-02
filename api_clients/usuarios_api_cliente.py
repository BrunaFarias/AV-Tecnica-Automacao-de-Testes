from .base_api_cliente import BaseApiCliente

class UsuariosApiCliente(BaseApiCliente):
    """
    Cliente de API para endpoints de usuários.
    """
    def __init__(self, base_url):
        super().__init__(base_url)
        self.endpoint = "/usuarios"

    def create_user(self, name, email, password, administrador="false"):
        """Cria um novo usuário."""
        user_data = {
            "nome": name,
            "email": email,
            "password": password,
            "administrador": administrador
        }
        return self.post(self.endpoint, data=user_data)

    def get_user_by_id(self, user_id):
        """Obtém um usuário pelo ID."""
        return self.get(f"{self.endpoint}/{user_id}")

    def get_all_users(self):
        """Obtém todos os usuários."""
        return self.get(self.endpoint)

    def delete_user(self, user_id, token):
        """Deleta um usuário pelo ID (requer token de autenticação)."""
        headers = {"Authorization": token}
        return self.delete(f"{self.endpoint}/{user_id}", headers=headers)
