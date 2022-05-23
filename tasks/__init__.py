from loader import tm


def setup():
    from . import poll_sheets

    tm.create_tasks()
