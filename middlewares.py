from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

import config
from loader import dp


class AccessChecker(BaseMiddleware):

    @staticmethod
    async def on_pre_process_message(msg: types.Message, *_):
        if msg.from_user.id not in config.ADMINS_IDS:
            raise CancelHandler


def setup():
    dp.setup_middleware(AccessChecker())
