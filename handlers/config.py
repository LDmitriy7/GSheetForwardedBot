from aiogram import types
from aiogram.dispatcher import FSMContext

import api
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
    config = api.config.get()
    config.sheet_id = msg.text
    config.save()

    await msg.answer(f'Новая таблица: {config.sheet_id}')
    await state.finish()


@dp.message_handler(state='change:group')
async def send_keyboard(msg: types.Message, state: FSMContext):
    config = api.config.get()
    config.group_to_forward_id = msg.text
    config.save()

    await msg.answer(f'Новый ID группы: {config.group_to_forward_id}')
    await state.finish()
