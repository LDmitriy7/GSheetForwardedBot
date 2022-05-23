from aiogram.utils import exceptions

from loader import dp


@dp.errors_handler(exception=exceptions.BotBlocked)
@dp.errors_handler(exception=exceptions.MessageNotModified)
async def ignore(*_):
    return True
