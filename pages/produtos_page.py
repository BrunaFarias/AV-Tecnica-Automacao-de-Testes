from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProdutosPage(BasePage):
    """
    Page Object para a página de produtos.
    Contém métodos para interações específicas com a página de produtos.
    """
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".card-body") # Cartões de produtos
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[data-test^='adicionar-produto']") # Botão "Adicionar ao carrinho"
    CART_ICON = (By.CSS_SELECTOR, "a[data-test='carrinho']") # Ícone do carrinho

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.path = "/home"

    def navegar_produtos(self):
        """Navega para a página de produtos."""
        self.open(self.path)

    def adicionar_produto_ao_carrinho(self, produto):
        """Adiciona um produto ao carrinho."""
        product_card_locator = (By.XPATH, f"//h5[text()='{produto}']/ancestor::div[@class='card-body']//button[contains(@data-test, 'adicionar-produto')]")
        self.click(product_card_locator)

    def nomes_dos_produtos(self):
        """Obtém os nomes de todos os produtos exibidos na página."""
        product_elements = self.find_elements((By.CSS_SELECTOR, ".card-title"))
        return [elem.text for elem in product_elements]
    
    def ir_carrinho(self):
        """Navega para a página do carrinho."""
        self.click(self.CART_ICON)