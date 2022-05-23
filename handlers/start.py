from aiogram import types
from aiogram.dispatcher import FSMContext

import api
import commands
from loader import dp

change_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
change_keyboard.add('Изменить таблицу', 'Изменить группу')


@dp.message_handler(commands=commands.START, state='*')
async def send_keyboard(msg: types.Message, state: FSMContext):
    await state.finish()

    config = api.config.get()

    texts = [
        'Приветствую!',
        f'<b>Заданная таблица</b>: {config.sheet_id}',
        f'<b>Заданная группа</b>: {config.group_to_forward_id}',
    ]

    await msg.answer('\n'.join(texts), reply_markup=change_keyboard)

    await dp.bot.set_my_commands(
        commands=commands.ADMIN_COMMANDS,
        scope=types.BotCommandScopeChat(msg.chat.id),
    )
