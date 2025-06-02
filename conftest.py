import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 

# Importa os clientes de API
from api_clients.usuarios_api_cliente import UsuariosApiCliente
from api_clients.autenticacao_api_cliente import AutenticacaoApiCliente
from api_clients.produtos_api_cliente import ProdutosApiCliente

# Importa o gerador de dados
from utils.data_generator import generate_random_user, generate_random_product

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
    options.add_argument("--window-size=1920,1080") 

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.maximize_window() 
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
        "email": "admin2@qa.com", 
        "password": "admin123"       
    }

# --- Fixtures de API ---
@pytest.fixture(scope="session")
def users_api_client(base_url_api):
    """Fixture que fornece um cliente para a API de usuários."""
    return UsuariosApiCliente(base_url_api) 

@pytest.fixture(scope="session")
def auth_api_client(base_url_api):
    """Fixture que fornece um cliente para a API de autenticação."""
    return AutenticacaoApiCliente(base_url_api) 

@pytest.fixture(scope="session")
def products_api_client(base_url_api):
    """Fixture que fornece um cliente para a API de produtos."""
    return ProdutosApiCliente(base_url_api) 

@pytest.fixture(scope="function")
def authenticated_admin_token(auth_api_client, admin_user_credentials):
    """
    Fixture que realiza o login de um administrador e retorna o token de autenticação.
    """
    token = auth_api_client.login(admin_user_credentials["email"], admin_user_credentials["password"])
    assert token is not None, "Falha ao obter token de autenticação para o administrador."
    return token