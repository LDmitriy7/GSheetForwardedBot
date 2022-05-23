from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

import config


class AccessChecker(BaseMiddleware):

    @staticmethod
    async def on_pre_process_message(msg: types.Message, *_):
        if msg.from_user.id not in config.admins.ids:
            raise CancelHandler
