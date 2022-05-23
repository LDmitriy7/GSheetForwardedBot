from aiogram import types
from aiogram.dispatcher import FSMContext

import commands
import texts
from loader import dp


@dp.message_handler(commands=commands.CANCEL, state='*')
async def cancel(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.answer(texts.cancelled)
