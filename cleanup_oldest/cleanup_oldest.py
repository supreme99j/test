#!usrbinenv python3

#github.comsupreme99j/test/cleanup_oldest/cleanup_oldest.py

import os
import time

CHECK_INTERVAL = 3 #24  60  60  # 24h

def delete_oldest_file()
    current_dir = os.getcwd()
    script_name = os.path.basename(__file__)

    files = []

    for entry in os.listdir(current_dir)
        full_path = os.path.join(current_dir, entry)

        if not os.path.isfile(full_path)
            continue

        if entry == script_name
            continue

        try
            mtime = os.path.getmtime(full_path)
            files.append((mtime, full_path))
        except OSError
            continue

    if len(files)  3
        print(Файлов меньше 3 — удаление не требуется)
        return

    files.sort(key=lambda x x[0]) 
    oldest_file = files[0][1]

    try
        os.remove(oldest_file)
        print(fУдалён самый старый файл {oldest_file})
    except Exception as e
        print(fОшибка при удалении {oldest_file} {e})

def main()
    print(Скрипт запущен. Проверка раз в сутки.)
    while True
        delete_oldest_file()
        time.sleep(CHECK_INTERVAL)

if __name__ == __main__
    main()
