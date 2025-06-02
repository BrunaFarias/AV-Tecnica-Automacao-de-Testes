import pytest
from pages.login_page import LoginPage
from pages.produtos_page import ProdutosPage
from pages.lista_de_compras_page import ListaDeComprasPage
from pages.carinho_page import CarinhoPage 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestAddProdutoFrontend: 
    """
    Conjunto de testes para o fluxo de adição de produtos ao carrinho no frontend.
    """

    def test_adicionar_produto_a_lista_e_depois_ao_carrinho(self, driver, base_url_frontend, admin_user_credentials): 
        """
        Testa a adição de um produto à Lista de Compras e depois ao Carrinho.
        Pré-condição: Login de um usuário.
        """
        login_page = LoginPage(driver, base_url_frontend)
        produtos_page = ProdutosPage(driver, base_url_frontend)
        lista_de_compras_page = ListaDeComprasPage(driver, base_url_frontend)
        carrinho_page = CarinhoPage(driver, base_url_frontend) 

        # 1. Realizar login como administrador
        login_page.nav_login() 
        login_page.login(admin_user_credentials["email"], admin_user_credentials["password"])
        login_page.wait.until(EC.url_contains("/home"))

        # 2. Obter o nome do primeiro produto dinamicamente
        product_to_add_name = produtos_page.obter_primeiro_nome_produto()
        print(f"DEBUG: Nome do produto obtido dinamicamente: '{product_to_add_name}'")
        assert product_to_add_name is not None, "Nenhum produto encontrado na página Home para adicionar à lista."        
        produtos_page.adicionar_produto_a_lista_de_compras(product_to_add_name)

        lista_de_compras_page.navegar_lista_de_compras()
        lista_de_compras_page.wait.until(EC.url_contains("/minhaListaDeProdutos"))

        lista_de_compras_page.adicionar_item_da_lista_ao_carrinho(product_to_add_name)

        # 3. Navegar para o carrinho
        produtos_page.ir_carrinho() 
        carrinho_page.wait.until(EC.url_contains("/carrinho"))

        # 4. Verificar se o produto está no carrinho
        cart_items = carrinho_page.obter_itens_do_carrinho() 
        assert product_to_add_name in cart_items, f"O produto '{product_to_add_name}' não foi encontrado no carrinho."
