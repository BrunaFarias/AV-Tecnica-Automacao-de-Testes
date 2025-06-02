from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    """
    Página de login da aplicação.
    """
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-testid='entrar']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert-danger")

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.path = "/login"

    def nav_login(self):
        """Navega para a página de login."""
        self.open(self.path)
    
    def login(self, email, password):
        """Realiza o login com email e senha."""
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        """Obtém a mensagem de erro exibida na página de login."""
        return self.get_text(self.ERROR_MESSAGE)