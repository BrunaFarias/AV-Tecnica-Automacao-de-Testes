from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegistroPage (BasePage):
    REGISTER_LINK = (By.CSS_SELECTOR, "a[data-testid='cadastrar']")
    NAME_INPUT = (By.ID, "nome")
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[data-testid='cadastrar']")
    ADMIN_CHECKBOX = (By.ID, "administrador") 
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert-danger") 

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.path = "/cadastrarusuarios"

    def navegar_regristro(self):
        """Navega para a página de registro."""
        self.open(self.path)

    def preencher_formulario(self, nome, email, password, admin=False):
        """Preenche o formulário de registro."""
        self.type_text(self.NAME_INPUT, nome)
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)   
        if admin:
            self.click(self.ADMIN_CHECKBOX)
        self.click(self.REGISTER_BUTTON)

    def obter_mensagem_sucesso(self):
        """Obtém a mensagem de sucesso exibida na página de registro."""
        return self.get_text(self.SUCCESS_MESSAGE)
    
    def obter_mensagem_erro(self):
        """Obtém a mensagem de erro exibida na página de registro."""
        return self.get_text(self.ERROR_MESSAGE)