from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

web_dr = None


def set_a_b_test_variant(a_b_test_name, variant='Control'):
    print(f"here is the start {web_dr.current_url} of our journey")
    a_b_test_extension = "?" + a_b_test_name + "=" + variant
    new_url = web_dr.current_url + a_b_test_extension
    print('This is where we are going to go ' + new_url)
    web_dr.get(new_url)


def find_element(locator: str) -> WebElement:
    return web_dr.find_element(By.XPATH, '//*[@data-test-selector="' + locator + '"]')


def find_element_with_xpath_locator(locator: str) -> WebElement:
    return web_dr.find_element(By.XPATH, locator)


def find_elements(locator: str) -> [WebElement]:
    return web_dr.find_elements_by_css_selector(locator)


def wait_for_visible(locator: str):
    WebDriverWait(web_dr, 14).until(EC.visibility_of_element_located((By.XPATH, '//*[@data-test-selector="' + locator + '"]')))


def wait_for_clickable(locator):
    WebDriverWait(web_dr, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@data-test-selector="' + locator + '"]')))


def wait_for_presence(locator):
    print("We are looking for:")
    print('//*[@data-test-selector=" ' + locator + '"]')
    WebDriverWait(web_dr, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@data-test-selector="' + locator + '"]')))


def select_option(locator, name):
    Select(find_element(locator)).select_by_visible_text(name)


# def wait_for_displayed(el: WebElement):
#     el.is_displayed()

def open_url(url: str):
    web_dr.get(url)


def wait_for_url(part_of_url: str):
    WebDriverWait(web_dr, 10).until(EC.url_contains(part_of_url))


def switch_to_window():
    web_dr.switch_to.window(web_dr.current_window_handle)


def js_execute(command, element):
    web_dr.execute_script(command, element)


def move_to_element(locator: str):
    ActionChains(web_dr).move_to_element(find_element(locator)).perform()
