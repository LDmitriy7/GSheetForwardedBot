import shelve

from aiogram import types
from aiogram.dispatcher import FSMContext

from config import SHELVE_FILE, SHEET_ID_KEY, PRIVATE_GROUP, PRIVATE_GROUP_KEY, SHEET_ID
from loader import dp
from utils.poll_sheets import SERVICE_ACCOUNT_EMAIL

change_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
change_keyboard.add('Изменить таблицу', 'Изменить группу')


@dp.message_handler(commands='start', state='*')
async def send_keyboard(msg: types.Message, state: FSMContext):
    await state.finish()

    with shelve.open(SHELVE_FILE) as sh:
        sheet_id = sh.get(SHEET_ID_KEY, SHEET_ID)
        private_group = sh.get(PRIVATE_GROUP_KEY, PRIVATE_GROUP)
        texts = [
            'Приветствую!',
            f'<b>Заданная таблица</b>: {sheet_id}',
            f'<b>Заданная группа</b>: {private_group}',
            f'<b>Сервисный аккаунт</b>: {SERVICE_ACCOUNT_EMAIL}',
        ]

    await msg.answer('\n'.join(texts), reply_markup=change_keyboard)
