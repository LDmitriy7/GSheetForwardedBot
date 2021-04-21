import asyncio
import shelve

import gspread

from config import SHEET_RECORDS_KEY, GOOGLE_CREDS_FILE, SHEET_ID, POLL_SHEET_DELAY
from loader import bot

client = gspread.service_account(GOOGLE_CREDS_FILE)
# print(client.auth.service_account_email)

sheet = client.open_by_key(SHEET_ID)
ws = sheet.sheet1


def get_new_records():
    headers = ws.row_values(1)
    all_records = {tuple(row) for row in ws.get_all_values()[1:]}

    with shelve.open('shelve') as sh:
        old_records = sh.get(SHEET_RECORDS_KEY, set())
        new_records = all_records - old_records
        sh[SHEET_RECORDS_KEY] = all_records

    for record in new_records:
        record_json = dict(zip(headers, record))
        yield record_json


async def poll_sheets():
    while True:
        for record in get_new_records():
            await bot.send_message(724477101, str(record), disable_web_page_preview=True)

        await asyncio.sleep(POLL_SHEET_DELAY)
