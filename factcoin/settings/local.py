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

CORS_ORIGIN_ALLOW_ALL = True

ALLOWED_HOSTS = []
