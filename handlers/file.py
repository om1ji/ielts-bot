from handlers.common import *
from handlers.states import UploadTest
from keyboard import buttons, keyboards
from common.common import bot
from aiogram.exceptions import TelegramBadRequest

router = Router()


@router.message(F.text == buttons.cancel.text)
async def cancel(message: Message, state: FSMContext):
    await state.clear()
    reply_markup = keyboards.build_main_keyboard(message.from_user)
    await message.answer("Cancelled", reply_markup=reply_markup)


@router.message(F.text == buttons.upload.text)
async def what_type_of_test(message: Message, state: FSMContext):
    await message.answer("What type of test it is?", reply_markup=keyboards.ielts_types)
    await state.set_state(UploadTest.wait_for_test_type)


@router.message(F.text.in_([buttons.speaking.text, buttons.writing.text]))
async def wait_for_upload(message: Message, state: FSMContext):
    await state.update_data(ielts_type=message.text)
    await message.reply(
        "Send the test",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[buttons.back]], resize_keyboard=True
        ),
    )
    await state.set_state(UploadTest.speaking_listening)


@router.message(F.text.in_([buttons.reading.text, buttons.listening.text]))
async def wait_for_upload(message: Message, state: FSMContext):
    await state.update_data(ielts_type=message.text)
    await message.reply(
        "Send the test",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[buttons.back]], resize_keyboard=True
        ),
    )
    await state.set_state(UploadTest.wait_for_test_upload)


@router.message(F.text == buttons.back.text)
async def return_to_choose(message: Message, state: FSMContext):
    await message.reply("What type of test it is?", reply_markup=keyboards.ielts_types)
    await state.set_state(UploadTest.wait_for_test_type)


@router.message(UploadTest.wait_for_test_type)
@router.message(F.text == buttons.menu.text)
async def return_to_choose(message: Message, state: FSMContext):
    reply_markup = keyboards.build_main_keyboard(message.from_user)
    await message.reply("Main menu", reply_markup=reply_markup)
    await state.clear()


@router.message(UploadTest.wait_for_test_upload)
async def wait_for_upload(message: Message, state: FSMContext):
    if message.document or message.audio:
        file = message.document if message.document is not None else message.audio
        category = await state.get_data()
        if db.insert_file(
            file_id=file.file_id,
            file_ext=file.mime_type,
            category=category["ielts_type"],
            file_name=file.file_name,
        ):
            await message.answer(
                "Now send the answers",
                reply_markup=ReplyKeyboardMarkup(
                    keyboard=[[buttons.back]], resize_keyboard=True
                ),
            )
            await state.set_state(states.UploadTest.wait_for_answers_upload)
            await state.update_data(file_id=file.file_id, file_name=file.file_name)
        else:
            await message.answer(
                f"File with name {file.file_name} already exists. Rename your file"
            )

    else:
        await message.answer(
            "It is not a document. If you want to send a photo, send it uncompressed",
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[[buttons.back]], resize_keyboard=True
            ),
        )


@router.message(UploadTest.speaking_listening)
async def wait_for_upload(message: Message, state: FSMContext):
    if message.document:
        category = await state.get_data()
        db.insert_file(
            file_id=message.document.file_id,
            file_ext=message.document.mime_type,
            category=category["ielts_type"],
        )

        await state.clear()
        await message.reply("Done!", reply_markup=keyboards.ielts_types)

    else:
        await message.answer(
            "It is not a document. If you want to send a photo, send it uncompressed",
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[[buttons.back]], resize_keyboard=True
            ),
        )


@router.message(UploadTest.wait_for_answers_upload)
async def wait_for_answer(message: Message, state: FSMContext):
    if message.document:
        file_id = await state.get_data()
        db.add_answers(
            test_file_id=file_id["file_id"],
            answer_file_id=message.document.file_id,
            test_file_name=file_id["file_name"],
            answer_file_name=message.document.file_name,
        )

        await message.answer("Done!", reply_markup=keyboards.ielts_types)
        await state.set_state(states.UploadTest.wait_for_test_type)

    else:
        await message.answer(
            "It is not a document. If you want to send a photo, send it uncompressed",
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[[buttons.back]], resize_keyboard=True
            ),
        )


# DEBUG
@router.message(Command("file"))
async def echo_start(message: Message):
    file_id = message.text.split(" ")[1]
    try:
        await bot.send_document(message.chat.id, document=file_id)
    except TelegramBadRequest:
        await message.reply("No file with that id :(")


@router.message(Command("answer"))
async def echo_start(message: Message):
    test_file_id = message.text.split(" ")[1]
    answer_file_id = db.get_answers(test_file_id)
    try:
        await bot.send_document(message.chat.id, document=answer_file_id)
    except TelegramBadRequest:
        await message.reply("No file with that id :(")


@router.message(Command("replace_answer"))
async def set_wait_for_test_file_upload(message: Message, state: FSMContext):
    await message.reply(
        "Send the test",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[buttons.back]], resize_keyboard=True
        ),
    )
    await state.set_state(UploadTest.wait_for_test_upload_edit)


@router.message(UploadTest.wait_for_test_upload_edit)
async def wait_for_test_file_upload(message: Message, state: FSMContext):
    if message.document and db.check_for_exist(message.document.file_name):
        await state.set_state(UploadTest.wait_for_answer_upload_edit)
        await state.update_data(test_file_name=message.document.file_name)
        await message.reply(
            "Send the test to replace", reply_markup=keyboards.back_keyboard
        )

    else:
        await message.answer(
            "No test in database or wrong document type",
            reply_markup=keyboards.back_keyboard,
        )


@router.message(UploadTest.wait_for_answer_upload_edit)
async def replace_answer_test(message: Message, state: FSMContext):
    test_file_name = await state.get_data()
    db.replace_answer_file(
        test_file_name=test_file_name["test_file_name"],
        answer_file_id=message.document.file_id,
        answer_file_name=message.document.file_name,
    )
    await state.clear()
    await message.reply(
        "Done!", reply_markup=keyboards.build_main_keyboard(message.from_user)
    )
