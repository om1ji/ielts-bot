from aiogram import Dispatcher, Bot
import asyncio
from settings import bot_token
from handlers import main_handler, file, ielts

bot = Bot(bot_token)
dp = Dispatcher()
dp.include_routers(main_handler.router, file.router, ielts.router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
    print("Bot started")
