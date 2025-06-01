from  selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CarinhoPage(BasePage):
    """
    Page Object para a página do carrinho.
    Contém métodos para interações específicas com a página do carrinho.
    """
    CART_ITEMS = (By.CSS_SELECTOR, ".list-group-item") # Itens no carrinho
    TOTAL_PRICE = (By.CSS_SELECTOR, "h3[data-test='valor-total']")
    FINALIZE_PURCHASE_BUTTON = (By.CSS_SELECTOR, "button[data-test='finalizar-compra']")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='shopping-cart-empty-message']")

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.path = "/carrinho"

    def obter_itens_do_carrinho(self):
        """Obtém os itens atualmente no carrinho."""
        item_name_elements = self.find_elements((By.CSS_SELECTOR, ".list-group-item h5"))
        return [elem.text for elem in item_name_elements]
    
    def obter_preco_total(self):
        """Obtém o preço total dos itens no carrinho."""
        return self.get_text(self.TOTAL_PRICE)
    
    def finalizar_compra(self):
        """Finaliza a compra."""
        self.click(self.FINALIZE_PURCHASE_BUTTON)

    def obter_mensagem_carrinho_vazio(self):
        """Obtém a mensagem exibida quando o carrinho está vazio."""
        return self.get_text(self.EMPTY_CART_MESSAGE)

