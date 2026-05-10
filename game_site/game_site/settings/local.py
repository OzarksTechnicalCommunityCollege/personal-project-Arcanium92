from .base import *

SECRET_KEY = "django-insecure-(-!$az5r7*1xl%4)$8kar=hmv#d#3&fe)4o2^*@m(%+z5_8ct@"

DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}