import asyncio
from aiogram.types import BotCommand, BotCommandScopeDefault
from loguru import logger
from bot import bot, dp
from config import *
from db.middleware.middleware import *



async def main():
    print("запустилось приложуха")
    # scheduler.add_job(send_time_msg, 'interval', seconds=10)
    # scheduler.start()

    dp.update.middleware(DBMiddlewareWithComm())
    dp.update.middleware(DBMiddlewareWithoutComm())
    # dp.include_router(quiz_router)
    # dp.include_router(admin_router)
    # dp.include_router(user_router)

    # dp.startup.register(start_bot)
    # dp.shutdown.register(stop_bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())