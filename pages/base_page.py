from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    """
    Classe base para todas as Page Objects.
    Contém métodos comuns para interações com elementos.
    """
    def __init__(self, driver: WebDriver, base_url: str):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 20)

    def open(self, path=""):
        """Abre uma URL específica."""
        url = f"{self.base_url}{path}"
        self.driver.get(url)

    def find_element(self, by_locator):
        """Encontra um elemento usando um localizador."""
        return self.wait.until(EC.presence_of_element_located(by_locator))

    def find_elements(self, by_locator):
        """Encontra múltiplos elementos usando um localizador."""
        return self.wait.until(EC.presence_of_all_elements_located(by_locator))

    def click(self, by_locator):
        """Clica em um elemento após ele ser clicável."""
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    def type_text(self, by_locator, text):
        """Digita texto em um campo após ele ser visível."""
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        element.clear() # Limpa o campo antes de digitar
        element.send_keys(text)

    def get_text(self, by_locator):
        """Obtém o texto de um elemento."""
        return self.wait.until(EC.presence_of_element_located(by_locator)).text

    def is_element_displayed(self, by_locator):
        """Verifica se um elemento está visível na página."""
        try:
            return self.find_element(by_locator).is_displayed()
        except:
            return False

    def wait_for_url_contains(self, path):
        """Espera até que a URL atual contenha o caminho especificado."""
        self.wait.until(EC.url_contains(path))

    def wait_for_element_to_disappear(self, by_locator):
        """Espera até que um elemento não esteja mais presente no DOM."""
        self.wait.until(EC.invisibility_of_element_located(by_locator))

    def scroll_to_element(self, by_locator):
        """Rola a página até que o elemento esteja visível."""
        element = self.find_element(by_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)