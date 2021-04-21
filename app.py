from aiogram import executor
import handlers
import middlewares
from loader import dp

if __name__ == '__main__':
    handlers.setup()
    middlewares.setup()
    executor.start_polling(dp)
