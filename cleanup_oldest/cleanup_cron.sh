#!/usr/bin/env bash

SCRIPT_NAME="$(basename "$0")"

mapfile -t FILES < <(
    find . -maxdepth 1 -type f ! -name "$SCRIPT_NAME" -printf "%T@ %p\n" | sort -n
)

if [ "${#FILES[@]}" -lt 3 ]; then
    exit 0
fi

OLDEST_FILE=$(echo "${FILES[0]}" | cut -d' ' -f2-)

rm -f -- "$OLDEST_FILE"

echo "Удалён файл: $OLDEST_FILE"