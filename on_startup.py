import os

DEFAULT_ENV = {
    'BOT_TOKEN': '',
    'DATABASE_NAME': 'ForwarderBot',
    'DATABASE_HOST': 'mongo',
    'LOG_LEVEL': '20',
    'ADMINS_IDS': '724477101,433120468',
}

GUIDE_TEXT = """
You should set environment variables.
You can skip any variable, it will be taken from "[]"
"""

END_TEXT = """
Starting docker...
"""

FP = '.env'
CREDS_FILE = 'creds.json'


def extract_vars(text):
    _vars = {}

    for string in text.strip().split('\n'):
        key, value = string.split('=', maxsplit=1)
        _vars[key] = value

    return _vars


def dump_vars(_vars: dict):
    text = ''

    for key, value in _vars.items():
        text += f'{key}={value}\n'

    return text


print(GUIDE_TEXT)

try:
    file = open(FP, mode='r')
except FileNotFoundError:
    env = {}
else:
    env = extract_vars(file.read())

for k, v in DEFAULT_ENV.items():
    cur_v = env.get(k, v)
    new_v = input(f'${k} [{cur_v}]: ') or cur_v
    env[k] = new_v

file = open(FP, mode='w')
file.write(dump_vars(env))

print(END_TEXT)

if not os.path.exists(CREDS_FILE):
    raise ValueError(f'File {CREDS_FILE} not found!')
