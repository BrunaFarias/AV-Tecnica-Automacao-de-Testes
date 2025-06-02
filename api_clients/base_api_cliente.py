import requests

class BaseApiCliente:
    """
    Classe base para todos os clientes de API.
    Gerencia a URL base e cabeçalhos comuns.
    """
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {"Content-Type": "application/json"}
  
    def _send_request(self, method, endpoint, data=None, headers=None, params=None):
        """
        Método genérico para enviar requisições HTTP.
        """
        url = f"{self.base_url}{endpoint}"
        combined_headers = {**self.headers, **(headers or {})} # Combina cabeçalhos padrão com os específicos
        try:
            response = requests.request(method, url, json=data, headers=combined_headers, params=params)
            response.raise_for_status() # Lança um HTTPError para códigos de status de erro (4xx ou 5xx)
            return response
        except requests.exceptions.HTTPError as e:
            print(f"Erro HTTP: {e.response.status_code} - {e.response.text}")
            raise
        except requests.exceptions.RequestException as e:
            print(f"Erro de requisição: {e}")
            raise

    def get(self, endpoint, headers=None, params=None):
        """Envia uma requisição GET."""
        return self._send_request("GET", endpoint, headers=headers, params=params)

    def post(self, endpoint, data, headers=None):
        """Envia uma requisição POST."""
        return self._send_request("POST", endpoint, data=data, headers=headers)

    def put(self, endpoint, data, headers=None):
        """Envia uma requisição PUT."""
        return self._send_request("PUT", endpoint, data=data, headers=headers)

    def delete(self, endpoint, headers=None):
        """Envia uma requisição DELETE."""
        return self._send_request("DELETE", endpoint, headers=headers)