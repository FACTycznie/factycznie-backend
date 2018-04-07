from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': os.environ.get('POSTGRES_PORT_5432_TCP_ADDR', 'postgres'),  # name of db service in docker compose
        'PORT': os.environ.get('POSTGRES_PORT_5432_TCP_PORT', 5432),
    }
}

ALLOWED_HOSTS += ['factycznie.pl', 'www.factycznie.pl']
