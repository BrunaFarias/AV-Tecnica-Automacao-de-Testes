import pytest
from pages.registro_page import RegistroPage 
from pages.login_page import LoginPage
from utils.data_generator import generate_random_user
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestRegistroFrontend:
    """
    Conjunto de testes para o fluxo de cadastro de usuário no frontend.
    """

    def test_cadastro_usuario_sucesso(self, driver, base_url_frontend, new_user_data):
        """
        Testa o cadastro bem-sucedido de um novo usuário.
        Após o cadastro, tenta fazer login com as novas credenciais para validar.
        """
        registro_page = RegistroPage(driver, base_url_frontend)
        login_page = LoginPage(driver, base_url_frontend)

        registro_page.navegar_regristro()

        # Realiza o cadastro do novo usuário
        registro_page.preencher_formulario( 
            new_user_data["nome"],
            new_user_data["email"],
            new_user_data["senha"]
        )

        # Verifica se a mensagem de sucesso é exibida
        success_message = registro_page.obter_mensagem_sucesso() 
        assert "Cadastro realizado com sucesso!" in success_message, "Mensagem de sucesso de cadastro não foi exibida ou está incorreta."

        # Tenta fazer login com o usuário recém-cadastrado para validar
        login_page.nav_login() 
        login_page.login(new_user_data["email"], new_user_data["senha"])

        # Verifica se o login foi bem-sucedido
        login_page.wait.until(EC.url_contains("/home"))
        assert "/home" in driver.current_url, "Não foi possível fazer login com o usuário recém-cadastrado."

    def test_cadastro_email_existente(self, driver, base_url_frontend, admin_user_credentials): 
        """
        Testa o cadastro de um usuário com um email já existente.
        Espera que uma mensagem de erro seja exibida.
        """
        registro_page = RegistroPage(driver, base_url_frontend) 
        registro_page.navegar_regristro()

        # Tenta cadastrar com um email já existente (usando o email do admin para exemplo)
        registro_page.preencher_formulario( 
            "Usuário Existente",
            admin_user_credentials["email"],
            "senha123"
        )

        # Verifica se a mensagem de erro é exibida
        # Assumindo que a mensagem de erro é exibida com o localizador definido em RegistroPage
        error_message = registro_page.obter_mensagem_erro() 
        assert "Este email já está sendo usado" in error_message, "Mensagem de erro para email existente não foi exibida ou está incorreta."