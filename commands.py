from aiogram import types
from aiogram.utils.exceptions import TelegramAPIError
from aiogram_utils.errors import suppress

import config
from loader import dp, log

START = 'start'
CANCEL = 'cancel'
LOGS = 'logs'
CHAT_ID = 'chat_id'

USER_COMMANDS = [
]

ADMIN_COMMANDS = USER_COMMANDS + [
    types.BotCommand(START, 'Старт'),
    types.BotCommand(LOGS, 'Логи'),
    types.BotCommand(CHAT_ID, 'Показать ID чата'),
    types.BotCommand(CANCEL, 'Отменить'),
]
