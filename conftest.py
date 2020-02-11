import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import web_driver as wd


@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--enable-automation")
    chrome_options.add_argument("--disable-extensions")
    wd.web_dr = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    yield wd.web_dr
    wd.web_dr.close()
    wd.web_dr.quit()


@pytest.fixture(autouse=True)
def open_page(driver):
    driver.get("http://localhost:8080")
    driver.maximize_window()



