from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

def wait_for_element_text_to_be(driver, by_locator, expected_text, timeout=10):
    """
    Espera até que o texto de um elemento seja exatamente o texto esperado.
    """
    try:
        WebDriverWait(driver, timeout).until(
            lambda d: d.find_element(*by_locator).text == expected_text
        )
        return True
    except TimeoutException:
        print(f"Tempo esgotado esperando pelo texto '{expected_text}' no elemento {by_locator}")
        return False