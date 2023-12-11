from handlers.common import *
from keyboard import keyboards

from common import texts
from aiogram.types.callback_query import CallbackQuery


router = Router()


@router.message(F.text == texts.main_menu["settings"])
async def show_settings_menu(message: Message):
    message.delete()
    await message.answer(
        texts.services_menu["text"], reply_markup=keyboards.settings_menu
    )


# LANGUAGE


@router.callback_query(F.data == "language")
async def show_language_menu(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        texts.language_menu["text"], reply_markup=keyboards.language_menu
    )


@router.callback_query(F.data.in_(texts.languages))
async def change_language(callback_query: CallbackQuery):
    db.change_language(callback_query.from_user, callback_query.data)
    await callback_query.answer(texts.language_changed)


@router.callback_query(F.data == "lang_back")
async def back_to_settings_menu(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        texts.settings_menu["text"], reply_markup=keyboards.settings_menu
    )


# SUBSCRIPTION


@router.callback_query(F.data == "subscription")
async def show_subscription_menu(callback_query: CallbackQuery):
    await NotImplemented(callback_query)
