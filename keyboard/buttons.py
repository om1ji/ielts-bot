from aiogram.types import KeyboardButton, InlineKeyboardButton
from common import texts

# MENU BUTTONS

back = KeyboardButton(text=texts.menu_back)
back_inline = InlineKeyboardButton(text=texts.menu_back, callback_data="back")
menu = KeyboardButton(text="Main menu")
cancel = KeyboardButton(text="Cancel")
upload = KeyboardButton(text="Upload")
delete = KeyboardButton(text="Delete")

# IELTS TYPE

reading = KeyboardButton(text="Reading")
speaking = KeyboardButton(text="Speaking")
listening = KeyboardButton(text="Listening")
writing = KeyboardButton(text="Writing")

ielts_types = [reading.text, speaking.text, listening.text, writing.text]

# IELTS LEVEL

a1 = KeyboardButton(text="A1")
a2 = KeyboardButton(text="A2")
b1 = KeyboardButton(text="B1")
b2 = KeyboardButton(text="B2")
c1 = KeyboardButton(text="C1")
c2 = KeyboardButton(text="C2")

# SUBSCRIBE

subscribe_button = InlineKeyboardButton(
    text=texts.pay_button, callback_data="subscribe"
)

# MAIN MENU

menu_tests = KeyboardButton(text=texts.main_menu["tests"])
menu_services = KeyboardButton(text=texts.main_menu["services"])
menu_settings = KeyboardButton(text=texts.main_menu["settings"])

main_menu = InlineKeyboardButton(
    text=texts.main_menu["text"], callback_data="main_menu"
)

# TESTS MENU

answers_today = InlineKeyboardButton(
    text=texts.tests_menu["answers"], callback_data="answers_today"
)
tests_today = InlineKeyboardButton(
    text=texts.tests_menu["tests"], callback_data="tests_today"
)

# SERVICES MENU

speaking_club = InlineKeyboardButton(
    text=texts.services_menu["speaking_club"], callback_data="speaking"
)
writing_checker = InlineKeyboardButton(
    text=texts.services_menu["writing_checker"], callback_data="writing_checker"
)
feed = InlineKeyboardButton(text=texts.services_menu["feed"], callback_data="feed")


# SERVICES WRITING CHECKER

part_1 = InlineKeyboardButton(
    text=texts.writing_checker_menu["part_1"], callback_data="part_1"
)

part_2 = InlineKeyboardButton(
    text=texts.writing_checker_menu["part_2"], callback_data="part_2"
)

writing_checker_back = InlineKeyboardButton(
    text=texts.menu_back, callback_data="writing_checker_back"
)


# SERVICES FEED

news = InlineKeyboardButton(text=texts.feed_menu["news"], callback_data="news")
sites = InlineKeyboardButton(text=texts.feed_menu["sites"], callback_data="sites")
podcasts = InlineKeyboardButton(
    text=texts.feed_menu["podcasts"], callback_data="podcasts"
)
feed_back = InlineKeyboardButton(text=texts.menu_back, callback_data="feed_back")

# SETTINGS MENU

language = InlineKeyboardButton(
    text=texts.settings_menu["language"], callback_data="language"
)
subscription = InlineKeyboardButton(
    text=texts.settings_menu["subscription"], callback_data="subscription"
)

# SETTINGS LANGUAGE

ru = InlineKeyboardButton(text=texts.language_menu["ru"], callback_data="ru")
en = InlineKeyboardButton(text=texts.language_menu["en"], callback_data="en")
uz = InlineKeyboardButton(text=texts.language_menu["uz"], callback_data="uz")
lang_back = InlineKeyboardButton(text=texts.menu_back, callback_data="lang_back")

# SETTINGS SUBSCRIPTION
