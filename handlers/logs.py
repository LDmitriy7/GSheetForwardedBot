from aiogram import types
from aiogram.utils.exceptions import TelegramAPIError

import commands
import config
from loader import dp


@dp.message_handler(commands=commands.LOGS, user_id=config.admins.ids)
async def logs(msg: types.Message):
    document = types.InputFile(config.log.file, filename='logs.txt')
    try:
        await msg.answer_document(document)
    except TelegramAPIError:
        await msg.answer('Файл пустой')
