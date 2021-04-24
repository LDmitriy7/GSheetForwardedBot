1) sudo apt update
2) sudo apt install python3 - установить python
3) sudo apt install python3-pip - установить менеджер пакетов
4) перейти в папку с ботом
5) python3 daemonizer.py -
    * скрипт установит зависимости проекта из requirements.txt
    * скопирует проект в /usr/local/bin
    * сделает скрипт бота юнитом systemd (фоновым процесом)
    * покажет статус юнита
    