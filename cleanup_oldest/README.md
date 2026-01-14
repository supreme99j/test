chmod +x cleanup.py


crontab -e

Добавить строку (например, запуск каждый день в 03:00):
0 3 * * * /usr/bin/python3 /path/to/cleanup.py >> /tmp/cleanup.log 2>&1