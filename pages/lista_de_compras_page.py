import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException 


class ListaDeComprasPage(BasePage):
    """
    Page Object para a página de Lista de Compras.
    """
    ADICIONAR_NO_CARRINHO_BUTTON = (By.CSS_SELECTOR, "button[data-testid='adicionar carrinho']")
    LIMPAR_LISTA_BUTTON = (By.CSS_SELECTOR, "button[data-testid='limparLista']")
    PAGINA_INICIAL_BUTTON = (By.CSS_SELECTOR, "button[data-testid='paginaInicial']")

    LIST_ITEM_NAME = (By.CSS_SELECTOR, "h5.card-title.negrito") 

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.path = "/minhaListaDeProdutos"

    def navegar_lista_de_compras(self):
        """Navega para a página da Lista de Compras."""
        self.open(self.path)

    def adicionar_item_da_lista_ao_carrinho(self, produto_nome):
        """
        Clica no botão 'Adicionar no carrinho' de um item específico na Lista de Compras.
        """
        adicionar_ao_carrinho_locator = (By.XPATH,
                                         f"//h5[text()='{produto_nome}']"
                                         f"//ancestor::div[contains(@class, 'card-body')]//button[@data-testid='adicionar carrinho']")
        print(f"DEBUG (ListaCompras): Tentando clicar no botão 'Adicionar no carrinho' para: '{produto_nome}'")
        print(f"DEBUG (ListaCompras): XPath gerado: {adicionar_ao_carrinho_locator}")

        try:
            time.sleep(2) # Pausa de 2 segundos para observação visual
            print(f"DEBUG (ListaCompras): Pausa de 2s antes de buscar o elemento.")
            
            # Espera que o elemento esteja PRESENTE no DOM e VISÍVEL
            self.wait.until(EC.visibility_of_element_located(adicionar_ao_carrinho_locator))
            print(f"DEBUG (ListaCompras): Botão para '{produto_nome}' AGORA ESTÁ VISÍVEL.")
            
            # Espera que o elemento seja CLICÁVEL
            self.wait.until(EC.element_to_be_clickable(adicionar_ao_carrinho_locator))
            print(f"DEBUG (ListaCompras): Botão para '{produto_nome}' AGORA ESTÁ CLICÁVEL.")
            
            self.click(adicionar_ao_carrinho_locator) 
            print(f"DEBUG (ListaCompras): Clique no botão 'Adicionar no carrinho' (da lista) realizado com sucesso.")

        except (TimeoutException, ElementClickInterceptedException) as e:
            print(f"DEBUG (ListaCompras): Clique NORMAL falhou ou foi interceptado: {e}. Tentando clique via JavaScript (se o problema for sobreposição).")
            # Tenta clique via JavaScript como fallback, se o problema for sobreposição ou algo impedindo o clique normal
            try:
                js_element = self.find_element(adicionar_ao_carrinho_locator) 
                self.driver.execute_script("arguments[0].click();", js_element)
                print(f"DEBUG (ListaCompras): Clique VIA JAVASCRIPT no botão para '{produto_nome}' realizado com sucesso.")
            except Exception as js_e:
                print(f"DEBUG (ListaCompras): Clique VIA JAVASCRIPT também falhou: {js_e}")
                raise 
        except Exception as e:
            print(f"DEBUG (ListaCompras): Erro inesperado ao tentar clicar no botão para '{produto_nome}': {e}")
            raise  

    def obter_nomes_dos_itens_da_lista(self):
        """Obtém os nomes de todos os produtos exibidos na Lista de Compras."""
        item_elements = self.find_elements(self.LIST_ITEM_NAME)
        return [elem.text for elem in item_elements]

    def clicar_limpar_lista(self):
        """Clica no botão 'Limpar Lista'."""
        self.click(self.LIMPAR_LISTA_BUTTON)

    def clicar_pagina_inicial(self):
        """Clica no botão 'Página Inicial'."""
        self.click(self.PAGINA_INICIAL_BUTTON)