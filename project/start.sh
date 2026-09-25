#!/bin/bash
# Dev server: Django runserver + Tailwind watcher (see Procfile.tailwind).
cd "$(dirname "$0")" || exit 1
source venv/bin/activate
python manage.py tailwind dev
