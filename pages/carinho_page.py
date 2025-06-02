from  selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CarinhoPage(BasePage):
    """
    Page Object para a página do carrinho (ou Lista de Compras).
    Contém métodos para interações específicas com a página.
    """
    # Seletores para itens na lista/carrinho
    CART_ITEM_NAME = (By.CSS_SELECTOR, "[data-testid^='shopping-cart-product-name']")
    CART_PRODUCT_CARD = (By.CSS_SELECTOR, ".card.col-3")

    # Botões na Lista de Compras
    ADD_TO_CART_FROM_LIST_BUTTON = (By.CSS_SELECTOR, "button[data-testid='adicionarNoCarrinho']")
    CLEAR_LIST_BUTTON = (By.CSS_SELECTOR, "button[data-testid='limparLista']")

    # Seletores para o preço total e botão finalizar compra (para a página /carrinho real, se for diferente)
    TOTAL_PRICE = (By.CSS_SELECTOR, "h3[data-testid='valor-total']")
    FINALIZE_PURCHASE_BUTTON = (By.CSS_SELECTOR, "button[data-testid='finalizar-compra']")

    # Mensagem de Carrinho/Lista vazia
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "h3[data-testid='shopping-cart-empty-message']")

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.path = "/carrinho" 

    def obter_itens_do_carrinho(self):
        """
        Obtém os nomes dos produtos atualmente no carrinho/lista.
        Ajustado para o data-testid do nome do produto na lista/carrinho.
        """
        item_name_elements = self.find_elements(self.CART_ITEM_NAME)
        return [elem.text for elem in item_name_elements]

    def obter_preco_total(self):
        """
        Obtém o preço total dos itens no carrinho.
        ATENÇÃO: Este seletor (TOTAL_PRICE) pode precisar de confirmação na página /carrinho real.
        """
        return self.get_text(self.TOTAL_PRICE)

    def finalizar_compra(self):
        """
        Finaliza a compra.
        ATENÇÃO: Este botão (FINALIZE_PURCHASE_BUTTON) pode precisar de confirmação na página /carrinho real.
        """
        self.click(self.FINALIZE_PURCHASE_BUTTON)

    def obter_mensagem_carrinho_vazio(self):
        """Obtém a mensagem exibida quando o carrinho está vazio."""
        return self.get_text(self.EMPTY_CART_MESSAGE)

    def adicionar_da_lista_ao_carrinho(self, produto_nome):
        """
        Clica no botão 'Adicionar no carrinho' de um item da Lista de Compras.
        """
        button_locator = (By.XPATH,
                          f"//div[contains(@data-testid, 'shopping-cart-product-name') and text()='{produto_nome}']"
                          f"/ancestor::div[contains(@class, 'card-body')]//button[contains(@data-testid, 'adicionarNoCarrinho')]")
        self.click(button_locator)

    def limpar_lista(self):
        """Clica no botão 'Limpar Lista'."""
        self.click(self.CLEAR_LIST_BUTTON)
