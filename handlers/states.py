from aiogram.fsm.state import StatesGroup, State


class UploadTest(StatesGroup):
    wait_for_test_type = State()
    wait_for_test_upload = State()
    wait_for_test_upload_edit = State()
    wait_for_answer_upload_edit = State()

    wait_for_answers_upload = State()
    speaking_listening = State()
