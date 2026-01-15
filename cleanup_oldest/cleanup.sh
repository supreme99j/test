#!/usr/bin/env bash

SCRIPT_NAME="$(basename "$0")"
SLEEP_SECONDS=86400  # 24 часа

while true; do
    mapfile -t FILES < <(
        find . -maxdepth 1 -type f ! -name "$SCRIPT_NAME" -printf "%T@ %p\n" | sort -n
    )

    if [ "${#FILES[@]}" -ge 3 ]; then
        OLDEST_FILE=$(echo "${FILES[0]}" | cut -d' ' -f2-)
        rm -f -- "$OLDEST_FILE"
        echo "$(date '+%F %T') Удалён файл: $OLDEST_FILE"
    fi

    sleep "$SLEEP_SECONDS"
done
