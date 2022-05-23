from aiogram import executor

from loader import dp


async def on_startup(_):
    import filters
    import handlers
    import middlewares
    import tasks

    filters.setup(dp)
    handlers.setup()
    middlewares.setup(dp)
    tasks.setup()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
