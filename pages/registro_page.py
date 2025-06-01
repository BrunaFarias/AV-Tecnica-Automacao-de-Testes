from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    REGISTER_LINK = (By.CSS_SELECTOR, "a[data-test='cadastrar']")
    NAME_INPUT = (By.ID, "nome")
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "senha")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[data-test='cadastrar']")
    ADMIN_CHECKBOX = (By.ID, "administrador") 
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.path = "/cadastrar"

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