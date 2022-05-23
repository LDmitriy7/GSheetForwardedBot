import os


def _get_env(key: str, default=None, required=False):
    value = os.getenv(key, default)
    if required and value is None:
        raise ValueError(f'You must set env ${key}')
    return value


class _Bot:

    @property
    def token(self) -> str:
        return _get_env('BOT_TOKEN', required=True)


bot = _Bot()


class _Database:

    @property
    def name(self) -> str:
        return _get_env('DATABASE_NAME', required=True)

    @property
    def host(self) -> str:
        return _get_env('DATABASE_HOST', required=True)


db = _Database()


class _Admins:

    @property
    def ids(self) -> list[int]:
        value = _get_env('ADMINS_IDS', required=True)
        return [int(i.strip()) for i in value.split(',')]


admins = _Admins()


class _Log:

    @property
    def file(self) -> str:
        value = _get_env('LOG_FILE', '.log')
        return value

    @property
    def level(self) -> int | None:
        value = _get_env('LOG_LEVEL', 30)
        return int(value)


log = _Log()
