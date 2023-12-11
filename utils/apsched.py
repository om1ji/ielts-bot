from aiogram import Bot
from orm import db
from common.texts import unsubscribed
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta


async def unbsubscribe_user(bot: Bot, user_id: int):
    await bot.send_message(user_id, unsubscribed)
    db.unsubscribe_user(user_id)


def start_saved_jobs(bot: Bot, scheduler: AsyncIOScheduler) -> None:
    plans = db.get_all_subscription_ends()
    if plans is not None:
        for plan in plans:
            scheduler.add_job(
                unbsubscribe_user,
                trigger="date",
                run_date=plan[1],
                kwargs={"bot": bot, "user_id": plan[0]},
            )
    else:
        print("No jobs found :)")
