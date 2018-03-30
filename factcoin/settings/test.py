from .base import *
# settings used when run ./manage.py test

DATABASE_URL = None

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'factcoin_test',
    }
}

STATIC_URL = '/static/'
SERVE_STATIC_FILES = False
