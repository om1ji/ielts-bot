import asyncio
from common.common import *
from utils import apsched
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from handlers import main_handler, file, tests_menu, services_menu, settings_menu

dp.include_routers(
    main_handler.router,
    file.router,
    tests_menu.router,
    services_menu.router,
    settings_menu.router,
)


async def main():
    scheduler = AsyncIOScheduler()
    apsched.start_saved_jobs(bot, scheduler)
    scheduler.start()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
