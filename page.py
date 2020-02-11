from locators import *
import web_driver


def get_header_text() -> str:
    return web_driver.find_element(HEADER_TEXT).text


def get_header_of_questions_list():
    return web_driver.find_element(QUESTION_LIST_HEADER).text


def get_number_of_questions() -> int:
    return len(web_driver.find_elements(QUESTION))


def get_list_of_questions() -> [str]:
    return [element.text for element in web_driver.find_elements(QUESTION)]


def click_on_first_question():
    web_driver.find_element(QUESTION).click()


def click_on_last_question():
    number_of_questions = get_number_of_questions()
    web_driver.find_elements(QUESTION)[number_of_questions-1].click()


def get_number_of_answers() -> int:
    return len(web_driver.find_elements(ANSWER))


def get_number_of_opened_answers() -> int:
    return len(web_driver.find_elements(ANSWER)) - len(web_driver.find_elements(HIDDEN_ANSWER))


def get_last_answer_text() -> str:
    number_of_answers = get_number_of_answers()
    return web_driver.find_elements(ANSWER)[number_of_answers-1].text


def are_answers_displayed() -> bool:
    if len(web_driver.find_elements(ANSWER)) == len(web_driver.find_elements(HIDDEN_ANSWER))\
            and len(web_driver.find_elements(ANSWER)) > 0:
        return False
    else:
        print("Some answers are opened")
        return True


def is_last_answer_displayed() -> bool:
    number_of_questions = len(web_driver.find_elements(QUESTION))
    last_answer = web_driver.find_elements(ANSWER)[number_of_questions-1]
    return False if last_answer.size.get("height") == 0 and last_answer.size.get("width") == 0\
        else True


def click_sort_questions_btn():
    web_driver.find_element(SORT_BTN).click()


def click_remove_questions_btn():
    web_driver.find_element(REMOVE_BTN).click()


def get_no_answers_warning() -> str:
    return web_driver.find_element(WARNING).text


def get_header_create_question():
    return web_driver.find_element(CREATE_QUESTION_HEADER).text


def get_tooltip_text_for_create_question() -> str:
    web_driver.move_to_element(CREATE_QUESTION_SECTION_TITLE)
    web_driver.wait_for_visible(web_driver.find_element(TOOLTIP_NEW_QUESTION))
    return web_driver.find_element(TOOLTIP_NEW_QUESTION).text


def create_question(question_text: str, answer_text: str):
    _type_question(question_text)
    _type_answer(answer_text)
    _click_create_question_btn()


def get_answer_tooltip() -> str:
    return web_driver.find_element(TOOLTIP_EMPTY_ANSWER).get_attribute("validationMessage")


def get_question_tooltip() -> str:
    return web_driver.find_element(TOOLTIP_EMPTY_QUESTION).get_attribute("validationMessage")


def get_sidebar_text() -> str:
    return web_driver.find_element(SIDEBAR_TEXT).text.replace('"', '')


def _type_question(question_text: str):
    web_driver.find_element(QUESTION_INPUT).click()
    web_driver.find_element(QUESTION_INPUT).clear()
    web_driver.find_element(QUESTION_INPUT).send_keys(question_text)


def _type_answer(answer_text: str):
    web_driver.find_element(ANSWER_INPUT).click()
    web_driver.find_element(ANSWER_INPUT).clear()
    web_driver.find_element(ANSWER_INPUT).send_keys(answer_text)


def _click_create_question_btn():
    web_driver.move_to_element(CREATE_QUESTION_BTN)
    web_driver.wait_for_clickable(CREATE_QUESTION_BTN)
    web_driver.find_element(CREATE_QUESTION_BTN).click()

