import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeDriverManager
from utils.data_generator import generate_random_user

# URL base do frontend para testes E2E
FRONTEND_BASE_URL = "https://front.serverest.dev"
# URL base da API para testes de API
API_BASE_URL = "https://serverest.dev"

@pytest.fixture(scope="session")
def base_url_frontend():
    """Fixture que fornece a URL base do frontend."""
    return FRONTEND_BASE_URL

@pytest.fixture(scope="session")
def base_url_api():
    """Fixture que fornece a URL base da API."""
    return API_BASE_URL

@pytest.fixture(scope="function")
def driver():
    """
    Fixture que inicializa e finaliza o WebDriver para cada teste.
    Usa WebDriverManager para baixar e gerenciar o driver do Chrome.
    """

    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080") # Define o tamanho da janela

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window() # Maximiza a janela do navegador
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def new_user_data():
    """
    Fixture que gera dados de um novo usuário aleatório para testes de cadastro.
    """
    return generate_random_user()

@pytest.fixture(scope="session")
def admin_user_credentials():
    """
    Fixture que fornece credenciais de um usuário administrador existente para login.
    Idealmente, estas credenciais viriam de um arquivo de configuração ou variáveis de ambiente.
    Para este exemplo, usaremos dados fictícios.
    """
    return {
        "email": "brunateste@qa.com", 
        "password": "brunateste123"       
    }