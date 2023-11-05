from handlers.common import *

router = Router()


@router.message(Command("start"))
async def echo_message(message: Message):
    db.add_user(message.from_user)

    reply_markup = (
        keyboards.main_menu_adm
        if db.is_admin(message.from_user)
        else keyboards.main_menu
    )

    await message.reply("Damn hi", reply_markup=reply_markup)


@router.message(F.text == buttons.back.text)
async def move_to_main_menu(message: Message):
    await message.reply("Main menu", reply_markup=keyboards.main_menu)


@router.message(F.text == buttons.upload.text)
async def move_to_main_menu(message: Message):
    await message.reply("Select test type", reply_markup=keyboards.upload_menu)
