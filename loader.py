import logging

import mongoengine as me
from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram.contrib.fsm_storage.mongo import MongoStorage
from aiogram_utils.task_manager import TaskManager

import config

me.connect(
    db=config.db.name,
    host=config.db.host,
)

storage = MongoStorage(
    db_name=config.db.name,
    host=config.db.host,
)

bot = Bot(config.bot.token, parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)
dp = Dispatcher(bot, storage=storage)

logging.basicConfig(
    level=config.log.level,
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(config.log.file, 'w')
    ]
)

log = logging.getLogger()

tm = TaskManager()
