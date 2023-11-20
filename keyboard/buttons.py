from aiogram.types import KeyboardButton

# MENU BUTTONS

back = KeyboardButton(text="Back")
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

# USER KEYBOARD

get_test = KeyboardButton(text="Get tests")
