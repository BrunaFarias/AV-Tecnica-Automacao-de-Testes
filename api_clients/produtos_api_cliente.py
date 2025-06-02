from .base_api_cliente import BaseApiCliente

class ProdutosApiCliente(BaseApiCliente):
    """
    Cliente de API para endpoints de produtos.
    """
    def __init__(self, base_url):
        super().__init__(base_url)
        self.endpoint = "/produtos"

    def get_all_products(self):
        """Obtém todos os produtos."""
        return self.get(self.endpoint)

    def create_product(self, name, price, description, quantity, token):
        """Cria um novo produto (requer token de autenticação)."""
        product_data = {
            "nome": name,
            "preco": price,
            "descricao": description,
            "quantidade": quantity
        }
        headers = {"Authorization": token}
        return self.post(self.endpoint, data=product_data, headers=headers)

    def get_product_by_id(self, product_id):
        """Obtém um produto pelo ID."""
        return self.get(f"{self.endpoint}/{product_id}")