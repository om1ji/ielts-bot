from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from keyboard import buttons

# MAIN MENU

main_menu_adm = ReplyKeyboardMarkup(keyboard=[[buttons.upload]], resize_keyboard=True)
main_menu = ReplyKeyboardMarkup(keyboard=[[buttons.get_test]], resize_keyboard=True)

upload_menu = ReplyKeyboardMarkup(
    keyboard=[
        [buttons.listening, buttons.speaking],
        [buttons.reading, buttons.writing],
        [buttons.back],
    ],
    resize_keyboard=True,
)
