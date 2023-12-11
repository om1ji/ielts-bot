from handlers.common import *
from common.common import bot

from aiogram.types.labeled_price import LabeledPrice
from aiogram.types.callback_query import CallbackQuery

from common import texts
from keyboard.keyboards import subscribe

router = Router()


@router.message(Command("start"))
async def echo_start(message: Message):
    if not db.user_exists(message.from_user):
        await message.answer(
            texts.welcome["text"],
            reply_markup=subscribe,
        )
        db.add_user(message.from_user)
        return

    reply_markup = keyboards.build_main_keyboard(message.from_user)
    await bot.delete_message(message.chat.id, message.message_id)
    await message.answer(texts.main_menu["text"], reply_markup=reply_markup)


@router.message(Command("send_invoice"))
async def send_invoice(message: Message):
    om1ji_price = LabeledPrice(label="Амаль", amount=150000000)
    await bot.send_invoice(
        message.chat.id,
        title="Вечный раб",
        description="Купить Амаля чтобы он делал Телеграм боты пожизненно",
        payload="Payload_Om1ji",
        provider_token="398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065",
        currency="UZS",
        prices=[om1ji_price],
    )


@router.callback_query(F.data == "subscribe")
async def subscribe_user(callback_data: CallbackQuery):
    db.subscribe_user(callback_data.from_user)

    await bot.send_message(
        callback_data.message.chat.id,
        "Subscribed",
        reply_markup=keyboards.build_main_keyboard(callback_data.from_user),
    )
    await callback_data.message.delete()


@router.callback_query(F.data == "main_menu")
async def show_main_menu(callback_query: CallbackQuery):
    await bot.delete_message(
        callback_query.message.chat.id, callback_query.message.message_id
    )
    await bot.send_message(
        callback_query.message.chat.id,
        texts.main_menu["text"],
        reply_markup=keyboards.build_main_keyboard(callback_query.from_user),
    )
