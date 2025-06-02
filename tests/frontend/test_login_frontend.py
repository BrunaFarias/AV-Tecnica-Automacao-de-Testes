import pytest
from pages.login_page import LoginPage
from pages.registro_page import RegistroPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestLoginFrontend:
    def test_cadastro_e_login_sucesso(self, driver, base_url_frontend, new_user_data):
        """
        Testa o cadastro e login com sucesso.
        Pré-condição: O usuário administrador deve existir no sistema.
        """
        login_page = LoginPage(driver, base_url_frontend)
        registro_page = RegistroPage(driver, base_url_frontend)

        # 1. Navega para a página de registro
        registro_page.navegar_regristro()
        registro_page.preencher_formulario(
            new_user_data["nome"],
            new_user_data["email"],
            new_user_data["senha"]
        )
        registro_page.wait.until(EC.url_contains("/login"))
        success_message = login_page.get_error_message()
        assert "Cadastro realizado com sucesso!" in success_message, "Mensagem de sucesso de cadastro não foi exibida ou está incorreta."

        login_page.login(new_user_data["email"], new_user_data["senha"])

        login_page.wait.until(EC.url_contains("/home"))
        assert "/home" in driver.current_url, "Não foi redirecionado para a página home após o login bem-sucedido."
 
    def test_login_falha(self, driver, base_url_frontend):
        """
        Testa o login com credenciais inválidas.
        Espera que uma mensagem de erro seja exibida.
        """
        login_page = LoginPage(driver, base_url_frontend)
        login_page.nav_login()

        login_page.login("email_invalido@teste.com", "senha_errada")

        error_message = login_page.get_error_message()
        assert "Email e/ou senha inválidos" in error_message, "Mensagem de erro de credenciais inválidas não foi exibida ou está incorreta."