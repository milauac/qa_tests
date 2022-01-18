from POM.login import *
from POM.organic_uploader import *


def test_login():
    click_login_from_header()
    fill_in_email()
    fill_in_password()
    click_submit_login_btn()


def test_organic_uploader():
    open_organic_uploader()
    upload_and_submit_document()
    fill_in_document_details('Summaries', '2020/2021')
    submit_documents_details()
