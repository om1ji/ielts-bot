from handlers.common import *
from common.common import bot
from aiogram.types.labeled_price import LabeledPrice

router = Router()


@router.message(Command("start"))
async def echo_start(message: Message):
    db.add_user(message.from_user)
    reply_markup = keyboards.build_main_keyboard(message.from_user)
    await bot.delete_message(message.chat.id, message.message_id)
    await message.answer("Damn hi", reply_markup=reply_markup)


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
