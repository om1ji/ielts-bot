import asyncio
from common.common import *
from handlers import main_handler, file, ielts

dp.include_routers(main_handler.router, file.router, ielts.router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
    print("Bot started")
