from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

web_dr = None


def find_element(locator: str) -> WebElement:
    return web_dr.find_element_by_css_selector(locator)


def find_elements(locator: str) -> [WebElement]:
    return web_dr.find_elements_by_css_selector(locator)


def wait_for_visible(element: WebElement):
    try:
        WebDriverWait(web_dr, 4).until(EC.visibility_of(element))
    except TimeoutException:
        print(f"Element {element} isn't visible")


def wait_for_clickable(locator):
    WebDriverWait(web_dr, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR,locator)))


def move_to_element(locator: str):
    ActionChains(web_dr).move_to_element(find_element(locator)).perform()
