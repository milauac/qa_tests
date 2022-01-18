import web_driver

cookie_selector = 'the-cookie-banner'


def wait_for_cookie_banner():
    web_driver.wait_for_presence(cookie_selector)
    web_driver.wait_for_visible(cookie_selector)
