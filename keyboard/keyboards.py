import aiogram.types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup

import settings
from keyboard.buttons import *

# MAIN MENU


def build_main_keyboard(user: aiogram.types.User) -> ReplyKeyboardMarkup:
    """Главное меню в зависимости от роли пользователя"""
    main_menu_adm = ReplyKeyboardMarkup(keyboard=[[upload]], resize_keyboard=True)
    main_menu = ReplyKeyboardMarkup(
        keyboard=[[menu_tests, menu_services, menu_settings]],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    return main_menu_adm if user.id in settings.admins else main_menu


ielts_types = ReplyKeyboardMarkup(
    keyboard=[
        [listening, speaking],
        [reading, writing],
        [menu],
    ],
    resize_keyboard=True,
)

back_keyboard = ReplyKeyboardMarkup(keyboard=[[back]], resize_keyboard=True)

subscribe = InlineKeyboardMarkup(inline_keyboard=[[subscribe_button]])

# TESTS

tests_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [tests_today, answers_today],
        # [back_inline],
        [main_menu],
    ]
)
# SERVICE

services_menu = InlineKeyboardMarkup(
    inline_keyboard=[[speaking_club], [writing_checker], [feed], [main_menu]]
)

writing_checker_menu = InlineKeyboardMarkup(
    inline_keyboard=[[part_1, part_2], [writing_checker_back]]
)

feed_menu = InlineKeyboardMarkup(
    inline_keyboard=[[news], [sites], [podcasts], [feed_back]]
)

feed_back = InlineKeyboardMarkup(inline_keyboard=[[writing_checker_back]])

# SETTINGS

settings_menu = InlineKeyboardMarkup(
    inline_keyboard=[[language, subscription], [main_menu]]
)
language_menu = InlineKeyboardMarkup(inline_keyboard=[[en, ru, uz], [lang_back]])
