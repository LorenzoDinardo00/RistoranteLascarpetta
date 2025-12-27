#!/usr/bin/env bash
# Script di build per Render - eseguito automaticamente ad ogni deploy

set -o errexit

# Installa le dipendenze
pip install -r requirements.txt

# Raccoglie i file statici
python manage.py collectstatic --no-input

# Esegue le migrazioni del database
python manage.py migrate
