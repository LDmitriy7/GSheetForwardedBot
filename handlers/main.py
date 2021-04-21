import shelve

from aiogram import types
from aiogram.dispatcher import FSMContext

import config
from config import SHELVE_FILE, CHANNEL_KEY, GROUP_KEY
from loader import dp

change_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
change_keyboard.add('Изменить канал', 'Изменить группу')


@dp.message_handler(commands='start', state='*')
async def send_keyboard(msg: types.Message, state: FSMContext):
    await state.finish()

    with shelve.open(SHELVE_FILE) as sh:
        channel = sh.get(CHANNEL_KEY, config.CHANNEL)
        group = sh.get(GROUP_KEY, config.GROUP)
        texts = ['Приветствую!', f'Заданный канал: {channel}', f'Заданная группа: {group}']

    await msg.answer('\n'.join(texts), reply_markup=change_keyboard)


@dp.channel_post_handler()
async def forward_to_group(msg: types.Message):
    with shelve.open(SHELVE_FILE) as sh:
        channel = sh.get(CHANNEL_KEY, config.CHANNEL)
        group = sh.get(GROUP_KEY, config.GROUP)

    if channel == msg.chat.id or isinstance(channel, str) and channel.strip('@') == msg.chat.username:
        await msg.forward(group)
