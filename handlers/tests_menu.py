from handlers.common import *
from keyboard import keyboards

from common.common import bot
from common import texts
from aiogram.types.callback_query import CallbackQuery


router = Router()


@router.message(F.text == texts.main_menu["tests"])
async def show_tests_menu(message: Message):
    message.delete()
    await bot.send_message(
        message.chat.id,
        texts.tests_menu["text"],
        reply_markup=keyboards.tests_menu,
    )


@router.callback_query(F.data == "tests_today")
@router.callback_query(F.data == "answers_today")
async def send_files(callback_query: CallbackQuery):
    if not db.user_is_subscribed(callback_query.from_user):
        await bot.send_message(
            callback_query.from_user.id,
            texts.not_subscribed,
            reply_markup=keyboards.subscribe,
        )
        return
    await NotImplemented(callback_query)
