from aiogram import Dispatcher
from aiogram_utils import middlewares
from .misc import AccessChecker


def setup(dp: Dispatcher):
    dp.setup_middleware(middlewares.AnswerAnyQuery())
    dp.setup_middleware(AccessChecker())
