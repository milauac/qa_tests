import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import web_driver as wd


@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--enable-automation")
    chrome_options.add_argument("--disable-extensions")
    srv = Service(ChromeDriverManager().install())
    wd.web_dr = webdriver.Chrome(service=srv, options=chrome_options)

    yield wd.web_dr
    wd.web_dr.close()
    wd.web_dr.quit()


@pytest.fixture(autouse=True)
def open_page(driver):
    driver.get("https://local.studocu.com")
    driver.maximize_window()
    print(f"at the beginning {driver.current_url}")




