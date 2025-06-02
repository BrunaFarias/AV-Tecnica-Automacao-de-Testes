import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class ProdutosPage(BasePage):
    """
    Page Object para a página de produtos.
    Contém métodos para interações específicas com a página de produtos.
    """
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".card-body") # Cartões de produtos
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".card-title.negrito") 
    PRODUCT_DETAIL_LINK = (By.CSS_SELECTOR, "a[data-testid='product-detail-link']")
    CART_ICON = (By.CSS_SELECTOR, "a[data-testid='carrinho']")
    ADD_TO_LIST_BUTTON = (By.CSS_SELECTOR, "button[data-testid='adicionarNaLista']")

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.path = "/home"

    def navegar_produtos(self):
        """Navega para a página de produtos."""
        self.open(self.path)

    def adicionar_produto_a_lista_de_compras(self, produto):
        """Adiciona um produto a lista."""
        detalhes_link_locator = (By.XPATH,
                                 f"//h5[text()='{produto}']/ancestor::div[@class='card-body']"
                                 f"//button[contains(@data-testid, 'adicionarNaLista')]")
        
        self.click(detalhes_link_locator)
        time.sleep(1) 
        print(f"DEBUG: Clique em 'Adicionar a lista' para '{produto}' realizado e 1s de pausa. Indo para a lista de compras.")

        try:
            # Espera explícita para o elemento estar visível e clicável
            self.wait.until(EC.visibility_of_element_located(detalhes_link_locator))
            print(f"DEBUG (ProdutosPage): Botão 'Adicionar a lista' para '{produto}' está VISÍVEL.")
            
            self.wait.until(EC.element_to_be_clickable(detalhes_link_locator))
            print(f"DEBUG (ProdutosPage): Botão 'Adicionar a lista' para '{produto}' está CLICÁVEL.")
            
            self.click(detalhes_link_locator) # Executa o clique
            print(f"DEBUG (ProdutosPage): Clique em 'Adicionar a lista' para '{produto}' realizado.")
            time.sleep(1) 

        except Exception as e:
            print(f"DEBUG (ProdutosPage): ERRO ao tentar clicar no botão 'Adicionar a lista' para '{produto}': {e}")
            raise       

    def nomes_dos_produtos(self):
        """Obtém os nomes de todos os produtos exibidos na página."""
        product_elements = self.find_elements(self.PRODUCT_TITLE)
        return [elem.text for elem in product_elements]
    
    def obter_primeiro_nome_produto(self):
        """
        Obtém o nome do primeiro produto exibido na página.
        Retorna None se nenhum produto for encontrado.
        """
        product_titles = self.nomes_dos_produtos()
        if product_titles:
            return product_titles[0]
        return None   
    
    def ir_carrinho(self):
        """Navega para a página do carrinho."""
        self.click(self.CART_ICON)