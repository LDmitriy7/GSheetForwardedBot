from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.files import PickleStorage

import config

bot = Bot(config.BOT_TOKEN)
storage = PickleStorage('aiogram_fsm')
dp = Dispatcher(bot, storage=storage)