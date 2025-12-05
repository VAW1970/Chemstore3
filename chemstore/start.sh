#!/usr/bin/env bash
set -e


# opcional: se usar env var para o sqlite, garante que o diretório exista
if [ -n "$SQLITE_PATH" ]; then
DIR=$(dirname "$SQLITE_PATH")
mkdir -p "$DIR"
fi


python manage.py migrate --noinput
python manage.py collectstatic --noinput


exec gunicorn myproject.wsgi --bind 0.0.0.0:$PORT --workers 3
