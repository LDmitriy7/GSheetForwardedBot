import asyncio
import shelve

import gspread

from config import SHEET_RECORDS_KEY, GOOGLE_CREDS_FILE, SHEET_ID, POLL_SHEET_DELAY, PRIVATE_GROUP
from loader import bot

client = gspread.service_account(GOOGLE_CREDS_FILE)
SERVICE_ACCOUNT_EMAIL = client.auth.service_account_email
sheet = client.open_by_key(SHEET_ID)
ws = sheet.sheet1


def get_new_records():
    all_records = {tuple(row) for row in ws.get_all_values()[1:]}

    with shelve.open('shelve') as sh:
        old_records = sh.get(SHEET_RECORDS_KEY, set())
        new_records = all_records - old_records
        sh[SHEET_RECORDS_KEY] = all_records

    for record in new_records:
        yield record


def form_message(record: list):
    texts = [
        f'<b>Дата</b>: {record[0]}',
        f'<b>ФИО</b>: {record[1]}',
        f'<b>Должность</b>: {record[2]}',
        f'<b>Заведение</b>: {record[3]}',
        f'<b>Соцсеть</b>: {record[4]}',
        f'<b>E-mail</b>: {record[5]}',
        f'<b>Тел.</b>: {record[6]}',
    ]
    return '\n'.join(texts)


async def poll_sheets():
    while True:
        for record in get_new_records():
            await bot.send_message(PRIVATE_GROUP, form_message(record), disable_web_page_preview=True)

        await asyncio.sleep(POLL_SHEET_DELAY)
