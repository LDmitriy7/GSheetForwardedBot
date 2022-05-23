import aiogram_utils
from aiogram import Dispatcher


def setup(dp: Dispatcher):
    aiogram_utils.filters.setup(dp)
