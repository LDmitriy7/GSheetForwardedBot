from utils.poll_sheets import poll_sheets
from loader import loop


def setup():
    loop.create_task(poll_sheets())
