import web_driver
from POM.cookie_banner import wait_for_cookie_banner


def click_login_from_header():
    web_driver.set_a_b_test_variant('testNewAuthentication')
    wait_for_cookie_banner()
    web_driver.wait_for_presence('loginLinkHeader')
    web_driver.wait_for_visible('loginLinkHeader')
    web_driver.find_element('loginLinkHeader').click()


def fill_in_email():
    web_driver.wait_for_url('login')
    email = 'email-input'
    web_driver.wait_for_presence(email)
    web_driver.wait_for_visible(email)
    web_driver.wait_for_clickable(email)
    web_driver.find_element(email).send_keys("my@study.tst")


def fill_in_password():
    web_driver.wait_for_clickable('password-input')
    web_driver.find_element('password-input').send_keys("milatests")


def click_submit_login_btn():
    web_driver.find_element('submit-login-button').click()
    _verify_logged_in()


def _verify_logged_in():
    web_driver.wait_for_presence('user-menu-button')
    web_driver.wait_for_presence('uploadButton')
