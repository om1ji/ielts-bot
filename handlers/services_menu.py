from handlers.common import *
from keyboard import keyboards

from common.common import bot
from common import texts
from aiogram.types.callback_query import CallbackQuery


router = Router()


@router.message(F.text == texts.main_menu["services"])
async def show_services_menu(message: Message):
    message.delete()
    await message.answer(
        texts.services_menu["text"], reply_markup=keyboards.services_menu
    )


@router.callback_query(F.data == "speaking")
async def speaking_club_menu(callback_query: CallbackQuery):
    await bot.send_message(callback_query.message.chat.id, texts.speaking_club["text"])


# WRITING CHECKER
@router.callback_query(F.data == "writing_checker")
async def speaking_club_menu(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        texts.writing_checker_menu["text"],
        reply_markup=keyboards.writing_checker_menu,
    )


@router.callback_query(F.data == "writing_checker_back")
async def back_to_services_menu(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        texts.services_menu["text"], reply_markup=keyboards.services_menu
    )


# TODO: Состояние если в каком то определенном Part то при back на уровень выше, а не в начало
# @router.callback_query(F.data == "writing_checker_back")
# async def back_to_services_menu(callback_query: CallbackQuery):
#     await callback_query.message.edit_text(
#         texts.services_menu["text"], reply_markup=keyboards.services_menu
#     )


# TODO: Состояние waiting ждать либо текст либо callback_data=feed_back
@router.callback_query(F.data == "part_1")
@router.callback_query(F.data == "part_2")
async def wait_for_essay(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        texts.writing_checker_menu["send_text"], reply_markup=keyboards.feed_back
    )


@router.message(F.text == texts.menu_back)
async def back_to_part_choose(message: Message):
    await bot.send_message(
        message.chat.id,
        texts.writing_checker_menu["text"],
        reply_markup=keyboards.writing_checker_menu,
    )


# FEED


# TODO Функционал рассылки
@router.callback_query(F.data == "feed")
async def show_feed_menu(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text=texts.feed_menu["text"], reply_markup=keyboards.feed_menu
    )


@router.callback_query(F.data == "news")
@router.callback_query(F.data == "sites")
@router.callback_query(F.data == "podcasts")
async def feed_menu(callback_query: CallbackQuery):
    await NotImplemented(callback_query)


# BACK
@router.callback_query(F.data == "feed_back")
async def back_to_services_menu(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        texts.services_menu["text"], reply_markup=keyboards.services_menu
    )
