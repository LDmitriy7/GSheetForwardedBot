import shelve

from aiogram import types
from aiogram.dispatcher import FSMContext

from config import SHELVE_FILE, CHANNEL_KEY, GROUP_KEY
from loader import dp


@dp.message_handler(text='Изменить канал', state='*')
async def send_keyboard(msg: types.Message, state: FSMContext):
    await state.set_state('change:channel')
    await msg.answer('Введи юзернейм или ID канала')


@dp.message_handler(text='Изменить группу', state='*')
async def send_keyboard(msg: types.Message, state: FSMContext):
    await state.set_state('change:group')
    await msg.answer('Введи юзернейм или ID группы')


@dp.message_handler(state='change:channel')
async def send_keyboard(msg: types.Message, state: FSMContext):
    try:
        channel = int(msg.text)
        await msg.answer(f'Новый ID канала: {channel}')
    except ValueError:
        channel = '@' + msg.text.strip('@')
        await msg.answer(f'Новый юзернейм канала: {channel}')

    with shelve.open(SHELVE_FILE) as sh:
        sh[CHANNEL_KEY] = channel

    await state.finish()


@dp.message_handler(state='change:group')
async def send_keyboard(msg: types.Message, state: FSMContext):
    try:
        group = int(msg.text)
        await msg.answer(f'Новый ID группы: {group}')
    except ValueError:
        group = '@' + msg.text.strip('@')
        await msg.answer(f'Новый юзернейм группы: {group}')

    with shelve.open(SHELVE_FILE) as sh:
        sh[GROUP_KEY] = group

    await state.finish()
