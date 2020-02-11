from page import *

HEADER_TEXT = 'The awesome Q/A tool'
HEADER_QUESTIONS_LIST = 'Created questions'
HOW_TO_CREATE_TIP = 'Just use the form below!'
HEADER_CREATE_QUESTION = 'Create a new question'
SIDEBAR_DEFAULT_INFO = 'Here you can find 1 question. Feel free to create your own questions!'
QUESTION_EXAMPLE = '1st question?'
ANSWER_EXAMPLE = 'answer for question'
QUESTIONS_ANSWER_SET = [('%is it 2nd question', 'answer for 2nd question'),
                        ('Are you here?', 'you are right'),
                        ('Are you here?', 'nope'),
                        ('are you here?', 'hide and sic'),
                        ('9 What is the day today?', 'lucky one'),
                        ('999 ?', 'after 9.'),
                        ('19', 'number in question'),
                        ('- is it the last one?', 'never stop'),
                        ('üben is it german?', 'oeps')]
SORTED_QUESTIONS = ['%is it 2nd question', '- is it the last one?', '19', '9 What is the day today?','999 ?',
                    'Are you here?', 'Are you here?', 'are you here?', 'How to add a question?', 'üben is it german?']
NO_ANSWERS_WARNING = 'No questions yet :-('
CREATE_QUESTION_TOOLTIP = 'Here you can create new questions and their answers.'
EMPTY_INPUT_TOOLTIP = 'Please fill out this field.'


def test_add_question():
    default = get_number_of_questions()

    # below check can be uncommented after fixing only space case
    # create_question(" ", " ")
    # assert get_number_of_questions() == default, \
    #     "Space shouldn't be count as provided answer/question"

    create_question(QUESTION_EXAMPLE, ANSWER_EXAMPLE)
    assert get_number_of_questions() == (default + 1), \
        f"Here have to be {get_number_of_questions()} questions in a list"

    assert not are_answers_displayed(), \
        "Answers aren't expected to be displayed"

    click_on_last_question()
    assert is_last_answer_displayed(), \
        "Answer should be visible after click on question"


def test_add_question_with_empty_fields():
    default = get_number_of_questions()
    create_question("", ANSWER_EXAMPLE)
    assert get_number_of_questions() == default, \
        "Shouldn't be possible to create empty question, only with answer"

    create_question(QUESTION_EXAMPLE, "")
    assert get_number_of_questions() == default, \
        "Shouldn't be possible to create question without answer"

    create_question("", "")
    assert get_number_of_questions() == default, \
        "Shouldn't be possible to create question without question itself and answer"


def test_remove_all_questions():
    click_remove_questions_btn()

    assert get_number_of_questions() == 0

    for item in QUESTIONS_ANSWER_SET:
        create_question(item[0], item[1])
    click_remove_questions_btn()

    assert get_number_of_questions() == 0


def test_sorting_and_answers_displaying():
    for item in QUESTIONS_ANSWER_SET:
        create_question(item[0], item[1])

    click_sort_questions_btn()
    assert get_list_of_questions() == SORTED_QUESTIONS, \
        "Sorted list of question isn't as expected"

    assert not are_answers_displayed(), \
        "Sorting shouldn't open answers"

    create_question(QUESTION_EXAMPLE, ANSWER_EXAMPLE)
    assert QUESTION_EXAMPLE in get_list_of_questions(), \
        "Just added question can't be found in list"

    click_on_last_question()
    assert get_last_answer_text() == ANSWER_EXAMPLE, \
        f"Last question should have answer {ANSWER_EXAMPLE}"

    click_on_first_question()
    assert get_number_of_opened_answers() == 2, \
        "Here should be 2 opened answers"

    click_sort_questions_btn()
    assert not get_last_answer_text() == ANSWER_EXAMPLE, \
        "Last question/answer should be changed after sorting"
    assert get_number_of_opened_answers() == 2, \
        "Here should be 2 opened answers as their state isn't changed after sorting"


def test_sidebar():
    assert get_sidebar_text() == SIDEBAR_DEFAULT_INFO, \
        "Default sidebar text doesn't match expected"

    create_question(QUESTION_EXAMPLE, ANSWER_EXAMPLE)
    assert "2 questions" in get_sidebar_text(), \
        "Here have to be '2 questions' info in sidebar after adding 1 question"

    click_remove_questions_btn()
    assert "no questions" in get_sidebar_text(), \
        "Here have to be 'no questions' info in sidebar after adding 1 question"


def test_titles_and_tips():
    click_on_last_question()
    get_last_answer_text()
    assert get_last_answer_text() == HOW_TO_CREATE_TIP, \
        f"Default question - tip ho to create questions should be {HOW_TO_CREATE_TIP} "
    assert get_header_text() == HEADER_TEXT, \
        f"Header text isn't as expected {HEADER_TEXT} "

    assert get_header_of_questions_list() == HEADER_QUESTIONS_LIST, \
        f"Question list header isn't as expected {HEADER_QUESTIONS_LIST}"

    assert get_header_create_question() == HEADER_CREATE_QUESTION, \
        f"Create questions header text isn't as expected {HEADER_CREATE_QUESTION} "


def test_warnings_and_tooltips():
    click_remove_questions_btn()
    assert get_no_answers_warning() == NO_ANSWERS_WARNING, \
        "Wrong warning after removing all questions"

    assert get_tooltip_text_for_create_question() == CREATE_QUESTION_TOOLTIP, \
        "Wrong tooltip for header 'Create a new question'"

    assert get_answer_tooltip() == EMPTY_INPUT_TOOLTIP

    assert get_question_tooltip() == EMPTY_INPUT_TOOLTIP
