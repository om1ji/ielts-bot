import aiogram.types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

import settings
from keyboard import buttons

# MAIN MENU


def build_main_keyboard(user: aiogram.types.User) -> ReplyKeyboardMarkup:
    main_menu_adm = ReplyKeyboardMarkup(
        keyboard=[[buttons.upload]], resize_keyboard=True
    )
    main_menu = ReplyKeyboardMarkup(keyboard=[[buttons.get_test]], resize_keyboard=True)
    return main_menu_adm if user.id in settings.admins else main_menu


ielts_types = ReplyKeyboardMarkup(
    keyboard=[
        [buttons.listening, buttons.speaking],
        [buttons.reading, buttons.writing],
        [buttons.menu],
    ],
    resize_keyboard=True,
)

back_keyboard = ReplyKeyboardMarkup(keyboard=[[buttons.back]], resize_keyboard=True)
