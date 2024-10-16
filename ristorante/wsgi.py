"""
WSGI config for ristorante project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ristorante.settings')

application = get_wsgi_application()
# Esegui le migrazioni all'avvio del server
try:
    call_command('migrate')
except Exception as e:
    print(f"Errore durante la migrazione: {e}")
