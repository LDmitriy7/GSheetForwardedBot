#!/usr/bin/env python3
"""
This script will daemonize your bot with systemd.
You must use it as Super User (sudo).

Copies project to /usr/local/bin/{bot_name}
You can specify own dirname and main_script_name with 2 arguments

By default:
 bot_name - $cwd_name
 main_script_name - app.py
"""

import os
import sys
import warnings

try:
    BOT_NAME = sys.argv[1]
except IndexError:
    BOT_NAME = os.getcwd().split('/')[-1]

try:
    MAIN_SCRIPT_NAME = sys.argv[2]
except IndexError:
    MAIN_SCRIPT_NAME = 'app.py'

UNIT_PATH = f'/etc/systemd/system/{BOT_NAME}.service'
NEW_PROJECT_DIR = f'/usr/local/bin/{BOT_NAME}'

UNIT_TEXT = f"""\
[Unit]
Description=TelegramBot: {BOT_NAME}
After=network.target

[Service]
Type=simple
WorkingDirectory={NEW_PROJECT_DIR}
ExecStart=python3 {NEW_PROJECT_DIR}/{MAIN_SCRIPT_NAME}
RestartSec=5
Restart=on-failure

[Install]
WantedBy=multi-user.target
"""

if os.path.exists('requirements.txt'):
    os.system('pip3 install -r requirements.txt')
else:
    warnings.warn("Can't find requirements.txt")

os.system(f'cp -r . {NEW_PROJECT_DIR}')
os.system(f'rm {NEW_PROJECT_DIR}/{__file__}')
os.system(f'echo "{UNIT_TEXT}" > {UNIT_PATH}')
os.system('systemctl daemon-reload')
os.system(f'systemctl enable {BOT_NAME}.service')
os.system(f'systemctl restart {BOT_NAME}.service')
os.system(f'systemctl status {BOT_NAME}')
