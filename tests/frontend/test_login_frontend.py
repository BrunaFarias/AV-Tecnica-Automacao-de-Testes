import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestLoginFrontend:
    def login_sucesso(self, driver, base_url_frontend, admin_user_credentials):
        """
        Testa o login com sucesso.
        Pré-condição: O usuário administrador deve existir no sistema.
        """
        login_page = LoginPage(driver, base_url_frontend)
        login_page.navigate_to_login_page()

        # Realiza o login com as credenciais do admin
        login_page.login(admin_user_credentials["email"], admin_user_credentials["password"])

        login_page.wait.until(EC.url_contains("/home"))
        assert "/home" in driver.current_url, "Não foi redirecionado para a página home após o login bem-sucedido."

    def login_falha(self, driver, base_url_frontend):
        """
        Testa o login com credenciais inválidas.
        Espera que uma mensagem de erro seja exibida.
        """
        login_page = LoginPage(driver, base_url_frontend)
        login_page.navigate_to_login_page()

        # Tenta fazer login com credenciais inválidas
        login_page.login("errr@teste.com", "senha_errada")

        # Verifica se a mensagem de erro é exibida
        error_message = login_page.get_error_message()
        assert "Email e/ou senha inválidos" in error_message, "Mensagem de erro de credenciais inválidas não foi exibida ou está incorreta."