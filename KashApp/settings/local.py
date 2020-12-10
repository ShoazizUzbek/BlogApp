from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'news',
        'USER': 'postgres',
        'PASSWORD': '99',
        'HOST': '127.0.0.1',
        'POST': '5432'
    }
}