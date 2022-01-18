from selenium.common.exceptions import TimeoutException
from POM.cookie_banner import wait_for_cookie_banner
import web_driver
import time


def open_organic_uploader():
    web_driver.open_url('https://local.studocu.com/en-gb/document/upload')
    web_driver.wait_for_presence('documents-drop-area')
    wait_for_cookie_banner()


def upload_and_submit_document():
    _upload_document()
    _submit_uploaded_document()


def fill_in_document_details(category, year):
    _select_university_in_uploader()
    _select_course_in_uploader()
    _select_category_in_uploader_details(category)
    _select_academic_year(year)
    _select_entire_course_checkbox()
    _fill_in_description()
    _make_long_document_title()


def _upload_document():
    file_input_selector = '//input[@type="file"]'
    web_driver.js_execute('arguments[0].style = ""; '
                          'arguments[0].style.display = "block";'
                          ' arguments[0].style.visibility="visible";',
                          web_driver.find_element_with_xpath_locator(file_input_selector))
    web_driver.find_element_with_xpath_locator(file_input_selector).send_keys("/home/mila/Documents/Skills_Lab.pdf")
    web_driver.wait_for_presence('uploaded-document-name')
    web_driver.wait_for_visible('uploaded-document-name')


def _submit_uploaded_document():
    submit_document_button = 'submit-uploads-button'
    web_driver.js_execute("arguments[0].scrollIntoView();", web_driver.find_element(submit_document_button))
    web_driver.wait_for_clickable(submit_document_button)
    web_driver.find_element(submit_document_button).click()

    try:
        web_driver.wait_for_presence('upload-more-modal')
        print("Double reward modal is displayed during uploading")
        web_driver.wait_for_clickable('dismiss-upload-more-modal')
        web_driver.find_element('dismiss-upload-more-modal').click()
    except TimeoutException:
        print("No double reward modal this time")

    web_driver.wait_for_url('details')
    web_driver.wait_for_presence('upload-step-2')


def _select_university_in_uploader():
    time.sleep(1)
    web_driver.find_element('institution-input').send_keys("Universiteit Leiden")
    time.sleep(1)
    web_driver.find_element('institution-input').click()
    web_driver.wait_for_visible('uploader-institution-autocomplete-results')
    web_driver.wait_for_clickable('uploader-institution-autocomplete-result-0')
    web_driver.find_element('uploader-institution-autocomplete-result-0').click()
    web_driver.wait_for_visible('institution-picker-selected-institution')


def _select_course_in_uploader():
    web_driver.find_element('uploader-course-input').send_keys("Chemische Biotechnologie")
    web_driver.find_element('uploader-course-input').click()
    web_driver.wait_for_visible('uploader-course-autocomplete-result')
    web_driver.wait_for_clickable('uploader-course-autocomplete-result-0')
    web_driver.find_element('uploader-course-autocomplete-result-0').click()
    web_driver.wait_for_visible('course-picker-edit-button')


def _select_category_in_uploader_details(category):
    web_driver.select_option('category-select-dropdown', category)


def _select_academic_year(year):
    web_driver.select_option('academic-year-select', year)


def _select_entire_course_checkbox():
    web_driver.find_element('summaryContent-entireCourse-checkbox').click()


def _fill_in_description():
    description = 'Description is the fiction-writing mode for transmitting a mental image of the particulars of a story.'
    web_driver.find_element('upload-document-description').send_keys(description)


def _make_long_document_title():
    web_driver.wait_for_visible('upload-document-title')
    web_driver.find_element('upload-document-title').send_keys("Text messaging, or texting, is the act of composing")


def submit_documents_details():
    web_driver.js_execute("arguments[0].scrollIntoView();", web_driver.find_element('submit-documents'))
    web_driver.find_element('submit-documents').click()
