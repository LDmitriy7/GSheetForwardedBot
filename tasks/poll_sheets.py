import shelve

import gspread

import api
from config import GOOGLE_CREDS_FILE, POLL_SHEET_DELAY
from loader import tm, bot
from models import documents

client = gspread.service_account(GOOGLE_CREDS_FILE)


def get_new_records(sheet_id: str):
    sheet = client.open_by_key(sheet_id)
    ws = sheet.sheet1

    all_records = {tuple(row) for row in ws.get_all_values()[1:]}

    for record in all_records:
        r = {
            'date': record[0],
            'full_name': record[1],
            'position': record[2],
            'institution': record[3],
            'social': record[4],
            'email': record[5],
            'tel': record[6],
        }
        if not documents.Record.object(**r):
            yield documents.Record(**r).save()


def form_message(record: documents.Record):
    texts = [
        f'<b>Дата</b>: {record.date}',
        f'<b>ФИО</b>: {record.full_name}',
        f'<b>Должность</b>: {record.position}',
        f'<b>Заведение</b>: {record.institution}',
        f'<b>Соцсеть</b>: {record.social}',
        f'<b>E-mail</b>: {record.email}',
        f'<b>Тел.</b>: {record.tel}',
    ]
    return '\n'.join(texts)


@tm.forever(POLL_SHEET_DELAY)
async def poll_sheets():
    config = api.config.get()

    for record in get_new_records(config.sheet_id):
        await bot.send_message(config.group_to_forward_id, form_message(record))
