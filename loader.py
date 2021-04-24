import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.files import PickleStorage

import config

bot = Bot(config.BOT_TOKEN, parse_mode='html')
loop = asyncio.get_event_loop()
storage = PickleStorage('aiogram_fsm')
dp = Dispatcher(bot, storage=storage, loop=loop)
