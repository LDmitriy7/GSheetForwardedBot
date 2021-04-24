from aiogram import executor

import handlers
import middlewares
import utils
from loader import dp

if __name__ == '__main__':
    handlers.setup()
    middlewares.setup()
    utils.setup()
    executor.start_polling(dp)
