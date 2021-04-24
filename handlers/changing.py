import shelve

from aiogram import types
from aiogram.dispatcher import FSMContext

from config import SHELVE_FILE, SHEET_ID_KEY, PRIVATE_GROUP_KEY
from loader import dp


@dp.message_handler(text='Изменить таблицу', state='*')
async def send_keyboard(msg: types.Message, state: FSMContext):
    await state.set_state('change:table')
    await msg.answer('Введи ID таблицы (из ссылки)')


@dp.message_handler(text='Изменить группу', state='*')
async def send_keyboard(msg: types.Message, state: FSMContext):
    await state.set_state('change:group')
    await msg.answer('Введи юзернейм или ID группы')


@dp.message_handler(state='change:table')
async def send_keyboard(msg: types.Message, state: FSMContext):
    with shelve.open(SHELVE_FILE) as sh:
        sh[SHEET_ID_KEY] = msg.text

    await msg.answer(f'Новая таблица: {msg.text}')
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
        sh[PRIVATE_GROUP_KEY] = group

    await state.finish()
