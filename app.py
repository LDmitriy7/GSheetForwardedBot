import asyncio

from aiogram import executor

import handlers
import middlewares
from loader import dp, loop
from utils.poll_sheets import poll_sheets

if __name__ == '__main__':
    loop.create_task(poll_sheets())
    handlers.setup()
    middlewares.setup()
    executor.start_polling(dp)
