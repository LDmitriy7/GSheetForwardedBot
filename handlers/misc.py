from aiogram import types

import commands
from loader import dp


@dp.message_handler(commands=commands.CHAT_ID)
async def send_chat_id(msg: types.Message):
    await msg.answer(f'ID этого чата: {msg.chat.id}')
