#!/usr/bin/env python3
import os
import sys
import time

def main():
    current_dir = os.getcwd()
    script_name = os.path.basename(__file__)

    files = []

    for entry in os.listdir(current_dir):
        full_path = os.path.join(current_dir, entry)

        if not os.path.isfile(full_path):
            continue

        if entry == script_name:
            continue

        try:
            mtime = os.path.getmtime(full_path)
            files.append((mtime, full_path))
        except OSError:
            continue

    # Если файлов меньше 3 — ничего не делаем
    if len(files) < 3:
        return

    # Сортировка по дате изменения (старые — первыми)
    files.sort(key=lambda x: x[0])

    oldest_file = files[0][1]

    try:
        os.remove(oldest_file)
        print(f"Удалён файл: {oldest_file}")
    except Exception as e:
        print(f"Ошибка при удалении {oldest_file}: {e}")

if __name__ == "__main__":
    main()
